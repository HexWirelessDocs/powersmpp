---
tags:
  - HTTP
  - DLR
  - Handler
  - Configuration
---

# HTTP DLR Handler Build

HTTP Gateway uygulaması üzerinde yapılandırıldıktan sonra, kullanıcı mesaj gönderebilir ve yanıt başvuruda güncellenecektir.

!!! note
 The The The The The The The The **Gateway Response** Sadece bu **1. yanıt** Bu, mesajların satıcıya başarıyla teslim olup olmadığını gösterir.

Kabul etmek için **DLR (Delivery Receipt)** Satıcıdan, yöneticinin bir yapılandırması gerekiyor **HTTP DLR Handler** Bu yüzden satıcı DLR gönderirse, DLR handler kullanarak uygulama üzerinde DLR güncellenecektir.

Bu belgede, uygulama üzerinde doğru DLR almak için yönetici tarafından yapılması gereken tüm adımları ve konfigürasyonları paylaşacağız.

![Manage HTTP DLR Handler list](images/dlrhandler-01-list.png)

---

## Navigation

<span data-ph="0"></span> <span data-ph="1"></span> <span data-ph="2"></span> <span data-ph="3"></span>.

![Add New Handler form with Method selector](images/dlrhandler-02-add-new.png)

---

## Örnek DLR Payload

HTTP DLR Handler'i yapılandırmak için, ihtiyacımız olacaktır **DLR yanıt format** veya satıcıdan bir örnek DLR, böylece yönetici uygulama üzerindeki yapılandırmayı tamamlayabilir.

Örneğin, aşağıdaki DLR örneklerini HTTP DLR Handler Build için kullanacağız:

```json
{
    "messageId": "161a9168-623c-4411-9e30-cf69353f9bef",
    "status": "EXPIRED",
    "errorCode": "1039",
    "mobile": "91123537072",
    "shortMessage": "Test Message",
    "doneDate": "2024-05-22 11:07:46"
}
```

---

## Kurulum Adımları

Yukarıda verilen DLR handler'i yapılandırmak için aşağıdaki adımları izleyin DLR örneği:

1. **Bir Kullanıcı Dostu İsim Ekle** Eller için.
2. **Whitelist the satıcının IP** *(Not Mandatory)*.
3. **Desteklenen yöntemi seçin** Satıcı tarafından - <span data-ph="0"></span> veya <span data-ph="1"></span>.
4. **Payloads** - Ücret yükleri altında, müşteri belirli değerleri depolayan parametre adını yapılandırmalıdır.

### Field Mapping Referans

| Uygulama Alanı | JSON Keyifine Haritalar | Örnek Değer |
|-------------------|------------------|---------------|
| **MesajId** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Mesaj Status** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Done Date** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Hata Kodu** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Mobile Number** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Sender ID** | *(isteğenim, harita eğer satıcı gönderirse)* | – |
| **Mesaj** | <span data-ph="0"></span> | <span data-ph="0"></span> |

!!! tip
 Yukarıdaki örnekte, parametre <span data-ph="0"></span> DLR statüsünün değerini depolar ve <span data-ph="1"></span> Hata kodunun değerini depolar. Bu parametreler içinde olduğu gibi yapılandırılmalıdır **Mesaj Status** ve **Hata Kodu** sırasıyla. Satıcı tarafından paylaşılan diğer tüm parametreler için aynı mantığı uygulayın.

![Handler configured with payload mapping](images/dlrhandler-03-configured.png)

---

## Yerel Endpoint

Eller kurtarıldığında, Power SMPP bir yaratır **Yerel Endpoint** URL (örneğin, <span data-ph="0"></span>). Bu, satıcının DLR ödeme yükleriyle geri çağıracağı URL'dir.

!!! warning "Önemli Önemli Önemli Önemli Önemli Önemli"
 Tüm detaylar uygulama üzerinde yapılandırıldıktan sonra, **Onu kurtarın ve lütfen ağ geçidi satıcınıza ulaşın ve sonunda DLR handler'in Endpointine sorun.**.

---

## Varsayılan Değerler

Çünkü onlar için **Mesaj Status** ve **Hata Kodu** Alanlar, bir Seçmeli <span data-ph="0"></span> yapılandırılabilir. Varsayılan değer, satıcının bu alanı belirli bir DLR'de iade etmediği zaman uygulanır. Bu, DLR kaydının hala tamamlanmış olmasını sağlar ve mesaj raporlarda kapalıdır.

---

## Doğrulama

DLR handler'i yapılandırdıktan sonra:

1. İlgili HTTP Gateway aracılığıyla bir test mesajı gönderin.
2. Satıcıya sorun (veya gibi bir test aracı kullanın) <span data-ph="0"></span> / <span data-ph="1"></span>Yerel Endpoint URL'ye örnek DLR ödeme yükü göndermek.
3. İlgili Açık **DLR Report** İçinde in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in <span data-ph="0"></span> DLR'nin alındığı ve doğru şekilde parsedildiğini teyit etmek.

DLR görünmüyorsa, parametre adı haritalarını yeniden kontrol edin - en yaygın nedeni, satıcının gönderdiği JSON anahtarı ile eller içindeki anahtar arasında yanlış bir eşleşmedir.
