---
tags:
  - Reporting
  - Business Insight
  - Gateway
  - Profit
---

# Gateway Wise Profit Report

**Navegación:** <span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span>.

## Sinopsis

El **Gateway Wise Profit Report** proporciona a los administradores un desglose detallado de la rentabilidad del nivel de entrada y análisis de tráfico SMS. Está diseñado para apoyar el análisis financiero, la verificación de facturación y la vigilancia del rendimiento de las vías de entrada presentando **costo de compra**, **valor de ventas**, y **márgenes de lucro** para el tráfico de SMS viajó por cada puerta de entrada.

---

## 1. Selección de puerta

Seleccione una puerta de entrada específica de la desplegable para generar un reporte de ganancias abarcado al tráfico de esa puerta.

![Gateway Wise Profit — Gateway dropdown selection](images/gwprofit-01-gateway-dropdown.png)

---

## 2. Selección de país

El informe puede ser filtrado por el país de destino, lo que permite un análisis de rentabilidad a nivel de los países.

![Gateway Wise Profit — Country filter dropdown](images/gwprofit-02-country-filter.png)

---

## 3. Filtro de rango de fecha

Los administradores pueden definir un **rango de fecha personalizado** generar informes de ganancias para cualquier período histórico.

!!! info "Características del rango de fecha"
    - Análisis diario e histórico del tráfico
    - Filtro de fecha flexible
    - Apoyo a la verificación del período de facturación
    - Examen de la ejecución operacional en cualquier plazo

---

## 4. Informe de la vista del cuadro

El **Cuadro Vista** presenta datos de beneficios de puerta de entrada en un formato tabular estructurado con las siguientes columnas:

| Columna | Descripción |
|--------|-------------|
| **Nombre de la puerta** | La puerta de entrada vagando el tráfico. |
| **Nombre del país** | País de destino del tráfico. |
| **MCCMNC** | Código de país móvil + Código de red móvil. |
| **Nombre de la red** | Red móvil de destino. |
| **Cuenta del mensaje** | Mensajes SMS totales enrutados para esta rebanada. |
| **Precio de compra** | Costo de rutina para esta rebanada. |
| **Precio de venta** | Ingresos ganados de esta rodaja. |
| **Margin (Ventas - Compra) %** | Porcentaje de ganancia calculado. |
| **Margin (Ventas - Compra) (EURO)** | Valor de ganancia absoluto en EURO. |

![Gateway Wise Profit — Table View](images/gwprofit-03-table-view.png)

!!! note
 <span data-ph="0"></span> contra un precio indica que el precio es un precio plano.

---

## 5. Informe de vista Gráfico

El **Vista Gráfico** proporciona una representación visual de bar-chart de la rentabilidad de la puerta de entrada, lo que permite la rápida identificación de las pasarelas o los países de destino de alto rendimiento y bajo rendimiento.

![Gateway Wise Profit — Graph View (Margin bar chart)](images/gwprofit-04-graph-view.png)

---

## 6. Fórmula de cálculo de beneficios

El informe utiliza las siguientes fórmulas estándar para obtener métricas de rentabilidad:

```
Margin (Base Currency) =  Sales Price − Purchase Price

Margin Percentage (%)  = ((Sales Price − Purchase Price) / Purchase Price) × 100
```

---

## Propósito del Informe de Profit de Gateway Wise

!!! info "Usa este informe para..."
    - Supervisar la rentabilidad de la puerta en tiempo real
    - Compare los márgenes a nivel nacional y en sentido de gateway
    - Seguimiento del volumen de tráfico de SMS y costos asociados
    - Revisar los ingresos de la puerta de entrada vs. costo de compra
    - Support financial reporting and billing verification
    - Optimizar las estrategias de rutas para mejorar la gestión de los ingresos
    - Informes de exportación para análisis sin conexión y mantenimiento de registros
