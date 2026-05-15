---
tags:
  - Billing
  - WhatsApp
  - Rate Plan
---

# Configuración del plan de tarifas de WhatsApp

**Navegación:** <span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span> ➔ <span data-ph="3"></span>.

## Sinopsis

El **Configuración del plan de tarifas de WhatsApp** módulo permite a los administradores definir **plantillas de fijación de precios** para mensajes de WhatsApp. Estos planes de tarifas rigen cómo se facturan y rastrean los mensajes dentro de la plataforma PowerSMPP y se asignan a las cuentas de usuario para una gestión precisa de costos e ingresos.

---

## Crear un nuevo plan de tarifas de WhatsApp

El proceso de creación del plan de tarifas se estructura en **tres pasos**.

![Manage WA Rate Plans — List of configured plans](images/warateplan-01-list.png)

### Paso 1: Detalles básicos

| Campo | Descripción |
|-------|-------------|
| **Nombre del Plan de Tasa** | Asignar un nombre único y descriptivo para el plan. |
| **Es Activo** | Toggle the plan to <span data-ph="0"></span> o <span data-ph="1"></span> estado. |

![Add New WA Rate Plan — Step 1: Basic Details](images/warateplan-02-step1-basic.png)

### Paso 2: Detalles del precio (por país)

Definir la estructura de precios para cada país de destino.

![Add New WA Rate Plan — Step 2: Price Details](images/warateplan-03-step2-price.png)

| Campo | Descripción |
|-------|-------------|
| **Código del país** | Seleccione el país de destino (por ejemplo, <span data-ph="0"></span>). El plan de tarifas soporta los precios de varios países. |
| **Precio del costo** | El costo de compra / mayorista por mensaje WhatsApp para el país seleccionado. |
| **Precio de venta** | El precio al por menor se cobra al usuario final o al cliente por cada mensaje WhatsApp. |
| **Plataforma de carga** | Tasa adicional de plataforma aplicada sobre el precio de venta (si es aplicable). |

### Paso 3: Asignar a los Usuarios

Una vez que se guarda el plan de tarifas, se pone a disposición para la asignación a cuentas individuales de usuario. Asignar el plan garantiza que todos los mensajes de WhatsApp enviados por el usuario sean facturados según la estructura de precios configurada.

---

## Gestión de planes de tarifas existentes

El **Gestionar el plan de tarifas** lista de pantalla todos los planes de velocidad WhatsApp configurados con la siguiente información:

| Columna | Descripción |
|--------|-------------|
| **Nombre del plan** | El identificador del plan de tarifas. |
| **Tasas** | Número de entradas configuradas por países. |
| **Usuario asignado** | Número de usuarios asignados al plan. |
| **Crear fecha** | Fecha en que se creó el plan. |
| **Es Activo** | Situación actual (<span data-ph="0"></span> / <span data-ph="1"></span>). |
| **Es Default** | Si el plan es el predeterminado del sistema. |
| **Medida** | <span data-ph="0"></span>, <span data-ph="1"></span>, <span data-ph="2"></span>o <span data-ph="3"></span> el plan. |

---

## Finalidad de la configuración del plan de tarifas de WhatsApp

!!! info "Utilice este módulo para..."
    - Defina precios de mensajería WhatsApp específicos para cada país.
    - Support multi-country rate plans within a single template.
    - Asignar tarifas planea a cuentas específicas de usuario para facturación.
    - Track WhatsApp costo de mensaje e ingresos por usuario.
    - Permitir un reporte financiero preciso para el tráfico de WhatsApp.
    - Gestionar los cargos de plataforma junto con los precios de costo y venta.

!!! tip
 El cierre es la manera más rápida de hacer girar una variante regional de un plan existente: clonar a los padres, ajustar uno o dos precios de los países, y asignar al nuevo grupo de usuarios.
