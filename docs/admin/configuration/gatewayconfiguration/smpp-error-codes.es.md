---
tags:
  - SMPP
  - Error Codes
  - Reference
  - Gateway
---

# Lista estándar del código de error SMPP

Esta página proporciona una referencia completa de todos los códigos de error del protocolo SMPP, códigos de error de aplicación iTextPro y códigos de error de iTextHub HTTP Gateway. Utilice esta referencia para diagnosticar fallos de entrega de mensajes vistos en informes, registros de PDU y espectadores de eventos.

---

## Códigos de error SMPP estándar

Estos son códigos de error de nivel protocolo definidos por la especificación SMPP v3.4. Son devueltos por el SMSC (Short Message Service Centre) en respuesta a las operaciones SMPP.

| Sr. No | Código de error (Hex) | Código de error (decimal) | Nombre del error | Descripción del error |
|--------|-----------------|---------------------|------------|-------------------|
| 1 | 0x00 | 0 | Mando ejecutado con éxito | El comando SMPP fue procesado sin errores |
| 2 | 0x01 | 1 | Duración del mensaje es inválida | La longitud del cuerpo del mensaje excede los límites permitidos |
| 3 | 0x02 | 2 | La duración del comando es inválida | El campo de longitud de comando PDU es incorrecto |
| 4 | 0x03 | 3 | ID de comando inválido | El ID de comando no es reconocido por el SMSC |
| 5 | 0x04 | 4 | Estado BIND incorrecto para el comando dado | El ESME intentó un comando que no se permite en su estado de unión actual |
| 6 | 0x05 | 5 | ESME Ya en estado de Libra | El ESME ya está obligado y no puede atar de nuevo |
| 7 | 0x06 | 6 | Bandera de Prioridad Inválida | El valor de la bandera prioritaria en el PDU no es válido |
| 8 | 0x07 | 7 | Bandera de entrega registrada inválida | El valor registrado de la bandera de entrega no es válido |
| 9 | 0x08 | 8 | Error de sistema | Un error del sistema general ocurrió en el SMSC |
| 10 | 0x0A | 10 | Dirección de Fuentes Inválidas | La dirección fuente (intendente) es nula o no se permite |
| 11 | 0x0B | 11 | Dirección de destino inválido | La dirección de destino (recipiente) es nula |
| 12 | 0x0C | 12 | El ID de mensaje es inválido | El ID de mensaje no existe |
| 13 | 0x0D | 13 | Bind Failed | La operación bind falló debido a problemas de autenticación o configuración |
| 14 | 0x0E | 14 | Contraseña inválida | La contraseña proporcionada durante el bind es incorrecta |
| 15 | 0x0F | 15 | ID del sistema inválido | No se reconoce el ID del sistema proporcionado durante el bind |
| 16 | 0x11 | 17 | Cancel SM Failed | La operación cancel sm no pudo completarse |
| 17 | 0x13 | 19 | Reemplace SM Failed | No se pudo completar la operación de sustitución |
| 18 | 0x15 | 21 | Tipo de servicio inválido | El parámetro service type no es válido |
| 19 | 0x33 | 51 | Número inválido de destinos | El número de destinos en submit multi es inválido |
| 20 | 0x34 | 52 | Nombre de la lista de distribución inválida | El nombre de la lista de distribución no existe |
| 21 | 0x40 | 64 | La bandera de destino es inválida (submit multi) | El dest flag en submit multi contiene un valor no válido |
| 22 | 0x42 | 66 | Submit w/replace unsupported | Se ha solicitado la funcionalidad de sustitución cuando no esté respaldada o inapropiada para el MC particular |
| 23 | 0x43 | 67 | Datos de campo inválidos esm class | El campo esm class contiene datos inválidos |
| 24 | 0x44 | 68 | No se puede presentar a la lista de distribución | El mensaje no se puede enviar a la lista de distribución especificada |
| 25 | 0x45 | 69 | submit sm, data sm o submit multi falló | La operación de presentación falló |
| 26 | 0x48 | 72 | Dirección de fuente inválida TON | El tipo de número para la dirección de origen es inválido |
| 27 | 0x49 | 73 | Dirección de fuentes inválidas | El indicador del plan de numeración para la dirección fuente es inválido |
| 28 | 0x51 | 81 | Dirección de destino inválida NPI | El indicador del plan de numeración para la dirección de destino es inválido |
| 29 | 0x53 | 83 | Sistema inválido campo tipo | El parámetro system type no es válido |
| 30 | 0x54 | 84 | Invalid replace if present flag | La bandera reemplaza if present contiene un valor inválido |
| 31 | 0x55 | 85 | Número inválido de mensajes | El número de mensajes parámetro es inválido |
| 32 | 0x58 | 88 | Error de interferencia | ESME ha superado los límites de mensajes permitidos (agitación de PTPS) |
| 33 | 0x61 | 97 | Tiempo de entrega programado inválido | El formato de tiempo de entrega programado o el valor es inválido |
| 34 | 0x62 | 98 | Período de validez del mensaje inválido | El período de validez del mensaje (tiempo de exposición) es inválido |
| 35 | 0x63 | 99 | ID de mensaje predefinido es inválido | El mensaje predefinido especificado no fue encontrado |
| 36 | 0x65 | 101 | Código de error de aplicación permanente del receptor ESME | Un error de aplicación permanente en el receptor ESME |
| 37 | 0x66 | 102 | Código de error del mensaje del receptor ESME | El receptor ESME rechazó el mensaje |
| 38 | 0x67 | 103 | Query Sm petición falló | La operación query sm no pudo completarse |
| 39 | 0xC0 | 192 | Error en la parte opcional del Cuerpo de PDU | Los parámetros opcionales TLV en el cuerpo PDU contienen errores |
| 40 | 0xC1 | 193 | TLV no está permitido | El parámetro TLV no está permitido para esta operación |
| 41 | 0xC2 | 194 | Longitud del parámetro inválido | Un parámetro TLV tiene una longitud invalida |
| 42 | 0xC3 | 195 | TLV esperada desaparecida | Falta un parámetro TLV requerido del PDU |
| 43 | 0xC4 | 196 | Valor de TLV inválido | Un parámetro TLV contiene un valor no válido |
| 44 | 0xFE | 254 | Fallo de entrega de transacciones | La transacción de mensajes no puede ser entregada |
| 45 | 0xFF | 255 | Error desconocido | Se produjo un error desconocido o no especificado |
| 46 | 0x100 | 256 | ESME No autorizado a utilizar el tipo de servicio especificado | El ESME no está autorizado para el tipo de servicio solicitado |
| 47 | 0x101 | 257 | ESME Prohibido utilizar una operación especificada | El ESME está anclado o prohibido utilizar la operación especificada |
| 48 | 0x102 | 258 | Tipo de servicio especificado no está disponible | El tipo de servicio solicitado no está disponible actualmente |
| 49 | 0x103 | 259 | Se niega el tipo de servicio especificado | Se ha negado el tipo de servicio solicitado |
| 50 | 0x105 | 261 | Fuente Dirección Sub unidad es inválida | El parámetro subunidad de dirección fuente es inválido |
| 51 | 0x106 | 262 | Dirección Sub unidad es inválida | El parámetro subunidad de dirección de destino es inválido |
| 52 | 0x107 | 263 | Intervalo de frecuencia de radio es inválido | El parámetro de intervalo de frecuencia de emisión es inválido |
| 53 | 0x108 | 264 | El nombre de Alias de Radiodifusión es inválido | El nombre del alias no es válido |
| 54 | 0x109 | 265 | Formato de área de radiodifusión es inválido | El parámetro de formato de área de difusión es inválido |
| 55 | 0x10A | 266 | Número de zonas de radiodifusión es inválido | El número de áreas de difusión especificadas es inválido |
| 56 | 0x10B | 267 | Tipo de contenido de radio es inválido | El parámetro tipo de contenido de transmisión es inválido |
| 57 | 0x10C | 268 | Clase de mensaje de radio no es válida | La clase de mensajes de difusión es inválida |
| 58 | 0x10D | 269 | La operación Broadcast sm falló | La operación de radiodifusión no pudo completarse |
| 59 | 0x10F | 271 | Cancel broadcast sm falló la operación | La operación de cancelación broadcast sm no pudo completarse |
| 60 | 0x110 | 272 | Número de repetidas transmisiones es inválido | El número de repetidas transmisiones es inválido |
| 61 | 0x111 | 273 | El Grupo de Servicios de Radiodifusión es inválido | El parámetro del grupo de servicios de difusión es inválido |
| 62 | 0x112 | 274 | El indicador del canal de radiodifusión es inválido | El indicador del canal de difusión es inválido |
| 63 | 0x15F95 | 90005 | Excepción local | Check LastException alojamiento para detalles |

---

## Códigos de error iTextPro

Estos son códigos de error de nivel de aplicación generados por la plataforma iTextPro / Power SMPP. Indican problemas con las operaciones de enrutamiento, facturación, configuración de cuentas o sistema.

| Sr. No | Código de error (Hex) | Código de error (decimal) | Nombre del error | Descripción del error |
|--------|-----------------|---------------------|------------|-------------------|
| 64 | 0x439 | 1081 | País Undef | País no definido por admin en Master Data Manager |
| 65 | 0x43A | 1082 | Invalid Network | Red no definida por admin en Master Data Manager |
| 66 | 0x43B | 1083 | Precio No definido | Precios no definidos por admin para cada país y red en la puerta principal |
| 67 | 0x43C | 1084 | Expired (Protección de la pérdida) | Mensaje no entregado debido a la política de protección de pérdidas |
| 68 | 0x43D | 1085 | Route Undef | Routing no definido por admin para el país y la red respectivos |
| 69 | 0x43E | 1086 | Failover Route Undef | Fallo maestro no definido por admin para país y red respectivos |
| 70 | 0x43F | 1087 | Failover Expired | Mensaje no entregado debido a la Protección de Pérdida en puerta de failover |
| 71 | 0x440 | 1088 | Failover Price Undef | Precios no definidos por admin para el país respectivo y la red en la puerta de baja |
| 72 | 0x441 | 1089 | Failover Failed | Error del sistema: Excepción sin manipular durante el enrutamiento |
| 73 | 0x442 | 1090 | Validez de la cuenta | La validez de la cuenta de usuario ha expirado |
| 74 | 0x443 | 1091 | Error de codificación | Error del sistema: Error de codificación debido al valor de codificación de datos inválidos (puede regenerarse enviando valores de codificación de datos excepto 0 & 8) |
| 75 | 0x444 | 1092 | Error OA/DA | Error del sistema: Error OA/DA debido a un Regex inválido en las reglas de normalización |
| 76 | 0x445 | 1093 | Mensaje de búsqueda | Error del sistema: El mensaje de cola expirado debido a la salida de puerta prolongada |
| 77 | 0x446 | 1094 | Inválido HTTP Gateway Config | Error del sistema: configuración de entrada HTTP inválida o código de respuesta |
| 78 | 0x417 | 1047 | Cuenta de usuario Inactive | La cuenta de usuario es inactiva y no puede enviar mensajes |
| 79 | 0x400 | 1024 | Cuenta de usuario bloqueada | La cuenta de usuario ha sido bloqueada por el administrador |
| 80 | 0x401 | 1025 | Saldo insuficiente | Equilibrio insuficiente en la cuenta de usuario (prepago) |
| 81 | 0x402 | 1026 | Plantilla Mismatch | Desigualdad de la plantilla detectada: el contenido del mensaje no coincide con la plantilla aprobada |
| 82 | 0x405 | 1029 | ID de remitente inválido | Detectado de ID de remitente inválido o no aprobado |
| 83 | 0x407 | 1031 | Número global de lista negra | El número de destino está en la lista negra global |
| 83 | 0x40B | 1035 | Sin conexión activa | No hay conexión SMPP activa disponible en la puerta de entrada |
| 84 | 0x40C | 1036 | Error de servidor de búsqueda | Error del sistema: error del servidor interno de la cola del mensaje |
| 85 | 0x40D | 1037 | Error del servidor de caché | Error del sistema: error de la base de datos de caché |
| 86 | 0x40E | 1038 | Estado de conexión inválida | Error de red: Gateway no accesible |
| 87 | 0x40F | 1039 | SMPP Timeout | Error de red: tiempo de entrada — no se recibió respuesta |
| 88 | 0x410 | 1040 | Error SMPP desconocido | Error del sistema: Se produjo un error SMPP no clasificado |
| 89 | 0x411 | 1041 | Desconexión final | La conexión SMPP se desconectó permanentemente |
| 90 | 0x412 | 1042 | Final Timeout | La conexión se fijó permanentemente |
| 91 | 0x413 | 1043 | No Gateway Found | No hay puerta de entrada adecuada para enrutar el mensaje |
| 92 | 0x404 | 1028 | IP inválida | Dirección IP inválida para la cuenta SMPP (la validación IP falló) |
| 93 | 0x414 | 1044 | Spam Detected | Mensaje fallado debido a la palabra clave de spam detectada en contenido |
| 94 | 0x448 | 1096 | Duración del mensaje | Longitud del mensaje SMS superó el límite permitido |

---

## iTextHub HTTP Códigos de error de puerta

Estos códigos de error son devueltos por el iTextHub HTTP Gateway al procesar las solicitudes de HTTP API.

| Sr. No | Código de error (decimal) | Nombre del error | Descripción del error |
|--------|---------------------|------------|-------------------|
| 95 | 110 | Error al recibir respuesta de texto | Failed to retrieve text response from the HTTP gateway |
| 96 | 111 | Error al recibir respuesta JSON/XML | Failed to parse JSON or XML response from the HTTP gateway |
| 97 | 112 | Error al leer respuesta | Failed to read the HTTP response stream |
| 98 | 113 | Error al leer la respuesta del resultado | Failed to extract data from the HTTP response result |
| 99 | 114 | Error al solicitar REST/JSON API | Failed to make a REST/JSON API request to the HTTP gateway |
| 100 | 115 | Error al solicitar Simple HTTP API | Failed to make a Simple HTTP API request to the HTTP gateway |
| 101 | 116 | Error al solicitar SOAP API | Failed to make a SOAP API request to the HTTP gateway |
| 102 | 1095 | Error al solicitar SOAP/Simple/RestJson API | Código de error combinado para 114, 115 y 116 (utilizado en la última versión) |

---

!!! tip "Cómo utilizar esta referencia"
    - Cuando vea un código de error en su **Campaign Reports**, **PDU Logs**o **Event Viewer**, míralo en las tablas arriba
    - **Códigos SMPP estándar** (0–255) son devueltos por el SMSC/gateway externo
    - **iTextPro codes** (1024–1096) son generados internamente por la plataforma Power SMPP
    - **Códigos HTTP GW** (110–1095) se refieren a problemas de conectividad de puerta HTTP
    - Para la configuración del código de error específico de la puerta de entrada, véase [Códigos de error de la autopista](errorcode.md)
