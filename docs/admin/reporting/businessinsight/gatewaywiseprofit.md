---
tags:
  - Reporting
  - Business Insight
  - Gateway
  - Profit
---

# Gateway Wise Profit Report

**Navigation:** `Reporting` ➔ `Business Insight` ➔ `Gateway Wise Profit`.

## Overview

The **Gateway Wise Profit Report** provides administrators with a detailed breakdown of gateway-level profitability and SMS traffic analytics. It is designed to support financial analysis, billing verification, and gateway performance monitoring by presenting **purchase cost**, **sales value**, and **profit margins** for SMS traffic routed through each gateway.

---

## 1. Gateway Selection

Select a specific gateway from the dropdown to generate a profit report scoped to that gateway's traffic.

![Gateway Wise Profit — Gateway dropdown selection](images/gwprofit-01-gateway-dropdown.png)

---

## 2. Country Selection

The report can be further filtered by destination country, enabling granular country-level profitability analysis.

![Gateway Wise Profit — Country filter dropdown](images/gwprofit-02-country-filter.png)

---

## 3. Date Range Filter

Administrators can define a **custom date range** to generate profit reports for any historical period.

!!! info "Date Range Features"
    - Daily and historical traffic analysis
    - Flexible date-based filtering
    - Billing period verification support
    - Operational performance review over any timeframe

---

## 4. Table View Report

The **Table View** presents country-wise gateway profit data in a structured tabular format with the following columns:

| Column | Description |
|--------|-------------|
| **Gateway Name** | The gateway routing the traffic. |
| **Country Name** | Destination country of the traffic. |
| **MCCMNC** | Mobile Country Code + Mobile Network Code. |
| **Network Name** | Destination mobile network. |
| **Message Count** | Total SMS messages routed for this slice. |
| **Purchase Price** | Routing cost for this slice. |
| **Sales Price** | Revenue earned from this slice. |
| **Margin (Sales − Purchase) %** | Calculated profit percentage. |
| **Margin (Sales − Purchase) (EURO)** | Absolute profit value in EURO. |

![Gateway Wise Profit — Table View](images/gwprofit-03-table-view.png)

!!! note
    `*` against a price indicates that the price is a flat price.

---

## 5. Graph View Report

The **Graph View** provides a visual bar-chart representation of gateway profitability, enabling rapid identification of high-performing and low-performing gateways or destination countries.

![Gateway Wise Profit — Graph View (Margin bar chart)](images/gwprofit-04-graph-view.png)

---

## 6. Profit Calculation Formula

The report uses the following standard formulas to derive profitability metrics:

```
Margin (Base Currency) =  Sales Price − Purchase Price

Margin Percentage (%)  = ((Sales Price − Purchase Price) / Purchase Price) × 100
```

---

## Purpose of the Gateway Wise Profit Report

!!! info "Use this report to…"
    - Monitor gateway profitability in real time
    - Compare country-wise and gateway-wise margins
    - Track SMS traffic volume and associated costs
    - Review gateway revenue vs. purchase cost
    - Support financial reporting and billing verification
    - Optimise routing strategies for better revenue management
    - Export reports for offline analysis and record-keeping
