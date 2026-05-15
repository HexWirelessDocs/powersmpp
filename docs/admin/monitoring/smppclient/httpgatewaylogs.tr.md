---
tags:
  - Monitoring
  - HTTP
  - Gateway
  - Logs
---

# HTTP Gateway Logs

**Navigation:** <span data-ph="0"></span> <span data-ph="1"></span> <span data-ph="2"></span>.

## Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış

The The The The The The The The **HTTP Gateway Logs** Bölüm, yöneticilerin tam HTTP'yi görmelerine izin verir **İstek isteği** ve **yanıt yanıt yanıt** PowerSMPP uygulaması ve yapılandırılmış ağ geçidi satıcılar arasında iletişim kurulur. Bu loglar teslimat başarısızlıklarını teşhis etmek, API ödeme yüklerini doğrulamak ve ağ geçidi etkileşimleri denetlemek için önemlidir.

---

## Logs'i Görme Adımları

1. Seç **HTTP Gateway** Bundan sonra **Gateway Name Name** düşüş.
2. Gerekli olanı seçin **Date Range** Tarih seçici kullanarak.
3. seçin the Select the **Log Type** (<span data-ph="0"></span> / <span data-ph="1"></span> / <span data-ph="2"></span>Gerekli olduğu gibi.
4. Seç **Verbosity** granular filtreleme gerekiyorsa seviye.
5. Click Click Click Click Click **Gönder** eşleştirme loglarını getirmek ve görüntülemek.

![HTTP Gateway Logs — Log list view](images/httplogs-01-list.png)

---

## Mevcut Log Bölümleri

### Vücut İste

The The The The The The The The **Vücut İste** PowerSMPP uygulamasından ağ geçidi satıcısına aktarılan tam ücret yükü içerir.

![HTTP Gateway Logs — Request Body expanded](images/httplogs-02-request-body.png)

!!! info "İste Vücut - Veri Dahil"
    - **Mobile Number** - SMS'in hedef numarası
    - **Sender ID** - Başlangıç adresi / Sender ID kullanılmış
    - **Parametreleri İste** – ağ geçidine gönderilen tam API parametreleri
    - **Host / IP Detayları** – IP adresi ve ağ geçidi uç noktası
    - **Submission Time** - Talebin gönderildiği zaman damgalanması

### Response Body

The The The The The The The The **Response Body** Ağ geçidi satıcısından alınan kabul ve durum verileri içerir.

![HTTP Gateway Logs — Response Body expanded](images/httplogs-03-response-body.png)

!!! info "Yanıt Vücut – Data"
    - **Gateway Response** - ağ geçidi tarafından iade edilen ham yanıt
    - **Durum Bilgileri** - teslimat veya kabul durumu kodları
    - **Hata Detayları** - Başarısız teslimler için hata kodları ve açıklamalar
    - **Cevap** - Ağ geçidin talebini işlediğini onaylayın

---

## Filtre Seçenekleri

Yöneticiler aşağıdaki ek filtreleri kullanarak log görünümünü geliştirebilirler:

| Filtre | Use Use Use Use Use Use |
|--------|-----|
| **IP Adresi** | Gateway sunucusu IP tarafından filtre girişleri. |
| **Sender ID** | Gönderer ID'den gelen filtre logları. |
| **Mobile Number** | Filtre girişleri hedef mobil numara tarafından. |

---

## Tipik Uyarı

1. Bir kampanya beklenmedik başarısızlıklar veya hayatta olmayan mesajlar rapor eder.
2. Open Open Open Open **HTTP Gateway Logs**Ancak etkilenen ağ geçidi ve konuyu kapsayan bir tarih aralığı seçin.
3. Set Set Set Set **Log Type** toklanmak için <span data-ph="0"></span> Yüzeye sadece başarısız borsalar.
4. genişletin **Vücut İste** Yukarıda belirtilen ücret yükünü doğrulamak doğruydu.
5. genişletin **Response Body** Gerçek hata kodunu / yazısını satıcı tarafından geri almak için.
6. Use Use Use Use Use Use **IP Adresi**, **Sender ID**Ya da **Mobile Number** Satıcının destek ekibi için belirli bir test örneği ayırmak için filtreler.
