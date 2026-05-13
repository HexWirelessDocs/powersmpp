---
tags:
  - HTTP
  - OAuth
  - Handler
  - Configuration
---

# OAuth Handler Build

In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In **HTTP Gateway**Biz destekliyoruz **3 Yazarlarizasyon türü**:

| # # # # | Tipi Tipi Tipi Tipi | Açıklama |
|---|------|-------------|
| 1 1 1 | **Hiçbir Auth** | Hiçbir yetki gerekli değildir. |
| 2 2 | **Temel Auth** | API'nin güvenli kimlik doğrulaması için bir kullanıcı ve şifre gereklidir. |
| 3 3 | **OAuth 2.0** | Son yetki sürümü, API'nin yüksek güvenliğini sağlamak için belirli bir süre sonra yeni kimlikleri yeniden tanımlamak için kullanılır **OAuth Handler** API. |

Bu belgede, gerekli olan tüm adımları ve bilgileri açıklayacağız. **OAuth Handler** HTTP Gateway için yapılandırma.

---

## Navigation

<span data-ph="0"></span> <span data-ph="1"></span> <span data-ph="2"></span> <span data-ph="3"></span>.

---

## OAuth Handler Fields

| Field | Gerekli Gerekli Gerekli Gerekli Gerekli Gerekli Gerekli | Açıklama |
|-------|----------|-------------|
| **Name Name Name Name Name Name Name Name Name Name Name** | Evet Evet Evet | OAuth handler için bir kullanıcı dostu isim. Uygulama içinde farklı OAuth eller tanımlamak ve yönetmek yardımcı olur. |
| **Hediye URL** | Evet Evet Evet | Uygulamanın OAuth token'i talep edeceği URL uç noktası. Satıcı tarafından erişim token elde edilen URL. |
| **Expiry Time** | Evet Evet Evet | Erişim token'in geçerli kalması için dakikalar içinde. Bu dönemden sonra, token sona erecek ve yeni bir tanesi oluşturulacak. |
| **Hediye Expiry Code** | Evet Evet Evet | Token'in sona erdiğini gösteren hata kodu. Bu hata kodu alındığında, sistem token yenilemesi gerektiğini bilecektir. |
| **İstek Yöntemi** | Evet Evet Evet | Hediye URL'den token talep etmek için kullanılan HTTP yöntemi - <span data-ph="0"></span> veya <span data-ph="1"></span>. |
| **Yanıt Türü** | Evet Evet Evet | Hediye URL'den gelen yanıtın alındığı format alınır - <span data-ph="0"></span>, <span data-ph="1"></span>Ya da <span data-ph="2"></span>. |
| **Access Token Field** | Seçmeli Seçmeli Seçmeli Seçmeli | Alan adı erişim token içeren yanıt. Sistem bu alandan gelecekteki istekleri doğrulamak için erişimi alacak. |
| **Yeni Hediye Field** | Seçmeli Seçmeli Seçmeli Seçmeli | Yeni token içeren yanıtdaki alan adı. Yeni token, mevcut kişinin sona erdiği zaman yeni bir erişim elde etmek için kullanılır. Bu alan, satıcının uygulamasına bağlı olarak opsiyoneldir. |

---

## Payload

Bu bölüm yöneticinin tanımlamak için izin verir **Ek anahtar değer çiftleri** Bu, token isteği ile birlikte gönderilmelidir.

| Field | Açıklama |
|-------|-------------|
| **KEY** | Talepte dahil edilecek parametrenin adı. |
| **VALUE** | Talepte dahil edilecek parametrenin değeri. |
| **TerasM TYPE** | parametre türünü belirtir. Ortak parametre türleri içerir <span data-ph="0"></span>, <span data-ph="1"></span>vs. |

!!! example
    - **KEY**: <span data-ph="0"></span>
    - **VALUE**: <span data-ph="0"></span>
    - **TerasM TYPE**: <span data-ph="0"></span> *(Bu parametrenin token talebinin vücuduna dahil edileceğine işaret ediyor)*

Bu yapılandırma, ayarlamaya yardımcı oluyor **OAuth doğrulama** API'leri elde etmek ve ferahlatıcı jetonları otomatikleştirmek için.

---

## Nasıl çalışır

1. Bir mesaj, kullandığı bir HTTP Gateway aracılığıyla gönderilmelidir **OAuth 2.0**Power SMPP ilk olarak geçerli bir erişimin önceden önbellek olup olmadığını kontrol eder.
2. Geçerli bir token varsa, yukarıdaki API çağrısına eklenmiştir (tipik olarak bir an aracılığıyla). <span data-ph="0"></span> Başlık).
3. Geçerli token yoksa - veya token sona ermiş ve yapılandırılmış **Hediye Expiry Code** Ağ geçidi tarafından geri döndü - Power SMPP çağrıları **Hediye URL** Yapı ile <span data-ph="0"></span>, <span data-ph="1"></span>Ve <span data-ph="2"></span> çift.
4. Yanıt parsed using the response is parsed using the the response is parsed using the the response is parsed using the the the the response is parsed using the the the response is parsed using the the the response is parsed using the the the the response is parsed using the the the the response is parsed using the **Yanıt Türü**, **Access Token Field** Kaldırılır ve token önbellek süresi için önlenir **Expiry Time**.
5. Outbound mesaj talepleri şimdi tekrar sona erinceye kadar yeni elde edilen token kullanın.

---

## OAuth Handler'i bir HTTP Gateway'e bağlayın

OAuth Handler'i kurtardıktan sonra:

1. OAuth ile güvence vermek istediğiniz HTTP Gateway açın.
2. Altında **Bölüm 1: Gerekli Credentials**, set **Kimlik Doğrulama** toklanmak için **OAuth 2.0**.
3. andan itibaren **OAuth Handler** düşüş, sadece yarattığınız eller seçin.
4. Ağ geçidi kurtarmak.

HTTP Gateway şimdi yapılandırılmış OAuth Handler'i otomatik olarak elde etmek ve yenilemek için kullanacak - hiçbir manuel token rotasyon gerekli değildir.

!!! tip
 Keep the keep the **Expiry Time** Satıcı tarafından ilan edilen değerden biraz daha kısa (örneğin, set <span data-ph="0"></span> Dakikalar satıcının jetonları son dakika <span data-ph="1"></span> dakikalar). Bu, expiry'nin başlamasından sonra ilk isteğin tetiklendiği yarış koşullarından kaçınır.
