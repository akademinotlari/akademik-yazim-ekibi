#!/usr/bin/env python3
"""Teslim öncesi mekanik tutarlılık denetimi.

Kullanım: python3 mekanik_kontrol.py <IS klasörü> [--cikti RAPOR]

Denetimler (dogrulama_listesi.md madde numaralarıyla):
  1-3  metindeki atıf anahtarları ile kaynaklar.bib iki yönlü eşleşmesi
  4    her bib anahtarının doğrulama kaydında DOĞRULANDI/DÜZELTİLDİ satırı
  10   Özet, Bulgular ve Sonuç'taki ondalıklı sayılar ve yüzdeler sayilar.csv'de (ya da matristeki temel_bulgu'da) var mı
  11   Özet ve Sonuç'taki ondalıklı sayılar Bulgular'da da geçiyor mu
  13   şekil ve tablo numaralarının ilk anılma sırası, yer tutucu öncesi anılma, dosya varlığı
  16   bölüm bazında kelime sayıları
Yalnız işaretler; düzeltmez.
"""
import csv
import glob
import os
import re
import sys

BOLUMLER = ["0_ozet.md", "1_giris.md", "2_yontem.md", "3_bulgular.md", "4_tartisma.md", "5_sonuc.md"]
ATIF = re.compile(r"\[@([^\]]+)\]")
SAYI = re.compile(r"(?<![\w.,])(\d+[.,]\d+)(\s?%)?")
ANMA = re.compile(r"\b(Şekil|Figure|Fig\.|Tablo|Table)\s+(\d+)")
YER = re.compile(r"^\[(ŞEKİL|TABLO)\s+(\d+):\s*([^\]]+)\]")


def oku(yol):
    return open(yol, encoding="utf-8").read() if os.path.exists(yol) else ""


def sayiya(t):
    return float(t.replace(",", "."))


def ondalik(t):
    return len(re.split(r"[.,]", t)[1])


def main():
    argv = sys.argv[1:]
    cikti = None
    if "--cikti" in argv:
        i = argv.index("--cikti")
        cikti = argv[i + 1]
        del argv[i:i + 2]
    if len(argv) != 1:
        sys.exit(__doc__)
    IS = argv[0]
    t = os.path.join(IS, "05_taslak")
    metin = {b: oku(os.path.join(t, b)) for b in BOLUMLER}
    rapor = ["# Mekanik kontrol raporu", ""]

    # 1-3 atıflar
    atiflar = set()
    for m in ATIF.finditer("\n".join(metin.values())):
        for k in re.split(r"[;,]\s*@?", m.group(1)):
            atiflar.add(k.strip().lstrip("@"))
    bib = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", oku(os.path.join(IS, "kaynaklar.bib"))))
    eksik_bib = sorted(atiflar - bib)
    kullanilmayan = sorted(bib - atiflar)
    rapor += [f"Madde 1: metinde {len(atiflar)} tekil atıf anahtarı.",
              f"Madde 2: {'GEÇTİ' if not eksik_bib else 'BAŞARISIZ'} | kaynakçada olmayan: {', '.join(eksik_bib) or 'yok'}",
              f"Madde 3: {'GEÇTİ' if not kullanilmayan else 'BAŞARISIZ'} | metinde anılmayan: {', '.join(kullanilmayan) or 'yok'}"]

    # 4 doğrulama kaydı
    dogrulanan = set()
    kayit = os.path.join(IS, "02_dogrulama_kaydi.csv")
    if os.path.exists(kayit):
        for r in csv.DictReader(open(kayit, encoding="utf-8")):
            if r.get("durum", "").strip() in ("DOĞRULANDI", "DÜZELTİLDİ"):
                dogrulanan.add(r.get("anahtar", "").strip())
    kayitsiz = sorted(bib - dogrulanan)
    rapor.append(f"Madde 4: {'GEÇTİ' if not kayitsiz else 'BAŞARISIZ'} | doğrulama kaydı olmayan: {', '.join(kayitsiz) or 'yok'}")

    # 10-11 sayılar
    degerler = []
    sy = os.path.join(IS, "04_analiz", "sayilar.csv")
    if os.path.exists(sy):
        for r in csv.DictReader(open(sy, encoding="utf-8")):
            try:
                degerler.append((r["id"], float(r["deger"])))
            except (KeyError, ValueError):
                pass
    lit = ""
    mat = os.path.join(IS, "02_literatur_matrisi.csv")
    if os.path.exists(mat):
        lit = " ".join(r.get("temel_bulgu", "") for r in csv.DictReader(open(mat, encoding="utf-8")))

    def bulunur(tok, yuzde):
        x, d = sayiya(tok), ondalik(tok)
        for _, v in degerler:
            for aday in (v, v * 100):
                if round(aday, d) == round(x, d):
                    return True
        return tok in lit or tok.replace(",", ".") in lit

    eslesmeyen = []
    for b in ("0_ozet.md", "3_bulgular.md", "5_sonuc.md"):
        for no, satir in enumerate(metin[b].split("\n"), 1):
            if satir.startswith("[ŞEKİL") or satir.startswith("[TABLO"):
                continue
            for m in SAYI.finditer(ATIF.sub("", satir)):
                if not bulunur(m.group(1), bool(m.group(2))):
                    eslesmeyen.append(f"{b}:{no} {m.group(0).strip()}")
    rapor.append(f"Madde 10: {'GEÇTİ' if not eslesmeyen else 'BAŞARISIZ'} | sayilar.csv ya da matriste bulunmayan {len(eslesmeyen)} sayı")
    rapor += [f"  {e}" for e in eslesmeyen]
    bulgular_sayilari = {sayiya(m.group(1)) for m in SAYI.finditer(metin["3_bulgular.md"])}
    ozet_fark = []
    for b in ("0_ozet.md", "5_sonuc.md"):
        for m in SAYI.finditer(ATIF.sub("", metin[b])):
            if sayiya(m.group(1)) not in bulgular_sayilari:
                ozet_fark.append(f"{b}: {m.group(0).strip()}")
    rapor.append(f"Madde 11: {'GEÇTİ' if not ozet_fark else 'BAŞARISIZ'} | Bulgular'da geçmeyen {len(ozet_fark)} sayı")
    rapor += [f"  {e}" for e in ozet_fark]

    # 13 şekil ve tablo numaraları
    sorunlar = []
    ilk_anma = {"ŞEKİL": [], "TABLO": []}
    anilan = {"ŞEKİL": set(), "TABLO": set()}
    yerler = {"ŞEKİL": set(), "TABLO": set()}
    for b in BOLUMLER[1:]:
        for no, satir in enumerate(metin[b].split("\n"), 1):
            y = YER.match(satir.strip())
            if y:
                tur, n, yol = y.group(1), int(y.group(2)), y.group(3).strip()
                yerler[tur].add(n)
                if n not in anilan[tur]:
                    sorunlar.append(f"{b}:{no} {tur} {n} yer tutucusundan önce metinde anılmamış")
                if not os.path.exists(os.path.join(IS, yol)):
                    sorunlar.append(f"{b}:{no} {tur} {n} dosyası yok: {yol}")
                continue
            for m in ANMA.finditer(satir):
                tur = "ŞEKİL" if m.group(1) in ("Şekil", "Figure", "Fig.") else "TABLO"
                n = int(m.group(2))
                if n not in anilan[tur]:
                    anilan[tur].add(n)
                    ilk_anma[tur].append(n)
    for tur in ("ŞEKİL", "TABLO"):
        if ilk_anma[tur] != list(range(1, len(ilk_anma[tur]) + 1)):
            sorunlar.append(f"{tur} ilk anılma sırası ardışık değil: {ilk_anma[tur]}")
        for n in sorted(anilan[tur] - yerler[tur]):
            sorunlar.append(f"{tur} {n} anılmış ama yer tutucusu ya da dosyası yok")
    rapor.append(f"Madde 13: {'GEÇTİ' if not sorunlar else 'BAŞARISIZ'}")
    rapor += [f"  {s}" for s in sorunlar]

    # 16 kelime sayıları
    rapor.append("Madde 16 (kelime sayıları, sınırla karşılaştırmayı Doğrulayıcı yapar):")
    toplam = 0
    for b in BOLUMLER:
        n = len(re.sub(r"\[[^\]]*\]", "", metin[b]).split())
        toplam += n if b != "0_ozet.md" else 0
        rapor.append(f"  {b}: {n}")
    rapor.append(f"  ana metin (özet hariç): {toplam}")

    sonuc = "\n".join(rapor) + "\n"
    if cikti:
        open(cikti, "w", encoding="utf-8").write(sonuc)
        print("\n".join(l for l in rapor if l.startswith("Madde")))
    else:
        print(sonuc)


if __name__ == "__main__":
    main()
