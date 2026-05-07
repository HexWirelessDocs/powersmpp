---
tags:
  - Admin
  - User Management
---

## Yönetim Yönetimi

**iTextPRO'e hoş geldiniz**Ağ geçidiniz verimli belge yönetimine!

iTextPRO admin sitesine erişmekle başlamak için, giriş yapmanız gerekir **Admin URL URL** ve **Giriş bilgileri** Hizmet Teslimat ekibimiz tarafından sağlanan.

Başarılı bir şekilde giriş yaptığınızda, biriniz tarafından selamlanacaksınız **kullanıcı dostu arayüz** Çeşitli navigasyon kontrolleri ile donatılmış. Deneyiminizi başlatmak için birincil navigasyon kontrolü **'Kullanıcı Yönetimi - Kullanıcı Yönetimi.'** Bu menü altındaki ilişkili kontrollerin yalnızca bir kez görünür olacağını unutmayın **Giriş belirli bir kullanıcı adı** Ve vur the **'View'** düğme.

Yönetim bölümünün işlevselliğine derinlemesine bilgi için, bulacaksınız **Kapsamlı açıklamalar** Bu belgenin sonraki bölümlerinde çeşitli kontroller.

---

## Kullanıcı Yönetimi

Selam olsun **Kullanıcı Yönetimi** Sayfa bir esintidir. Sadece tıklayın **'Kullanıcı Yönetimi'** seçenek ve sizi Kullanıcı Yönetimi sayfasına yönlendirecektir.

Devam etmek için, **Kullanıcıya girin** Özel arama kutusu içinde ilgileniyorsunuz ve vurmak **'View'** düğme. Arama kutusu **Otomatik olarak popülates eşleştirme kayıtları** alfabetik sırayla, aramanızı hızlı ve zahmetsiz hale getirin.

![User Management](images/Administration1.png)

---

## Yeni Kullanıcı ekle

Kullanıcı tabanınızı genişletmek için işlem basit. Sadece tıklayın **"Add New User"** Bir yepyeni kullanıcı hesabının oluşturulmasını başlatmak için düğme.

Ancak, kapsamlı bir kurulum sağlamak için, aşağıdaki temel bilgileri vermeniz gerekir.

### **Adım 1: Kullanıcı Detayları**

Upon **"Add New User"** düğme, iTextPRO sizi özel bir sayfaya yönlendirecektir. Aşağıdakide doldurun:

- **İlk Adı**
- **Son Ad**
- **Adres**
- **Kullanıcı Adı** - eşsiz olmalıdır.
- **Şifre Şifre** - En az 8 karakter, en azından:
  - 1. Üst harf mektubu
  - 1 düşük harf mektubu
  - 1 numeric karakter
  - 1 özel karakter
- **E-posta ID** - OTPs ve hoş e-postalar dahil e-posta uyarıları için kullanılır ( Admin SMTP ayarlarına göre).
- **Mobile Number**
- **Zaman Bölgesi** - Etkiler rapor zamanları ve kullanıcı özel görüntüler.
- **Kullanıcı Parası** - Ekran amacı sadece; gerçek zamanlı dönüşüme tabi.
- **Kullanıcı Hesabı Geçerlilik**:
  - **Özel Geçerlilik** - Son bir tarihi tanımlayın.
  - **Lifetime Validity** - No expiry (permanent access).
- **Kullanıcı Hesabı Türü**:
  - **Kullanıcı** - Kullanıcı Paneline Erişim.
  - **Bayilik** - Beyaz-label marka ve fiyat seçenekleri ile hesap.

![Add User Step 1](images/adduser1.png)

---

### **Adım 2: Bildirim Detayları (Okul)**

Uyarılar için birden fazla paydaş e-posta ekleyerek bildirimlerinizi özelleştirin:

- Login OTPs
- Yeni Kullanıcı Doğrulama
- Plan Updates
- Onay Bildirimleri

![Add User Step 2](images/adduser2.png)

Upon **"Yeni Kullanıcı Oluştur"**, a **Hoşgeldiniz e-posta e-posta** gönderilir (gerçekten SMTP konfigürasyonu). iTextPRO başarı ve hediyeleri doğrular:

- **Bunu başka bir zaman yapacağım** – Yeni kullanıcının profiline yönlendirmeler.
- **Tamam! Bunu yapalım** – Başlayın **Kurulum Sihirbazı**.

![Add User Step 3](images/adduser3.png)

---

### **Adım 3: Gateway Ayarları**

routing yönteminizi seçin:

- **Evet Evet Evet** – Bir tane kullanın **Sabit ağ geçidi** Tüm mesajlar için.
- **Hayır, routing kuralı daha sonra ekleyeceğim** - Let the **Main Routing Engine** Dinamik olarak routing ile başa çıkmak.

Ayrıca tıklayabilirsiniz **"Skip"** Devam etmek için.

![Gateway Settings](images/adduser4.png)
![Routing Option](images/adduser5.png)

---

### **Adım 4: SMS Kredi eklemek**

- **Krediler girin** - SMS kredi sayısı.
- **Save Changes**
- **Sonraki Adım**

!!! note
 Tüm kredi işlemleri içeridedir **baz para sadece sadece sadece**.

![Credits](images/adduser6.png)

---

### **Adım 5: Sender ID Policy seçmek**

Select from:

- **Dynamic Sender ID** Kullanıcılar herhangi bir gönderici kimlik kullanabilir (numeric/alphanumeric).
- **Sabit Sender ID** - tutarlılık için önceden tanımlanmış bir gönderici kimlik kullanın.

Click Click Click Click Click **" Kaydet"** Onaylamak için.

![Sender ID](images/adduser7.png)
![Sender ID Settings](images/adduser8.png)

---

### **Adım 6: Set Up SMPP Toptan Müşteriler için Hesap**

SMPP hesabı oluşturmak için:

- Select Select Select Select **Evet Evet Evet**
- Configure:
  - **Sistem ID**
  - **Şifre Şifre**
  - **Beyaz Liste IPs** (Güvenlik için)

!!! tip "En İyi Uygulama"
 Beyaz liste IP'ler SMS spamlarından kaçınmak için.

Use Use Use Use Use Use **0.0.0.0** Açık erişim için (Sistem ID ve şifre yoluyla bağlantı).

![SMPP Setup 1](images/adduser9.png)
![SMPP Setup 2](images/adduser10.png)

---

### **Adım 7: Kullanıcı Hesabını Yönetin**

Kurulum tamamlandıktan sonra, son mesajı 3 seçenekle göreceksiniz:

#### **Seçenek 1: Impersonate**
Hemen kullanıcı olarak kayıt olun - ayrı kimliklere gerek yok.

#### **Seçenek 2: Gelişmiş Billing**
Hız planlarını yönetin:

- **Yeni Satış Fiyatı Ekle**:
  - Ülke Ülke Ülke Ülke
  - MCC/MNC
  - Satış Fiyatı
  - Aktivasyon durumu
- **Import Rate Plan Şablon**

!!! warning "Kayıp Koruma Koruma"
 Emin olun **Satış fiyatı ≥ ağ geçidi maliyeti** Mesaj damlalarından kaçınmak (Los Koruma Politikası).

#### **Seçenek 3: Bu Kullanıcıyı Yönetin**
Erişim **Profil Profili** veya **Kullanıcı Yönetimi** Daha fazla ayarlama için sayfa.

A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A **Hoşgeldiniz e-posta e-posta** otomatik olarak gönderilir.

![Impersonate](images/adduser11.png)
![Rate Plan Setup](images/adduser12.png)
![Manage User](images/adduser13.png)

---

 **Hepiniz setsiniz!** Şimdi tamamen bir kullanıcı yapılandırdın **iTextPRO**Ve kullanıcıları, faturalandırma, bildirimleri ve daha fazlasını yönetmek için hazır - hepsi bir yerden.

# Kullanıcı Yönetimi

The The The The The The The The **Kullanıcı Yönetimi** bölüm gelişmiş kontrol düzeni için birden fazla sekmede düzenlenir. Kullanıcı hesabı ile ilişkili kontrollerin bu bölümü sağlar **Kullanıcı hesabını etkin bir şekilde yönetmede kolaylık**.

Belirli bir kullanıcı bulmak için, sadece **Kullanıcıya girin** Arama kutusunda ve tıklayın **View View View View** düğme. Arama kutusu birbiriyle donatılmıştır **Akıllı özellik** Bu otomatik olarak kutuyu popülates **alfabetik düzende eşleştirme kayıtları**.

Bir görsel temsil için lütfen aşağıdaki rakama bakınız:

![User Management](images/usermanagement1.png)

---

## User Management Tabs Detayları

### İlk Row Seçenekleri

#### **Immanation**
- **Açıklama:** Bu seçeneği seçmek size izin verir **Bir kullanıcı için oturum açma veya yönlendirme** Onların hesabına.
- **Kimlik:** girin **admin** doğrulama için.
- **Not:** Kullanıcı hesabı bir bakışta açılır **Yeni sekme** Aynı tarayıcı penceresinde, kolaylaştırıcı **Paralel yönetim** Hem kullanıcı hem de yönetici hesapları.

#### **Hızlandırma Planı**
- **Fonksiyonellik:** Bu hiperlink sizi yönlendiriyor **User Rate Plan Plan** Sayfa.
- **Amaç:** Configure **Ülkeler ve ağlar için fiyatlar satıyor**.

#### **Durum durumu**
- **Kullanım:** **Activate veya deactivate** Bir kullanıcı/reseller hesabı.
- **Sonuç:** devre dışı kullanıcılar **İçeri girilemez**.

#### **Delete this User**
- **Eylem:** Sürekli olarak **Bir kullanıcı hesabı silmek**.
- **Caution:** Deleted users **restore edilemez**.

---

### İkinci Row Seçenekleri

#### **Profil (Details included)**

- Kullanıcı Adı 
- Kullanıcı kimliği 
- Mobile Number 
- E-posta ID *(iletişim ve uyarılar için kullanılır)* 
- Zaman Bölgesi 
- Kullanıcı Önceliği *(Hazır mesajları için)* 
- Hesap Rolü *(Reseller veya Kullanıcı)* 
- Kullanıcı Parası *(display para, dönüşüme tabi)* 
- Validity Up-to *(Müşteri veya Yaşam Süresi)* 
- Son Giriş IP 
- Last Login Date Time 

**Fonksiyonellik:** Access and manage **Temel kullanıcı profili bilgisi**.

#### **Şifre sıfırlama Şifre**
- **Eylem:** Şifreyi sıfırlamak için **Kullanıcılar veya bayi hesapları**.

!!! note
 Kullanıcı Yönetimi bölümündeki tüm eylemler bir kişiye katkıda bulunur **Kapsamlı ve basitleştirilmiş kullanıcı hesabı yönetimi** deneyim. Daha fazla ayrıntı için, iTextPRO kullanıcı kılavuzuna danışın.

---

## Ek Privileges ve Gelişmiş Ayarlar

![Advanced Privileges](images/usermanagement2.png)

### **User Lock Status**
- **Açıklama:** Bu seçeneği enabling **Kullanıcı hesabı kilitler**, giriş faaliyetlerini kısıtlayın.

### **User Spam Validation**
- **Açıklama:** etkinleştirildiği zaman, iTextPro **Kullanıcı SPAM anahtar kelimelerini doğrular** Her kampanya için. Güvenilen kullanıcılar güvenebilir **Override** Bu, toggletan vazgeçerek.

### **Global Spam Validation**
- **Açıklama:** Enables the application to **Global SPAM anahtar kelimelerini doğrulama** kullanıcı kampanyaları için. Güvenilen kullanıcılar bu geçerliliği abartabilir.

### **API IP Validation**
- **Açıklama:** Bu seçeneği ihlal etmek iTextPRO sağlar **Beyaz listelenmiş IP adresini doğrular** API isteklerini işlemeden önce.

### **SMS HTTP Web Push**
- **Açıklama:** etkinleştirildiği zaman, uygulama **DLR kopyaları** Kullanıcı hesabında yapılandırılan HTTP uç noktası URL'ye webhooks seçeneği.

### **WhatsApp HTTP Web Push**
- **Açıklama:** Enabling this toggle düğmesi, yöneticinin etkinleştirmesine izin verir **WhatsApp webhook seçeneği** Kullanıcı, yapılandırılmış uç noktalarına WhatsApp DLRs/Conversations almak için.

![WhatsApp HTTP Web Push](images/usermanagement14.png)

### **Maskeli Mobile Number Show**
- **Açıklama:** Gösteri maskeli sayı, yöneticinin özelliğinin etkinleştirilmesine izin verir **Sayı maskeleme**. Bu toggle düğmesi aktif olarak belirlendikten sonra, kampanyaların başvurudan başlatıldığı tüm mobil sayılar, onların **Son dört basamak** Mobil sayı için maskelenecek.

![Show Masked Mobile Number](images/usermanagement15.png)

!!! example
 Kullanıcının Kampanya Raporunda maskelenen rakamlar sanki görünür <span data-ph="0"></span>.

![Masked Number in Report](images/usermanagement16.png)

### **Kullanıcı Over çok satan Threshold**
- **Açıklama:** Enables configuration of an an **Çok satan Threshold limiti** Kullanıcılarda, tahsis edilen bakiyenin ötesinde belirtilen miktarda tüketmelerine izin verin.

**Örnek: Örnek:** 
Eğer eşik ayarlanırsa **500 EUROS**, kullanıcı için tüketebilir **500 EUROS daha fazla** tahsis edilen dengeden daha fazlası.

---

## Gelişmiş Ayarlar

![Advanced Settings](images/usermanagement3.png)

### **Open Sender**
- **Açıklama:** Enables end-users bir mesaj göndermek için **dinamik gönderen ID** (numeric veya alfanumeric).

### **Open Şablon**
- **Açıklama:** Enables kullanıcıları kullanmak için **dinamik içerik** Açık şablonlara izin vererek mesajlarda.

### **Skip Profile OTP**
- **Açıklama:** Gönder **Kullanıcının kayıtlı e-posta kimliğine OTP** Profil güncelleme faaliyetleri için.

### **Skip Login OTP**
- **Açıklama:** Gönder **Kullanıcının kayıtlı e-posta kimliğine OTP** Giriş faaliyetleri için.

### **DLR Compensation İzin Ver**
- **Açıklama:** İzin verir veya rahatsız eder **DLR tazminat tazminat** Çocuk domaini için.

### **DLR Compensation**
- **Açıklama:** Bu özellik, yöneticinin mesajların tazminatını uygulayarak ve DLR'yi uygulama uygulamasından bir miktar ek kazanç elde etmesini sağlar. **Mesajları ağ geçidine göndermeden önce**.

![DLR Compensation](images/dlrcompensation1.png)

**Kurulum:**

- **DLR durumu:** tazminatın uygulandığı mesajlar için uygulanması gereken mesaj statüsünü seçin.
- **Yüzde:** Hangi tazminatın uygulanması gereken yüzde değerini ekleyin.
- **Hata Kodu:** Duruma karşı hata kodu yapılandırın, bu yüzden aynı raporlarda güncellenecektir.
- **Threshold SMS Limit:** DLR tazminatını uygulamak için hedef sayı eşini tanımlar. Eşlik ulaştıktan sonra, tazminat yapılandırmaya göre uygulanacaktır.

!!! note
 Web arayüzü için eşik sınırı kampanya temelinde ve SMPP/API durumunda, eşik günlük olarak çalışacaktır.

![DLR Compensation Controller](images/dlrcompensation2.png)

??? example "DLR Compensation Örnek Örnek"
 Bir kullanıcı, aşağıdaki yapılandırma ile 2000 numara üzerinde bir kampanya başlattı:

    - **DLR Compensation:** 20 Yüzde
    - **Threshold Limit:** 1000 1000

 yapılandırmaya gelince:

    - 2000 mesajların dışında, sadece **1600 mesaj** Ağ geçidi satıcısına gönderilecek.
    - For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For **400 mesaj**, iTextPRO üretir **Otomatik sahte DLRs**400 mesaj için kârlılığınızı maksimize etmek.

 Eğer kullanıcı bir kampanya gönderirse **1000> mobil sayılar** (below eşi) **DLR tazminatı uygulanmaz**.

---

## Aktif Hizmetler

Bu bölümden oluşur **iTextPRO**Bu eklentilerin olması gerekiyor **Ayrı ayrı ayrı ayrı ayrı ayrı ayrı ayrı ayrı tercih edildi** Paketlenmiş uygulamanın bir parçası olmadıkları için.

![Active Services](images/activeservices1.png)

**Aktif Hizmetler Ekran:** Şu anda etkinleştirilen eklentileri göster. Ayrıca, yönetici, takvatan düğmesinden eklentileri etkinleştirebilir veya devre dışı bırakabilir.

### 1. **MO (Mobile Originator)**
- **Fonksiyonlar:** Activates the the **MO hizmeti** kullanıcılar için.
- ITextPRO+ bir kez daha alır **Gelen mesaj (MO)**İçinde görünüyor **user's inbox Report**.
- Mesajlar öne çıkabilir **SMPP, HTTP it, email**, veya tetikleyici **Otomatik yanıtlar**.

### 2. **Akıllı SMS**
- **Fonksiyonlar:** Activates the the **Akıllı SMS** özellik.
- Uzun URL'leri dönüştürmek **kısaltıl akıllı bağlantılar**.
- Tracks:
  - Kullanıcının Kullanıcısı **mobil numara**,
  - **IP adresi**,
  - **Cihaz detayları**,
  - **Geolok**.

### 3. **SMS için e-posta**
- **Fonksiyonlar:** dönüştürücüler **SMS mesajları**e-posta ağ geçidi aracılığıyla iletişim etkinleştirin.

### 4. **WhatsApp WhatsApp WhatsApp**
- **Fonksiyonlar:** Bu, olanak sağlar **WhatsApp hizmetleri** Kullanıcıya.
- Eklenti etkinleştirildikten sonra, WhatsApp modülü uygulamada görünecektir.
- Kullanıcılar iş hesabını başvuruya bağlanabilirler.
- şablonları ekleyin, DLR ve Talks için webhooks yapılandırın.
- API'ler API'ler aracılığıyla mesajları göndermek için alın.

---

## Sender ID

The The The The The The The The **Sender ID** sekme, kullanıcıların posta kimliklerini doğrudan yapılandırmasını sağlar. Ekranlar:

- **Pending Pending**
- **Onaylanmış Onaylanmış Onaylanmış Onay Onay Onaylandı**
- **Rejected** gönderen IDs

Accessible via the **"View Sender ID"** bağlantı.

![Sender ID](images/usermanagement6.png)

To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To To **Add a Sender ID**:

- Click Click Click Click Click **Yeni Ekle Yeni Ekle Yeni Ekle Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Add Add Yeni Add Add Yeni Add Add Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Yeni Add Yeni Add Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Add Add Yeni Add Yeni Add Add Add Add Yeni Add Yeni Add Add Add Add Yeni Add Add Yeni Add Add Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Add**
- Define the the **Sender ID** ve **amaç amacı**
- Click Click Click Click Click **Kaydet Kaydet Kaydet**

gönderen ID (status: **onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış onaylanmış**) kullanıcı hesabına eklenecektir.

![Add Sender ID](images/usermanagement7.png)

---

## Şablon

The The The The The The The The **Şablon** Bölüm, kullanıcıların mevcut şablonları görmelerini sağlar. Her şablonun **Durum durumu** ( onaylanmış, bekleyen, reddedilmiş) açıkça işaretlenmiştir.

![Templates](images/usermanagement8.png)

---

## Mesaj Detayları

Kullanıcılar anlayış kazanır **Son üç kampanya mesajı** ve onların **Duruma dayalı istatistikler**, değerlendirme yardım **Performans kampanyası**.

![Message Details](images/usermanagement9.png)

---

## Krediler

The The The The The The The The **Krediler** sekme şovları:

- **Kullanıcının mevcut dengesi**
- **İşlem tarihi**

Kullanıcılar hesabı bakiyelerini hesap üzerinden yönetebilir **"Add More Credit"**:

![Credits](images/usermanagement10.png)

Kredi eklemek için:

- Select Select Select Select **hizmet türü**
- Enter Enter Enter Enter Enter Enter girin **Ödeme detayları**
- Konaklamayı paylaşın **Kredi miktarı**

!!! note
 Krediler eklenmelidir **Temel para birimi**.

![Add Credit](images/usermanagement11.png)

---

## Filtre

The The The The The The The The **Filtre** Seçenek, kullanıcıların kullanıcıların kullanıcıların kullanıcılara izin vermesine izin verir **beyaz liste mobil sayılar**, sağlamak **DLR tazminatı uygulanmaz** Onlara.

Mobil sayılar ekleyin **Ülke kodları** Kolayca.

![Filter](images/usermanagement12.png)

---

## MT Routing

The The The The The The The The **MT Routing Rule** önemli bir özelliktir. You can:

- Create Create Create Create Create Create **Kuralları** SMS trafiğini yönlendirmek için
- Başvuru:
  - **Web arayüzü**
  - **APIs**
  - **SMPP gönderimleri**

Kullanıcılar ayrıca yapılandırılabilir **Sabit ağ geçidi kuralları**, oto-popül girişleri içeri **Main Routing Engine**.

!!! tip
 Sabit bir ağ geçidi oluşturmak isteğe bağlıdır, ancak geliştirir **Verimlilik**.

![MT Routing](images/usermanagement13.png)

---

## Hızlandırma Planı

The The The The The The The The **Hızlandırma Planı** seçenek yöneticinin yapılandırmasına izin verir **Satış fiyatı** kullanıcı için.

**Satış Fiyatı:** Sayı yöneticisi, kullanıcılarına mesaj başına şarj edilecek, satış fiyatı olacaktır.

Kullanıcıya bir satış fiyatı eklemek için aşağıdaki adımları izleyin:

**Adım 1:** Yönetime git >> Kullanıcı Yönetimi >> Kullanıcı Yönetimi >> Arama Kullanıcı >> **Hızlandırma Planı**.

![Manage Rate Plan](images/rateplan1.png)

**Adım 2:** Fiyat satmak için uygun yöntemi seçin.

### 1) Yeni Satış Fiyatı Ekle

Bu, yöneticinin bir-by-one'yi kullanıcı için Ülke ve Ağlara satmasını sağlar.

Interface Type'ı seçin: **TÜM** veya **SMPP**

![Add New Selling Price](images/rateplan2.png)

#### a) ALL Interface

Eğer arayüz ALL olarak seçildiyse, yönetici Ülke ve Ağı belirtmeli, sonra satış fiyatı. Tüm detaylar eklendikten sonra, tıklayın **ADD** yapılandırmayı kurtarmak için.

![ALL Interface](images/rateplan3.png)

#### b) SMPP Interface

Interface SMPP olarak seçildiyse, yöneticinin belirtmek gerekir **SMPP85 adı veya ESME adı**Bu nedenle, fiyat planı bu özel SMPP hesabı için uygulanabilir olacaktır. Sonra Ülke ve Ağı ve satış fiyatı belirt. Tüm detaylar eklendikten sonra, tıklayın **ADD** yapılandırmayı kurtarmak için.

![SMPP Interface](images/rateplan4.png)

!!! info "ALL vs SMPP Interface"
 **TÜM** Tüm arayüzlerden başlayan mesajları gösterir (Web, API ve SMPP). **SMPP** Kullanıcının SMPP arayüzü kullanarak trafik gönderdiğinde bir oran planı gösterir. SMPP'ye özel satış fiyatı yapılandırılmıyorsa, mesajlar ALL için yapılandırılan fiyatla işlenecektir.

![Rate Plan List](images/rateplan8.png)

### 2] İthalat Puanı

Bu seçenek, yöneticinin mevcut tüm oranları ithal etmesine veya bir seferde kullanıcı hesabına fiyatlar hazırlamasına izin verir. Kullanıcı hesabına birkaç satış fiyatı eklemek için iterasyonları azaltacaktır.

**Adım 1:** Hız planı seçin
**Adım 2:** Admin arayüzü de seçebilir (ALL veya SMPP)
**Adım 3:** Mevcut herhangi bir satış fiyatı yazma seçeneği.
**Adım 4:** Satış fiyatını kullanıcı hesabına eklemek için İthalat düğmesine tıklayın.

![Import Rate Plan Template](images/rateplan6.png)

### Kullanıcı Değil

Ne zaman satış fiyatı yönetici tarafından güncellenirse, bir e-posta, konu satırı ile kullanıcı hesabında kayıtlı e-postaya gönderilir. **"Pricing Update Bildirim - Messaging Fiyatlarınız Revized"**.

Bu e-posta, uygulamada yapılandırılan tüm satış fiyatları için mükemmel dosyaları içerir.

Ayrıca, yönetici/Reseller tıkılabilir **Kullanıcı Değil** Kullanıcıya e-postayı herhangi bir e-posta almamaları durumunda yönlendirmek için düğme.

![Notify User](images/rateplan5.png)

---

## Kullanıcı Yaratılışı - Billing Mode

sırasında **kullanıcı oluşturma**Eğer **Invoicing modülü** Uygulamada etkinleştirilir, yönetici yapılandırmalıdır **Billing Mode** kullanıcı için. Seçilen fatura modu, mesaj kullanımının nasıl tahsil edildiğini ve faturaların nasıl oluşturulduğunu belirler.

![Billing Mode](images/billingmode1.png)

Aşağıdaki fatura modları mevcuttur:

"Pre ücretli"

 Bir kullanıcı yapılandırıldığında **Pre ücretli**:

    - Yöneticinin sahip olması gerekir **Bir fatura manuel olarak oluşturmak**.
    - Fatura miktarı olmalıdır **Kullanıcının hesabına yatırıldı**.
    - Sadece fatura iddia edilir ve denge mevcut olduğunda, kullanıcı başvurudan mesaj gönderebilir.
    - Mesaj gönderme, mevcut ücretli bakiyeye göre sınırlandırılır.

"Post ücretli"

 Bir kullanıcı yapılandırıldığında **Posta ücretsiz**:

    - Yöneticinin sahip olması gerekir **Bir overdraft limit tayin et** Kullanıcıya.
    - Uygulama uygulanacak **Otomatik olarak faturalar üretir** Buna dayanarak, **Billing Cycle**.
    - Kullanıcı, overdraft limitine kadar mesajları göndermeye devam edebilir.
    - Billing, fatura döneminde gerçek kullanımlara göre hesaplanır.

!!! warning "Anahtar Notları"
    - The The The The The The The The **Billing Mode** Yalnızca Invoicing modülü aktif olduğunda geçerlidir.
    - Billing configuration doğrudan kullanıcı mesaj teslimatını ve fatura nesillerini etkiler.
    - Proper overdraft sınırları ve fatura döngüleri, hizmet kesintisinden kaçınmak için ücretsiz kullanıcılar için yapılandırılmalıdır.
