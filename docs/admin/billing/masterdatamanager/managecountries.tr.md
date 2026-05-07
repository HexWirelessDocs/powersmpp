---
tags:
  - Billing
  - Rate Plan
  - Pricing
---

# Billing

## ITextPRO ile Basitleştirilmiş Billing Yönetimi

SMS endüstrisindeki aggregatörler genellikle yönetmekte zorlukla karşı karşıya **Birden fazla ağ geçidi**, **Çeşitli fiyatlandırma yapıları**Ve **Uluslararası işlemler**. 
The The The The The The The The **iTextPRO Billing Modül** Bu sorunları, kolaylaştırılan, doğru ve kârlı operasyonları sağlayan gelişmiş özelliklerle ele alır.

---

## 1. Base Para Para birimi

- **Önemlilik**: Finansal işlemlerde tutarlılık ve doğruluk sağlayın.
- **Öneri Öneri Önerisi**Euro (EUR) küresel SMS aggregasyon endüstrisinde yaygın olarak kullanılır.
- **Düşünmek**: Temel para birimi ayarlandığında, onu değiştirmek karmaşık olabilir. İş yolculuğunda erken karar verin.

---

## 2. MCC ve MNC Kodlarını Anlamak

- **MCC (Mobile Country Code)** ve **MNC (Mobile Network Code)** Bir ülke içinde mobil ağlara dayanan fiyatlama için çok önemlidir.
- **Operatör Fiyatlandırma**Birçok telecom operatörleri, MCC + MNC kombinasyonlarında fiyatlarını temel almaktadır.
- **Flexability**: iTextPRO etkinleştirir **Ağa özgü fiyatlandırma** Daha büyük gelir optimizasyonu için.

---

## 3. Ters Mühendislik Mobile Numbers için Prefix'i anlamak

- **Amaç**: Bir mobil sayının kökenini ve ağını belirtir.
- **Prefix**: İlk 3-4 rakam algılamaya yardımcı olur **Ülke Kodu** ve **Mobile Network**.
- **Örnek Örnek Örnek Örnek Örnek Örnek Örnek**: 
  - Sayı: Sayı: <span data-ph="0"></span> 
  - Ülke Kodu: <span data-ph="0"></span> (UAE) 
  - Düz fiyatlandırma ile: Maliyet hesaplaması basit. 
  - MCC/MNC fiyatlandırması ile: Ek arama gereklidir (Mevcut araç doğrudan bu sayıdan MCC/MNC sağlar).

![Manage Countries](images/managecountries1.png)

---

## 4. Para Dönüşümü

- **Base Para**: İç işlemler için kullanılır.
- **Ekran Paraları**Kullanıcılar, tercih ettikleri para biriminde işlemleri görebilirler.
- **Faydalar**: Muhasebe doğruluğunu sürdürürken uluslararası işlemleri basitleştirir.

---

## 5. Kayıp Koruma Politikası

- **Gelir Leakage Tool**: Gerçek zamanlı olarak potansiyel gelir kayıpları haklı çıkarır.
- **Önlemler**: Tipos, numara manipülasyonu veya yönetici hataları nedeniyle kaynaklanan işlemleri durdurun.
- **Financial Safeguard**: Gelir kaybına karşı korur ve fatura doğruluk sağlar.

---

## Anahtar Faydaları

- **Operasyonel Simplification** – Akışkan global SMS faturası. 
- **Precise Fiyat** - Rekabetçi fiyat için ağ düzeyinde kontrol. 
- **Clear Döviz İşleme** – Katı ve para yönetimi gösterir. 
- **Finansal Güvenlik** - Otomatik kayıp önleme politikaları. 

---

# Master Data Manager

The The The The The The The The **Master Data Manager** bölüm dört anahtar konfigürasyon seçeneği içeriyor:

1. **Ülkeleri Yönetmek** 
2. **MCC/MNC** 
3. **Yönetin Prefix** 
4. **Gateway Price**

---

## 1. Ülkeleri Yönetmek

The The The The The The The The **Ülkeleri Yönetmek** özellik, birden çok ülkede SMS trafik sonlandırmasının konfigürasyonunu ve yönetimini sağlar.

![Manage Countries](images/managecountries2.png)

### Tek Bir Ülke Ekle

- **Ülke Adı** - Açık kimlik için tam ülke adı. 
- **Ülke Kodu** - routing için eşsiz tanımlayıcı. 
- **Ülke ISO Kodu** - Küresel uyumluluk için standartlaştırılmış kod. 
- **Add Process** - Click - Click **Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add** Ülkeyi master listesinde dahil etmek.

![Single Country Add](images/managecountries3.png)

---

### Bulkload Fonksiyonelity

![Bulk Upload](images/managecountries4.png)

- **Örnek Excel** - Kolay düzenleme için tüm ülkelerle önceden programlanmıştır. 
- **File & Upload** – Birden çok girişi bir kez destekler. 
- **Köşe** - Map Excel alanları için **Ülke Adı**, **ISO ISO ISO ISO**Ve **Kod Kodu**. 
- **Gönder & Ekran** – Bulk add countries and customize record display.

![Bulk Upload Results](images/managecountries5.png)

---

### Action Feature

![Action Options](images/managecountries6.png)

- **Edit** - Mevcut ayrıntıları Güncelleme. 
- **Update Update Update Update Update Update Update** – Yeni ülke verileri. 
- **Delete** - Kullanılmamış girişleri çıkarın. 

---

**En İyi Uygulama:** 
Düzenli olarak inceleme ve güncelleme **Master Data Manager** Ülke ve ağ yapılandırmalarının fiyat ve routing için doğru kalmasını sağlamak.
