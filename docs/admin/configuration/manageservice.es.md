
## Servicios de gestión

El **Servicios de gestión** sección en iTextPRO proporciona visibilidad a los diversos **servicios de antecedentes y sobre el terreno** que conduce las funcionalidades básicas de la plataforma. Esta interfaz está destinada principalmente a usuarios expertos o administradores.

!!! danger "Precaución"
 Si bien es posible detener o iniciar un servicio desde la interfaz web, esto debe hacerse **con extrema precaución**, especialmente durante los tiempos de carga máxima, como puede resultar en **pérdida de datos** o **interrupción de los servicios**.

---

### Sinopsis del servicio

A continuación se muestra una breve descripción de cada servicio visible en el **Servicios de gestión** sección:

| **Nombre del servicio**         | **Descripción**                                                                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Servicio al Cliente**       | Conecta iTextPRO con su SMSC a través de SMPP para gestionar **SMS MT (Mobile Terminated)** y **SMS MO (Mobile Originated)** tráfico.                      |
| **DLR Service**          | Maneja en tiempo real **Informes de entrega (DLRs)** y actualiza el estado del mensaje dentro del sistema para una presentación precisa.                                      |
| **SMPP Server Service**  | Escucha el tráfico SMPP entrante de **Usuarios ESME** en un puerto predefinido, permitiendo a los usuarios externos enviar SMS.                                      |
| **Servicio de recogida de archivos**  | Lee los archivos de mensajes de campaña subidos por los usuarios y los envía al **gateway queue** para el procesamiento.                                               |
| **Servicio de validación**    | Validaciones **Parámetros de fijación** para usuarios que se conectan a través de interfaces API y SMPP, garantizando que el tráfico sea aceptado sólo por clientes autorizados.       |
| **Data Builder Service** | Gestiona el almacenamiento de **Registros de PDU** y **Registros de mensajes** en la base de datos para fines de registro y depuración.                                          |
| **Report Builder Service** | Perfiles y compilaciones **recuentos enviados e informes resumidos** para usuarios, ayuda en el seguimiento del uso y facturación.                                            |
| **Descargar Report Service** | Procesos y genera **Informes descargables** para administradores y usuarios basados en datos solicitados.                                                  |
| **Servicio de notificación** | Sends **Notificaciones de alerta por correo electrónico** a usuarios y administradores y monitores activos **estado de salud de las puertas**.                                               |

---

### Características clave

- ✅ Ver el **Situación actual** de cada servicio.
- 🔁 Opción a **Comienzo** o **Para.** servicios desde la interfaz web.
- 🛠 Designed for use by **usuarios avanzados o administradores** con una fuerte comprensión de las dependencias de servicios.
- Cada servicio incluye metadatos como **versión de aplicación**.

---

### Buenas prácticas

- Siempre confirme horas de tráfico máximo antes de detener cualquier servicio crítico (por ejemplo, Cliente, DLR, Validador).
- Evite reiniciar servicios sin consultar registros del sistema o soporte técnico.
- Asegurar que los servicios de base de datos y portales estén sincronizados para prevenir incoherencias de datos.

---

El **Servicios de gestión** característica ofrece una manera centralizada de monitorear y controlar los procesos a nivel del sistema, garantizando operaciones fluidas dentro del entorno iTextPRO.
