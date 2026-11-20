# Ortak ajan kuralları

Her ajan bu dosyayı görev dosyasından önce okur. Görev dosyası bu dosyayla çelişirse görev dosyası geçerlidir; ancak madde 3 (uydurma yasağı) hiçbir durumda gevşemez.

1. Çalışma klasörü {IS} değişkeniyle verilir. Yalnız görev dosyanın "YAZACAĞIN DOSYALAR" bölümünde sayılan dosyalara yaz. Başka dosyayı değiştirme, silme ya da yeniden adlandırma.
2. Bu görevin öncesindeki konuşmayı görmüyorsun. Gereken her şey sayılan dosyalardadır. Sayılan bir dosya yoksa ya da boşsa tahmin yürütme, SORUNLAR altında bildir. Görev o dosya olmadan yapılamıyorsa DURUM: BAŞARISIZ dön.
3. Kaynak, DOI, sayı, veri, alıntı ya da sonuç uydurma. Doğrulayamadığın hiçbir şeyi yazma. Bilmediğin alanı görev dosyasının söylediği ifadeyle, söylemiyorsa "bilinmiyor" ile doldur.
4. Kullanıcıya soru sorma ve alt ajan başlatma (Agent aracını kullanma). Karar gerekirse en temkinli savunulabilir seçeneği uygula ve kararı gerekçesiyle çıktı dosyanın sonundaki "Kararlar" başlığına (görev dosyası başka yer gösteriyorsa oraya) yaz.
5. Aynı hata aynı biçimde iki kez tekrarlanırsa üçüncü kez deneme; dur ve bildir.
6. Düz biçim kullan: renkli başlık, süslü tablo, emoji yok. Uzun tire (em dash) kullanma.
7. Komut satırından genel web sitelerine erişim kapalıdır; web için yalnız WebSearch ve WebFetch kullan. Paket kurmak için: `pip install --break-system-packages <paket>`.
8. Görev dosyasındaki sayısal sınırlara (arama sayısı, WebFetch sayısı, kelime, deneme sayısı) uy. Sınır dolarsa dur ve kalan işi SORUNLAR altında yaz.
9. Dönüş mesajın en fazla 150 kelime olsun ve tam olarak şu biçimi izlesin:

```
DURUM: TAMAM | KISMEN | BAŞARISIZ
YAZILAN DOSYALAR: <yol listesi>
ÖZET: <en çok 5 madde, her biri tek cümle>
SORUNLAR: <yoksa "yok">
EDİTÖRDEN BEKLENEN KARAR: <yoksa "yok">
```

Görev dosyasında "DÖNÜŞTE AYRICA" bölümü varsa o bilgiler ÖZET maddelerine eklenir.

## Ortak dosya biçimleri

Literatür matrisi, aday ve parça dosyaları (başlık satırı aynen):

```
anahtar,yazarlar,yil,baslik,dergi,doi,tur,yontem,veri,temel_bulgu,sinirlilik,alt_konu,kanit_duzeyi,dogrulama_durumu,not
```

Aday ve parça dosyalarında bu başlığın sonuna `kaynak_adresi,iddia_no` sütunları eklenir.
tur: makale, derleme, bildiri, kitap, onbaski, veri, tez.
kanit_duzeyi: T tam metin okundu, O özetten doğrulandı, M yalnız üst veri görüldü.
dogrulama_durumu: DOĞRULANDI, DÜZELTİLDİ, BEKLEMEDE, DOĞRULANAMADI, GERİ ÇEKİLMİŞ (aday dosyalarında boş bırakılır).
anahtar: ilk yazar soyadı (küçük harf, Türkçe karakterler ASCII karşılığıyla) + yıl + başlığın ilk anlamlı kelimesi küçük harf. Örnek: chen2016xgboost.

sayilar.csv (başlık satırı aynen):

```
id,deger,birim,aciklama,uretici_betik,tablo_sekil
```

Kimlikler S001'den başlar ve hiçbir zaman yeniden kullanılmaz. Örnek: `S012,0.874,-,XGBoost test R2,kod/03_model.py,Tablo 3`

Taslak metin yer tutucuları: atıf `[@anahtar]`; şekil `[ŞEKİL n: 04_analiz/sekiller/sekiln.png]` ve altında başlığı; tablo `[TABLO n: 04_analiz/tablolar/tablon.csv]` ve üstünde başlığı.
