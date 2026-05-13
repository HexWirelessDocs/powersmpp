---
tags:
  - HTTP
  - MO
  - Handler
  - Configuration
---

# HTTP MO Handler

## Sinopsis

El **HTTP MO Handler** en iTextPro se utiliza para recibir y procesar la entrada **MO (Mobile Originated)** mensajes de operadores de telecomunicaciones o proveedores de portales. El manejador actúa como un punto final de API que acepta las solicitudes MO y envía los datos recibidos a la plataforma para seguir enrutándose y procesando.

La configuración HTTP MO Handler define:

- Método de comunicación
- Detalles del canal
- Cartografía de carga
- Restricciones de seguridad
- Endpoint generation

!!! warning "Prerrequisito"
 Esta configuración es **obligatorio** antes de crear MO Routing Rules.

---

## Sendero de navegación

<span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span>.

![Manage MO Handler list](images/mohandler-01-list.png)

---

## Parámetros de configuración del manipulador

Los siguientes parámetros deben configurarse al crear un HTTP MO Handler.

### 1] Nombre del manipulador

El **Nombre del administrador** se utiliza para identificar la configuración MO Handler dentro de la plataforma.

Este nombre se utiliza internamente para:

- Configuración de rotación
- Selección de personal
- Mapa de tráfico
- Administración y solución de problemas

!!! example
    ```
    MO_HANDLER_INDIA_01
    ```

---

### 2] Tipo de canal

El **Tipo de canal** define el tipo de número de telecomunicaciones asociado con el tráfico MO entrante.

**Tipos de canal compatibles:**

| Tipo | Descripción |
|------|-------------|
| **Long Code** | Un número móvil estándar utilizado para la comunicación de mensajería bidireccional. |
| **Código** | Un código numérico corto generalmente utilizado para campañas empresariales, sistemas de votación, suscripciones o servicios promocionales. |

El tipo de canal seleccionado debe coincidir con la configuración del operador o proveedor.

![Manage MO Handler — full configuration form](images/mohandler-02-add-new.png)

---

### 3] Número de canales

El **Número de canal** representa el número de destino real sobre el cual se recibirá el tráfico MO.

!!! example
    ```
    567890
    ```

Este número debe configurarse **exactamente según lo dispuesto** por el operador de telecomunicaciones o vendedor de portones.

---

### 4] Local Endpoint

El **Local Endpoint** se genera automáticamente por iTextPro una vez que se crea la configuración del controlador.

Este punto final actúa como la URL receptora para recibir solicitudes HTTP MO.

La URL generada de endpoint se comparte generalmente con:

- Proveedores SMS Gateway
- Operadores de Telecom
- Aggregadores
- Plataformas de terceros

El proveedor utiliza este punto final para empujar mensajes entrantes en la plataforma iTextPro.

**Flujo de ejemplo:**

```
Operator/Vendor → Local Endpoint → iTextPro Processing
```

---

### 5] Whitelist IP

El **Whitelist IP** la sección se utiliza para asegurar el punto final MO restringiendo el acceso sólo a direcciones IP autorizadas.

Sólo las solicitudes recibidas de direcciones IP configuradas serán aceptadas por la plataforma.

**Propósito:**

- Prevención del acceso no autorizado
- Mejorar la seguridad de la API
- Restringir el tráfico desconocido
- Proteger el punto final MO de uso indebido

!!! example
    ```
    192.168.10.20
    ```

!!! tip
 Múltiples IPs se pueden configurar según los requisitos operativos.

---

### 6] Método

El **Método** define el método de comunicación HTTP utilizado por el proveedor al enviar solicitudes MO.

**Métodos respaldados:** <span data-ph="0"></span>, <span data-ph="1"></span>.

#### Método

En el método GET:

- Los parámetros se transmiten dentro de la URL.
- Los datos se envían como parámetros de consulta.
- Adecuado para integraciones ligeras.

!!! example
    ```
    https://domain.com/mo?originator=9876543210&destination=567890&message=TEST
    ```

#### POST Method

En el método POST:

- Los parámetros se transmiten dentro del cuerpo de solicitud HTTP.
- Apoya cargas de pago estructuradas y grandes.
- Comúnmente utilizado para las integraciones modernas de API.

**Beneficios:**

- Mejor seguridad
- Estructura de solicitud de limpieza
- Admite cargas de pago JSON / XML
- Adecuado para integraciones complejas

---

## Configuración de carga

El **Carga** sección define cómo los parámetros de solicitud entrante se mapean dentro de iTextPro.

Cartografía correcta de la carga útil **obligatorio** para el procesamiento exitoso de MO. Configure los parámetros de carga útil exactamente como se menciona a continuación:

| Parámetro de la plataforma | Parámetro de proveedores |
|--------------------|------------------|
| **Originator** | <span data-ph="0"></span> |
| **Destino** | <span data-ph="0"></span> |
| **Mensaje** | <span data-ph="0"></span> |

### Parámetro de carga

#### Originator

El **Originator** El parámetro representa el número móvil del remitente desde el que se recibe el mensaje MO.

!!! example
    ```
    9876543210
    ```

#### Destino

El **Destino** El parámetro representa el **Código** o **Long Code** número en el que se envió el mensaje MO.

!!! example
    ```
    567890
    ```

#### Mensaje

El **Mensaje** El parámetro representa el contenido de texto actual presentado por el usuario final.

!!! example
    ```
    ASKRK BALANCE
    ```

---

## Guardar configuración de Handler

Después de completar todas las configuraciones:

1. Verifique todos los detalles configurados.
2. Haga clic en **Guardar**.

El HTTP MO Handler ahora está configurado y listo para recibir tráfico MO.

!!! tip "Siguiente paso"
 Una vez que se guarda el manejador, proceder a crear un **MO Routing Rule** para definir cómo el tráfico entrante MO será filtrado y entregado a los usuarios finales.
