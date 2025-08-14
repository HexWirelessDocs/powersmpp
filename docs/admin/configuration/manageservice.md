## Manage Services

The **Manage Services** section in iTextPRO provides visibility into the various **background and foreground services** that drive the core functionalities of the platform. This interface is primarily intended for expert users or administrators.

> ⚠️ **Caution:** While it is possible to stop or start a service from the web interface, this should be done **with extreme caution**, particularly during peak load times, as it may result in **data loss** or **service disruption**.

---

### Service Overview

Below is a brief description of each service visible in the **Manage Services** section:

| **Service Name**         | **Description**                                                                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Client Service**       | Connects iTextPRO with your SMSC via SMPP for managing **SMS MT (Mobile Terminated)** and **SMS MO (Mobile Originated)** traffic.                      |
| **DLR Service**          | Handles real-time **Delivery Reports (DLRs)** and updates message status within the system for accurate reporting.                                      |
| **SMPP Server Service**  | Listens for inbound SMPP traffic from **ESME users** on a pre-defined port, allowing external users to submit SMS.                                      |
| **File Pickup Service**  | Reads campaign message files uploaded by users and forwards them to the **gateway queue** for processing.                                               |
| **Validator Service**    | Validates **binding parameters** for users connecting through API and SMPP interfaces, ensuring traffic is accepted only from authorized clients.       |
| **Data Builder Service** | Manages the storage of **PDU logs** and **message logs** into the database for logging and debugging purposes.                                          |
| **Report Builder Service** | Profiles and compiles **sent counts and summary reports** for users, aiding in usage tracking and billing.                                            |
| **Download Report Service** | Processes and generates **downloadable reports** for both admins and users based on requested data.                                                  |
| **Notification Service** | Sends **Email alert notifications** to users and admins and actively monitors **gateway health status**.                                               |

---

### Key Features

- ✅ View the **current status** of each service.
- 🔁 Option to **Start** or **Stop** services from the web interface.
- 🛠️ Designed for use by **advanced users or administrators** with a strong understanding of service dependencies.
- 💡 Each service includes metadata such as the **application version**.

---

### Best Practices

- Always confirm peak traffic hours before stopping any critical service (e.g., Client, DLR, Validator).
- Avoid restarting services without consulting system logs or technical support.
- Ensure database and gateway services are in sync to prevent data inconsistencies.

---

The **Manage Services** feature offers a centralized way to monitor and control system-level processes, ensuring smooth operations within the iTextPRO environment.
