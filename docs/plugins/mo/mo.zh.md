
# 毛泽东

## 定义
MO 消息 (**移动来源** )由移动电话用户发起,并使用特定关键词发送到专用的短码或长码. 
它们允许客户或订户与供应商或应用程序直接互动。

---

## 进程

### 用户启动
客户向专用短码或长码发送带有特定关键词的短信.

**示例** 
<span data-ph="0"></span> → <span data-ph="1"></span>

### 消息运行
电文被传送到与该短码或号码相链接的应用程序或供应商.

---

## 关键点
- 实现用户与供应商双向通信.
- 使用特定关键词来触发响应.
- 通过专用短码或长码工作.

---

## HTTP MO 处理器配置

### 概览
HTTP MO 处理器在 **电子文本Pro** 收到供应商寄来的MO消息。 
有效载荷结构因供应商而异。

### 步骤1: 添加新处理器
1. 点击 **添加新处理器**。 。 。 。
2. 在UI中映射有效载荷参数.

![MO Handler Config](images/mo1.png)

**先决条件:** 
对RESTFL API的基本理解.

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
- 内容类型 : <span data-ph="0"></span>
- 发件人密钥 : <span data-ph="0"></span>
- 目标密钥 : <span data-ph="0"></span>
- 信件密钥 : <span data-ph="0"></span>

![MO Config 2](images/mo2.png)

---

### 第2步:为用户账户配置MO服务
1. 登录到 iTextPro 找到用户账户 。
2. 启动 **MO 服务** 内 **管理服务**。 。 。 。
3. 设定 MO 编号关键词( K) :
   - 结束日期
   - 选择频道( MO 号码)
   - 关键词(或 <span data-ph="0"></span> 成员名单)
   - 状态: 活动
4. 点击 **添加**。 。 。 。

![MO Config 3](images/mo3.png) 
![MO Config 4](images/mo4.png)

---

### 第3步:MO 运行规则配置
1. 转到 **MO 运行规则**。 。 。 。
2. 创建或编辑一条规则 :
   - 规则名称、开始/结束日期
   - 网关接口:HTTP/SMPP
   - 条件: 发件人、 目的地、 信件
   - 用户端点( E) : HTTP Webhook 或 ESME

![MO Routing](images/mo5.png) 
![MO Routing UI](images/mo6.png) 
![MO Routing Rule](images/mo7.png)

---

## MO 模块访问
1. 假名/ Login 到用户账户 。
2. 打开 **MO 模块** 以查看MO消息。

![MO Inbox](images/mo8.png) 
![MO Keyword](images/mo9.png) 
![MO Keyword Details](images/mo10.png)

---

## 自动回复
- 设置 MO 消息的自动回复 。

![MO Auto Reply](images/mo11.png)

---

## 通知
- **电子邮件转发** – 通过电子邮件接收MO提醒. 
- **移动转发** - 通过短信接收警报(包括国家代码)。

![MO Mobile Notify](images/mo12.png)

---

## 管理子关键字
子关键词是主关键词后起的次要触发.

**示例**
- **主要关键词:** 中非共和国 
- **自动响应 :** 
 <span data-ph="0"></span>
- **子关键词 1:** 对 <span data-ph="0"></span> 
- **分关键词2:** 没有 □ <span data-ph="0"></span>

![MO Sub-keyword](images/mo13.png)

---

## 报告
- 导出MO报告给Excel.
- 由关键词或子关键词过滤.

**步骤 :**
1. 转到 **报告**。 。 。 。
2. 点击 **导出报告**。 。 。 。
3. 下载和定制 。

![MO Reports](images/mo14.png) 
![MO Reports 2](images/mo15.png)

---

## MO 网络呼号
实时 MO 消息发送到给定的 HTTP 端点.

**设置 :**
1. 启用 **HTTP 网络推** 在父账户中。
2. 转到 **MO 网络呼号** → **添加新 Webhook 选项**。 。 。 。
3. 设定 :
   - 名称
   - 端点 URL
   - 方法:获取/部署
   - 处理器:MO

**说明:** 
如果端点无法到达,MO会被丢弃. 暂停10秒。

![MO Webhook](images/mo16.png) 
![MO Webhook Config](images/mo17.png)