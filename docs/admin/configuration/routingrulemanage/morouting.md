---
tags:
  - MO
  - Routing
  - Rules
  - Configuration
---

# MO Routing Rule

## Overview

**MO Routing Rules** in iTextPro are used to define how incoming MO messages should be identified, filtered, and routed within the platform.

The routing rule determines:

- Which incoming MO traffic should be processed
- Which keyword should trigger the routing
- Which user should receive the MO traffic
- Which interface type should be used for delivery

MO Routing Rules work together with the configured **HTTP MO Handler**.

---

## Navigation Path

`Configuration` ➔ `Routing Rule Manager` ➔ `MO Routing Rules` ➔ `Add New MO Rule`.

![Manage MO Routing Rules list](images/morouting-01-list.png)

---

## MO Routing Rule Parameters

The following parameters must be configured while creating the routing rule.

## General Parameters

### 1] Rule Name

The **Rule Name** uniquely identifies the MO Routing Rule within the platform.

This name is used for:

- Rule management
- Traffic monitoring
- Administration
- Troubleshooting

!!! example
    ```
    MO_ROUTE_KEYWORD_01
    ```

---

### 2] Lifetime

The **Lifetime** parameter defines the validity duration of the routing rule.

**Usage:**

- Can be used for temporary campaigns
- Supports time-based MO routing
- Useful for limited-time services

!!! tip
    If no expiry is required, this field can be left blank.

---

## Gateway Interface Configuration

### Handler

The **Handler** field is used to select the HTTP MO Handler previously configured in the platform.

This handler will process all MO requests matching the routing conditions. The handler will be used in case the vendor sends MO with **HTTP connection**.

### Gateway

In case the vendor supports the **SMPP** protocol for sending the MO hits, then during creation of the MO Routing Rule the admin needs to select the **Gateway** and pick the correct gateway in order to fetch the hits from the correct gateway.

**Purpose:**

- Links MO traffic with the correct endpoint
- Associates routing with the incoming channel
- Enables message processing workflow

![Add New MO Rule — General Parameters & Gateway Interface](images/morouting-02-general.png)

---

## Routing Conditions

Routing conditions define the **filtering logic** for incoming MO traffic. The platform evaluates these conditions before processing or routing the MO request.

### 1] Originator Condition

The **Originator** condition defines filtering based on the sender mobile number.

**Example Configuration:** `Any`

Selecting **Any** allows MO messages from all sender numbers. Specific sender filtering can also be configured if required.

---

### 2] Destination Condition

The **Destination** condition defines the receiving Short Code or Long Code number.

| Field | Value |
|-------|-------|
| **Condition Type** | `Equals` |
| **Example** | `567890` |

The routing rule will trigger only if the incoming MO message is received on the configured destination number.

---

### 3] Message Condition

The **Message** condition defines the keyword matching criteria.

| Field | Value |
|-------|-------|
| **Condition Type** | `Starts With` |
| **Example Keyword** | `ASKRK` |

The routing rule will trigger only if the incoming message starts with the configured keyword.

!!! example
    For an incoming message `ASKRK BALANCE`, since the message starts with `ASKRK`, the routing rule will process the MO request.

![Routing Conditions and User / Endpoint selection](images/morouting-03-condition-user.png)

---

## User and Endpoint Mapping

### 1] User

Select the **user account** to which the MO traffic should be mapped and delivered.

This mapping ensures that the correct user receives the incoming MO messages.

### 2] User Interface Type

The **User Interface Type** defines how the MO message should be forwarded after routing.

**Supported Interface Types:**

| Type | Description |
|------|-------------|
| **Not Selected** | No interface-specific routing will be applied. |
| **ESME** | Routes the MO traffic through SMPP connectivity. Generally used when the user is connected via SMPP protocol. |
| **Webhook** | Routes the MO traffic to an external HTTP API endpoint. Commonly used for CRM integrations, third-party applications, web-based processing systems, and API-driven workflows. |

---

## Save Routing Rule

After configuring all routing parameters:

1. Verify the routing conditions.
2. Validate the keyword configuration.
3. Click on **Save**.

The MO Routing Rule is now successfully configured and active for MO traffic processing.

!!! tip "Verification"
    After saving the rule, send a test MO message that matches the configured conditions (sender allowed, correct destination number, message starting with the configured keyword) and confirm that the rule fires by checking the user's MO inbox or webhook endpoint logs.
