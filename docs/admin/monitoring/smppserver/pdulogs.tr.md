
# Server PDU Logs

The The The The The The The The **SMPP Server PDU Logs** iTextPRO, iTextPRO için önemlidir **İzleme ve sorun giderme** Mesaj işlemleri arasında **ESME (Son Kısa Mesaj Entity) kullanıcı** ve iTextPRO platformu. 
Bu loglar yakalama **downstream trafik** Ve verimli sorun çözümünde yardımcı olan ayrıntılı bilgi sağlar.

---

## Anahtar Özellikler
- **Kapsamlı İşlem Logging** - ESME kullanıcısı ve iTextPRO arasındaki her mesajı izleyin.
- **Sorun Giderme Desteği** - Haberleşme sorunlarını teşhis etmek ve çözmek için eleştirel.
- **Admin Time Zone** – Logs, yöneticinin zamanında doğru referans için gösterilir.

---

## Downstream Trafik
Tracks the Tracks the **mesajların yolculuğu** ESME kullanıcıdan iTextPRO'e, teslimat akışı ve statüsüne görünürlük sağlar.

![Server PDU Logs](images/pdulogs1.png)

---

## Verbosity Levels

Anlamayı Anlayın **Cümle seviyeleri** İzleme ve sorun gidermede yardımcı olur:

| **Verbosity Level** | **Açıklama** | **Amaç** |
|---------------------|-----------------|-------------|
| **Bind İstek** | ESME kullanıcısı bağlantı başlatır. | iTextPRO ile bağlantı kurmak. |
| **Bin Cevap** | iTextPRO bağlantı isteğine cevap verir. | ESME kullanıcısının bağlantısını tanır. |
| **Enquire Link Request** / **Yanıt** | Sağlık kontrolü ESME kullanıcı ve ilgili yanıtdan çağrır. | iTextPRO seans durumunu belirtir (geçmiş aralığı: 30 saniye). |
| **Send SM Talep İste** | ESME kullanıcısı mesaj talebini başlatır. | ITextPRO için SMS mesajları gönderin. |
| **Send SM Response** | iTextPRO mesaj isteğine yanıt verir. | SMS başvurularını kabul edin. |
| **Teslimat SM Talep İste** | DLR (Delivery Report) iTextPRO tarafından gönderilen bir mesaj için alındı. | Gönderilen SMS için teslimat durumu Güncellemeler. |
| **Teslimat SM Yanıt** | ESME kullanıcısı DLR talebini kabul eder. | Teslimat statüsünü onaylayın. |
| **Unbind Request** | ESME kullanıcısı unbind istek başlatır. | Terminates bağlantılı seanslar. |

---

## En İyi Uygulamaları
- **Düzenli olarak Review Logs** - İşlemle ilgili konularda sağlam izleme ve hızlı bir algılama sağlar.
- **Verbosity Insights** - ESME ve iTextPRO arasında etkili iletişim sağlamak için yakalanan PDU ayrıntıları kullanın.
- **Prompt Action** - En kısa sürede optimal sistem performansını korumak için tespit edilen anomalilere ulaşın.
