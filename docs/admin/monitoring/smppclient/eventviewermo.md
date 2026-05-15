---
tags:
  - Monitoring
  - MO
  - Event Viewer
---

# Event Viewer (MO) — Mobile Originated

**Navigation:** `Monitoring` ➔ `SMPP Client` ➔ `Event Viewer (MO)`.

## Overview

The **Event Viewer (MO)** section is used to monitor **Mobile Originated (MO)** messages and related system events within PowerSMPP. MO messages are inbound messages received from a gateway vendor or end user directed towards the application.

---

## Purpose

The Event Viewer (MO) helps administrators monitor, audit, and troubleshoot all incoming MO-related activity in the system.

!!! info "Primary Use Cases"
    - Monitoring MO message activity in real time
    - Checking incoming user or vendor communication logs
    - Troubleshooting MO-related delivery or routing issues
    - Reviewing system-generated MO events
    - Verifying gateway communication logs for inbound traffic

---

## Available Information

The module displays the following fields for each log entry:

| Field | Description |
|-------|-------------|
| **Time** | Exact timestamp of the MO event. |
| **Log Type** | Classification of the event — `Info` or `Error`. |
| **Message** | Description of the MO event or activity. |

![Event Viewer (MO) — Info log entries](images/eventmo-01-info.png)

![Event Viewer (MO) — Error log type (no entries shown)](images/eventmo-02-error.png)

---

## Log Types

| Log Type | Description |
|----------|-------------|
| **Info** | Informational system events, successful gateway changes, user list updates. |
| **Error** | Error-level events indicating failures, rejected MO messages, or system exceptions. |

---

## Features

!!! info "Event Viewer (MO) Capabilities"
    - View MO event logs in real time.
    - Monitor gateway and user inbound activities.
    - Track incoming MO message requests.
    - Troubleshoot and resolve MO-related issues.
    - Refresh logs on demand using the **Refresh** button.
    - Filter logs by **log type** (Info / Error).
    - Filter logs by **date range** for historical review.

---

## Date Range Filter

Administrators can select a specific date range to retrieve **historical MO event logs**. This supports retrospective troubleshooting, compliance auditing, and operational review.

!!! tip
    When chasing an intermittent issue, set **Log Type = Error** first to focus on failures only, then widen to **All** if no error events are visible during the window.
