---
tags:
  - MO
  - Routing
  - Rules
  - Configuration
---

# MO Routing Rule

## Sinopsis

**MO Routing Rules** en iTextPro se utilizan para definir cómo los mensajes entrantes MO deben ser identificados, filtrados y enrutados dentro de la plataforma.

La regla de enrutamiento determina:

- Que tráfico entrante MO debe ser procesado
- Que palabra clave debe desencadenar el enrutamiento
- Que usuario debe recibir el tráfico MO
- Que tipo de interfaz se debe utilizar para la entrega

MO Routing Rules trabajar junto con los configurados **HTTP MO Handler**.

---

## Sendero de navegación

<span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span> ➔ <span data-ph="3"></span>.

![Manage MO Routing Rules list](images/morouting-01-list.png)

---

## MO Parámetros de Regla de Routing

Los siguientes parámetros deben configurarse al crear la regla de enrutamiento.

## Parámetros generales

### 1] Nombre de la Regla

El **Nombre de la regla** identifica de forma única la Regla de Routing MO dentro de la plataforma.

Este nombre se utiliza para:

- Gestión de las normas
- Supervisión del tráfico
- Administración
- Solución de problemas

!!! example
    ```
    MO_ROUTE_KEYWORD_01
    ```

---

### 2] Duración de la vida

El **Vida** El parámetro define la duración de validez de la regla de enrutamiento.

**Usage:**

- Se puede utilizar para campañas temporales
- Soporta la ruta MO basada en el tiempo
- Útil para servicios de tiempo limitado

!!! tip
 Si no se requiere expiración, este campo se puede dejar en blanco.

---

## Configuración de interfaz de puerta

### Handler

El **Handler** campo se utiliza para seleccionar el HTTP MO Handler previamente configurado en la plataforma.

Este manejador procesará todas las solicitudes MO que coincidan con las condiciones de enrutamiento. El manipulador se utilizará en caso de que el vendedor envíe MO con **Conexión HTTP**.

### Gateway

En caso de que el vendedor apoye **SMPP** protocolo para el envío de los golpes MO, entonces durante la creación de la Regla de Routing MO el administrador necesita seleccionar el **Gateway** y elegir la puerta de entrada correcta para buscar los golpes de la puerta correcta.

**Propósito:**

- Enlaces tráfico MO con el punto final correcto
- Asociados pudriéndose con el canal entrante
- Permite el procesamiento de mensajes

![Add New MO Rule — General Parameters & Gateway Interface](images/morouting-02-general.png)

---

## Condiciones de funcionamiento

Condiciones de rotación definen **lógica filtrante** para entrar en tráfico MO. La plataforma evalúa estas condiciones antes de procesar o enrutar la solicitud MO.

### 1] Estado de origen

El **Originator** condición define el filtrado basado en el número móvil del remitente.

**Configuración de ejemplo:** <span data-ph="0"></span>

Selección **Cualquier** permite mensajes MO de todos los números del remitente. El filtrado específico del remitente también se puede configurar si es necesario.

---

### 2] Estado de destino

El **Destino** condición define el Código Corto o el número de Código Largo.

| Campo | Valor |
|-------|-------|
| **Tipo de condición** | <span data-ph="0"></span> |
| **Ejemplo** | <span data-ph="0"></span> |

La regla de enrutamiento sólo activará si el mensaje de entrada MO se recibe en el número de destino configurado.

---

### 3] Estado del mensaje

El **Mensaje** condición define los criterios de coincidencia de palabras clave.

| Campo | Valor |
|-------|-------|
| **Tipo de condición** | <span data-ph="0"></span> |
| **Ejemplo de palabra clave** | <span data-ph="0"></span> |

La regla de enrutamiento sólo activará si el mensaje entrante comienza con la palabra clave configurada.

!!! example
 Para un mensaje entrante <span data-ph="0"></span>, ya que el mensaje comienza con <span data-ph="1"></span>, la regla de enrutamiento procesará la solicitud MO.

![Routing Conditions and User / Endpoint selection](images/morouting-03-condition-user.png)

---

## Mapping de usuario y punto final

### 1] Usuario

Seleccione **cuenta de usuario** a la que el tráfico MO debe ser mapeado y entregado.

Esta asignación asegura que el usuario correcto reciba los mensajes entrantes MO.

### 2] Tipo de interfaz de usuario

El **Tipo de interfaz de usuario** define cómo debe enviarse el mensaje MO después de la ruta.

**Tipos de interfaz compatibles:**

| Tipo | Descripción |
|------|-------------|
| **No se selecciona** | No se aplicará ningún enrutamiento específico de la interfaz. |
| **ESME** | Rutas del tráfico MO a través de conectividad SMPP. Uso general cuando el usuario está conectado a través del protocolo SMPP. |
| **Webhook** | Ruta el tráfico MO a un punto final externo HTTP API. Comúnmente utilizado para las integraciones de CRM, aplicaciones de terceros, sistemas de procesamiento basados en web y flujos de trabajo impulsados por API. |

---

## Save Routing Rule

Después de configurar todos los parámetros de enrutamiento:

1. Verifica las condiciones de enrutamiento.
2. Valida la configuración de la palabra clave.
3. Haga clic en **Guardar**.

El MO Routing Rule está ahora configurado y activo con éxito para el procesamiento de tráfico MO.

!!! tip "Verificación"
 Después de guardar la regla, envíe un mensaje MO de prueba que coincida con las condiciones configuradas (sender permitido, número de destino correcto, mensaje comenzando con la palabra clave configurada) y confirme que la regla se dispara mediante la comprobación de los registros de entrada MO del usuario o webhook.
