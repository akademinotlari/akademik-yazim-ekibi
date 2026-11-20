---
name: baslat
description: Çok ajanlı akademik yazım ekibinin giriş noktası. Konu verilip makale, bildiri, kitap bölümü ya da proje metni üretilmesi istendiğinde, "akademik yazım ekibi" anıldığında ya da bir devir paketi (*_devir_*.zip) eklenip kaldığı yerden devam edilmek istendiğinde kullan.
---

# Akademik Yazım Ekibi (yönlendirici)

Bu skill işi kendisi yapmaz; doğru aşama skill'ini seçip yükler. Ekip, bağlam ve token tüketimini sınırlamak için dört aşama skill'ine bölünmüştür. Her aşama ayrı bir sohbette çalışır ve bir sonrakine devir paketiyle (zip) geçer.

| Sıra | Skill | Aşamalar | Kapı | Önerilen sohbet modeli |
|---|---|---|---|---|
| 1 | ay-arastirma | 0 brief, 1 mini tarama, 2 detaylı tarama, 3 boşluk-yöntem | G1, G2 | Opus |
| 2 | ay-analiz | 4 analiz, şekil, tekrarlanabilirlik | G3 | Sonnet |
| 3 | ay-yazim | 5 yazım, 6 şablon ve ekler | yok | Sonnet |
| 4 | ay-hakem-teslim | 7 hakem süreci, 8 son kontrol | G4 | Opus |

## Hangi skill yüklenecek

Aşağıdaki sırayla ilk tutan kural uygulanır:

1. Kullanıcı bir devir paketi eklediyse: `find / -name '*_devir_*.zip' -not -path '/proc/*' 2>/dev/null` ile bul, `unzip -q -o <zip> -d "$PWD"` ile aç, açılan klasördeki durum.md'nin "Sıradaki skill" satırını oku ve o skill'i yükle. "bitti" yazıyorsa kullanıcıya işin tamamlandığını söyle ve ne istediğini sor.
2. Çalışma alanında durum.md varsa (`find "$PWD" -maxdepth 3 -name durum.md`): aynı şekilde "Sıradaki skill" yüklenir.
3. Kullanıcı belli bir aşamayı adıyla istediyse ("analizi yap", "yazıma geç", "hakem sürecini çalıştır"): o skill yüklenir. Skill kendi önkoşulunu denetler; önkoşul yoksa kullanıcıya eksik olanı söyler.
4. Hiçbiri yoksa yeni iştir: ay-arastirma yüklenir.

Yükleme Skill aracıyla yapılır. Plugin'den kurulan skill'ler listede ön ekle görünür (örnek: akademik-yazim-ekibi:ay-arastirma); listedeki adı aynen kullan. Skill listede yoksa kullanıcıya "ay-... skill'i kurulu değil" de ve dur; aşamayı bellekten yürütme.

## Yardımcı skill'ler

- human: aynı plugin'le gelir; yazım, üslup düzeltme, ek metin ve çeviri ajanları yükler. Kapatılmışsa ajanlar yazim_kurallari.md madde 7 ve üslup tarama betiğiyle çalışır.
- docx ve dataviz: claude.ai'nin hazır skill'leri; biçimlendirme ve şekil ajanları varsa kullanır, yoksa yedek kurallara geçer.
- Hedef dergi seçimi, proje panel denetimi ya da gerçek hakem raporuna yanıt için kullanıcının kurulu başka bir skill'i varsa, aşama skill'leri onu önerebilir. Bu ekibin hakem süreci gönderim öncesi iç değerlendirmedir; dergiden gelen gerçek hakem raporuna yanıt bu ekibin işi değildir.

## Token kuralları (özet)

- Bir sohbette bir aşama. Aşama bitince devir zip'i gönderilir; kullanıcı yeni sohbet açıp zip'i ekler.
- Ana oturum ajan görev dosyalarını, kodu, veriyi ve taslağın tamamını okumaz; ajanlar kendi dosyalarını okur.
- Mekanik işler betikle (birleştirme, üslup taraması, mekanik kontrol) ya da haiku ile, arama ve kalıba bağlı metin sonnet ile, analiz, ana metin ve hakemlik opus ile yapılır. Ayrıntılı tablo her aşama skill'inin references/ortak_yonetim.md dosyasındadır.
