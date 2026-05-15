---
tags:
  - Billing
  - WhatsApp
  - Rate Plan
---

# WhatsApp Rate Plan Build

**Navigation:** <span data-ph="0"></span> <span data-ph="1"></span> <span data-ph="2"></span> <span data-ph="3"></span>.

## Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış

The The The The The The The The **WhatsApp Rate Plan Build** Modül, yöneticilerin tanımlayabilmelerini sağlar **Fiyatlama şablonları** WhatsApp mesajlaşması için. Bu oran planları, mesajların PowerSMPP platformu içinde nasıl onaylandığını ve takip edildiğini ve doğru maliyet ve gelir yönetimi için kullanıcı hesaplarına tayin edilir.

---

## Yeni bir WhatsApp Rate Planı oluşturmak

Hız planı oluşturma süreci yapılandırılır **Üç adım adım**.

![Manage WA Rate Plans — List of configured plans](images/warateplan-01-list.png)

### Adım 1: Temel Detaylar

| Field | Açıklama |
|-------|-------------|
| **Rate Plan Name Name** | Plan için eşsiz, tanımlayıcı bir isim imzalayın. |
| **Aktif** | Planı yakalamak için <span data-ph="0"></span> veya <span data-ph="1"></span> Durum. |

![Add New WA Rate Plan — Step 1: Basic Details](images/warateplan-02-step1-basic.png)

### Adım 2: Fiyat Detayları (Per Country)

Her varış ülkesi için fiyat yapısını tanımlar.

![Add New WA Rate Plan — Step 2: Price Details](images/warateplan-03-step2-price.png)

| Field | Açıklama |
|-------|-------------|
| **Ülke Kodu** | Hedef ülkeyi seçin (örneğin, <span data-ph="0"></span>). Puan planı çok ülke fiyatlarını destekler. |
| **Maliyet Fiyatı** | Satın almak / seçilen ülke için WhatsApp mesajı başına ucuz maliyet. |
| **Satış Fiyatı** | Perakende fiyatı, her WhatsApp mesajı için son kullanıcıya veya müşteriye ücret verdi. |
| **Platform** | Satış fiyatının üst kısmında uygulanan ek platform ücreti (eğer uygulanabilirse). |

### Adım 3: Kullanıcılara kaydolun

Hız planı kurtarıldığında, bireysel kullanıcı hesaplarına atama için kullanılabilir. Planın imzalanması olarak, kullanıcı tarafından gönderilen tüm WhatsApp mesajlarını yapısal fiyat yapısına göre faturalandırılır.

---

## Mevcut Hız Planlarının Yönetimi

The The The The The The The The **WA Rate Planını Yönetin** Ekran tüm yapılandırılmış WhatsApp oranı planlarını aşağıdaki bilgilerle listeler:

| Köşe | Açıklama |
|--------|-------------|
| **Plan Adı** | Oran planının tanımlayıcısı. |
| **Oranlar** | Ülke bazlı giriş sayısı yapılandırıldı. |
| **Kullanıcı Assigned** | Şu anda kullanıcıların sayısı plana atanmıştır. |
| **Create Date** | Tarih planı oluşturuldu. |
| **Aktif** | Şimdiki statü (<span data-ph="0"></span> / <span data-ph="1"></span>). |
| **Tembel** | Plan sistem varsayılan olup olmadığını. |
| **Eylem** | <span data-ph="0"></span>, <span data-ph="1"></span>, <span data-ph="2"></span>Ya da <span data-ph="3"></span> Plan. |

---

## WhatsApp Rate Plan Yapılanması

!!! info "Bu modülü kullanmak..."
    - Ülkeye özgü WhatsApp mesajlaşma fiyatlarını tanımlayın.
    - Tek bir şablon içinde çoklu ülke oranı planlarını destekler.
    - Onay oranı fatura için belirli kullanıcı hesaplarını planlamaktadır.
    - WhatsApp mesajlarını takip edin ve kullanıcı başına gelir.
    - WhatsApp trafiği için en uygun finansal raporlama.
    - Platform maliyeti ve fiyatları satmanın yanı sıra suçlamaları yönetin.

!!! tip
 Cloning, mevcut bir planın bölgesel bir varyantını spin etmenin en hızlı yoludur - ebeveyni klonlayın, bir veya iki ülke fiyatlarını hazırlayın ve yeni kullanıcı grubuna atanır.
