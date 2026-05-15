---
tags:
  - Reporting
  - Business Insight
  - Gateway
---

# Gateway Wise Count

**Navigation:** `Reporting` ➔ `Business Insight` ➔ `Gateway Wise Count`.

## Overview

The **Gateway Wise Count** report provides administrators with a consolidated view of message submission volumes across all configured gateways. The report covers the **last seven days** on a per-day basis, making it easy to identify traffic patterns and load distribution at a glance.

![Gateway Wise Count — All Gateways (7-day view)](images/gwcount-01-all-gateways.png)

---

## Using the Gateway Filter

To narrow the report to a specific gateway, select the desired gateway from the **dropdown filter** available on the report screen. The table will refresh to show only that gateway's submission data.

![Gateway Wise Count — Filtered by a single gateway](images/gwcount-02-filtered.png)

---

## What the Report Shows

| Column | Description |
|--------|-------------|
| **Gateway Name** | Friendly name of the configured gateway. |
| **Date columns (one per day)** | Total message count routed through that gateway on the corresponding day. |

!!! note
    The visible message counts are computed against each **gateway's own timezone**, not the application timezone. This is shown in the in-page note above the table.

---

## When to Use This Report

- Spot day-over-day traffic dips that could indicate vendor or network issues.
- Identify under-utilised gateways that may be candidates for retirement or re-routing.
- Verify that newly added gateways are receiving the expected share of traffic.
- Provide quick week-at-a-glance volume snapshots for stakeholders.
