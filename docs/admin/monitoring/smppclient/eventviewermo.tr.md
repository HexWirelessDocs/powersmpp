---
tags:
  - Monitoring
  - MO
  - Event Viewer
---

# Event Viewer (MO) – Mobile Originated

**Navigation:** <span data-ph="0"></span> <span data-ph="1"></span> <span data-ph="2"></span>.

## Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış Genel Bakış

The The The The The The The The **Event Viewer (MO)** Bölüm izlemek için kullanılır **Mobile Originated (MO)** PowerSMPP içindeki mesajlar ve ilgili sistem olayları. MO mesajları bir ağ geçidi satıcısından alınan veya uygulamaya yönlendirilen son kullanıcıdan alınan mesajlardır.

---

## Amaç

Event Viewer (MO) yöneticilerin izlenmesine yardımcı olur, denetim ve sistemdeki tüm gelen MO ile ilgili aktiviteyi sorun.

!!! info "Birincil Kullanım Vakaları"
    - Gerçek zamanlı olarak MO mesaj aktivitesini izleyin
    - Gelen kullanıcı veya satıcı iletişim loglarını kontrol edin
    - MO ile ilgili teslimat veya yönlendirme sorunları
    - Sistem tarafından üretilen MO olayları
    - Bağlantılı trafik için ağ geçidi iletişim loglarını onaylayın

---

## Mevcut Bilgiler

Modül her giriş girişi için aşağıdaki alanları gösterir:

| Field | Açıklama |
|-------|-------------|
| **Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman Zaman** | MO Etkinliğinin zaman çizelgesi. |
| **Log Type** | Etkinliğin sınıflandırılması - <span data-ph="0"></span> veya <span data-ph="1"></span>. |
| **Mesaj** | MO olayın veya aktivitenin tanımı. |

![Event Viewer (MO) — Info log entries](images/eventmo-01-info.png)

![Event Viewer (MO) — Error log type (no entries shown)](images/eventmo-02-error.png)

---

## Log types

| Log Type | Açıklama |
|----------|-------------|
| **Info Info** | Bilgi sistemi olayları, başarılı ağ geçidi değişiklikleri, kullanıcı listesi güncellemeleri. |
| **Hata hatası** | Hata seviyesi olayları, MO mesajlarını veya sistem istisnalarını reddetti. |

---

## Özellikler Özellikler Özellikler Özellikler

!!! info "Event Viewer (MO) Yetenekleri"
    - MO event loglarını gerçek zamanlı olarak görüntüle.
    - Ağ geçidi ve kullanıcı erişimli aktiviteler.
    - Gelen MO mesaj isteklerini takip edin.
    - Sorun Gider ve MO ile ilgili sorunları çöz.
    - Talep üzerine yeni girişler **Yenileme** düğme.
    - Filtre girişleri **log tipi** (Info / Hata).
    - Filtre girişleri **tarih aralığı** Tarihi inceleme için.

---

## Date Range Filter

Yöneticiler, almak için belirli bir tarih aralığı seçebilir **Tarihi MO olayı girişleri**Bu, retrospektif sorun giderme, uyumluluk denetimi ve operasyonel incelemeyi destekler.

!!! tip
 Intermittent sorununu kovalarken, set **Log Type = Hata** İlk önce başarısızlıklara odaklanmak sadece, sonra geniş ton **Bütün Bütün Hepsi** Pencere sırasında hata olayları görünmezse.
