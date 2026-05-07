
# Invoicing

Invoicing modülü, Yöneticilerin doğrudan kullanıcıları için faturalandırmasını sağlar (Account type: **Kullanıcı**Faturalar oluşturmak için bir eklenti sağlayarak, onları indirin veya e-posta yoluyla gönderin. Fatura nesli akışı, Admin tarafından yapılandırılan belirli aralıklarla otomatik ve tetiklenir.

Bu modül, Admins'in çocuklarının kullanıcılarını etkin bir şekilde yönetmesine yardımcı olur.

---

## Fatura [Preted / Post ücretli] olarak Plugin

Yöneticiyi tercih etmeli **Invoicing Lisans** ayrı ayrı. etkinleştirdikten sonra, invoicing modülü, seçilen fatura modu ile başvuruda erişilebilir hale gelir -**Pre ücretli** veya **Posta ücretsiz**.

- The The The The The The The The **Billing Method** (Pre ücretli / ücretsiz) her kullanıcı için kullanıcı oluşturma sırasında tanımlanır.
- Admin her kullanıcı için invoicing yöntemi yapılandırabilir.
- Kendi başlarına kaydolan kullanıcılar sahip olacak **Pre ücretli** Varsayılan olarak fatura.

---

## Invoicing Dashboard

Admin invoicing modülüne eriştiğinde, sunulan ilk görüş **Invoicing Dashboard**Panel anahtar faturalama anlayışları sağlar:

### 1. Toplam Fatura
Gösterileri göster **toplam fatura sayısı**Ayrıca:
- Onaylanmış faturalar 
- Onaylanmamış faturalar 

### 2. Ücretli Faturalar
Ekranlar The count of the count of **Tamamen ücretli faturalar**.

### 3. Faturalar Unsettled In bills
Hala bekleyen faturaların sayısını gösterir:
- ödenmemiş faturalar 
- Kısmen ücretli faturalar 

### 4. Faturayı Yönetin
Kısa bir özeti *Faturayı Yönetin* Bölüm. 
Adminler tıkılabilir **Go to Page** ayrıntılı fatura yönetimine gitmek.

### 5. Faturaları Yeniden Değerlendirmeyi Yönetin
Geçerli uygulanabilir **Sadece Post ücretli kullanıcılar için**. 
Buradan itibaren, Adminler şunlar olabilir:
- Tekrarlanan faturaları oluşturun 
- Başlayın veya fatura döngüsünü durdurun 
- Fatura döngüsü ayarlarını Değiştirin 

### 6. Ödeme Kabul Edildi
Kısa bir özeti *Ödeme Kabul Edildi* Bölüm. 
Yöneticiler ayrıntılı sayfaya yönlendirilebilir **Go to Page** düğme.

---

## Faturaları Yönetin

The The The The The The The The **Faturaları Yönetin** Sayfa tüm faturaları gösterir (önemli faturalar dahil) ödeme durumu ile birlikte. Yöneticiler faturaları iddia edebilir, onları indirin ve ödeme hatırlatma e-postalarını gönderebilirler.

![Manage Invoices](images/manage1.png)

### Anahtar Özellikler:

#### **Download In bill Report**
Adminlerin fatura raporunu bir Excel sayfası olarak ihraç etmelerine ve indirmelerine izin verin.

#### **Gönder**
Faturaları olan kullanıcılara ödeme hatırlatıcıları gönderilebilir **ücretsiz** veya **Kısmen Ücretli**.

#### **Taslaklar**
Posta ücretli kullanıcılar için üretilen faturaları geri almak, olarak depolanır **draftlar**. 
Adminler, taslakları Action menüsünden manuel olarak incelemeli ve onaylamalıdır.

#### **Gelişmiş Arama**
Gelişmiş arama seçeneği, faturaların filtrelenmesine izin verir:
- Kullanıcı 
- Fatura ID 
- Çünkü durum 
- Ödeme durumu 

Bu, Adminlerin belirli gereksinimlere göre hızlı bir şekilde bulmalarına yardımcı olur.

---

## Create In bill

Bu bölüm, Adminlerin kullanıcılar için faturalar oluşturmak için izin verir.

---

### **Pre ücretli Kullanıcılar için:**

1. Kullanıcı tipini seçin: **Pre ücretli**
2. Kullanıcıyı seçin.
3. girin **Fatura Tarihi** ve **Çünkü Tarih**.
4. girin **Recharge $** (Kaçlardan önce).
5. Bir sağlayın **Açıklama** Fatura için.
6. Modifyify **Şartlar ve Koşullar** veya **Müşteri Notları** Gerekirse (veya varsayılan yapılandırılmış değerleri kullanır).
7. Bir tanesini seçin:
   - **Create In bill** (Eğer ödeme henüz alınmazsa)
   - **Create & Request In bill** (Eğer ödeme zaten alındıysa - sistem ödeme ayrıntılarına girmek için hızlı olacaktır)

---

### **Post ücretli Kullanıcılar için:**

Posta ödenmiş faturalar genellikle otomatik olarak belirlenen fatura döngüsü sonunda yapılır. **Faturaları geri almak**. 
Ancak, bir döngü atılır veya manuel müdahaleye ihtiyaç duyarsa, Adminler faturayı manuel olarak yaratabilir:

1. Kullanıcı tipini seçin: **Posta ücretsiz**
2. Kullanıcıyı seçin.
3. Seç **tarih aralığı** Faturanın oluşturulması ve kayıtları getirebilmesi için.
4. Sistem seçilen süre için mesajlaşma kayıtlarını gösterecektir.
5. doğrulamadan sonra, seçin:
   - **Create In bill**
   - **Oluşturun ve Fatura Teklifi**

