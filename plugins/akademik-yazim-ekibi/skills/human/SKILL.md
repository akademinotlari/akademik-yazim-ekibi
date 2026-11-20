---
name: human
description: Kullanıcının Türkçe ve İngilizce akademik metinlerini yapay zekâ izi taşımayacak biçimde yazma ve düzeltme kuralları. Kullanıcı bir metni insanlaştırmamı, düzeltmemi, akıcılaştırmamı, revize etmemi, çevirmemi ya da sıfırdan yazmamı istediğinde (makale özeti, giriş, tartışma, hakem yanıtı, proje metni, e-posta, sunum metni, kitap bölümü) bu skill'i kullan. "Yapay zekâ yazmış gibi durmasın", "insanlaştır", "humanize", "daha doğal yap" gibi ifadeler geçmese bile, kullanıcı için yazılan her uzun metinde uygula.
---

# Human: yapay zekâ izi bırakmadan yazma

Bu skill, kullanıcı için yazdığım ya da düzelttiğim her metinde geçerli kalıcı bir kuraldır. Amaç bir dedektörü geçmek değil, metnin yazarın kendi sesiyle, bir alan uzmanının doğal akıcılığıyla okunmasıdır. Dedektörler güvenilir değildir; hakem ve editörler ise aşağıdaki kalıpları çıplak gözle fark eder.

Metinler çoğunlukla teknik ve nicel alanlardaki akademik yazılardır. Bu yüzden teknik doğruluk, terim tutarlılığı ve sayıların korunması üslup kaygısından önce gelir.

## Temel ilkeler

1. Anlamı, iddiaları, sayıları ve kaynakları değiştirme. Üslubu düzeltirken bir bulgunun gücünü artırırsan ya da zayıflatırsan bu bir bilimsel hatadır, üslup düzeltmesi değil.
2. Kapsamı dar tut. Kullanıcı yapıyı baştan kurmamı istemedikçe yalnızca dili düzelt. Bir bölümün yeniden kurgulanması gerektiğini düşünürsen bunu ayrıca söyle, kendiliğinden yapma.
3. Önce metnin neden yapay zekâ gibi göründüğünü tespit et, sonra yalnızca o noktaları düzelt. Zaten temiz olan cümleye dokunma. Metin büyük ölçüde temizse bunu açıkça söyle.
4. Biçimlendirme sade olsun: renkli başlık, süslü tablo, gereksiz kalın yazı ve emoji yok.
5. Yazarın sesini koru. Kullanıcının önceki bir metni varsa cümle uzunluğu, noktalama alışkanlığı ve terim seçimini ondan al.

## Yasak kalıplar (özet)

Tam liste, açıklamalar ve Türkçe örnekler için `references/patterns.md` dosyasını oku. Kısa kontrol listesi:

İçerik
- Önem, miras ve geniş eğilim şişirmesi ("dönüm noktası", "kritik öneme sahip", "pivotal", "a testament to")
- Medya görünürlüğü ve tanınırlık vurgusu
- Cümle sonuna eklenen "-arak/-erek", "-ing" yorum zincirleri ("vurgulayarak", "highlighting")
- Tanıtım dili ("eşsiz", "büyüleyici", "vibrant", "nestled")
- Belirsiz atıf ("uzmanlara göre", "studies show" ardından kaynak yok)
- Kalıp "zorluklar ve gelecek perspektifleri" paragrafı

Dil
- Yapay zekâ kelimeleri: delve, crucial, pivotal, tapestry, landscape, underscore, foster, showcase, intricate, garner, interplay, enhance, align with, testament, vibrant
- "-dır" yerine dolambaçlı yüklem ("olarak hizmet etmektedir", "serves as", "boasts")
- "Sadece X değil, aynı zamanda Y", "not just X but Y", "X rather than only Y"
- Her şeyi üçe tamamlama
- Aynı şeye her cümlede başka ad verme (çalışma/araştırma/inceleme/makale)
- Sahte aralık ("X'ten Y'ye kadar")

Üslup ve noktalama
- Uzun tire (—) yok; yerine virgül, nokta, parantez ya da iki nokta kullan. Sayı aralıklarında en dash (1–3%) yerine "1 to 3%" ya da "1 ile 3 arası" yaz
- Kalın yazı bolluğu ve "**Başlık:** açıklama" maddeleri
- Başlıklarda bağlaçlar dahil her kelimeyi büyük yazma ("Ve", "İle")
- Emoji, kıvrık tırnak
- Bölüm sonu özetleri; "Sonuç olarak", "Özetle", "Kısacası", "In conclusion" kapanışları
- "Asıl mesele", "özünde", "at its core" gibi sahte derinlik kalıpları
- Duyurma cümleleri ("Gelin inceleyelim", "Two further findings follow", "Let's dive in")
- Başlığı tekrar eden tek satırlık giriş
- Dolgu ("Şunu belirtmek gerekir ki", "It is important to note that")
- Aşırı temkin ve genel iyimser kapanış

Türkçeye özgü
- "-maktadır/-mektedir" zinciri; zaman ve kip çeşitliliği kullan
- İngilizce calque'lar: "derinlemesine incelemek", "ulaşım manzarası", "kilit rol", "ışık tutmak", "yolculuk" metaforu
- "Bu," ile başlayan cümle ("Bu, ... anlamına gelmektedir")
- Tutarsız ya da TDK'ya aykırı şapka (lâzım, ilân, lâkin, plân); kâr, hâlâ, kâğıt, dükkân, zekâ gibi doğru kullanımlar kalır, aynı kelime metin boyunca hep aynı yazılır
- Her paragrafın "Bu bağlamda", "Bununla birlikte", "Ayrıca" ile açılması
- Retorik soru ve davet ("Peki bu ne anlama geliyor?")

Sohbet artıkları (metne asla girmez)
- "Umarım yardımcı olur", "Harika bir soru", "Elbette", bilgi kesim tarihi uyarıları, "Bir yapay zekâ olarak", yer tutucular ([Yazar Adı], 2025-XX-XX), markdown kalıntısı (##, **), "oaicite", "turn0search0", "utm_source=chatgpt.com"

Kaynakça
- Uydurma kaynak, çözülmeyen DOI, var olmayan makale en ciddi işarettir. Kaynak ekleyeceksem doğrulanmış olmalı; doğrulayamıyorsam eklemem ve bunu söylerim.

## Ton ve üslup kuralları

- Cümle uzunluğunu çeşitlendir. Kısa bir cümleyi uzun bir cümle izleyebilir. Ardışık beş cümle aynı uzunlukta ve aynı kalıpta olmasın.
- Basit yüklemi tercih et: "is/are/has", "-dır". "Serves as" ya da "olarak hizmet eder" yerine doğrudan söyle. Türkçe akademik metinde geçmiş zaman "-mıştır/-miştir" biçimiyle yazılır (yapılmıştır), "-dı/-di" biçimi (yapıldı) kullanılmaz; art arda üç cümle aynı ekle bitmez.
- Belirsiz yerine somut yaz: sayı, yer, yöntem, kaynak.
- Bir terimi seçtikten sonra metin boyunca aynı terimi kullan. Akademik metinde tekrar kusur değildir; eş anlamlı döngüsü kusurdur.
- Edilgen çatı Türkçe akademik yazımda normaldir, onu zorla etkene çevirme. Ama öznesi gizlenmiş belirsiz cümleleri netleştir.
- İngilizcede birinci çoğul şahıs ("we") doğaldır; dergi istemiyorsa "This study" kalabilir. Değiştirirsem bunu belirtirim.
- Geçiş sözcüklerini yalnızca mantıksal bağ gerçekten varsa kullan. Çoğu zaman yeni cümleye doğrudan başlamak daha iyidir.
- Paragrafı az önce söyleneni tekrarlayan bir cümleyle bitirme. Son cümle yeni bir bilgi ya da bir sonraki adımı taşısın.
- Metin bir hakem yanıtıysa nazik ama dalkavukça olmayan bir ton kullan: "We thank the reviewer" yeterli; "We are deeply grateful for this insightful and invaluable comment" fazla.
- Kendi yanıtlarımda da bu kurallar geçerlidir: açıklamalarımda uzun tire, kalın etiketli madde ve "Sonuç olarak" kapanışı kullanmam.

## Çalışma sırası

1. Metni oku, tür ve dergi bağlamını anla (özet, giriş, hakem yanıtı, e-posta vb.).
2. `references/patterns.md` listesine göre kalıpları tespit et.
3. Yalnızca tespit edilen yerleri yeniden yaz. Sayıları ve iddiaları karşılaştırarak koru.
4. Son okuma: "Bu metni yapay zekâ yazmış gibi gösteren ne kaldı?" sorusunu sor, kalanları düzelt. Kendi düzeltmemin yeni kalıp üretmediğini kontrol et (örneğin bir uzun tireyi kaldırıp yerine üçlü sıralama koymak).
5. Çıktıyı şu sırayla ver:
   - Düzeltilmiş metin (düz, kopyalanabilir)
   - Temizlenen kalıplar, madde madde, her biri için orijinal ifade ve yapılan değişiklik
   - Bilerek dokunulmayan noktalar ve nedeni (teknik terim, dergi stili, yazarın kavramsal tercihi)
   - Varsa hakemin soracağını düşündüğüm içerik sorunları; bunları düzeltmem, yalnızca belirtirim

## Etik not

Yayıncıların çoğu yapay zekâ kullanımının beyan edilmesini istiyor. Metni insanlaştırmak bu yükümlülüğü kaldırmaz. Kullanıcı sorarsa bunu kısa ve yargılamadan hatırlatırım.

## Örnekler

Önce/sonra örnekleri için `references/examples.md` dosyasını oku. Bu örnekler, gerçek bir abstract üzerinde yapılan düzeltmeyi ve Türkçe akademik paragraflardaki tipik dönüşümleri gösterir.
