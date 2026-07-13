---
tags:
  - HTTP
  - DLR
  - Handler
  - Configuration
---

# HTTP DLR 处理器配置

HTTP 网关在应用程序上配置完毕后,用户就可以发送消息,并在应用程序上更新响应.

!!! note
 这个 **网关响应** 仅仅是 **第一次答复** 说明电文是否已成功提交供应商。

接收 **DLR( 交货收据)** 从供应商,管理员需要配置 **HTTP DLR 处理器** 这样,每当供应商发送DLR时,DLR将使用DLR处理器更新应用程序.

在本文件中,我们将分享为了正确接收DLR的应用程序而需要行政部门完成的所有步骤和配置.

![Manage HTTP DLR Handler list](images/dlrhandler-01-list.png)

---

## 导航

<span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span> ➔ <span data-ph="3"></span>。 。 。 。

![Add New Handler form with Method selector](images/dlrhandler-02-add-new.png)

---

## 样本 DLR 有效载荷

要配置 HTTP DLR 处理器,我们需要 **DLR 响应格式** 或来自供应商的 DLR 样本,以便管理员能够完成应用程序上的配置。

例如,我们将使用以下 DLR 样本用于 HTTP DLR 处理器配置 :

```json
{
    "messageId": "161a9168-623c-4411-9e30-cf69353f9bef",
    "status": "EXPIRED",
    "errorCode": "1039",
    "mobile": "91123537072",
    "shortMessage": "Test Message",
    "doneDate": "2024-05-22 11:07:46"
}
```

---

## 配置步骤

遵循以下步骤配置上述提供的 DLR 样本的 DLR 处理器:

1. **添加方便用户的名称** 给处理者。
2. **将销售商的IP白名单** *(非强制性)*。 。 。 。
3. **选择所支持的方法** 由供应商进行—— <span data-ph="0"></span> 或者说 <span data-ph="1"></span>。 。 。 。
4. **配置有效载荷** ——在有效载荷下,客户端需要配置存储特定值的参数名称.

### 实地绘图参考文献

| 应用程序字段 | JSON 密钥地图 | 示例数值 |
|-------------------|------------------|---------------|
| **信件编号** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **信件状态** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **完成日期** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **错误代码** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **移动号码** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **发件人标识** | *(可选的,如果供应商发送地图)* | —— 说 |
| **消息** | <span data-ph="0"></span> | <span data-ph="0"></span> |

!!! tip
 在上述例子中,参数 <span data-ph="0"></span> 存储 DLR 状态的值,并 <span data-ph="1"></span> 存储错误代码的值。 这些参数需要配置,如在 **信件状态** 财务报告和审定财务报表 **错误代码** 页:1 对供应商共用的所有其他参数适用同样的逻辑。

![Handler configured with payload mapping](images/dlrhandler-03-configured.png)

---

## 本地终点

当处理器被保存时, Power SMPP 生成一个 **本地终点** URL(例如, <span data-ph="0"></span>) (中文(简体) ). 这是销售商用 DLR 有效载荷调回的 URL 。

!!! warning "重要"
 一旦所有的细节 配置在应用程序上, **请保存它,请联系您的网关供应商, 并让他们将 DLR 处理器的端点白化**。 。 。 。

---

## 默认值

给 **信件状态** 财务报告和审定财务报表 **错误代码** 字段,可选 <span data-ph="0"></span> 可配置。 如果供应商不返回某一德国航天中心中的该字段,则适用默认值。 这保证了DLR记录仍然完整,并且信件在报告中被关闭.

---

## 核查

在配置 DLR 处理器后 :

1. 通过相应的HTTP Gateway发送测试消息.
2. 询问供应商(或使用测试工具,例如 <span data-ph="0"></span> 编号 : <span data-ph="1"></span>)将DLR有效载荷样本发送到本地端点URL.
3. 打开相关的 **德国航天中心报告** 内 <span data-ph="0"></span> 以确认德国航天中心已收到并正确分析。

如果 DLR 不出现,则重新检查参数名称映射——最常见的原因是供应商发送的JSON密钥和处理器中配置的密钥不匹配.
