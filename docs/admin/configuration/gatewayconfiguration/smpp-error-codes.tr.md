---
tags:
  - SMPP
  - Error Codes
  - Reference
  - Gateway
---

# Standart SMPP Error Code Listesi

Bu sayfa tüm SMPP protokolü hata kodlarının tam bir referansını sağlar, iTextPro uygulama hata kodları ve iTextHub HTTP Gateway hata kodları. Raporlarda görülen mesaj teslimat başarısızlıklarını teşhis etmek için bu referansı kullanın, PDU logları ve etkinlik izleyicileri.

---

## Standart SMPP Hata kodları

Bunlar SMPP v3.4 spesifikasyonu tarafından tanımlanan protokol düzeyinde hata kodlarıdır. SMSC (Short Message Service Centre) tarafından SMPP operasyonlarına yanıt olarak geri döndüler.

| Sr. Hayır | Hata Kodu (Hex) | Hata Kodu (Decimal) | Hata Adı | Hata Açıklama |
|--------|-----------------|---------------------|------------|-------------------|
| 1 1 1 | 0x00 | 0 0 0 0 | Komutan başarıyla idam edildi | SMPP komutu hata yapmadan işlendi |
| 2 2 | 0x01 | 1 1 1 | Mesaj uzunluğu geçersizdir | Mesaj gövdesi uzunluğu sınırları aşıyor |
| 3 3 | 0x02 | 2 2 | Komut Uzunluk geçersizdir | PDU komut uzunluğu alanı yanlış |
| 4 4 4 | 0x03 | 3 3 | Invalid Komutanlığı ID | Komut kimliği SMSC tarafından tanınmaz |
| 5 5 | 0x04 | 4 4 4 | Verilen komut için uygun BIND statüsü | ESME, mevcut bağlayıcı devletine izin verilmeyen bir komuta denedi |
| 6 6 | 0x05 | 5 5 | ESME Zaten Bound State | ESME zaten bağlıdır ve tekrar bağlayamaz |
| 7 7 7 | 0x06 | 6 6 | Invalid Beforeity Flag | PDU'daki öncelikli bayrak değeri geçerli değil |
| 8 8 | 0x07 | 7 7 7 | Invalid Registered Delivery Flag | Kayıtlı teslimat bayrağı değeri geçerli değildir |
| 9 9 | 0x08 | 8 8 | Sistem Hatası | SMSC'de genel bir sistem hatası meydana geldi |
| 10 10 | 0x0A | 10 10 | Invalid Source Address | Kaynak (sender) adresi geçersizdir veya izin verilmez |
| 11 11 11 | 0x0B | 11 11 11 | Invalid Destination Address | Hedef (recipient) adresi geçersizdir |
| 12 | 0x0C | 12 | Mesaj ID geçersizdir | Kimlik referansı mevcut değildir |
| 13 13 | 0x0D | 13 13 | Bind Başarısız | Bağlantı işlemi kimlik doğrulama veya yapılandırma sorunları nedeniyle başarısız oldu |
| 14 14 | 0x0E | 14 14 | Invalid Password | Bağlanma sırasında sağlanan şifre yanlış |
| 15 15 | 0x0F | 15 15 | Invalid System ID | Bağlantı sırasında sağlanan sistem kimliği tanınmamıştır |
| 16 | 0x11 | 17 17 17 | SM Başarısız Oldu | İptal sm operasyonu tamamlanmamış olabilir |
| 17 17 17 | 0x13 | 19 19 | SM'yi Değiştirin Başarısız | sm operasyonu tamamlanmamış olabilir |
| 18 | 0x15 | 21 21 21 | Invalid Service Type | Servis type parametresi geçerli değildir |
| 19 19 | 0x33 | 51 51 51 51 | Invalid sayıda destinasyon | Transfer multi'deki destinasyon sayısı geçersizdir |
| 20 20 | 0x34 | 52 52 52 | Invalid Dağıtım Listesi adı | Dağıtım listesi adı referansı mevcut değildir |
| 21 21 21 | 0x40 | 64 64 64 | Hedef bayrağı geçersizdir (submit multi) | Temsil flag in submit multi, geçersiz bir değer içeriyor |
| 2222 | 0x42 | 66 66 66 66 | w/replace unsupported | Özel MC için desteklenmeyen veya uygunsuz olduğu yerde yükleme işlemi talep edildi. |
| 23 23 23 | 0x43 | 67 | Invalid esm class field data data | esm class alanı geçersiz veri içeriyor |
| 24 | 0x44 | 68 68 68 | Dağıtım Listesine gönderilemez | Mesaj belirtilen dağıtım listesine gönderilemez |
| 25 | 0x45 | 69 69 69 69 | sm, data sm veya gönderin multi başarısız | Teklif işlemi başarısız oldu |
| 26 | 0x48 | 72 72 72 | Invalid Source adresi TON | Kaynak adresi için Sayı Türü geçersizdir |
| 27 27 | 0x49 | 73 73 | Invalid Source adresi NPI | Kaynak adresi için Sayısal Plan Göstergesi geçersizdir |
| 28 28 28 | 0x51 | 81 81 81 81 | Invalid Destination NPI | Hedef adresi için Sayısal Plan Göstergesi geçersizdir |
| 29 29 29 | 0x53 | 83 83 | Invalid system type field | Sistem type parametresi geçerli değildir |
| 30 30 30 | 0x54 | 84 84 84 84 | Invalid replace if present Flag | Değiştirilmiş bayrak geçersiz bir değer içeriyor |
| 31 31 31 | 0x55 | 85 85 85 85 | Invalid sayıda mesaj | Mesaj parametresi sayısı geçersizdir |
| 32 32 32 | 0x58 | 88 88 88 88 | Throttling hatası | ESME mesaj sınırlarını aştı (TPS throttling) |
| 33 33 33 33 | 0x61 | 97 97 97 | Invalid Scheduled Delivery Time | Planlanan teslimat süresi veya değeri geçersizdir |
| 34 | 0x62 | 98 98 98 | Invalid mesajı geçerlilik süresi | Mesaj geçerliliği süresi (expiry zamanı) geçersizdir |
| 35 35 35 | 0x63 | 99 99 99 99 | Predefined Message ID Invalid | Belirtilen önceden tanımlanmış mesaj bulunamadı |
| 36 | 0x65 | 101 101 101 | ESME Sürekli App Hata Kodu | ESME alıcısında kalıcı bir uygulama hatası |
| 37 37 37 37 | 0x66 | 102 102 | ESME Alıcı Reject Mesaj Hata Kodu | ESME alıcı mesajı reddetti |
| 38 38 38 | 0x67 | 103 103 103 | Query Sm isteği başarısız oldu | Soru sm operasyonu tamamlanmamış olabilir |
| 39 39 | 0xC0 | 192 192 192 192 | PDU Bedeninin Seçmeli bölümünde hata | PDU vücudundaki opsiyonel TLV parametreleri hataları içerir |
| 40 40 | 0xC1 | 193 | TLV izin verilmez | TLV parametresi bu işlem için izin verilmez |
| 41 41 | 0xC2 | 194 | Invalid parametre uzunluğu | Bir TLV parametresinin geçersiz bir uzunluğu vardır |
| 42 42 42 | 0xC3 | 195 195 195 | Beklemiş TLV eksik | Gerekli TLV parametresi PDU'dan eksik |
| 43 43 43 43 | 0xC4 | 196 | Invalid TLV Değer | Bir TLV parametresi geçersiz bir değer içeriyor |
| 44 44 | 0xFE | 254 | İşlem Teslimi Başarısızlık Başarısızlık Başarısızlığı | Mesaj işlemi teslim edilemez |
| 45 | 0xFF | 255 255 | Bilinmeyen Hata | Bilinmeyen veya tanımlanmamış bir hata meydana geldi |
| 46 46 46 | 0x100 | 256 256 256 | ESME Belirtilen hizmet türü kullanmaya yetkili değil | ESME talep edilen hizmet türü için yetkili değildir |
| 47 | 0x101 | 257 | Belirtilen işlemden alınan ESME Prohibited | ESME, belirtilen operasyonu kullanarak siyah listelenmiş veya yasaklanmıştır. |
| 48 | 0x102 | 258 | Specified service type is available | Talep edilen hizmet türü şu anda mevcut değildir |
| 49 49 49 | 0x103 | 259 | Açıklamalı hizmet türü reddedilir | Talep edilen hizmet türü reddedilmiştir. |
| 50 50 50 | 0x105 | 261 | Source Address Sub ünitesi Invalid | Kaynak adresi alt parametresi geçersizdir |
| 51 51 51 51 | 0x106 | 262 | Hedef Adres Alt ünitesi Invalid | Hedef adresi alt parametresi geçersizdir |
| 52 52 52 | 0x107 | 263 | Yayın Frekans Interval geçersizdir | Yayın frekansı parametresi geçersizdir |
| 53 53 53 | 0x108 | 264 | Yayın Alias Name geçersiz | Yayın alias adı geçerli değil |
| 54 54 54 | 0x109 | 265 | Yayın Alan Formatı geçersizdir | Yayın alanı formatı parametresi geçersizdir |
| 55 55 55 | 0x10A | 266 | Yayın Alanları sayısı geçersizdir | Belirtilen yayın alanlarının sayısı geçersizdir. |
| 56 56 56 56 | 0x10B | 267 | Yayın Tipi geçersizdir | Yayın içerik türü parametresi geçersizdir |
| 57 57 57 | 0x10C | 268 | Yayın Mesaj Sınıfı geçersizdir | Yayın mesajı sınıfı geçersizdir |
| 58 58 | 0x10D | 269 | Yayın sm operasyonu başarısız oldu | Yayın sm operasyonu tamamlanmamış olabilir |
| 59 59 59 | 0x10F | 271 | Cancel broadcast sm operasyonu başarısız oldu | İptal broadcast sm operasyonu tamamlanmamış olabilir |
| 60 60 60 | 0x110 | 272 | Tekrarlanan Yayın Sayısı geçersiz | Tekrarlanan yayınların parametresi sayısı geçersizdir |
| 61 | 0x111 | 273 | Yayın Servisi Grubu geçersizdir | Yayın servisi grubu parametresi geçersizdir |
| 62 | 0x112 | 274 | Yayın Kanal Göstergesi geçersizdir | Yayın kanalı göstergesi geçersizdir |
| 63 | 0x15F95 | 90005 | Local Exception | Detaylar için LastException mülkünü kontrol edin |

---

## iTextPro Hata kodları

Bunlar iTextPro / Power SMPP platformu tarafından üretilen uygulama düzeyinde hata kodlarıdır. Sorunları routing, billing, hesap yapılandırması veya sistem operasyonları ile göstermektedir.

| Sr. Hayır | Hata Kodu (Hex) | Hata Kodu (Decimal) | Hata Adı | Hata Açıklama |
|--------|-----------------|---------------------|------------|-------------------|
| 64 64 64 | 0x439 | 1081 | Ülke Undef | Ülke, Master Data Manager tarafından tanımlanmadı |
| 65 65 65 | 0x43A | 1082 | Invalid Network | Master Data Manager tarafından tanımlanmamış ağ |
| 66 66 66 66 | 0x43B | 1083 | Fiyat Tanımlanmamış | İlgili ülke ve ağ için yönetici tarafından tanımlanamayan fiyat birincil ağda |
| 67 | 0x43C | 1084 | Açıklama : (Loss Protection) | Koruma politikası nedeniyle hiçbir şey yaşamadı |
| 68 68 68 | 0x43D | 1085 | Route Undef | İlgili ülke ve ağ ağı için yönetici tarafından tanımlanma |
| 69 69 69 69 | 0x43E | 1086 | Failover Route Undef | Master failover, ilgili ülke ve ağ için yönetici tarafından tanımlanmadı |
| 70 70 70 | 0x43F | 1087 | Başarısızlık Açıklama | Başarısızlık ağ geçidi üzerinde koruma nedeniyle mesajların hayatta kalması |
| 71 71 71 | 0x440 | 1088 | Başarısız fiyat | İlgili ülke ve ağ için yönetici tarafından tanımlanamayan fiyatsız ağ |
| 72 72 72 | 0x441 | 1089 | Başarısızlık Başarısızlık | Sistem Hatası: Başarısızlık sırasında dışlanmış istisna |
| 73 73 | 0x442 | 1090 | Hesap Geçerliliği Açıklama | Kullanıcı hesabı geçerliliği sona ermiştir |
| 74 74 | 0x443 | 1091 | Encoding Error | Sistem Hatası: Başarısız veri kodlama değeri nedeniyle hata ( 0 & 8 dışında veri kodlama değerlerini göndererek yeniden oluşturulabilir) |
| 75 75 | 0x444 | 1092 | OA/DA Hata | Sistem Hatası: OA/DA Hatası normalleştirme kuralları nedeniyle |
| 76 76 76 76 | 0x445 | 1093 | Queue Mesaj Açıklama | Sistem Hatası: Queue mesajı uzun ağ geçidi nedeniyle sona erdi |
| 77 77 77 | 0x446 | 1094 | Invalid HTTP Gateway Config | Sistem Hatası: Invalid HTTP ağ geçidi yapılandırma veya yanıt kodu |
| 78 | 0x417 | 1047 | Kullanıcı Hesabı Inaktif | Kullanıcı hesabı aktiftir ve mesajları gönderemez |
| 79 79 79 | 0x400 | 1024 1024 | Kullanıcı Hesabı Locked | Kullanıcı hesabı yönetici tarafından kilitlendi |
| 80 80 80 | 0x401 | 1025 | Yetersiz Denge | Kullanıcı hesabında yeterli bakiye (pre ücretli) |
| 81 81 81 81 | 0x402 | 1026 | Template Mismatch | Şablon yanlış uyumlu - mesaj içeriği onaylanmış şablonla eşleşmez |
| 82 82 82 | 0x405 | 1029 | Invalid Sender ID | Invalid veya onaylanmamış Sender ID tespit edildi |
| 83 83 | 0x407 | 1031 | Global Blacklist Number | Hedef numarası küresel kara liste üzerindedir |
| 83 83 | 0x40B | 1035 | Aktif Bağlantı No Active Connection | Ağ geçidi için mevcut olan aktif SMPP bağlantısı yok |
| 84 84 84 84 | 0x40C | 1036 | Queue Server Hata | Sistem Hatası: Mesaj kuyruk iç sunucu hatası |
| 85 85 85 85 | 0x40D | 1037 | Cache Server Hata | Sistem Hatası: Cache veritabanı hatası |
| 86 86 86 | 0x40E | 1038 | Invalid Connection State | Ağ Hatası: Gateway ulaşılamaz |
| 87 87 87 | 0x40F | 1039 | SMPP Timeout | Ağ Hatası: Gateway zamanıout – hiçbir cevap alındı |
| 88 88 88 88 | 0x410 | 1040 | Bilinmeyen SMPP Hatası | Sistem Hatası: Sınıfsız SMPP hatası meydana geldi |
| 89 89 | 0x411 | 1041 | Final Disconnection | SMPP bağlantısı kalıcı olarak kesildi |
| 90 90 90 90 | 0x412 | 1042 | Final Timeout | Bağlantı süresi kalıcı olarak çıktı |
| 91 91 91 91 | 0x413 | 1043 | No Gateway Found | Mesajı takip etmek için uygun bir ağ geçidi bulunamadı |
| 92 92 92 92 | 0x404 | 1028 | Invalid IP | SMPP hesabı için uygun IP adresi (IP doğrulama başarısız oldu) |
| 93 93 93 93 | 0x414 | 1044 | Spam tespit edildi | Mesaj, içerikte tespit edilen spam anahtar kelime nedeniyle başarısız oldu |
| 94 94 94 | 0x448 | 1096 | Mesaj uzunluğu | SMS mesajı uzunluğu izin verilen sınırı aştı |

---

## iTextHub HTTP Gateway Hata kodları

Bu hata kodları iTextHub HTTP Gateway tarafından HTTP API isteklerini işlemekte.

| Sr. Hayır | Hata Kodu (Decimal) | Hata Adı | Hata Açıklama |
|--------|---------------------|------------|-------------------|
| 95 95 95 | 110 110 | metin yanıtlarken hata | HTTP Gateway yanıtını almak için başarısız oldu |
| 96 | 111 | JSON/XML yanıt alırken hata | HTTP ağ geçidinden JSON veya XML yanıtını başarısız oldu |
| 97 97 97 | 112 112 | Hata, yanıt verirken | HTTP yanıt akışını okumak için başarısız oldu |
| 98 98 98 | 113 113 | Hata, sonuçta yanıt okuyarak | HTTP yanıt sonucu verileri çıkarmak için başarısız oldu |
| 99 99 99 99 | 114 | REST/JSON API talep ederken hata | HTTP ağ geçidi için bir REST /JSON API isteği yapmak için başarısız oldu |
| 100 100 100 100 | 115 115 | Basit HTTP API talep ederken hata | HTTP ağ geçidi için basit bir HTTP API isteği yapmak için başarısız oldu |
| 101 101 101 | 116 | SOAP API talep ederken hata | HTTP Gateway isteği yapmak için başarısız oldu |
| 102 102 | 1095 | SOAP/Simple/RestJson API talep ederken hata | 114, 115 ve 116 için birleşik hata kodu (en son versiyonda kullanılır) |

---

!!! tip "Bu referansı nasıl kullanılır"
    - Bir hata kodu gördüğünüzde **Kampanya Raporları**, **PDU Logs**Ya da **Event Viewer**Yukarıdaki tablolara bakın
    - **Standart SMPP kodları** (0-255) dış SMSC/gateway tarafından geri döndü
    - **iTextPro kodları** (1024-1096), Power SMPP platformu tarafından içsel olarak üretilir.
    - **HTTP GW kodları** (110-1095) HTTP ağ bağlantı sorunlarıyla ilgilidir
    - Belirli bir hata kodu yapılandırması için [Gateway Hata kodları](errorcode.md)
