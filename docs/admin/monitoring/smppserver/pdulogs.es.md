
# Registros de PDU del servidor

El **SMPP Server PDU Logs** en iTextPRO son esenciales para **monitoreo y solución de problemas** transacciones de mensajes entre **Usuario ESME (Entidad de Mensaje corto externo)** y la plataforma iTextPRO. 
Estos registros capturan **tráfico de aguas abajo** y proporcionar detalles granulares que ayuden a resolver problemas de manera eficiente.

---

## Características clave
- **Registro de transacciones amplias** – Registra cada transacción de mensajes entre el usuario ESME y iTextPRO.
- **Apoyo a la solución de problemas** – Crítica para diagnosticar y resolver problemas de comunicación.
- **Zona horaria de Admin** – Los registros se muestran en la zona horaria del administrador para una referencia precisa.

---

## Tráfico de aguas abajo
Seguimiento de los **viaje de mensajes** desde el usuario ESME a iTextPRO, proporcionando visibilidad al flujo de entrega y estado.

![Server PDU Logs](images/pdulogs1.png)

---

## Niveles de verbosidad

Comprender el **niveles de verbosidad** ayuda en monitoreo y solución de problemas:

| **Nivel de verbosidad** | **Descripción** | **Propósito** |
|---------------------|-----------------|-------------|
| **Bind Request** | El usuario ESME inicia la conexión. | Establece conexión con iTextPRO. |
| **Respuesta bind** | iTextPRO responde a la solicitud de conexión. | Reconoce la conexión del usuario ESME. |
| **Solicitud de Enlace** / **Respuesta** | Llamada de comprobación de salud del usuario de ESME y respuesta correspondiente. | Verifica el estado de la sesión iTextPRO (intervalo recomendado: 30 segundos). |
| **Submit SM Solicitud** | El usuario de ESME inicia la solicitud de mensajes. | Envía mensajes SMS a iTextPRO. |
| **Submit SM Response** | iTextPRO responde a la solicitud de mensajes. | Reconoce la comunicación SMS. |
| **Deliver SM Solicitud** | DLR (Delivery Report) recibido por iTextPRO para un mensaje enviado. | Actualiza el estado de entrega para SMS enviado. |
| **Deliver SM Respuesta** | El usuario de ESME reconoce la solicitud DLR. | Confirma la recepción del estado de entrega. |
| **Solicitud unbind** | El usuario de ESME inicia solicitud unbind. | Termina las sesiones relacionadas. |

---

## Buenas prácticas
- **Revisión periódica de los registros** – Garantiza un monitoreo robusto y una rápida detección de problemas relacionados con las transacciones.
- **Leverage Verbosity Insights** – Utilice los detalles de PDU capturados para mantener una comunicación efectiva entre ESME e iTextPRO.
- **Prompt Action** – Abordar anomalías tan pronto como se detecten para mantener el rendimiento óptimo del sistema.
