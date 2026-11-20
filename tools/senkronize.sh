#!/usr/bin/env bash
# ortak/ altındaki ana kopyaları aşama skill'lerinin references klasörlerine dağıtır.
# Kullanım:
#   tools/senkronize.sh            kopyalar
#   tools/senkronize.sh --kontrol  yalnız denetler; fark varsa 1 ile çıkar (CI için)
set -euo pipefail
KOK="$(cd "$(dirname "$0")/.." && pwd)"
KONTROL=0
[ "${1:-}" = "--kontrol" ] && KONTROL=1

# dosya:hedef skill'ler (boşlukla ayrılmış)
ESLEME=(
  "ortak_yonetim.md:ay-arastirma ay-analiz ay-yazim ay-hakem-teslim"
  "ortak_ajan.md:ay-arastirma ay-analiz ay-yazim ay-hakem-teslim"
  "atif_protokolu.md:ay-arastirma ay-yazim ay-hakem-teslim"
  "ajan_literatur_arama.md:ay-arastirma ay-yazim ay-hakem-teslim"
  "ajan_kaynak_dogrulama.md:ay-arastirma ay-yazim ay-hakem-teslim"
  "birlestir_literatur.py:ay-arastirma ay-yazim ay-hakem-teslim"
  "analiz_kontrol.md:ay-arastirma ay-analiz ay-yazim ay-hakem-teslim"
  "yazim_kurallari.md:ay-yazim ay-hakem-teslim"
  "uslup_tarama.py:ay-yazim ay-hakem-teslim"
  "ajan_uslup_duzeltici.md:ay-yazim ay-hakem-teslim"
  "ajan_bicimlendirme.md:ay-yazim ay-hakem-teslim"
)

FARK=0
for satir in "${ESLEME[@]}"; do
  dosya="${satir%%:*}"
  for skill in ${satir#*:}; do
    hedef="$KOK/plugins/akademik-yazim-ekibi/skills/$skill/references/$dosya"
    if [ "$KONTROL" -eq 1 ]; then
      if ! cmp -s "$KOK/ortak/$dosya" "$hedef"; then
        echo "FARKLI ya da EKSİK: plugins/akademik-yazim-ekibi/skills/$skill/references/$dosya"
        FARK=1
      fi
    else
      mkdir -p "$(dirname "$hedef")"
      cp "$KOK/ortak/$dosya" "$hedef"
    fi
  done
done

if [ "$KONTROL" -eq 1 ]; then
  [ "$FARK" -eq 0 ] && echo "Bütün kopyalar ortak/ ile aynı."
  exit "$FARK"
fi
echo "Senkronize edildi."
