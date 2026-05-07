---
tags:
  - SMPP
  - ESME
  - HTTP API
  - Configuration
---

## Yönetişim Interface

The The The The The The The The **Yönetişim Interface** iTextPRO'deki bölüm, yöneticilerin ortak bağlantılarını yapılandırmasını ve yönetmelerini sağlar **SMPPups (ESME Hesapları)** ve **HTTPups**Bu konektörler, dış sistemlerle sorunsuz entegrasyon sağlayarak iletişim yeteneklerini geliştirir.

---

### 1. SMPPws (ESME Hesabı)

![SMPP Connector](images/manage1.png)

The The The The The The The The **SMPPws**Ayrıca bir an olarak da adlandırılır **ESME (Son Kısa Messaging Entity) Hesabı**, partner bağlantılarını şirkete kolaylaştır **SMPP Server** iTextPRO içinde.

#### Yeni bir SMPP Tools'u nasıl ekleyebilirsiniz:
1. Belirli kullanıcı hesabı için arayın.
2. Click Click Click Click Click **"Add New"** yapılandırmayı başlatmak için.
3. Gerekli ayrıntılarda doldurun:

**ESME Hesap Ayarları Alanlar:**

| Field | Açıklama |
|-------|-------------|
| **Sistem ID** | Kullanıcı adı ESME hesabına bağlanmak için kullanılır |
| **Şifre Şifre** | ESME hesabı için kimlik doğrulama şifresi |
| **Beyaz Liste IP** | Bu IP'den sadece bağlantılar izin verilir |
| **Tx Count** | Sayı (Tx) seansları |
| **Rx Count** | Alıcı Sayısı (Rx) seansları |
| **TRx Count** | Transceiver (TRx) seans sayısı |

#### Gelişmiş Ayarlar:
- **Geçerli IP**: Kaynak IP adreslerinin geçerliliği. Sadece beyaz listelenmiş IP'ler bağlanabilir.
- **Hesap Active**etkinleştirildiği zaman, ESME kullanıcısı SMPP sunucusuna bağlanabilir.
- **Blacklisted**: Bu otomatik olarak ESME kullanıcısının ihlal ettiği takdirde etkinleştirilir **ESME Blacklist Rule**.

---

### 2. HTTP Tools

![HTTP Connector Setup](images/manage2.png)

The The The The The The The The **HTTP Links** partnerlerin iTextPRO ile entegre etmesini sağlar **HTTP tabanlı APIs**.

#### Enable HTTP API Access için adımlar:
1. Activate **API durumu** İstenen kullanıcı hesabında.
2. Bir kez aktive edildiğinde, **Geliştirici API API** bölüm kullanıcı arayüzünde görünür hale gelir.
3. Oradan, kullanıcılar olabilir:
   - View View View View **API Credentials**
   - **Download API belgeleri** (PDF format)
   - HTTP API uç noktalarını mesaj göndermeler, raporlar ve daha fazlası için kullanmaya başlayın.

![HTTP API Dashboard](images/manage3.png)

---

### Özet Özet Özet Özet

The The The The The The The The **Yönetişim Interface** iTextPRO her ikisi için de birleşik ve sezgisel bir kurulum sunuyor **SMPP ve HTTPches**, etkinleştirin:
- Ortaklar ve satıcılar için güvenli ve kontrollü erişim.
- Kolay entegrasyon için API belgeleri ve araçları.
- Oturum seviyesi kontrol ve IP tabanlı erişim yönetimi.

Bu konektörleri kullanarak, iTextPRO kullanıcıları, sıkı kontrolü ve esnekliği korumak için mesajlaşmalarını genişletebilir.
