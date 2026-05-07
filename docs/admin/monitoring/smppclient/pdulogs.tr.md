---
tags:
  - Monitoring
  - PDU
  - Troubleshooting
---

# İzleme İzleme İzleme İzleme İzleme

iTextPRO kapsamlı bir şekilde sunuyor **İzleme araçları izleme araçları** optimal SMS teslimat performansı ve sistem istikrarı sağlamak. Bu da içerir. **Gerçek zamanlı Canlı İzleme** Trafik öngörüleri ve sağlam bir **PDU Logger** Derin mesaj seviyesi analizi için.

---

## Canlı Takip

The The The The The The The The **Canlı Takip** ITextPRO dinamik olarak izler ve SMS trafiği ile ilgili anahtar veri puanlarını analiz eder, etkinleştirir **Gerçek zamanlı karar verme** routing ve performans optimizasyonu için.

### Anahtar Faydaları
- **Proaktif Trafik Yönetimi** - SMS trafiğini canlı verilere dayanan dinamik olarak yönetin.
- **Optimized Routing** - Teslimat oranlarını geliştirmek için routing kararlarını bilgilendirin.
- **Verimli Kaynak Allocation** – Top saatler boyunca stratejik olarak tüm kaynakları.
- **Geliştirilmiş Performans** - Doğru zaman anlayışları ile karşıtlığı ve yönlendirmeyi geliştirin.

**Özet**Canlı İzleme, kullanıcıların sahip olmasını sağlar **up-to-the-minute görünürlük** SMS trafik akışına, özellikle yüksek talep süreleri boyunca.

---

## PDU Logs

iTextPRO bir işe yarar **PDU (Protocol Data Unit) Logger** SMSC'ye giren veya ayrılan her mesajı yakalamak ve oturum açmak. Bu araç için hayati önem taşıyor **Problem çözme**, **İzleme izleme izleme**Ve **bakımı korumak** Sistem sağlığı.

### Anahtar Özellikler
- **Gerçek zamanlı Mesaj Yolculuğu** – Hemen analiz için gerçek zamanlı olarak her mesajı girin.
- **Gürültüyü filtrelemek** – Bir tıklama ile bir mesajın yolculuğunu izleyin.
- **PDU Type Support** – Inspect SendSM, DeliverSM, Bind, Unbind ve daha fazlası.
- **Viability & Retention** – Logs takip eder **admin time zone** Ve için muhafaza edilir **3 gün**.
- **Upstream Trafik Denetimi** – Bir düşüş listesinden ağ geçidi seçerek mesaj akışını görün.
- **Sorun Giderme Desteği** - Hızlı teslimat veya SMPP seans sorunları.

![PDU Logs](images/pdulogs1.png)

### Kullanım Kılavuzları
1. Erişim **PDU Logger** iTextPRO arayüzünden.
2. Başvuru Başvuru **filtreler filtreler filtreler** Belirli mesajları izole etmek ve denetlemek.
3. Use Use Use Use Use Use **Upstream trafik logları** Mesaj yolculuklarını doğrulamak için.
4. Gerçek Performans Performansı **Düzenli izleme** Sistem güvenilirliğini korumak için.

---

## Verbosity Levels in PDU Logging

iTextPRO'in PDU logu birden çok destekler **Cümle seviyeleri**ITextPRO ve SMPP ağ geçidi arasında iletişim kurmak.

| Verbosity Level | Amaç | Eylem |
|-----------------|---------|--------|
| **Bind İstek** | SMPP bağlayıcı | iTextPRO, SMPP ağ geçidine bağlanmak için bir istek gönderir |
| **Bin Cevap** | SMPP bağlayıcısını onaylar | SMPP ağ geçidi, bağlayıcı isteke cevap verir |
| **Enquire Link Request / Response** | SMPP oturumunun sağlık kontrolü | iTextPRO her 30s talep eder; ağ geçidi yanıt verir |
| **Send SM Talep İste** | Mesaj gönderme isteği | iTextPRO, SMPP ağ geçidine bir SMS gönderir |
| **Send SM Response** | Submission acknowledgment | Gateway mesaj göndermelerine yanıt verir |
| **Teslimat SM Talep İste** | Teslimat Raporu (DLR) Resepsiyon | SMPP ağ geçidi teslimat durumunu gönderir |
| **Teslimat SM Yanıt** | Acknowledgment of DLR | iTextPRO, DLR'nin makbulunu doğruluyor |
| **Unbind Request** | Oturum sonu | iTextPRO veya ağ geçidi, unbind talebini başlatır |

**Önemli:** Bu loglar yöneticilere hizmet verir **mesaj akışlarının görünümü**Ancak algılamaya, teşhis etmeye ve sorunları verimli bir şekilde çözmeye yardım edin.

---

With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With With **Canlı Takip** ve **PDU Logging**, iTextPRO yöneticileri korumak için güçlendiriyor **Son derece güvenilir SMS teslimat sistemi**proaktif olarak sorunları tespit edin ve gerçek zamanlı olarak trafiği optimize edin.
