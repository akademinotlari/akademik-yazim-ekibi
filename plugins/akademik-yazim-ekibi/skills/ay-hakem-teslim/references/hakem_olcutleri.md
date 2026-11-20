# Hakem ölçütleri, rapor şablonu ve yanıt matrisi

## 11.1 Değerlendirme ölçütleri (her biri 1-5 puan)

Puan anlamı: 5 yayın standardını aşıyor; 4 karşılıyor, yalnız küçük düzeltme gerekir; 3 karşılamaya yakın, belirli düzeltmelerle karşılar; 2 önemli eksik var, yeni analiz ya da yeniden yazım gerekir; 1 giderilemez ya da temel düzeyde eksik.

Ö1. Özgünlük ve katkı. Araştırma sorusu yeni mi, katkı açıkça ve doğru biçimde ifade edilmiş mi, mevcut çalışmalardan farkı kanıtla gösterilmiş mi.
Ö2. Önem ve dergi kapsamına uyum. Soru alan için anlamlı mı, hedef derginin okur kitlesine ve kapsamına uyuyor mu.
Ö3. Yöntemin sağlamlığı. Yöntem soruya uygun mu, doğrulama kurgusu doğru mu, veri sızıntısı var mı, karşılaştırma adil mi (analiz_kontrol.md maddeleri).
Ö4. Veri ve tekrarlanabilirlik. Veri yeterli ve uygun mu, kaynağı ve ön işlemesi açık mı, bir başka araştırmacı çalışmayı yeniden üretebilir mi.
Ö5. Bulguların geçerliliği ve istatistik. Belirsizlik raporlanmış mı, testler doğru mu, sayılar tablolarla tutarlı mı, seçici raporlama var mı.
Ö6. Literatürün kapsamı ve doğruluğu. Temel ve güncel çalışmalar var mı, kaynaklar iddiaları gerçekten destekliyor mu, dengeli mi.
Ö7. Tartışma ve yorum. Bulgular literatürle karşılaştırılmış mı, alternatif açıklamalar ele alınmış mı, sınırlılıklar dürüstçe yazılmış mı.
Ö8. Sonuçların verilerle desteklenmesi. Her sonuç bir bulguya dayanıyor mu, aşırı genelleme ya da nedensellik iddiası var mı.
Ö9. Sunum. Yapı, dil, akademik kayıt, şekil ve tabloların niteliği ve gerekliliği, başlık ve özetin içeriği yansıtması.
Ö10. Etik ve beyanlar. Etik onay, veri erişilebilirliği, çıkar çatışması, finansman, yapay zekâ kullanım beyanı; intihal ya da yinelenen yayın belirtisi.

## 11.2 Sorun önem düzeyleri

ÖLÜMCÜL: giderilmediği sürece ana sonucu geçersiz kılan ve eldeki veriyle giderilmesi mümkün görünmeyen sorun (ana sonucu doğuran veri sızıntısı, aynı sorunun daha önce yanıtlanmış olması, doğrulanamayan veri, ana iddiayı çürüten hata).
BÜYÜK: yeni analiz, yeni veri ya da bir bölümün yeniden yazılmasını gerektiren sorun (eksik temel model, belirsizlik ölçüsü yok, yanlış test, desteklenmeyen sonuç, önemli literatür eksiği).
KÜÇÜK: yeni analiz gerektirmeyen metin, atıf, şekil ya da sunum düzeltmesi.

## 11.3 Hakem raporu şablonu

```
HAKEM RAPORU
Hakem: <1 ya da 2>   Tur: <1 ya da 2>   Hedef: <dergi>
Başlık: <metnin başlığı>

1. Çalışmanın özeti (hakemin kendi cümleleriyle, 3-5 cümle: soru, veri, yöntem, ana bulgu, iddia edilen katkı)

2. Genel değerlendirme (tek paragraf: katkı yayın için yeterli mi, en önemli güçlü ve zayıf yön)

3. Güçlü yönler (2-5 madde, somut)

4. Ölçüt puanları
Ö1 <puan> <gerekçe>
...
Ö10 <puan> <gerekçe>

5. Büyük sorunlar (ÖLÜMCÜL ve BÜYÜK)
B1 | <etiket> | <önem> | Yer: <dosya, alt başlık, şekil/tablo>
Kanıt: <kısa alıntı, kod satırı ya da sayı kimliği>
İstenen değişiklik: <uygulanabilir talimat>
B2 ...

6. Küçük sorunlar
K1 | <etiket> | Yer: <...> | <sorun ve istenen değişiklik>
K2 ...

7. Sayı denetimi (karşılaştırılan sayı adedi, uyuşmayanların listesi)

8. Öneri: KABUL / KÜÇÜK REVİZYON / BÜYÜK REVİZYON / RET
Gerekçe: <puanlara ve madde numaralarına bağlı 2-3 cümle>

9. Hakemin güven düzeyi: yüksek / orta / düşük (ve hangi konuda uzmanlık dışı kaldığı)

10. Editöre not (yazara iletilmeyecek kaygılar; yoksa "yok")

Tur 2 ise 5 ve 6 yerine: önceki her madde için GİDERİLDİ / KISMEN / GİDERİLMEDİ ve tek cümle gerekçe; ardından revizyondan doğan yeni sorunlar.
```

## 12.4 Hakem yanıt matrisi ve yanıt mektubu

İç süreçte 06_hakem/yanit_matrisi.md şu sütunlarla tutulur (her madde bir satır):

```
No | Kaynak (H1-B2 gibi) | Eleştirinin özeti | Etiket | Karar (KABUL / KISMEN / GEREKÇELİ RET) | Yapılan değişiklik | Yer (dosya, alt başlık, paragraf) | Tur 2 durumu
```

Gerçek dergi revizyonunda (kullanıcı dergiden gelen hakem raporlarını verdiğinde) aynı matris doldurulur ve şu kalıba dökülür:

```
Response to Reviewers
Manuscript: [numara], "[Başlık]"

We thank the editor and reviewers for their comments. Each comment is reproduced below, followed by our response and the change made. Line numbers refer to the revised manuscript; changes are marked in [renk/izleme biçimi].

Reviewer 1
Comment 1.1: [hakemin yorumu, aynen]
Response: [doğrudan yanıt; kabul ediliyorsa ne yapıldığı, edilmiyorsa kanıtlı gerekçe]
Change: [değişen metnin kısa alıntısı ya da "No change"], Section [x], lines [a to b]
```

Yanıt kuralları: her yorum ayrı yanıtlanır, hiçbiri atlanmaz; yanıt ilk cümlede ne yapıldığını söyler; "We thank the reviewer for this insightful comment" türü kalıp her yanıtta yinelenmez; reddedilen öneride kanıt (veri, analiz ya da kaynak) gösterilir; yapılmamış değişiklik yapılmış gibi yazılmaz; satır numaraları son dosyadan alınır.
