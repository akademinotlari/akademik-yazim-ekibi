# Ortak yönetim kuralları (yalnız ana oturum okur)

Her aşama skill'i yüklendiğinde ana oturum bu dosyayı bir kez okur. Ajanlar bu dosyayı okumaz; onların kuralları ortak_ajan.md ve kendi görev dosyalarındadır. Bu dosyadaki her kural bağlayıcıdır. "Gerekirse" türü bir ifadenin yanında ölçüt yoksa en temkinli seçenek uygulanır ve kararlar.md dosyasına yazılır.

## 1. Temel ilkeler

1. Uydurma yok. Her atıf DOI ya da yayıncı sayfasıyla doğrulanır (atif_protokolu.md). Doğrulanamayan kaynak metne girmez. Analizden gelen her sayı 04_analiz/sayilar.csv dosyasında, kaynaktan gelen her sayı o kaynağın okunan özetinde ya da tam metninde bulunur. Bu iki yerden birinde bulunmayan sayı metne yazılmaz.
2. Onay kapıları: G1 ve G2 (ay-arastirma), G3 (ay-analiz), G4 (ay-hakem-teslim). Kapıda çıktı sunulur, kullanıcı onaylamadan sonraki adıma geçilmez. Tek istisna kullanıcının açıkça istediği otomatik moddur (Bölüm 7).
3. Ana oturum yönetir, ajanlar üretir. Ana oturum kod, ham ya da işlenmiş veri, taslak bölümlerin tamamı, kaynak tam metni ve ajan görev dosyalarını okumaz (Bölüm 9).
4. Alan sınırı. Brief'teki `alan_siniri` alanına uyulur: literatür, araştırma soruları ve analiz bu sınırın dışına taşmaz (örnek: alan ulaştırma mühendisliği, sınır yalnız karayolu). `alan_siniri` "yok" ise brief'teki `alan` içinde kalınır. Kullanıcı sınırı sohbet içinde değiştirirse yeni sınır brief'e ve kararlar.md'ye yazılır.
5. Biçim. Düz biçim: renkli başlık, süslü tablo, emoji yok.
6. Dışarıya dönük işlem yok. Hiçbir modda dergi sistemine yükleme, e-posta gönderme ya da dosya paylaşma yapılmaz. Gönderimi kullanıcı yapar.
7. Dosya gerçektir. Ajanın dönüş özeti ile yazdığı dosya çelişirse dosya esas alınır. Ajan döndükten sonra beklenen dosyalar `ls` ile denetlenir.
8. Bir sohbette bir aşama. Her aşama skill'i ayrı bir sohbette çalıştırılır; aşamalar arası geçiş devir paketiyle yapılır (Bölüm 10). Kullanıcı aynı sohbette devam etmeyi açıkça isterse bir sonraki skill Skill aracıyla yüklenir.

## 2. Çalışma klasörü

{IS} iş klasörünün mutlak yoludur. Klasör adı kısa, ASCII ve alt çizgilidir (örnek: erisilebilirlik_bildiri).

```
<is_adi>/
  00_brief.md
  01_mini_tarama.md
  02_aday_<altkonu>.csv          arama ajanının aday listesi (doğrulanmamış)
  02_parca_<altkonu>.csv         doğrulanmış parça (birleştirilince matrise girer)
  02_literatur_matrisi.csv       yalnız doğrulanmış kaynaklar
  02_dogrulama_kaydi.csv         her adayın doğrulama kaydı
  02_arama_gunlugu.md
  03_bosluk_yontem.md
  04_analiz/
    kod/ veri/ham/ veri/islenmis/ sonuclar/ sekiller/ tablolar/ log/
    veri_profili.md ozet.md sayilar.csv kontrol_listesi.md sekil_plani.md
    denetim_raporu.md requirements.txt calistir.sh
  05_taslak/                     0_ozet.md ... 5_sonuc.md, ekler/, yazim_notlari.md, uslup_raporu.md
  06_hakem/                      masabasi.md, hakem<n>_tur<t>.md, editor_karari_tur<t>.md, yanit_matrisi.md
  07_teslim/                     son dosyalar, dogrulama raporları
  _kurallar/                     skill'in references dosyalarının kopyası (ajanlar buradan okur)
  kaynaklar.bib                  yalnız doğrulanmış kaynaklar
  kararlar.md
  durum.md
```

kararlar.md kayıt biçimi (numara artan, her karar bir blok):

```
K-<no> | <tarih> | Aşama <n> | Kip: etkileşimli/otomatik
Karar: <tek cümle>
Gerekçe: <dayandığı dosya ve bulgu>
Değerlendirilen seçenekler: <seçenek, neden elendi>
Risk: <yanlışsa ne olur>
Geri alma maliyeti: düşük / orta / yüksek
Kullanıcı onayı: alındı / bekliyor
```

durum.md biçimi (her adım sonunda güncellenir):

```
İş: <is_adi>
Son güncelleme: <tarih saat>
Tamamlanan aşamalar: <0, 1, ...>
Onaylanan kapılar: <G1 (tarih, kullanıcı ya da otomatik), ...>
Sıradaki skill: <ay-arastirma / ay-analiz / ay-yazim / ay-hakem-teslim / bitti>
Sıradaki adım: <tek cümle>
Kip: etkileşimli / otomatik      Bütçe: normal / ekonomik
Açık sorunlar: <liste ya da "yok">
Çağrı sayaçları: <Aşama n: ajan=sayı, ...>
```

## 3. Aşama başlangıcı (her aşama skill'inin ilk adımı)

1. SKILL_DIR, skill yüklenirken bildirilen taban klasördür. `ls "$SKILL_DIR/references"` ile dosyaların varlığını denetle. references klasörü yoksa ya da boşsa dur ve kullanıcıya "skill eksik yüklenmiş, references klasörüyle birlikte yeniden yüklenmeli" de; görev dosyalarını bellekten yazma.
2. İş klasörünü bul, şu sırayla:
   a. Çalışma alanında var mı: `find "$PWD" -maxdepth 3 -name durum.md 2>/dev/null`.
   b. Kullanıcı devir paketi eklediyse: `find / -name '*_devir_*.zip' -not -path '/proc/*' 2>/dev/null`; bulunan en yeni zip'i `unzip -q -o <zip> -d "$PWD"` ile aç.
   c. İkisi de yoksa: aşama ay-arastirma ise yeni klasör aç; değilse dur ve kullanıcıdan devir paketini iste (otomatik kipte de durulur).
3. Kuralları kopyala: `mkdir -p "$IS/_kurallar" && cp "$SKILL_DIR"/references/* "$IS/_kurallar/" && ls "$IS/_kurallar"`.
4. durum.md dosyasını oku. kararlar.md dosyasının yalnız son 30 satırını oku (`tail -n 30`). Aşama skill'inin önkoşulunu denetle; sağlanmıyorsa durum.md'deki "Sıradaki skill" değerini kullanıcıya söyle ve dur.
5. Aşamanın adımlarını TaskCreate ile görev listesine ekle.

## 4. Ajan çağırma

Her ajan Agent aracıyla, `subagent_type: "general-purpose"` ve Bölüm 5'teki `model` değeriyle başlatılır. İstem aşağıdaki çağrı kalıbıdır; görev dosyasının içeriği isteme kopyalanmaz, ajan dosyayı kendisi okur.

```
Akademik yazım ekibinde <AJAN ADI> olarak çalışıyorsun.
1. Önce {IS}/_kurallar/ortak_ajan.md dosyasını, sonra {IS}/_kurallar/<görev dosyası> dosyasını baştan sona oku. Rolün, okuyacağın ve yazacağın dosyalar, adımlar, kalite ölçütleri ve dönüş biçimi bu dosyalardadır; harfiyen uygula.
2. Değişkenler (görev dosyasındaki {AD} yerlerine bunları koy):
IS = <mutlak yol>
<AD> = <değer>
...
3. EK BAĞLAM: <en çok 100 kelime ya da "yok">
```

Kurallar:
- Görev dosyasında tanımlı her değişken doldurulur; isteme boş değişken gitmez.
- Sonucu bir sonraki adımın girdisi olan tekil çağrılarda `run_in_background: false`.
- Paralel çağrılar tek mesajda art arda yazılır; hepsinin sonucu gelmeden sonraki adıma geçilmez. Paralel ajanlar aynı dosyaya yazmaz.
- Ajan döndükten sonra: (a) DURUM satırını oku; (b) YAZILAN DOSYALAR'ı `ls -la` ile denetle; (c) durum.md'deki çağrı sayacını artır.
- DURUM KISMEN ya da BAŞARISIZ ise Bölüm 8 uygulanır.

## 5. Model ataması

İlke: kurala bağlı ve sonucu denetlenebilir işler betik ya da haiku; arama, çıkarım, düzenleme ve kalıba bağlı metin sonnet; çok adımlı muhakeme ve özgün akademik metin opus; kapı ve editör kararları ana oturum.

| Skill | Ajan / görev | Görev dosyası | Normal | Ekonomik |
|---|---|---|---|---|
| ay-arastirma | Literatür Arama | ajan_literatur_arama.md | sonnet | sonnet |
| ay-arastirma | Kaynak Doğrulama | ajan_kaynak_dogrulama.md | haiku | haiku |
| ay-arastirma | Araştırma Sorusu | ajan_arastirma_sorusu.md | opus | opus |
| ay-arastirma | Literatür birleştirme | birlestir_literatur.py | betik | betik |
| ay-arastirma | Boşluk, yöntem, analiz planı | yok | ana oturum | ana oturum |
| ay-analiz | Veri Profili | ajan_veri_profili.md | haiku | haiku |
| ay-analiz | Veri Hazırlama | ajan_veri_hazirlama.md | sonnet | sonnet |
| ay-analiz | Analiz | ajan_analiz.md | opus | opus |
| ay-analiz | Şekil | ajan_sekil.md | sonnet | sonnet |
| ay-analiz | Tekrarlanabilirlik Denetçisi | ajan_tekrar_denetci.md | haiku | haiku |
| ay-yazim | Yazım (TAM ve PROJE kipi) | ajan_yazim.md | opus | opus |
| ay-yazim | Yazım (NOT_KAPAT kipi) | ajan_yazim.md | sonnet | sonnet |
| ay-yazim | Üslup taraması | uslup_tarama.py | betik | betik |
| ay-yazim | Üslup Düzeltici | ajan_uslup_duzeltici.md | sonnet | sonnet |
| ay-yazim | Ek Metin | ajan_ek_metin.md | sonnet | sonnet |
| ay-yazim | Biçimlendirme | ajan_bicimlendirme.md | sonnet | sonnet |
| ay-hakem-teslim | Masa Başı Denetçisi | ajan_masabasi.md | haiku | haiku |
| ay-hakem-teslim | Hakem 1 (yöntem) | ajan_hakem.md | opus | opus |
| ay-hakem-teslim | Hakem 2 (alan) | ajan_hakem.md | opus | sonnet |
| ay-hakem-teslim | Editör kararı | yok | ana oturum | ana oturum |
| ay-hakem-teslim | Revizyon [ANALİZ] | ajan_revizyon.md | opus | opus |
| ay-hakem-teslim | Revizyon [YAZIM], BÜYÜK madde varsa | ajan_revizyon.md | opus | sonnet |
| ay-hakem-teslim | Revizyon [YAZIM], yalnız KÜÇÜK | ajan_revizyon.md | sonnet | sonnet |
| ay-hakem-teslim | Revizyon [LİTERATÜR] | ajan_revizyon.md | sonnet | sonnet |
| ay-hakem-teslim | Çeviri (ikinci dil) | ajan_ceviri.md | sonnet | sonnet |
| ay-hakem-teslim | Doğrulayıcı Mekanik | ajan_dogrulayici_mekanik.md | haiku | haiku |
| ay-hakem-teslim | Doğrulayıcı İçerik | ajan_dogrulayici_icerik.md | sonnet | sonnet |

Model yükseltme kuralı: Bir ajan aynı adımda iki kez KISMEN ya da BAŞARISIZ döner ve neden araç ya da veri değil de çıktının niteliğiyse (kurala uymayan çıktı, yanlış çıkarım, eksik adım), görev bir üst modelle (haiku sonra sonnet, sonnet sonra opus) bir kez daha verilir ve kararlar.md'ye yazılır. Opus ajanı iki kez başarısız olursa Bölüm 8 uygulanır.

Ana oturum modeli (kullanıcı sohbeti açarken seçer): ay-arastirma ve ay-hakem-teslim için Opus; ay-analiz ve ay-yazim için Sonnet yeterlidir, çünkü bu iki aşamada ana oturum yalnız ajan çağırır ve kapı özeti sunar.

## 6. Kapılarda sunum

Özet 250 kelimeyi geçmez ve şu sırayı izler: üretilen dosyalar; onayı beklenen karar (tek cümle); seçenekler ve her birinin riski; editörün önerisi ve gerekçesi; bilinen açık sorunlar. Dosyalar SendUserFile ile eklenir. Sonra durulur. Kullanıcı değişiklik isterse yalnız istenen kısım düzeltilir ve aynı kapı yeniden sunulur.

## 7. Otomatik mod (isteğe bağlı)

Varsayılan kip etkileşimlidir. Otomatik mod yalnız kullanıcı açıkça isterse açılır: "otomatik mod", "kapılarda durma", "sormadan ilerle", "onay bekleme" ifadelerinden biri ya da brief'te kip: otomatik. Kullanıcı "dur" ya da "etkileşimli moda dön" derse bir sonraki kapıdan itibaren etkileşimli kipe geçilir.

Otomatik modda G1, G2 ve G3'te durulmaz. Ana oturum kapının karar kuralını (ilgili aşama skill'inde yazılıdır) uygular, kararı kararlar.md dosyasına "Kullanıcı onayı: bekliyor" notuyla yazar, kapı özetini SendUserMessage ile bilgi olarak gönderir ve devam eder. G4 her kipte sunulur; otomatik modda G4 özetine kararlar.md içindeki bütün kararlar tek satırlık liste olarak eklenir.

Zorunlu duruşlar (otomatik modda bile durulur, durum ve seçenekler kullanıcıya sunulur):
- D1. G1'de eleme sonrası aday kalmadı.
- D2. Veri yalnız kullanıcıdan gelebiliyor, ücretli, lisans başvurusu ya da etik kurul izni gerektiriyor.
- D3. Önerilen yöntem birincil metrikte en iyi temel modeli %95 güven aralıkları örtüşmeyecek biçimde geçemedi ve ana katkı bu üstünlüğe dayanıyor; ya da ana hipotez desteklenmedi ve araştırma sorusunun değişmesi gerekiyor.
- D4. Editör kararı RET.
- D5. Yedek yollardan sonra doğrulanmış kaynak sayısı hedef alt sınırının %70'inin altında.
- D6. Aynı adımda üçüncü başarısızlık.
- D7. Analiz planından sapma birincil metriği ya da veri setini değiştiriyor.

Otomatik mod hiçbir kuralı gevşetmez: uydurma yasağı, doğrulama protokolü, kontrol listeleri ve tur sınırları aynen geçerlidir. Otomatik kip aşama sınırında da devir paketiyle durur; yeni sohbette kullanıcı devir paketini ekleyince kaldığı yerden otomatik devam edilir.

## 8. Genel hata kuralları

Her hata için önce neden belirlenir, tek düzeltme uygulanır, sonuç kararlar.md'ye yazılır. Aynı adımda ikinci düzeltme de başarısız olursa etkileşimli kipte kullanıcıya seçeneklerle sunulur; otomatik kipte D6 tetiklenir. Hiçbir hata eksiği uydurarak kapatılmaz. Aşamaya özgü hata durumları ilgili SKILL.md dosyasındadır; aşağıdakiler her aşamada geçerlidir.

H9. Ajan dosyasını yazmadan döndü ya da dönüş biçimi bozuk. `ls` ile beklenen dosyalar denetlenir. Eksik varsa aynı istem, EK BAĞLAM'a "önceki çağrıda şu dosyalar yazılmadı: ..." eklenerek bir kez yeniden gönderilir. Kısmen yazılmış dosyalar silinmez; ajan kaldığı yerden sürdürür.

H12. Gerekli bir skill yüklenemiyor. human yoksa yazim_kurallari.md madde 7 ve uslup_tarama.py tek başına uygulanır. dataviz yoksa ajan_sekil.md içindeki yedek kurallar uygulanır. docx yoksa teslim dosyaları Markdown olarak verilir ve G4'te belirtilir. Aşama skill'inin kendisi bulunamıyorsa kullanıcıya hangi skill'in eksik olduğu söylenir; işi bellekten yürütme.

H13. Oturum kesildi ya da yeni oturumda devam ediliyor. Bölüm 3 uygulanır. Son tamamlanan adımın çıktı dosyaları `ls` ile doğrulanır. Tamamlanmış adım yeniden çalıştırılmaz.

H15. Bütçe tükeniyor (kullanım sınırı uyarısı geldi ya da kullanıcı durdurdu). Bulunulan adım tamamlanmaya çalışılmaz; durum.md güncellenir, devir paketi hazırlanıp gönderilir (Bölüm 10), kalan adımlar tek paragrafla yazılır.

## 9. Token bütçesi

Ana oturumun okuma kuralları:
- Hiç okunmayanlar: ham ya da işlenmiş veri, kod dosyaları, log dosyalarının tamamı, taslak bölümlerin tamamı, kaynak tam metinleri, _kurallar altındaki ajan görev dosyaları.
- Okunabilenler: aşama skill'inde açıkça sayılan dosyalar ve satır aralıkları.
- 300 satırdan uzun dosya Read ile baştan sona açılmaz; Grep ile yer bulunur, offset ve limit ile yalnız ilgili parça okunur.
- Şekiller yalnız G3 öncesinde bir kez görüntülenir.

İstem ekonomisi:
- Kural metni ve dosya içeriği isteme yapıştırılmaz; yalnız dosya yolu ve değişken verilir.
- EK BAĞLAM en çok 100 kelimedir.
- Ajan dönüşü en çok 150 kelimedir (ortak_ajan.md).

Yeniden çalıştırma:
- Onaylanmış aşama yeniden çalıştırılmaz. Kullanıcı değişiklik isterse yalnız etkilenen dosyalar için ilgili ajan tek çağrıyla çalıştırılır.
- Analiz değiştiğinde yalnız değişen sayı kimliklerinin geçtiği bölümler yeniden yazdırılır; bölümler `grep -l` ile bulunur.
- Aynı girdiyle aynı ajan ikinci kez başlatılmaz (H9 ve model yükseltme kuralı dışında).

Bütçe kipi brief'teki `butce` alanından okunur. Kullanıcı "bütçe dar", "ekonomik mod", "az harca" derse ekonomik kipe geçilir. Ekonomik kip yalnız aşama skill'lerinde "ekonomik" diye yazılan kısıntıları uygular; atıf doğrulama protokolünü, analiz kontrol listelerini, Doğrulayıcı'yı ve uydurma yasağını kısmaz. Her aşamanın çağrı tavanları kendi SKILL.md dosyasındadır; tavan dolunca yeni çağrı yapılmaz, kalan sorun açık sorun olarak kaydedilir.

## 10. Aşama bitişi ve devir paketi

1. durum.md güncellenir: tamamlanan aşama, onaylanan kapı, sıradaki skill, sıradaki adım.
2. Devir paketi hazırlanır:
```bash
cd "$(dirname "$IS")" && AD="$(basename "$IS")" && BOYUT=$(du -sm "$AD/04_analiz/veri/ham" 2>/dev/null | cut -f1)
if [ "${BOYUT:-0}" -gt 200 ]; then zip -qr "${AD}_devir_<asama>.zip" "$AD" -x "$AD/04_analiz/veri/ham/*"; else zip -qr "${AD}_devir_<asama>.zip" "$AD"; fi
ls -la "${AD}_devir_<asama>.zip"
```
   <asama> yerine biten skill'in kısa adı yazılır (arastirma, analiz, yazim, teslim). Ham veri 200 MB'ı aşıp pakete alınmadıysa kullanıcıya bir sonraki sohbette ham veriyi ayrıca eklemesi söylenir.
3. Zip ve kapı dosyaları SendUserFile ile gönderilir.
4. Kullanıcıya tek cümleyle sonraki adım söylenir: "Yeni bir sohbet açın, bu zip'i ekleyin ve '<sıradaki skill> ile devam et' yazın."
