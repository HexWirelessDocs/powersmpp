
# 電子郵件模板

## 關鍵特性

### 自動監測
- **電子文字Pro** 持續定期監測應用程式的關鍵引數。
- 在潛在問題升級前主動查明.

### 透過電子郵件發出警告
- 利益攸關方透過電子郵件通知收到提醒。
- 提前發出通知,使利益攸關方能夠採取預防措施。

### 自定義模板管理
- 支援自定義的提醒模板 。
- 使用者可以根據自己的要求管理和調整通知模板.

### 系統變數整合
- 自定義模板可以包括相關的系統變數.
- 透過動態更新的系統資訊實現個性化通訊.

---

## 使用準則

### 模板管理
- 自定義提醒模板,以適應特定的通訊需要。
- 納入動態和對上下文有敏感認識通知的相關係統變數。

### 利益攸關方的參與
- 確保為接收通知對相關利益攸關方進行配置。
- 驗證電子郵件設定是否為無縫通訊正確配置 。

---

## 福利
- 增強《公約》的可靠性和穩定性 **電子文字Pro** 應用。
- 提供積極主動的發現和警報機制。
- 定製的模板和系統變數能夠進行個性化和內容化的交流。
- 幫助各組織克服潛在的挑戰。

!!! note
 SMTP的細節對於管理員以及再銷售賬戶來說都是強制性的,以觸發電子郵件.

---

## 電子郵件模板管理

![Email Templates](images/template1.png)

---

## 通知事件和對應模板

### 總體報告失敗
當彙總報告服務遇到未知失敗時觸發. 
![Aggregate Reporting Failure](images/template2.png)

### 核准通知
在發件人ID和模板請求的管理員批准後傳送。 
![Approval Notification 1](images/template3.png) 
![Approval Notification 2](images/template4.png)

### 核准請求
當再銷售者/使用者啟動發件人ID或模板批准請求時觸發. 
![Approval Request Notification 1](images/template5.png) 
![Approval Request Notification 2](images/template6.png)

### 更改密碼
當用戶成功更改密碼時傳送 。 
![Change Password](images/template7.png)

### 信用通知
當用戶可用餘額低於信用門檻時發出警報。 
![Credit Notification](images/template8.png)

### 信貸轉賬
由使用者或轉售者在使用者賬戶中新增餘額後觸發. 
![Credit Transfer](images/template9.png)

### 電子郵件郵箱
當 MO 電子郵件轉發啟用時, 當收到信件時傳送 。 
![Email Post](images/template10.png)

### 埃斯梅黑名單
當一個ESME賬戶因垃圾郵件而被列入黑名單時會發出警報. 
![Esme Blacklist](images/template11.png)

### 失敗的閘道器
當由於主閘道器中斷而發生自動訊息切換時觸發. 
![Failover Gateway](images/template12.png)

### 忘記密碼
當請求更改登入賬戶密碼時傳送 。 
![Forgot Password](images/template13.png)

### 黑名單閘道器
當一個 SMPP 供應商閘道器/ 路由在失敗的繫結嘗試後被列入黑名單時提醒 。 
![Gateway Blacklisted](images/template14.png)

### 閘道器價格過期
當檢測到有過期速率的路徑時觸發 。 
![Gateway Price Expiry](images/template15.png)

### 工作不批准通知
當傳送者ID或模板請求被管理員/銷售者不批准時傳送. 
![Job Disapproved Notification 1](images/template16.png) 
![Job Disapproved Notification 2](images/template17.png)

### 信件佇列
當供應商閘道器佇列違反閾限時觸發. 
![Message Queue](images/template18.png)

### 由管理員建立的新賬戶
當行政部門新增或簽名時傳送。 
![New Account by Admin](images/template19.png)

### Reseller 新建賬戶
當再銷售者添加了新使用者或新使用者簽名後傳送到再銷售使用者. 
![New Account by Reseller](images/template20.png)

### 新建使用者電子郵件驗證
觸發新使用者報名電子郵件驗證 。 
![New User Email Verification](images/template21.png)

### 檢察官辦公室
在使用者登入時傳送檢察官辦公室核查。 
![OTP](images/template22.png)

### 服務狀況
當惡魔/服務自動恢復時發出警報.

### 服務已停止
當惡魔/服務被故意停止時觸發. 
![Service Stopped](images/template23.png)

### 垃圾郵件檢測
當發現SPAM內容時發出警報. 
![Spam Detection](images/template24.png)

### 使用者銷售更新
客戶銷售價格由母賬戶更新後傳送. 
![User Selling Update](images/template25.png)

---

這些通知涵蓋廣泛的活動,提供了全面的見解並及時發出警報,以確保有效監測和管理 **電子文字Pro** 平臺。
