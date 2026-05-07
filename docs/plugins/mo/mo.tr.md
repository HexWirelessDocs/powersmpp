
# MO MO MO

## Tanım Tanımı
MO mesajları (**Mobile Originated** mesajlar) mobil telefon kullanıcıları tarafından başlatılır ve belirli anahtar kelimeleri kullanarak kısa kod numaralarına gönderilir. 
Müşterilerin veya abonelerin doğrudan satıcılar veya uygulamalarla etkileşime girmesine izin verirler.

---

## Süreç Süreci

### Kullanıcı Girişi
Bir müşteri belirli bir anahtar kelime ile özel bir kısa kod veya uzun kod ile bir metin mesajı gönderir.

**Örnek: Örnek:** 
<span data-ph="0"></span> → <span data-ph="1"></span>

### Mesaj Routing
Mesaj, bu kısa kod veya numara ile bağlantılı uygulama veya satıcıya yol açıyor.

---

## Anahtar Noktaları
- Kullanıcılar ve satıcılar arasındaki iki yönlü iletişim.
- Yanıtları tetiklemek için belirli anahtar kelimeler kullanın.
- Özel kısa kodlar veya uzun kodlar aracılığıyla çalışır.

---

## HTTP MO Tutrs Yapın

### Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış
HTTP MO Tutarlar **iTextPro** Gelen MO mesajları satıcılardan alın. 
Payload yapıları satıcılar arasında farklılık gösterebilir.

### Adım 1: Yeni Bir Eller Ekle
1. Click Click Click Click Click **Yeni Eller Ekle**.
2. Harita UI'deki yük parametreleri.

![MO Handler Config](images/mo1.png)

**Önlemler:** 
RESTful API'lerin temel anlayışı.

**Örnek (Vendor: Airtel):**
```json
{
  "originatorAddress": "999563256",
  "destinationAddress": "8754321565",
  "messageContent": "BINGO 101",
  "CustomerId": "669912"
}
```

**iTextPro Config:**
- Yöntem: <span data-ph="0"></span>
- Content Type: <span data-ph="0"></span>
- Originator Key: <span data-ph="0"></span>
- Hedef Anahtar: <span data-ph="0"></span>
- Mesaj Anahtar: <span data-ph="0"></span>

![MO Config 2](images/mo2.png)

---

### Adım 2: Kullanıcı Hesabı için MO Hizmetleri
1. Giriş yap iTextPro → kullanıcı hesabı bulmak.
2. Activate **MO Services** İçinde in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in in **Yönetme Hizmetleri**.
3. MO Number & Keyword:
   - End Date
   - Kanal seçin (MO number)
   - Anahtar Kelime (veya <span data-ph="0"></span> Hepsi için)
   - Durum: Aktif
4. Click Click Click Click Click **Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add**.

![MO Config 3](images/mo3.png) 
![MO Config 4](images/mo4.png)

---

### Adım 3: MO Routing Rule Build
1. Go to Go to Go to Go **MO Routing Rule**.
2. Bir kural oluşturun veya düzenler:
   - Kural Adı, Start/Bit Date
   - Gateway Interface: HTTP/SMPP
   - Koşullar: Originator, Hedef, Mesaj
   - Kullanıcı ve Endpoint: HTTP Webhook veya ESME

![MO Routing](images/mo5.png) 
![MO Routing UI](images/mo6.png) 
![MO Routing Rule](images/mo7.png)

---

## MO Modül Access Access
1. Impersonate/Login to user account.
2. Open Open Open Open **MO Modül** MO mesajları görmek.

![MO Inbox](images/mo8.png) 
![MO Keyword](images/mo9.png) 
![MO Keyword Details](images/mo10.png)

---

## Auto Reply
- MO mesajları için otomatik yanıtlar ayarlayın.

![MO Auto Reply](images/mo11.png)

---

## Bildirimler
- **Email Forwarding** – MO uyarılarını e-posta ile alın. 
- **Mobile Forwarding** – SMS yoluyla uyarıları alın (Ülke kodu dahil).

![MO Mobile Notify](images/mo12.png)

---

## Sub-keyword
Alt anahtar kelimeler ana anahtar kelimeden sonra ikincil tetikleyicilerdir.

**Örnek: Örnek:**
- **Ana Anahtar Kelime:** CAR CAR CAR CAR CAR 
- **Auto-response:** 
 <span data-ph="0"></span>
- **Sub-keyword 1:** EVET <span data-ph="0"></span> 
- **Sub-keyword 2:** Hayır <span data-ph="0"></span>

![MO Sub-keyword](images/mo13.png)

---

## Raporlar Raporları Raporlar Raporlar Raporları
- İhracat MO Excel'ye rapor verir.
- Anahtar kelimeler veya alt anahtar kelimeler tarafından filtre.

**Adımlar:**
1. Go to Go to Go to Go **Raporlar Raporları Raporlar Raporlar Raporları**.
2. Click Click Click Click Click **İhracat Raporu**.
3. Download and customize.

![MO Reports](images/mo14.png) 
![MO Reports 2](images/mo15.png)

---

## MO Webhooks
Gerçek zamanlı MO mesajı belirli bir HTTP uç noktasına teslimat.

**Kurulum:**
1. Enable **HTTP Web Push** ebeveyn hesabında.
2. Go to Go to Go to Go **MO Webhooks** → **Yeni Webhook ekle**.
3. Set:
   - Name Name Name Name Name Name Name Name Name Name Name
   - Endpoint URL
   - Yöntem: GET /POST
   - Handler: MO

**Not:** 
Eğer son nokta ulaşılamazsa, MO kaybolur. Timeout 10 saniyedir.

![MO Webhook](images/mo16.png) 
![MO Webhook Config](images/mo17.png)