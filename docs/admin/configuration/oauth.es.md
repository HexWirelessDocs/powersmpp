---
tags:
  - HTTP
  - OAuth
  - Handler
  - Configuration
---

# OAuth Handler Configuration

In **HTTP Gateway**, apoyamos **3 tipos de autorización**:

| # | Tipo | Descripción |
|---|------|-------------|
| 1 | **No Auth** | No se requiere autorización. |
| 2 | **Auxilio básico** | Se requiere un nombre de usuario y contraseña para la autenticación segura de la API. |
| 3 | **OAuth 2.0** | La última versión de autorización, utilizada para regenerar nuevas credenciales después de un determinado período para mantener la alta seguridad de la API utilizando la **OAuth Handler** API. |

En este documento, explicaremos todos los pasos e información necesarios para el **OAuth Handler** configuración para el HTTP Gateway.

---

## Navegación

<span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span> ➔ <span data-ph="3"></span>.

---

## OAuth Handler Fields

| Campo | Necesario | Descripción |
|-------|----------|-------------|
| **Nombre** | Sí. | Un nombre fácil para el manipulador OAuth. Ayuda a identificar y gestionar fácilmente diferentes controladores OAuth dentro de la aplicación. |
| **Token URL** | Sí. | El punto final de URL donde la aplicación solicitará el token OAuth. Es la URL proporcionada por el vendedor para obtener la ficha de acceso. |
| **Tiempo de explotación** | Sí. | La duración en minutos para los cuales el acceso a la ficha seguirá siendo válida. Después de este período, la ficha expirará, y será necesario generar una nueva. |
| **Token Expiry Code** | Sí. | El código de error indica que la ficha ha expirado. Cuando se reciba este código de error, el sistema sabrá que necesita refrescar la ficha. |
| **Método de solicitud** | Sí. | El método HTTP utilizado para solicitar la ficha de la URL Token — <span data-ph="0"></span> o <span data-ph="1"></span>. |
| **Tipo de respuesta** | Sí. | El formato en el que se recibirá la respuesta de la URL Token <span data-ph="0"></span>, <span data-ph="1"></span>o <span data-ph="2"></span>. |
| **Access Token Field** | Facultativo | El nombre de campo en la respuesta que contiene el token de acceso. El sistema extraerá la ficha de acceso de este campo para autenticar futuras solicitudes. |
| **Refresh Token Field** | Facultativo | El nombre de campo en la respuesta que contiene el token refrescante. El token refrescante se utiliza para obtener un nuevo token de acceso cuando el actual expira. Este campo es opcional dependiendo de la implementación del proveedor. |

---

## Carga

Esta sección permite al administrador definir **pares adicionales de valor clave** que debe ser enviado junto con la solicitud de señalización.

| Campo | Descripción |
|-------|-------------|
| **KEY** | El nombre del parámetro que se incluirá en la solicitud. |
| **VALOR** | El valor del parámetro que se incluirá en la solicitud. |
| **PARAM TYPE** | Especifica el tipo de parámetro. Tipos de parámetro comunes incluyen <span data-ph="0"></span>, <span data-ph="1"></span>, etc. |

!!! example
    - **KEY**: <span data-ph="0"></span>
    - **VALOR**: <span data-ph="0"></span>
    - **PARAM TYPE**: <span data-ph="0"></span> *(indicando que este parámetro se incluirá en el cuerpo de la solicitud de ficha)*

Esta configuración ayuda a configurar **autenticación OAuth** para acceder a APIs mediante la automatización del proceso de obtención y actualización de fichas.

---

## Cómo funciona

1. Cuando un mensaje necesita ser enviado a través de una pasarela HTTP que utiliza **OAuth 2.0**, Power SMPP primero comprueba si un token de acceso válido (no utilizado) ya está en caché.
2. Si existe un token válido, se adjunta a la llamada API de salida (típicamente a través de una <span data-ph="0"></span> cabecera).
3. Si no existe un token válido, o el token ha caducado y configurado **Token Expiry Code** es devuelto por la puerta de entrada - Power SMPP llama a la **Token URL** con el configurado <span data-ph="0"></span>, <span data-ph="1"></span>, y <span data-ph="2"></span> pares.
4. La respuesta se analiza utilizando la **Tipo de respuesta**, el **Access Token Field** es extraído, y el token es caché para la duración de **Tiempo de explotación**.
5. Las solicitudes de mensajes de salida utilizan ahora el token recién obtenido hasta que caduca de nuevo.

---

## Enlace al Handler OAuth a una puerta HTTP

Después de salvar el Handler OAuth:

1. Abra la puerta HTTP que desea asegurar con OAuth.
2. Under **Sección 1: Credenciales requeridos**, set **Autenticación** a **OAuth 2.0**.
3. Desde **OAuth Handler** desplegable, elige el manejador que acabas de crear.
4. Guarda la entrada.

El HTTP Gateway utilizará ahora el OAuth Handler configurado para obtener y actualizar las fichas automáticamente, sin necesidad de rotación manual.

!!! tip
 Manténganse. **Tiempo de explotación** ligeramente más corto que el valor anunciado por el vendedor (por ejemplo, conjunto <span data-ph="0"></span> minutos si las fichas del vendedor duran <span data-ph="1"></span> minutos). Esto evita las condiciones de carrera donde la primera solicitud después de que el vencimiento falla antes de que se active el refresco.
