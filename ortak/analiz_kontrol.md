# Analiz kontrol listeleri

Analiz ajanı bu listeleri uygular, Tekrarlanabilirlik Denetçisi kanıtların varlığını, Hakem 1 içeriğini denetler. 9.1 her çalışmada zorunludur; 9.2-9.5 arası 03_bosluk_yontem.md içindeki "Yöntem türleri" başlığına göre zorunludur. Bir çalışma birden çok türe giriyorsa (örneğin trafik tahmini hem 9.2 hem 9.3) hepsi uygulanır. Maddeler kontrol_listesi.md dosyasında numarasıyla anılır ve UYGUN / UYGUN DEĞİL / İLGİSİZ olarak işaretlenir. UYGUN için kanıt (betik adı ve satır ya da log dosyası), İLGİSİZ için tek cümle gerekçe zorunludur.

## 9.1 Genel (her çalışmada)

G1. Ham veri değiştirilmedi; her dönüşüm betikle yapıldı ve ham veriden yeniden üretilebiliyor.
G2. Veri kaynağı, erişim tarihi, lisansı, dönemi ve gözlem sayısı kayıtlı.
G3. Bütün rastgelelik kaynaklarında tohum sabit (numpy, random, model, bölme, derin öğrenme çatısı).
G4. Python ve paket sürümleri requirements.txt içinde sürüm numarasıyla.
G5. calistir.sh temiz durumdan çalışıyor ve sayilar.csv değerleri yeniden aynı çıkıyor (göreli fark 1e-6 altında).
G6. Eksik veri oranı değişken bazında raporlandı; eksiklik mekanizması (rastgele mi, sensör arızası gibi sistematik mi) tartışıldı; doldurma yöntemi gerekçeli.
G7. Aykırı değer kuralı sonuç görülmeden önce tanımlandı; çıkarılan gözlem sayısı raporlandı; aykırılar dahil duyarlılık analizi yapıldı.
G8. Birimler, zaman dilimi ve koordinat sistemi tutarlı ve belgeli.
G9. Birincil metrik ve birincil analiz 03_bosluk_yontem.md ile aynı; sapmalar "keşifsel" olarak etiketli.
G10. Her nokta tahmini için belirsizlik ölçüsü var (güven aralığı, standart sapma ya da tahmin aralığı) ve nasıl hesaplandığı yazılı.
G11. Yapılan bütün analizler raporlandı; yalnız olumlu çıkanlar seçilmedi.
G12. Her şekil ve tablo üretici betiğiyle eşleşiyor; metne girecek her sayı sayilar.csv içinde.
G13. Örneklem büyüklüğünün amaca yeterliliği tartışıldı (ML'de gözlem/öznitelik oranı, testlerde güç).
G14. Kişisel veri ya da insan katılımcı varsa etik izin ve anonimleştirme durumu kayıtlı.

## 9.2 Makine öğrenmesi

Veri sızıntısı:
M1. Eğitim-test bölmesi bütün ön işlemelerden önce yapıldı.
M2. Ölçekleme, kodlama, eksik doldurma, öznitelik seçimi ve boyut indirgeme yalnız eğitim verisinde öğrenildi (sklearn Pipeline ya da eşdeğeriyle çapraz doğrulamanın içinde).
M3. Hedef değişkenden ya da sonuçtan sonra oluşan bilgiyi taşıyan öznitelik yok (örnek: kaza şiddeti tahmininde hastanede kalış süresi). Her özniteliğin tahmin anında bilinebilir olduğu tek tek doğrulandı.
M4. Grup sızıntısı yok: aynı yol kesimi, sensör, sürücü, kaza ya da güzergâha ait gözlemler hem eğitimde hem testte yer almıyor (GroupKFold ya da grup bazlı bölme). Yinelenen ve neredeyse yinelenen satırlar bölmeden önce ayıklandı.
M5. Aşırı örnekleme ve sentetik veri (SMOTE, CTGAN ve benzerleri) yalnız eğitim katmanında üretildi; doğrulama ve test kümeleri yalnız gerçek gözlemlerden oluşuyor. Sentetik verinin gerçek veriye benzerliği (dağılım karşılaştırması, TSTR gibi) raporlandı.
M6. Zaman sıralı veride gelecekten bilgi sızmıyor (9.3 de uygulanır).
M7. Sızıntı duman testi yapıldı: beklenmedik ölçüde yüksek başarı (örneğin R2 ya da AUC 0,99 üstü) varsa en önemli öznitelikler tek tek incelendi ve sonuç loga yazıldı.

Doğrulama kurgusu:
M8. Kurgu veri yapısına uygun: bağımsız gözlemde katmanlı k-kat (k=5 ya da 10), gruplu veride grup bazlı, zamansal veride zamana göre, mekânsal veride mekânsal blok.
M9. Hiperparametre ayarı test kümesine dokunmadan yapıldı: iç içe çapraz doğrulama ya da ayrı doğrulama kümesi. Arama uzayı, yöntemi ve deneme sayısı tabloda.
M10. Test kümesi yalnız bir kez, son değerlendirmede kullanıldı.
M11. Temel modeller var: en az bir naif temel ve bir basit doğrusal model. Karşılaştırma modelleri de aynı özenle ayarlandı (aynı arama bütçesi).
M12. Eğitim ve doğrulama başarımı birlikte raporlandı; aşırı öğrenme farkı tartışıldı.

Metrik ve belirsizlik:
M13. Metrikler probleme uygun: regresyonda MAE, RMSE ve R2 (MAPE yalnız hedef sıfıra yakın değilse); dengesiz sınıflamada doğruluk tek başına verilmez, sınıf bazında kesinlik, duyarlılık, F1, ayrıca MCC ve PR-AUC verilir; karışıklık matrisi eklenir.
M14. Belirsizlik: en az 5 tohum ya da tekrarlı çapraz doğrulama ile ortalama ± standart sapma; test metriği için en az 1000 yinelemeli bootstrap %95 güven aralığı.
M15. Modeller arası fark istatistiksel olarak sınandı: aynı katmanlarda eşleştirilmiş Wilcoxon işaretli sıra testi ya da düzeltilmiş yeniden örneklemeli t testi (Nadeau-Bengio); AUC için DeLong; çok veri setli karşılaştırmada Friedman ve ardından Nemenyi. Güven aralıkları örtüşen fark için "üstün" denmez.
M16. Olasılık çıktısı kullanılıyorsa kalibrasyon raporlandı (Brier skoru, güvenilirlik eğrisi).

Yorumlanabilirlik ve sağlamlık:
M17. SHAP ya da öznitelik önemi eğitimde görülmemiş veride hesaplandı; birden çok tohumda sıralamanın kararlılığı denetlendi; yüksek korelasyonlu öznitelikler (|r| > 0,8) belirtilip yorum buna göre sınırlandı. SHAP değerleri nedensellik olarak yorumlanmadı.
M18. Ablasyon ya da duyarlılık analizi: önerilen bileşenlerin her birinin katkısı ayrı gösterildi.
M19. Hata analizi: modelin en çok yanıldığı alt gruplar (yol tipi, saat dilimi, sınıf) incelendi.
M20. Hesaplama maliyeti (eğitim süresi, donanım) raporlandı.

## 9.3 Zaman serisi ve tahmin

Z1. Bölme kronolojik; karıştırma (shuffle) yok. Test dönemi eğitim döneminden sonra.
Z2. Çapraz doğrulama kayan başlangıçlı ya da genişleyen pencereli (TimeSeriesSplit gibi); eğitim ile doğrulama arasında en az tahmin ufku kadar boşluk bırakıldı.
Z3. Gecikme ve kayan pencere öznitelikleri yalnız geçmiş değerlerden üretildi (önce shift, sonra rolling). Ortalanmış pencere, geriye doğru doldurma (bfill) ve iki yönlü enterpolasyon kullanılmadı.
Z4. Ölçekleme, ayrıştırma ve gürültü giderme (dalgacık, EMD, VMD, STL) bütün seriye birden uygulanmadı; yalnız eğitim döneminde ya da her tahmin anında yalnız geçmiş veriyle uygulandı. Bütün seriye uygulanan ayrıştırma sızıntıdır.
Z5. Bölme sınırını aşan pencereler (girdi eğitimde, hedef testte olan örnekler) atıldı.
Z6. Tahmin ufku, girdi penceresi uzunluğu ve çok adımlı strateji (doğrudan, özyinelemeli, çok çıktılı) açıkça tanımlandı; sonuçlar ufuk bazında ayrı raporlandı.
Z7. Temel modeller: naif (son değer), mevsimsel naif (bir gün ve bir hafta önce), tarihsel ortalama; ayrıca en az bir klasik istatistiksel model (ARIMA/SARIMA ya da ETS).
Z8. Metrikler: MAE ve RMSE; MAPE yalnız sıfıra yakın değer yoksa (varsa sMAPE ya da eşik üstü maskeli MAPE, eşik raporlanır); ölçekten bağımsız karşılaştırma için MASE.
Z9. Modeller arası fark Diebold-Mariano testiyle (küçük örneklemde Harvey düzeltmesiyle) sınandı.
Z10. Tahmin aralığı verildi (kantil regresyon, konformal tahmin ya da bootstrap) ve kapsama oranı test döneminde ölçüldü.
Z11. İstatistiksel model kullanılıyorsa durağanlık (ADF ve KPSS birlikte) ve artık tanılaması (Ljung-Box, artıkların ACF'si) raporlandı.
Z12. Eksik zaman damgaları, sensör arızaları ve sıfır okumaları belgeli; doldurma yalnız geçmiş bilgiyle yapıldı; arızalı sensörlerin eleme kuralı önceden tanımlı.
Z13. Test dönemi en az bir tam haftalık döngüyü (tercihen birkaç haftayı) kapsıyor; tatil, olay ve olağandışı dönemler belirtildi.
Z14. Zaman dilimi ve yaz saati geçişleri kontrol edildi; yinelenen ya da atlanan saat yok.
Z15. Mekân-zamansal ağ modellerinde (sensör ağı): komşuluk matrisi yalnız eğitim dönemi verisinden ya da sabit yol ağı mesafesinden kuruldu; sensör bazlı normalizasyon eğitim dönemi istatistikleriyle yapıldı; literatürle karşılaştırma aynı veri bölmesi ve aynı ufuklarla yapıldı.
Z16. Kavram kayması: test dönemi içinde başarımın zamanla değişimi çizildi.

## 9.4 Mekânsal analiz

K1. Her katmanın koordinat referans sistemi kayıtlı; mesafe ve alan hesapları izdüşümlü (metrik) bir sistemde yapıldı (Türkiye için bölgeye uygun UTM dilimi ya da TUREF/TM dilimi; EPSG kodu yazıldı). Coğrafi koordinatta (derece) mesafe hesabı yapılmadı.
K2. Geometri geçerliliği, yinelenen geometri ve topoloji hataları denetlendi ve düzeltme sayıları raporlandı.
K3. Veri kaynaklarının tarihi, ölçeği ya da çözünürlüğü ve konum doğruluğu yazıldı; OpenStreetMap kullanılıyorsa çalışma alanındaki tamlığı tartışıldı.
K4. Hedef değişkende ve model artıklarında mekânsal otokorelasyon sınandı (Global Moran I; yerel örüntü için LISA). Artıklarda anlamlı otokorelasyon varsa model mekânsal yapıyı kapsayacak biçimde değiştirildi ya da sınırlılık olarak yazıldı.
K5. Mekânsal ağırlık matrisinin tanımı (k en yakın komşu, mesafe bandı, komşuluk türü) gerekçeli; en az bir alternatif tanımla duyarlılık analizi yapıldı.
K6. Tahmin modeli varsa doğrulama mekânsal: mekânsal blok çapraz doğrulama ya da tampon bölgeli birini dışarıda bırakma. Rastgele çapraz doğrulama yalnız karşılaştırma için verilir, çünkü mekânsal bağımlılık nedeniyle başarımı olduğundan yüksek gösterir.
K7. Değiştirilebilir alan birimi sorunu (MAUP): sonuçların en az bir farklı ölçek ya da bölgelemeyle değişip değişmediği gösterildi.
K8. Kenar etkisi: çalışma alanı sınırındaki birimler için tampon ya da düzeltme uygulandı veya sınırlılık yazıldı.
K9. Yol ağına bağlı olaylarda (kaza, erişilebilirlik, hizmet alanı) Öklid mesafesi değil ağ mesafesi kullanıldı; ağın bağlantılılığı, yönlülüğü ve empedans tanımı (süre, uzunluk) denetlendi.
K10. Çekirdek yoğunluk tahmininde bant genişliği ve hücre boyutu seçim yöntemi yazıldı; farklı bant genişliğiyle duyarlılık gösterildi.
K11. Sıcak nokta analizinde (Getis-Ord Gi*, LISA) çoklu karşılaştırma düzeltmesi (FDR) uygulandı; mesafe eşiğinin seçimi gerekçeli.
K12. Mekânsal regresyonda model seçimi sınamaya dayalı: OLS artıklarında Moran I, Lagrange çarpanı testleriyle mekânsal gecikme ya da hata modeli seçimi; GWR/MGWR'de bant genişliği AICc ile, yerel çoklu doğrusallık denetimiyle.
K13. Çok ölçütlü karar analizinde (AHP ve benzerleri): tutarlılık oranı 0,10'un altında; ölçüt ağırlıkları için duyarlılık analizi (ağırlıkları ±%10-20 değiştirerek ya da Monte Carlo) yapıldı; sonuç bağımsız veriyle (mevcut tesisler, gözlenen olaylar) doğrulandı.
K14. Raster işlemlerinde çözünürlük, yeniden örnekleme yöntemi (kategorik veride en yakın komşu, sürekli veride bilineer ya da kübik) ve hizalama belgeli.
K15. Girdi belirsizliğinin sonuca yayılımı değerlendirildi (en azından duyarlılık analiziyle).
K16. Haritalarda ölçek çubuğu, kuzey oku, lejant, koordinat sistemi notu ve renk körü dostu palet var; sınıflama yöntemi (doğal kırılma, kantil, eşit aralık) yazıldı.

## 9.5 İstatistiksel testler ve çıkarımsal modeller

T1. Hipotezler, birincil sonuç değişkeni ve anlamlılık düzeyi (varsayılan 0,05, çift yönlü) veriye bakılmadan önce tanımlandı.
T2. Test seçimi değişken türüne ve tasarıma uygun (bağımsız ya da eşleştirilmiş; iki ya da çok grup; sürekli, sıralı, kategorik, sayım).
T3. Varsayımlar sınandı ve raporlandı: normallik (Shapiro-Wilk ve Q-Q grafiği), varyans homojenliği (Levene), gözlemlerin bağımsızlığı, tekrarlı ölçümde küresellik. Varsayım sağlanmıyorsa parametrik olmayan karşılığı ya da sağlam yöntem kullanıldı.
T4. Her test için etki büyüklüğü ve %95 güven aralığı verildi (Cohen d ya da Hedges g, eta kare, r, odds oranı, Cramér V). Yalnız p değeri raporlanmadı.
T5. p değerleri tam yazıldı (p = 0,032; yalnız çok küçükse p < 0,001); test istatistiği ve serbestlik derecesiyle birlikte.
T6. Çoklu karşılaştırmada düzeltme yapıldı (aile bazında Holm; çok sayıda keşifsel testte Benjamini-Hochberg). Yapılan test sayısı açıkça yazıldı.
T7. Güç: ön güç analizi ya da saptanabilir en küçük etki için duyarlılık analizi verildi. Gözlenen etkiden geriye dönük güç hesabı yapılmadı.
T8. Anlamlı çıkmayan sonuç "etki yok" diye yorumlanmadı; güven aralığıyla birlikte "saptanamadı" olarak yazıldı.
T9. Regresyon tanılaması: çoklu doğrusallık (VIF; 5 üstü incelenir, 10 üstü sorunlu), artık grafikleri, değişen varyans (Breusch-Pagan; varsa sağlam standart hata), etkili gözlemler (Cook mesafesi), doğrusallık.
T10. Kümelenmiş ya da tekrarlı veri (aynı sürücü, aynı kesim, aynı gün) için karma etkili model ya da küme sağlam standart hata kullanıldı.
T11. Sayım verisinde (kaza sıklığı gibi) Poisson varsayımı sınandı; aşırı yayılım varsa negatif binom; sıfır fazlalığı varsa sıfır yığılmalı model sınandı; maruziyet (trafik hacmi, kesim uzunluğu) ofset olarak alındı.
T12. Sıralı sonuç değişkeninde (yaralanma şiddeti gibi) sıralı lojit ya da probit kullanıldı ve orantılı odds varsayımı sınandı; sağlanmıyorsa kısmi orantılı ya da çok terimli model.
T13. Eksik veri: eksiklik mekanizması tartışıldı; gerekiyorsa tam gözlem analizi yerine çoklu atama; iki sonuç karşılaştırıldı.
T14. Anket verisinde güvenirlik (Cronbach alfa ve McDonald omega) ve geçerlik (doğrulayıcı faktör analizi, AVE, HTMT) raporlandı; ortak yöntem yanlılığı ele alındı.
T15. Yapısal eşitlik modelinde uyum indeksleri birlikte verildi (CFI, TLI, RMSEA ve güven aralığı, SRMR); model değişiklikleri kuramsal gerekçeyle yapıldı.
T16. Meta-analizde heterojenlik (I kare, tau kare, tahmin aralığı), yayın yanlılığı (huni grafiği, Egger) ve duyarlılık analizi verildi.
T17. İstatistiksel anlamlılık ile uygulamadaki önem ayrı tartışıldı; gözlemsel veride nedensellik dili kullanılmadı.
