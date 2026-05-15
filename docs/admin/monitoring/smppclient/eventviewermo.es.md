---
tags:
  - Monitoring
  - MO
  - Event Viewer
---

# Event Viewer (MO) — Mobile Originated

**Navegación:** <span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span>.

## Sinopsis

El **Event Viewer (MO)** sección se utiliza para monitorear **Origen móvil (MO)** mensajes y eventos del sistema relacionados dentro de PowerSMPP. Los mensajes MO son mensajes de entrada recibidos de un proveedor de puerta o usuario final dirigido hacia la aplicación.

---

## Propósito

El Event Viewer (MO) ayuda a los administradores a monitorear, auditar y resolver toda la actividad relacionada con MO entrante en el sistema.

!!! info "Casos de uso primario"
    - Monitorización de la actividad de mensajes MO en tiempo real
    - Comprobación de registros de comunicación del usuario entrante o del vendedor
    - Solución de problemas relacionados con la entrega o el enrutamiento
    - Revisión de los eventos generados por el sistema
    - Registros de comunicación de portales verificadores para el tráfico de entrada

---

## Información disponible

El módulo muestra los siguientes campos para cada entrada de registro:

| Campo | Descripción |
|-------|-------------|
| **Hora** | Exact timestamp of the MO event. |
| **Tipo de registro** | Clasificación del evento — <span data-ph="0"></span> o <span data-ph="1"></span>. |
| **Mensaje** | Descripción del evento o actividad MO. |

![Event Viewer (MO) — Info log entries](images/eventmo-01-info.png)

![Event Viewer (MO) — Error log type (no entries shown)](images/eventmo-02-error.png)

---

## Tipos de registro

| Tipo de registro | Descripción |
|----------|-------------|
| **Info** | Eventos de sistemas informativos, cambios exitosos de gateway, actualizaciones de la lista de usuarios. |
| **Error** | Eventos de nivel de error que indican fallos, mensajes MO rechazados o excepciones del sistema. |

---

## Características

!!! info "Capacidades del espectador (MO)"
    - Ver los registros de eventos MO en tiempo real.
    - Supervise las actividades de gateway y el usuario.
    - Seguimiento de las solicitudes de mensajes MO entrantes.
    - Solución y resolución de problemas relacionados con el MO.
    - Refresh logs on demand using the **Refresh** botón.
    - Registros de filtro por **Tipo de registro** (Info / Error).
    - Registros de filtro por **rango de fecha** para el examen histórico.

---

## Filtro de rango de fecha

Los administradores pueden seleccionar un rango de fechas específico para recuperar **registros históricos de eventos MO**Esto es compatible con la solución de problemas retrospectiva, la auditoría del cumplimiento y el examen operacional.

!!! tip
 Al perseguir un problema intermitente, establecer **Tipo de registro = error** primero para centrarse en los fracasos solamente, luego más ancho para **Todos** si no hay eventos de error visibles durante la ventana.
