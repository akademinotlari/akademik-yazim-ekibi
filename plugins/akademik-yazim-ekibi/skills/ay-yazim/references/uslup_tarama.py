#!/usr/bin/env python3
"""Taslak metinlerde yapay zekâ yazım kalıplarını ve yasak üslup öğelerini tarar.

Kullanım: python3 uslup_tarama.py [--son] [--cikti RAPOR] DOSYA [DOSYA ...]
  --son     teslim öncesi tarama: yer tutucuları da raporlar
  --cikti   raporu dosyaya yazar (yoksa ekrana)

Rapor satırı: <dosya>:<satır> | <KOD> | <eşleşen metin>
Betik yalnız işaretler; düzeltmez. Kodların anlamı ajan_uslup_duzeltici.md içindedir.
"""
import re
import sys
from collections import Counter

HARF = r"[\wçğıöşüÇĞİÖŞÜâîû'-]"

KURALLAR = [
    ("EM_DASH", re.compile("—")),
    ("EN_DASH_ARALIK", re.compile(r"\d\s?–\s?\d")),
    ("KALIN", re.compile(r"\*\*")),
    ("KIVRIK_TIRNAK", re.compile("[“”‘’]")),
    ("KAPANIS", re.compile(r"(?:^|(?<=[.!?]\s))(Sonuç olarak|Özetle|Kısacası|Sonuç itibarıyla|Toparlamak gerekirse|"
                           r"In conclusion|To sum up|In summary|To conclude|Overall,)", re.I)),
    ("YONLENDIRME", re.compile(r"(ele alınacaktır|incelenecektir|sunulacaktır|bu bölümde|aşağıda sunulmuştur|"
                               r"this section (presents|describes|discusses)|in this section|"
                               r"(the )?(remainder|rest) of (this|the) paper|this paper is organi[sz]ed|let us|let's)", re.I)),
    ("YAPAY_SOZCUK", re.compile(r"\b(delve[sd]?|delving|crucial|pivotal|tapestry|landscape|underscore[sd]?|foster(s|ed|ing)?|"
                                r"showcase[sd]?|intricate|garner(s|ed)?|interplay|testament|vibrant|seamless(ly)?|"
                                r"groundbreaking|game-changer|paradigm shift|"
                                r"kritik öneme sahip|kritik bir rol|kritik rol|dönüm noktası|hayati öneme|"
                                r"büyük önem taşı\w*|son derece önemli)\b", re.I)),
    ("CALQUE", re.compile(r"(derinlemesine incele\w*|ışık tut\w*|kilit rol\w*|manzara\w*|yolculu\w*|"
                          r"önemli bir rol oyna\w*)", re.I)),
    ("DOLGU", re.compile(r"(şunu belirtmek gerekir|belirtmek gerekir ki|belirtmekte fayda var|"
                         r"it is important to note|it is worth noting|it should be noted|needless to say)", re.I)),
    ("SAPKA", re.compile(r"\b(lâzım|ilân\w*|lâkin|plân\w*|kâtip)\b", re.I)),
]

YER_TUTUCU = re.compile(r"(\[@|\[ŞEKİL|\[TABLO|\{[A-Z_]+\}|TODO|YAZAR DOLDURACAK)")
MAKTADIR = re.compile(r"(maktadır|mektedir|maktadırlar|mektedirler)[.!?]?$")
DI_GECMIS = re.compile(r"\b" + HARF + r"{3,}(?:[dt][ıiuü])(?:lar|ler)?[.!?]?$")
MISTIR = re.compile(r"m[ıiuü]şt[ıiuü]r(?:lar|ler)?[.!?]?$|d[ıiuü]r[.!?]?$")
UCLU = re.compile(r"(?:" + HARF + r"+(?: " + HARF + r"+){0,3}), (?:" + HARF + r"+(?: " + HARF + r"+){0,3}),? "
                  r"(?:ve|veya|ya da|and|or) " + HARF + r"+")
ACILIS = re.compile(r"^(Bu bağlamda|Bununla birlikte|Ayrıca|Bunun yanı sıra|Öte yandan|Moreover|Furthermore|Additionally)\b")
BU_VIRGUL = re.compile(r"(?:^|(?<=[.!?]\s))Bu, ")
CUMLE = re.compile(r"(?<=[.!?])\s+")


def turkce_mi(metin):
    return sum(metin.count(c) for c in "ğışçöüİĞŞ") > len(metin) / 200


def tara(yol, son):
    bulgular = []
    satirlar = open(yol, encoding="utf-8").read().split("\n")
    tr = turkce_mi("\n".join(satirlar))
    acilis_satirlari = []
    zincir = []
    for no, satir in enumerate(satirlar, 1):
        s = satir.strip()
        if not s or s.startswith("#") or s.startswith("[ŞEKİL") or s.startswith("[TABLO"):
            zincir = []
            continue
        for kod, desen in KURALLAR:
            for m in desen.finditer(s):
                bulgular.append((no, kod, m.group(0)))
        if son:
            for m in YER_TUTUCU.finditer(s):
                bulgular.append((no, "YER_TUTUCU", m.group(0)))
        if len(UCLU.findall(s)) >= 2:
            bulgular.append((no, "UCLU", "; ".join(UCLU.findall(s)[:2])))
        if ACILIS.match(s):
            acilis_satirlari.append((no, ACILIS.match(s).group(0)))
        if tr:
            for m in BU_VIRGUL.finditer(s):
                bulgular.append((no, "BU_VIRGUL", "Bu,"))
            for cumle in CUMLE.split(s):
                c = cumle.strip()
                if not c:
                    continue
                son_kelime = c.split()[-1]
                if MAKTADIR.search(c):
                    zincir.append((no, son_kelime))
                    if len(zincir) == 3:
                        bulgular.append((zincir[0][0], "MAKTADIR_ZINCIR", ", ".join(k for _, k in zincir)))
                else:
                    zincir = []
                if DI_GECMIS.search(son_kelime) and not MISTIR.search(son_kelime):
                    bulgular.append((no, "DI_GECMIS", son_kelime))
    if len(acilis_satirlari) >= 3:
        for no, ifade in acilis_satirlari:
            bulgular.append((no, "PARAGRAF_ACILIS", ifade))
    return bulgular


def main():
    argv = sys.argv[1:]
    son = "--son" in argv
    cikti = None
    if "--cikti" in argv:
        i = argv.index("--cikti")
        cikti = argv[i + 1]
        del argv[i:i + 2]
    dosyalar = [a for a in argv if a != "--son"]
    if not dosyalar:
        sys.exit(__doc__)
    tum = []
    for d in dosyalar:
        tum += [(d, no, kod, eslesme) for no, kod, eslesme in tara(d, son)]
    sayim = Counter(k for _, _, k, _ in tum)
    rapor = ["# Üslup tarama raporu", "",
             f"Toplam bulgu: {len(tum)}",
             "Kod sayıları: " + (", ".join(f"{k}={v}" for k, v in sorted(sayim.items())) or "yok"), "",
             "## Bulgular", ""]
    rapor += [f"{d}:{no} | {kod} | {eslesme}" for d, no, kod, eslesme in tum]
    metin = "\n".join(rapor) + "\n"
    if cikti:
        open(cikti, "w", encoding="utf-8").write(metin)
        print(rapor[2])
        print(rapor[3])
    else:
        print(metin)


if __name__ == "__main__":
    main()
