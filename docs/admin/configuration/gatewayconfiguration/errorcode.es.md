
## Códigos de error de puerta

![Gateway Error Codes](images/error1.png)

**Códigos de error de puerta** en iTextPRO le permite interpretar y gestionar mensajes de respuesta desde el **Short Message Service Center (SMSC)** cuando la entrega del mensaje falla. Esta característica mejora la visibilidad sobre los fallos de entrega y permite rollbacks de crédito basados en códigos de error específicos.

---

![Configure Error Codes](images/error2.png)

### 1. Sinopsis
Cuando el SMSC no puede entregar un mensaje, devuelve un **código de error no cero** junto con un mensaje de referencia. These are referred to as **Códigos de error de puerta**.

### 2. Propósito
iTextPRO permite a los administradores configurar y mapear estos códigos de error. Cuando una **Informe de entrega (DLR)** se recibe, iTextPRO comprueba la configuración y:
- Muestra un **personalizado error-tag**
- Maps it to a **estatus estándar de SMPP** 
Esta información se muestra en ambos **Admin** y **Informes de usuario**, mejora de la transparencia.

### 3. Prerequisitos
Antes de la configuración, obtener un **Lista de códigos de error de puerta** desde su SMSC.

---

### 4. Pasos de configuración

#### a. Selección de puerta
Elija la puerta de entrada para la que está configurando el código de error.

#### b. Código de error
Entra en **código de error específico** recibido de su SMSC.

#### c. Etiqueta de error de visualización
Insertar el **Estado de referencia** o nombre de la etiqueta del SMSC (por ejemplo, <span data-ph="0"></span>, <span data-ph="1"></span>).

#### d. Código de error estándar
Mape el error a uno de los estatus estándar SMPP:
- <span data-ph="0"></span>
- <span data-ph="0"></span>
- <span data-ph="0"></span>
- <span data-ph="0"></span>
- <span data-ph="0"></span>

#### e. Descripción del error
Proporcione un **breve descripción** de la etiqueta de error. Esto se mostrará en el **Informes de usuario** para ayudar a entender el estado de entrega.

#### f. Es activo
Toggle the error code **encendido o apagado** según sea necesario.

#### g. Credit Rollback
Permitir esta opción **reembolso de los créditos del usuario** automáticamente si un mensaje falla con el código de error mapeado.

---

### 5. Bulk Upload

- Usar el **Bulk Upload** función para configurar varios códigos de error simultáneamente.
- Haga clic **"Bulk Upload"**Entonces:
  - **Descargar el archivo de muestra**
  - **Mapa columna headers** en el mago de importación

---

### 6. Presentar
Una vez configurado, haga clic **"Enviar"** para guardar los códigos de error para la puerta seleccionada.

📌 **Nota:** 
Configuración adecuada de código de error mejora el monitoreo y permite un seguimiento preciso **faltas de envío de mensajes**, **Medidas de retroceso**, y **exactitud de la información**.

---
