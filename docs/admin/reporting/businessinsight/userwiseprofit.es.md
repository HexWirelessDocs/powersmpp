---
tags:
  - Reporting
  - Business Insight
  - User
  - Profit
---

# Informe de Profit de usuario

**Navegación:** <span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span>.

## Sinopsis

El **Informe de Profit de usuario** permite a los administradores analizar el tráfico de SMS a nivel de usuario y la rentabilidad para cualquier rango de fecha seleccionado. El informe se basa **enteramente sobre los mensajes enviados por los usuarios a través de la solicitud** y proporciona ingresos detallados, costos y datos de margen por cuenta del cliente.

---

## 1. Selección de usuario

Seleccione una cuenta de usuario específica de la lista desplegable para generar un informe de beneficio específico para ese cliente.

## 2. Selección de país

Filtrar datos de tráfico por país de destino para obtener análisis granular de rentabilidad de los usuarios por región.

## 3. Filtro de rango de fecha

Define un rango de fechas personalizado para generar informes de ganancias de usuario para cualquier facturación o período operativo.

---

## 4. Informe de la vista del cuadro

El **Cuadro Vista** muestra información detallada de rentabilidad del usuario en formato tabular.

![User Wise Profit — Table View (all users)](images/userprofit-01-table-all.png)

![User Wise Profit — Table View (highlighted)](images/userprofit-02-table-highlighted.png)

### Referencia de columna

| Columna | Descripción |
|--------|-------------|
| **Nombre del usuario** | Nombre / identificador de la cuenta de usuario. |
| **Nombre del país** | País de destino del tráfico SMS del usuario. |
| **MCCMNC** | Código de país móvil + Código de red móvil. |
| **Nombre de la red** | Nombre de red móvil de destino. |
| **Cuenta del mensaje** | Mensajes SMS totales enviados por el usuario. |
| **Precio de compra** | Costo real de enrutamiento incurrido para procesar el tráfico del usuario. |
| **Precio de venta** | Cantidad total de venta cargada al usuario. |
| **Margen % (Ventas - Compra)** | Porcentaje de ganancia calculado para el tráfico del usuario. |
| **Margin (Ventas - Compra)** | Ganancia total obtenida del tráfico de usuarios en USD. |

---

## 5. Informe de vista Gráfico

El **Vista Gráfico** hace un gráfico de barras de rentabilidad de usuario, permitiendo una comparación rápida entre los clientes.

![User Wise Profit — Graph View (Margin by user)](images/userprofit-03-graph-view.png)

---

## 6. Análisis de la comunicación de mensajes

Todos los cálculos en el Informe de Profit de Usuario son impulsados **exclusivamente exclusivamente exclusivamente** por mensajes enviados desde el lado del usuario a través de la solicitud. El tráfico que circunvala la ruta de presentación del usuario de la aplicación no está incluido en este informe.

---

## 7. Fórmula de cálculo de beneficios

```
Margin (USD)          =  Sales Price − Purchase Price

Margin Percentage (%) = ((Sales Price − Purchase Price) / Purchase Price) × 100
```

!!! tip
 Combine este informe con **Gateway Wise Profit** para ver la rentabilidad de dos ángulos complementarios: el cliente (parte de ingresos) y el proveedor (parte de costo).
