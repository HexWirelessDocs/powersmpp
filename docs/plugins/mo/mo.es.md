
# MO

## Definición
Mensajes MO (M)**Origen móvil** mensajes) son iniciados por los usuarios de teléfonos móviles y enviados a códigos breves dedicados o números de código largo utilizando palabras clave específicas. 
Permiten a clientes o suscriptores interactuar directamente con proveedores o aplicaciones.

---

## Proceso

### Iniciación del usuario
Un cliente envía un mensaje de texto con una palabra clave específica a un código corto o código largo dedicado.

**Ejemplo:** 
<span data-ph="0"></span> → <span data-ph="1"></span>

### Mensaje Routing
El mensaje se dirige a la aplicación o proveedor vinculado a ese código o número.

---

## Puntos clave
- Permite la comunicación bidireccional entre usuarios y proveedores.
- Usa palabras clave específicas para activar respuestas.
- Funciona a través de códigos breves dedicados o códigos largos.

---

## Configuración de HTTP MO Handlers

### Sinopsis
HTTP MO Handlers in **iTextPro** recibir mensajes MO entrantes de proveedores. 
Las estructuras de carga pueden diferir entre los proveedores.

### Paso 1: Añadir un nuevo Handler
1. Haga clic **Añadir nuevo Handler**.
2. Parámetros de carga de mapa en la UI.

![MO Handler Config](images/mo1.png)

**Prerrequisitos:** 
Comprensión básica de API RESTful.

**Ejemplo (Vendor: Airtel):**
```json
{
  "originatorAddress": "999563256",
  "destinationAddress": "8754321565",
  "messageContent": "BINGO 101",
  "CustomerId": "669912"
}
```

**iTextPro Config:**
- Método: <span data-ph="0"></span>
- Tipo de contenido: <span data-ph="0"></span>
- Clave del creador: <span data-ph="0"></span>
- Clave del destino: <span data-ph="0"></span>
- Clave del mensaje: <span data-ph="0"></span>

![MO Config 2](images/mo2.png)

---

### Paso 2: Configure MO Services for User Account
1. Inicia sesión en iTextPro → localiza la cuenta de usuario.
2. Activar **MO Services** dentro **Servicios de gestión**.
3. Set MO Número > Palabra clave:
   - Fecha final
   - Seleccionar Canal (número de OMI)
   - Palabras clave (o <span data-ph="0"></span> para todos)
   - Estado: Activo
4. Haga clic **Añadir**.

![MO Config 3](images/mo3.png) 
![MO Config 4](images/mo4.png)

---

### Paso 3: Configuración de reglas de rutina
1. Ve. **MO Routing Rule**.
2. Crear o editar una regla:
   - Nombre de la regla, Fecha de inicio/final
   - Interfaz de puerta: HTTP/SMPP
   - Condiciones: Orientador, Destino, Mensaje
   - Usuario & Endpoint: HTTP Webhook o ESME

![MO Routing](images/mo5.png) 
![MO Routing UI](images/mo6.png) 
![MO Routing Rule](images/mo7.png)

---

## MO Module Access
1. Impersonate/Login a la cuenta de usuario.
2. Abierto **Módulo MO** para ver mensajes MO.

![MO Inbox](images/mo8.png) 
![MO Keyword](images/mo9.png) 
![MO Keyword Details](images/mo10.png)

---

## Auto Responder
- Establecer respuestas automatizadas para mensajes MO.

![MO Auto Reply](images/mo11.png)

---

## Notificaciones
- **Email Forwarding** – Recibir alertas MO por correo electrónico. 
- **Forwarding móvil** – Recibir alertas vía SMS (incluye código de país).

![MO Mobile Notify](images/mo12.png)

---

## Gestionar Sub-keyword
Las sub-palabras son disparadores secundarios después de la palabra clave principal.

**Ejemplo:**
- **Palabras clave principales:** CAR 
- **Autorespuesta:** 
 <span data-ph="0"></span>
- **Sub-keyword 1:** SÍ → <span data-ph="0"></span> 
- **Sub-keyword 2:** NO → <span data-ph="0"></span>

![MO Sub-keyword](images/mo13.png)

---

## Informes
- Exportar informes MO a Excel.
- Filtrar por palabras clave o sub-palabras.

**Pasos:**
1. Ve. **Informes**.
2. Haga clic **Export Report**.
3. Descargar y personalizar.

![MO Reports](images/mo14.png) 
![MO Reports 2](images/mo15.png)

---

## MO Webhooks
Entrega de mensajes MO en tiempo real a un punto final HTTP dado.

**Configuración:**
1. Habilitación **HTTP Web Push** en la cuenta de padres.
2. Ve. **MO Webhooks** → **Añadir New Webhook**.
3. Set:
   - Nombre
   - URL de punto final
   - Método: GET/POST
   - Handler: MO

**Nota:** 
Si el punto final es inalcanzable, el MO es descartado. El tiempo es de 10 segundos.

![MO Webhook](images/mo16.png) 
![MO Webhook Config](images/mo17.png)