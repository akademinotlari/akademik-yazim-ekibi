---
name: ay-hakem-teslim
description: Kullanıcının akademik yazım ekibinin 4. aşaması. Taslak ve teslim dosyaları hazırlandıktan sonra iç hakem değerlendirmesi, editör kararı, revizyon turları, son doğrulama ve teslim paketi (G4) gerektiğinde ya da devir paketindeki durum.md "Sıradaki skill: ay-hakem-teslim" dediğinde kullan. Dergiden gerçek hakem raporu geldiyse bu skill kullanılmaz; bu ekibin hakem süreci gönderim öncesi iç değerlendirmedir.
---

# Akademik yazım ekibi, 4. aşama: Hakem süreci ve son kontrol (Aşama 7-8)

Sen ana oturum ve editörsün. Hakem raporlarını okur, kanıtları denetler, karar verirsin. Taslak bölümlerin tamamını okumazsın. Bu aşamada ana oturum için Opus önerilir.

## Başlangıç

1. `$SKILL_DIR/references/ortak_yonetim.md` dosyasını oku.
2. ortak_yonetim.md Bölüm 3'ü uygula. Önkoşul: 05_taslak altında altı bölüm dosyası ve durum.md'de "Sıradaki skill: ay-hakem-teslim". Değilse dur.
3. Görev listesi: masa başı, hakem turu 1, editör kararı 1, revizyon 1, (hakem turu 2, editör kararı 2, revizyon 2), ikinci dil, biçimlendirme güncelleme, son doğrulama, düzeltme, G4.

## Aşama 7: Hakem süreci

### Adım 1: Masa başı denetimi (haiku; ajan_masabasi.md)

Değişken yalnız IS. Yalnız `06_hakem/masabasi.md` dosyasını oku. HAYIR çıkan madde varsa hakemler başlatılmaz: eksik, etiketine göre Revizyon ajanına (Adım 4'teki model kuralıyla) tek çağrıyla giderilir (KAYNAK=06_hakem/masabasi.md, TUR=0), sonra masa başı bir kez daha çalışır. Bu çağrılar tur sayısına dahil değildir. İkinci denetimde de HAYIR kalırsa G4'te açık sorun olarak yazılır ve hakemlere geçilir.

### Adım 2: Hakemler (ajan_hakem.md; tek mesajda paralel)

- Hakem 1: model opus; HAKEM_NO=1; TUR=<tur>; HEDEF=brief'teki hedef adı ve kapsamı.
- Hakem 2: model opus (ekonomik: sonnet); HAKEM_NO=2; aynı değişkenler.

### Adım 3: Editör kararı (ana oturum)

İki raporu oku (`06_hakem/hakem1_tur<t>.md`, `hakem2_tur<t>.md`). Her ÖLÜMCÜL ve BÜYÜK maddenin gösterdiği yeri kendin denetle: yalnız o paragrafı (Grep ile satırı bul, Read ile offset ve limit 15), o kod satırını ya da o sayı kimliğini oku. Kanıtı doğrulanmayan madde "editörce reddedildi" notuyla düşürülür.

Karar kuralları yukarıdan aşağıya uygulanır; koşulu sağlanan ilk kural geçerlidir.

RET: (i) en az bir ÖLÜMCÜL madde var ve kanıtı doğrulandı; ya da (ii) Ö1 ya da Ö3 puanı iki hakemden birinde 1; ya da (iii) iki hakemin 10 ölçüt ortalamalarının ortalaması 2,5'in altında; ya da (iv) tur 2 sonunda GİDERİLMEDİ durumunda BÜYÜK madde kaldı ve giderilmesi yeni veri gerektiriyor.
Sonuç: süreç durur. Kullanıcıya raporlar, ret gerekçesi ve üç seçenek sunulur: ay-arastirma Aşama 3'e dönüp soruyu ya da yöntemi değiştirmek, ay-analiz'e dönüp analizi yeniden kurmak, çalışmayı bırakmak. Otomatik kipte de durulur (D4).

BÜYÜK REVİZYON: RET koşulu yok ve (i) en az bir doğrulanmış BÜYÜK madde var; ya da (ii) Ö3, Ö4, Ö5 ya da Ö8 puanlarından biri herhangi bir hakemde 2 ya da altında; ya da (iii) hakemlerden biri BÜYÜK REVİZYON ya da RET önerdi ve dayandığı madde doğrulandı.
Sonuç: revizyon (Adım 4), ardından hakemler tur 2 için yeniden çalışır. Ekonomik kipte tur 2'de yalnız doğrulanmış BÜYÜK maddeyi yazan hakem(ler) çalışır.

KÜÇÜK REVİZYON: yukarıdaki koşullar yok, BÜYÜK madde yok, bütün ölçütler iki hakemde de en az 3 ve en az bir KÜÇÜK madde var.
Sonuç: revizyon; hakemler yeniden çalıştırılmaz. Editör yanıt matrisinden her maddenin giderildiğini değişen yerin kendisini (yalnız o paragraf) okuyarak denetler ve Aşama 8'e geçer.

KABUL: BÜYÜK madde yok, bütün ölçütler en az 4, KÜÇÜK madde sayısı toplam 5'i geçmiyor ve hepsi sunumla ilgili.
Sonuç: küçük maddeler tek Revizyon çağrısıyla ([YAZIM], sonnet) giderilir, Aşama 8'e geçilir.

Yardımcı kurallar:
- Hakem görüş ayrılığı: öneriler bir kademe ayrıysa ağır olan, yalnız dayandığı madde doğrulanmışsa geçerlidir. İki ya da daha çok kademe ayrıysa ayrılığa yol açan maddeler tek tek doğrulanır ve karar yalnız doğrulanan maddelere göre verilir. Üçüncü hakem başlatılmaz.
- Birleştirme: aynı soruna işaret eden maddeler tek maddede birleştirilir; çelişen istekler için hangisinin uygulanacağı gerekçesiyle yazılır.
- Tur sınırı: en fazla iki tur. Tur 2 sonunda kalan KÜÇÜK maddeler ve yeni veri gerektirmeyen GİDERİLMEDİ BÜYÜK maddeler G4'te açık sorun olarak listelenir.

`06_hakem/editor_karari_tur<t>.md` biçimi:

```
EDİTÖR KARARI, tur <t>
Karar: <KABUL / KÜÇÜK REVİZYON / BÜYÜK REVİZYON / RET>
Uygulanan kural: <kural adı ve koşul numarası>
Hakem önerileri: H1 <...>, H2 <...>; ölçüt ortalamaları: H1 <x>, H2 <x>
Doğrulanan büyük maddeler: <liste>; düşürülen maddeler ve gerekçesi: <liste>
Görev listesi (birleştirilmiş, yeniden numaralı):
E1 | [LİTERATÜR] | <önem> | kaynak madde: H2-B1 | <yapılacak iş> | Yer: <...>
E2 | [ANALİZ] | ...
E3 | [YAZIM] | ...
Analizden etkilenecek bölümler: <dosyalar>
```

`06_hakem/yanit_matrisi.md` dosyasını aç (hakem_olcutleri.md 12.4 sütunları) ve her E maddesi için satır ekle; Karar ve sonraki sütunları revizyon ajanları doldurur.

### Adım 4: Revizyon (ajan_revizyon.md)

Sıra sabittir: önce [LİTERATÜR], sonra [ANALİZ], en son [YAZIM]. Her etiket için o etiketteki bütün E maddeleri tek çağrıyla verilir. Değişkenler: IS; ETIKET; TUR; KAYNAK=06_hakem/editor_karari_tur<t>.md.

- [LİTERATÜR]: model sonnet. Ajan yeni kaynak adaylarını 02_aday_revizyon<t>.csv dosyasına yazar. Ardından Kaynak Doğrulama (haiku; ADAY=02_aday_revizyon<t>.csv, PARCA=02_parca_revizyon<t>.csv, BIB=kaynaklar_revizyon<t>.bib, KAYIT=02_dogrulama_kaydi_revizyon<t>.csv) ve `python3 "$IS/_kurallar/birlestir_literatur.py" "$IS"`. Kaynağın metne eklenmesi [YAZIM] revizyonunun işidir; editör bu maddeleri [YAZIM] çağrısına da ekler.
- [ANALİZ]: model opus. Döndükten sonra ozet.md'deki "Tur <t> değişiklikleri" başlığından değişen sayı kimliklerini al; eski değerleri `grep -l` ile 05_taslak'ta ara ve etkilenen bölümleri [YAZIM] çağrısına ekle.
- [YAZIM]: doğrulanmış BÜYÜK madde varsa opus (ekonomik: sonnet), yalnız KÜÇÜK madde varsa sonnet.

Her revizyondan sonra üslup taraması: `python3 _kurallar/uslup_tarama.py --cikti 05_taslak/uslup_raporu.md <değişen dosyalar>`; bulgu varsa Üslup Düzeltici (sonnet) bir kez.

### Adım 5: İkinci dil (yalnız brief'te ikinci dil varsa)

Çeviri Ajanı (sonnet; ajan_ceviri.md). Değişkenler: IS; HEDEF_DIL=brief'teki ikinci_dil. Ardından `python3 _kurallar/uslup_tarama.py --cikti 05_taslak/<dil kodu>/uslup_raporu.md 05_taslak/<dil kodu>/*.md` ve gerekirse Üslup Düzeltici bir kez. Ekonomik kipte bu adım G4'ten sonra, kullanıcı isterse yapılır.

### Adım 6: Biçimlendirme güncellemesi

Hakem sürecinde değişen taslak dosyası varsa Biçimlendirme (sonnet; ajan_bicimlendirme.md) KIP=GUNCELLE, DEGISEN=<değişen dosyalar>, SABLON=brief'teki şablon. İkinci dil sürümü varsa KIP=TAM ile o dil için ayrı bir çağrı (EK BAĞLAM: "05_taslak/<dil kodu>/ altındaki dosyaları kullan, çıktıları 07_teslim/<dil kodu>/ altına yaz").

## Aşama 8: Son kontrol

1. Doğrulayıcılar tek mesajda paralel:
   - Doğrulayıcı Mekanik (haiku; ajan_dogrulayici_mekanik.md). Değişkenler: IS; IKINCI_KONTROL=hayır.
   - Doğrulayıcı İçerik (sonnet; ajan_dogrulayici_icerik.md). Değişkenler: IS; IKINCI_KONTROL=hayır.
2. Yalnız iki raporun özet satırlarını oku (`grep -E '^[0-9]+ \|' 07_teslim/dogrulama_*.md` ve son satırlar). BAŞARISIZ maddeler etiketlerine göre Revizyon ajanına verilir (KAYNAK=07_teslim/dogrulama_mekanik.md ya da dogrulama_icerik.md, TUR=son). [BİÇİM] etiketli maddeler Biçimlendirme (KIP=GUNCELLE) ile giderilir.
3. Doğrulayıcılar yalnız BAŞARISIZ maddeler için bir kez daha çalışır (IKINCI_KONTROL=evet). Kalan maddeler G4'te açık sorun olarak listelenir.

## G4: Teslim

Her kipte sunulur. 07_teslim altındaki her dosya, kararlar.md, iki doğrulama raporu, yanit_matrisi.md ve 05_taslak/ekler/eksikler.md SendUserFile ile gönderilir. Özet ortak_yonetim.md Bölüm 6'ya göre; ayrıca "[YAZAR DOLDURACAK]" alanları ve açık sorunlar listelenir. Otomatik modda kararlar.md'deki bütün kararlar tek satırlık liste olarak eklenir.

Son olarak ortak_yonetim.md Bölüm 10'daki devir paketi `<is>_devir_teslim.zip` adıyla hazırlanıp gönderilir (arşiv amaçlı). durum.md: "Sıradaki skill: bitti".

## Bu aşamanın hata durumları

H14. Hakem raporları birbiriyle ya da analizle çelişiyor. Adım 3'teki kanıt doğrulama ve görüş ayrılığı kuralları uygulanır; ek hakem başlatılmaz.

H2 (son kontrol). Doğrulayıcı DOI'leri çözümleyemezse ilgili kaynaklar BEKLEMEDE kalır; ikinci kontrolde de çözümlenemezse G4'te "doğrulanamayan kaynaklar" olarak listelenir ve kullanıcının karar vermesi istenir. Kaynak metinden kendiliğinden çıkarılmaz.

Analiz revizyonu başarısız olursa (H5) ay-analiz'deki H5 yolu uygulanır: log dosyasının son 50 satırı okunur, nedenle tek yeni çağrı yapılır; o da başarısızsa madde açık sorun olarak kalır.

## Çağrı tavanları (normal / ekonomik)

- Masa başı: Masa Başı Denetçisi 2; düzeltme için Revizyon en çok 3 (etiket başına 1).
- Tur başına: Hakem 2 / tur 2'de en çok 1 (ekonomik); Revizyon etiket başına 1 (en çok 3); [LİTERATÜR] için ek Kaynak Doğrulama 1; Üslup Düzeltici 1.
- Tur sayısı en çok 2.
- İkinci dil: Çeviri 1; Üslup Düzeltici 1.
- Biçimlendirme: en çok 2 (ana dil ve ikinci dil) ve son kontrol düzeltmesi için 1.
- Son kontrol: Doğrulayıcı Mekanik 2; Doğrulayıcı İçerik 2; düzeltme için Revizyon etiket başına 1.
