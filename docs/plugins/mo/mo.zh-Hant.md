
# 毛澤東

## 定義
MO 訊息 (**移動來源** )由行動電話使用者發起,並使用特定關鍵詞傳送到專用的短碼或長碼. 
它們允許客戶或訂戶與供應商或應用程式直接互動。

---

## 程序

### 使用者啟動
客戶向專用短碼或長碼傳送帶有特定關鍵詞的簡訊.

**示例** 
<span data-ph="0"></span> → <span data-ph="1"></span>

### 訊息執行
電文被傳送到與該短碼或號碼相連結的應用程式或供應商.

---

## 關鍵點
- 實現使用者與供應商雙向通訊.
- 使用特定關鍵詞來觸發響應.
- 透過專用短碼或長碼工作.

---

## HTTP MO 處理器配置

### 概覽
HTTP MO 處理器在 **電子文字Pro** 收到供應商寄來的MO訊息。 
有效載荷結構因供應商而異。

### 步驟1: 新增新處理器
1. 點選 **新增新處理器**。 。 。 。
2. 在UI中對映有效載荷引數.

![MO Handler Config](images/mo1.png)

**先決條件:** 
對RESTFL API的基本理解.

**示例( Vendor: Airtel) :**
```json
{
  "originatorAddress": "999563256",
  "destinationAddress": "8754321565",
  "messageContent": "BINGO 101",
  "CustomerId": "669912"
}
```

**iTextPro 配置 :**
- 方法 : <span data-ph="0"></span>
- 內容型別 : <span data-ph="0"></span>
- 發件人金鑰 : <span data-ph="0"></span>
- 目標金鑰 : <span data-ph="0"></span>
- 信件金鑰 : <span data-ph="0"></span>

![MO Config 2](images/mo2.png)

---

### 第2步:為使用者賬戶配置MO服務
1. 登入到 iTextPro 找到使用者賬戶 。
2. 啟動 **MO 服務** 內 **管理服務**。 。 。 。
3. 設定 MO 編號關鍵詞( K) :
   - 結束日期
   - 選擇頻道( MO 號碼)
   - 關鍵詞(或 <span data-ph="0"></span> 成員名單)
   - 狀態: 活動
4. 點選 **新增**。 。 。 。

![MO Config 3](images/mo3.png) 
![MO Config 4](images/mo4.png)

---

### 第3步:MO 執行規則配置
1. 轉到 **MO 執行規則**。 。 。 。
2. 建立或編輯一條規則 :
   - 規則名稱、開始/結束日期
   - 閘道器介面:HTTP/SMPP
   - 條件: 發件人、 目的地、 信件
   - 使用者端點( E) : HTTP Webhook 或 ESME

![MO Routing](images/mo5.png) 
![MO Routing UI](images/mo6.png) 
![MO Routing Rule](images/mo7.png)

---

## MO 模組訪問
1. 假名/ Login 到使用者賬戶 。
2. 開啟 **MO 模組** 以檢視MO訊息。

![MO Inbox](images/mo8.png) 
![MO Keyword](images/mo9.png) 
![MO Keyword Details](images/mo10.png)

---

## 自動回覆
- 設定 MO 訊息的自動回覆 。

![MO Auto Reply](images/mo11.png)

---

## 通知
- **電子郵件轉發** – 透過電子郵件接收MO提醒. 
- **移動轉發** - 透過簡訊接收警報(包括國家程式碼)。

![MO Mobile Notify](images/mo12.png)

---

## 管理子關鍵字
子關鍵詞是主關鍵詞後起的次要觸發.

**示例**
- **主要關鍵詞:** 中非共和國 
- **自動響應 :** 
 <span data-ph="0"></span>
- **子關鍵詞 1:** 對 <span data-ph="0"></span> 
- **分關鍵詞2:** 沒有 □ <span data-ph="0"></span>

![MO Sub-keyword](images/mo13.png)

---

## 報告
- 匯出MO報告給Excel.
- 由關鍵詞或子關鍵詞過濾.

**步驟 :**
1. 轉到 **報告**。 。 。 。
2. 點選 **匯出報告**。 。 。 。
3. 下載和定製 。

![MO Reports](images/mo14.png) 
![MO Reports 2](images/mo15.png)

---

## MO 網路呼號
實時 MO 訊息傳送到給定的 HTTP 端點.

**設定 :**
1. 啟用 **HTTP 網路推** 在父賬戶中。
2. 轉到 **MO 網路呼號** → **新增新 Webhook 選項**。 。 。 。
3. 設定 :
   - 名稱
   - 端點 URL
   - 方法:獲取/部署
   - 處理器:MO

**說明:** 
如果端點無法到達,MO會被丟棄. 暫停10秒。

![MO Webhook](images/mo16.png) 
![MO Webhook Config](images/mo17.png)