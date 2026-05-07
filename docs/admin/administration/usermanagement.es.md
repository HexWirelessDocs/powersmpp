---
tags:
  - Admin
  - User Management
---

## Administración

**Bienvenido a iTextPRO**, su puerta de entrada a la gestión eficiente de documentos!

Para empezar con el acceso al sitio de administración iTextPRO, necesitará iniciar sesión utilizando el **URL de Admin** y **credenciales de inicio** proporcionado por nuestro equipo de entrega de servicio.

Una vez que hayas iniciado sesión, serás recibido por un **interfaz fácil de usar** equipado con varios controles de navegación. El control de navegación primario para iniciar su experiencia es **Administración de usuarios - Gestión de usuarios.** Tenga en cuenta que los controles asociados anidados en este menú solo serán visibles una vez que usted **introducir un nombre de usuario específico** y golpear el **'Ver'** botón.

Para obtener información detallada sobre la funcionalidad de la sección Administración, encontrará **descripciones generales** de los diversos controles en las secciones posteriores de este documento.

---

## Administración de usuarios

Navigando a **Gestión de usuarios** La página es una brisa. Simplemente haga clic en **'User Management'** opción, y te guiará sin problemas a la página de Gestión de Usuarios.

Para continuar, **Introduzca el nombre de usuario** usted está interesado en el cuadro de búsqueda dedicado y golpear el **'Ver'** botón. El cuadro de búsqueda **popula automáticamente los registros coincidentes** en orden alfabético, haciendo su búsqueda rápida y sin esfuerzo.

![User Management](images/Administration1.png)

---

## Agregar nuevo usuario

Pasar al proceso de ampliar su base de usuario es simple. Simplemente haga clic en **"Añadir nuevo usuario"** botón para iniciar la creación de una nueva cuenta de usuario.

Sin embargo, para asegurar una configuración completa, necesitará proporcionar la siguiente información esencial.

### **Paso 1: Ingrese los datos del usuario**

Al hacer clic en **"Añadir nuevo usuario"** botón, iTextPRO te guiará a una página dedicada. Rellene lo siguiente:

- **Nombre**
- **Apellido**
- **Dirección**
- **Nombre del usuario** - Debe ser único.
- **Contraseña** – Mínimo 8 caracteres, con al menos:
  - 1 carta mayúscula
  - 1 minúscula
  - 1 carácter numérico
  - 1 carácter especial
- **ID de correo** – Se utiliza para alertas de correo electrónico, incluyendo OTPs y correos electrónicos de bienvenida (basados en configuraciones de Admin SMTP).
- **Número de móvil**
- **Zona horaria** – Los efectos reportan los tiempos y la pantalla específica del usuario.
- **Moneda de usuario** – Propósito de visualización solamente; sujeto a conversión en tiempo real.
- **Validez de la cuenta de usuario**:
  - **Validez personalizada** – Definir una fecha final.
  - **Validez de la vida** – No vencimiento (acceso permanente).
- **Tipo de cuenta de usuario**:
  - **Usuario** – Acceso al Panel de Usuarios.
  - **Revendedor** – Cuenta de marca blanca con opciones de marca y precios.

![Add User Step 1](images/adduser1.png)

---

### **Paso 2: Detalles de notificación (opcional)**

Personaliza tus notificaciones añadiendo correos electrónicos de múltiples partes interesadas para alertas como:

- Login OTPs
- Nueva verificación de usuario
- Actualizaciones de planes de tarifas
- Notificación de aprobación

![Add User Step 2](images/adduser2.png)

Al hacer clic **"Crear nuevo usuario"**, a **correo electrónico de bienvenida** se envía (requiere configuración SMTP). iTextPRO confirma el éxito y presenta:

- **Lo haré en otro momento.** – Redirecta al perfil del nuevo usuario.
- **¡Está bien! Hagámoslo** – Lanza los **Asistente de configuración de la cuenta**.

![Add User Step 3](images/adduser3.png)

---

### **Paso 3: Configurar los ajustes de la puerta de entrada**

Elija su método de enrutamiento:

- **Sí.** – Usar un **Puerta fija** para todos los mensajes.
- **No, añadiré la regla de enrutamiento más tarde.** – Dejar **Main Routing Engine** dinámicamente maneje la ruta.

También puede hacer clic **"Skip"** para proceder.

![Gateway Settings](images/adduser4.png)
![Routing Option](images/adduser5.png)

---

### **Paso 4: Agregar créditos SMS**

- **Introduzca créditos** – Número de créditos SMS.
- **Guardar cambios**
- **Proceder al siguiente paso**

!!! note
 Todas las transacciones de crédito están en **moneda base únicamente**.

![Credits](images/adduser6.png)

---

### **Paso 5: Elegir la política de identificación del remitente**

Seleccione:

- **ID dinámico del remitente** – Los usuarios pueden utilizar cualquier ID de remitente (numeric/alfanumérico).
- **ID de remitente fijo** – Use un ID de remitente predefinido para la consistencia.

Haga clic **"Save"** para confirmar.

![Sender ID](images/adduser7.png)
![Sender ID Settings](images/adduser8.png)

---

### **Paso 6: Configuración de SMPP Cuenta para Clientes Mayoristas**

Para crear una cuenta SMPP:

- Seleccione **Sí.**
- Configure:
  - **ID del sistema**
  - **Contraseña**
  - **Whitelist IPs** (para seguridad)

!!! tip "Buenas prácticas"
 Whitelist IPs para evitar el spam SMS.

Uso **0.0.0.0** para el acceso abierto (autenticación a través de ID de sistema & contraseña).

![SMPP Setup 1](images/adduser9.png)
![SMPP Setup 2](images/adduser10.png)

---

### **Paso 7: Gestión de la Cuenta de Usuario**

Después de completar la configuración, verá el mensaje final con 3 opciones:

#### **Opción 1: Impersonate**
Inicie sesión como usuario al instante, sin necesidad de credenciales separadas.

#### **Opción 2: Facturación de avance de configuración**
Planes de gestión:

- **Añadir nuevo precio de venta**:
  - País
  - MCC/MNC
  - Precio de venta
  - Estado de activación
- **Plantilla de tarifas de importación**

!!! warning "Protección de las pérdidas"
 Garantía **precio de venta ≥ costo de entrada** para evitar caídas de mensajes (Política de Protección de Pérdidas).

#### **Opción 3: Administrar este Usuario**
Acceso **Perfil** o **Gestión de usuarios** página para nuevos ajustes.

A **correo electrónico de bienvenida** será enviado automáticamente.

![Impersonate](images/adduser11.png)
![Rate Plan Setup](images/adduser12.png)
![Manage User](images/adduser13.png)

---

▪ **¡Estás listo!** Ahora ha configurado completamente un usuario en **iTextPRO**, y están listos para gestionar usuarios, facturación, notificaciones y mucho más - todo de un lugar.

# Gestión de usuarios

El **Gestión de usuarios** sección se organiza en múltiples pestañas para mejorar el diseño de control. Esta división de controles asociados a la cuenta de usuario proporciona **comodidad en la gestión eficaz de la cuenta de usuario**.

Para encontrar un usuario específico, simplemente **Introduzca el nombre de usuario** en el cuadro de búsqueda y haga clic en **Vista** botón. La caja de búsqueda está equipada con un **característica inteligente** que automáticamente popula la caja con **registros coincidentes en orden alfabético**.

Para una representación visual, consulte la siguiente figura:

![User Management](images/usermanagement1.png)

---

## Detalles de Gestión de Usuarios

### Opciones de primera fila

#### **Impersonation**
- **Descripción:** Seleccionar esta opción le permite **iniciar sesión o hacerse pasar por un usuario** en su cuenta.
- **Autenticación:** Entra en **Contraseña de administración** para verificación.
- **Nota:** La cuenta de usuario se abre en **nueva pestaña** dentro de la misma ventana del navegador, facilitando **Gestión simultánea** de cuentas de usuario y administración.

#### **Plan de tarifas de gestión**
- **Funcionalidad:** Este hipervínculo le redirige a la **Plan de tarifas de usuario** página.
- **Propósito:** Configuración **venta de precios para países y redes**.

#### **Situación**
- **Usage:** **Activar o desactivar** una cuenta de usuario/reseller.
- **Resultado:** Usuarios desactivados **no puede iniciar sesión**.

#### **Eliminar este Usuario**
- **Action:** Permanente **Borrar una cuenta de usuario**.
- **Precaución:** Usuarios eliminados **no se puede restaurar**.

---

### Opciones de segunda fila

#### **Perfil (Detalles incluidos)**

- Nombre del usuario 
- ID de usuario 
- Número de móvil 
- ID de correo *(utilizado para comunicaciones y alertas)* 
- Zona horaria 
- Prioridad del usuario *(por mensajes de enrutamiento)* 
- Función de la cuenta *(Reseller o Usuario)* 
- Moneda de usuario *(versión monetaria, sujeto a conversión)* 
- Validez Hasta *(Atención o tiempo de vida)* 
- Último acceso IP 
- Última hora de inicio de sesión 

**Funcionalidad:** Acceso y gestión **Información básica sobre el perfil de usuario**.

#### **Reset Password**
- **Action:** Restablecer la contraseña para **usuarios o cuentas de revendedor**.

!!! note
 Todas las acciones en la sección Gestión de Usuarios contribuyen a **Gestión amplia y simplificada de las cuentas de usuario** experiencia. Para más detalles, consulte el manual de usuario iTextPRO.

---

## Prerrogativas adicionales y ajustes avanzados

![Advanced Privileges](images/usermanagement2.png)

### **Estado de bloqueo de usuario**
- **Descripción:** Facilitar esta opción **bloquea la cuenta del usuario**, restringiendo las actividades de acceso.

### **Validación del usuario Spam**
- **Descripción:** Cuando esté habilitado, iTextPro **valida las palabras clave del usuario SPAM** para cada campaña. Los usuarios confiables pueden **Anulación** esto desactivando la palanca.

### **Validación Global de Spam**
- **Descripción:** Permite la aplicación **validar las palabras clave de Global SPAM** para campañas de usuario. Los usuarios confiados pueden anular esta validación.

### **Validación IP de API**
- **Descripción:** Facilitar esta opción garantiza iTextPRO **valida la dirección IP lista blanca** antes de procesar las solicitudes de API.

### **SMS HTTP Web Push**
- **Descripción:** Cuando esté habilitado, la aplicación **DLR copias** a la URL de punto final HTTP configurada en la opción gestionar webhooks de la cuenta de usuario.

### **WhatsApp HTTP Web Push**
- **Descripción:** Habilitar este botón de cambio permite al administrador habilitar el **WhatsApp webhook opción** para que el usuario reciba los DLRs/Conversaciones de WhatsApp a los puntos finales configurados.

![WhatsApp HTTP Web Push](images/usermanagement14.png)

### **Mostrar número móvil enmascarado**
- **Descripción:** El número de serie enmascarado permite a admin habilitar la característica **Número de máscaras**. Una vez que este botón de cambio se ha fijado como activo, todos los números móviles en los que se han iniciado las campañas desde la aplicación, sus **los últimos cuatro dígitos** para el número móvil será enmascarado.

![Show Masked Mobile Number](images/usermanagement15.png)

!!! example
 En el informe de campaña del usuario, los números enmascarados aparecen como <span data-ph="0"></span>.

![Masked Number in Report](images/usermanagement16.png)

### **Usuario sobre venta**
- **Descripción:** Permite la configuración de un **Excesivo límite del umbral** en usuarios, permitiéndoles consumir una cantidad determinada más allá del saldo asignado.

**Ejemplo:** 
Si el umbral está fijado **500 EUROS**, el usuario puede consumir hasta **500 EUROS más** que el saldo asignado.

---

## Ajustes avanzados

![Advanced Settings](images/usermanagement3.png)

### **Open Sender**
- **Descripción:** Permite a los usuarios finales enviar mensajes con un **ID de remitente dinámico** (número o alfanumérico).

### **Plantilla abierta**
- **Descripción:** Permite a los usuarios utilizar **contenido dinámico** en mensajes permitiendo plantillas abiertas.

### **Is Skip Profile OTP**
- **Descripción:** Enviar un **OTP al ID de correo electrónico registrado del usuario** para actividades de actualización de perfiles.

### **Is Skip Login OTP**
- **Descripción:** Enviar un **OTP al ID de correo electrónico registrado del usuario** para actividades de login.

### **Indemnización DLR**
- **Descripción:** Permite habilitar o desactivar **DLR compensation** para cuentas de revendedor infantil.

### **DLR Compensation**
- **Descripción:** Esta función permite a admin generar algún beneficio adicional aplicando compensación en los mensajes y generando el DLR de la aplicación **sin enviar los mensajes a la entrada**.

![DLR Compensation](images/dlrcompensation1.png)

**Configuración:**

- **DLR Status:** Seleccione el estado del mensaje que debe aplicarse para los mensajes en los que se ha aplicado la indemnización.
- **Porcentaje:** Añádase el valor porcentual al que debe aplicarse la indemnización.
- **Código de error:** Configurar código de error contra el estado, por lo que el mismo será actualizado en los informes.
- **Límite SMS del Umbral:** Define el umbral del número de destino para la aplicación de la indemnización DLR. Una vez alcanzado el umbral, la compensación se aplicará según la configuración.

!!! note
 Para la interfaz web el límite de umbral funcionará sobre la base de la campaña y en caso de SMPP/API, el umbral funcionará diariamente.

![DLR Compensation Controller](images/dlrcompensation2.png)

??? example "Ejemplo de compensación DLR"
 Un usuario ha iniciado una campaña sobre los números 2000 con la siguiente configuración:

    - **DLR Compensation:** 20 por ciento
    - **Límite del Umbral:** 1000

 Según la configuración:

    - De 2000 mensajes, sólo **1600 mensajes** será enviado al vendedor de la puerta de entrada.
    - Para **400 mensajes**iTextPRO genera **DLRs automática**, resultando en maximizar su rentabilidad para 400 mensajes.

 Si el usuario envía una campaña en **1000 números móviles** ( umbral bajo), **DLR compensation is not applied**.

---

## Servicios activos

Esta sección consta de la **Plugins ofrecidos por iTextPRO**. Estos plugins necesitan ser **optado por separado** ya que no son parte de la aplicación empaquetada.

![Active Services](images/activeservices1.png)

**Visualización de servicios activos:** Muestra los plugins actualmente habilitados. Además, el administrador puede activar o desactivar los plugins desde el botón de cambio.

### 1. **MO (Mobile Originator)**
- **Función:** Activa el **MO service** para usuarios.
- Una vez que iTextPRO+ recibe el **mensaje entrante (MO)**, aparece en el **informe de la caja del usuario**.
- Los mensajes pueden enviarse a **SMPP, HTTP push, email**, o gatillo **respuestas automáticas**.

### 2. **SMS inteligente**
- **Función:** Activa el **SMS inteligente** función.
- Convertir URLs largas en **enlaces inteligentes acortados**.
- Pistas:
  - Usuarios **Número de móvil**,
  - **Dirección IP**,
  - **Detalles del dispositivo**,
  - **Geolocalización**.

### 3. **Correo electrónico a SMS**
- **Función:** Convertires **correos electrónicos en mensajes SMS**, permitiendo la comunicación a través de portales de correo electrónico.

### 4. **WhatsApp**
- **Función:** Permite el **Servicios de WhatsApp** al usuario.
- Una vez activado el plugin, el módulo WhatsApp aparecerá en la aplicación.
- Los usuarios pueden conectar su cuenta de negocio a la aplicación.
- Agregue plantillas, configure los webhooks para DLR y Conversaciones.
- Obtener APIs para enviar mensajes a través de APIs.

---

## ID del remitente

El **ID del remitente** pestaña habilita a los usuarios para configurar sus IDs de remitente directamente. Muestra:

- **Pendiente**
- **Aprobado**
- **Rechazado** ID de remitente

Accesible a través de **"View Sender ID"** enlace.

![Sender ID](images/usermanagement6.png)

A **agregar un ID de remitente**:

- Haga clic **Añadir nuevo**
- Define el **ID del remitente** y **propósito**
- Haga clic **Guardar**

El ID del remitente (Estado: **aprobado**) se añadirá a la cuenta de usuario.

![Add Sender ID](images/usermanagement7.png)

---

## Plantilla

El **Plantilla** sección permite a los usuarios ver plantillas existentes. Cada plantilla **Situación** (aprobado, pendiente, rechazado) está claramente marcado.

![Templates](images/usermanagement8.png)

---

## Detalles del mensaje

Los usuarios obtienen información sobre el **los últimos tres mensajes de campaña** y sus **estadísticas basadas en el estado**, ayudar a evaluar **ejecución de la campaña**.

![Message Details](images/usermanagement9.png)

---

## Créditos

El **Créditos** ficha muestra:

- **Equilibrio disponible del usuario**
- **Historia de la transacción**

Los usuarios pueden gestionar su saldo de cuenta a través de **"Añadir más crédito"**:

![Credits](images/usermanagement10.png)

Para añadir créditos:

- Seleccione **tipo de servicio**
- Entra **Detalles del pago**
- Especifique el **Crédito**

!!! note
 Los créditos deben añadirse en el **moneda base**.

![Add Credit](images/usermanagement11.png)

---

## Filtro

El **Filtro** opción permite a los usuarios **números móviles de lista blanca**, asegurando **DLR compensation is not applied** a esos.

Agregar números móviles con **códigos de país** fácilmente.

![Filter](images/usermanagement12.png)

---

## MT Routing

El **MT Regla de Routing** es una característica pivotal. Puedes:

- Crear **reglas de enrutamiento** para dirigir el tráfico de SMS
- Aplique a:
  - **Interfaz web**
  - **API**
  - **SMPP submissions**

Los usuarios también pueden configurar **reglas fijas de la puerta de entrada**, entradas auto-populares en **Main Routing Engine**.

!!! tip
 Configurar una puerta fija es opcional pero mejora **eficiencia de enrutamiento**.

![MT Routing](images/usermanagement13.png)

---

## Plan de tarifas de gestión

El **Plan de tarifas de gestión** opción permite al administrador configurar **precio de venta** para el usuario.

**Precio de venta:** El administrador de la cantidad se cargará a su usuario por mensaje será el precio de venta.

Para añadir un precio de venta al usuario, siga los siguientes pasos:

**Paso 1:** Vaya a la Administración √≥ Principal Administración de Usuarios √≠ confía en Gestión de Usuarios Búsqueda de usuario **Plan de tarifas de gestión**.

![Manage Rate Plan](images/rateplan1.png)

**Paso 2:** Elija el método adecuado para añadir precio de venta.

### 1] Añadir nuevo precio de venta

Esto permite que el administrador ingrese el precio de venta uno por uno al País y Redes para el usuario.

Seleccione el tipo de interfaz: **TODOS** o **SMPP**

![Add New Selling Price](images/rateplan2.png)

#### a) TODA la interfaz

Si la interfaz ha sido elegida como TODAS, el administrador necesita especificar la Red País y luego el precio de venta. Una vez que se han añadido todos los detalles, haga clic en **ADD** para guardar la configuración.

![ALL Interface](images/rateplan3.png)

#### b) Interfaz SMPP

Si la Interfaz ha sido elegida como SMPP, el administrador necesita especificar el **SMPP Nombre del conector o nombre ESME**, por lo que el plan de tarifas será aplicable para esa cuenta SMPP específica. A continuación, especificar la Red País y el precio de venta. Una vez que se han añadido todos los detalles, haga clic en **ADD** para guardar la configuración.

![SMPP Interface](images/rateplan4.png)

!!! info "ALL vs SMPP Interface"
 **TODOS** indica los mensajes iniciados desde todas las interfaces (Web, API y SMPP). **SMPP** indica un plan de tarifas sólo aplicable cuando el usuario envía tráfico usando la interfaz SMPP. Si no se configura ningún precio de venta específico de SMPP, los mensajes se procesarán con el precio configurado para TODOS.

![Rate Plan List](images/rateplan8.png)

### 2] Plantilla de Plan de Precios

Esta opción permite al administrador importar todas las tarifas existentes o una hoja de tarifas preparada a la cuenta de usuario en una sola go. Reducirá las iteraciones para añadir varios precios de venta a la cuenta de usuario.

**Paso 1:** Seleccione el plan de tarifas
**Paso 2:** Admin también puede elegir la interfaz (ALL o SMPP)
**Paso 3:** Opción de sobreescribir cualquier precio de venta existente.
**Paso 4:** Haga clic en el botón Importar para añadir el precio de venta a la cuenta de usuario.

![Import Rate Plan Template](images/rateplan6.png)

### Notificar usuario

Cuando el precio de venta sea actualizado por el administrador, se enviará un correo electrónico al correo electrónico registrado en la cuenta de usuario con la línea de asunto **"Notificación de actualización de precios - sus tasas de mensajería han sido revisadas"**.

Este email contiene los archivos de Excel para todos los precios de venta configurados en la aplicación.

Además, el administrador/Reseller puede hacer clic en **Notificar usuario** botón para activar el correo electrónico al usuario en caso de que no hayan recibido ningún email.

![Notify User](images/rateplan5.png)

---

## Creación de usuarios - Modo de facturación

Durante **creación del usuario**Si el **Módulo de facturación** está habilitado en la aplicación, el administrador debe configurar **Modo de facturación** para el usuario. El modo de facturación seleccionado determina cómo se carga el uso del mensaje y cómo se generan las facturas.

![Billing Mode](images/billingmode1.png)

Los siguientes modos de facturación están disponibles:

=== "Prepagado"

 Cuando un usuario se configura como **Prepago**:

    - El administrador debe **generar una factura manualmente**.
    - El importe de la factura debe ser **acreditado a la cuenta del usuario**.
    - Sólo después de la factura se reclama y el saldo está disponible el usuario podrá enviar mensajes de la aplicación.
    - El envío de mensajes está restringido sobre la base del saldo prepago disponible.

=== "Postpaid"

 Cuando un usuario se configura como **Puestos pagados**:

    - El administrador debe **asignar un límite de sobreproyecto** al usuario.
    - La solicitud será **generar facturas automáticamente** basado en el configurado **Ciclo de facturación**.
    - El usuario puede continuar enviando mensajes hasta que se alcance el límite de sobreimpresión asignado.
    - La facturación se calcula sobre la base del uso real durante el período de facturación.

!!! warning "Notas clave"
    - El **Modo de facturación** es aplicable sólo cuando el módulo de facturación está activo.
    - La configuración de facturación impacta directamente la entrega de mensajes de usuario y la generación de facturas.
    - Los límites de sobreimpresión adecuados y los ciclos de facturación deben configurarse para que los usuarios postpagados eviten la interrupción del servicio.
