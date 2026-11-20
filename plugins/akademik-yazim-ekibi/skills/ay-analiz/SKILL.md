---
name: ay-analiz
description: Kullanıcının akademik yazım ekibinin 2. aşaması. Onaylı bir 03_bosluk_yontem.md (G2) sonrasında veri profili, veri hazırlama, modelleme, istatistiksel analiz, şekil ve tablo üretimi ve G3 onayı gerektiğinde ya da devir paketindeki durum.md "Sıradaki skill: ay-analiz" dediğinde kullan.
---

# Akademik yazım ekibi, 2. aşama: Analiz (Aşama 4)

Sen ana oturumsun. Kod yazmaz, veri ve kod okumazsın; ajanları sırayla çağırır, raporlarını okur, G3'ü sunarsın. Bu aşamada ana oturum için Sonnet yeterlidir.

## Başlangıç

1. `$SKILL_DIR/references/ortak_yonetim.md` dosyasını oku.
2. ortak_yonetim.md Bölüm 3'ü uygula. Önkoşul: `03_bosluk_yontem.md` var ve durum.md'de G2 onaylı (kullanıcı ya da otomatik). Değilse dur.
3. Görev listesi: veri yerleşimi, Veri Profili, Veri Hazırlama (koşullu), Analiz, Şekil, Tekrarlanabilirlik denetimi, G3, devir.

## Adım 1: Veri yerleşimi

- Kullanıcı veri dosyası eklediyse dosyaları `$IS/04_analiz/veri/ham/` altına kopyala (orijinali değiştirme).
- Açık veriyse 03_bosluk_yontem.md'deki erişim yolundan komut satırıyla indir. Site izin listesinde değilse indirme reddedilir; aynı siteyi başka komutla deneme, H4(b) uygula.
- `ls -la "$IS/04_analiz/veri/ham"` ile dosyaları denetle. Boşsa H4.

## Adım 2: Veri Profili (haiku; ajan_veri_profili.md)

Değişken yalnız IS. Döndükten sonra yalnız `04_analiz/veri_profili.md` dosyasının son bölümünü ("Veri Hazırlama gerekli mi") ve "Plan değişkenleri" tablosunu oku. Plan değişkenlerinden biri YOK ise H4(c).

## Adım 3: Veri Hazırlama (sonnet; ajan_veri_hazirlama.md)

Yalnız veri_profili.md "Veri Hazırlama gerekli mi: EVET" diyorsa çalışır. Değişken yalnız IS.

## Adım 4: Analiz (opus; ajan_analiz.md)

Değişkenler: IS; YONTEM_TURLERI = 03_bosluk_yontem.md "Yöntem türleri" başlığındaki liste (örnek: "9.2, 9.3"); HP_DENEME = 50 (ekonomik: 30); MODEL_SAYISI = 6 (ekonomik: 4).

Döndükten sonra yalnız `04_analiz/ozet.md` ve `04_analiz/kontrol_listesi.md` dosyalarını oku. kontrol_listesi.md içinde "UYGUN DEĞİL" varsa H6.

## Adım 5: Şekil (sonnet; ajan_sekil.md)

Değişkenler: IS; DIL = brief'teki ana_dil. Analiz Ajanı 04_analiz/sekil_plani.md yazmamışsa önce H9 uygulanır.

## Adım 6: Tekrarlanabilirlik denetimi (haiku; ajan_tekrar_denetci.md)

Değişken yalnız IS. Yalnız `04_analiz/denetim_raporu.md` dosyasını oku. BAŞARISIZ satırı varsa:
- yeniden üretim, sayı uyuşmazlığı ya da kanıtsız UYGUN: Analiz Ajanına tek düzeltme çağrısı (EK BAĞLAM: "denetim_raporu.md içindeki BAŞARISIZ maddeleri gider; yalnız bunları değiştir"), ardından denetçi bir kez daha.
- şekil sorunu (dpi, eksik dosya): Şekil Ajanına tek düzeltme çağrısı, ardından denetçi bir kez daha.
- ikinci denetimde de BAŞARISIZ kalan madde G3'te açık sorun olarak sunulur.

Çıkış ölçütü: kontrol_listesi.md'de UYGUN DEĞİL yok; ozet.md'de her hipotez için "desteklendi / desteklenmedi / belirsiz" hükmü ve dayandığı sayı kimliği var; denetim_raporu.md'de BAŞARISIZ yok ya da açık sorun olarak kaydedildi.

## G3: Bulgular onayı

Şekilleri bir kez Read ile görüntüle. Etkileşimli kipte ortak_yonetim.md Bölüm 6'ya göre sun: ekler ozet.md, bütün şekiller, tablolar, kontrol_listesi.md, denetim_raporu.md.

Otomatik kip karar kuralı: kontrol_listesi.md'de UYGUN DEĞİL yoksa, denetim_raporu.md'de BAŞARISIZ yoksa ve D3 ya da D7 tetiklenmediyse onaylanmış sayılır.

## Devir

ortak_yonetim.md Bölüm 10. durum.md: "Sıradaki skill: ay-yazim". Gönderilecekler: devir zip'i, ozet.md, şekiller.

## Bu aşamanın hata durumları

H4. Veri eksik ya da erişilemiyor. Karar sırası:
(a) Veri kullanıcıda ve eklenmemişse kullanıcıdan istenir (otomatik kipte D2).
(b) Açık veri komut satırından indirilemiyorsa kullanıcıdan dosyayı eklemesi istenir. Başka komutla aynı siteye yeniden denenmez.
(c) Veri kısmen eksikse (bazı değişkenler ya da dönemler yok): eksik kısım analiz planından çıkarılabiliyorsa ve birincil hipotez hâlâ sınanabiliyorsa plan daraltılır, kararlar.md'ye "plan değişikliği" yazılır ve G3'te bildirilir. Birincil hipotez sınanamıyorsa durulur.
(d) Eşdeğer açık veri seti varsa (aynı değişkenler, benzer bağlam) aday olarak kullanıcıya sunulur. Otomatik kipte bu D7 kapsamındadır, durulur.
(e) Hiç veri yoksa sentetik veriyle bulgu üretilmez. Kullanıcıya seçenekler sunulur: veri toplama planı içeren proje ya da protokol metnine dönmek, derleme ya da kavramsal çalışmaya dönmek, konuyu değiştirmek.
Sentetik veri yalnız kod hattını sınamak için kullanılabilir; dosya adı `SENTETIK_` ile başlar ve sonuçları hiçbir tabloya, sayilar.csv'ye ya da metne girmez.

H5. Analiz çalışmıyor (kod ya da ortam hatası). Analiz Ajanı hatayı kendisi sınıflandırır ve iki kez düzeltmeyi dener (ajan_analiz.md). BAŞARISIZ dönerse ana oturum ilgili log dosyasının yalnız son 50 satırını okur (`tail -n 50`) ve nedeni EK BAĞLAM olarak yazarak tek yeni çağrı yapar. O da başarısızsa model yükseltme yoktur (zaten opus); durulur (otomatik kipte D6).

H6. Kontrol listesinde UYGUN DEĞİL var. Madde giderilebilir türdense (eksik temel model, belirsizlik hesabı, sızıntılı ön işleme) Analiz Ajanına yalnız o maddeler için tek düzeltme çağrısı yapılır. Giderilemiyorsa (veri yapısı uygun doğrulamaya izin vermiyor gibi) G3'te açıkça sunulur ve metinde sınırlılık olarak yazılması kararlaştırılır.

H7. Sonuçlar hipotezi desteklemiyor ya da model temel modeli geçemiyor. Bu bir hata değil, bulgudur ve aynen raporlanır. Yasak: metriği değiştirmek, tohum aramak, test kümesinde ayar yapmak, yalnız olumlu alt grubu sunmak, aykırı değer kuralını sonradan değiştirmek. İzinli: analiz planındaki duyarlılık analizleri ve "keşifsel" etiketli ek incelemeler. G3'te seçenekler: olumsuz sonucu yayımlamak (güven aralıkları ve güç tartışmasıyla), soruyu yeniden çerçevelemek (ay-arastirma Aşama 3'e dönüş), çalışmayı bırakmak. Otomatik kipte D3.

H8. Model yakınsamıyor ya da tohumlar arasında büyük fark var. Analiz Ajanı öğrenme oranı, düzenlileştirme ve ölçeklemeyi denetler, tohum sayısını 10'a çıkarır ve dağılımı raporlar. Kararsızlık sürüyorsa bulgu olarak yazılır ve model iddiası buna göre zayıflatılır.

## Çağrı tavanları (normal / ekonomik)

Veri Profili 1; Veri Hazırlama 0 ya da 1; Analiz 1 ve düzeltme en çok 2 / 1; Şekil 1 ve düzeltme en çok 1; Tekrarlanabilirlik Denetçisi en çok 2.
