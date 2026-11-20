# Önce/sonra örnekleri

## Örnek 1: İngilizce abstract (uydurma örnek metin)

Bu örnekteki çalışma ve sayılar gösterim amacıyla uydurulmuştur.

Önce:
Bus dwell time prediction is commonly evaluated using average error over entire test periods. This study investigates what lies behind that error. Using automatic passenger counter data from 214 stops on 11 urban routes, four predictors ranging from linear regression to a gradient-boosted ensemble, and two prediction horizons, the boarding surge at school closing times — the 20-minute window in which boardings triple — accounts for most of the residual error in every configuration, holding stop by stop rather than only on average. Removing these windows lowers mean absolute error by 38–46%, and no predictor examined captured the surge. Two further findings follow. Larger models do not reduce surge error, being no better than the linear baseline at the 5-minute horizon. Error during rain is 1.8 to 2.6 times the dry-weather average under every threshold tested.

Sonra:
Bus dwell time predictions are usually judged by their average error over a whole test period. We examine what that error is made of. We used automatic passenger counter data from 214 stops on 11 urban routes and compared four predictors, from linear regression to a gradient-boosted ensemble, at two horizons. In every configuration, most of the residual error comes from the boarding surge at school closing times, a 20-minute window in which boardings triple. The pattern holds at each stop, not only in the network average. Removing these windows lowers mean absolute error by 38 to 46%, and none of the predictors captured the surge. Larger models do not reduce surge error: at the 5-minute horizon they are no better than the linear baseline. During rain, error is 1.8 to 2.6 times the dry-weather average under every threshold we tested.

Temizlenenler:
- Uzun tire: "the boarding surge at school closing times — the 20-minute window... —" tanımı virgülle bağlanan ayrı bir ifadeye taşındı.
- Olumsuz paralellik: "stop by stop rather than only on average" ayrı cümleye açıldı.
- Duyurma: "Two further findings follow." silindi.
- "-ing" eklemesi: "being no better than..." iki noktayla bağlı tam cümle oldu.
- 50 kelimeyi aşan cümle bölündü; cümle uzunlukları çeşitlendi.
- En dash aralık: "38–46%" yerine "38 to 46%", diğer aralıkla tutarlı.
- "This study investigates" yerine "We examine" (dergi istemezse geri alınır).

Dokunulmayanlar: "gradient-boosted ensemble", "automatic passenger counter" teknik terim. Hiçbir sayı ve iddia değişmedi.

Ders: Metin zaten büyük ölçüde temizdi. Düzeltme dar tutuldu; yalnızca işaretli yerler değişti.

## Örnek 2: Türkçe giriş paragrafı

Önce:
Günümüzde kentsel ulaşım sistemleri, hızla artan nüfus ve araç sahipliği nedeniyle kritik bir dönüm noktasındadır. Bu bağlamda, trafik tahmini akıllı ulaşım sistemlerinin temel taşlarından biri olarak hizmet etmekte ve karar vericilere paha biçilmez içgörüler sunmaktadır. Derin öğrenme yöntemleri — özellikle LSTM ve Transformer tabanlı modeller — bu alanda çığır açan sonuçlar elde etmiştir. Bununla birlikte, bu modeller sadece yüksek hesaplama maliyeti değil, aynı zamanda yorumlanabilirlik sorunu da taşımaktadır. Sonuç olarak, doğru, verimli ve yorumlanabilir tahmin yöntemlerine duyulan ihtiyaç giderek artan bir önem kazanmaktadır.

Sonra:
Kentlerde nüfus ve araç sayısı arttıkça yol ağlarının kapasitesi daha sık aşılıyor. Kısa vadeli trafik tahmini, sinyal kontrolü ve yolcu bilgilendirmesi gibi uygulamalarda bu sorunu yönetmenin araçlarından biridir. Son yıllarda LSTM ve Transformer tabanlı modeller bu alanda klasik istatistiksel yöntemlerden daha düşük hata vermiştir (Kaynak, yıl). Ancak bu modellerin eğitimi pahalıdır ve bir tahminin neden o değeri aldığını açıklamak zordur. Bu çalışmada, hesaplama maliyeti daha düşük ve çıktıları yorumlanabilen bir yaklaşımın aynı doğruluğa ulaşıp ulaşamayacağını sınıyoruz.

Temizlenenler:
- Önem şişirme: "kritik bir dönüm noktasındadır", "giderek artan bir önem kazanmaktadır" kaldırıldı; yerine somut sorun kondu.
- Calque: "temel taşlarından biri olarak hizmet etmekte", "paha biçilmez içgörüler" kaldırıldı.
- Uzun tire: ara söz kaldırıldı, modeller doğrudan özne yapıldı.
- Tanıtım dili: "çığır açan sonuçlar" yerine ölçülebilir iddia ve kaynak yeri.
- Olumsuz paralellik: "sadece ... değil, aynı zamanda ..." iki düz cümleye bölündü.
- Üçlü: "doğru, verimli ve yorumlanabilir" kaldırıldı; araştırma sorusu doğrudan yazıldı.
- "Sonuç olarak" kapanışı ve "Bu bağlamda" açılışı kaldırıldı.
- "-maktadır" zinciri kırıldı: -ıyor, -dir, -miştir, -dır, -uyoruz.

Not: "(Kaynak, yıl)" bir yer tutucudur ve yazar tarafından doldurulmalıdır. Kaynağı uydurmam; kullanıcıya bunu açıkça belirtirim.

## Örnek 3: Hakem yanıtı (İngilizce)

Önce:
We are deeply grateful to the reviewer for this insightful and invaluable comment, which has significantly enhanced the quality of our manuscript. In response, we have carefully revised Section 3 to delve deeper into the intricate interplay between the prediction horizon and the boarding surge — a crucial aspect of our analysis. This revision not only clarifies our methodology but also underscores the robustness of our findings.

Sonra:
We thank the reviewer for this comment. We have revised Section 3 (lines 212-240) to show how surge error changes with the prediction horizon, and added Figure 5, which plots surge error for each stop at the 5- and 15-minute horizons. The revised text also states that surge windows were identified on the test period only.

Temizlenenler:
- Dalkavukça ton: "deeply grateful", "insightful and invaluable", "significantly enhanced" kaldırıldı.
- Yapay zekâ kelimeleri: delve, intricate, interplay, crucial, underscores.
- Uzun tire ve olumsuz paralellik ("not only... but also").
- Belirsiz "carefully revised" yerine satır numarası, şekil ve yöntem bilgisi. Hakem için asıl önemli olan budur.

## Örnek 4: Kısa e-posta (Türkçe)

Önce:
Sayın Hocam,
Umarım bu e-posta sizi iyi bulur. Sizinle, ortak yürüttüğümüz projemiz kapsamında kritik öneme sahip bir konuyu paylaşmak istiyorum. Bu bağlamda, veri toplama sürecinin zamanında, eksiksiz ve verimli bir şekilde tamamlanabilmesi için desteğinize ihtiyaç duymaktayım. Değerli geri dönüşlerinizi sabırsızlıkla bekliyorum.

Sonra:
Sayın Hocam,
Proje kapsamındaki saha ölçümleri için 20 Ekim haftasında iki gün sizin laboratuvarınızdaki ölçüm cihazını kullanmamız gerekiyor. Uygun olduğunuz günleri iletebilir misiniz?
Saygılarımla,

Temizlenenler:
- Kalıp açılış ve kapanış ("Umarım bu e-posta sizi iyi bulur", "sabırsızlıkla bekliyorum").
- Önem şişirme ve "Bu bağlamda".
- Üçlü: "zamanında, eksiksiz ve verimli".
- Belirsiz istek yerine somut tarih ve soru. Tarih ve cihaz bilgisi yazar tarafından doğrulanmalı.
