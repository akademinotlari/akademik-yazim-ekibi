# Son kontrol listesi (20 madde)

"Uygulayan" sütunu: M = Doğrulayıcı Mekanik (haiku), İ = Doğrulayıcı İçerik (sonnet). Her doğrulayıcı yalnız kendi maddelerini uygular ve hiçbir maddeyi atlamaz; uygulanamayan madde İLGİSİZ ve gerekçesiyle yazılır.

| No | Uygulayan | Madde | Başarısızlık etiketi |
|---|---|---|---|
| 1 | M | Metindeki bütün atıflar çıkarıldı ve tekil anahtar listesi oluşturuldu (mekanik_kontrol.py). | [YAZIM] |
| 2 | M | Metinde atıf yapılan her anahtar kaynakçada var. | [YAZIM] |
| 3 | M | Kaynakçadaki her kayıt metinde en az bir kez anılıyor. | [YAZIM] |
| 4 | M | Her kaynakça kaydının 02_dogrulama_kaydi.csv'de DOĞRULANDI ya da DÜZELTİLDİ satırı var. | [LİTERATÜR] |
| 5 | M | Kaynakçadaki DOI'lerin tamamı WebFetch ile yeniden çözüldü (api.crossref.org/works/DOI; olmazsa doi.org); başlık ve ilk yazar eşleşiyor. BEKLEMEDE olanlar yeniden denendi. | [LİTERATÜR] |
| 6 | M | Geri çekilmiş kaynak yok (5. maddedeki kayıtta denetlendi). | [LİTERATÜR] |
| 7 | İ | İddia desteği: sayı, karşılaştırma ya da "ilk/tek/en" içeren her atıflı cümle ile geri kalan atıflardan kaynakça sırasına göre her beşincisi seçildi; her biri matristeki temel_bulgu, yontem, veri alanlarıyla ve gerekirse kaynağın özetiyle karşılaştırıldı. | [LİTERATÜR] |
| 8 | İ | Kanıt düzeyi M olan kaynağa özgül iddia atfedilmemiş. | [YAZIM] |
| 9 | M | Kaynakça biçimi hedef derginin biçimine uygun ve kendi içinde tutarlı (07_teslim/ana_metin.docx üzerinde). | [BİÇİM] |
| 10 | M | Özet, Bulgular ve Sonuç'taki her analiz sayısı sayilar.csv ya da tablolarla aynı (mekanik_kontrol.py). | [YAZIM] |
| 11 | M | Özetteki ve Sonuç'taki sayılar Bulgular'daki sayılarla aynı (mekanik_kontrol.py). | [YAZIM] |
| 12 | İ | Örneklem büyüklükleri, yüzdeler ve toplamlar tutarlı (alt grupların toplamı genel toplamı veriyor, yüzdeler 100'e tamamlanıyor, metin ile tablo aynı n değerini veriyor). | [ANALİZ] ya da [YAZIM] |
| 13 | M | Şekil ve tablo numaraları ilk atıf sırasına göre ardışık; her biri kendisinden önce anılıyor; anılan her numaranın karşılığı var (mekanik_kontrol.py). | [YAZIM] |
| 14 | İ | Kısaltmalar ilk kullanımda açılmış; aynı kavram için tek terim; birimler SI ve tutarlı; ondalık ayracı dile uygun. | [YAZIM] |
| 15 | M | Başlık, yazar bilgisi ve anahtar kelimeler bütün teslim dosyalarında aynı. | [BİÇİM] |
| 16 | M | Kelime sınırları (ana metin, özet, highlights karakter sınırı, anahtar kelime sayısı) brief'teki değerlere uygun. | [YAZIM] |
| 17 | M | Zorunlu beyanlar var: çıkar çatışması, finansman, veri erişilebilirliği, CRediT, yapay zekâ kullanım beyanı, gerekiyorsa etik onay. | [YAZIM] |
| 18 | M | Çift kör hakemlikte ana metinde yazar adı, kurum, teşekkür, proje numarası ve kendini ele veren öz atıf ifadesi ("önceki çalışmamızda", "our previous work", "in our earlier") yok. | [BİÇİM] |
| 19 | M | Üslup taraması (uslup_tarama.py --son): bulgu yok. Kalan her bulgu yeriyle listelendi. | [YAZIM] |
| 20 | M | Teslim paketindeki her dosya açılıyor; yer tutucu kalmamış; şekiller en az 300 dpi. | [BİÇİM] |

Rapor biçimi (her doğrulayıcı için):

```
<no> | GEÇTİ / BAŞARISIZ / İLGİSİZ | <bulgu sayısı> | <etiket>
```

BAŞARISIZ maddelerin altında her bulgu: yer (dosya ve alt başlık), sorun, önerilen düzeltme. Sonda: GEÇTİ ve BAŞARISIZ sayıları ve "gönderime hazır: evet/hayır" (tek BAŞARISIZ varsa hayır).
