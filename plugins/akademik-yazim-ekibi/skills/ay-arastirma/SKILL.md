---
name: ay-arastirma
description: Kullanıcının akademik yazım ekibinin 1. aşaması. Yeni bir makale, bildiri, kitap bölümü ya da proje için konu verildiğinde; brief, literatür taraması, araştırma sorusu seçimi ya da boşluk-yöntem-analiz planı (G1, G2) gerektiğinde ya da devir paketindeki durum.md "Sıradaki skill: ay-arastirma" dediğinde kullan.
---

# Akademik yazım ekibi, 1. aşama: Araştırma tasarımı (Aşama 0-3)

Sen ana oturumsun: yönetir, karar verir, ajan çağırırsın. Arama, doğrulama ve soru üretimini ajanlar yapar. Bu aşamanın çıktısı onaylı bir 03_bosluk_yontem.md dosyası ve doğrulanmış literatür matrisidir.

## Başlangıç

1. `$SKILL_DIR/references/ortak_yonetim.md` dosyasını oku. Oradaki kurallar bu skill'in parçasıdır.
2. ortak_yonetim.md Bölüm 3'teki aşama başlangıcını uygula. Önkoşul yok; iş klasörü yoksa Aşama 0'da açılır.
3. Görev listesini kur: Aşama 0, Aşama 1, G1, Aşama 2, Aşama 3, G2, devir.

## Aşama 0: Brief

Kullanıcıdan şu bilgileri al; eksik olanları tek mesajda sor:
konu; bilim alanı (örnek: ulaştırma mühendisliği); varsa alan sınırı (örnek: yalnız karayolu); yazarın uzmanlık alanları ve kullandığı yöntemler (araştırma sorusu seçiminde puanlanır); çıktı türü (makale, bildiri, kitap bölümü, proje); ana dil ve varsa ikinci dil; hedef (dergi, kongre, yayınevi ya da fon programı); şablon dosyası; veri durumu; yazarlar ve kurum bilgisi; finansman; kip (etkileşimli ya da otomatik); bütçe (normal ya da ekonomik).

Hedef dergi belirtilmemişse ve çıktı makaleyse etkileşimli kipte kullanıcıdan hedef dergiyi belirlemesini iste (dergi seçimi için kurulu bir skill varsa onu öner). Otomatik kipte hedef "belirtilmedi" kalır.

İş klasörünü aç (ortak_yonetim.md Bölüm 2), _kurallar klasörünü doldur, `00_brief.md` dosyasını yaz. Alanlar (hepsi doldurulur; bilinmeyen için "belirtilmedi"):

```
konu:
alan:
alan_siniri: <alt alan ya da "yok">
yazar_uzmanligi: <yöntemler ve araçlar>
cikti_turu:
ana_dil:            ikinci_dil:
hedef_ad:           hedef_kapsam:
kelime_siniri:      ozet_siniri:        kaynak_bicimi:      hakemlik: tek kör / çift kör
sablon: <yol ya da "yok">
veri_durumu: hazır / temizlenmemiş / açık veri aranacak / yok
yontem_turleri: <ML, zaman serisi, mekânsal, istatistiksel test; Aşama 3'te kesinleşir>
yazarlar_kurum:
finansman:
kip: etkileşimli / otomatik
butce: normal / ekonomik
```

Hedef derginin yazım kuralları bilinmiyorsa "guide for authors" sayfasını WebFetch ile bir kez oku, sınırları brief'e yaz. Yeni klasörde kararlar.md ve durum.md dosyalarını aç.

Çıkış ölçütü: brief'te boş alan yok, `_kurallar` dolu.

## Aşama 1: Mini tarama

1. Literatür Arama ajanı (sonnet; görev dosyası ajan_literatur_arama.md). Değişkenler: KIP=MINI, KONU=brief'teki konu, ALT_KONU=genel, HEDEF_ADAY=30 (ekonomik: 20), YIL_BAS=bu yıl eksi 5, YIL_BIT=bu yıl, CIKTI=02_aday_genel.csv, IDDIA_DOSYASI=yok, KULLANICI_DOSYALARI=kullanıcı verdiyse yolları, yoksa "yok".
2. Kaynak Doğrulama ajanı (haiku; ajan_kaynak_dogrulama.md). ADAY=02_aday_genel.csv, PARCA=02_parca_genel.csv, BIB=kaynaklar_genel.bib, KAYIT=02_dogrulama_kaydi_genel.csv.
3. Birleştir: `python3 "$IS/_kurallar/birlestir_literatur.py" "$IS"`. Çıktıdaki doğrulanmış kaynak sayısını oku.
4. Doğrulanmış kaynak 15'ten azsa H3 uygulanır.
5. Araştırma Sorusu ajanı (opus; ajan_arastirma_sorusu.md). Değişken yalnız IS.
6. Ana oturum 01_mini_tarama.md dosyasını okur.

Çıkış ölçütü: matriste en az 15 doğrulanmış kaynak, 01_mini_tarama.md içinde en az 3 aday soru.

## G1: Araştırma sorusu seçimi

Etkileşimli kip: adayları ortak_yonetim.md Bölüm 6'ya göre sun (01_mini_tarama.md eki), kullanıcı bir soru seçip onaylayana kadar bekle.

Otomatik kip karar kuralı. Her adayın 01_mini_tarama.md içindeki puanları kullanılır. Ağırlıklar: yenilik 0,30; veri erişilebilirliği 0,30; yöntemin kullanıcının uzmanlığına uygunluğu 0,15; alan sınırına uyum 0,15; hedef dergi kapsamına uyum 0,10 (hedef belirtilmediyse bütün adaylara 3). Yenilik ya da veri puanı 3'ün altında olan ve alan sınırı dışında kalan adaylar elenir. Kalanlardan ağırlıklı toplamı en yüksek olan seçilir; eşitlikte veri puanı yüksek olan seçilir. Aday kalmazsa D1.

Seçilen soru kararlar.md ve 00_brief.md'ye (yeni alan: `secilen_soru:`) yazılır.

## Aşama 2: Detaylı tarama

Hedef doğrulanmış kaynak: makale, kitap bölümü ve proje için 40-60; bildiri için 20-30. Ekonomik kipte aralığın alt sınırı hedeftir.

1. Alt konular: yontem, uygulama, veri, rakip. Ekonomik kipte üç alt konu: yontem, uygulama, veri_rakip.
2. Alt konu başına HEDEF_ADAY = yukarı yuvarla(hedef üst sınırı × 1,3 / alt konu sayısı). Ekonomik kipte hedef alt sınırı kullanılır.
3. Literatür Arama ajanları paralel (tek mesajda, alt konu başına bir çağrı). Değişkenler: KIP=DETAY, KONU=secilen_soru, ALT_KONU=<alt konu>, YIL_BAS=bu yıl eksi 10, YIL_BIT=bu yıl, CIKTI=02_aday_<alt konu>.csv, IDDIA_DOSYASI=yok, KULLANICI_DOSYALARI ilgili olanlar ya da "yok". 
4. Kaynak Doğrulama ajanları paralel, alt konu başına bir çağrı (ADAY=02_aday_<alt>.csv, PARCA=02_parca_<alt>.csv, BIB=kaynaklar_<alt>.bib, KAYIT=02_dogrulama_kaydi_<alt>.csv).
5. Birleştir: `python3 "$IS/_kurallar/birlestir_literatur.py" "$IS"`.
6. Alt sınıra ulaşılmadıysa H3.

Çıkış ölçütü: doğrulanmış kaynak sayısı hedef alt sınırında ya da üstünde (H3 kapsamında %70 ve üstü kabul edilir ve G2'de bildirilir).

## Aşama 3: Boşluk, yöntem ve veri (ana oturum)

Matrisi Read ile açma. Gereken sütunları şu komutla al:

```bash
python3 -c "import csv,sys;[print(r['anahtar'],r['yil'],r['yontem'],r['veri'],r['temel_bulgu'],r['sinirlilik'],sep=' | ') for r in csv.DictReader(open(sys.argv[1],encoding='utf-8'))]" "$IS/02_literatur_matrisi.csv"
```

Ekonomik kipte yalnız `anahtar, yontem, sinirlilik` sütunları alınır.

`03_bosluk_yontem.md` dosyasını şu sabit başlıklarla yaz:

1. Boşluk: tek paragraf; dayandığı en az 5 kaynak anahtarıyla.
2. Araştırma sorusu ve hipotezler: H1, H2...; her biri sınanabilir ve yönü belirli.
3. Veri: kaynak, erişim yolu, lisans, dönem, gözlem sayısı, etik izin gereği.
4. Yöntem türleri: analiz_kontrol.md'deki listelerden hangileri geçerli (9.2 ML, 9.3 zaman serisi, 9.4 mekânsal, 9.5 istatistiksel test).
5. Analiz planı: birincil metrik (tek, adıyla); ikincil metrikler; karşılaştırma modelleri; doğrulama kurgusu; istatistiksel karşılaştırma testi; duyarlılık analizleri; aykırı değer ve eksik veri kuralı. Planı yazmadan önce `$IS/_kurallar/analiz_kontrol.md` içinde seçilen listelerin yalnız doğrulama kurgusu ve metrik maddelerini oku (9.2'de M8-M15, 9.3'te Z1-Z10, 9.4'te K4-K6, 9.5'te T1-T7; Grep ile bul, offset ve limit ile oku) ki plan bu maddelerle çelişmesin.
6. Başlık önerisi: en çok 3.
7. Bölüm ve alt başlık iskeleti.
8. Hedef dergiye uyum notu.

Analiz planı sonuç görülmeden yazıldığı için ön kayıt işlevi görür. G2'den sonraki her değişiklik kararlar.md'ye "plan değişikliği" olarak yazılır ve metinde keşifsel analiz diye belirtilir.

Veri erişimini fiilen dene: açık veriyse indirme adresini WebFetch ile aç ya da komut satırından küçük bir parça indirmeyi dene; kullanıcının verisiyse dosyanın eklendiğini doğrula. Sonucu Veri başlığına "erişim doğrulandı: evet/hayır" olarak yaz. Erişim yalnız kullanıcıdan, ücretle, lisans başvurusuyla ya da etik izinle mümkünse D2.

`00_brief.md` içindeki yontem_turleri alanını güncelle.

## G2: Tasarım onayı

Etkileşimli kip: 03_bosluk_yontem.md'yi sun, onay bekle.

Otomatik kip karar kuralı: 03_bosluk_yontem.md içindeki sekiz başlık doluysa, birincil metrik tek ise, her hipotez için sınama yöntemi yazılıysa ve veri erişimi doğrulandıysa onaylanmış sayılır. Biri eksikse eksik giderilir; ikinci denemede de eksikse D6.

## Devir

ortak_yonetim.md Bölüm 10'u uygula. durum.md: "Sıradaki skill: ay-analiz". Gönderilecek dosyalar: devir zip'i, 03_bosluk_yontem.md, 02_literatur_matrisi.csv. Veri kullanıcıdan gelecekse yeni sohbette veriyi de eklemesi söylenir.

## Bu aşamanın hata durumları

H1. Elicit çalışmıyor. Arama ajanı yedek yollara (WebSearch, Crossref, OpenAlex) kendisi geçer. Hedef sayılar değişmez. Ana oturum G1 ya da G2 özetinde "Elicit kullanılamadı" diye belirtir.

H2. Doğrulama servislerine ulaşılamıyor. BEKLEMEDE kaynaklar metne girmez. Aşama 2 sonunda BEKLEMEDE oranı (kayıttaki BEKLEMEDE sayısı / toplam aday) %20'yi aşıyorsa BEKLEMEDE adaylar için Kaynak Doğrulama bir kez daha çalıştırılır (ADAY: BEKLEMEDE satırlarından oluşturulan 02_aday_bekleyen.csv). Yine aşıyorsa G2 özetinde bildirilir.

H3. Doğrulanmış kaynak hedefin altında. Eksik kalan alt konu için tek ek Literatür Arama çağrısı yapılır: yıl aralığı 10 yıla (Aşama 2'de 15 yıla) genişletilir, EK BAĞLAM'a "önceki sorgular günlükte; farklı eş anlamlılar ve yöntem adları kullan" yazılır; ardından Kaynak Doğrulama ve birleştirme. Yine alt sınırın altındaysa: %70 ve üstünde devam edilir ve eksiklik G1 ya da G2 özetinde yazılır; %70'in altında D5. Sayıyı tutturmak için doğrulanmamış kaynak eklenmez.

## Çağrı tavanları (normal / ekonomik)

- Aşama 1: Literatür Arama 1 / 1; Kaynak Doğrulama 1 / 1; Araştırma Sorusu 1 / 1.
- Aşama 2: Literatür Arama 4 / 3 paralel; Kaynak Doğrulama 4 / 3 paralel.
- H2 ve H3 kapsamında: ek Literatür Arama en çok 1, ek Kaynak Doğrulama en çok 2.
- Model yükseltme kuralı (ortak_yonetim.md Bölüm 5) bu tavanların içinde sayılmaz, ancak her ajan için bir kez uygulanır.
