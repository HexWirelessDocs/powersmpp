

# İzinler

## Hesap Rol Executive Privileges in iTextPRO

In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In **iTextPRO**Ancak yöneticiler ve bayiler belirli ayrıcalıklar sağlayabilir **Hesap Rol Yöneticileri**, belirli çalışma alanlarına erişimlerini tertemiz. 
Çeşitli sorumluluklar yerine getirmek için birden fazla Executive rolü oluşturulabilir.

### Örnek Roller

**Finans Ekibi Rol**
- Billing Bölüm Access
- Raporlama Bölüm Access
- Diğer İlişkili Privileges

**NOC Team Role**
- İzleme Log Access
- Raporlama Bölüm Access
- Yönetim Seçenekleri
- Diğer İlişkili Privileges

**Giriş Prosedürleri:**
- **Admin'in Yöneticisi:** Admin'in Giriş URL ve Port'ı kullanın.
- **Bayilik Yöneticisi:** Bayinin Giriş URL ve Port'ı kullanın.

Bu segregasyon, yöneticiler için güvenli ve özel bir giriş deneyimi sağlar, hareketle sorumluluklarıyla uyumlu fonksiyonelliğe erişim sağlar.

![Permission Example](images/permission1.png)

---

## İzin Kategoriler

iTextPRO'deki Executive kullanıcılar için izinler modüller içindeki erişim düzeyi ve eylemlere göre kategorize edilir.

### Kategoriler Kategoriler

**View View View View** 
- Belirtilen modül içindeki içerikleri görebilir. 
- *Hiçbir değişiklik veya kesintiler izin verilmez.*

**Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add Add** 
- Modüle yeni girişler ekleyebilir. 
- *Mevcut girişleri düzenleyebilir veya silemez.*

**Edit** 
- Mevcut girişleri düzenleyebilir / değiştirebilir. 
- *Hiçbir kesinti hakkı yok.*

**Delete** 
- Modülden girişleri silebilir. 
- *Hiçbir düzenleme hakkı yok.*

**Full Control Full** 
- Grants view, add, edit ve belirtilen modül için hakları sil. 
- Unrestricted access.

![Permission Categories](images/permission2.png)

---

## Full Control & Hierarchy

In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In In **iTextPRO**, **Full Control Full** Kapsamlı erişim sağlar.

**Aktivasyon Senaryoları:**
1. Enabling Full Control at the **Üst seviye seviye** otomatik olarak tüm alt-modules'a verir.
2. Onu bir kere için **Özel modül** View, Add, Edit ve Delete.

**Hierarchy:**
- Seviyeler farklı bölümler, işlevleri veya veri kategorileri temsil eder.
- Daha yüksek düzeydeki tüm alt düzeylere tam kontrol.

**Explicit Disabling:**
- Sub-modules'teki özel izinler, Full Control ile bile manuel olarak devre dışı kalabilir.

![Permission Hierarchy](images/permission3.png)

---

## İzin Türü

### Bireysel Kullanıcı İzinleri
- Grants belirli bir yönetici kullanıcıya izin verir.

**Prosedür:**
1. Go to Go to Go to Go **Yönetme izni** Sayfa.
2. Select Select Select Select **Bireysel Bireysel** İzin türü olarak.
3. Aşağıdan bir kullanıcı seçin.
4. Click Click Click Click Click **Show Show Show Show Show** Görmek / Yetkilendirme izni.

![Individual Permissions](images/permission4.png)

---

### Executive User Group Permissions
- Grants bir gruba izin verir; tüm grup üyeleri tarafından miras alınır.

**Prosedür:**
1. Go to Go to Go to Go **Yönetici Kullanıcı Gruplarını Yönetin** Sayfa.
2. Click Click Click Click Click **Ekle User Group**.
3. Grup adı girin ve kullanıcıları seçin.
4. Gruptan tasarruf edin.
5. Use Use Use Use Use Use **Toplam Kullanıcılar** Üyeleri görüntülemek için.
6. Gerekli olduğu gibi grupları analiz veya sil.

 *Bir yöneticinin hem kullanıcı özel hem de grup izni varsa, ikisi de alırlar.*

![Group Permissions](images/permission5.png)

---

## Modül Viability

- Eğer bir yönetici izinden yoksunlarsa, görecekler **"Yedi Denied"** Giriş üzerine sayfa.
- İzinler giriş yaparken iptal edilirse, eylemler gösterecektir **"Yedi Denied"**.
- Modüller, verilen izinlere dayalı olarak gösteriliyor.

Örnek: Örnek: 
- Eğer eğer **Yapılandırma** ve **Billing** verilir, sadece bu modüller görünür.

![All Modules](images/permission6.png) 
![Filtered Modules](images/permission7.png)