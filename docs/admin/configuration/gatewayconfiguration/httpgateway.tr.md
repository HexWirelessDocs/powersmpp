---
tags:
  - HTTP
  - Gateway
  - Configuration
---

# HTTP Gateway

In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In **Power SMPP**Her ikisini de destekliyoruz **SMPP** ve **HTTP HTTP** Satıcı bağlantı için protokolleri. Sonuç olarak, yönetici SMPP tabanlı bir ağ geçidi veya HTTP ağ geçidi yapılandırma seçeneğine sahiptir. Bu belge, HTTP ağ geçidi konfigürasyonunun bir genel bakışını sağlar. Yöneticilerin anlaşılmasına ve güç SMPP uygulaması içindeki bir HTTP ağ geçidi kurmalarına yardımcı olmak için tasarlanmıştır.

Adının önerdiği gibi, HTTP ağ geçidine dayanmaktadır **Hipertext Transfer Protokolü (HTTP)**. Bu protokol, müşterilerin Power SMPP uygulamasında bir ağ geçidi olarak çalışan bir API aracılığıyla mesaj göndermelerini sağlar.

![Manage Gateway list view](images/httpgw-01-manage-gateway.png)

**Navigation:** <span data-ph="0"></span> <span data-ph="1"></span> <span data-ph="2"></span> <span data-ph="3"></span> <span data-ph="4"></span>.

![HTTP Gateway Detail sections](images/httpgw-02-detail-sections.png)

!!! tip "View Documentation"
 Ne zaman tıklayarak **Yeni Ekle Yeni Ekle Yeni Ekle Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Add Add Yeni Add Add Yeni Add Add Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Yeni Add Yeni Add Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Add Add Yeni Add Yeni Add Add Add Add Yeni Add Yeni Add Add Add Add Yeni Add Add Yeni Add Add Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Add**, ilk seçenek olacak **View Documentation**. Bu belgeyi ağ geçidi konfigürasyonunda bahsedilen terimlerle aşina hale getirmek için tavsiye ederiz.

HTTP Gateway Detay ekranı aşağıdaki bölümlere düzenlenir:

- Gerekli Credentials
- Mesaj Türleri
- Parametreler
- Koşullu Parametreler
- Gateway Özellikler
- Yanıt Özellikler
- Oturum Oturum
- Otomatik Mesaj Teslimatı

---

## Bölüm 1: Gerekli Credentials

Bu bölümde, çeşitli bilgi parçaları gereklidir, örneğin **Gateway Name Name**, **Talep Türü**, **Kimlik Doğrulama**, **Base URL URL**Ve **UDH**.

**Gateway Name Name** - HTTP Gateway için kolay üye bir isim.

**UDH gerekli mi?** - Yayın, **UDH (Kullanıcı Data Header)** Bu ağ geçidinden gönderilen mesajlar için gereklidir. UDH, koncatenasyon mesajları için kullanılır.

**Talep Türü** - HTTP isteğinin türünü belirtir. Olabilir **Basit HTTP**, **REST/JSON**Ya da **SOAP**Farklı istek türleri farklı konfigürasyonlar gerektirir. Genel olarak, Basit HTTP kullanılır <span data-ph="0"></span> Yöntemler, REST/JSON her ikisi için de kullanılabilirken <span data-ph="1"></span> ve <span data-ph="2"></span> Yöntemler.

![Required Credentials form](images/httpgw-03-required-credentials.png)

**Base URL Detay** - HTTP API için temel URL'yi belirtir, **hariç** Diğer tüm parametreler.

!!! example
 API URL'si ise <span data-ph="0"></span>Ardından Base URL'si yapılandırılmalıdır <span data-ph="1"></span>.

**Kimlik Doğrulama** – Power SMPP şu anda üç tür yetkiyi destekliyor:

| # # # # | Tipi Tipi Tipi Tipi | Açıklama |
|---|------|-------------|
| 1 1 1 | **Hiçbir Auth** | Hiçbir yetki gerekli değildir. |
| 2 2 | **Temel Auth** | API'nin güvenli kimlik doğrulaması için bir kullanıcı ve şifre gereklidir. |
| 3 3 | **OAuth 2.0** | Son yetki sürümü, API'nin yüksek güvenliğini sağlamak için belirli bir süre sonra yeni kimlikleri yeniden tanımlamak için kullanılır **OAuth Handler** API. |

![Authentication options](images/httpgw-04-authentication.png)

---

## Bölüm 2: Mesaj Türü

**Mesaj Türü** Yöneticinin satıcı tarafından kabul edilen veri kodlamasının değerini yapılandırabileceği bir isteğe bağlı bölümdür. Her veri kodlama türü için varsayılan değerler, braketlerde belirtilmiştir.

| Tipi Tipi Tipi Tipi | Varsayılan olarak | Amaç |
|------|---------|---------|
| **TEXT** | <span data-ph="0"></span> | Doğru metin mesajları için ağ geçidine özgü mesaj türü. |
| **UNICODE** | <span data-ph="0"></span> | Unicode mesajları için ağ geçidine özgü mesaj türünü haritalayın. |
| **BINARY** | <span data-ph="0"></span> | İkili mesajlar için ağ geçidine özgü mesaj türünü haritalayın. |
| **FLASH** | <span data-ph="0"></span> veya <span data-ph="1"></span> | Flash mesajları için ağ geçidine özgü mesaj türünü haritalayın. |

!!! note
 Ağ geçidinize özel mesaj türlerinizi sistem mesajı türleri ile haritalayın. Uygulayamayan alanları boş bırakın.

![Message Types form](images/httpgw-05-message-types.png)

---

## Bölüm 3: Parametreleri

The The The The The The The The **Parametre parametresi** Bölüm, yöneticinin ağ geçidi satıcısı tarafından sağlanan ağ geçidi ayrıntılarını ve talep parametrelerini yapılandırmasını sağlar. Bu parametreler Power SMPP tarafından yapılır ve API istek verilerini / ilgili ağ geçidi satıcısına mesaj işleme ve teslimat için gönderir.

yapılandırılmış parametreler HTTP isteğinin API iletişimi sırasında nasıl oluşturulacağını ve idam edileceğini tanımlar.

### Yöntem Yöntemi

Power SMPP, API infazı için aşağıdaki HTTP yöntemlerini destekliyor:

#### 1] GET Yöntemi

GET yöntemi, yöneticinin istek parametrelerini yapılandırmasına izin verir **anahtar değerli çift** format. API uygulaması sırasında, tüm yapılandırılmış parametreler doğrudan URL'ye gönderilir **Soru parametreleri**.

Bu yöntem genellikle için kullanılır:

- Basit API talepleri
- URL tabanlı parametre iletim
- Hafif API entegrasyonu
- Legacy HTTP entegrasyonu

!!! example
 <span data-ph="0"></span>

GET yönteminde, Power SMPP aşağıdaki parametre türlerini destekliyor:

##### Ebeveyn Adı

The The The The The The The The **Ebeveyn Adı** Alan temel olarak için kullanılır **SOAP tabanlı** Parametrelerin bir ebeveyn XML node veya istek nesnesi altında gruplandırılması gereken API entegrasyonları.

Bu yapılandırma, yapılandırılmış SOAP istek ödeme yüklerini satıcı API özelliklerine kadar oluşturmaya yardımcı olur.

!!! example
    ```xml
    <SendSMS>
        <username>admin</username>
        <password>test123</password>
    </SendSMS>
    ```
 Yukarıdaki örnekte, <span data-ph="0"></span> Ebeveyn Adı olarak davranır.

##### Header Parametre

The The The The The The The The **Header Parametre** bölüm API infaz sırasında gerekli HTTP başlık değerlerini yapılandırmak için kullanılır.

Bu parametreler genellikle kullanılır:

- Kimlik Hediyeleri
- API Keys
- Authorization Credentials
- Content-Type Tanımları
- Özel Satıcı Headers

!!! example
    ```
    Authorization: Bearer xxxxx
    Content-Type: application/json
    ```

Header parametreleri API iletişimi sırasında HTTP istek başlığı içinde aktarılır.

##### Vücut Parası

The The The The The The The The **Vücut Parası** bölüm HTTP API isteği için gerekli tüm genel istek parametreleri içerir.

Bu parametreler genellikle şunları içerir:

- Mobile Number
- Mesaj Content
- Sender ID
- Şablon ID
- Güvenilirlik ID
- Parametreleri
- Özel Satıcı Parametreleri

For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For **GET** İstekler, bu parametreler API uygulama sırasında sorgu parametreleri olarak talep URL'de gerçekleştirilir.

![Parameters configuration with example rows](images/httpgw-06-parameters.png)

#### 2] POST Yöntemi

The The The The The The The The **POST** Yöntem, yöneticinin ağ geçidini tüm gerekli istek parametrelerini içeride göndererek yapılandırmasına izin verir **vücut isteği** Onları URL'de uygulama yerine. Bu yöntem, büyük miktarda veri, kimlik doğrulama parametreleri, üst düzeyler, belirteçler veya karmaşık para yük yapıları gerektiğinde API entegrasyonları için önerilir.

POST yöntemi kullanarak aşağıdaki avantajları sağlar:

- URL uzunluğu ve karmaşıklığı azaltır.
- URL'de hassas bilgi maruziyetinden kaçınarak güvenliği geliştirir.
- yapılandırılmış ve büyük para yükü verileri destekler.
- Gelişmiş API entegrasyonu ile enables uyumluluğu.
- API gereksinimlerine dayanan esnek istek vücut formatına izin verin.

yapılandırılmış ücret yükü API infazı sırasında HTTP isteği vücudunda iletilir.

##### Payload Type

POST yöntemini seçerken, yönetici aşağıdaki ödeme yük türlerinden birini kullanarak talep yükünü yapılandırabilir:

###### I] Key-Value parametresi [POST FORM DATA]

Bu seçenek, yöneticinin talep yükünü standart olarak yapılandırmasına izin verir **Anahtar değer parametre** format, her parametrenin bir alan adı ve ilgili değeri ayrı olarak tanımladığı yerdir.

Bu ücret yükü türü kabul edilen API'ler için uygundur:

- Form Data
- URL Encoded Parametreleri
- Basit yapılandırılmış istek organları

!!! example
    ```
    Key        Value
    username   admin
    password   test123
    senderid   ABCDEF
    ```

**Faydaları:**

- Konsül etmek ve yönetmek kolay.
- Basit API entegrasyonu için uygun.
- Dinamik parametre haritasına izin verin.
- İstek doğrulama ve sorun gidermeyi basitleştirir.

![POST Form Data Key-Value parameters](images/httpgw-07-post-form-data.png)

###### II)

Bu seçenek yöneticinin geçiş yapmasına izin verir **komple istek vücut** Doğrudan bireysel anahtar değerli parametreleri ayrı tanımlamadan ham içerik olarak.

RAW Payload yöntemi, hedef API'nin gerektirdiğinde kullanılır:

- JSON Payload
- XML Payload
- Plain Text Payload
- Özel Yapılı Veri

Yönetici doğrudan varış noktası API tarafından gerekli olduğu gibi tam ücret yükleme içeriğini yapılandırabilir veya yapılandırabilir.

**Desteklenen RAW Payload Formats:** <span data-ph="0"></span>, <span data-ph="1"></span>, <span data-ph="2"></span>.

!!! example "JSON Payload"
    ```json
    {
      "username": "admin",
      "password": "test123",
      "senderid": "ABCDEF"
    }
    ```

**Faydaları:**

- Karmaşık ve nested maaş yapıları destekler.
- Modern REST APIs ile sorunsuz entegrasyon.
- Özel API istek biçimleri için esneklik sağlar.
- Paraload yapısı ve formatı üzerinde doğrudan kontrol sağlar.

![RAW JSON payload editor](images/httpgw-08-raw-payload.png)

Power SMPP'de yönetici tanımlayabilir **yer sahipleri** Çeşitli değerler için, örneğin <span data-ph="0"></span> Sender ID için, <span data-ph="1"></span> Metin içeriği için, <span data-ph="2"></span> Hedef için ve daha fazlası. Bu, yöneticinin parametreleri için çeşitli dinamik değerleri yapılandırmasını sağlar. Ek olarak, yönetici parametre türü değiştirebilir, bunun olup olmadığını değiştirebilir **Header** veya **Vücut Bedeni** parametre, değerleri yapılandırırken.

---

## Bölüm 4: Koşullu Parametreler

Bölümde **Koşullu Parametreler**Bununla birlikte, uygulama, bir koşulu yapılandırarak yapılandırılan parametrenin değerlerini değiştirmek için bir özelliktir.

![Conditional Parameters](images/httpgw-09-conditional-parameters.png)

Koşullu parametre inşaatı aşağıdaki mantık için yapılır:

> Eğer eğer <span data-ph="0"></span> Seçilen ile <span data-ph="1"></span> maçları <span data-ph="2"></span>Sonra, <span data-ph="3"></span> değiştirilecek <span data-ph="4"></span>.

| Field | Açıklama |
|-------|-------------|
| **Parametre parametresi** | Paraload listesindeki anahtar parametre, koşulun uygulanmasıdır. |
| **Durum** | Kontrol edilmesi gereken koşul türü. |
| **Mevcut Para Değeri** | Seçilmiş parametrenin değeri, durumda karşılaştırılacaktır. |
| **Parametre Değiştirilmiş Olmak** | Yukarıdaki koşulun memnun olup olmayacağı para yükü listesinden gelen anahtar parametre. |
| **Değiştirilmiş Para Değeri** | Durum karşılanırsa anahtar parametreye verilecek yeni değer. |

---

## Bölüm 5: Gateway Properties

**Gateway Properties Build** Yöneticinin HTTP ağ geçidinin sorunsuz çalışması için satıcı tarafından desteklenen yöntemi ve yanıt türünü yapılandırmasına izin verir.

| Emlak | Açıklama |
|----------|-------------|
| **Yöntem Yöntemi** | HTTP ağ geçidine istekleri gönderme yöntemi belirtir. Yönetici, satıcı tarafından desteklenen yöntemi yapılandırabilir: <span data-ph="0"></span>, <span data-ph="1"></span>Ya da <span data-ph="2"></span>. |
| **Yanıt Türü** | Yanıtın ağ geçidinden alınması gereken format: <span data-ph="0"></span>, <span data-ph="1"></span>Ya da <span data-ph="2"></span>. |
| **Fiyatı Dur** | Ağ geçidi için varsayılan fiyat olarak kullanılırken mesajları kullanarak **Blind Routing**. |
| **Kör Routing mi?** | Gateway Cost Price ülke ve ağ için yapılandırılmamış olsa bile yollanan mesajlara izin verin. Böyle durumlarda, **Fiyatı Dur** uygulanacak. |
| **Gateway Time Zone** | Satıcının çalışma süresini uygulamadaki yapılandırın, bunu sağlamak için **Teslimat Receipt (DLR)** Güncelleme süreleri doğru kaydedilir. |
| **Aktif mı?** | Ağ geçidini sağlamak veya devre dışı bırakmak. |
| **Gateway Open / Close Time** | Ağ geçidi için zaman penceresi <span data-ph="0"></span> format. |

![Gateway Properties — Method](images/httpgw-10-gateway-properties-method.png)

![Gateway Properties — Response Type](images/httpgw-11-gateway-properties-response.png)

---

## Bölüm 6: Yanıt Özellikler

The The The The The The The The **Yanıt Özellikler** Uygulamada başvuru için kullanılır **Cevabı harita** Ağ geçidi satıcısından raporlara alındı, sonra güncellemek için kullanılır **Teslimat Receipts (DLRs)**.

Uygulamada mevcut yanıt konfigürasyonu türleri şunlardır:

### 1] JSON veya XML

Satıcı yanıt türünü desteklerse **JSON** veya **XML**Ancak cevap yapılandırması aşağıdaki alanlara göre ayarlanabilir:

| Field | Açıklama |
|-------|-------------|
| **Hata Kodu Alan** | Hata kodunun cevabında bulunduğu alan. |
| **MesajId Field** | Mesaj ID'nin yanıtda bulunduğu alan. |
| **Mesaj Status Field** | Mesaj statüsünün yanıtda bulunduğu alan. |
| **Mobile Number Field** | Yanıtda mobil sayı içeren alan. |

![Response Properties — JSON / XML](images/httpgw-12-response-properties-json.png)

### 2]

Satıcı yanıt türünü desteklerse **TEXT**Ancak yönetici, Yanıt Özellikleri altında ek parametreleri yapılandırmalıdır:

| Field | Açıklama |
|-------|-------------|
| **Key-Value Splitter** | Mani, cevaptan anahtar değerli çiftleri ayırmak ve tanımlamak için kullandı. Bu alan sadece TEXT yanıt türü için kullanılır. Örneğin, alınan yanıt alınırsa, <span data-ph="0"></span>Sonra bölünme olacaktı <span data-ph="1"></span>. |
| **Emlak** | Manif yanıtdaki çeşitli özellikleri ayırmak için kullanılır. Bu alan ayrıca TEXT yanıt türüne de özeldir. |
| **Hata Kodu Alan** | Hata kodunun yanıtda bulunduğu alanı belirtir. |
| **MesajId Field** | Mesaj ID'nin yanıtda bulunduğu alanı belirtir. |
| **Mesaj Status Field** | Mesaj statüsünün yanıtda bulunduğu alanı belirtir. |
| **Mobile Number Field** | Mobil numarayı yanıtdan getirmek için kullanılır. Yönetici, yanıtdaki mobil sayıyı içeren alanı belirtmeli. |

![Response Properties — TEXT](images/httpgw-13-response-properties-text.png)

!!! note
 Yanıt yapılandırmasında, yönetici yukarıda bahsedilen alanların değerlerini barındıran parametre isimlerini yapılandırmalıdır.

!!! example
 Aşağıdaki cevabı düşünün:
    ```json
    { "data": [{
        "message_error_code": 0,
        "message_error_description": "Success",
        "mobile_number": "9174XXXXXXX",
        "message_id": "b349f1c2-5ae9-4076-867e-5fa15044b207"
    }]}
    ```
 Bu JSON yanıtında:

    - The The The The The The The The **Hata Kodu Alan** parametre adı içerecek <span data-ph="0"></span>.
    - The The The The The The The The **MesajId Field** parametre adı içerecek <span data-ph="0"></span>.

Yanıt özelliklerini bir araya geldiğinde **TEXT** Cevap, değerler benzer olacaktır. Ek olarak, aşağıdakileri belirtmek gerekir:

- **Key-Value Splitter** - Yanıtda, değer için <span data-ph="0"></span> Is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is is <span data-ph="1"></span>. The Key-Value Splitter, bu durumda bir kolon olan değerden anahtarı ayırmak için kullanılan kasıtlıdır.<span data-ph="2"></span>). Yani, Anahtar-Value Splitter olurdu <span data-ph="3"></span>.
- **Emlak** Yanıtda, parametreler gibi <span data-ph="0"></span> ve <span data-ph="1"></span> Bir komün tarafından ayrılır (<span data-ph="2"></span>). Bu nedenle, bu parametreleri ayırmak için mülk Splitter olurdu <span data-ph="3"></span>.

Bu konfigürasyon haritaya yardımcı olur ve yanıt türü JSON, XML veya TEXT olup olmadığına bakılmaksızın gerekli alanları yanıtdan çıkarın.

---

## Bölüm 7: Oturum

The The The The The The The The **seans seans seans oturumu** Bağlantı sayısını gösterir ve HTTP Gateway için önerilen seansın **1 1 1**.

| Field | Önerilen Değer |
|-------|-------------------|
| **No. of Sessions** | <span data-ph="0"></span> |

![Session configuration](images/httpgw-14-session.png)

---

## Bölüm 8: Otomatik Mesaj Teslimat

Gateway satıcısı göndermezse **Teslimat Receipts (DLRs)**HTTP ağ geçidi yapılandırması adı verilen bir özellik içerir **Otomatik Teslimat**. Bu özellik, yöneticinin bir durumu yapılandırmasına izin verir, böylece DLR'ler otomatik olarak güncellenecektir.

| Field | Açıklama |
|-------|-------------|
| **Teslimat olarak otomatik olarak Marked mı?** | DLR'nin ağ geçidi satıcısından alınmadığı mesajların teslim durumunu Güncellemeler. Bu durumda, bu durumda, **DLR Status** kullanılacak. |
| **DLR Status** | Otomatik teslimat özelliği etkinleştirilirse mesajlara atanan varsayılan teslimat durumu. Sistem, ağ geçidinden bir DLR'nin yokluğunda teslim edilen mesajları işaretlemesi gerektiğinde kullanılır. Seçenekler: <span data-ph="0"></span>, <span data-ph="1"></span>, <span data-ph="2"></span>, <span data-ph="3"></span>. |

![Automatic Message Delivery](images/httpgw-15-automatic-delivery.png)

!!! info "DLR'leri sorun etmeyen ağ geçidi için kullanışlı"
 Otomatik Teslimatı sadece üst düzey satıcı gerçekten bir DLR geri dönmediğinde. Aksi takdirde, satıcıdan gerçek DLR'lerin raporu kullandığı için devre dışı bırak.
