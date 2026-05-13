---
tags:
  - HTTP
  - DLR
  - Handler
  - Configuration
---

# HTTP DLR Handler Configuration

Once the HTTP Gateway has been configured over the application the user will be able to send messages and the response will be updated on the application.

!!! note
    The **Gateway Response** is only the **1st response** which indicates whether the messages have been submitted to the vendor successfully or not.

To receive the **DLR (Delivery Receipt)** from the vendor, the admin needs to configure an **HTTP DLR Handler** so that whenever the vendor sends the DLR, the DLR will be updated over the application using the DLR handler.

In this document, we will share all the steps and configuration which need to be done by the admin in order to receive the DLR correctly over the application.

---

## Navigation

`Configuration` ➔ `Gateway Configuration` ➔ `HTTP DLR Handlers` ➔ `Add New Handler`.

---

## Sample DLR Payload

To configure the HTTP DLR Handler, we would require the **DLR response format** or a sample DLR from the vendor so that the admin can complete the configuration over the application.

For example, we will use the below DLR sample for HTTP DLR Handler Configuration:

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

## Configuration Steps

Follow the below steps to configure the DLR handler for the above provided DLR sample:

1. **Add a User Friendly Name** for the handler.
2. **Whitelist the vendor's IP** *(Not Mandatory)*.
3. **Select the supported method** by the vendor — `GET` or `POST`.
4. **Configure Payloads** — Under the payloads, the client needs to configure the parameter name which stores the specific values.

### Field Mapping Reference

| Application Field | Maps to JSON Key | Example Value |
|-------------------|------------------|---------------|
| **MessageId** | `messageId` | `161a9168-623c-4411-9e30-cf69353f9bef` |
| **Message Status** | `status` | `EXPIRED` |
| **Done Date** | `doneDate` | `2024-05-22 11:07:46` |
| **Error Code** | `errorCode` | `1039` |
| **Mobile Number** | `mobile` | `91123537072` |
| **Sender ID** | *(optional, map if vendor sends it)* | — |
| **Message** | `shortMessage` | `Test Message` |

!!! tip
    In the example above, the parameter `status` stores the value of DLR status and `errorCode` stores the value of Error code. These parameters need to be configured as it is in **Message Status** and **Error Code** respectively. Apply the same logic for all other parameters shared by the vendor.

---

## Local Endpoint

When the handler is saved, Power SMPP generates a **Local Endpoint** URL (for example, `https://user01.smslane.com/api/dlr/3jfs9rnmdt`). This is the URL the vendor will call back with DLR payloads.

!!! warning "Important"
    Once all the details have been configured over the application, **save it and please reach out to your gateway vendor and ask them to whitelist the Endpoint of the DLR handler at their end**.

---

## Default Values

For the **Message Status** and **Error Code** fields, an optional `Default value (if any)` can be configured. The default value is applied when the vendor does not return that field in a particular DLR. This ensures the DLR record is still complete and the message is closed out in reports.

---

## Verification

After configuring the DLR handler:

1. Send a test message through the corresponding HTTP Gateway.
2. Ask the vendor (or use a test tool such as `curl` / `Postman`) to send a sample DLR payload to the Local Endpoint URL.
3. Open the relevant **DLR Report** in `Reporting` to confirm that the DLR has been received and parsed correctly.

If the DLR does not appear, re-check the parameter name mappings — the most common cause is a mismatch between the JSON key the vendor sends and the key configured in the handler.
