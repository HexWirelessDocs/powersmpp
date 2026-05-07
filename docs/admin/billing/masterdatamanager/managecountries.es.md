---
tags:
  - Billing
  - Rate Plan
  - Pricing
---

# Facturación

## Gestión simplificada de facturación con iTextPRO

Los Aggregadores en la industria de SMS a menudo enfrentan desafíos en la gestión **múltiples gateways**, **diversas estructuras de precios**, y **transacciones internacionales**. 
El **iTextPRO Módulo de facturación** aborda estos desafíos con características avanzadas que aseguran operaciones racionales, precisas y rentables.

---

## 1. Configuración de la moneda base

- **Importancia**: Garantiza la coherencia y exactitud en las transacciones financieras.
- **Recomendación**: Euro (EUR) es ampliamente utilizado en la industria global de agregación SMS.
- **Examen**: Una vez que se establece la moneda base, cambiarla puede ser compleja. Decidir temprano en el viaje de negocios.

---

## 2. Understanding MCC and MNC Codes

- **MCC (Mobile Country Code)** y **MNC (Mobile Network Code)** son cruciales para personalizar los precios basados en redes móviles dentro de un país.
- **Precios de Operador**: Muchos operadores de telecomunicaciones basan sus precios en combinaciones MCC + MNC.
- **Flexibilidad**iTextPRO permite **fijación de precios específicas de la red** para mayor optimización de ingresos.

---

## 3. Comprensión de prefijo para números móviles de ingeniería inversa

- **Propósito**: Identifica el origen y la red de un número móvil.
- **Prefijo**: Los primeros 3-4 dígitos ayudan a detectar **Código del país** y **Red Móvil**.
- **Ejemplo**: 
  - Número: <span data-ph="0"></span> 
  - Código del país: <span data-ph="0"></span> (UAE) 
  - Con precios planos: El cálculo de costos es sencillo. 
  - Con precios MCC/MNC: Se requiere una búsqueda adicional (ninguna herramienta actual proporciona MCC/MNC directamente desde este número).

![Manage Countries](images/managecountries1.png)

---

## 4. Conversión de Moneda

- **Moneda básica**: Utilizado para transacciones internas.
- **Mostrar moneda**: Los usuarios pueden ver las transacciones en su moneda preferida.
- **Prestaciones**: Simplifica las operaciones internacionales manteniendo la precisión contable.

---

## 5. Política de protección de las pérdidas

- **Revenue Leakage Tool**: Identifica posibles pérdidas de ingresos en tiempo real.
- **Medidas preventivas**: Detiene las transacciones causadas por errores de tipo, manipulación de números o administración.
- **Seguridad financiera**: Protege contra la pérdida de ingresos y garantiza la exactitud de facturación.

---

## Beneficios clave

- **Simplificación operacional** – Facturación de SMS global simplificada. 
- **Precio preciso** – Control de nivel de red para precios competitivos. 
- **Manejo de moneda clara** – Base sin costuras y gestión de divisas. 
- **Seguridad financiera** – Políticas de prevención de pérdidas automatizadas. 

---

# Master Data Manager

El **Master Data Manager** sección contiene cuatro opciones clave de configuración:

1. **Países de gestión** 
2. **Gestion MCC/MNC** 
3. **Manage Prefix** 
4. **Precio de la puerta de entrada**

---

## 1. Gestion Countries

El **Países de gestión** característica permite la configuración y gestión de la terminación del tráfico SMS en varios países.

![Manage Countries](images/managecountries2.png)

### Agregar un País Único

- **Nombre del país** – Nombre completo del país para una identificación clara. 
- **Código del país** – Unico identificador para el enrutamiento. 
- **Country ISO Code** – Código estandarizado para compatibilidad global. 
- **Agregar proceso** - Haga clic **Añadir** incluir al país en la lista principal.

![Single Country Add](images/managecountries3.png)

---

### Funcionalidad de carga a granel

![Bulk Upload](images/managecountries4.png)

- **Descargar Muestra Excel** – Pre-formatted with all countries for easy editing. 
- **Elija Archivo > Subir** – Admite múltiples entradas a la vez. 
- **Columna Mapping** – Mapa Excel campos a **Nombre del país**, **ISO**, y **Código**. 
- **Presentar & Mostrar** – Bulk añade países y personaliza la visualización de registros.

![Bulk Upload Results](images/managecountries5.png)

---

### Tasa de acción

![Action Options](images/managecountries6.png)

- **Editar** – Actualizar los detalles existentes. 
- **Actualización** – Actualizar los datos del país. 
- **Suprimir** – Eliminar las entradas no utilizadas. 

---

**Mejor práctica:** 
Revisar y actualizar regularmente su **Master Data Manager** para garantizar que las configuraciones de los países y las redes sigan siendo precisas para la fijación de precios y la enrutamiento.
