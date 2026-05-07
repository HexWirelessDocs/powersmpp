
# Utilidad – Transferencia de cola a cola

El **Transferencia de Queue a Queue** característica en iTextPro permite la transferencia sin problemas del tráfico de SMS entre las pasarelas, asegurando una gestión eficiente de las operaciones de mensajería. 
Esta funcionalidad es particularmente útil cuando tu **puerta principal** experiencias inactividad o no funciona. Al utilizar esta opción, puede **redirigir el tráfico a una puerta de entrada alternativa**, asegurando una comunicación ininterrumpida.

![Queue-to-Queue Overview](../images/queue1.png)

---

## Configuración de transferencia

### 1. Propósito de transferencia
Especifique el propósito o la razón para transferir el tráfico SMS. 
Esto ayuda a mantener **registros claros** y proporciona contexto para la transferencia.

### 2. Fuente Gateway
Seleccione **puerta de entrada** de los cuales se transferirán mensajes. 
iTextPro permite elegir el **línea de mensaje específica** asociado con esta puerta de entrada.

### 3. Portal de destino
Elija el **destino** donde se deben enviar mensajes. 
Esto asegura que el tráfico sea redirigido al punto final operacional correcto.

### 4. Iniciación de la Transferencia
Una vez que se establezcan los parámetros de transferencia:
- Haga clic en **"Añadir trabajo"** botón.
- iTextPro añadirá el trabajo a la cola de transferencia.
- El sistema transferirá automáticamente mensajes de los seleccionados **puerta de entrada** a la **destino**.

Este proceso sin costura garantiza **continuidad de los servicios SMS** incluso en caso de salidas de puerta.

![Queue Transfer Execution](../images/queue2.png)
