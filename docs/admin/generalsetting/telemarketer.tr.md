
# Telemarketer Build

Giriş ile **TRAI DLT düzenlemeleri**, Hindistan'daki SMS trafiği zorunlu bir şekilde takip etmelidir **PE-TM Zinciri** (Principal Entity-Telemarketer zinciri). Bu zincir, mesaj teslimi dahil tüm paydaşların takip edilebilirliği ve düzenleyici uyumu sağlar, dahil olmak üzere **Kullanıcı, Bayilik, Uygulama ve Satıcı**.

Bu düzenlemelere uymak için, uygulama yapılandırılmalıdır **Gerekli Telemarketer bilgilerini gönderin** mesajları üst düzey satıcıya veya SMSC'ye göndermeden önce.

---

## PE-TM Chain Formation Logic

PE-TM zinciri, mesaj teslimi sırasında dinamik olarak inşa edilir **satıcı türü**.

### Mesaj

1. The The The The The The The The **kullanıcı kullanıcısı** Mesajları kendileriyle birlikte gönderir **Entity ID (PEID)**.
2. The The The The The The The The **Başvuru uygulaması** Onu yapılandırır **Telemarketer ID (TMID)**.
3. zincirin son yapısı satıcı türüne bağlıdır.

---

## Satış veya Türler ve Zincir Formasyon

"Aggregator"

 An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An **Aggregator** Mesajı başka bir satıcıya veya SMSC'ye daha ileri götürecek bir orta satıcıdır.

    - Uygulama onu sona erdirir **TMID**
    - The aggregator kendi kendini kınatıyor **TMID2**
    - Mesaj daha sonra bir sonraki umutla ilerliyor

 **Zincir Formasyon:** <span data-ph="0"></span>

    !!! info
 Hashing is **Gerekli değil** Aggregator satıcılar için uygulama seviyesinde.

"Delivery Partner"

 A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A **Teslimat Partneri** Mesajı ellere teslim etmekten sorumlu son SMSC.

    - Uygulama onu sona erdirir **TMID**
    - Son zincir olmalıdır **hashed** Daha önce

 **Zincir Formasyon:** <span data-ph="0"></span>

    !!! info
 hash TRAI'nın güvenlik ve bütünlük gereksinimlerine uyum sağlar.

---

## Uygulamada Telemarketer Kurulum

**Navigasyon Yolu:** <span data-ph="0"></span>

![Telemarketer Configuration List](images/telemarketer1.png)

---

## Kurulum Adımları

1. Click on Click on Click **Yeni Ekle Yeni Ekle Yeni Ekle Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Add Add Yeni Add Add Yeni Add Add Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Yeni Add Yeni Add Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Add Add Yeni Add Yeni Add Add Add Add Yeni Add Yeni Add Add Add Add Yeni Add Add Yeni Add Add Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Add**
2. Seç **Gateway Name Name**
3. girin **Telemarketer ID (TMID)**
4. Configure hashing based on satıcılar type:
    - **Aggregator:** Set Set Set Set **Hashing Active = OFF**
    - **Teslimat Ortağı:** Set Set Set Set **Etkin = ON**
5. **Hash Type:**
    - Temsiller için **SHA-256** (Altı ve TRAI-compliant)
6. Click Click Click Click Click **Kaydet Kaydet Kaydet** yapılandırma işlemini uygulamak için

![Telemarketer Configuration Dialog](images/telemarketer2.png)

---

!!! danger "Önemli Notlar"
    - Incorrect hashing yapılandırması sonucu olabilir **DLT reddedilme** Satıcı veya SMSC tarafından.
    - Sağlam satıcı türü (Aggregator vs Delivery Partner) yapılandırmadan önce doğrulanır.
    - SHA-256, düzenleyici standartları karşılamak için varsayılan hashing algoritması olarak uygulanır.
