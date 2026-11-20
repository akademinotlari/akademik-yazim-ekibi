# Akademik Yazım Ekibi

Konu verildiğinde araştırma sorusundan gönderime hazır makale, bildiri, kitap bölümü ya da proje metnine kadar ilerleyen çok ajanlı akademik yazım iş akışı. Claude (claude.ai, Claude masaüstü uygulaması ve Claude Code) için bir plugin olarak dağıtılır. Talimatlar Türkçedir; üretilen metin Türkçe, İngilizce ya da ikisi olabilir.

## Ne yapar

- Literatür taraması yapar ve her kaynağı DOI üzerinden doğrular; doğrulanamayan kaynak metne girmez.
- Araştırma sorusu adayları üretir, yeniliklerini ve veri erişimini sınar.
- Analiz planını sonuçlar görülmeden yazar (ön kayıt mantığı), analizi Python ile yapar; veri sızıntısı, doğrulama kurgusu, belirsizlik ve tekrarlanabilirlik için yöntem türüne göre kontrol listeleri uygular (makine öğrenmesi, zaman serisi, mekânsal analiz, istatistiksel testler).
- Metni Yöntem, Bulgular, Sonuç, Tartışma, Giriş, Özet sırasıyla yazar; her sayıyı analiz çıktısıyla, her atfı kaynağın özetiyle eşleştirir.
- Yapay zekâ yazım kalıplarını (uzun tire, "Sonuç olarak" kapanışları, -maktadır zincirleri, abartılı önem vurgusu vb.) betikle tarar ve düzeltir.
- İki bağımsız hakem ajanı ve kurala bağlı editör kararıyla gönderim öncesi iç değerlendirme yapar.
- Kapak mektubu, highlights, başlık sayfası, beyanlar ve dergi biçiminde Word dosyası hazırlar.

Ekip dergiye kendisi gönderim yapmaz, e-posta atmaz; teslim paketini kullanıcıya verir.

## Kurulum

### claude.ai ve Claude masaüstü uygulaması

1. Customize > Plugins sayfasında Add > Add marketplace seçin.
2. Repo adresini girin: `https://github.com/akademinotlari/akademik-yazim-ekibi` ya da kısaca `akademinotlari/akademik-yazim-ekibi`.
3. Listede görünen `akademik-yazim-ekibi` plugin'ini ekleyin.
4. Güncellemeler için aynı sayfada Check for updates seçin ya da Sync automatically ayarını açın.

Team ve Enterprise planlarında kullanıcıların kendi marketplace'lerini ekleyip ekleyemeyeceğini kuruluş yöneticisi belirler.

Repo eklemek istemeyenler Releases sayfasındaki `akademik-yazim-ekibi-plugin.zip` dosyasını Customize > Plugins > Add > Upload plugin ile yükleyebilir. Bu yolla güncellemeler otomatik gelmez.

### Claude Code

```
/plugin marketplace add akademinotlari/akademik-yazim-ekibi
/plugin install akademik-yazim-ekibi@akademik-yazim
```

### Gerekenler

- Kod çalıştırma ve dosya oluşturma özelliğinin açık olması (betikler ve analiz için).
- Web araması (literatür ve DOI doğrulaması için). Elicit bağlayıcısı varsa kullanılır; yoksa Crossref ve OpenAlex ile devam edilir.
- İsteğe bağlı: Claude'un hazır docx ve dataviz skill'leri. Yoksa ekip yedek kurallarla çalışır.

## Kullanım

Ekip dört aşamaya bölünmüştür. Her aşamayı ayrı bir sohbette çalıştırmanız önerilir; aşama sonunda iş klasörü zip olarak (devir paketi) verilir, bir sonraki sohbete eklenir. Böylece bağlam aşamalar boyunca birikmez ve kullanım hakkı daha az tükenir.

| Sohbet | Yazacağınız | Skill | Kapı | Önerilen model |
|---|---|---|---|---|
| 1 | "Akademik yazım ekibiyle şu konuda bir makale hazırlayalım: ..." | ay-arastirma | G1 araştırma sorusu, G2 yöntem planı | Opus |
| 2 | devir zip'ini ekleyip "ay-analiz ile devam et" | ay-analiz | G3 bulgular | Sonnet |
| 3 | devir zip'ini ekleyip "ay-yazim ile devam et" | ay-yazim | yok | Sonnet |
| 4 | devir zip'ini ekleyip "ay-hakem-teslim ile devam et" | ay-hakem-teslim | G4 teslim paketi | Opus |

İlk sohbette ekip bir brief doldurur: konu, bilim alanı, varsa alan sınırı (örnek: "ulaştırma mühendisliği, yalnız karayolu"), yazarın uzmanlık alanları, çıktı türü, dil, hedef dergi, şablon, veri durumu, kip ve bütçe.

Otomatik mod: brief'te `kip: otomatik` ya da "kapılarda durma" derseniz G1-G3'te durulmaz; kararlar gerekçesiyle kararlar.md dosyasına yazılır ve G4'te topluca sunulur. Veri yalnız sizden gelebiliyorsa, editör kararı ret ise ya da analiz planından sapmak gerekiyorsa otomatik modda da durulur.

Ekonomik kip: brief'te `butce: ekonomik` ya da "ekonomik mod". Kaynak hedeflerini, alt konu sayısını, hiperparametre denemesini ve ikinci hakem turunu kısar; atıf doğrulamayı ve kontrol listelerini kısmaz.

## Model dağılımı

| Düzey | İşler |
|---|---|
| Betik (model yok) | literatür parçalarını birleştirme, üslup kalıbı taraması, atıf-kaynakça eşleşmesi, metindeki sayıların analiz çıktılarıyla karşılaştırılması, şekil ve tablo numara sırası |
| haiku | DOI ve künye doğrulama, veri profili, tekrarlanabilirlik denetimi, masa başı denetimi, son kontrolün mekanik maddeleri |
| sonnet | literatür arama ve özetten bilgi çıkarma, veri hazırlama, şekil çizimi, üslup düzeltme, ek metinler, Word biçimlendirme, literatür revizyonu, küçük yazım revizyonları, çeviri, iddia-kaynak uyumu denetimi |
| opus | araştırma sorusu üretimi, analiz ve modelleme, ana metin yazımı, iki hakem, analiz revizyonu, büyük yazım revizyonu |
| ana oturum | brief, kapı kararları, boşluk-yöntem-analiz planı, editör kararı |

Bir ajan aynı adımda iki kez nitelik nedeniyle başarısız olursa görev bir kez bir üst modele verilir.

## Repo yapısı

```
.claude-plugin/marketplace.json        marketplace tanımı
plugins/akademik-yazim-ekibi/
  .claude-plugin/plugin.json           plugin tanımı ve sürüm
  skills/
    baslat/                            yönlendirici: hangi aşamanın yükleneceğine karar verir
    ay-arastirma/                      Aşama 0-3
    ay-analiz/                         Aşama 4
    ay-yazim/                          Aşama 5-6
    ay-hakem-teslim/                   Aşama 7-8
    human/                             yapay zekâ izi bırakmadan yazma kuralları
ortak/                                 birden çok skill'in kullandığı dosyaların ana kopyaları
tools/senkronize.sh                    ortak/ dosyalarını skill'lere dağıtır (--kontrol ile yalnız denetler)
tools/paketle.sh                       denetler ve dist/ altına zip paketleri üretir
```

Her aşama skill'inde SKILL.md yalnız ana oturumun okuduğu kısa yönetim talimatıdır. Ajanların görev tanımları (ajan_*.md), kontrol listeleri, şablonlar ve betikler references/ altındadır; ana oturum bunları okumaz, iş klasörüne kopyalar ve her ajan kendi dosyasını kendisi okur.

## Katkı ve geliştirme

- Paylaşılan dosyaları yalnız `ortak/` altında düzenleyin, sonra `tools/senkronize.sh` çalıştırın. Skill klasörlerindeki kopyaları elle düzenlemeyin; GitHub Actions denetimi farkı yakalar.
- Yeni ortak dosya eklerseniz `tools/senkronize.sh` içindeki ESLEME listesine hangi skill'lere gideceğini yazın.
- Her yayımda `plugins/akademik-yazim-ekibi/.claude-plugin/plugin.json` içindeki `version` değerini artırın; kullanıcılara güncelleme bu sürüm üzerinden gider.
- Release için `tools/paketle.sh` çalıştırın ve `dist/akademik-yazim-ekibi-plugin.zip` dosyasını release'e ekleyin.

## Sınırlar

- Ekip çıktısı bir taslaktır. Metni, analizleri ve kaynakları yayın öncesinde yazar denetlemeli ve sorumluluğunu üstlenmelidir.
- Yapay zekâ kullanımını beyan edin; ekip başlık sayfasına beyan alanı koyar ama içeriğini yazar onaylar.
- Uydurma kaynak ve sayıya karşı çok katmanlı denetim vardır, ancak hiçbir denetim hatasızlığı garanti etmez.

## Lisans

MIT. Ayrıntı için LICENSE dosyasına bakın.

## Sürüm notları

2.0.0
- Tek skill dört aşama skill'ine ve yönlendiriciye bölündü; aşamalar arası devir paketi eklendi.
- Plugin ve marketplace olarak paketlendi; human skill'i plugin'e dahil edildi.
- Görevler zorluğuna göre betik, haiku, sonnet ve opus arasında paylaştırıldı.
- Üç betik eklendi: birlestir_literatur.py, uslup_tarama.py, mekanik_kontrol.py.
- Alan, alan sınırı ve yazar uzmanlığı brief'te sorulan alanlara dönüştü.
- Yazım kurallarına netleştirme: Türkçe akademik metinde geçmiş zaman -mıştır biçimiyle yazılır.

1.0.0
- Tek SKILL.md içinde ekip, aşamalar, kapılar, ajan istemleri, kontrol listeleri, şablonlar, otomatik mod, hata durumları ve token bütçesi.
