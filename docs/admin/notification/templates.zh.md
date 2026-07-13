
# 电子邮件模板

## 关键特性

### 自动监测
- **电子文本Pro** 持续定期监测应用程序的关键参数。
- 在潜在问题升级前主动查明.

### 通过电子邮件发出警告
- 利益攸关方通过电子邮件通知收到提醒。
- 提前发出通知,使利益攸关方能够采取预防措施。

### 自定义模板管理
- 支持自定义的提醒模板 。
- 用户可以根据自己的要求管理和调整通知模板.

### 系统变量集成
- 自定义模板可以包括相关的系统变量.
- 通过动态更新的系统信息实现个性化通信.

---

## 使用准则

### 模板管理
- 自定义提醒模板,以适应特定的通信需要。
- 纳入动态和对上下文有敏感认识通知的相关系统变量。

### 利益攸关方的参与
- 确保为接收通知对相关利益攸关方进行配置。
- 验证电子邮件设置是否为无缝通信正确配置 。

---

## 福利
- 增强《公约》的可靠性和稳定性 **电子文本Pro** 应用。
- 提供积极主动的发现和警报机制。
- 定制的模板和系统变量能够进行个性化和内容化的交流。
- 帮助各组织克服潜在的挑战。

!!! note
 SMTP的细节对于管理员以及再销售账户来说都是强制性的,以触发电子邮件.

---

## 电子邮件模板管理

![Email Templates](images/template1.png)

---

## 通知事件和对应模板

### 总体报告失败
当汇总报告服务遇到未知失败时触发. 
![Aggregate Reporting Failure](images/template2.png)

### 核准通知
在发件人ID和模板请求的管理员批准后发送。 
![Approval Notification 1](images/template3.png) 
![Approval Notification 2](images/template4.png)

### 核准请求
当再销售者/用户启动发件人ID或模板批准请求时触发. 
![Approval Request Notification 1](images/template5.png) 
![Approval Request Notification 2](images/template6.png)

### 更改密码
当用户成功更改密码时发送 。 
![Change Password](images/template7.png)

### 信用通知
当用户可用余额低于信用门槛时发出警报。 
![Credit Notification](images/template8.png)

### 信贷转账
由用户或转售者在用户账户中添加余额后触发. 
![Credit Transfer](images/template9.png)

### 电子邮件邮箱
当 MO 电子邮件转发激活时, 当收到信件时发送 。 
![Email Post](images/template10.png)

### 埃斯梅黑名单
当一个ESME账户因垃圾邮件而被列入黑名单时会发出警报. 
![Esme Blacklist](images/template11.png)

### 失败的网关
当由于主网关中断而发生自动消息切换时触发. 
![Failover Gateway](images/template12.png)

### 忘记密码
当请求更改登录账户密码时发送 。 
![Forgot Password](images/template13.png)

### 黑名单网关
当一个 SMPP 供应商网关/ 路由在失败的绑定尝试后被列入黑名单时提醒 。 
![Gateway Blacklisted](images/template14.png)

### 网关价格过期
当检测到有过期速率的路径时触发 。 
![Gateway Price Expiry](images/template15.png)

### 工作不批准通知
当发送者ID或模板请求被管理员/销售者不批准时发送. 
![Job Disapproved Notification 1](images/template16.png) 
![Job Disapproved Notification 2](images/template17.png)

### 信件队列
当供应商网关队列违反阈限时触发. 
![Message Queue](images/template18.png)

### 由管理员创建的新账户
当行政部门添加或签名时发送。 
![New Account by Admin](images/template19.png)

### Reseller 新建账户
当再销售者添加了新用户或新用户签名后发送到再销售用户. 
![New Account by Reseller](images/template20.png)

### 新建用户电子邮件验证
触发新用户报名电子邮件验证 。 
![New User Email Verification](images/template21.png)

### 检察官办公室
在用户登录时发送检察官办公室核查。 
![OTP](images/template22.png)

### 服务状况
当恶魔/服务自动恢复时发出警报.

### 服务已停止
当恶魔/服务被故意停止时触发. 
![Service Stopped](images/template23.png)

### 垃圾邮件检测
当发现SPAM内容时发出警报. 
![Spam Detection](images/template24.png)

### 用户销售更新
客户销售价格由母账户更新后发送. 
![User Selling Update](images/template25.png)

---

这些通知涵盖广泛的活动,提供了全面的见解并及时发出警报,以确保有效监测和管理 **电子文本Pro** 平台。
