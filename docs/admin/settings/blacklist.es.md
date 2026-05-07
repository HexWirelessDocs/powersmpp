
# Números de lista negra

El **Números de lista negra** función permite a los administradores definir una lista de números móviles que se bloquean a través de la aplicación. Una vez que se agrega un número a la lista negra, **todos los mensajes de salida a ese número son rechazados automáticamente por la aplicación**, y ningún usuario podrá enviar mensajes a él.

## Propósito

Esta característica se utiliza para prevenir la entrega de mensajes a números restringidos, inválidos, no compatibles o prohibidos para mantener el cumplimiento regulatorio y controlar el uso indebido.

![Blacklist Numbers](images/blacklist2.png)

---

## Agregar números a la lista negra

1. Navigate a la **Números de lista negra** sección en el panel de administración.
2. Haga clic en **Añadir nuevo**.
3. Introduzca los números móviles en el campo de entrada.
    - Múltiples números se pueden añadir inmediatamente separandolos con comas (<span data-ph="0"></span>).
4. Garantizar que **cada número de móvil incluye el código de país** (por ejemplo, +91XXXXXXXXXX).
5. Guardar los cambios para aplicar las entradas de la lista negra a través de la aplicación.

![Add Blacklist Numbers](images/blacklist3.png)

---

## Eliminar números de lista negra

El soporte de aplicación **Eliminación masiva**, permitiendo a los administradores eliminar múltiples entradas de lista negra en una sola operación.

Los administradores también pueden **eliminar entradas seleccionadas individualmente** según sea necesario.

![Bulk Delete Blacklist](images/blacklist4.png)

---

## Comportamiento de manejo de mensajes

!!! warning "Mensajes bloqueados"
    - Cualquier mensaje enviado a un número de lista negra será **bloqueado a nivel de aplicación**.
    - La solicitud de mensaje será **rechazado inmediatamente**, y no será enviado al vendedor.

!!! tip
 Garantizar que cada número de móvil incluya el **código de país** (por ejemplo, +91XXXXXXXXXX) para una correcta funcionalidad.
