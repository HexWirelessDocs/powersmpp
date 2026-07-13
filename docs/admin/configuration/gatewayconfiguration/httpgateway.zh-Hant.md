---
tags:
  - HTTP
  - Gateway
  - Configuration
---

# HTTP 閘道器

單位 **電源 SMPP**我們兩個都支援 **SMPP 軟體** 財務報告和審定財務報表 **HTTP 密碼** 供應商連通協議。 因此,管理員可以選擇配置基於 SMPP 的閘道器或 HTTP 閘道器 。 該檔案提供了HTTP閘道器配置的簡明概覽. 它旨在幫助管理員理解並輕鬆地在Power SMPP應用程式內設定了HTTP閘道器.

如名稱所示,HTTP閘道器基於 **超文字傳輸協議( HTTP)**。此協議允許客戶端透過一個作為Power SMPP應用程式內閘道器的API傳送訊息.

![Manage Gateway list view](images/httpgw-01-manage-gateway.png)

**導航 :** <span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span> ➔ <span data-ph="3"></span> ➔ <span data-ph="4"></span>。 。 。 。

![HTTP Gateway Detail sections](images/httpgw-02-detail-sections.png)

!!! tip "檢視文件"
 點選時 **新增新內容**,第一個選項是 **檢視文件**。我們建議管理員審查該檔案,以便熟悉閘道器配置中提及的術語。

HTTP Gateway 詳細螢幕分為以下幾節:

- 所需全權證書
- 信件型別
- 引數
- 有條件引數
- 閘道器屬性
- 響應屬性
- 會議
- 自動傳送信件

---

## 第1節:必要的全權證書

本節需要各種資料,例如: **閘道器名稱**, (中文(簡體) ). **請求型別**, (中文(簡體) ). **認證**, (中文(簡體) ). **基礎 URL**,以及 **UDH 軟體**。 。 。 。

**閘道器名稱** ——HTTP Gateway的易名.

**需要UDH嗎?** - 指定是否為 **UDH (使用者資料頭)** 用於從此閘道器傳送信件。 UDH用於收縮信件.

**請求型別** ——指定HTTP請求的型別。 這可能是 **簡單 HTTP**, (中文(簡體) ). **資源/JSON**,或 **SOPAP 軟體**。不同的請求型別需要不同的配置。 一般情況下,簡單的HTTP用於 <span data-ph="0"></span> 方法,而 REST/JSON 可用於兩者 <span data-ph="1"></span> 財務報告和審定財務報表 <span data-ph="2"></span> 方法。 。 。

![Required Credentials form](images/httpgw-03-required-credentials.png)

**基礎 URL 細節** 指定 HTTP API 的基礎 URL, **不包括** 所有其他引數。

!!! example
 如果 API URL 是 <span data-ph="0"></span>,然後將 Base URL 配置為 <span data-ph="1"></span>。 。 。 。

**認證** - Power SMPP目前支援三種授權:

| {\fn方正粗倩簡體\fs12\an8\1cHFFFF00\b0} | 型別 | 說明 |
|---|------|-------------|
| 1個 | **無授權** | 無需批准。 |
| 2個 | **基本認證** | API的安全認證需要使用者名稱和密碼. |
| 3個 | **OAuth 2.0 資料** | 最新版本的授權,用於在一段時間後重新生成新的證書,以保持API的高安全性。 **OAuth 處理器** API (英語). |

![Authentication options](images/httpgw-04-authentication.png)

---

## 第2節:資訊型別

**信件型別** 是一個可選的段落,管理員可以在此配置供應商接受的資料編碼值。 每個資料編碼型別的預設值在括號中被提及.

| 型別 | 預設 | 目的 |
|------|---------|---------|
| **文字** | <span data-ph="0"></span> | 繪製純文字訊息的閘道器專用訊息型別 。 |
| **聯合國** | <span data-ph="0"></span> | 繪製Unicode訊息的閘道器專用訊息型別. |
| **比利時** | <span data-ph="0"></span> | 繪製二進位制信件的閘道器專用訊息型別 。 |
| **弗拉什語Name** | <span data-ph="0"></span> 或者說 <span data-ph="1"></span> | 繪製快閃記憶體訊息的閘道器專用訊息型別 。 |

!!! note
 以系統訊息型別對映您的閘道器特定訊息型別 。 如果不適用,請將欄位留空。

![Message Types form](images/httpgw-05-message-types.png)

---

## 第3節:引數

這個 **引數** 區域允許管理員配置閘道器細節並請求閘道器供應商提供的引數。 這些引數被Power SMPP用於構建並傳送API請求的資料/體給相應的閘道器供應商進行訊息處理和傳送.

所配置的引數定義了HTTP請求如何在API通訊中生成和執行.

### 方法

Power SMPP支援下列HTTP方法用於API執行:

#### 1] 獲取方法

GET 方法允許管理員在 **鍵值對** 格式。 API 執行期間,所有配置的引數直接被附加到 URL 上作為 **查詢引數**。 。 。 。

這種方法一般用於:

- 簡單的 API 請求
- 基於 URL 的引數傳輸
- 輕量級 API 整合
- 遺產 HTTP 整合

!!! example
 <span data-ph="0"></span>

在GET方法中,Power SMPP支援以下引數型別:

##### 父名稱

這個 **父名稱** 欄位主要用於 **基於 SOAP** API整合,其中需要將引數組合到父 XML 節點或請求物件下.

這種配置有助於按照供應商API的規格生成結構化的SOAP請求有效載荷.

!!! example
    ```xml
    <SendSMS>
        <username>admin</username>
        <password>test123</password>
    </SendSMS>
    ```
 在上述例子中, <span data-ph="0"></span> 作為父母姓名。

##### 頁首引數

這個 **頁首引數** 區域用於配置 API 執行過程中所需的 HTTP 頭值。

這些引數一般用於:

- 身份驗證
- API 金鑰
- 全權證書
- 內容 - 型別定義
- 自定義供應商信頭

!!! example
    ```
    Authorization: Bearer xxxxx
    Content-Type: application/json
    ```

標題引數在API通訊期間在HTTP請求標題內傳輸.

##### 引數

這個 **引數** 區域包含 HTTP API 請求所需的所有一般請求引數。

這些引數通常包括:

- 移動號碼
- 信件內容
- 發件人標識
- 模板 ID
- 實體標識
- 執行引數
- 自定義供應商引數

對於 **獲取** 請求,這些引數在請求 URL 中作為查詢引數在 API 執行過程中附加.

![Parameters configuration with example rows](images/httpgw-06-parameters.png)

#### 2] POST 方法

這個 **郵政** 方法允許管理員透過在 **請求正文** 而不是在 URL 中附加它們 。 在需要大量資料、認證引數、信使、信使或複雜有效載荷結構的情況下,建議對API整合採用這種方法。

使用POST方法提供以下優點:

- 減少 URL 長度和複雜性 。
- 透過在URL中避免敏感資訊曝光來提高安全性.
- 支援結構化和大型有效載荷資料。
- 允許與高階API整合相容.
- 允許基於API要求的靈活請求正文格式化.

所配置的有效載荷在API執行期間被傳送到HTTP請求正文中.

##### 有效載荷型別

在選擇 POST 方法時,管理員可以使用下列有效載荷型別之一配置請求的有效載荷:

###### [POST格式資料]

此選項允許管理員按照標準配置請求的有效載荷 **鍵值引數** 格式,其中每個引數使用欄位名稱和相應的值分別定義。

這種有效載荷型別適用於接受下列條件的API:

- 窗體資料
- URL 編碼引數
- 簡單的結構化請求機構

!!! example
    ```
    Key        Value
    username   admin
    password   test123
    senderid   ABCDEF
    ```

**福利:**

- 易於配置和管理.
- 適合簡單的API整合.
- 允許動態引數對映.
- 簡化請求驗證和故障排除.

![POST Form Data Key-Value parameters](images/httpgw-07-post-form-data.png)

###### II) RAW 有效載荷

此選項允許管理員透過 **完整的請求正文** 直接作為原始內容,而不單獨定義單個鍵值引數。

RAW 有效載荷方法主要用於目標API要求時:

- JSON 有效載荷
- XML 有效載荷
- 純文字有效載荷
- 自定義結構資料

管理員可以按照目的地API的要求,直接貼上或配置完整的有效載荷內容.

**支援的 RAW 有效載荷格式 :** <span data-ph="0"></span>, (中文(簡體) ). <span data-ph="1"></span>, (中文(簡體) ). <span data-ph="2"></span>。 。 。 。

!!! example "JSON 有效載荷"
    ```json
    {
      "username": "admin",
      "password": "test123",
      "senderid": "ABCDEF"
    }
    ```

**福利:**

- 支援複雜而嵌入的有效載荷結構.
- 啟用與現代 REST API 的無縫整合.
- 為自定義 API 請求格式提供靈活性。
- 允許直接控制有效載荷結構和格式。

![RAW JSON payload editor](images/httpgw-08-raw-payload.png)

在 Power SMPP 中,管理員可以定義 **佔位符** 用於各種值,例如 <span data-ph="0"></span> 傳送者身份證明, <span data-ph="1"></span> 關於文字內容, <span data-ph="2"></span> 目的地,還有更多。 這樣管理員就可以為引數配置各種動態值. 此外,管理員可以更改引數型別,無論它是 **頁首** 或一個 **體質** 引數,同時配置值。

---

## 第4節:條件引數

第三節 **有條件引數**,該應用程式具有透過配置一個條件來改變任何已配置引數的值的特性。

![Conditional Parameters](images/httpgw-09-conditional-parameters.png)

有條件引數構建按照以下邏輯進行: 1.

> 若為 <span data-ph="0"></span> 與選定的 <span data-ph="1"></span> 與 <span data-ph="2"></span>,則 <span data-ph="3"></span> 將改為 <span data-ph="4"></span>。 。 。 。

| 外地 | 說明 |
|-------|-------------|
| **引數** | 適用條件的有效載荷清單的關鍵引數。 |
| **條件** | 要檢查的條件型別 。 |
| **當前引數值** | 條件中要比較的選定引數的值 。 |
| **待修改引數** | 有效載荷清單中的關鍵引數,如果滿足上述條件,其價值將改變。 |
| **修改引數值** | 如果條件得到滿足,則要分配給關鍵引數的新值 。 |

---

## 第5節:門戶屬性

**閘道器屬性配置** 允許管理員為HTTP閘道器的無縫操作配置由供應商支援的方法和響應型別.

| 財產 | 說明 |
|----------|-------------|
| **方法** | 指定向HTTP閘道器傳送請求的方法。 管理員可以配置供應商支援的方法: <span data-ph="0"></span>, (中文(簡體) ). <span data-ph="1"></span>,或 <span data-ph="2"></span>。 。 。 。 |
| **反應型別** | 從閘道器收到答覆的格式: <span data-ph="0"></span>, (中文(簡體) ). <span data-ph="1"></span>,或 <span data-ph="2"></span>。 。 。 。 |
| **停止損失價格** | 使用路由信件時用作閘道器的預設價格 **盲從**。 。 。 。 |
| **盲跑嗎?** | 即使沒有為國家和網路配置 Gateway 成本價格, 也允許對訊息進行路由 。 在這種情況下, **停止損失價格** 將被應用。 |
| **閘道器時區** | 在應用程式中配置供應商的執行時區,以確保 **交貨收據(DLR)** 更新時間記錄準確。 |
| **活動嗎?** | 切換以啟用或停用閘道器 。 |
| **閘道器開啟/ 關閉時間** | 閘道器的執行時間視窗 <span data-ph="0"></span> 格式。 |

![Gateway Properties — Method](images/httpgw-10-gateway-properties-method.png)

![Gateway Properties — Response Type](images/httpgw-11-gateway-properties-response.png)

---

## 第6節:反應屬性

這個 **響應屬性** 在應用程式中用於 **對映響應** 從閘道器供應商收到的報告,然後用於更新 **交貨收據(DLR)**。 。 。 。

以下是應用程式中可用的響應配置型別:

### 1] JSON 或 XML 資料

如果供應商支援響應型別為: **賈森** 或者說 **XML 資料**,反應配置可以設定如下欄位:

| 外地 | 說明 |
|-------|-------------|
| **錯誤程式碼欄位** | 回覆中錯誤程式碼所在的欄位. |
| **信件ID 欄位** | 響應中訊息ID所在的欄位. |
| **信件狀態欄位** | 響應中信件狀態所在的欄位 。 |
| **移動數字欄位** | 響應中包含移動編號的欄位. |

![Response Properties — JSON / XML](images/httpgw-12-response-properties-json.png)

### 2] 文字

如果供應商支援響應型別為: **文字**,管理員需要配置響應屬性下的額外引數:

| 外地 | 說明 |
|-------|-------------|
| **鍵值分割符** | 分隔器用於從響應中分離並識別金鑰值對. 此欄位僅用於TEXT響應型別. 例如,如果收到的答覆是: <span data-ph="0"></span>,那麼拆分器將是 <span data-ph="1"></span>。 。 。 。 |
| **財產分割器** | 分隔符用於在響應中分離出各種屬性. 此欄位也特指TEXT響應型別. |
| **錯誤程式碼欄位** | 表示回覆中錯誤程式碼所在的欄位。 |
| **信件ID 欄位** | 顯示回覆中訊息ID所在的欄位。 |
| **信件狀態欄位** | 顯示回覆中信件狀態所在的欄位。 |
| **移動數字欄位** | 曾從響應取出手機號碼. 管理員需要指定響應中包含移動號的欄位. |

![Response Properties — TEXT](images/httpgw-13-response-properties-text.png)

!!! note
 在響應配置中,管理員必須配置儲存上述欄位值的引數名稱.

!!! example
 考慮以下答覆:
    ```json
    { "data": [{
        "message_error_code": 0,
        "message_error_description": "Success",
        "mobile_number": "9174XXXXXXX",
        "message_id": "b349f1c2-5ae9-4076-867e-5fa15044b207"
    }]}
    ```
 在JSON的答覆中:

    - 這個 **錯誤程式碼欄位** 將包含引數名稱 <span data-ph="0"></span>。 。 。 。
    - 這個 **信件ID 欄位** 將包含引數名稱 <span data-ph="0"></span>。 。 。 。

當配置響應屬性時 **文字** 響應時,數值將相似。 此外,您需要具體說明以下內容:

- **鍵值分割符** - 在答覆中,價值為: <span data-ph="0"></span> 實值 <span data-ph="1"></span>。按鍵-Value Splitter是用於將按鍵與值相分離的分隔符,在此情況下是結號(<span data-ph="2"></span>) (中文(簡體) ). 所以,鍵 - value 分割器將是 <span data-ph="3"></span>。 。 。 。
- **財產分割器** 在反應中,引數如: <span data-ph="0"></span> 財務報告和審定財務報表 <span data-ph="1"></span> 由逗號分隔(<span data-ph="2"></span>) (中文(簡體) ). 因此,將這些引數分開的財產分割器將是: <span data-ph="3"></span>。 。 。 。

這種配置幫助繪製和從響應中提取出必要的欄位,無論響應型別是JSON,XML還是TEXT.

---

## 第7節:會議

這個 **第二屆會議** 表示連線次數, HTTP 閘道器的建議會話是 **1個**。 。 。 。

| 外地 | 建議價值 |
|-------|-------------------|
| **屆會次數** | <span data-ph="0"></span> |

![Session configuration](images/httpgw-14-session.png)

---

## 第8節:自動傳送信件

如果閘道器供應商不傳送 **交貨收據(DLR)**, HTTP 閘道器配置包括一個名為 **自動交付**。此特性允許管理員配置一個狀態,以便自動更新 DLR 。

| 外地 | 說明 |
|-------|-------------|
| **自動標記為交付嗎 ?** | 更新信件的傳送狀態, 即使沒有從閘道器供應商收到 DLR 。 在這種情況下, **預設 DLR 狀態** 將被使用。 |
| **預設 DLR 狀態** | 如果自動送出功能被啟用,則指定給訊息的預設送出狀態. 當系統需要在閘道器上沒有DLR的情況下標出傳送的資訊時使用. 選項 : <span data-ph="0"></span>, (中文(簡體) ). <span data-ph="1"></span>, (中文(簡體) ). <span data-ph="2"></span>, (中文(簡體) ). <span data-ph="3"></span>。 。 。 。 |

![Automatic Message Delivery](images/httpgw-15-automatic-delivery.png)

!!! info "對不發行 DLRs 的閘道器有用"
 只有當上遊供應商真正不返回德國航天中心時,才啟動自動交付。 否則,讓它停用,讓供應商真正的DLR驅動報告。
