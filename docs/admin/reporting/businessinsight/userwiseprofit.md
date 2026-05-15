---
tags:
  - Reporting
  - Business Insight
  - User
  - Profit
---

# User Wise Profit Report

**Navigation:** `Reporting` ➔ `Business Insight` ➔ `User Wise Profit`.

## Overview

The **User Wise Profit Report** enables administrators to analyse user-level SMS traffic and profitability for any selected date range. The report is based **entirely on messages submitted by users through the application** and provides detailed revenue, cost, and margin data per customer account.

---

## 1. User Selection

Select a specific user account from the dropdown list to generate a targeted profit report for that customer.

## 2. Country Selection

Filter traffic data by destination country to obtain granular analysis of user profitability per region.

## 3. Date Range Filter

Define a custom date range to generate user profit reports for any billing or operational period.

---

## 4. Table View Report

The **Table View** displays detailed user-wise profitability information in tabular format.

![User Wise Profit — Table View (all users)](images/userprofit-01-table-all.png)

![User Wise Profit — Table View (highlighted)](images/userprofit-02-table-highlighted.png)

### Column Reference

| Column | Description |
|--------|-------------|
| **User Name** | Name / identifier of the user account. |
| **Country Name** | Destination country of the user's SMS traffic. |
| **MCCMNC** | Mobile Country Code + Mobile Network Code. |
| **Network Name** | Destination mobile network name. |
| **Message Count** | Total SMS messages submitted by the user. |
| **Purchase Price** | Actual routing cost incurred for processing the user's traffic. |
| **Sales Price** | Total selling amount charged to the user. |
| **Margin % (Sales − Purchase)** | Calculated profit percentage for the user's traffic. |
| **Margin (Sales − Purchase)** | Total profit earned from user traffic in USD. |

---

## 5. Graph View Report

The **Graph View** renders a bar chart of user-wise profitability, enabling quick comparison across customers.

![User Wise Profit — Graph View (Margin by user)](images/userprofit-03-graph-view.png)

---

## 6. Message Submission Analysis

All calculations in the User Wise Profit Report are driven **exclusively** by messages submitted from the user side through the application. Traffic that bypasses the application user submission path is not included in this report.

---

## 7. Profit Calculation Formula

```
Margin (USD)          =  Sales Price − Purchase Price

Margin Percentage (%) = ((Sales Price − Purchase Price) / Purchase Price) × 100
```

!!! tip
    Combine this report with **Gateway Wise Profit** to see profitability from two complementary angles — the customer (revenue side) and the vendor (cost side).
