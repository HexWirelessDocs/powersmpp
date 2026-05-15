---
tags:
  - Reporting
  - Business Insight
  - Gateway
---

# Gateway Wise Count

**Navegación:** <span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span>.

## Sinopsis

El **Gateway Wise Count** report proporciona a los administradores una visión consolidada de los volúmenes de envío de mensajes en todas las entradas configuradas. El informe abarca el informe **los últimos siete días** sobre una base diaria, facilitando la identificación de patrones de tráfico y la distribución de carga a un vistazo.

![Gateway Wise Count — All Gateways (7-day view)](images/gwcount-01-all-gateways.png)

---

## Utilizando el filtro Gateway

Para estrechar el informe a una puerta de entrada específica, seleccione la puerta deseada de la **filtro de desplegable** disponible en la pantalla del informe. La mesa se refrescará para mostrar sólo los datos de la comunicación de la puerta de entrada.

![Gateway Wise Count — Filtered by a single gateway](images/gwcount-02-filtered.png)

---

## Lo que el informe muestra

| Columna | Descripción |
|--------|-------------|
| **Nombre de la puerta** | Nombre amistoso de la pasarela configurada. |
| **Columnas de fecha (uno por día)** | El recuento total de mensajes viajó por esa puerta de entrada el día correspondiente. |

!!! note
 Los recuentos de mensajes visibles se calculan contra cada uno **la propia zona temporal**, no la zona de tiempo de aplicación. Esto se muestra en la nota en página sobre la tabla.

---

## Cuándo utilizar este informe

- Spot day-over-day traffic dips that could indicate vendedor or network issues.
- Identificar las pasarelas infrautilizadas que pueden ser candidatos para la jubilación o la reorganización.
- Verifique que los portales recién añadidos están recibiendo la parte esperada del tráfico.
- Proporcionar instantáneas rápidas de volumen semana-a-glance para los interesados.
