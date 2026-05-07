
## OA/DA Normalleştirme Kuralları ITextPRO

![OA/DA Normalization](images/oada1.png)

**OA (Origin Adresi)** ve **DA (Destination Address)** iTextPRO'de normalleşme mesaj içeriğine, göndericiye (kaynak) izin verir ve alıcı adresleri **Mobile Terminated (MT)** Önceden tanımlanmış kurallara göre otomatik olarak ayarlanmış mesajlar.

Bu özellik, farklı satıcılar veya telecom ağ geçitleri ile çalışırken, farklı protokolleri veya formatlandırma gereklilikleri takip edebilir.

---

### 1. Amaç
Normalize **(OA)** ve **destinasyon (DA)** adreslere:
- Meet Meet Meet Meet **düzenleyici kurallar**
- Fulfill **Özel iş veya satıcı gereksinimleri**

---

### 2. iTextPRO OA/DA Engine
iTextPRO, yerleşik bir-in içerir **OA/DA normalizasyon motoru** Bu, routing motoru ile birlikte çalışır. 
Dinamik değişikliklerine olanak sağlar **PDU (Protocol Data Unit)** Sürekli mesaj teslimat ve uyumluluk için başlıklar.

---

### 3. Gerçek Dünya Örneği

#### Orijinal Mesaj Sent:
- **Sender ID**: <span data-ph="0"></span> 
- **Mesaj**: 
 <span data-ph="0"></span>

#### OA/DA Kuralı Uygulamalı:
- **Sender ID**: <span data-ph="0"></span> 
- **Değiştirilmiş Mesaj**: 
 <span data-ph="0"></span>

Bu dönüşüm otomatik olarak iTextPRO içinde belirlenen OA/DA normalleştirme kuralları tarafından ele alınacaktır.

---

### 4. Unicode Karakterleri Üzerine Not

- For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For **Unicode** Mesaj: Max karakter limit = **70 karakter**
- For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For For **İngilizce (GSM)** Mesaj: Max karakter limit = **160 karakter**

Bir mesaj bu sınırları aşıyorsa, sistem **Otomatik olarak kırılırlar** SMS kodlamaları içinde kalmak için ekstra karakterler.

---

### 5. Uygulama Adımları

OA/DA normalizasyonu uygulamak:

1. **Yeni OA/DA Kuralları oluşturun** yapılandırma panelinde.
2. Dönüşüm mantığını tanımlar:
   - Modify Sender ID
   - Rewrite message content
   - Uyumlu hedef numarası formatı
3. Kuralları ilgili ağ geçidi veya trafik kaynaklarına imzalayın.

---

### 6. Anahtar Faydaları

- Katı satıcı içilebilirlik
- tele Telcom veya düzenleyici standartlar ile uygunluk
- Otomatik içerik sanitizasyon veya yeniden yazma
- Gönderer ID'nin Özelleştirilmesi ve içerik mesajlaşma

---

**OA/DA Normalizasyon** iTextPRO, mesaj formatı ve uyum için güçlü bir mekanizma sunuyor, bu mesajın hem teknik olarak sağlam hem de yönetmelik dostu olmasına izin veriyor.
