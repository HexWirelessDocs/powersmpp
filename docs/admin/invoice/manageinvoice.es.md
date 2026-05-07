
# Invocación

El módulo de facturación permite a los administradores gestionar la facturación de sus usuarios directos (tipo de cuenta: **Usuario**) proporcionando un plugin para generar facturas, descargarlas o enviarlas por correo electrónico. El flujo de generación de facturas es automatizado y se activa a intervalos específicos configurados por el Admin.

Este módulo ayuda a los administradores a gestionar la operación de facturación de sus usuarios de niños de manera eficiente.

---

## Factura [Prepagada / Postpaida] como Plugin

El administrador debe optar por un **Licencia de facturación** por separado. Una vez habilitado, el módulo de facturación se hace accesible en la aplicación con el modo de facturación seleccionado:**Prepago** o **Puestos pagados**.

- El **Método de facturación** (Prepagado/Postpaid) para cada usuario se define durante la creación del usuario.
- Admin puede configurar el método de facturación para cada usuario.
- Los usuarios que se inscriban por su cuenta tendrán **Prepago** facturación por defecto.

---

## Dashboard de facturación

Cuando el Admin accede al módulo de facturación, la primera vista presentada es la **Dashboard de facturación**. El panel proporciona información de facturación clave:

### 1. Invocación total
Muestra los **total de facturas**, incluyendo:
- Facturas aprobadas 
- Facturas no aprobadas 

### 2. Facturas pagadas
Muestra el conteo de **facturas totalmente pagadas**.

### 3. Facturas no resueltas
Muestra el número de facturas que aún están pendientes, con:
- Facturas impagadas 
- Facturas pagadas parcialmente 

### 4. Gestión de la facturación
Un breve resumen del *Gestionar facturación* sección. 
Los administradores pueden hacer clic **Ir a la página** para navegar a la gestión detallada de facturas.

### 5. Administrar las facturas recurrentes
Aplicable **sólo para los usuarios Postpaid**. 
Desde aquí, los administradores pueden:
- Crear facturas recurrentes 
- Iniciar o detener el ciclo de facturación 
- Modificar la configuración del ciclo de facturación 

### 6. Administrar el pago recibido
Un breve resumen del *Administrar el pago recibido* sección. 
Los administradores pueden redirigir a la página detallada usando la **Ir a la página** botón.

---

## Gestionar facturas

El **Gestionar facturas** página muestra todas las facturas (incluyendo facturas recurrentes) junto con su estado de pago. Los administradores pueden reclamar facturas, descargarlas y enviar correos electrónicos recordatorios de pago.

![Manage Invoices](images/manage1.png)

### Características clave:

#### **Descargar Invoice Report**
Permite a los administradores exportar y descargar el informe de la factura como hoja de Excel.

#### **Enviar recordatorio a granel**
Permite enviar recordatorios de pago a los usuarios cuyas facturas son **No pagado** o **Pagado parcialmente**.

#### **Proyectos**
Las facturas recurrentes autogeneradas para los usuarios de Postpaid se almacenan como **borradores**. 
Los administradores deben revisar y aprobar los borradores manualmente del menú Acción.

#### **Búsqueda anticipada**
La opción de búsqueda avanzada permite filtrar facturas por:
- Usuario 
- Identificación de facturación 
- Situación debida 
- Estado de pago 

Esto ayuda a los administradores a localizar facturas rápidamente basadas en requisitos específicos.

---

## Crear factura

Esta sección permite a los administradores crear manualmente facturas para los usuarios.

---

### **Para los Usuarios Prepagados:**

1. Seleccione el tipo de usuario: **Prepago**
2. Elige al usuario.
3. Entra en **Fecha de facturación** y **Fecha prevista**.
4. Entra en **Cuantía de recarga** (antes de impuestos).
5. Proporcione un **descripción** para la factura.
6. Modificar **Términos y condiciones** o **Notas de clientes** si es necesario (o utilizar valores predeterminados configurados).
7. Elija uno de:
   - **Crear factura** (si el pago aún no se ha recibido)
   - **Crear " Solicitud de Reclamación "** (si ya se ha recibido el pago, el sistema dará lugar a detalles del pago)

---

### **Para los usuarios postales:**

Las facturas postales generalmente se autogeneran al final del ciclo de facturación definido bajo **Facturas recurrentes**. 
Sin embargo, si se saltó un ciclo o necesita intervención manual, los administradores pueden crear la factura manualmente:

1. Seleccione el tipo de usuario: **Puestos pagados**
2. Elige al usuario.
3. Seleccione **rango de fecha** para el cual se debe crear la factura y buscar los registros.
4. El sistema mostrará los registros de mensajería para el período seleccionado.
5. Después de la verificación, elija:
   - **Crear factura**
   - **Crear y Reclamar Factura**

