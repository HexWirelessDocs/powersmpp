---
tags:
  - SMPP
  - Error Codes
  - Reference
  - Gateway
---

# Standard SMPP Error Code List

This page provides a complete reference of all SMPP protocol error codes, iTextPro application error codes, and iTextHub HTTP Gateway error codes. Use this reference to diagnose message delivery failures seen in reports, PDU logs, and event viewers.

---

## Standard SMPP Error Codes

These are protocol-level error codes defined by the SMPP v3.4 specification. They are returned by the SMSC (Short Message Service Centre) in response to SMPP operations.

| Sr. No | Error Code (Hex) | Error Code (Decimal) | Error Name | Error Description |
|--------|-----------------|---------------------|------------|-------------------|
| 1 | 0x00 | 0 | Command executed successfully | The SMPP command was processed without errors |
| 2 | 0x01 | 1 | Message Length is invalid | The message body length exceeds allowed limits |
| 3 | 0x02 | 2 | Command Length is invalid | The PDU command length field is incorrect |
| 4 | 0x03 | 3 | Invalid Command ID | The command ID is not recognized by the SMSC |
| 5 | 0x04 | 4 | Incorrect BIND Status for given command | The ESME attempted a command that is not allowed in its current bind state |
| 6 | 0x05 | 5 | ESME Already in Bound State | The ESME is already bound and cannot bind again |
| 7 | 0x06 | 6 | Invalid Priority Flag | The priority flag value in the PDU is not valid |
| 8 | 0x07 | 7 | Invalid Registered Delivery Flag | The registered delivery flag value is not valid |
| 9 | 0x08 | 8 | System Error | A general system error occurred on the SMSC |
| 10 | 0x0A | 10 | Invalid Source Address | The source (sender) address is invalid or not allowed |
| 11 | 0x0B | 11 | Invalid Destination Address | The destination (recipient) address is invalid |
| 12 | 0x0C | 12 | Message ID is invalid | The message ID referenced does not exist |
| 13 | 0x0D | 13 | Bind Failed | The bind operation failed due to authentication or configuration issues |
| 14 | 0x0E | 14 | Invalid Password | The password provided during bind is incorrect |
| 15 | 0x0F | 15 | Invalid System ID | The system ID provided during bind is not recognized |
| 16 | 0x11 | 17 | Cancel SM Failed | The cancel_sm operation could not be completed |
| 17 | 0x13 | 19 | Replace SM Failed | The replace_sm operation could not be completed |
| 18 | 0x15 | 21 | Invalid Service Type | The service_type parameter is not valid |
| 19 | 0x33 | 51 | Invalid number of destinations | The number of destinations in submit_multi is invalid |
| 20 | 0x34 | 52 | Invalid Distribution List name | The distribution list name referenced does not exist |
| 21 | 0x40 | 64 | Destination flag is invalid (submit_multi) | The dest_flag in submit_multi contains an invalid value |
| 22 | 0x42 | 66 | Submit w/replace unsupported | Submit with replace functionality has been requested where it is either unsupported or inappropriate for the particular MC |
| 23 | 0x43 | 67 | Invalid esm_class field data | The esm_class field contains invalid data |
| 24 | 0x44 | 68 | Cannot Submit to Distribution List | The message cannot be submitted to the specified distribution list |
| 25 | 0x45 | 69 | submit_sm, data_sm or submit_multi failed | The submit operation failed |
| 26 | 0x48 | 72 | Invalid Source address TON | The Type of Number for the source address is invalid |
| 27 | 0x49 | 73 | Invalid Source address NPI | The Numbering Plan Indicator for the source address is invalid |
| 28 | 0x51 | 81 | Invalid Destination address NPI | The Numbering Plan Indicator for the destination address is invalid |
| 29 | 0x53 | 83 | Invalid system_type field | The system_type parameter is not valid |
| 30 | 0x54 | 84 | Invalid replace_if_present flag | The replace_if_present flag contains an invalid value |
| 31 | 0x55 | 85 | Invalid number of messages | The number of messages parameter is invalid |
| 32 | 0x58 | 88 | Throttling error | ESME has exceeded allowed message limits (TPS throttling) |
| 33 | 0x61 | 97 | Invalid Scheduled Delivery Time | The scheduled delivery time format or value is invalid |
| 34 | 0x62 | 98 | Invalid message validity period | The message validity period (expiry time) is invalid |
| 35 | 0x63 | 99 | Predefined Message ID is Invalid | The specified predefined message was not found |
| 36 | 0x65 | 101 | ESME Receiver Permanent App Error Code | A permanent application error on the ESME receiver |
| 37 | 0x66 | 102 | ESME Receiver Reject Message Error Code | The ESME receiver rejected the message |
| 38 | 0x67 | 103 | Query_Sm request failed | The query_sm operation could not be completed |
| 39 | 0xC0 | 192 | Error in the optional part of the PDU Body | The optional TLV parameters in the PDU body contain errors |
| 40 | 0xC1 | 193 | TLV not allowed | The TLV parameter is not permitted for this operation |
| 41 | 0xC2 | 194 | Invalid Parameter Length | A TLV parameter has an invalid length |
| 42 | 0xC3 | 195 | Expected TLV missing | A required TLV parameter is missing from the PDU |
| 43 | 0xC4 | 196 | Invalid TLV Value | A TLV parameter contains an invalid value |
| 44 | 0xFE | 254 | Transaction Delivery Failure | The message transaction could not be delivered |
| 45 | 0xFF | 255 | Unknown Error | An unknown or unspecified error occurred |
| 46 | 0x100 | 256 | ESME Not authorized to use specified service type | The ESME is not authorized for the requested service type |
| 47 | 0x101 | 257 | ESME Prohibited from using specified operation | The ESME is blacklisted or prohibited from using the specified operation |
| 48 | 0x102 | 258 | Specified service type is unavailable | The requested service type is currently unavailable |
| 49 | 0x103 | 259 | Specified service type is denied | The requested service type has been denied |
| 50 | 0x105 | 261 | Source Address Sub unit is Invalid | The source address sub-unit parameter is invalid |
| 51 | 0x106 | 262 | Destination Address Sub unit is Invalid | The destination address sub-unit parameter is invalid |
| 52 | 0x107 | 263 | Broadcast Frequency Interval is invalid | The broadcast frequency interval parameter is invalid |
| 53 | 0x108 | 264 | Broadcast Alias Name is invalid | The broadcast alias name is not valid |
| 54 | 0x109 | 265 | Broadcast Area Format is invalid | The broadcast area format parameter is invalid |
| 55 | 0x10A | 266 | Number of Broadcast Areas is invalid | The number of broadcast areas specified is invalid |
| 56 | 0x10B | 267 | Broadcast Content Type is invalid | The broadcast content type parameter is invalid |
| 57 | 0x10C | 268 | Broadcast Message Class is invalid | The broadcast message class is invalid |
| 58 | 0x10D | 269 | Broadcast_sm operation failed | The broadcast_sm operation could not be completed |
| 59 | 0x10F | 271 | Cancel_broadcast_sm operation failed | The cancel_broadcast_sm operation could not be completed |
| 60 | 0x110 | 272 | Number of Repeated Broadcasts is invalid | The number of repeated broadcasts parameter is invalid |
| 61 | 0x111 | 273 | Broadcast Service Group is invalid | The broadcast service group parameter is invalid |
| 62 | 0x112 | 274 | Broadcast Channel Indicator is invalid | The broadcast channel indicator is invalid |
| 63 | 0x15F95 | 90005 | Local Exception | Check LastException property for details |

---

## iTextPro Error Codes

These are application-level error codes generated by the iTextPro / Power SMPP platform. They indicate issues with routing, billing, account configuration, or system operations.

| Sr. No | Error Code (Hex) | Error Code (Decimal) | Error Name | Error Description |
|--------|-----------------|---------------------|------------|-------------------|
| 64 | 0x439 | 1081 | Country Undef | Country not defined by admin in Master Data Manager |
| 65 | 0x43A | 1082 | Invalid Network | Network not defined by admin in Master Data Manager |
| 66 | 0x43B | 1083 | Price Undefined | Pricing not defined by admin for respective country and network on the primary gateway |
| 67 | 0x43C | 1084 | Expired (Loss Protection) | Message undelivered due to Loss Protection policy |
| 68 | 0x43D | 1085 | Route Undef | Routing not defined by admin for respective country and network |
| 69 | 0x43E | 1086 | Failover Route Undef | Master failover not defined by admin for respective country and network |
| 70 | 0x43F | 1087 | Failover Expired | Message undelivered due to Loss Protection on failover gateway |
| 71 | 0x440 | 1088 | Failover Price Undef | Pricing not defined by admin for respective country and network on failover gateway |
| 72 | 0x441 | 1089 | Failover Failed | System Error: Unhandled exception during failover routing |
| 73 | 0x442 | 1090 | Account Validity Expired | User account validity has expired |
| 74 | 0x443 | 1091 | Encoding Error | System Error: Encoding error due to invalid data coding value (can be regenerated by sending data coding values except 0 & 8) |
| 75 | 0x444 | 1092 | OA/DA Error | System Error: OA/DA Error due to invalid Regex in normalization rules |
| 76 | 0x445 | 1093 | Queue Message Expired | System Error: Queue message expired due to prolonged gateway outage |
| 77 | 0x446 | 1094 | Invalid HTTP Gateway Config | System Error: Invalid HTTP gateway configuration or response code |
| 78 | 0x417 | 1047 | User Account Inactive | User account is inactive and cannot send messages |
| 79 | 0x400 | 1024 | User Account Locked | User account has been locked by the administrator |
| 80 | 0x401 | 1025 | Insufficient Balance | Insufficient balance in user account (prepaid) |
| 81 | 0x402 | 1026 | Template Mismatch | Template mismatch detected — message content does not match approved template |
| 82 | 0x405 | 1029 | Invalid Sender ID | Invalid or unapproved Sender ID detected |
| 83 | 0x407 | 1031 | Global Blacklist Number | The destination number is on the global blacklist |
| 83 | 0x40B | 1035 | No Active Connection | No active SMPP connection available to the gateway |
| 84 | 0x40C | 1036 | Queue Server Error | System Error: Message queue internal server error |
| 85 | 0x40D | 1037 | Cache Server Error | System Error: Cache database error |
| 86 | 0x40E | 1038 | Invalid Connection State | Network Error: Gateway not reachable |
| 87 | 0x40F | 1039 | SMPP Timeout | Network Error: Gateway timeout — no response received |
| 88 | 0x410 | 1040 | Unknown SMPP Error | System Error: An unclassified SMPP error occurred |
| 89 | 0x411 | 1041 | Final Disconnection | The SMPP connection was permanently disconnected |
| 90 | 0x412 | 1042 | Final Timeout | The connection timed out permanently |
| 91 | 0x413 | 1043 | No Gateway Found | No suitable gateway found for routing the message |
| 92 | 0x404 | 1028 | Invalid IP | Invalid IP address for SMPP account (IP validation failed) |
| 93 | 0x414 | 1044 | Spam Detected | Message failed due to spam keyword detected in content |
| 94 | 0x448 | 1096 | Message Length Exceeded | SMS message length exceeded the allowed limit |

---

## iTextHub HTTP Gateway Error Codes

These error codes are returned by the iTextHub HTTP Gateway when processing HTTP API requests.

| Sr. No | Error Code (Decimal) | Error Name | Error Description |
|--------|---------------------|------------|-------------------|
| 95 | 110 | Error while getting text response | Failed to retrieve text response from the HTTP gateway |
| 96 | 111 | Error while getting JSON/XML response | Failed to parse JSON or XML response from the HTTP gateway |
| 97 | 112 | Error while reading response | Failed to read the HTTP response stream |
| 98 | 113 | Error while reading response from result | Failed to extract data from the HTTP response result |
| 99 | 114 | Error while requesting REST/JSON API | Failed to make a REST/JSON API request to the HTTP gateway |
| 100 | 115 | Error while requesting Simple HTTP API | Failed to make a Simple HTTP API request to the HTTP gateway |
| 101 | 116 | Error while requesting SOAP API | Failed to make a SOAP API request to the HTTP gateway |
| 102 | 1095 | Error while requesting SOAP/Simple/RestJson API | Combined error code for 114, 115, and 116 (used in latest version) |

---

!!! tip "How to use this reference"
    - When you see an error code in your **Campaign Reports**, **PDU Logs**, or **Event Viewer**, look it up in the tables above
    - **Standard SMPP codes** (0–255) are returned by the external SMSC/gateway
    - **iTextPro codes** (1024–1096) are generated internally by the Power SMPP platform
    - **HTTP GW codes** (110–1095) relate to HTTP gateway connectivity issues
    - For gateway-specific error code configuration, see [Gateway Error Codes](errorcode.md)
