# Email Templates

## Key Features

### Automated Monitoring
- **iTextPro** continuously monitors critical parameters of the application at regular intervals.
- Proactive identification of potential issues before they escalate.

### Alerts via Email
- Stakeholders receive alerts through email notifications.
- Notifications are sent in advance, allowing stakeholders to take preventive measures.

### Custom Template Management
- Supports customizable alert templates.
- Users can manage and tailor notification templates according to their requirements.

### System Variables Integration
- Custom templates can include relevant system variables.
- Personalized communication through dynamically updated system information.

---

## Usage Guidelines

### Template Management
- Customize alert templates to suit specific communication needs.
- Incorporate relevant system variables for dynamic and context-aware notifications.

### Stakeholder Engagement
- Ensure that concerned stakeholders are configured to receive notifications.
- Verify that email settings are correctly configured for seamless communication.

---

## Benefits
- Enhances the reliability and stability of the **iTextPro** application.
- Provides a proactive mechanism for issue detection and alerting.
- Customizable templates and system variables enable personalized and informative communication.
- Helps organizations stay ahead of potential challenges.

> **Note:** SMTP details are mandatory for Admin as well as for reseller accounts to trigger emails.

---

## Email Template Management

![Email Templates](images/template1.png)

---

## Notification Events and Corresponding Templates

### Aggregate Reporting Failure
Triggered when the aggregate reporting service encounters an unknown failure.  
![Aggregate Reporting Failure](images/template2.png)

### Approval Notification
Sent upon admin approval of Sender ID and template requests.  
![Approval Notification 1](images/template3.png)  
![Approval Notification 2](images/template4.png)

### Approval Request Notification
Triggered when a reseller/user initiates a Sender ID or template approval request.  
![Approval Request Notification 1](images/template5.png)  
![Approval Request Notification 2](images/template6.png)

### Change Password
Sent when a user successfully changes their password.  
![Change Password](images/template7.png)

### Credit Notification
Alerted when a user's available balance falls below the credit threshold.  
![Credit Notification](images/template8.png)

### Credit Transfer
Triggered upon the addition of balance to a user account by the user or resellers.  
![Credit Transfer](images/template9.png)

### Email Post
Sent upon receiving an incoming message (MO) when MO email forwarding is active.  
![Email Post](images/template10.png)

### Esme Blacklist
Alerted when an ESME account is blacklisted due to spamming.  
![Esme Blacklist](images/template11.png)

### Failover Gateway
Triggered when automatic message switching occurs due to a primary gateway outage.  
![Failover Gateway](images/template12.png)

### Forgot Password
Sent when there is a request to change the login account password.  
![Forgot Password](images/template13.png)

### Gateway Blacklisted
Alerted when an SMPP vendor gateway/route is blacklisted after failed bind attempts.  
![Gateway Blacklisted](images/template14.png)

### Gateway Price Expiry
Triggered when a route with an expired rate is detected.  
![Gateway Price Expiry](images/template15.png)

### Job Disapproved Notification
Sent when a sender ID or template request is disapproved by the admin/reseller.  
![Job Disapproved Notification 1](images/template16.png)  
![Job Disapproved Notification 2](images/template17.png)

### Message Queue
Triggered when the vendor gateway queue breaches the threshold limit.  
![Message Queue](images/template18.png)

### New Account by Admin
Sent when a new user is added from administration or signs up.  
![New Account by Admin](images/template19.png)

### New Account by Reseller
Sent to reseller users when a reseller adds a new user or a new user signs up.  
![New Account by Reseller](images/template20.png)

### New User Email Verification
Triggered for new users signing up for email verification.  
![New User Email Verification](images/template21.png)

### OTP
Sent for OTP verification during user logins.  
![OTP](images/template22.png)

### Service Status
Alerted when a demon/service is automatically recovered.

### Service Stopped
Triggered when a demon/service is intentionally stopped.  
![Service Stopped](images/template23.png)

### Spam Detection
Alerted when SPAM content is detected.  
![Spam Detection](images/template24.png)

### User Selling Update
Sent when the customer selling price is updated by the parent account.  
![User Selling Update](images/template25.png)

---

These notifications cover a wide range of events, providing comprehensive insights and timely alerts to ensure efficient monitoring and management of the **iTextPro** platform.
