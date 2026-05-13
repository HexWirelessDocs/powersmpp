---
tags:
  - HTTP
  - Gateway
  - Configuration
---

# HTTP Gateway

In **Power SMPP**, we support both **SMPP** and **HTTP** protocols for vendor connectivity. Consequently, the administrator has the option to configure either an SMPP-based gateway or an HTTP gateway. This document provides a concise overview of the HTTP gateway configuration. It is designed to help administrators understand and set up an HTTP gateway within the Power SMPP application with ease.

As the name suggests, the HTTP gateway is based on the **Hypertext Transfer Protocol (HTTP)**. This protocol allows clients to send messages via an API that acts as a gateway within the Power SMPP application.

![Manage Gateway list view](images/httpgw-01-manage-gateway.png)

**Navigation:** `Configuration` ➔ `Gateway Configuration` ➔ `SMPP/HTTP Gateways` ➔ `HTTP Gateway` ➔ `Add New`.

![HTTP Gateway Detail sections](images/httpgw-02-detail-sections.png)

!!! tip "View Documentation"
    When clicking on **Add New**, the first option will be **View Documentation**. We recommend that the administrator review this document to become familiar with the terms mentioned in the gateway configuration.

The HTTP Gateway Detail screen is organised into the following sections:

- Required Credentials
- Message Types
- Parameters
- Conditional Parameters
- Gateway Properties
- Response Properties
- Session
- Automatic Message Delivery

---

## Section 1: Required Credentials

In this section, various pieces of information are required, such as **Gateway Name**, **Request Type**, **Authentication**, **Base URL**, and **UDH**.

**Gateway Name** — An easy-to-remember name for the HTTP Gateway.

**Is UDH Required?** — Specifies whether the **UDH (User Data Header)** is necessary for the messages sent from this gateway. UDH is used for concatenated messages.

**Request Type** — Specifies the type of HTTP request. It could be **Simple HTTP**, **REST/JSON**, or **SOAP**. Different request types require different configurations. Generally, Simple HTTP is used for `GET` methods, while REST/JSON can be used for both `GET` and `POST` methods.

![Required Credentials form](images/httpgw-03-required-credentials.png)

**Base URL Detail** — Specifies the base URL for the HTTP API, **excluding** all other parameters.

!!! example
    If the API URL is `http://testsmsportal.com/sendsms?number=9184545&msg=test`, then the Base URL should be configured as `http://testsmsportal.com/sendsms`.

**Authentication** — Power SMPP currently supports three kinds of authorization:

| # | Type | Description |
|---|------|-------------|
| 1 | **No Auth** | No authorization is required. |
| 2 | **Basic Auth** | A username and password are required for secure authentication of the API. |
| 3 | **OAuth 2.0** | The latest version of authorization, used to regenerate new credentials after a certain period to maintain high security of the API using the **OAuth Handler** API. |

![Authentication options](images/httpgw-04-authentication.png)

---

## Section 2: Message Types

**Message Type** is an optional section where the administrator can configure the value of data coding accepted by the vendor. The default values for each data coding type are mentioned in brackets.

| Type | Default | Purpose |
|------|---------|---------|
| **TEXT** | `00` | Mapping the gateway-specific message type for plain text messages. |
| **UNICODE** | `08` | Mapping the gateway-specific message type for Unicode messages. |
| **BINARY** | `02` | Mapping the gateway-specific message type for binary messages. |
| **FLASH** | `F2` or `10` | Mapping the gateway-specific message type for flash messages. |

!!! note
    Map your gateway-specific message types with system message types. Leave the fields blank if not applicable.

![Message Types form](images/httpgw-05-message-types.png)

---

## Section 3: Parameters

The **Parameter** section allows the admin to configure the gateway details and request parameters provided by the gateway vendor. These parameters are used by Power SMPP to construct and transmit the API request data/body to the respective gateway vendor for message processing and delivery.

The configured parameters define how the HTTP request will be generated and executed during API communication.

### Method

Power SMPP supports the following HTTP methods for API execution:

#### 1] GET Method

The GET method allows the admin to configure the request parameters in **key-value pair** format. During API execution, all configured parameters are appended directly to the URL as **query parameters**.

This method is generally used for:

- Simple API requests
- URL-based parameter transmission
- Lightweight API integrations
- Legacy HTTP integrations

!!! example
    `https://api.vendor.com/sendSMS?username=admin&password=test123&mobile=9876543210`

In the GET method, Power SMPP supports the following parameter types:

##### Parent Name

The **Parent Name** field is mainly used for **SOAP-based** API integrations where parameters need to be grouped under a parent XML node or request object.

This configuration helps in generating structured SOAP request payloads as per the vendor API specification.

!!! example
    ```xml
    <SendSMS>
        <username>admin</username>
        <password>test123</password>
    </SendSMS>
    ```
    In the above example, `SendSMS` acts as the Parent Name.

##### Header Parameter

The **Header Parameter** section is used to configure HTTP header values required during API execution.

These parameters are generally used for:

- Authentication Tokens
- API Keys
- Authorization Credentials
- Content-Type Definitions
- Custom Vendor Headers

!!! example
    ```
    Authorization: Bearer xxxxx
    Content-Type: application/json
    ```

Header parameters are transmitted within the HTTP request header during API communication.

##### Body Parameter

The **Body Parameter** section contains all general request parameters required for the HTTP API request.

These parameters typically include:

- Mobile Number
- Message Content
- Sender ID
- Template ID
- Entity ID
- Routing Parameters
- Custom Vendor Parameters

For **GET** requests, these parameters are appended within the request URL as query parameters during API execution.

![Parameters configuration with example rows](images/httpgw-06-parameters.png)

#### 2] POST Method

The **POST** method allows the admin to configure the gateway by sending all required request parameters within the **request body** instead of appending them in the URL. This method is recommended for API integrations where large amounts of data, authentication parameters, headers, tokens, or complex payload structures are required.

Using the POST method provides the following advantages:

- Reduces URL length and complexity.
- Improves security by avoiding sensitive information exposure in the URL.
- Supports structured and large payload data.
- Enables compatibility with advanced API integrations.
- Allows flexible request body formatting based on API requirements.

The configured payload is transmitted in the HTTP request body during API execution.

##### Payload Type

While selecting the POST method, the admin can configure the request payload using one of the following payload types:

###### I] Key-Value Parameter [POST FORM DATA]

This option allows the admin to configure the request payload in a standard **key-value parameter** format, where each parameter is defined separately using a field name and corresponding value.

This payload type is suitable for APIs that accept:

- Form Data
- URL Encoded Parameters
- Simple structured request bodies

!!! example
    ```
    Key        Value
    username   admin
    password   test123
    senderid   ABCDEF
    ```

**Benefits:**

- Easy to configure and manage.
- Suitable for simple API integrations.
- Allows dynamic parameter mapping.
- Simplifies request validation and troubleshooting.

![POST Form Data Key-Value parameters](images/httpgw-07-post-form-data.png)

###### II] RAW Payload

This option allows the admin to pass the **complete request body** directly as raw content without defining individual key-value parameters separately.

The RAW Payload method is mainly used when the target API requires:

- JSON Payload
- XML Payload
- Plain Text Payload
- Custom Structured Data

The admin can directly paste or configure the complete payload content exactly as required by the destination API.

**Supported RAW Payload Formats:** `JSON`, `XML`, `TEXT`.

!!! example "JSON Payload"
    ```json
    {
      "username": "admin",
      "password": "test123",
      "senderid": "ABCDEF"
    }
    ```

**Benefits:**

- Supports complex and nested payload structures.
- Enables seamless integration with modern REST APIs.
- Provides flexibility for custom API request formats.
- Allows direct control over payload structure and formatting.

![RAW JSON payload editor](images/httpgw-08-raw-payload.png)

In Power SMPP, the administrator can define **placeholders** for various values, such as `##senderid##` for Sender ID, `##message##` for the text content, `##mobile##` for the destination, and many more. This allows the administrator to configure various dynamic values for the parameters. Additionally, the administrator can change the parameter type, whether it is a **Header** or a **Body** parameter, while configuring the values.

---

## Section 4: Conditional Parameters

In the section of **Conditional Parameters**, the application has a feature to change any of the configured parameter's values by configuring a condition.

![Conditional Parameters](images/httpgw-09-conditional-parameters.png)

Conditional parameter construction is done as per the following logic:

> If `{Parameter_Key}` with the selected `{Condition}` matches the `{Current Parameter Value}`, then `{Parameter to be Modified_Key}` will be changed to `{Modified Parameter Value}`.

| Field | Description |
|-------|-------------|
| **Parameter** | The key parameter from the payload list on which the condition is to be applied. |
| **Condition** | The type of condition to be checked. |
| **Current Parameter Value** | The value of the selected parameter to be compared in the condition. |
| **Parameter To be Modified** | The key parameter from the payload list whose value will be changed if the above condition is satisfied. |
| **Modified Parameter Value** | The new value to be assigned to the key parameter if the condition is met. |

---

## Section 5: Gateway Properties

**Gateway Properties Configuration** allows the administrator to configure the method and response type supported by the vendor for the seamless operation of the HTTP gateway.

| Property | Description |
|----------|-------------|
| **Method** | Specifies the method of sending requests to the HTTP gateway. The administrator can configure the method supported by the vendor: `GET`, `POST`, or `POST Form Data`. |
| **Response Type** | The format in which the response is to be received from the gateway: `XML`, `JSON`, or `TEXT`. |
| **Stop Loss Price** | Used as the default price for the gateway when routing messages using **Blind Routing**. |
| **Is Blind Routing?** | Allows messages to be routed even if the Gateway Cost Price is not configured for the country and network. In such cases, the **Stop Loss Price** will be applied. |
| **Gateway Time Zone** | Configure the vendor's operating time zone in the application to ensure that **Delivery Receipt (DLR)** update times are recorded accurately. |
| **Is Active?** | Toggle to enable or disable the gateway. |
| **Gateway Open / Close Time** | Operational time window for the gateway in `hh:mm` format. |

![Gateway Properties — Method](images/httpgw-10-gateway-properties-method.png)

![Gateway Properties — Response Type](images/httpgw-11-gateway-properties-response.png)

---

## Section 6: Response Properties

The **Response Properties** in the application are used to **map the response** received from the gateway vendor into the reports, which are then used for updating **Delivery Receipts (DLRs)**.

Below are the types of response configuration available in the application:

### 1] JSON or XML

If the vendor supports the response type as **JSON** or **XML**, the response configuration can be set up with the following fields:

| Field | Description |
|-------|-------------|
| **Error Code Field** | The field where the error code is located in the response. |
| **MessageId Field** | The field where the message ID is located in the response. |
| **Message Status Field** | The field where the message status is located in the response. |
| **Mobile Number Field** | The field that contains the mobile number in the response. |

![Response Properties — JSON / XML](images/httpgw-12-response-properties-json.png)

### 2] TEXT

If the vendor supports the response type as **TEXT**, the administrator needs to configure additional parameters under Response Properties:

| Field | Description |
|-------|-------------|
| **Key-Value Splitter** | The delimiter used to separate and identify key-value pairs from the response. This field is only used for the TEXT response type. For example, if the response received is `ErrorCode:404`, then the splitter would be `:`. |
| **Property Splitter** | The delimiter used to separate various properties in the response. This field is also specific to the TEXT response type. |
| **Error Code Field** | Indicates the field where the error code is located in the response. |
| **MessageId Field** | Indicates the field where the message ID is located in the response. |
| **Message Status Field** | Indicates the field where the message status is located in the response. |
| **Mobile Number Field** | Used to fetch the mobile number from the response. The administrator needs to specify the field that contains the mobile number in the response. |

![Response Properties — TEXT](images/httpgw-13-response-properties-text.png)

!!! note
    In the response configuration, the administrator must configure the parameter names that store the values of the fields mentioned above.

!!! example
    Consider the following response:
    ```json
    { "data": [{
        "message_error_code": 0,
        "message_error_description": "Success",
        "mobile_number": "9174XXXXXXX",
        "message_id": "b349f1c2-5ae9-4076-867e-5fa15044b207"
    }]}
    ```
    In this JSON response:

    - The **Error Code Field** will contain the parameter name `message_error_code`.
    - The **MessageId Field** will contain the parameter name `message_id`.

When configuring response properties for a **TEXT** response, the values will be similar. Additionally, you need to specify the following:

- **Key-Value Splitter** — In the response, the value for `message_id` is `"b349f1c2-5ae9-4076-867e-5fa15044b207"`. The Key-Value Splitter is the delimiter used to separate the key from the value, which in this case is a colon (`:`). So, the Key-Value Splitter would be `:`.
- **Property Splitter** — In the response, parameters like `"message_error_description": "Success"` and `"mobile_number": "9174XXXXXXX"` are separated by a comma (`,`). Therefore, the Property Splitter to separate these parameters would be `,`.

This configuration helps map and extract the necessary fields from the response, regardless of whether the response type is JSON, XML, or TEXT.

---

## Section 7: Session

The **session** indicates the number of connections, and the recommended session for an HTTP gateway is **1**.

| Field | Recommended Value |
|-------|-------------------|
| **No. of Sessions** | `1` |

![Session configuration](images/httpgw-14-session.png)

---

## Section 8: Automatic Message Delivery

If the gateway vendor does not send **Delivery Receipts (DLRs)**, the HTTP gateway configuration includes a feature called **Automatic Delivery**. This feature allows the administrator to configure a status so that DLRs will be updated automatically.

| Field | Description |
|-------|-------------|
| **Is Automatically Marked as Delivered?** | Updates the delivery status of messages even if a DLR is not received from the gateway vendor. In this case, the **Default DLR Status** will be used. |
| **Default DLR Status** | The default delivery status assigned to messages if the automatic delivery feature is activated. It is used when the system needs to mark messages as delivered in the absence of a DLR from the gateway. Options: `DELIVRD`, `UNDELIV`, `REJECTD`, `EXPIRED`. |

![Automatic Message Delivery](images/httpgw-15-automatic-delivery.png)

!!! info "Useful for gateways that do not issue DLRs"
    Activate Automatic Delivery only when the upstream vendor genuinely never returns a DLR. Otherwise, leave it disabled so that real DLRs from the vendor drive the report.
