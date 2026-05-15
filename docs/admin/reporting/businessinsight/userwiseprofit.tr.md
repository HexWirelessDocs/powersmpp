---
tags:
  - Reporting
  - Business Insight
  - User
  - Profit
---

# Kullanıcı bilge Kar Raporu

**Navigation:** <span data-ph="0"></span> <span data-ph="1"></span> <span data-ph="2"></span>.

## Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış

The The The The The The The The **Kullanıcı bilge Kar Raporu** Yöneticilerin herhangi bir seçilmiş tarih aralığı için kullanıcı düzeyinde SMS trafiği ve kârlılığı analiz etmesini sağlar. Rapor dayanmaktadır **Uygulama aracılığıyla kullanıcılar tarafından gönderilen mesajlar tamamen** Ve müşteri hesabı için ayrıntılı gelir, maliyet ve marj verileri sağlar.

---

## 1. User Selection

Bu müşteri için hedeflenen bir kar raporu oluşturmak için düşüş listesinden belirli bir kullanıcı hesabı seçin.

## 2. Country Selection

Hedef ülke tarafından filtre trafiği verileri bölge başına kullanıcı kârlılığı analizi elde etmek için.

## 3. Tarih Aralığı Filtre

Herhangi bir fatura veya operasyonel süre için kullanıcı kar raporları oluşturmak için özel bir tarih aralığı tanımlayın.

---

## 4. Table View Report

The The The The The The The The **Masa View** Tellar formatında ayrıntılı kullanıcı-bilinç bilgilerini gösterir.

![User Wise Profit — Table View (all users)](images/userprofit-01-table-all.png)

![User Wise Profit — Table View (highlighted)](images/userprofit-02-table-highlighted.png)

### Metin çevirisi

| Köşe | Açıklama |
|--------|-------------|
| **Kullanıcı Adı** | Kullanıcı hesabının adı / tanımlayıcısı. |
| **Ülke Adı** | Kullanıcının SMS trafiğinin hedef ülkesi. |
| **MCCMNC** | Mobile Country Code + Mobile Network Code. |
| **Network Name Network Name** | Hedef mobil ağ adı. |
| **Mesaj Count** | Kullanıcı tarafından sunulan toplam SMS mesajları. |
| **Satın almak Fiyat satın almak** | Kullanıcının trafiğini işlemek için yapılan gerçek routing maliyeti. |
| **Satış Fiyatı** | Kullanıcıya ödenen toplam satış miktarı. |
| **Margin% (Satış - Satın Alma)** | Kullanıcının trafiği için kâr yüzdesi hesaplandı. |
| **Margin (Satış - Satın Alma)** | USD'de kullanıcı trafiğinden elde edilen toplam kazanç. |

---

## 5. Graph View Report

The The The The The The The The **Graph View** Kullanıcı-bilinçlerinin bir bar grafiği oluşturur, müşteriler arasında hızlı karşılaştırma sağlar.

![User Wise Profit — Graph View (Margin by user)](images/userprofit-03-graph-view.png)

---

## 6. Mesaj Submission Analysis

Kullanıcı Bilge Kar Raporundaki tüm hesaplar yönlendiriliyor **Sadece sadece sadece sadece sadece sadece sadece sadece sadece sadece sadece** Uygulama yoluyla kullanıcı tarafında gönderilen mesajlar tarafından. Uygulama kullanıcı gönderme yolunu atlayan trafik bu rapora dahil değildir.

---

## 7. Kar Hesaplama Formülü

```
Margin (USD)          =  Sales Price − Purchase Price

Margin Percentage (%) = ((Sales Price − Purchase Price) / Purchase Price) × 100
```

!!! tip
 Bu raporu bu raporu bir araya getirin **Gateway Wise Profit** İki tamamlayıcı açıdan kârlılığı görmek - müşteri (revenue side) ve satıcı (cost side).
