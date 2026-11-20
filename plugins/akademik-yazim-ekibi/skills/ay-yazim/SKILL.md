---
name: ay-yazim
description: Kullanıcının akademik yazım ekibinin 3. aşaması. Analiz bulguları onaylandıktan (G3) sonra makale, bildiri, kitap bölümü ya da proje metninin bölüm bölüm yazılması, üslup denetimi, kapak mektubu, highlights, başlık sayfası gibi eklerin ve dergi biçiminin hazırlanması gerektiğinde ya da devir paketindeki durum.md "Sıradaki skill: ay-yazim" dediğinde kullan.
---

# Akademik yazım ekibi, 3. aşama: Yazım ve teslim hazırlığı (Aşama 5-6)

Sen ana oturumsun. Taslak bölümleri okumazsın; yazımı ajanlar yapar, üslup taramasını betik yapar. Bu aşamada ana oturum için Sonnet yeterlidir.

## Başlangıç

1. `$SKILL_DIR/references/ortak_yonetim.md` dosyasını oku.
2. ortak_yonetim.md Bölüm 3'ü uygula. Önkoşul: `04_analiz/ozet.md` var ve durum.md'de G3 onaylı. Değilse dur.
3. Görev listesi: kelime hedefleri, Yazım 1, Yazım 2, Yazım 3, üslup taraması ve düzeltme, yazım notlarını kapatma, ek metinler, biçimlendirme, devir.

## Aşama 5: Yazım

1. Kelime hedeflerini yazim_kurallari.md'deki "Kelime hedefleri" kuralıyla hesapla ve `05_taslak/plan.md` dosyasına bölüm başına aralık olarak yaz. Brief'teki iskelet (03_bosluk_yontem.md başlık 7) bölüm adlarını belirler.
2. Yazım Ajanı üç ardışık çağrıyla (opus; ajan_yazim.md). Her çağrı bir öncekinin bitmesini bekler.
   - Çağrı 1: KIP=TAM, BOLUMLER="2_yontem.md, 3_bulgular.md".
   - Çağrı 2: KIP=TAM, BOLUMLER="5_sonuc.md, 4_tartisma.md".
   - Çağrı 3: KIP=TAM, BOLUMLER="1_giris.md, 0_ozet.md".
   Ortak değişkenler: IS; DIL = brief'teki ana_dil.
   Çıktı türü proje ise tek fark: KIP=PROJE ve bölüm dosyaları sablonlar.md 12.5 iskeletine göre adlandırılır (Yazım Ajanı dosya adlarını kendisi belirler); çağrı 1 Yöntem, İş Paketleri, Risk; çağrı 2 Yaygın Etki, Bütçe gerekçesi; çağrı 3 Amaç ve Hedefler, Özgün Değer, Özet. Kitap bölümünde bölüm adları yayınevi şablonuna göre değişir, yazım sırası korunur.
3. Üslup taraması (betik, ajan yok):
```bash
cd "$IS" && python3 _kurallar/uslup_tarama.py --cikti 05_taslak/uslup_raporu.md 05_taslak/[0-5]_*.md
```
   Ekrandaki iki satırı (toplam ve kod sayıları) oku. Toplam 0 değilse Üslup Düzeltici (sonnet; ajan_uslup_duzeltici.md) çağrılır: RAPOR=05_taslak/uslup_raporu.md, DOSYALAR=05_taslak/[0-5]_*.md dosyalarının listesi. Ardından tarama bir kez daha çalışır; kalan bulgular açık sorun olarak durum.md'ye yazılır.
4. Yazım notlarını kapatma. `grep -c '^\[LİTERATÜR\]\|^\[ANALİZ\]' "$IS/05_taslak/yazim_notlari.md"` ile not sayısını al.
   - [LİTERATÜR] notları varsa: notları `05_taslak/iddialar.md` dosyasına numaralı olarak kopyala (`grep '^\[LİTERATÜR\]'`). Literatür Arama (sonnet) KIP=HEDEFLI, ALT_KONU=hedefli, HEDEF_ADAY=iddia sayısı × 2, YIL_BAS=bu yıl eksi 15, YIL_BIT=bu yıl, CIKTI=02_aday_hedefli.csv, IDDIA_DOSYASI=<iş klasörünün mutlak yolu>/05_taslak/iddialar.md, KULLANICI_DOSYALARI=yok. Ardından Kaynak Doğrulama (haiku) ADAY=02_aday_hedefli.csv, PARCA=02_parca_hedefli.csv, BIB=kaynaklar_hedefli.bib, KAYIT=02_dogrulama_kaydi_hedefli.csv. Ardından `python3 _kurallar/birlestir_literatur.py "$IS"`.
   - [ANALİZ] notlarını ana oturum okur (yalnız bu satırları, grep ile). Metin ile sayilar.csv çelişiyorsa sayilar.csv doğrudur ve metin düzeltilir. Yeni analiz gerekiyorsa etkileşimli kipte kullanıcıya sorulur; otomatik kipte iddia metinden çıkarılır, sınırlılık olarak yazılır ve kararlar.md'ye kaydedilir.
   - Sonra Yazım Ajanı (sonnet) KIP=NOT_KAPAT, BOLUMLER=notların geçtiği dosyalar: her notu ya bulunan kaynakla destekler ya da iddiayı metinden çıkarır.

Çıkış ölçütü: altı bölüm dosyası var; ikinci taramada KAPANIS, EM_DASH, KALIN, YAPAY_SOZCUK bulgusu yok; yazim_notlari.md'de kapatılmamış not yok.

## Aşama 6: Şablon ve ekler

1. Ek Metin Ajanı (sonnet; ajan_ek_metin.md). Değişkenler: IS; CIKTI_TURU = brief'teki çıktı türü.
   Çıktı türüne göre üretilecekler:
   - Makale: kapak mektubu, highlights, başlık sayfası, beyanlar.
   - Bildiri: bildiri özeti (kongre sınırında) ve sunum planı.
   - Kitap bölümü: başlık sayfası ve yazar biyografisi (yayınevi istiyorsa).
   - Proje: proje özeti ve bütçe gerekçesi tablosu (tutarlar "[YAZAR DOLDURACAK]").
2. Üslup taraması ek metinler için de çalışır: `python3 _kurallar/uslup_tarama.py --cikti 05_taslak/ekler/uslup_raporu.md 05_taslak/ekler/*.md`; bulgu varsa Üslup Düzeltici bir kez.
3. Çıktı türü proje ise ve proje değerlendirme ya da panel denetimi için kurulu bir skill varsa, etkileşimli kipte kullanıcıya onunla denetim yapmayı öner. Otomatik kipte yapılmaz.
4. Biçimlendirme Ajanı (sonnet; ajan_bicimlendirme.md). KIP=TAM, DEGISEN=yok, SABLON=brief'teki şablon yolu ya da "yok".

Çıkış ölçütü: 07_teslim altında ana_metin.docx ve çıktı türünün ek dosyaları var.

Bu aşamanın sonunda kapı yoktur. Hakem sürecinde metin değişirse biçimlendirme ay-hakem-teslim'de yalnız değişen dosyalar için yeniden çalışır.

## Devir

ortak_yonetim.md Bölüm 10. durum.md: "Sıradaki skill: ay-hakem-teslim". Gönderilecekler: devir zip'i ve 07_teslim/ana_metin.docx (kullanıcı ara taslağı görmek isterse).

## Bu aşamanın hata durumları

H11. Kelime sınırı aşılıyor. Yazım Ajanı 9. adımda kendisi denetler. Aşım sürerse ana oturum `wc -w` ile bölüm başına sayıyı alır ve Yazım Ajanını (sonnet, KIP=TAM, BOLUMLER=yalnız aşan bölüm) şu EK BAĞLAM'la bir kez çağırır: "<bölüm> dosyasından <n> kelime kısalt. Sıra: Giriş'teki genel bağlam, Yöntem'deki işleyiş açıklamalarının uzunluğu (tanım ve uygulama korunur), Tartışma'daki yinelemeler. Bulgulardaki sayılar ve sınırlılıklar kısaltılmaz; gereken ayrıntı 05_taslak/ekler/ek_dosya.md'ye taşınır."

H10. Şablon ya da dergi yazım kuralı bulunamıyor. Derginin yazar rehberi WebFetch ile okunur. Ulaşılamazsa ajan_bicimlendirme.md'deki varsayılan biçim ve APA 7 kullanılır; G4 özetinde "dergi biçimi doğrulanamadı" yazılır.

## Çağrı tavanları (normal / ekonomik)

Yazım (TAM) 3; Üslup Düzeltici en çok 2; not kapatma için Literatür Arama 1, Kaynak Doğrulama 1, Yazım (NOT_KAPAT) 1; H11 için Yazım 1; Ek Metin 1; Biçimlendirme 1.
