---
tags:
  - MO
  - Routing
  - Rules
  - Configuration
---

# MO Routing Rule

## Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış

**MO Routing Kuralları** iTextPro, gelen MO mesajlarının nasıl belirleneceğini, filtrelenmiş ve platformda rotalanmış olduğunu tanımlamak için kullanılır.

Posta kuralı belirler:

- Hangi gelen MO trafiği işlenmelidir
- Hangi anahtar kelime routing tetiklenmelidir
- Hangi kullanıcı MO trafiğini almalıdır
- Hangi arayüz türü teslimat için kullanılmalıdır

MO Routing Kuralları, yapılandırılan sistemle birlikte çalışır **HTTP MO Handler**.

---

## Navigation Path

<span data-ph="0"></span> <span data-ph="1"></span> <span data-ph="2"></span> <span data-ph="3"></span>.

![Manage MO Routing Rules list](images/morouting-01-list.png)

---

## MO Routing Rule Parametreleri

Aşağıdaki parametreler routing kuralı oluştururken yapılandırılmalıdır.

## Genel Parametreler

### 1] Kural Adı

The The The The The The The The **Kural Adı** platformun içinde MO Routing Rule'i eşsiz bir şekilde tanımlar.

Bu isim için kullanılır:

- Kural yönetimi
- Trafik izleme
- Yönetim Yönetimi
- Sorun Giderme

!!! example
    ```
    MO_ROUTE_KEYWORD_01
    ```

---

### 2] Lifetime

The The The The The The The The **Lifetime** parametre routing kuralının geçerliliğini tanımlar.

**Kullanım:**

- Geçici kampanyalar için kullanılabilir
- Zaman temelli MO routing
- Sınırlı zamanlı hizmetler için kullanışlı

!!! tip
 No expiry gerekli değilse, bu alan boş bırakılabilir.

---

## Gateway Interface Build

### Handler

The The The The The The The The **Handler** Alan daha önce platformda yapılandırılmış HTTP MO Handler seçmek için kullanılır.

Bu eller tüm MO talepleri routing koşullarını eşleştirecektir. Eller, satıcı MO'yi gönderdiği durumlarda kullanılacak. **HTTP bağlantısı**.

### Gateway Gateway

Satıcının desteklediği durumlarda, **SMPP** MO vuruşlarını göndermek için protokol, o zaman MO Routing kuralının oluşturulması sırasında yöneticinin seçmesi gerekir **Gateway Gateway** Doğru ağ geçidini doğru ağ geçidinden almak için doğru ağ geçidi seçin.

**Amaç:**

- Linkler MO trafiği doğru uç nokta ile
- Önler gelen kanalla geziyor
- Enables message processing iş akışı

![Add New MO Rule — General Parameters & Gateway Interface](images/morouting-02-general.png)

---

## Routing Koşulları

Routing koşulları tanımlar **filtreleme mantığı** Gelen MO trafiği için. Platform bu koşulları MO talebini işlemeden veya yönlendirmeden önce değerlendirir.

### 1] Originator Durum

The The The The The The The The **Originator** Durum filtrelemeyi gönderen mobil numaraya göre tanımlar.

**Örnek Yapılandırma:** <span data-ph="0"></span>

Selecting **Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any Any** MO mesajları tüm gönderileyici sayılardan sağlar. Özel gönderici filtreleme de gerekirse yapılandırılabilir.

---

### 2.

The The The The The The The The **Hedef** Durum, kısa Kod veya Long Code numarasını tanımlar.

| Field | Değer değeri |
|-------|-------|
| **Durum Türü** | <span data-ph="0"></span> |
| **Örnek Örnek Örnek Örnek Örnek Örnek Örnek** | <span data-ph="0"></span> |

Routing kuralı, yalnızca gelen MO mesajının yapısal varış noktası numarasında alındığı konusunda tetiklenecektir.

---

### 3) Mesaj

The The The The The The The The **Mesaj** Durum anahtarlama kriterlerini tanımlar.

| Field | Değer değeri |
|-------|-------|
| **Durum Türü** | <span data-ph="0"></span> |
| **Örnek Anahtar Kelime** | <span data-ph="0"></span> |

Routing kuralı, yalnızca gelen mesajın yapısal anahtar kelime ile başladığını tetikleyecek.

!!! example
 Gelen bir mesaj için <span data-ph="0"></span>Ancak mesaj başladığından beri <span data-ph="1"></span>Ancak routing kuralı MO isteği ile işlem yapacaktır.

![Routing Conditions and User / Endpoint selection](images/morouting-03-condition-user.png)

---

## Kullanıcı ve Endpoint Mapping

### 1] Kullanıcı

Seç **kullanıcı hesabı** MO trafiğinin haritalanması ve teslim edilmesi gerekene.

Bu haritalama, doğru kullanıcının gelen MO mesajlarını almasını sağlar.

### 2] Kullanıcı Interface Type

The The The The The The The The **User Interface Type** MO mesajının routing sonrası nasıl ilerlemesi gerektiğini tanımlar.

**Desteklenen Interface Türleri:**

| Tipi Tipi Tipi Tipi | Açıklama |
|------|-------------|
| **Seçilmedi** | Hiçbir arayüze özgü routing uygulanacak. |
| **ESME** | MO trafiğini SMPP bağlantı üzerinden rotalar. Genellikle kullanıcı SMPP protokolü ile bağlantılı olduğunda kullanılır. |
| **Webhook** | MO trafiğini dış bir HTTP API uç noktasına yönlendirir. Yaygın olarak CRM entegrasyonları, üçüncü taraf uygulamaları, web tabanlı işlem sistemleri ve API tabanlı iş akışları için kullanılır. |

---

## Kaydet Routing Rule

Tüm routing parametrelerini yapılandırdıktan sonra:

1. Routing koşullarını onaylayın.
2. Anahtar kelime yapılandırmasını uygulayın.
3. Click on Click on Click **Kaydet Kaydet Kaydet**.

MO Routing Rule şimdi MO trafik işleme için başarıyla yapılandırılmış ve aktif.

!!! tip "Doğrulama"
 Kuralı tasarruf ettikten sonra, yapılandırılan koşulları karşılayan bir test MO mesajı gönder (sender izin verdi, doğru varış numarası, yapılandırılmış anahtar kelime ile başlayan mesaj) ve kullanıcının MO inbox veya webhook endpoint loglarını kontrol ederek kuralı onaylayın.
