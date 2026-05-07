
# Números de lista blanca

El **Números de lista blanca** característica permite a los administradores definir una lista de números móviles de lista blanca global. Cuando **DLR compensation** está habilitado en la solicitud, cualquier mensaje enviado a un número incluido en la lista blanca siempre será enviado al proveedor y **no se considerará la indemnización DLR**, independientemente del estado de entrega.

## Propósito

Esta característica es útil para excluir números específicos (como números de prueba, números de monitoreo interno o contactos prioritarios) de la lógica de compensación al tiempo que garantiza la entrega de mensajes ininterrumpida.

![White List Numbers](images/whitelist1.png)

---

## Agregar números a la lista blanca

1. Navigate a la **Números de lista blanca** sección del panel de administración.
2. Haga clic en **Añadir nuevo**.
3. Introduzca los números móviles en el campo de entrada.
4. Múltiples números se pueden añadir inmediatamente separandolos con comas (<span data-ph="0"></span>).
5. Garantizar que **cada número de móvil incluye el código de país** (por ejemplo, +91XXXXXXXXXX).
6. Guardar los cambios para aplicar las entradas de la lista blanca a nivel mundial.

![Add Whitelist Numbers](images/whitelist2.png)

---

## Eliminar números de lista blanca

El soporte de aplicación **Eliminación masiva**, permitiendo a los administradores eliminar múltiples entradas de lista blanca en una sola acción.

Los administradores también pueden suprimir **entradas seleccionadas individualmente** según sea necesario.

![Bulk Delete Whitelist](images/whitelist4.png)

---

## Notas clave

!!! info "Importante"
    - Se aplican números de lista blanca **globalmente a través de la aplicación**.
    - Los mensajes enviados a estos números son **excluidos de los cálculos de las indemnizaciones DLR**.
    - El formato adecuado con códigos de país es obligatorio para una correcta funcionalidad.
