---
tags:
  - Reporting
  - Business Insight
  - Gateway
  - Profit
---

# Gateway Wise Profit Report

**Navigation:** <span data-ph="0"></span> <span data-ph="1"></span> <span data-ph="2"></span>.

## Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış

The The The The The The The The **Gateway Wise Profit Report** Ağ geçidi seviyesindeki kârlılık ve SMS trafik analizlerinin ayrıntılı bir bozulması ile yöneticiler sağlar. Finansal analiz, fatura doğrulama ve ağ geçidi performans izlemesini desteklemek için tasarlanmıştır **Satın alma maliyeti**, **Satış değeri**Ve **kar marjları** SMS trafik her ağ geçidi aracılığıyla yollandı.

---

## 1. Gateway Selection

O ağ geçidinin trafiğine yönelik bir kar raporu oluşturmak için damladown'tan belirli bir ağ geçidi seçin.

![Gateway Wise Profit — Gateway dropdown selection](images/gwprofit-01-gateway-dropdown.png)

---

## 2. Country Selection

Rapor, varış ülkesi tarafından daha fazla filtrelenebilir, ülke düzeyinde kârlılık analizi sağlar.

![Gateway Wise Profit — Country filter dropdown](images/gwprofit-02-country-filter.png)

---

## 3. Tarih Aralığı Filtre

Yöneticiler bir tanımlayabilir **Özel tarih aralığı** Herhangi bir tarihsel dönem için kar raporları oluşturmak.

!!! info "Date Range Özellikler"
    - Günlük ve tarihsel trafik analizi
    - Esnek tarih tabanlı filtreleme
    - Billing period doğrulama desteği
    - Operasyonel performans incelemesi her zaman üzerinde

---

## 4. Table View Report

The The The The The The The The **Masa View** Ülkeye bağlı ağ geçidi kâr verileri aşağıdaki sütunlarla yapılandırılmış bir tabu formatta sunar:

| Köşe | Açıklama |
|--------|-------------|
| **Gateway Name Name** | Ağ geçidi trafikten geçiyor. |
| **Ülke Adı** | Trafikteki varış ülkesi. |
| **MCCMNC** | Mobile Country Code + Mobile Network Code. |
| **Network Name Network Name** | Hedef mobil ağ. |
| **Mesaj Count** | Bu dilim için toplam SMS mesajları yollandı. |
| **Satın almak Fiyat satın almak** | Routing bu dilim için maliyeti. |
| **Satış Fiyatı** | Bu dilimden kazanılan gelir. |
| **Margin (Satın - Satın Alma) %** | Kan yüzdesi hesapladı. |
| **Margin (Satın - Satın Alma) (EURO)** | EURO'da mutlak kar değeri. |

![Gateway Wise Profit — Table View](images/gwprofit-03-table-view.png)

!!! note
 <span data-ph="0"></span> Bir fiyata karşı fiyat, fiyatın düz bir fiyat olduğunu gösterir.

---

## 5. Graph View Report

The The The The The The The The **Graph View** Ağ geçidi kârlılığının görsel bir bar-kart gösterimi sağlar, yüksek performanslı ve düşük performanslı ağ geçidi veya varış ülkelerinin hızlı bir şekilde tanımlanmasına olanak sağlar.

![Gateway Wise Profit — Graph View (Margin bar chart)](images/gwprofit-04-graph-view.png)

---

## 6. Kar Hesaplama Formula

Rapor, kârlı metrikleri elde etmek için aşağıdaki standart formülleri kullanır:

```
Margin (Base Currency) =  Sales Price − Purchase Price

Margin Percentage (%)  = ((Sales Price − Purchase Price) / Purchase Price) × 100
```

---

## Gateway Wise Profit Raporu

!!! info "Bu raporu kullanmak..."
    - İzleme ağ geçidi kârlılığı gerçek zamanlı
    - Ülkeye bağlı olarak ve ağ geçidi-bilinç marjları
    - SMS trafik hacmi ve ilişkili maliyetler
    - Ağ geçidi geliri vs. satın alma maliyeti
    - Finansal raporlama ve fatura doğrulama
    - Daha iyi gelir yönetimi için optimize stratejileri
    - çevrimdışı analiz ve rekor koruma raporları
