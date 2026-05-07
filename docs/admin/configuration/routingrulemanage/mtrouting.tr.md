---
tags:
  - Routing
  - Configuration
  - MT
---

## Routing Rule Manager Manager

Routing rekabetçi bir kenar ve maksimum gelir sağlamak için önemli bir rol oynar. The The The The The The The The **Routing Rule Manager Manager** iTextPRO, kullanıcı SMS trafiğinin dinamik ve akıllı routing mantığı aracılığıyla nihai hedefine verimli bir şekilde ilerlemesine olanak sağlar.

SMPP uygulamaları birden fazla yönlendirme yolu destekler. iTextPRO, teslimat performansını artırmak, maliyetleri azaltmak ve trafik akıllı dağıtmanızı sağlayan dinamik MT (Mobile Terminated) routing kuralları oluşturmanıza izin vererek bu karmaşıklığı basitleştirir.

Anahtar faydaları şunlardır:
- teslimat zamanından itibaren Gateway seçimi
- Maliyet optimizasyonu en az maliyetli routing
- HTTP ve SMPP protokolleri arasındaki dinamik toggling
- Gerçek zamanlı trafik dağılımı ve dengelemek

Bir kez içeride **MT Routing Rule** Bölüm, zaten yapılandırılmış routing kurallarının bir listesi gösterilecektir. Yapabilirsiniz **Düzenleme** Düzenleme ikonuna tıklayarak herhangi bir kural.

!!! tip
 Hiçbir manuel yeniden başlatma veya yeniden yükleme gerekli değildir. Tüm routing kuralı güncelleştirmeleri-the-fly üzerinde uygulanır.

---

### MT Routing Rule

![Manage Routing Rule](images/routingrule1.png)

Yeni bir kural oluşturmak için, tıklayın **"Add New MT Rule"** düğme. Aşağıdakileri yapılandırmanız istenecektir:

#### 1. **Kural Adı**
- Kolay kimlik için samimi, tanımlayıcı bir isim girin.

#### 2. **Filtre Tipi**
- İki filtre türü mevcuttur:

##### **Filtre Yoluyla Geçin**
- Küresel routing politikaları için tasarlanmıştır.
- Bir geri dönüş rotası olarak hizmet etmek için yüksek öncelikli bir geçiş kuralı oluşturmak için önerilir.

![Pass Through Filter](images/routingrule2.png)

##### **Özel Filtre**
- Daha spesifik parametrelere dayanan rota mesajları:

![Custom Filter](images/routingrule3.png)

- **Ülke Kodu**: SMS trafiğini yok etmek için ülkeyi seçin.
- **MCC/MNC**: Seçilmiş ülkenin belirli bir mobil ağı seçin.
- **Kullanıcı**: Kuralı bireysel bir kullanıcıya uygulayın.
- **Kullanıcı Grubu**: Kuralı belirli bir kullanıcı grubuna uygulayın.
- **Start Date & End Date**: Kuralın geçerlilik süresini ayarlayın.
- **Kaynak Adres**: Kaynak-address-sping.
- **Hedef Adres**: Hedefe özgü routing.

---

### Routing Politikaları

İş gereksinimlerine veya SLAs'a dayanan politikaları tanımlayabilirsiniz. Mevcut routing politikaları şunları içerir:

#### **LCR (Least Cost Routing)**
- Belirli bir varış için en düşük yapılandırılmış maliyeti sunan satıcı ağ geçidi aracılığıyla trafik.
- Fiyatlarını optimize etmek ve kâr marjlarını artırmak yardımcı olur.

#### **Sabit Gateway**
- Tüm trafik tek, önceden tanımlanmış bir ağ geçidi aracılığıyla yollanır.

#### **Yuvarlak Robin**
- Dağcılık, seçilmiş ağ geçitlerinde bile geçerlidir.
- Tüm yapılandırılmış ağ geçidinin optimal kullanımını sağlar.

#### **Dağıtılmış**
- Gelişmiş yük dengeleme yöntemi.
- Yollar trafik oranına göre birden fazla ağ geçidine yol açıyor (örneğin,% 60,% 10).

#### **ACD/DLR (Acbilgid Delivery)**
- Ayrıca teslimat tabanlı routing olarak da bilinir.
- En yüksek Teslimat Oranı (DLR) ile satıcı ağ geçidine yol açıyor, gerçek zamanlı kaliteli performans sağlar.

---

### Öncelik

!!! info "Öncelik"
 Birden fazla yönlendirme kuralı bir mesajla eşleştirirse, **iTextPRO en yüksek öncelik değeri ile kuralı seçecek** (toplam olarak en yüksek).

Bu güçlü routing mantığı, SMS trafiğinizin verimli, ekonomik ve iş mantığına uygun olmasını sağlar - hizmet kesintilerine veya sistem yeniden başlatmalarına gerek kalmadan.
