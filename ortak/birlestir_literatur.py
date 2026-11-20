#!/usr/bin/env python3
"""Doğrulanmış literatür parçalarını matrise, kaynakçaya ve doğrulama kaydına birleştirir.

Kullanım: python3 birlestir_literatur.py <IS klasörü>

Girdi: 02_literatur_matrisi.csv (varsa), 02_parca_<alt>.csv, kaynaklar.bib (varsa),
kaynaklar_<alt>.bib, 02_dogrulama_kaydi_<alt>.csv.
Çıktı: 02_literatur_matrisi.csv, kaynaklar.bib, 02_dogrulama_kaydi.csv (üzerine yazar).
Yalnız DOĞRULANDI ve DÜZELTİLDİ satırları alınır. Aynı DOI bir kez alınır.
Aynı anahtar farklı DOI ile gelirse sonuna b, c, ... eklenir.
Parça dosyaları silinmez.
"""
import csv
import glob
import os
import re
import sys

KABUL = {"DOĞRULANDI", "DÜZELTİLDİ"}
MATRIS_BASLIK = ["anahtar", "yazarlar", "yil", "baslik", "dergi", "doi", "tur", "yontem", "veri",
                 "temel_bulgu", "sinirlilik", "alt_konu", "kanit_duzeyi", "dogrulama_durumu", "not"]


def bib_oku(yol):
    """[(anahtar, doi, kayıt metni)] listesi döndürür."""
    kayitlar = []
    if not os.path.exists(yol):
        return kayitlar
    metin = open(yol, encoding="utf-8").read()
    for parca in re.split(r"\n(?=\s*@)", metin):
        m = re.match(r"\s*@\w+\s*\{\s*([^,\s]+)\s*,", parca)
        if m:
            d = re.search(r"\bdoi\s*=\s*[{\"]([^}\"]+)", parca, re.I)
            kayitlar.append((m.group(1), norm_doi(d.group(1)) if d else "", parca.strip()))
    return kayitlar


def bib_bul(kayitlar, anahtar, doi):
    """Önce DOI ile, DOI yoksa anahtarla eşleşen kaydı bulur."""
    if doi:
        for k, d, metin in kayitlar:
            if d == doi:
                return k, metin
    for k, d, metin in kayitlar:
        if k == anahtar and (not doi or not d):
            return k, metin
    return None, None


def anahtar_degistir(kayit, eski, yeni):
    return re.sub(r"(@\w+\s*\{\s*)" + re.escape(eski) + r"(\s*,)", r"\g<1>" + yeni + r"\g<2>", kayit, count=1)


def norm_doi(d):
    d = (d or "").strip().lower()
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", d)


def main():
    if len(sys.argv) != 2:
        sys.exit("Kullanım: python3 birlestir_literatur.py <IS klasörü>")
    os.chdir(sys.argv[1])

    satirlar, bib, dois, anahtarlar = [], {}, {}, set()
    eklenen = yinelenen = yeniden_adlandirilan = bibsiz = 0

    kaynaklar = []
    if os.path.exists("02_literatur_matrisi.csv"):
        kaynaklar.append(("02_literatur_matrisi.csv", "kaynaklar.bib"))
    for f in sorted(glob.glob("02_parca_*.csv")):
        alt = f[len("02_parca_"):-len(".csv")]
        kaynaklar.append((f, f"kaynaklar_{alt}.bib"))

    for csv_yol, bib_yol in kaynaklar:
        parca_bib = bib_oku(bib_yol)
        for r in csv.DictReader(open(csv_yol, encoding="utf-8")):
            if r.get("dogrulama_durumu", "").strip() not in KABUL:
                continue
            doi = norm_doi(r.get("doi"))
            d = doi or (r.get("baslik", "").strip().lower())
            if not d:
                continue
            if d in dois:
                yinelenen += 1
                continue
            k = r.get("anahtar", "").strip()
            bib_anahtar, kayit = bib_bul(parca_bib, k, doi)
            if kayit is None:
                bibsiz += 1
                print(f"UYARI: {csv_yol} içindeki {k} için bib kaydı yok, alınmadı.")
                continue
            yeni = k
            ek = ord("b")
            while yeni in anahtarlar:
                yeni = k + chr(ek)
                ek += 1
            if yeni != bib_anahtar:
                kayit = anahtar_degistir(kayit, bib_anahtar, yeni)
            if yeni != k:
                yeniden_adlandirilan += 1
            r["anahtar"] = yeni
            anahtarlar.add(yeni)
            dois[d] = yeni
            bib[yeni] = kayit
            satirlar.append({b: r.get(b, "") for b in MATRIS_BASLIK})
            if csv_yol != "02_literatur_matrisi.csv":
                eklenen += 1

    with open("02_literatur_matrisi.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=MATRIS_BASLIK)
        w.writeheader()
        w.writerows(satirlar)
    with open("kaynaklar.bib", "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(bib[k] for k in sorted(bib)) + "\n")

    kayit_satirlari, baslik, gorulen = [], None, set()
    for f in ["02_dogrulama_kaydi.csv"] + sorted(glob.glob("02_dogrulama_kaydi_*.csv")):
        if not os.path.exists(f):
            continue
        for r in csv.DictReader(open(f, encoding="utf-8")):
            baslik = baslik or list(r.keys())
            d = norm_doi(r.get("doi_ya_da_adres"))
            if d in dois:
                r["anahtar"] = dois[d]
            anahtar = (r.get("anahtar", ""), d)
            if anahtar in gorulen:
                continue
            gorulen.add(anahtar)
            kayit_satirlari.append(r)
    if baslik:
        with open("02_dogrulama_kaydi.csv", "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=baslik)
            w.writeheader()
            w.writerows(kayit_satirlari)

    print(f"Matris: {len(satirlar)} doğrulanmış kaynak (bu birleştirmede eklenen {eklenen}, "
          f"yinelenen DOI {yinelenen}, yeniden adlandırılan anahtar {yeniden_adlandirilan}, bib kaydı olmayan {bibsiz}).")
    print(f"Doğrulama kaydı: {len(kayit_satirlari)} satır.")


if __name__ == "__main__":
    main()
