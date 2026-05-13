---
tags:
  - HTTP
  - OAuth
  - Handler
  - Configuration
---

# OAuth Handler Configuration

In **HTTP Gateway**, we support **3 types of Authorization**:

| # | Type | Description |
|---|------|-------------|
| 1 | **No Auth** | No authorization is required. |
| 2 | **Basic Auth** | A username and password are required for secure authentication of the API. |
| 3 | **OAuth 2.0** | The latest version of authorization, used to regenerate new credentials after a certain period to maintain high security of the API using the **OAuth Handler** API. |

In this document, we will explain all the steps and information which is required for the **OAuth Handler** configuration for the HTTP Gateway.

---

## Navigation

`Configuration` ➔ `Gateway Configuration` ➔ `OAuth Handlers` ➔ `Add New`.

---

## OAuth Handler Fields

| Field | Required | Description |
|-------|----------|-------------|
| **Name** | Yes | A user-friendly name for the OAuth handler. It helps in easily identifying and managing different OAuth handlers within the application. |
| **Token URL** | Yes | The URL endpoint where the application will request the OAuth token. It is the URL provided by the vendor to obtain the access token. |
| **Expiry Time** | Yes | The duration in minutes for which the access token will remain valid. After this period, the token will expire, and a new one will need to be generated. |
| **Token Expiry Code** | Yes | The error code indicating that the token has expired. When this error code is received, the system will know it needs to refresh the token. |
| **Request Method** | Yes | The HTTP method used to request the token from the Token URL — `GET` or `POST`. |
| **Response Type** | Yes | The format in which the response from the Token URL will be received — `JSON`, `XML`, or `TEXT`. |
| **Access Token Field** | Optional | The field name in the response that contains the access token. The system will extract the access token from this field to authenticate future requests. |
| **Refresh Token Field** | Optional | The field name in the response that contains the refresh token. The refresh token is used to obtain a new access token when the current one expires. This field is optional depending on the vendor's implementation. |

---

## Payload

This section allows the administrator to define **additional key-value pairs** that need to be sent along with the token request.

| Field | Description |
|-------|-------------|
| **KEY** | The name of the parameter to be included in the request. |
| **VALUE** | The value of the parameter to be included in the request. |
| **PARAM TYPE** | Specifies the type of parameter. Common parameter types include `BodyParameter`, `HeaderParameter`, etc. |

!!! example
    - **KEY**: `client_id`
    - **VALUE**: `your_client_id`
    - **PARAM TYPE**: `BodyParameter` *(indicating that this parameter will be included in the body of the token request)*

This configuration helps in setting up **OAuth authentication** for accessing APIs by automating the process of obtaining and refreshing tokens.

---

## How It Works

1. When a message needs to be sent through an HTTP Gateway that uses **OAuth 2.0**, Power SMPP first checks whether a valid (non-expired) access token is already cached.
2. If a valid token exists, it is attached to the outbound API call (typically via an `Authorization: Bearer <token>` header).
3. If no valid token exists — or the token has expired and the configured **Token Expiry Code** is returned by the gateway — Power SMPP calls the **Token URL** with the configured `Request Method`, `Payload`, and `KEY/VALUE` pairs.
4. The response is parsed using the **Response Type**, the **Access Token Field** is extracted, and the token is cached for the duration of **Expiry Time**.
5. Outbound message requests now use the newly obtained token until it expires again.

---

## Linking the OAuth Handler to an HTTP Gateway

After saving the OAuth Handler:

1. Open the HTTP Gateway you wish to secure with OAuth.
2. Under **Section 1: Required Credentials**, set **Authentication** to **OAuth 2.0**.
3. From the **OAuth Handler** dropdown, choose the handler you just created.
4. Save the gateway.

The HTTP Gateway will now use the configured OAuth Handler to obtain and refresh tokens automatically — no manual token rotation is required.

!!! tip
    Keep the **Expiry Time** slightly shorter than the value advertised by the vendor (for example, set `55` minutes if the vendor's tokens last `60` minutes). This avoids race conditions where the first request after expiry fails before the refresh is triggered.
