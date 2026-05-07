
# Mesaj Body Normalizasyon

The The The The The The The The **Mesaj Body Normalizasyon** Kural, içinde yerleşik bir özelliktir **Power SMPP**Ağ geçidine teslim etmeden önce yöneticilere esneklik vermek ve mesaj içeriğini düzeltmek için tasarlanmıştır. 
Bu, tüm giden mesajların doğru şekilde biçimlendirilmesini sağlar, hem de okunabilirliği ve etkinliğini arttırır.

Bu belge nasıl açıklıyor **Mesaj Body Normalizasyon** İşler ve yöneticiler, önceden tanımlanmış kurallara dayanan mesaj içeriğini otomatik olarak ayarlamayı nasıl yapılandırabilirler - ağ geçidi gereksinimlerine tutarlılık ve uyum sağlamak.

---

## Anahtar Özellikler

Mesaj Vücut Normalleştirme Kuralı mevcut olan süreyi genişletiyor **OA/DA Normalleştirme Kuralı**Ayrıca mesaj içeriğini manipüle etmek için birçok yol sunar:

- **Kodların/OTP'lerin Çıkarılması:** Otomatik olarak mesaj metninden OTPs veya belirli kodları öğrenin. 
- **Prefixes veya Suf ekleri ekleyin:** Standart bir format korumak için mesajdan önce veya sonra belirli metin girin. 
- **Textchange:** Daha iyi tutarlılık için önceden tanımlanmış kurallara göre belirli kelimeler veya cümleleri değiştirin.

Bu seçenekler yöneticilere tüm mesajların ağ geçidi standartlarına uygun olmasını sağlar, genel mesajlaşma deneyimini geliştirir.

---

## Mesaj Vücut Normalizasyona Erişim

Mesaj Body Normalizasyonunu yapılandırmak için:

1. Navigate to the **Kurulum Modülleri**. 
2. Select Select Select Select **Gateway Build**. 
3. seçin **Mesaj Body Normalizasyon**. 
4. Click Click Click Click Click **Yeni Ekle Yeni Ekle Yeni Ekle Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Add Add Yeni Add Add Yeni Add Add Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Yeni Add Yeni Add Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Add Add Yeni Add Yeni Add Add Add Add Yeni Add Yeni Add Add Add Add Yeni Add Add Yeni Add Add Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Add** Yeni bir normalleştirme kuralı oluşturmak.

![Message Body Normalization UI](images/mbn1.png)

---

## Revizyon

Bir kez tıkladığınızda **Yeni Ekle Yeni Ekle Yeni Ekle Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Add Add Yeni Add Add Yeni Add Add Add Yeni Add Add Yeni Add Add Yeni Add Add Yeni Add Yeni Add Yeni Add Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Yeni Add Add Yeni Add Add Add Yeni Add Yeni Add Add Add Add Yeni Add Yeni Add Add Add Add Yeni Add Add Yeni Add Add Add Yeni Add Yeni Add Yeni Add Yeni Add Yeni Add Add Add**Ancak bir yapılandırma sayfası birden çok alanda görünür.

### **Kural Adı**
Kural için tanımlayıcı ve anlamlı bir isim tanımlayın.

---

### **Durum Ayarları**

#### 1. Interface Interface
Kuralın nerede uygulandığı arayüze bakın. Aşağıdakilerden birini veya daha fazlasını seçebilirsiniz:

- WEB WEB 
- API API API API 
- SMPP 
- Tüm Interfaces 

![Interface Selection](images/mbn3.png)

Bu, operasyonel arayüze bağlı olarak hedefli kural uygulaması sağlar.

---

#### 2. Kullanıcı
Kuralın geçerli olup olmadığını seçin:
- Belirli bir **Kullanıcı**Ya da 
- **ANYA** (Tüm kullanıcılara uygulanır).

---

#### 3. Gönderer ID
Configure Sender ID koşulları belirli eşleştirme kalıplarına dayanan:

- **eşit eşit eşit eşit eşit** – Tam olarak belirtilen Sender ID'yi eşleştirin 
- **Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start** – Sender ID'si belirli bir anahtar kelime ile başlarsa 
- **End With End With End** – Sender ID belirli bir anahtar kelime ile biterse 
- **Contains** - Anahtar kelimeler Sender ID'de herhangi bir yerde bulunursa 

![Sender ID Condition](images/mbn4.png)

---

#### 4. Hedef Adres
Fonksiyonlar aynı şekilde **Sender ID**Ancak aynı koşullara izin verin - *eşit eşit eşit eşit eşit*, *Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start with Start*, *End With End With End*, *Contains* - destinasyon adresi formatına dayanan kuralları uygulamak.

---

#### 5. Mesaj
Yukarıdaki olarak aynı koşullu seçenekler mesaj içeriğine uygulanabilir, kesin formatlama kontrolü sağlar.

---

## Eylemler: Detaylı Açıklama

In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In **Power SMPP**, **Eylem** Bölüm, ağ geçidine teslim etmeden önce mesaj içeriğini manipüle etmek için üç yapılandırılabilir yöntem sunar:

1. **Kod** 
2. **Bul ve Değiştirin** 
3. **Append ve Prepend**

Her biri belirli bir kullanım durumuna hizmet eder. Her şeyi ayrıntılı olarak inceleyelim.

---

### 1️⃣ Extract Code

The The The The The The The The **Kod** Eylem, yöneticilerin OTP'leri veya kodları mesajlardan çekmelerini sağlar.

#### A) From Down Şablon
Eğer mesaj sabit bir model varsa, kullanabilirsiniz <span data-ph="0"></span> Ekstraksiyon için karakter sayısını tanımlamak.

**Örnek: Örnek:**

- Mesaj: <span data-ph="0"></span> 
- Kurulum: <span data-ph="0"></span> 
- Çıktı: <span data-ph="0"></span> 

![Extract Code - Fixed Template](images/mbn6.png)

---

#### b) Occurrence Index
mesajların birden fazla kod içerdiğinde bunu kullanın ve indeksi tarafından birini çıkarmak istersiniz.

**Örnek: Örnek:**
- Mesaj: <span data-ph="0"></span> 
- Kurulum: 
  - Uzunluk: <span data-ph="0"></span> 
  - Index: Index: Index: <span data-ph="0"></span> 
- Çıktı: <span data-ph="0"></span>

![Extract Code - Occurrence Index](images/mbn7.png)

---

### 2️⃣ Bul ve Değiştir

Mesajdaki belirli kelimeleri veya cümleleri değiştirmek için bunu kullanın.

**Örnek: Örnek:**
- Mesaj: <span data-ph="0"></span> 
- Kurulum: 
  - Bul: <span data-ph="0"></span> 
  - Değişim: <span data-ph="0"></span> 
- Çıktı: <span data-ph="0"></span>

![Find and Replace](images/mbn8.png)

---

### 3️⃣ Append ve Prepend

Bu, daha önce (prepend) veya sonra (append) mesajı veya her ikisini de eklemeye olanak sağlar.

#### a) Append  
Metinleri ekleyin **end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end end** Mesajın. 
**Örnek: Örnek:** 
- Mesaj: <span data-ph="0"></span> 
- Append: <span data-ph="0"></span> 
- Çıktı: <span data-ph="0"></span> 

![Append Example](images/mbn10.png)

---

#### b)  
Metinleri ekleyin **başlangıç başlangıç başlangıç başlangıcı** Mesajın. 
**Örnek: Örnek:** 
- Mesaj: <span data-ph="0"></span> 
- Prepend: <span data-ph="0"></span> 
- Çıktı: <span data-ph="0"></span> 

![Prepend Example](images/mbn11.png)

---

#### c) İkisi de  
Hem bir ek hem de ek ekleyin. 
**Örnek: Örnek:** 
- Mesaj: <span data-ph="0"></span> 
- Prepend: <span data-ph="0"></span> 
- Append: <span data-ph="0"></span> 
- Çıktı: <span data-ph="0"></span> 

![Append and Prepend Both](images/mbn12.png)

---

## Multi Actions Combining multiple Actions

Adminler tek bir kural içinde birden fazla eylem uygulayabilir.

**Örnek: Örnek:**
- Mesaj: <span data-ph="0"></span> 
- Eylemler: 
  - Türleme Kodu (Kayıt Şablonundan) 
  - Append ve Prepend (Both) 

Bu OTP'yi çıkarır ve yapılandırılmış olarak ek metin formatı uygular.

![Combined Actions](images/mbn13.png)

---

## Öncekilik ve Uyumluluk

- **Mesaj Body Normalizasyon** Gerçekler **Daha önce daha önce** The the the the the **OA/DA Normalizasyon**. 
- Bu, mesaj içeriği optimize edilmiş ve ilk önce biçimlendirilmiş, kural çatışmalarını önlemek. 
- Her iki normalleştirme kuralları doğru ağ geçidi teslimi için katmanlarda çalışır.

---

## Özet Özet Özet Özet

**Mesaj Body Normalizasyon** Power SMPP yöneticilerini güçlendiriyor:
- OTPs veya kodları, 
- Add prefixes/suffixes, 
- Kelimeleri veya cümleleri değiştirin, 
- Birden fazla kuralı birleştirin ve 
- Kullanıcı başına kurallar uygulayın, gönderici veya arayüz. 

Bu özellik, tüm mesajların tutarlı bir formatta tutulmasını ve ağ geçidi gereksinimlerine uymasını sağlar - mesaj tesliminde güvenilirlik ve profesyonelliği artırmak.
