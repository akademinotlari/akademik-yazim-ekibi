# Atıf doğrulama protokolü

Bu protokol her kaynak için sırayla uygulanır. Literatür Arama ajanı P1, P5, P6 ve P7'yi; Kaynak Doğrulama ajanı P1-P4, P8 ve P9'u; Doğrulayıcılar bütününü kullanır.

## Protokol

P1. Tanımlayıcı. Kaynağın DOI'si aranır. DOI yoksa kabul edilen tanımlayıcılar: yayıncının ya da derginin kendi sayfası (DergiPark dahil), kitap için ISBN ve yayınevi sayfası, tez için YÖK Ulusal Tez Merkezi kaydı, resmî kurum yayını için kurumun kendi sayfası. Bunların hiçbiri yoksa kaynak alınmaz.

P2. Çözümleme. WebFetch ile `https://api.crossref.org/works/<DOI>` açılır. Yanıt gelmezse sırayla `https://doi.org/<DOI>`, `https://api.openalex.org/works/doi:<DOI>` ve veri setleri için `https://api.datacite.org/dois/<DOI>` denenir. Hepsi başarısızsa durum BEKLEMEDE yazılır.

P3. Üst veri eşleşmesi. Beş alan çözümlenen kayıtla karşılaştırılır: başlık (büyük-küçük harf ve noktalama dışında aynı), ilk yazarın soyadı, yıl, dergi ya da yayın adı, cilt ve sayfa ya da makale numarası. Yılda çevrimiçi ilk yayın ile basılı yayın arasındaki bir yıllık fark kabul edilir; basılı cildin yılı esas alınır. Başlık ya da ilk yazar uyuşmuyorsa DOĞRULANAMADI. Diğer alanlardaki fark çözümlenen kayda göre düzeltilir ve DÜZELTİLDİ yazılır.

P4. Yayın durumu. Crossref kaydında geri çekme ya da düzeltme bildirimi aranır (update-to, relation alanları ya da başlıkta "RETRACTED"). Geri çekilmiş kaynak alınmaz (GERİ ÇEKİLMİŞ). Düzeltme yayımlanmışsa not sütununa yazılır. Önbaskının yayımlanmış sürümü varsa yayımlanmış sürüm alınır.

P5. İçerik erişimi ve kanıt düzeyi. Özet ya da tam metin okunur (Elicit kaydı, yayıncı sayfası, açık erişim kopyası). Kanıt düzeyi yazılır: T tam metin okundu, O yalnız özet okundu, M yalnız üst veri görüldü.

P6. İddia desteği. Metinde bir kaynağa atfedilen her iddia o kaynağın okunan kısmında yer almalıdır. Sayısal değer, yöntem ayrıntısı, karşılaştırma ya da "ilk", "tek", "en" içeren iddia için düzey T ya da ilgili bilgiyi içeren O gerekir. Düzeyi M olan kaynak yalnız "bu konuda çalışma yapılmıştır" türünden varlık bildiren cümlede anılabilir.

P7. İkincil atıf yasağı. Bir kaynağın ne söylediği başka bir makalenin anlatımından öğrenildiyse, özgün kaynak P5'ten geçmeden o iddia için atıf yapılmaz.

P8. BibTeX kaydı. Çözümlenen üst veriden kurulur; bellekten yazılmaz. Zorunlu alanlar: author, title, year, journal ya da booktitle ya da publisher, volume, pages ya da makale numarası, doi (DOI'siz kaynakta url). Yazar adları kayıttaki yazımıyla, Türkçe karakterler korunarak.

P9. Kayıt. Doğrulama kaydı dosyasına satır yazılır. Sütunlar (başlık satırı aynen):

```
anahtar,doi_ya_da_adres,cozumleme_yolu,baslik_eslesti,yazar_eslesti,yil_eslesti,dergi_eslesti,geri_cekilme,kanit_duzeyi,durum,tarih,not
```

P10. Kullanıcının verdiği kaynaklar da aynı protokolden geçer. Doğrulanamayanlar silinmez; kullanıcıya listelenir.

## Durum değerleri

DOĞRULANDI: P1-P4 sorunsuz. DÜZELTİLDİ: ikincil alanlar kayda göre düzeltildi. BEKLEMEDE: çözümleme servislerine ulaşılamadı; metne girmez, son kontrolde bir kez daha denenir. DOĞRULANAMADI: başlık ya da yazar uyuşmuyor ya da tanımlayıcı yok; metne girmez. GERİ ÇEKİLMİŞ: metne girmez. Yalnız DOĞRULANDI ve DÜZELTİLDİ durumundaki kaynaklar matrise ve kaynaklar.bib dosyasına yazılır.
