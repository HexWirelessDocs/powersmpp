
## ESME Blacklist Rule

The The The The The The The The **ESME Blacklist Rule** iTextPRO, SMPP sunucunuzu rogue veya yanlış yapılandırılmış ESME müşterilerinden korumak için proaktif bir koruma olarak hizmet vermektedir. Bu müşteriler, tekrarlanan veya anormal komut talepleri nedeniyle performans bozulmasına neden olabilir. Bu kurala dayanarak, yöneticiler yönetebilir **otomatik olarak siyah liste** şüpheli müşteriler ve daha fazla hasarın önlenmesi.

---

### Amaç

Bir rogue ESME kullanıcısının bir tehdit oluşturduğunu senaryolarda - yanlış uygulama veya istenmeyen yüksek frekanslı taleplerden ne - bu kural, iTextPRO'in bu kullanıcıdan kalıcı olarak düşmesine olanak tanır, bu kullanıcının isteklerini sürdürmesine olanak sağlar. **Sunucu stabilitesi ve bütünlüğü**.

---

### Yapı Seçenekleri

![Blacklist Rule Setup](images/blacklist1.png) 
![Blacklist Rule Fields](images/blacklist2.png)

Yeni bir ESME Blacklist kuralı yapılandırmak için:

1. **Kural Adı**: 
   - Siyah liste kuralı için tanımlayıcı, dost bir isim girin (örneğin, <span data-ph="0"></span>).

2. **Kullanıcı**: 
   - ESME kullanıcı hesabı seçin kuralın izlemesi gerekir.

3. **ESME System ID**: 
   - Özelliği seçin **Sistem ID** ESME kullanıcısının.

4. **Komut Türü**: 
   - İzlemek için komut türünü seçin:
     - **Enquire Link**
     - **Bin**

5. **Time Interval**: 
   - aralıkları ayarlayın:
     - Saatler
     - Dakika Dakika Dakika Dakika Dakika Dakika Dakika Dakika Dakika Dakika Dakika
     - İkincisi

6. **Frekans Frekans Frekans**: 
   - Seçilmiş komut türünin belirtilen süre aralığında kaç kez gerçekleşebileceğini tanımlayın.

7. Ayrıntıları doldurduktan sonra, tıklayın **" Kaydet"** Kuralı aktive etmek için.

---

### Örnek Use Case

Gönderilen bir ESME kullanıcısını engellemek istediğinizi varsayalım **Bind veya Enquire Link istekleri** Daha fazlası **1 dakika içinde 10 kez**. 
- Set Set Set Set <span data-ph="0"></span> 
- Set Set Set Set <span data-ph="0"></span> 
- Durum karşılanırsa, iTextPRO olacaktır:
  - **Blacklist the ESME account**
  - **Kayıtlı admin e-posta adresi için bir uyarı gönder**

Bu, müşterilere SMPP sunucusunu aşırı yüklemesini veya yanlış yapılandırmayı önler.

---

### Sonuç & Uyarılar

Kural ihlal edildiğinde:
- ESME otomatik olarak otomatik olarak **Blacklisted**.
- An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An An **e-posta uyarı** Yönetime gönderilir.

![Blacklist Result](images/blacklist3.png)

---

### Özet Özet Özet Özet

The The The The The The The The **ESME Blacklist Rule** Önemli bir özelliktir:
- anormal veya kötü niyetli müşteri davranışları.
- Altyapınızı performans bozulmasından korumak.
- Gerçek zamanlı kara listeleme için Automate mitigation by enforcing real-time blacklisting.

Bu özelliği sağlam tutmak için kullanın **SMPP server performans** Ve tüm ESME bağlantıları boyunca operasyonel hijyen uygulamak.
