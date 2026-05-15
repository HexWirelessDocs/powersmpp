---
tags:
  - Billing
  - WhatsApp
  - Rate Plan
---

# WhatsApp Rate Plan Configuration

**Navigation:** `Admin Panel` ➔ `Billing` ➔ `WhatsApp Rate Plan` ➔ `Create Template`.

## Overview

The **WhatsApp Rate Plan Configuration** module enables administrators to define **pricing templates** for WhatsApp messaging. These rate plans govern how messages are billed and tracked within the PowerSMPP platform and are assigned to user accounts for accurate cost and revenue management.

---

## Creating a New WhatsApp Rate Plan

The rate plan creation process is structured into **three steps**.

![Manage WA Rate Plans — List of configured plans](images/warateplan-01-list.png)

### Step 1: Basic Details

| Field | Description |
|-------|-------------|
| **Rate Plan Name** | Assign a unique, descriptive name for the plan. |
| **Is Active** | Toggle the plan to `Active` or `Inactive` status. |

![Add New WA Rate Plan — Step 1: Basic Details](images/warateplan-02-step1-basic.png)

### Step 2: Price Details (Per Country)

Define the pricing structure for each destination country.

![Add New WA Rate Plan — Step 2: Price Details](images/warateplan-03-step2-price.png)

| Field | Description |
|-------|-------------|
| **Country Code** | Select the destination country (for example, `India +91`). Rate plan supports multi-country pricing. |
| **Cost Price** | The purchase / wholesale cost per WhatsApp message for the selected country. |
| **Selling Price** | The retail price charged to the end user or customer for each WhatsApp message. |
| **Platform Charge** | Additional platform fee applied on top of the selling price (if applicable). |

### Step 3: Assign to Users

Once the rate plan is saved, it becomes available for assignment to individual user accounts. Assigning the plan ensures all WhatsApp messages sent by the user are billed according to the configured pricing structure.

---

## Managing Existing Rate Plans

The **Manage WA Rate Plan** screen lists all configured WhatsApp rate plans with the following information:

| Column | Description |
|--------|-------------|
| **Plan Name** | The rate plan's identifier. |
| **Rates** | Number of country-rate entries configured. |
| **User Assigned** | Number of users currently assigned to the plan. |
| **Create Date** | Date the plan was created. |
| **Is Active** | Current status (`Active` / `Inactive`). |
| **Is Default** | Whether the plan is the system default. |
| **Action** | `Edit`, `View`, `Clone`, or `Delete` the plan. |

---

## Purpose of WhatsApp Rate Plan Configuration

!!! info "Use this module to…"
    - Define country-specific WhatsApp messaging pricing.
    - Support multi-country rate plans within a single template.
    - Assign rate plans to specific user accounts for billing.
    - Track WhatsApp message costs and revenue per user.
    - Enable accurate financial reporting for WhatsApp traffic.
    - Manage platform charges alongside cost and selling prices.

!!! tip
    Cloning is the fastest way to spin up a regional variant of an existing plan — clone the parent, adjust one or two country prices, and assign to the new user group.
