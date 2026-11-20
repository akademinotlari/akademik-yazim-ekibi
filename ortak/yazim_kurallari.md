# Yazım kuralları

Yazım sırası: Materyal ve Yöntem, Bulgular, Sonuç, Tartışma, Giriş, Özet.

1. Giriş. Huni yapısı: genel problem ve önemi, alanın mevcut durumu, ilgili çalışmalar ve sınırlılıkları, net boşluk, çalışmanın amacı, katkıları ve makalenin düzeni. Her iddia doğru kaynağa atıflanır.
2. Materyal ve Yöntem. Her yöntem önce tanımlanır ve kaynak gösterilir, sonra uzman olmayan bir okurun anlayacağı biçimde nasıl çalıştığı açıklanır (örneğin XGBoost, SHAP, CTGAN nedir, nasıl işler), ardından bu çalışmada hangi girdilerle, hangi ayarlarla nasıl uygulandığı yazılır. Veri seti, kaynağı, ön işleme ve değerlendirme metrikleri ayrıntılı verilir.
3. Bulgular. Her şekil ve tablo için sıra sabittir: metinde önce şekle/tabloya atıf, sonra şekil/tablo, sonra yorumu. Atıfsız şekil veya tablo bırakılmaz.
4. Tartışma. Genelden özele ilerler, bulgular literatürle karşılaştırılır (benzerlik ve farklılıkların nedenleriyle), sınırlılıklar açıkça yazılır.
5. Sonuç. Genelden özele özetler, uygulamaya ve gelecek çalışmalara yönelik önerilerle biter.
6. Özet. En son yazılır; amaç, yöntem, temel nicel bulgular ve katkıyı içerir, dergi kelime sınırına uyar.
7. Dil ve üslup. Akademik kayıt kullanılır, rapor dili veya sohbet dili kullanılmaz. Türkçe ve İngilizce metinlerde human skill'inin kuralları zorunludur. Kesin yasaklar: uzun tire (em dash), "Sonuç olarak" ile biten kapanışlar, tutarsız şapka kullanımı, üçlü sıralama alışkanlığı, art arda -maktadır/-mektedir zincirleri, çeviri kokan kalıplar, abartılı önem vurgusu, "bu bölümde ... ele alınacaktır" türü yönlendirme cümleleri, kalın etiketli madde listeleri.

## Uygulama netleştirmeleri

Bu maddeler yukarıdaki kuralları değiştirmez; nasıl uygulanacaklarını sabitler.

- Türkçe akademik metinde geçmiş zaman "-mıştır/-miştir" biçimiyle yazılır (yapılmıştır, kullanılmıştır, bulunmuştur); "-dı/-di" biçimi (yapıldı, kullanıldı) kullanılmaz. Bu kural -maktadır zinciri yasağıyla birlikte uygulanır: art arda üç cümle aynı ekle bitmez, zaman ve kip çeşitlenir (geniş zaman, -mıştır, ad cümlesi).
- Taslakta atıf `[@anahtar]` biçiminde yazılır; dergi biçimine biçimlendirme aşamasında çevrilir. Anahtar kaynaklar.bib içinde yoksa atıf yazılmaz.
- Şekil yeri `[ŞEKİL n: 04_analiz/sekiller/sekiln.png]` satırı ve altında başlığıyla; tablo yeri `[TABLO n: 04_analiz/tablolar/tablon.csv]` satırı ve üstünde başlığıyla gösterilir. Numaralar ilk atıf sırasına göre verilir.
- Yöntem tanımındaki kaynak, yöntemi ilk öneren özgün çalışmadır (ikincil anlatım değil).
- Giriş'teki "makalenin düzeni" cümlesi yalnız hedef dergi bunu istiyorsa ya da metin 8000 kelimeyi aşıyorsa yazılır ve tek cümleyi geçmez. Madde 7'deki yönlendirme cümlesi yasağı diğer bütün bölümlerde geçerlidir.
- Bulgular bölümünde yorum, sayının ne olduğunu ve neyle karşılaştırıldığını söyler; nedensel açıklama ve literatür karşılaştırması Tartışma'ya bırakılır.
- Sınırlılıklar Tartışma'nın son alt bölümüdür ve en az veri kapsamı, yöntem varsayımları ve genellenebilirliği ele alır.
- Ondalık ayracı Türkçe metinde virgül, İngilizce metinde noktadır. Sayı aralığında en dash yerine "1 ile 3 arası" ya da "1 to 3" yazılır.
- Bulguların gücünü aşan ifade kullanılmaz: korelasyon için nedensellik dili, tek veri seti için genelleme, istatistiksel olarak anlamlı olmayan fark için "üstün" yazılmaz.
- Kısaltma ilk geçtiği yerde açılır; aynı kavram metin boyunca aynı terimle anılır (çalışma/araştırma/inceleme arasında gidip gelinmez).

## Kelime hedefleri

Derginin toplam sınırı L ise: Giriş %15-20, Materyal ve Yöntem %25-30, Bulgular %25-30, Tartışma %15-20, Sonuç %5-8. Özet derginin özet sınırı, belirtilmemişse 250 kelime. L belirtilmemişse makale ve kitap bölümü için 7000, bildiri için 4000 kelime alınır.
