# Teslim şablonları

Şablonlar çıktının diline çevrilerek kullanılır. Köşeli parantezli alanların hepsi doldurulur; doldurulamayan alan "[YAZAR DOLDURACAK: ...]" olarak bırakılır. Şablonlardaki hiçbir ifade abartılmaz; bulgu ne diyorsa o yazılır.

## 12.1 Kapak mektubu (en çok 400 kelime, tek sayfa)

```
[Tarih]

Dear Dr. [Editörün soyadı; bilinmiyorsa "Dear Editor"],

We submit our manuscript, "[Başlık]", for consideration as a [makale türü] in [Dergi adı].

[Paragraf 1, 2-3 cümle: ele alınan problem ve literatürdeki somut boşluk. Genel önem cümlesiyle başlama; doğrudan problemi yaz.]

[Paragraf 2, 3-4 cümle: ne yapıldı (veri, yöntem) ve en önemli iki nicel bulgu, sayılarıyla. Sayılar özetteki sayılarla aynı.]

[Paragraf 3, 2-3 cümle: çalışmanın bu derginin kapsamına neden uyduğu; derginin kapsam ifadesindeki bir konuya ya da dergide son üç yılda yayımlanmış en çok iki ilgili makaleye somut gönderme. Makale anılacaksa kaynaklar.bib'de olmalı.]

This manuscript is original, has not been published, and is not under consideration elsewhere. All authors have approved the submission. [Çıkar çatışması cümlesi.] [Varsa finansman cümlesi.] [Veri ve kod erişilebilirliği cümlesi.]

[Dergi hakem önerisi istiyorsa: önerilen hakemler, ad, kurum, e-posta; YAZAR DOLDURACAK.]

Sincerely,
[Sorumlu yazarın adı, unvanı, kurumu, adresi, e-postası, ORCID]
```

Türkçe dergi için aynı yapı Türkçe yazılır, hitap "Sayın Editör," olur.

## 12.2 Highlights

Kurallar: 3 ile 5 madde; her madde boşluklar dahil en çok 85 karakter (dergi başka sınır veriyorsa o geçerli); her madde tek bir bulgu ya da katkı; en az iki madde nicel sonuç içerir; kısaltma, atıf ve "novel", "first" gibi kanıtlanmamış sıfat yok; geniş zaman ya da geçmiş zaman, özne "we" olmadan.

```
- [Ne yapıldı: veri ve yöntem, tek satır]
- [Ana nicel bulgu 1]
- [Ana nicel bulgu 2]
- [Yöntemsel katkı ya da karşılaştırma sonucu]
- [Uygulamaya dönük çıkarım]
```

## 12.3 Başlık sayfası

```
Başlık: [tam başlık]
Kısa başlık: [en çok 50 karakter]
Makale türü: [...]

Yazarlar: [Ad Soyad 1]a,*, [Ad Soyad 2]b
a [Bölüm/Merkez, Üniversite, posta kodu Şehir, Ülke]
b [...]
* Sorumlu yazar: [e-posta], [telefon; YAZAR DOLDURACAK]
ORCID: [Yazar 1: ...; Yazar 2: ...]

Özet kelime sayısı: [n]   Ana metin kelime sayısı: [n]   Şekil: [n]   Tablo: [n]   Kaynak: [n]
Anahtar kelimeler: [4-6 adet; başlıktaki kelimeleri yinelemeyen]

Yazar katkıları (CRediT): [Yazar 1: ...; Yazar 2: ...]
Finansman: [kurum ve proje numarası ya da "Bu çalışma için özel bir destek alınmamıştır."]
Çıkar çatışması: [beyan]
Veri erişilebilirliği: [verinin nerede, hangi koşulla erişilebilir olduğu; kısıtlıysa nedeni]
Etik onay: [kurul, tarih, sayı ya da "gerekmemektedir" ve nedeni]
Yapay zekâ kullanım beyanı: [hangi araç, hangi amaçla kullanıldı; yazarların içeriği gözden geçirdiği ve sorumluluğu üstlendiği. Derginin kendi beyan kalıbı varsa o kullanılır. Son metni yazar onaylar.]
Teşekkür: [varsa]
```

CRediT rolleri yalnız şu 14 rolden seçilir: Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing (original draft), Writing (review and editing). Rol dağılımı kullanıcıdan alınır; verilmediyse "[YAZAR DOLDURACAK]" bırakılır. Yapay zekâ aracı yazar olarak gösterilmez.

## 12.5 Proje formu

Fon programının güncel başvuru formu varsa başlıklar ve sınırlar o formdan alınır (form kullanıcıdan istenir ya da programın resmî sayfasından WebFetch ile okunur). Aşağıdaki iskelet yalnız form yokken ya da ön taslak için kullanılır. TÜBİTAK ARDEB tipi formlarda bu başlıklar Özgün Değer, Yöntem, Proje Yönetimi ve Yaygın Etki ana bölümlerine yerleştirilir.

```
1. Proje başlığı, anahtar kelimeler, süre, yürütücü ve ekip
2. Özet [form sınırı; yoksa 250 kelime: amaç, yöntem, beklenen çıktı, yaygın etki]
3. Amaç ve hedefler
   Amaç: [tek cümle]
   Hedefler: [H1, H2...; her biri ölçülebilir, süreli ve bir iş paketine bağlı]
4. Konunun önemi, özgün değer ve araştırma sorusu/hipotezi [literatürdeki boşluk, atıflarla; hipotezler]
5. Yöntem [her hedef için: veri, yöntem (tanım, işleyiş, uygulama sırasıyla), doğrulama, analiz planı; analiz_kontrol.md maddeleri tasarıma yansıtılır]
6. İş paketleri ve iş-zaman çizelgesi
   İP no | Ad | Hedef | Görevler | Sorumlu | Başlangıç-bitiş ayı | Çıktı | Başarı ölçütü (ölçülebilir, eşik değerli) | Projeye katkı payı (%)
7. Risk yönetimi
   Risk | İlgili İP | Olasılık | Etki | B planı (uygulanabilir ve bütçeye yansımış)
8. Araştırma olanakları ve ekip yetkinliği [mevcut altyapı; ekibin konuyla ilgili doğrulanmış yayınları]
9. Yaygın etki: bilimsel çıktılar (hedef yayın sayısı ve türü) | yetişecek araştırmacılar | uygulamaya ve politikaya katkı | yeni proje potansiyeli
10. Bütçe ve gerekçesi
   Kalem | Miktar | Birim maliyet | Toplam | Gerekçe (hangi İP için, neden gerekli) [tutarlar YAZAR DOLDURACAK; fiyat uydurulmaz]
11. Etik kurul ve yasal izinler
12. Kaynaklar
```

Proje metni kuralları: her hedefin en az bir iş paketi ve her iş paketinin ölçülebilir başarı ölçütü vardır; iş paketlerinin katkı payları toplamı 100'dür; her yüksek riskin B planı vardır; ön çalışma ya da pilot veri varsa nicel olarak verilir, yoksa uydurulmaz.
