
## Gateway Hata kodları

![Gateway Error Codes](images/error1.png)

**Gateway Hata kodları** iTextPRO, yanıt mesajlarını yorumlamanıza ve yönetmenize izin verir **Kısa Mesaj Servis Merkezi (SMSC)** Mesaj teslimi başarısız olduğunda. Bu özellik teslimat başarısızlıkları üzerinde görünürlüğü artırır ve belirli hata kodlarına dayanan kredi geri yüklemelerini sağlar.

---

![Configure Error Codes](images/error2.png)

### 1. Genel bakış
SMSC bir mesaj gönderemediğinde, geri döner **non-zero hatası kodu** Referans mesajı statüsü ile birlikte. Bunlar olarak adlandırılır **Gateway Hata kodları**.

### 2. Amaç
iTextPRO, yöneticilerin bu hata kodlarının yapılandırılmasını ve haritalanmasını sağlar. Ne zaman bir ne zaman **Teslimat Raporu (DLR)** alındı, iTextPRO yapılandırmayı kontrol eder ve:
- Ekranlar a **Özel hata-tag**
- Map it to a a **standart SMPP statüsü** 
Bu bilgiler her ikisinde de gösterilir **Admin Admin Admin** ve **Kullanıcı Raporları**şeffaflığı geliştirmek.

### 3. Önkoşullar
yapılandırmadan önce, bir tane alın **Gateway Error Code Listesi** SMSC'nizden.

---

### 4. Kurulum Adımları

#### A. Gateway Selection
Hata kodunu yapılandırdığınız için ağ geçidi seçin.

#### b. Hata Kodu
girin **Belirli hata kodu kodu kodu kodu** SMSC'nizden alındı.

#### c. Display Error Tag
De ki: **Referans durumu** veya SMSC'den isim (örneğin, <span data-ph="0"></span>, <span data-ph="1"></span>).

#### d. Standart Hata Kodu (Mapped)
Standart SMPP statüsünden birine hatayı haritalayın:
- <span data-ph="0"></span>
- <span data-ph="0"></span>
- <span data-ph="0"></span>
- <span data-ph="0"></span>
- <span data-ph="0"></span>

#### E. Hata Açıklama
Bir sağlayın **kısa açıklama** Hata etiketinden. Bu, gösterilecek **Kullanıcı Raporları** Teslimat durumunu anlamak için yardım etmek.

#### f. Aktif
Hata kodunu yakalamak **veya kapalı** Gerekli olarak.

#### g. Credit Rollback
Bu seçeneği enable **roll back user kredi** Otomatik olarak bir mesaj haritalanmış hata kodu ile başarısız olursa.

---

### 5.

- Kullanın **Bulk Upload** Birden fazla hata kodu aynı anda yapılandırın.
- Click Click Click Click Click **"Bulk Upload"**Sonra:
  - **Örnek Dosyayı İndirin**
  - **Harita sütun başlıkları** In the import Sihirbazı

---

### 6. gönder
Bir kez yapılandırıldığında, tıklayın **"Submit"** Seçilen ağ geçidi için hata kodlarını kurtarmak için.

 **Not:** 
Proper hata kodu konfigürasyonu izlemeyi geliştirir ve kesin takip sağlar **Mesaj teslimat başarısızlıkları**, **geri dönüş eylemleri**Ve **raporlama doğruluk**.

---
