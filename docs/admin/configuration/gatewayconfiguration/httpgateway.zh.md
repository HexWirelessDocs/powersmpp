---
tags:
  - HTTP
  - Gateway
  - Configuration
---

# HTTP 网关

单位 **电源 SMPP**我们两个都支持 **SMPP 软件** 财务报告和审定财务报表 **HTTP 密码** 供应商连通协议。 因此,管理员可以选择配置基于 SMPP 的网关或 HTTP 网关 。 该文件提供了HTTP网关配置的简明概览. 它旨在帮助管理员理解并轻松地在Power SMPP应用程序内设置了HTTP网关.

如名称所示,HTTP网关基于 **超文本传输协议( HTTP)**。此协议允许客户端通过一个作为Power SMPP应用程序内网关的API发送消息.

![Manage Gateway list view](images/httpgw-01-manage-gateway.png)

**导航 :** <span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span> ➔ <span data-ph="3"></span> ➔ <span data-ph="4"></span>。 。 。 。

![HTTP Gateway Detail sections](images/httpgw-02-detail-sections.png)

!!! tip "查看文档"
 点击时 **添加新内容**,第一个选项是 **查看文档**。我们建议管理员审查该文件,以便熟悉网关配置中提及的术语。

HTTP Gateway 详细屏幕分为以下几节:

- 所需全权证书
- 信件类型
- 参数
- 有条件参数
- 网关属性
- 响应属性
- 会议
- 自动发送信件

---

## 第1节:必要的全权证书

本节需要各种资料,例如: **网关名称**, (中文(简体) ). **请求类型**, (中文(简体) ). **认证**, (中文(简体) ). **基础 URL**,以及 **UDH 软件**。 。 。 。

**网关名称** ——HTTP Gateway的易名.

**需要UDH吗?** - 指定是否为 **UDH (用户数据头)** 用于从此网关发送信件。 UDH用于收缩信件.

**请求类型** ——指定HTTP请求的类型。 这可能是 **简单 HTTP**, (中文(简体) ). **资源/JSON**,或 **SOPAP 软件**。不同的请求类型需要不同的配置。 一般情况下,简单的HTTP用于 <span data-ph="0"></span> 方法,而 REST/JSON 可用于两者 <span data-ph="1"></span> 财务报告和审定财务报表 <span data-ph="2"></span> 方法。 。 。

![Required Credentials form](images/httpgw-03-required-credentials.png)

**基础 URL 细节** 指定 HTTP API 的基础 URL, **不包括** 所有其他参数。

!!! example
 如果 API URL 是 <span data-ph="0"></span>,然后将 Base URL 配置为 <span data-ph="1"></span>。 。 。 。

**认证** - Power SMPP目前支持三种授权:

| {\fn方正粗倩简体\fs12\an8\1cHFFFF00\b0} | 类型 | 说明 |
|---|------|-------------|
| 1个 | **无授权** | 无需批准。 |
| 2个 | **基本认证** | API的安全认证需要用户名和密码. |
| 3个 | **OAuth 2.0 数据** | 最新版本的授权,用于在一段时间后重新生成新的证书,以保持API的高安全性。 **OAuth 处理器** API (英语). |

![Authentication options](images/httpgw-04-authentication.png)

---

## 第2节:信息类型

**信件类型** 是一个可选的段落,管理员可以在此配置供应商接受的数据编码值。 每个数据编码类型的默认值在括号中被提及.

| 类型 | 默认 | 目的 |
|------|---------|---------|
| **文本** | <span data-ph="0"></span> | 绘制纯文本消息的网关专用消息类型 。 |
| **联合国** | <span data-ph="0"></span> | 绘制Unicode消息的网关专用消息类型. |
| **比利时** | <span data-ph="0"></span> | 绘制二进制信件的网关专用消息类型 。 |
| **弗拉什语Name** | <span data-ph="0"></span> 或者说 <span data-ph="1"></span> | 绘制闪存消息的网关专用消息类型 。 |

!!! note
 以系统消息类型映射您的网关特定消息类型 。 如果不适用,请将字段留空。

![Message Types form](images/httpgw-05-message-types.png)

---

## 第3节:参数

这个 **参数** 区域允许管理员配置网关细节并请求网关供应商提供的参数。 这些参数被Power SMPP用于构建并传送API请求的数据/体给相应的网关供应商进行消息处理和发送.

所配置的参数定义了HTTP请求如何在API通信中生成和执行.

### 方法

Power SMPP支持下列HTTP方法用于API执行:

#### 1] 获取方法

GET 方法允许管理员在 **键值对** 格式。 API 执行期间,所有配置的参数直接被附加到 URL 上作为 **查询参数**。 。 。 。

这种方法一般用于:

- 简单的 API 请求
- 基于 URL 的参数传输
- 轻量级 API 整合
- 遗产 HTTP 集成

!!! example
 <span data-ph="0"></span>

在GET方法中,Power SMPP支持以下参数类型:

##### 父名称

这个 **父名称** 字段主要用于 **基于 SOAP** API集成,其中需要将参数组合到父 XML 节点或请求对象下.

这种配置有助于按照供应商API的规格生成结构化的SOAP请求有效载荷.

!!! example
    ```xml
    <SendSMS>
        <username>admin</username>
        <password>test123</password>
    </SendSMS>
    ```
 在上述例子中, <span data-ph="0"></span> 作为父母姓名。

##### 页眉参数

这个 **页眉参数** 区域用于配置 API 执行过程中所需的 HTTP 头值。

这些参数一般用于:

- 身份验证
- API 密钥
- 全权证书
- 内容 - 类型定义
- 自定义供应商信头

!!! example
    ```
    Authorization: Bearer xxxxx
    Content-Type: application/json
    ```

标题参数在API通信期间在HTTP请求标题内传输.

##### 参数

这个 **参数** 区域包含 HTTP API 请求所需的所有一般请求参数。

这些参数通常包括:

- 移动号码
- 信件内容
- 发件人标识
- 模板 ID
- 实体标识
- 运行参数
- 自定义供应商参数

对于 **获取** 请求,这些参数在请求 URL 中作为查询参数在 API 执行过程中附加.

![Parameters configuration with example rows](images/httpgw-06-parameters.png)

#### 2] POST 方法

这个 **邮政** 方法允许管理员通过在 **请求正文** 而不是在 URL 中附加它们 。 在需要大量数据、认证参数、信使、信使或复杂有效载荷结构的情况下,建议对API集成采用这种方法。

使用POST方法提供以下优点:

- 减少 URL 长度和复杂性 。
- 通过在URL中避免敏感信息曝光来提高安全性.
- 支持结构化和大型有效载荷数据。
- 允许与高级API集成兼容.
- 允许基于API要求的灵活请求正文格式化.

所配置的有效载荷在API执行期间被传送到HTTP请求正文中.

##### 有效载荷类型

在选择 POST 方法时,管理员可以使用下列有效载荷类型之一配置请求的有效载荷:

###### [POST格式数据]

此选项允许管理员按照标准配置请求的有效载荷 **键值参数** 格式,其中每个参数使用字段名称和相应的值分别定义。

这种有效载荷类型适用于接受下列条件的API:

- 窗体数据
- URL 编码参数
- 简单的结构化请求机构

!!! example
    ```
    Key        Value
    username   admin
    password   test123
    senderid   ABCDEF
    ```

**福利:**

- 易于配置和管理.
- 适合简单的API集成.
- 允许动态参数映射.
- 简化请求验证和故障排除.

![POST Form Data Key-Value parameters](images/httpgw-07-post-form-data.png)

###### II) RAW 有效载荷

此选项允许管理员通过 **完整的请求正文** 直接作为原始内容,而不单独定义单个键值参数。

RAW 有效载荷方法主要用于目标API要求时:

- JSON 有效载荷
- XML 有效载荷
- 纯文本有效载荷
- 自定义结构数据

管理员可以按照目的地API的要求,直接粘贴或配置完整的有效载荷内容.

**支持的 RAW 有效载荷格式 :** <span data-ph="0"></span>, (中文(简体) ). <span data-ph="1"></span>, (中文(简体) ). <span data-ph="2"></span>。 。 。 。

!!! example "JSON 有效载荷"
    ```json
    {
      "username": "admin",
      "password": "test123",
      "senderid": "ABCDEF"
    }
    ```

**福利:**

- 支持复杂而嵌入的有效载荷结构.
- 启用与现代 REST API 的无缝集成.
- 为自定义 API 请求格式提供灵活性。
- 允许直接控制有效载荷结构和格式。

![RAW JSON payload editor](images/httpgw-08-raw-payload.png)

在 Power SMPP 中,管理员可以定义 **占位符** 用于各种值,例如 <span data-ph="0"></span> 发送者身份证明, <span data-ph="1"></span> 关于文本内容, <span data-ph="2"></span> 目的地,还有更多。 这样管理员就可以为参数配置各种动态值. 此外,管理员可以更改参数类型,无论它是 **页眉** 或一个 **体质** 参数,同时配置值。

---

## 第4节:条件参数

第三节 **有条件参数**,该应用程序具有通过配置一个条件来改变任何已配置参数的值的特性。

![Conditional Parameters](images/httpgw-09-conditional-parameters.png)

有条件参数构建按照以下逻辑进行: 1.

> 若为 <span data-ph="0"></span> 与选定的 <span data-ph="1"></span> 与 <span data-ph="2"></span>,则 <span data-ph="3"></span> 将改为 <span data-ph="4"></span>。 。 。 。

| 外地 | 说明 |
|-------|-------------|
| **参数** | 适用条件的有效载荷清单的关键参数。 |
| **条件** | 要检查的条件类型 。 |
| **当前参数值** | 条件中要比较的选定参数的值 。 |
| **待修改参数** | 有效载荷清单中的关键参数,如果满足上述条件,其价值将改变。 |
| **修改参数值** | 如果条件得到满足,则要分配给关键参数的新值 。 |

---

## 第5节:门户属性

**网关属性配置** 允许管理员为HTTP网关的无缝操作配置由供应商支持的方法和响应类型.

| 财产 | 说明 |
|----------|-------------|
| **方法** | 指定向HTTP网关发送请求的方法。 管理员可以配置供应商支持的方法: <span data-ph="0"></span>, (中文(简体) ). <span data-ph="1"></span>,或 <span data-ph="2"></span>。 。 。 。 |
| **反应类型** | 从网关收到答复的格式: <span data-ph="0"></span>, (中文(简体) ). <span data-ph="1"></span>,或 <span data-ph="2"></span>。 。 。 。 |
| **停止损失价格** | 使用路由信件时用作网关的默认价格 **盲从**。 。 。 。 |
| **盲跑吗?** | 即使没有为国家和网络配置 Gateway 成本价格, 也允许对消息进行路由 。 在这种情况下, **停止损失价格** 将被应用。 |
| **网关时区** | 在应用程序中配置供应商的运行时区,以确保 **交货收据(DLR)** 更新时间记录准确。 |
| **活动吗?** | 切换以启用或禁用网关 。 |
| **网关打开/ 关闭时间** | 网关的运行时间窗口 <span data-ph="0"></span> 格式。 |

![Gateway Properties — Method](images/httpgw-10-gateway-properties-method.png)

![Gateway Properties — Response Type](images/httpgw-11-gateway-properties-response.png)

---

## 第6节:反应属性

这个 **响应属性** 在应用程序中用于 **映射响应** 从网关供应商收到的报告,然后用于更新 **交货收据(DLR)**。 。 。 。

以下是应用程序中可用的响应配置类型:

### 1] JSON 或 XML 数据

如果供应商支持响应类型为: **贾森** 或者说 **XML 数据**,反应配置可以设置如下字段:

| 外地 | 说明 |
|-------|-------------|
| **错误代码字段** | 回复中错误代码所在的字段. |
| **信件ID 字段** | 响应中消息ID所在的字段. |
| **信件状态字段** | 响应中信件状态所在的字段 。 |
| **移动数字字段** | 响应中包含移动编号的字段. |

![Response Properties — JSON / XML](images/httpgw-12-response-properties-json.png)

### 2] 文本

如果供应商支持响应类型为: **文本**,管理员需要配置响应属性下的额外参数:

| 外地 | 说明 |
|-------|-------------|
| **键值分割符** | 分隔器用于从响应中分离并识别密钥值对. 此字段仅用于TEXT响应类型. 例如,如果收到的答复是: <span data-ph="0"></span>,那么拆分器将是 <span data-ph="1"></span>。 。 。 。 |
| **财产分割器** | 分隔符用于在响应中分离出各种属性. 此字段也特指TEXT响应类型. |
| **错误代码字段** | 表示回复中错误代码所在的字段。 |
| **信件ID 字段** | 显示回复中消息ID所在的字段。 |
| **信件状态字段** | 显示回复中信件状态所在的字段。 |
| **移动数字字段** | 曾从响应取出手机号码. 管理员需要指定响应中包含移动号的字段. |

![Response Properties — TEXT](images/httpgw-13-response-properties-text.png)

!!! note
 在响应配置中,管理员必须配置存储上述字段值的参数名称.

!!! example
 考虑以下答复:
    ```json
    { "data": [{
        "message_error_code": 0,
        "message_error_description": "Success",
        "mobile_number": "9174XXXXXXX",
        "message_id": "b349f1c2-5ae9-4076-867e-5fa15044b207"
    }]}
    ```
 在JSON的答复中:

    - 这个 **错误代码字段** 将包含参数名称 <span data-ph="0"></span>。 。 。 。
    - 这个 **信件ID 字段** 将包含参数名称 <span data-ph="0"></span>。 。 。 。

当配置响应属性时 **文本** 响应时,数值将相似。 此外,您需要具体说明以下内容:

- **键值分割符** - 在答复中,价值为: <span data-ph="0"></span> 实值 <span data-ph="1"></span>。按键-Value Splitter是用于将按键与值相分离的分隔符,在此情况下是结号(<span data-ph="2"></span>) (中文(简体) ). 所以,键 - value 分割器将是 <span data-ph="3"></span>。 。 。 。
- **财产分割器** 在反应中,参数如: <span data-ph="0"></span> 财务报告和审定财务报表 <span data-ph="1"></span> 由逗号分隔(<span data-ph="2"></span>) (中文(简体) ). 因此,将这些参数分开的财产分割器将是: <span data-ph="3"></span>。 。 。 。

这种配置帮助绘制和从响应中提取出必要的字段,无论响应类型是JSON,XML还是TEXT.

---

## 第7节:会议

这个 **第二届会议** 表示连接次数, HTTP 网关的建议会话是 **1个**。 。 。 。

| 外地 | 建议价值 |
|-------|-------------------|
| **届会次数** | <span data-ph="0"></span> |

![Session configuration](images/httpgw-14-session.png)

---

## 第8节:自动发送信件

如果网关供应商不发送 **交货收据(DLR)**, HTTP 网关配置包括一个名为 **自动交付**。此特性允许管理员配置一个状态,以便自动更新 DLR 。

| 外地 | 说明 |
|-------|-------------|
| **自动标记为交付吗 ?** | 更新信件的发送状态, 即使没有从网关供应商收到 DLR 。 在这种情况下, **默认 DLR 状态** 将被使用。 |
| **默认 DLR 状态** | 如果自动送出功能被激活,则指定给消息的默认送出状态. 当系统需要在网关上没有DLR的情况下标出发送的信息时使用. 选项 : <span data-ph="0"></span>, (中文(简体) ). <span data-ph="1"></span>, (中文(简体) ). <span data-ph="2"></span>, (中文(简体) ). <span data-ph="3"></span>。 。 。 。 |

![Automatic Message Delivery](images/httpgw-15-automatic-delivery.png)

!!! info "对不发行 DLRs 的网关有用"
 只有当上游供应商真正不返回德国航天中心时,才启动自动交付。 否则,让它停用,让供应商真正的DLR驱动报告。
