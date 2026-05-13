---
tags:
  - HTTP
  - DLR
  - Handler
  - Configuration
---

# Configuración de HTTP DLR Handler

Una vez que el HTTP Gateway haya sido configurado sobre la aplicación, el usuario podrá enviar mensajes y la respuesta será actualizada en la aplicación.

!!! note
 El **Gateway Response** es sólo **Primera respuesta** , que indica si los mensajes se han presentado al proveedor con éxito o no.

Para recibir **DLR (Delivery Receipt)** del proveedor, el administrador necesita configurar un **HTTP DLR Handler** para que cada vez que el proveedor envía el DLR, el DLR será actualizado sobre la aplicación utilizando el controlador DLR.

En este documento, compartiremos todos los pasos y la configuración que necesite el administrador para recibir correctamente el DLR sobre la aplicación.

---

## Navegación

<span data-ph="0"></span> ➔ <span data-ph="1"></span> ➔ <span data-ph="2"></span> ➔ <span data-ph="3"></span>.

---

## Muestra de carga DLR

Para configurar el HTTP DLR Handler, necesitaremos el **Formato de respuesta DLR** o una muestra DLR del proveedor para que el administrador pueda completar la configuración sobre la aplicación.

Por ejemplo, utilizaremos la siguiente muestra DLR para la configuración de HTTP DLR Handler:

```json
{
    "messageId": "161a9168-623c-4411-9e30-cf69353f9bef",
    "status": "EXPIRED",
    "errorCode": "1039",
    "mobile": "91123537072",
    "shortMessage": "Test Message",
    "doneDate": "2024-05-22 11:07:46"
}
```

---

## Pasos de configuración

Siga los siguientes pasos para configurar el controlador DLR para la muestra DLR proporcionada anteriormente:

1. **Agregar un nombre de usuario amigable** para el manejador.
2. **Whitelist la IP del vendedor** *(No obligatorio)*.
3. **Seleccione el método compatible** por el vendedor <span data-ph="0"></span> o <span data-ph="1"></span>.
4. **Configure Payloads** — Bajo las cargas de pago, el cliente necesita configurar el nombre del parámetro que almacena los valores específicos.

### Referencia relativa a la elaboración de mapas

| Aplicación | Mapas a JSON Key | Valor de ejemplo |
|-------------------|------------------|---------------|
| **MessageId** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Estado del mensaje** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Fecha** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Código de error** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **Número de móvil** | <span data-ph="0"></span> | <span data-ph="0"></span> |
| **ID del remitente** | *(opcional, mapa si el vendedor lo envía)* | — |
| **Mensaje** | <span data-ph="0"></span> | <span data-ph="0"></span> |

!!! tip
 En el ejemplo anterior, el parámetro <span data-ph="0"></span> almacena el valor del estado DLR y <span data-ph="1"></span> almacena el valor del código Error. Estos parámetros deben ser configurados como en **Estado del mensaje** y **Código de error** respectivamente. Aplicar la misma lógica para todos los demás parámetros compartidos por el vendedor.

---

## Local Endpoint

Cuando el manipulador se guarda, Power SMPP genera un **Local Endpoint** URL (por ejemplo, <span data-ph="0"></span>). Esta es la URL que el vendedor devolverá con cargas DLR.

!!! warning "Importante"
 Una vez que todos los detalles han sido configurados sobre la aplicación, **guardarlo y por favor llegar a su proveedor de la puerta de entrada y pedirles que blanquee el punto final del controlador DLR al final**.

---

## Valores predeterminados

Para el **Estado del mensaje** y **Código de error** campos, opcional <span data-ph="0"></span> se puede configurar. El valor predeterminado se aplica cuando el vendedor no devuelve ese campo en un DLR particular. Esto asegura que el registro DLR aún está completo y el mensaje está cerrado en los informes.

---

## Verificación

Después de configurar el controlador DLR:

1. Envíe un mensaje de prueba a través de la entrada HTTP correspondiente.
2. Pregúntele al proveedor (o utilice una herramienta de prueba como <span data-ph="0"></span> / <span data-ph="1"></span>) para enviar una muestra de carga DLR a la URL local de Endpoint.
3. Abrir el relevante **DLR Report** dentro <span data-ph="0"></span> para confirmar que el DLR ha sido recibido y analizado correctamente.

Si el DLR no aparece, vuelva a revisar los mapas del nombre del parámetro — la causa más común es un desajuste entre la tecla JSON que envía el vendedor y la clave configurada en el manejador.
