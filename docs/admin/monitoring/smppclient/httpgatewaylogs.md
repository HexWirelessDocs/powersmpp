---
tags:
  - Monitoring
  - HTTP
  - Gateway
  - Logs
---

# HTTP Gateway Logs

**Navigation:** `Monitoring` ➔ `SMPP Client` ➔ `HTTP Gateway Logs`.

## Overview

The **HTTP Gateway Logs** section allows administrators to view the complete HTTP **request** and **response** communication exchanged between the PowerSMPP application and configured gateway vendors. These logs are essential for diagnosing delivery failures, verifying API payloads, and auditing gateway interactions.

---

## Steps to View Logs

1. Select the **HTTP Gateway** from the **Gateway Name** dropdown.
2. Select the required **Date Range** using the date picker.
3. Choose the **Log Type** (`All` / `Info` / `Error`) as needed.
4. Select the **Verbosity** level if granular filtering is required.
5. Click **Submit** to fetch and display the matching logs.

![HTTP Gateway Logs — Log list view](images/httplogs-01-list.png)

---

## Available Log Sections

### Request Body

The **Request Body** contains the complete payload transmitted from the PowerSMPP application to the gateway vendor.

![HTTP Gateway Logs — Request Body expanded](images/httplogs-02-request-body.png)

!!! info "Request Body — Included Data"
    - **Mobile Number** — destination number of the SMS
    - **Sender ID** — the originating address / Sender ID used
    - **Request Parameters** — full API parameters sent to the gateway
    - **Host / IP Details** — IP address and port of the gateway endpoint
    - **Submission Time** — timestamp of when the request was dispatched

### Response Body

The **Response Body** contains the acknowledgement and status data received back from the gateway vendor.

![HTTP Gateway Logs — Response Body expanded](images/httplogs-03-response-body.png)

!!! info "Response Body — Included Data"
    - **Gateway Response** — raw response returned by the gateway
    - **Status Information** — delivery or acceptance status codes
    - **Error Details** — error codes and descriptions for failed submissions
    - **Response Acknowledgement** — confirmation that the gateway processed the request

---

## Filter Options

Administrators can refine the log view using the following additional filters:

| Filter | Use |
|--------|-----|
| **IP Address** | Filter logs by the gateway server IP. |
| **Sender ID** | Filter logs by originating Sender ID. |
| **Mobile Number** | Filter logs by destination mobile number. |

---

## Typical Troubleshooting Flow

1. A campaign reports unexpected failures or undelivered messages.
2. Open **HTTP Gateway Logs**, select the affected gateway and a date range that covers the issue.
3. Set **Log Type** to `Error` to surface only failed exchanges.
4. Expand the **Request Body** to confirm the outbound payload was correct.
5. Expand the **Response Body** to read the actual error code/description returned by the vendor.
6. Use **IP Address**, **Sender ID**, or **Mobile Number** filters to isolate a specific test sample for the vendor's support team.
