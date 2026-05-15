---
tags:
  - Monitoring
  - HTTP
  - Gateway
  - Logs
---

# HTTP Gateway Logs

**Navegación:** <span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span>.

## Sinopsis

El **HTTP Gateway Logs** sección permite a los administradores ver el HTTP completo **solicitud** y **respuesta** comunicación intercambiada entre la aplicación PowerSMPP y los proveedores de puerta configurados. Estos registros son esenciales para diagnosticar fallos de entrega, verificar las cargas de pago de API y auditar interacciones de gateway.

---

## Pasos para ver los registros

1. Seleccione **HTTP Gateway** de la **Nombre de la puerta** desplegable.
2. Seleccione el requisito **Fecha de rango** usando el selector de citas.
3. Elija el **Tipo de registro** ()<span data-ph="0"></span> / <span data-ph="1"></span> / <span data-ph="2"></span>Como sea necesario.
4. Seleccione **Verbosidad** nivel si se requiere filtrado granular.
5. Haga clic **Submit** para buscar y mostrar los registros coincidentes.

![HTTP Gateway Logs — Log list view](images/httplogs-01-list.png)

---

## Secciones de registro disponibles

### Solicitud

El **Solicitud** contiene la carga útil completa transmitida desde la aplicación PowerSMPP al proveedor de la puerta de entrada.

![HTTP Gateway Logs — Request Body expanded](images/httplogs-02-request-body.png)

!!! info "Cuerpo de solicitud - Datos incluidos"
    - **Número de móvil** — número de destino del SMS
    - **ID del remitente** — la dirección originaria / ID de remitente utilizado
    - **Solicitar parámetros** — parámetros completos de API enviados a la puerta de entrada
    - **Host / IP Details** — Dirección IP y puerto de la puerta de entrada
    - **Tiempo de presentación** - horarios de envío de la solicitud

### Response Body

El **Response Body** contiene los datos de reconocimiento y estado recibidos del proveedor de la puerta de entrada.

![HTTP Gateway Logs — Response Body expanded](images/httplogs-03-response-body.png)

!!! info "Órgano de respuesta — Datos incluidos"
    - **Gateway Response** — respuesta cruda devuelta por la puerta
    - **Información sobre el estado** — códigos de estado de entrega o aceptación
    - **Detalles del error** — códigos y descripciones de errores para comunicaciones fallidas
    - **Reconocimiento de la respuesta** — confirmación de que el portal tramitó la solicitud

---

## Opciones de filtro

Los administradores pueden refinar la vista de registro utilizando los siguientes filtros adicionales:

| Filtro | Uso |
|--------|-----|
| **Dirección IP** | Registros de filtro por el servidor de gateway IP. |
| **ID del remitente** | Registros de filtro por origen Sender ID. |
| **Número de móvil** | Registros de filtro por número móvil de destino. |

---

## Flujo típico de solución de problemas

1. Una campaña reporta fracasos inesperados o mensajes no entregados.
2. Abierto **HTTP Gateway Logs**, seleccione la puerta de entrada afectada y un rango de fecha que cubre el problema.
3. Set **Tipo de registro** a <span data-ph="0"></span> a la superficie sólo fallaron los intercambios.
4. Ampliar el **Solicitud** para confirmar que la carga de pago de salida era correcta.
5. Ampliar el **Response Body** para leer el código de error/descripción real devuelto por el proveedor.
6. Uso **Dirección IP**, **ID del remitente**o **Número de móvil** filtros para aislar una muestra de prueba específica para el equipo de soporte del proveedor.
