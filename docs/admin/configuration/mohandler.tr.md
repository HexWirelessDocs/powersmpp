---
tags:
  - HTTP
  - MO
  - Handler
  - Configuration
---

# HTTP MO Handler

## Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış

The The The The The The The The **HTTP MO Handler** iTextPro almak ve gelecek süreci almak için kullanılır **MO (Mobile Originated)** Telecom operatörlerinden veya ağ geçidi satıcılarından gelen mesajlar. Eller MO isteklerini kabul eden ve alınan verileri daha fazla routing ve işleme için platforma doğru ilerleten bir API uç noktası olarak hareket eder.

HTTP MO Handler yapılandırması şunları tanımlar:

- İletişim yöntemi
- Kanal detayları
- Payload mapping
- Güvenlik kısıtlamaları
- Endpoint nesli

!!! warning "Önkoşul"
 Bu yapılandırmadır **zorunlu zorunlu zorunlu zorunlu zorunlu zorunlu zorunlu zorunlu** MO Routing Kuralları oluşturmadan önce.

---

## Navigation Path

<span data-ph="0"></span> <span data-ph="1"></span> <span data-ph="2"></span>.

![Manage MO Handler list](images/mohandler-01-list.png)

---

## Handler Build Paralar

Aşağıdaki parametreler HTTP MO Handler oluştururken yapılandırılmalıdır.

### 1] Handler Name

The The The The The The The The **Handler Name** Platformda MO Handler konfigürasyonunu eşsiz bir şekilde tanımlamak için kullanılır.

Bu isim içsel olarak kullanılır:

- Routing configuration configuration
- Handler seçimi
- MO trafik haritası
- Yönetim ve sorun giderme

!!! example
    ```
    MO_HANDLER_INDIA_01
    ```

---

### 2] Channel Type

The The The The The The The The **Kanal Türü** Gelen MO trafiği ile ilişkili telecom numarasını tanımlar.

**Desteklenen Kanal Türleri:**

| Tipi Tipi Tipi Tipi | Açıklama |
|------|-------------|
| **Uzun Kod** | İki yönlü mesajlaşma iletişimi için kullanılan standart bir mobil sayı. |
| **Kısa Kod** | Kısa bir sayısal kod genellikle işletme kampanyaları, oylama sistemleri, abonelikler veya promosyon hizmetleri için kullanılır. |

Seçilen kanal türü operatör veya satıcı konfigürasyonunu eşleştirmeli.

![Manage MO Handler — full configuration form](images/mohandler-02-add-new.png)

---

### 3] Channel Number

The The The The The The The The **Kanal Numarası** MO trafiğinin alındığı gerçek varış sayısını temsil eder.

!!! example
    ```
    567890
    ```

Bu sayı yapılandırılmalıdır **Tam olarak verildiği gibi** Telecom operatörü veya ağ geçidi satıcısı tarafından.

---

### 4] Yerel Endpoint

The The The The The The The The **Yerel Endpoint** iTextPro tarafından otomatik olarak eller yapılandırması oluşturulur.

Bu uç nokta, gelen HTTP MO talepleri için URL almak gibi davranır.

Oluşturulan uç noktası URL genellikle ile paylaşılır:

- SMS Gateway Vendors
- Telecom Operators
- Aggregators
- Üçüncü taraf Platformlar

Satıcı, gelen MO mesajlarını iTextPro platformuna itmek için bu son noktayı kullanıyor.

**Örnek Akış:**

```
Operator/Vendor → Local Endpoint → iTextPro Processing
```

---

### 5] Whitelist IP

The The The The The The The The **Beyaz Liste IP** bölüm MO endpoint'i yalnızca yetkili IP adreslerini kısıtlayarak güvence altına almak için kullanılır.

Sadece yapılandırılmış IP adreslerinden alınan talepler platform tarafından kabul edilecektir.

**Amaç:**

- İzinsiz erişim
- Geliştirilmiş API güvenliği
- Bilinmeyen trafik
- MO endpoint'i kötüye kullanmaktan korumak

!!! example
    ```
    192.168.10.20
    ```

!!! tip
 Birden çok IP operasyonel gereklilikler olarak yapılandırılabilir.

---

### 6] Yöntem

The The The The The The The The **Yöntem Yöntemi** MO istekleri gönderirken satıcı tarafından kullanılan HTTP iletişim yöntemini tanımlar.

**Desteklenen Yöntemler:** <span data-ph="0"></span>, <span data-ph="1"></span>.

#### GET Yöntemi

GET yönteminde:

- Parametreler URL içinde gönderilir.
- Veriler sorgu parametreleri olarak gönderilir.
- Hafif entegrasyonlar için uygun.

!!! example
    ```
    https://domain.com/mo?originator=9876543210&destination=567890&message=TEST
    ```

#### POST Yöntemi

POST yönteminde:

- Parametreler HTTP istek gövdesi içinde gönderilir.
- yapılandırılmış ve daha büyük maaş yüklerini destekler.
- Yaygın olarak modern API entegrasyonu için kullanılır.

**Faydaları:**

- Daha iyi güvenlik
- Daha temiz istek yapısı
- Destekler JSON / XML para yükleri
- Karmaşık entegrasyonlar için uygun

---

## Payload Build

The The The The The The The The **Payload** Bölüm, gelen istek parametrelerinin iTextPro içinde haritalandırılacağını tanımlar.

Doğru para yükü haritası **zorunlu zorunlu zorunlu zorunlu zorunlu zorunlu zorunlu zorunlu** Başarılı MO işleme için. Ücret yükleme parametreleri tam olarak aşağıda belirtildiği gibi yapılandırın:

| Platform Parametresi | Satış veya Parametre |
|--------------------|------------------|
| **Originator** | <span data-ph="0"></span> |
| **Hedef** | <span data-ph="0"></span> |
| **Mesaj** | <span data-ph="0"></span> |

### Payload parametresi Description

#### Originator

The The The The The The The The **Originator** parametre, MO mesajının alındığı gönderici mobil numarasını temsil eder.

!!! example
    ```
    9876543210
    ```

#### Hedef

The The The The The The The The **Hedef** parametre temsil eder **Kısa Kod** veya **Uzun Kod** MO mesajının gönderildiği numara.

!!! example
    ```
    567890
    ```

#### Mesaj

The The The The The The The The **Mesaj** parametre son kullanıcı tarafından sunulan gerçek metin içeriğini temsil eder.

!!! example
    ```
    ASKRK BALANCE
    ```

---

## Save Handler Build

Tüm konfigürasyonları tamamladıktan sonra:

1. Tüm yapısal ayrıntıları doğrulayın.
2. Click on Click on Click **Kaydet Kaydet Kaydet**.

HTTP MO Handler şimdi başarıyla yapılandırılmış ve MO trafiği almaya hazır.

!!! tip "Sonraki Adım"
 Eller kurtarıldığında, bir an yaratmak için devam edin **MO Routing Rule** Gelen MO trafiğinin nasıl filtreleneceğini ve son kullanıcılara teslim olacağını tanımlamak.
