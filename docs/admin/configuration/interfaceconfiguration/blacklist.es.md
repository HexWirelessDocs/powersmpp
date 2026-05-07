
## ESME Blacklist Rule

El **ESME Blacklist Rule** en iTextPRO sirve como una salvaguardia proactiva para proteger a su servidor SMPP de clientes corruptos o mal configurados de ESME. Estos clientes pueden causar degradación del rendimiento debido a solicitudes de comando repetidas o anormales. Al establecer esta regla, los administradores pueden **automaticamente blacklist** clientes sospechosos y evitar nuevos daños.

---

### Propósito

En escenarios en los que un usuario rogue ESME plantea una amenaza, ya sea de aplicación defectuosa o solicitudes de alta frecuencia no intencionadas, esta regla permite a iTextPRO abandonar permanentemente las solicitudes de ese usuario, manteniendo **estabilidad e integridad del servidor**.

---

### Opciones de configuración

![Blacklist Rule Setup](images/blacklist1.png) 
![Blacklist Rule Fields](images/blacklist2.png)

Para configurar una nueva Regla ESME Blacklist:

1. **Nombre de la regla**: 
   - Introduzca un nombre descriptivo y amistoso para la regla de la lista negra (por ejemplo, <span data-ph="0"></span>).

2. **Usuario**: 
   - Seleccione la cuenta de usuario ESME que la regla debe monitorizar.

3. **ESME System ID**: 
   - Elija el específico **ID del sistema** del usuario ESME.

4. **Tipo de comando**: 
   - Elija el tipo de comando para monitorizar:
     - **Preguntar Enlace**
     - **Bind**

5. **Intervalo de tiempo**: 
   - Establecer el intervalo en:
     - Horas
     - Minutes
     - Segundos

6. **Frecuencia**: 
   - Defina cuántas veces puede ocurrir el tipo de comando seleccionado dentro del intervalo de tiempo especificado.

7. Después de llenar los detalles, haga clic **"Save"** para activar la regla.

---

### Ejemplo de casos de uso

Supongamos que desea bloquear un usuario ESME que envía **Solicitudes de enlace o búsqueda** más que más **10 veces dentro de 1 minuto**. 
- Set <span data-ph="0"></span> 
- Set <span data-ph="0"></span> 
- Si se cumple la condición, iTextPRO:
  - **Lista negra de la cuenta ESME**
  - **Enviar una alerta a la dirección de correo electrónico registrada**

Esto evita que los clientes abusivos o malconfigurados sobrecargan el servidor SMPP.

---

### Resultado " Alertas

Una vez violada la norma:
- El ESME es automáticamente **negras**.
- An **Alerta de correo electrónico** es enviado al administrador.

![Blacklist Result](images/blacklist3.png)

---

### Resumen

El **ESME Blacklist Rule** es una característica vital para:
- Detectar comportamiento anormal o abusivo del cliente.
- Protege tu infraestructura de la degradación del rendimiento.
- Automatizar la mitigación mediante la aplicación de la lista negra en tiempo real.

Utilice esta característica para mantener robusto **Función del servidor SMPP** y hacer cumplir la higiene operacional en todas las conexiones ESME.
