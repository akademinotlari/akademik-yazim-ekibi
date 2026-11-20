#!/usr/bin/env bash
# Repoyu denetler ve dist/ altına iki tür paket üretir:
#   dist/akademik-yazim-ekibi-plugin.zip   claude.ai > Customize > Plugins > Upload plugin için
#   dist/skills/<skill>.zip                skill'leri tek tek yüklemek isteyenler için
# GitHub'dan marketplace olarak eklemek için paket gerekmez; bu betik yine de denetim için çalıştırılır.
set -euo pipefail
KOK="$(cd "$(dirname "$0")/.." && pwd)"
PLUGIN="$KOK/plugins/akademik-yazim-ekibi"
"$KOK/tools/senkronize.sh"

# Manifestler geçerli JSON mu, adlar tutarlı mı
python3 - "$KOK" <<'EOF'
import json, sys, os
kok = sys.argv[1]
m = json.load(open(os.path.join(kok, ".claude-plugin/marketplace.json"), encoding="utf-8"))
for alan in ("name", "owner", "plugins"):
    assert alan in m, f"marketplace.json: {alan} eksik"
for e in m["plugins"]:
    yol = os.path.normpath(os.path.join(kok, e["source"]))
    assert ".." not in e["source"], f"marketplace.json: {e['source']} '..' içeriyor"
    p = json.load(open(os.path.join(yol, ".claude-plugin/plugin.json"), encoding="utf-8"))
    assert p["name"] == e["name"], f"plugin.json adı ({p['name']}) marketplace girdisiyle ({e['name']}) aynı değil"
print("Manifestler geçerli.")
EOF

rm -rf "$KOK/dist" && mkdir -p "$KOK/dist/skills"
for dizin in "$PLUGIN"/skills/*/; do
  ad="$(basename "$dizin")"
  skill="$dizin/SKILL.md"
  head -1 "$skill" | grep -qx -- '---' || { echo "HATA: $ad/SKILL.md frontmatter ile başlamıyor"; exit 1; }
  grep -q "^name: $ad\$" "$skill" || { echo "HATA: $ad/SKILL.md içindeki name alanı klasör adıyla aynı değil"; exit 1; }
  if [ -d "$dizin/references" ] && [ "$ad" != human ]; then
    # ortak_yonetim.md bütün ajanları listeleyen genel tabloyu içerdiği için denetim dışıdır
    kaynaklar=("$skill")
    for f in "$dizin"references/*; do [ "$(basename "$f")" != ortak_yonetim.md ] && kaynaklar+=("$f"); done
    for ref in $(grep -ohE '[a-z_]+\.(md|py)' "${kaynaklar[@]}" 2>/dev/null | sort -u); do
      case "$ref" in
        ajan_*|ortak_*|atif_protokolu.md|analiz_kontrol.md|yazim_kurallari.md|sablonlar.md|hakem_olcutleri.md|dogrulama_listesi.md|birlestir_literatur.py|uslup_tarama.py|mekanik_kontrol.py)
          [ -f "$dizin/references/$ref" ] || { echo "HATA: $ad içinde anılan references/$ref yok"; exit 1; } ;;
      esac
    done
  fi
  (cd "$PLUGIN/skills" && zip -qr "$KOK/dist/skills/$ad.zip" "$ad" -x '*/__pycache__/*' '*.pyc')
done
(cd "$KOK/plugins" && zip -qr "$KOK/dist/akademik-yazim-ekibi-plugin.zip" akademik-yazim-ekibi -x '*/__pycache__/*' '*.pyc')
ls -1 "$KOK/dist" "$KOK/dist/skills"
