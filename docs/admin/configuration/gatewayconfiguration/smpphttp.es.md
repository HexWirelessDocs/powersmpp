---
tags:
  - SMPP
  - Gateway
  - Configuration
---

# Configuración

## SMPP Gateways (MO/MT)

El **iTextPRO Application** prioriza a **experiencia fácil de usar** a través de una interfaz de diseño flexible y un flujo de trabajo de configuración simplificado. El objetivo es alejarse de las complejidades CLI y los propietarios de aplicaciones sumergibles en un **Interfaz gráfica de usuario (GUI)**- entorno basado en él. Una integración **Communicator Engine** maneja todos los comandos de backend, racionalizando sus tareas operativas.

---

![Manage Gateway](images/httpgateway1.png)

---

El **"Manage Gateway"** característica habilita a los usuarios para manejar la conectividad con externa **Short Message Service Centers (SMSCs)** via **SMPP** y **HTTP** protocolos.

Para **SMPP**, a **único bind** permite operaciones Mobile-Originated (MO), Mobile-Terminated (MT), y Delivery Reports (DLR). iTextPRO soporta **múltiples SMPP Gateways**, permitiendo **redundancia** y **costo-eficacia**.

---

### Configuración de una nueva puerta

Para configurar un conector SMPP:

1. Haga clic **"Añadir nuevo"**.
2. Introduzca las credenciales proporcionadas por su **Vendedor de puerta de entrada** o **operador de telecomunicaciones**.

---

![SMPP Gateway Credentials](images/httpgateway2.png)

---

#### Credenciales necesarias

| Campo | Descripción |
|-------|-------------|
| **Nombre de la puerta** | Un nombre fácil de usar para identificar tu puerta de entrada |
| **Dirección IP** | La IP de su SMSC/vendor |
| **ID del sistema** | Nombre de usuario proporcionado por su proveedor/SMSC |
| **Contraseña** | Se utiliza para la autenticación al SMSC |
| **Puerto Tx / Puerto Rx / Puerto TxR** | Puertos para transmisor, receptor y transceptor se unen |
| **Tipo de sistema** | *(Opcional)* Introduzca sólo si es requerido por el vendedor |

!!! warning
 Verifique todos los valores según la documentación SMSC/vendor para asegurar una conexión exitosa.

---

### Propiedades de entrada

![Gateway Properties](images/httpgateway3.png)

Configure SMPP Propiedades de entrada en iTextPRO para un rendimiento óptimo:

1. **Mantener Alive (Segundos):** 
 Intervalo para *Preguntar Enlace* para mantener la sesión viva.

2. **Gateway Open Time / Close Time:** 
 Definir las horas operativas, a menudo utilizadas para cumplir **No te molestes** políticas.

3. **Gateway Encoding:** 
 Selección de caracteres compatible con el telco/SMSC.

4. **Convertir Message-ID:** 
 Permite la conversión entre **Decimal ↔ Hex** Formatos de mensaje-ID para DLRs precisos.

5. **Zona horaria:** 
 Todos los informes reflejarán esta zona horaria seleccionada.

6. **Stop Loss Price:** 
 Establece los **Precio máximo permitido de la puerta de entrada** cuando se utiliza el enrutamiento ciego.

7. **Mediación por segundo (TPS):** 
 Definir basado en la capacidad de los proveedores. 
 **Fórmula:** <span data-ph="0"></span>

---

### TON/NPI

![TON/NPI Setup](images/httpgateway4.png)

- **TON (Tipo de Número):** 
 Seleccione según la documentación de SMSC (por ejemplo, International, Alphanumeric, etc.)

- **NPI (Numbering Plan Indicator):** 
 Indica el estándar de numeración en uso (E.164, ISDN, etc.)

- **Reunión:** 
 Configurar las sesiones Tx, Rx y TxR por asignación de proveedores.

---

### Roles " Routing

![Gateway Roles](images/httpgateway5.png)

- **Está activo:** 
 Marca la puerta de entrada como en vivo y listo para el tráfico de ruta.

- **Es Default:** 
 Sólo una puerta de entrada se puede marcar como predeterminado. Los mensajes sin rutas iguales van aquí.

- **Es Async:** 
 Enables **modo asincrónico** para mensajes más rápidos.

- **Blind Routing:** 
 Permite la presentación de mensajes a países **sin costos definidos**.

!!! tip
 Después de la configuración, haga clic **"Save"** envía un **on-the-fly bind request** - ningún reinicio manual requerido.
