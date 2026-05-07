---
tags:
  - Monitoring
  - PDU
  - Troubleshooting
---

# Supervisión

iTextPRO proporciona una amplia **Instrumentos de vigilancia** para garantizar el rendimiento óptimo de la entrega de SMS y la estabilidad del sistema. Esto incluye **en tiempo real Monitoreo en vivo** para información de tráfico y una robusta **PDU Logger** para el análisis profundo del nivel de mensajes.

---

## Vigilancia en vivo

El **Vigilancia en vivo** módulo en iTextPRO rastrea dinámicamente y analiza puntos clave de datos relacionados con el tráfico de SMS, permitiendo **toma de decisiones en tiempo real** para el enrutamiento y la optimización del rendimiento.

### Beneficios clave
- **Proactive Traffic Management** – Gestionar el tráfico SMS dinámicamente basado en datos en vivo.
- **Routing optimizado** – Tomar decisiones informadas de enrutamiento para mejorar las tasas de entrega.
- **Asignación de recursos eficiente** – Asignar recursos estratégicamente durante las horas pico.
- **Rendimiento mejorado** – Mejorar la capacidad de respuesta y el rendimiento con información en tiempo real.

**Resumen**, Live Monitoring asegura que los usuarios tienen **visibilidad de hasta el minuto** a flujo de tráfico SMS, especialmente durante períodos de alta demanda.

---

## PDU Logs

iTextPRO emplea un **PDU (Protocol Data Unit) Logger** para capturar y registrar cada mensaje entrando o saliendo del SMSC. Esta herramienta es vital para **solución de problemas**, **Supervisión**, y **mantenimiento** salud del sistema.

### Características clave
- **Viaje de Mensaje en tiempo real** – Logra cada mensaje en tiempo real para el análisis inmediato.
- **Capacidades de filtración** – Trazar el viaje de un mensaje con un clic.
- **Soporte tipo PDU** – Inspeccione SubmitSM, DeliverSM, Bind, Unbind, y más.
- **Visibilidad " Retención "** – Los registros siguen el **Zona horaria de administración** y se mantienen **3 días**.
- **Inspección de tráfico** – Ver el flujo de mensaje seleccionando las puertas de una lista desplegable.
- **Apoyo a la solución de problemas** – Diagnóstico rápido de los problemas de entrega o sesión SMPP.

![PDU Logs](images/pdulogs1.png)

### Directrices de uso
1. Acceso **PDU Logger** desde la interfaz iTextPRO.
2. Aplicar **filtros** para aislar e inspeccionar mensajes específicos.
3. Uso **Registros de tráfico de aguas arriba** para verificar los viajes de mensajes.
4. Perform **Supervisión periódica** para mantener la fiabilidad del sistema.

---

## Niveles de Verbosidad en PDU

El registro PDU de iTextPRO admite múltiples **niveles de verbosidad**, proporcionando información detallada sobre la comunicación entre las puertas de iTextPRO y SMPP.

| Nivel de verbosidad | Propósito | Medida |
|-----------------|---------|--------|
| **Bind Request** | Initiates SMPP binding | iTextPRO envía una solicitud para conectarse a la puerta de entrada SMPP |
| **Respuesta bind** | Confirma la unión SMPP | La puerta de entrada SMPP responde a la solicitud de enlace |
| **Preguntar Enlace Solicitud / Respuesta** | Examen de la salud de la sesión del SMPP | iTextPRO envía solicitud cada 30s; la puerta responde |
| **Submit SM Solicitud** | Solicitud de envío de mensajes | iTextPRO envía un SMS al portal SMPP |
| **Submit SM Response** | Agradecimientos | Gateway responde a la comunicación de mensajes |
| **Deliver SM Solicitud** | Informe de entrega (DLR) recepción | El portal SMPP envía el estado de entrega |
| **Deliver SM Respuesta** | Reconocimiento del DLR | iTextPRO confirma la recepción de DLR |
| **Solicitud unbind** | Terminación de la sesión | iTextPRO o gateway inicia solicitud unbind |

**Importancia:** Estos registros dan a los administradores a **vista granular de los flujos de mensajes**, ayudar a detectar, diagnosticar y resolver problemas de manera eficiente.

---

Con **Vigilancia en vivo** y **PDU Logging**iTextPRO faculta a los administradores para mantener un **sistema de envío de SMS altamente fiable**, detectar proactivamente problemas y optimizar el tráfico en tiempo real.
