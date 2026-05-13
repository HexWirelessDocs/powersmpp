---
tags:
  - HTTP
  - Gateway
  - Configuration
---

# HTTP Gateway

In **Power SMPP**, apoyamos ambos **SMPP** y **HTTP** protocolos para conectividad de proveedores. En consecuencia, el administrador tiene la opción de configurar una puerta de entrada basada en SMPP o una puerta de entrada HTTP. Este documento proporciona un panorama conciso de la configuración de la puerta de entrada HTTP. Está diseñado para ayudar a los administradores a entender y establecer una puerta de entrada HTTP dentro de la aplicación Power SMPP con facilidad.

Como el nombre sugiere, la puerta de entrada HTTP se basa en la **Protocolo de transferencia de hipertexto (HTTP)**. Este protocolo permite a los clientes enviar mensajes a través de una API que actúa como puerta de entrada dentro de la aplicación Power SMPP.

![Manage Gateway list view](images/httpgw-01-manage-gateway.png)

**Navegación:** <span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span> ➔ <span data-ph="3"></span> ➔ <span data-ph="4"></span>.

![HTTP Gateway Detail sections](images/httpgw-02-detail-sections.png)

!!! tip "Ver documentación"
 Al hacer clic en **Añadir nuevo**, la primera opción será **Ver documentación**. Recomendamos que el administrador revise este documento para familiarizarse con los términos mencionados en la configuración de la puerta de entrada.

La pantalla HTTP Gateway Detail se organiza en las siguientes secciones:

- Credenciales necesarias
- Tipos de mensaje
- Parámetros
- Parámetros condicionales
- Gateway Properties
- Propiedades de respuesta
- Período de sesiones
- Entrega automática de mensajes

---

## Sección 1: Credenciales requeridos

En esta sección se requieren varias informaciones, como **Nombre de la puerta**, **Tipo de solicitud**, **Autenticación**, **Base URL**, y **UDH**.

**Nombre de la puerta** — Un nombre fácil de recordar para el portal HTTP.

**¿Es necesaria la UDH?** - Especifica si **UDH (User Data Header)** es necesario para los mensajes enviados desde esta entrada. La UDH se utiliza para mensajes concatenados.

**Tipo de solicitud** — Especifica el tipo de solicitud HTTP. Podría ser **HTTP simple**, **REST/JSON**o **SOAP**. Los diferentes tipos de solicitud requieren diferentes configuraciones. Generalmente, Simple HTTP se utiliza para <span data-ph="0"></span> métodos, mientras que REST/JSON se puede utilizar para ambos <span data-ph="1"></span> y <span data-ph="2"></span> métodos.

![Required Credentials form](images/httpgw-03-required-credentials.png)

**Base URL Detalle** — Especifica la URL base para la API HTTP, **excluyendo** todos los otros parámetros.

!!! example
 Si la URL de API es <span data-ph="0"></span>, entonces la URL de Base debe configurarse como <span data-ph="1"></span>.

**Autenticación** — Power SMPP actualmente apoya tres tipos de autorización:

| # | Tipo | Descripción |
|---|------|-------------|
| 1 | **No Auth** | No se requiere autorización. |
| 2 | **Auxilio básico** | Se requiere un nombre de usuario y contraseña para la autenticación segura de la API. |
| 3 | **OAuth 2.0** | La última versión de autorización, utilizada para regenerar nuevas credenciales después de un determinado período para mantener la alta seguridad de la API utilizando la **OAuth Handler** API. |

![Authentication options](images/httpgw-04-authentication.png)

---

## Sección 2: Tipos de mensaje

**Tipo de mensaje** es una sección opcional donde el administrador puede configurar el valor de codificación de datos aceptado por el proveedor. Los valores predeterminados de cada tipo de codificación de datos se mencionan entre corchetes.

| Tipo | Default | Propósito |
|------|---------|---------|
| **TEXTO** | <span data-ph="0"></span> | Mapping the gateway-specific message type for plain text messages. |
| **UNICODE** | <span data-ph="0"></span> | Mapping the gateway-specific message type for Unicode messages. |
| **BINARY** | <span data-ph="0"></span> | Mapping the gateway-specific message type for binario messages. |
| **FLASH** | <span data-ph="0"></span> o <span data-ph="1"></span> | Mapping the gateway-specific message type for flash messages. |

!!! note
 Mapee los tipos de mensajes específicos de la puerta de entrada con tipos de mensajes del sistema. Deje los campos en blanco si no es aplicable.

![Message Types form](images/httpgw-05-message-types.png)

---

## Sección 3: Parámetros

El **Parámetro** sección permite al administrador configurar los detalles de la puerta de entrada y los parámetros de solicitud proporcionados por el proveedor de la puerta de entrada. Estos parámetros son utilizados por Power SMPP para construir y transmitir los datos/cuerpo de solicitud de API al respectivo proveedor de portales para el procesamiento y entrega de mensajes.

Los parámetros configurados definen cómo se generará y ejecutará la solicitud HTTP durante la comunicación API.

### Método

Power SMPP admite los siguientes métodos HTTP para la ejecución de API:

#### 1] GET Method

El método GET permite al administrador configurar los parámetros de solicitud en **par de valor clave** formato. Durante la ejecución de API, todos los parámetros configurados se adjuntan directamente a la URL como **parámetros de consulta**.

Este método se utiliza generalmente para:

- Solicitudes sencillas de API
- Transmisión de parámetro basada en URL
- Integraciones de API de peso ligero
- Integraciones de HTTP Legacy

!!! example
 <span data-ph="0"></span>

En el método GET, Power SMPP admite los siguientes tipos de parámetro:

##### Nombre del pariente

El **Nombre del pariente** el campo se utiliza principalmente para **SOAP-based** Integraciones de API donde los parámetros deben agruparse bajo un nodo XML padre o objeto de solicitud.

Esta configuración ayuda a generar cargas de pago de solicitud estructuradas SOAP según la especificación de la API del proveedor.

!!! example
    ```xml
    <SendSMS>
        <username>admin</username>
        <password>test123</password>
    </SendSMS>
    ```
 En el ejemplo anterior, <span data-ph="0"></span> actúa como el Nombre del Padre.

##### Parámetro del encabezado

El **Parámetro del encabezado** se utiliza para configurar los valores de encabezado HTTP requeridos durante la ejecución de API.

Estos parámetros se utilizan generalmente para:

- Authentication Tokens
- API Keys
- Credenciales de autorización
- Definiciones del tipo de contenido
- Responsables de proveedores personalizados

!!! example
    ```
    Authorization: Bearer xxxxx
    Content-Type: application/json
    ```

Los parámetros de encabezado se transmiten dentro del encabezado de solicitud HTTP durante la comunicación API.

##### Parámetro del cuerpo

El **Parámetro del cuerpo** sección contiene todos los parámetros de solicitud general requeridos para la solicitud HTTP API.

Estos parámetros suelen incluir:

- Número de móvil
- Contenido del mensaje
- ID del remitente
- ID de plantilla
- ID de Entidad
- Parámetros de rotación
- Parámetros de proveedores personalizados

Para **#** solicitudes, estos parámetros se adjuntan dentro de la URL de solicitud como parámetros de consulta durante la ejecución de API.

![Parameters configuration with example rows](images/httpgw-06-parameters.png)

#### 2) Método POST

El **POST** método permite al administrador configurar la puerta de entrada enviando todos los parámetros de solicitud requeridos dentro del **petición del cuerpo** en lugar de gastarlos en la URL. Este método se recomienda para las integraciones de API donde se requieren grandes cantidades de datos, parámetros de autenticación, encabezados, fichas o estructuras complejas de carga útil.

Utilizando el método POST ofrece las siguientes ventajas:

- Reduce la longitud y complejidad de la URL.
- Mejora la seguridad evitando la exposición de información sensible en la URL.
- Soporta datos estructurados y grandes de carga útil.
- Permite compatibilidad con integraciones avanzadas de API.
- Permite el formato flexible del cuerpo de solicitud basado en los requisitos de API.

La carga útil configurada se transmite en el cuerpo de solicitud HTTP durante la ejecución de API.

##### Tipo de carga

Al seleccionar el método POST, el administrador puede configurar la carga útil de solicitud utilizando uno de los siguientes tipos de carga útil:

###### I] Parámetro de valor clave [POST FORM DATA]

Esta opción permite al administrador configurar la carga útil de la solicitud en un estándar **parámetro key-value** formato, donde cada parámetro se define por separado utilizando un nombre de campo y el valor correspondiente.

Este tipo de carga útil es adecuado para APIs que aceptan:

- Datos del formulario
- Parámetros cifrados de URL
- Órganos de solicitud estructurados simples

!!! example
    ```
    Key        Value
    username   admin
    password   test123
    senderid   ABCDEF
    ```

**Beneficios:**

- Fácil de configurar y gestionar.
- Adecuado para integraciones sencillas de API.
- Permite la asignación dinámica del parámetro.
- Simplifica validación de solicitudes y solución de problemas.

![POST Form Data Key-Value parameters](images/httpgw-07-post-form-data.png)

###### II] RAW Payload

Esta opción permite que el administrador pase **cuerpo de solicitud completo** directamente como contenido bruto sin definir los parámetros individuales de valor clave por separado.

El método RAW Payload se utiliza principalmente cuando la API de destino requiere:

- JSON Payload
- Carga XML
- Carga de texto simple
- Datos estructurados personalizados

El administrador puede pegar directamente o configurar el contenido de carga útil completo exactamente según lo requerido por la API de destino.

**Formatos de carga de RAW compatibles:** <span data-ph="0"></span>, <span data-ph="1"></span>, <span data-ph="2"></span>.

!!! example "JSON Payload"
    ```json
    {
      "username": "admin",
      "password": "test123",
      "senderid": "ABCDEF"
    }
    ```

**Beneficios:**

- Soporta estructuras de carga útil complejas y anidadas.
- Permite una integración perfecta con API REST modernas.
- Proporciona flexibilidad para formatos personalizados de solicitud API.
- Permite el control directo sobre la estructura de carga útil y el formato.

![RAW JSON payload editor](images/httpgw-08-raw-payload.png)

En Power SMPP, el administrador puede definir **propietarios de puestos** para diversos valores, como <span data-ph="0"></span> para la identificación del remitente, <span data-ph="1"></span> para el contenido de texto, <span data-ph="2"></span> para el destino, y muchos más. Esto permite al administrador configurar varios valores dinámicos para los parámetros. Además, el administrador puede cambiar el tipo de parámetro, si es un **Header** o a **Cuerpo** parámetro, mientras que configuración los valores.

---

## Sección 4: Parámetros condicionales

En la sección de **Parámetros condicionales**, la aplicación tiene una función para cambiar cualquiera de los valores del parámetro configurado mediante la configuración de una condición.

![Conditional Parameters](images/httpgw-09-conditional-parameters.png)

La construcción del parámetro condicional se realiza según la lógica siguiente:

> Si <span data-ph="0"></span> con el seleccionado <span data-ph="1"></span> partidos <span data-ph="2"></span>Entonces <span data-ph="3"></span> será cambiado <span data-ph="4"></span>.

| Campo | Descripción |
|-------|-------------|
| **Parámetro** | El parámetro clave de la lista de carga útil en la que se aplicará la condición. |
| **Estado** | El tipo de condición a revisar. |
| **Valor del parámetro actual** | El valor del parámetro seleccionado para ser comparado en la condición. |
| **Parámetro a ser modificado** | El parámetro clave de la lista de carga útil cuyo valor será cambiado si la condición anterior está satisfecha. |
| **Valor del parámetro modificado** | El nuevo valor que se asignará al parámetro clave si se cumple la condición. |

---

## Sección 5: Propiedades de puerta de entrada

**Configuración de propiedades de puerta** permite al administrador configurar el método y el tipo de respuesta apoyado por el proveedor para el funcionamiento sin fisuras de la pasarela HTTP.

| Propiedad | Descripción |
|----------|-------------|
| **Método** | Especifica el método de envío de solicitudes a la puerta de entrada HTTP. El administrador puede configurar el método compatible con el proveedor: <span data-ph="0"></span>, <span data-ph="1"></span>o <span data-ph="2"></span>. |
| **Tipo de respuesta** | El formato en el que la respuesta debe ser recibida de la puerta de entrada: <span data-ph="0"></span>, <span data-ph="1"></span>o <span data-ph="2"></span>. |
| **Stop Loss Price** | Utilizado como el precio predeterminado de la puerta de entrada cuando se utilizan mensajes de enrutamiento **Blind Routing**. |
| **¿Blind Routing?** | Permite que los mensajes sean enrutados incluso si el precio del coste de la puerta no está configurado para el país y la red. En esos casos, **Stop Loss Price** se aplicará. |
| **Gateway Time Zone** | Configurar la zona de tiempo de operación del vendedor en la aplicación para asegurar que **Recibo de entrega (DLR)** Los tiempos de actualización se registran con precisión. |
| **¿Es Activo?** | Toggle para habilitar o desactivar la puerta de entrada. |
| **Gateway Open / Close Time** | Ventana de tiempo operacional para la entrada <span data-ph="0"></span> formato. |

![Gateway Properties — Method](images/httpgw-10-gateway-properties-method.png)

![Gateway Properties — Response Type](images/httpgw-11-gateway-properties-response.png)

---

## Sección 6: Propiedades de respuesta

El **Propiedades de respuesta** en la aplicación se utilizan para **mapa de la respuesta** recibido del proveedor de la puerta de entrada en los informes, que luego se utilizan para actualizar **Receipts de entrega (DLRs)**.

A continuación se presentan los tipos de configuración de respuesta disponibles en la aplicación:

### 1] JSON o XML

Si el proveedor apoya el tipo de respuesta como **JSON** o **XML**, la configuración de respuesta se puede configurar con los siguientes campos:

| Campo | Descripción |
|-------|-------------|
| **Código de error** | El campo donde el código de error se encuentra en la respuesta. |
| **Campo MessageId** | El campo donde el ID de mensaje se encuentra en la respuesta. |
| **Campo de estado del mensaje** | El campo donde el estado del mensaje se encuentra en la respuesta. |
| **Número de móvil** | El campo que contiene el número móvil en la respuesta. |

![Response Properties — JSON / XML](images/httpgw-12-response-properties-json.png)

### 2] TEXTO

Si el proveedor apoya el tipo de respuesta como **TEXTO**, el administrador necesita configurar parámetros adicionales bajo Propiedades de Respuesta:

| Campo | Descripción |
|-------|-------------|
| **Divisor de valor clave** | El delimitador utilizó para separar e identificar pares de valor clave de la respuesta. Este campo solo se utiliza para el tipo de respuesta TEXT. Por ejemplo, si la respuesta recibida es <span data-ph="0"></span>, entonces el separador sería <span data-ph="1"></span>. |
| **Divisor de propiedad** | El delimitador utilizó para separar varias propiedades en la respuesta. Este campo también es específico para el tipo de respuesta TEXT. |
| **Código de error** | Indica el campo donde se encuentra el código de error en la respuesta. |
| **Campo MessageId** | Indica el campo donde se encuentra el ID de mensaje en la respuesta. |
| **Campo de estado del mensaje** | Indica el campo donde se encuentra el estado del mensaje en la respuesta. |
| **Número de móvil** | Solía buscar el número móvil de la respuesta. El administrador necesita especificar el campo que contiene el número móvil en la respuesta. |

![Response Properties — TEXT](images/httpgw-13-response-properties-text.png)

!!! note
 En la configuración de respuesta, el administrador debe configurar los nombres de parámetros que almacenan los valores de los campos mencionados anteriormente.

!!! example
 Considerar la siguiente respuesta:
    ```json
    { "data": [{
        "message_error_code": 0,
        "message_error_description": "Success",
        "mobile_number": "9174XXXXXXX",
        "message_id": "b349f1c2-5ae9-4076-867e-5fa15044b207"
    }]}
    ```
 En esta respuesta de JSON:

    - El **Código de error** contendrá el nombre del parámetro <span data-ph="0"></span>.
    - El **Campo MessageId** contendrá el nombre del parámetro <span data-ph="0"></span>.

Al configurar las propiedades de respuesta para un **TEXTO** respuesta, los valores serán similares. Además, debe especificar lo siguiente:

- **Divisor de valor clave** - En la respuesta, el valor <span data-ph="0"></span> es <span data-ph="1"></span>. El Divisor Key-Value es el delimitador utilizado para separar la clave del valor, que en este caso es un colon (<span data-ph="2"></span>). Entonces, el Splitter de Valor Clave sería <span data-ph="3"></span>.
- **Divisor de propiedad** — En la respuesta, parámetros como <span data-ph="0"></span> y <span data-ph="1"></span> están separados por un coma (<span data-ph="2"></span>). Por lo tanto, el Divisor de Propiedad para separar estos parámetros sería <span data-ph="3"></span>.

Esta configuración ayuda a mapear y extraer los campos necesarios de la respuesta, independientemente de si el tipo de respuesta es JSON, XML o TEXT.

---

## Sección 7: período de sesiones

El **período de sesiones** indica el número de conexiones, y la sesión recomendada para una puerta HTTP es **1**.

| Campo | Valor recomendado |
|-------|-------------------|
| **Número de sesiones** | <span data-ph="0"></span> |

![Session configuration](images/httpgw-14-session.png)

---

## Sección 8: Entrega automática de mensajes

Si el vendedor de la puerta de entrada no envía **Receipts de entrega (DLRs)**, la configuración de entrada HTTP incluye una función llamada **Entrega automática**. Esta función permite al administrador configurar un estado para que los DLR se actualicen automáticamente.

| Campo | Descripción |
|-------|-------------|
| **¿Se marca automáticamente como se entrega?** | Actualiza el estado de entrega de mensajes incluso si un DLR no es recibido del proveedor de la puerta de entrada. En este caso, el **Default DLR Status** será usado. |
| **Default DLR Status** | El estado de entrega predeterminado asignado a los mensajes si la función de entrega automática está activada. Se utiliza cuando el sistema necesita marcar mensajes tal como se entrega en ausencia de un DLR desde la entrada. Opciones: <span data-ph="0"></span>, <span data-ph="1"></span>, <span data-ph="2"></span>, <span data-ph="3"></span>. |

![Automatic Message Delivery](images/httpgw-15-automatic-delivery.png)

!!! info "Útil para puertas que no emiten DLRs"
 Activar la entrega automática sólo cuando el vendedor de corriente superior realmente nunca devuelve un DLR. De lo contrario, déjelo desactivado para que los DLR reales del proveedor conduzcan el informe.
