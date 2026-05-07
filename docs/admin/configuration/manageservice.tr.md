
## Yönetme Hizmetleri

The The The The The The The The **Yönetme Hizmetleri** ITextPRO'deki bölüm çeşitli görünürlüğe sunar **arka plan ve foreground hizmetleri** Bu, platformun temel işlevlerine yol açıyor. Bu arayüz öncelikle uzman kullanıcılar veya yöneticiler için tasarlanmıştır.

!!! danger "Caution"
 Web arayüzünden bir hizmet durdurmak veya başlatmak mümkün olsa da, bu yapılmalıdır. **Aşırı uyarı ile**Özellikle üst yük zamanlarında, sonuçlanabilir gibi **veri kaybı** veya **Servis kesintisi**.

---

### Servis Genel Bakış

Aşağıda, her hizmetin görünür olduğu kısa bir açıklamadır. **Yönetme Hizmetleri** Bölüm:

| **Servis Adı**         | **Açıklama**                                                                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Müşteri Hizmetleri**       | Connects iTextPRO with your SMSC via SMPP for managing **SMS MT (Mobile Terminated)** ve **SMS MO (Mobile Originated)** trafik.                      |
| **DLR Service**          | Gerçek zamanlı temaslar **Teslimat Raporları (DLRs)** ve doğru raporlama için sistem içindeki mesaj durumunu güncellemek.                                      |
| **SMPP Server Servisi**  | Inbound SMPP trafiği için dinleyin **ESME kullanıcıları** Önceden tanımlanmış bir limanda, dış kullanıcıların SMS göndermesine izin veriyor.                                      |
| **File Pickup Service**  | Kullanıcı tarafından yüklenen kampanya mesaj dosyalarını okuyun ve onları onlara **ağ geçidi kuyruğu** işleme için.                                               |
| **Validator Service**    | Geçerlilikler **bağlayıcı parametreler** API ve SMPP arabirimleri ile bağlantı sağlayan kullanıcılar için, trafik yalnızca yetkili müşteriler tarafından kabul edilir.       |
| **Data Builder Service** | Depolamayı Yönetin **PDU logları** ve **Mesaj logları** Log ve debugging amaçları için veritabanına.                                          |
| **Report Builder Service** | Profiller ve derleyiciler **Gönderilen Sayılar ve Özet raporlar** Kullanıcılar için, kullanım izleme ve faturalama konusunda yardım edin.                                            |
| **Download Report Service Service** | Süreçler ve üretirler **indirilebilir raporlar** Talep edilen verilere dayanan hem yöneticiler hem de kullanıcılar için.                                                  |
| **Bildirim Hizmeti** | Gönder **E-posta uyarı bildirimleri** Kullanıcılara ve yöneticilere ve aktif olarak monitörlere **ağ geçidi sağlık durumu**.                                               |

---

### Anahtar Özellikler

- the View the the the **Mevcut durum durumu** Her hizmetten.
- seçeneği **Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start Start** veya **Dur Dur Dur Dur Dur** Web arayüzünden servisler.
- tarafından kullanılmak için tasarlanmıştır **Gelişmiş kullanıcılar veya yöneticiler** Servis bağımlılıkları güçlü bir anlayışla.
- the Her hizmet metadata'yı da içerir **Uygulama versiyonu**.

---

### En İyi Uygulamaları

- Her zaman kritik hizmeti durdurmadan önce zirve trafik saatlerini onaylayın (örneğin, Müşteri, DLR, Validator).
- Danışmanlık sistemi logları veya teknik destek olmadan hizmetleri yeniden başlatmaktan kaçının.
- Verilerin tutarsızlıklarını önlemek için veritabanı ve ağ geçidi hizmetleri senkronize edilir.

---

The The The The The The The The **Yönetme Hizmetleri** Özellikler, iTextPRO ortamında düzgün işlemleri sağlamak için merkezileştirilmiş bir yol sunar.
