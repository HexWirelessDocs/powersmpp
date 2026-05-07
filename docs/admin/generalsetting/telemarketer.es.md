
# Configuración de Telemarketer

Con la introducción de **Reglas de TRAI DLT**, tráfico de SMS en la India debe seguir un obligatorio **PE-TM Chain** (Entidad Principal-Telemarketer chain). Esta cadena garantiza la trazabilidad y el cumplimiento reglamentario de todas las partes interesadas en la entrega de mensajes, incluida la **Usuario, revendedor, aplicación y proveedor**.

Para cumplir con estas regulaciones, se debe configurar la aplicación **Apéndice la información requerida de Telemarketer** antes de enviar mensajes al vendedor o SMSC.

---

## Formación de la cadena PE-TM

La cadena PE-TM se construye dinámicamente durante la presentación de mensajes basado en **Tipo de vendedor**.

### Flujo de mensaje

1. El **usuario** presenta el mensaje junto con su **Principal Entity ID (PEID)**.
2. El **aplicación** apéndices configurados **Telemarketer ID (TMID)**.
3. La estructura final de la cadena depende del tipo de vendedor.

---

## Tipos de vendedor y formación de cadena

=== "Aggregator"

 An **Aggregator** es un vendedor intermedio que adelanta el mensaje a otro vendedor o SMSC.

    - La aplicación apéndice su **TMID**
    - El agregador anexa su propio **TMID2**
    - El mensaje se envía luego a la siguiente fuente

 **Formación de la cadena:** <span data-ph="0"></span>

    !!! info
 Hashing **no requerido** a nivel de aplicación para los proveedores de Aggregator.

=== "Asociado de animación"

 A **Socio de entrega** es el SMSC final responsable de entregar el mensaje al teléfono.

    - La aplicación apéndice su **TMID**
    - La cadena final debe ser **.** antes de la presentación

 **Formación de la cadena:** <span data-ph="0"></span>

    !!! info
 El hash asegura el cumplimiento de los requisitos de seguridad e integridad de TRAI.

---

## Configuración de Telemarketer en la aplicación

**Sendero de navegación:** <span data-ph="0"></span>

![Telemarketer Configuration List](images/telemarketer1.png)

---

## Pasos de configuración

1. Haga clic en **Añadir nuevo**
2. Seleccione **Nombre de la puerta**
3. Entra en **Telemarketer ID (TMID)**
4. Configurar el hashing basado en el tipo de vendedor:
    - **Aggregator:** Set **Es Hashing Active = OFF**
    - **Socio de entrega:** Set **Es Hashing Active = ON**
5. **Tipo de ceniza:**
    - Defaults to **SHA-256** (recomendado y compatible con el TRAI)
6. Haga clic **Guardar** para aplicar la configuración

![Telemarketer Configuration Dialog](images/telemarketer2.png)

---

!!! danger "Notas importantes"
    - Configuración incorrecta de corte puede resultar en **Rechazo DLT** por el vendedor o SMSC.
    - Garantizar el tipo de proveedor (Aggregator vs Delivery Partner) se confirma antes de la configuración.
    - SHA-256 se aplica como el algoritmo de piratería predeterminado para cumplir con los estándares regulatorios.
