---
tags:
  - Reference
  - SMPP
  - Getting Started
---

# Glossary

A quick reference guide to common terms used throughout the PowerSMPP documentation.

---

## Messaging Terms

| Term | Full Form | Description |
|------|-----------|-------------|
| **SMS** | Short Message Service | Standard text messaging protocol for mobile devices |
| **MT** | Mobile Terminated | A message sent **to** a mobile handset (outbound) |
| **MO** | Mobile Originated | A message sent **from** a mobile handset (inbound) |
| **DLR** | Delivery Report | Status notification confirming whether an MT message was delivered |
| **A2P** | Application-to-Person | Automated messages sent from an application to end users |
| **P2P** | Person-to-Person | Messages exchanged between individual users |

---

## SMPP Protocol

| Term | Full Form | Description |
|------|-----------|-------------|
| **SMPP** | Short Message Peer-to-Peer | Industry-standard protocol for exchanging SMS between systems |
| **SMSC** | Short Message Service Centre | Central system that stores, routes, and delivers SMS messages |
| **ESME** | External Short Messaging Entity | An external application that connects to the SMSC via SMPP |
| **PDU** | Protocol Data Unit | A single SMPP data packet exchanged between ESME and SMSC |
| **Bind** | — | The process of establishing an SMPP session between ESME and SMSC |
| **Tx** | Transmitter | An SMPP session that can only **send** messages |
| **Rx** | Receiver | An SMPP session that can only **receive** messages |
| **TRx** | Transceiver | An SMPP session that can both **send and receive** messages |
| **TPS** | Transactions Per Second | The throughput capacity of an SMPP connection |

---

## Addressing

| Term | Full Form | Description |
|------|-----------|-------------|
| **TON** | Type of Number | Defines the format of the address (e.g., International, Alphanumeric) |
| **NPI** | Numbering Plan Indicator | Identifies the numbering standard (e.g., E.164, ISDN) |
| **OA** | Originating Address | The sender address (source) of a message |
| **DA** | Destination Address | The recipient address (destination) of a message |
| **MCC** | Mobile Country Code | A 3-digit code identifying a mobile subscriber's country |
| **MNC** | Mobile Network Code | A 2-3 digit code identifying a mobile network operator |
| **MSISDN** | Mobile Station International Subscriber Directory Number | The full international phone number of a mobile subscriber |

---

## Platform Features

| Term | Description |
|------|-------------|
| **Rate Plan** | A pricing template that defines per-message costs for different destinations |
| **Routing Rule** | A rule that determines which gateway handles a message based on criteria like destination, sender, or content |
| **Gateway** | An external SMSC or aggregator connection configured in iTextPRO |
| **Interface** | An SMPP or HTTP connector that allows partners to connect to iTextPRO |
| **Blind Routing** | Allows message submission to destinations without pre-defined cost prices |
| **Stop Loss** | A maximum gateway cost threshold to prevent losses on blind-routed messages |
| **HLR Lookup** | Home Location Register query to validate a mobile number before sending |
| **DLT** | Distributed Ledger Technology — India's regulatory framework for A2P SMS requiring pre-registration of senders and templates |

---

## Billing & Business

| Term | Description |
|------|-------------|
| **Prepaid** | Billing mode where users must have sufficient credit balance before sending |
| **Postpaid** | Billing mode where users are billed after consumption |
| **Base Currency** | The primary currency used for all internal billing calculations |
| **Recurring Invoice** | Automated invoice generated at regular intervals (weekly, monthly, etc.) |

---

## System & Monitoring

| Term | Description |
|------|-------------|
| **Event Viewer** | A log viewer for monitoring system events, errors, and warnings |
| **Audit Log** | A chronological record of all user and system actions for compliance |
| **PDU Logger** | A tool to capture and inspect raw SMPP protocol data packets |
| **Enquire Link** | An SMPP keep-alive packet sent periodically to maintain active sessions |
| **QoS** | Quality of Service — metrics used to evaluate gateway delivery performance |
