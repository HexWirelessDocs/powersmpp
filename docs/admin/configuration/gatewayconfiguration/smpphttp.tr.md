---
tags:
  - SMPP
  - Gateway
  - Configuration
---

# Yapılandırma

## SMPP Gateways (MO/MT)

The The The The The The The The **iTextPRO Application** Önceliklere öncelik verir **kullanıcı dostu deneyim** Esnek bir tasarım arayüzü ve basitleştirilmiş bir yapılandırma akışı aracılığıyla. Hedef, CLI komplekslerinden uzaklaşmak ve bir uygulama sahibine bir uygulama olmaktır **Grafik Kullanıcı Interface (GUI)**- temelli çevre. Bir bütünleşik **İletişimci Motor** Tüm geri dönüş komutlarını idare edin, operasyonel görevlerinizi akışlayın.

---

![Manage Gateway](images/httpgateway1.png)

---

The The The The The The The The **"Manage Gateway"** özelliği, kullanıcıları dış bağlantı ile dış bağlantı kurmak için güçlendiriyor **Kısa Mesaj Servis Merkezleri (SMSCs)** via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via via **SMPP** ve **HTTP HTTP** protokolleri.

For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For **SMPP**, a **tek tek tek tek tek bağ** Mobile-Originated (MO), Mobile-Terminated (MT), ve Teslimat Raporları (DLR) operasyonlarına olanak sağlar. iTextPRO destekler **Birden fazla SMPP Gateways**, izin vermek **Red dışı** ve **Maliyet etkisiz routing**.

---

### Yeni bir Gateway yapılandırın

Bir SMPP bağlantı kurmak için:

1. Click Click Click Click Click **"Add New"**.
2. Sizin için verilen kimlikleri girin **ağ geçidi satıcısı** veya **telecom operatörü**.

---

![SMPP Gateway Credentials](images/httpgateway2.png)

---

#### Gerekli Credentials

| Field | Açıklama |
|-------|-------------|
| **Gateway Name Name** | Ağ geçidinizi tanımlamak için kullanıcı dostu bir isim |
| **IP Adresi** | IP from your SMSC/vendor |
| **Sistem ID** | Kullanıcı adınız satıcınız/SMSC |
| **Şifre Şifre** | SMSC'ye kimlik doğrulama için kullanılır |
| **Tx Port / Rx Port / TxR Port** | Ports for 3.2, Alıcı ve Transceiver bağlar |
| **Sistem Türü** | *(Okul)* Sadece satıcı tarafından gerekiyorsa girin |

!!! warning
 Başarılı bir bağlantı sağlamak için tüm değerleri SMSC/vendor belgelerinde kontrol edin.

---

### Gateway Özellikler

![Gateway Properties](images/httpgateway3.png)

SMPP iTextPRO'de en iyi performans için geçit özellikleri:

1. **Alive (İkinciler):** 
 Interval for Interval for *Enquire Link* Oturumu canlı tutmak için.

2. **Gateway Open Time / Close Time:** 
 Operasyon saatlerini tanımlar, genellikle uymaya kullanılır **Yapmayın** Politikalar.

3. **Gateway Encoding:** 
 Karakter, telco/SMSC ile uyumlu seçim ayarladı.

4. **Mesaj-ID:** 
 İzinler arasındaki dönüşüm **Decimal** Doğru DLR için Mesaj-ID formatları.

5. **Zaman Bölgesi:** 
 Tüm raporlar bu seçilmiş zaman bölgesini yansıtacak.

6. **Kayıp Fiyatı Durdurun:** 
 Setleri ayarlar **max izin verilen ağ geçidi maliyeti** Kör routing kullanırken.

7. **İkinci (TPS):** 
 Satıcı kapasitesine dayanarak tanımlamak. 
 **Formula:** <span data-ph="0"></span>

---

### TON/NPI Build

![TON/NPI Setup](images/httpgateway4.png)

- **TON ( Sayı Türü):** 
 SMSC belgelerinde (e.g., International, Alphanumeric, vs.)

- **NPI (Numbering Plan Göstergesi):** 
 Kullanımda Sayısal Standartlar (E.164, ISDN vs.)

- **Oturum:** 
 Tx, Rx ve TxR oturumları satıcı tahsis başına yapılandırın.

---

### Roller & Routing

![Gateway Roles](images/httpgateway5.png)

- **Aktif:** 
 Marks the Gateway as live and ready to Route traffic.

- **Temsil:** 
 Yalnızca bir ağ geçidi varsayılan olarak işaretlenebilir. eşleşen rotalar olmadan Mesajlar buraya gider.

- **Async:** 
 Enables **asynchronous mod** Daha hızlı mesaj için.

- **Blind Routing:** 
 Ülkelere mesaj göndermelerine izin verir **Tanımsız maliyet fiyatları olmadan**.

!!! tip
 Kurulumdan sonra, tıklayın **" Kaydet"** Bir gönderir **on-the-fly require request** - Hiçbir manuel yeniden başlatma gerekli.
