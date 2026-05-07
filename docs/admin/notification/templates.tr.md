
# E-posta Şablonları

## Anahtar Özellikler

### Otomatik İzleme Otomatik İzleme
- **iTextPro** Düzenli aralıklarla uygulamanın kritik parametrelerini düzenli aralıklarla izler.
- Yükselmeden önce potansiyel konuların proaktif tanımı.

### E-posta yoluyla Uyarılar
- Pay sahipleri e-posta bildirimleri aracılığıyla uyarı alırlar.
- Bildirimler önceden gönderilir, paydaşların önleyici önlemleri almalarına izin verir.

### Özel Şablon Yönetimi
- Özelleştirilebilir uyarı şablonları destekler.
- Kullanıcılar gereksinimlerine göre bildirim şablonlarını yönetebilir ve sunabilirler.

### Sistem Değişkenleri Entegrasyon
- Özel şablonlar ilgili sistem değişkenlerini içerebilir.
- Dinamik olarak güncellenen sistem bilgileri aracılığıyla kişiselleştirilmiş iletişim.

---

## Kullanım Kılavuzları

### Şablon Yönetimi
- Belirli iletişim ihtiyaçlarını karşılamak için uyarı şablonlarını özelleştirin.
- Dinamik ve bağlam-aware bildirimleri için ilgili sistem değişkenleri.

### Paydaş Katılım
- Endişeli paydaşların bildirimleri almak için yapılandırıldığını sağlayın.
- Bu e-posta ayarlarının sorunsuz iletişim için doğru şekilde yapılandırıldığı anlamına gelir.

---

## Faydaları Faydaları
- Güvenilirliği ve istikrarı geliştirir **iTextPro** Uygulama.
- Sorun tespiti ve uyarılama için proaktif bir mekanizma sağlar.
- Özelleştirilebilir şablonlar ve sistem değişkenleri kişisel ve bilgilendirici iletişim sağlar.
- Organizasyonların potansiyel zorluklardan önce kalmasına yardımcı olur.

!!! note
 SMTP detayları, e-postaları tetiklemek için bayi hesapları için de zorunludur.

---

## Email Şablon Yönetimi

![Email Templates](images/template1.png)

---

## Bildirim Etkinlikler ve Şablonları

### Aggregate Raporlama Başarısızlık
Kombinasyon hizmeti bilinmeyen bir başarısızlıkla karşılaştığında sorgulandı. 
![Aggregate Reporting Failure](images/template2.png)

### Onay Bildirim
Sender ID ve şablon isteklerinin admin onayına dayanarak. 
![Approval Notification 1](images/template3.png) 
![Approval Notification 2](images/template4.png)

### Onay Dilek Bildirim
Bir bayi / kullanıcı bir Sender ID veya şablon onayı talebi başlatırken sorgulandı. 
![Approval Request Notification 1](images/template5.png) 
![Approval Request Notification 2](images/template6.png)

### Change Password
Bir kullanıcı parolalarını başarıyla değiştirirken sent. 
![Change Password](images/template7.png)

### Kredi Bildirim
Bir kullanıcının mevcut bakiyesi kredi eşinin altındayken uyarılandı. 
![Credit Notification](images/template8.png)

### Kredi Transferi
Kullanıcı veya bayiler tarafından bir kullanıcı hesabına dengenin eklenmesine yönelik. 
![Credit Transfer](images/template9.png)

### Email Post
Gelen bir mesaj (MO) almak için MO e-posta ileriye dönük aktif olduğunda. 
![Email Post](images/template10.png)

### Esme Blacklist
ESME hesabı spam nedeniyle kara listelenmiş olduğunda uyarın. 
![Esme Blacklist](images/template11.png)

### Başarısızlık Gateway
Otomatik mesaj geçişi birincil bir ağ geçidi nedeniyle gerçekleştiğinde sorgulandı. 
![Failover Gateway](images/template12.png)

### Forgot Password
Giriş hesabı şifresini değiştirmek için bir istek olduğunda.Yout when there is a request to change the login account password. 
![Forgot Password](images/template13.png)

### Gateway Blacklisted
Bir SMPP satıcı ağ geçidi /route başarısız bağlayıcı girişimlerden sonra kara listelenir. 
![Gateway Blacklisted](images/template14.png)

### Gateway Price Expiry
Limitli bir oranı olan bir rota tespit edildiğinde. 
![Gateway Price Expiry](images/template15.png)

### İş Onaylandı Bildirim
Bir gönderici kimlik veya şablon isteği yönetici/reseller tarafından onaylanmadığında. 
![Job Disapproved Notification 1](images/template16.png) 
![Job Disapproved Notification 2](images/template17.png)

### Mesaj Queue
Satıcı ağ geçidi kuyruğu eşik sınırı ihlal ettiğinde sorgulandı. 
![Message Queue](images/template18.png)

### Yeni Hesap Tarafından Admin
Yeni bir kullanıcı yönetimden veya işaretlerden eklendiğinde. 
![New Account by Admin](images/template19.png)

### Yeni Hesap Tarafından Bayi
Bir bayi yeni bir kullanıcı veya yeni bir kullanıcı işaretleri eklerken domain bayi kullanıcılarına mesaj vermeyin. 
![New Account by Reseller](images/template20.png)

### Yeni User Email Verification
Yeni kullanıcılar e-posta doğrulama için kaydoldu. 
![New User Email Verification](images/template21.png)

### OTP
Kullanıcı girişleri sırasında OTP doğrulama için değil. 
![OTP](images/template22.png)

### Hizmet Durumu
Bir şeytan / hizmet otomatik olarak kurtarıldığında uyarılandı.

### Hizmet Durdu
Bir şeytan / hizmet kasıtlı olarak durduruldu. 
![Service Stopped](images/template23.png)

### Spam Tespiti
SPAM içeriği tespit edildiğinde uyarılandı. 
![Spam Detection](images/template24.png)

### Kullanıcı Paylaşımı
Müşteri satış fiyatının ebeveyn hesabı tarafından güncellendiği zaman sent. 
![User Selling Update](images/template25.png)

---

Bu bildirimler, geniş bir dizi olayı kapsar, kapsamlı öngörüler ve zaman uyarıları verimli izleme ve yönetim sağlamak için **iTextPro** platform.
