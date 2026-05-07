
# Normalización del cuerpo del mensaje

El **Normalización del cuerpo del mensaje** Regla es una característica incorporada dentro **Power SMPP**, diseñado para dar a los administradores flexibilidad para modificar y perfeccionar el contenido del mensaje antes de sumisión a la puerta de entrada. 
Esto garantiza que todos los mensajes salientes se formatee correctamente, mejorando la legibilidad y la eficacia.

Este documento explica cómo **Normalización del cuerpo del mensaje** funciona y cómo los administradores pueden configurarlo para ajustar automáticamente el contenido de mensajes basado en reglas predefinidas, garantizando la coherencia y el cumplimiento de los requisitos de gateway.

---

## Características clave

La Regla de Normalización del Cuerpo de Mensajes amplía la existente **OA/DA Normalization Rule**. Proporciona múltiples maneras de manipular el contenido del mensaje, incluyendo:

- **Extracción de Códigos/OTPs:** Detecta y extrae automáticamente OTPs o códigos específicos del texto del mensaje. 
- **Añadir Prefijos o Sufijos:** Insertar texto específico antes o después del mensaje para mantener un formato estándar. 
- **Reemplazo de texto:** Sustitúyase ciertas palabras o frases según reglas predefinidas para una mejor consistencia.

Estas opciones ayudan a los administradores a asegurar que todos los mensajes se ajusten a las normas de gateway, mejorando la experiencia general de mensajería.

---

## Acceso a la Normalización del Cuerpo del Mensaje

Para configurar la Normalización del Cuerpo del Mensaje:

1. Navigate a la **Módulo de configuración**. 
2. Seleccione **Configuración de entrada**. 
3. Elija **Normalización del cuerpo del mensaje**. 
4. Haga clic **Añadir nuevo** crear una nueva regla de normalización.

![Message Body Normalization UI](images/mbn1.png)

---

## Configuración de reglas

Una vez que haga clic **Añadir nuevo**, una página de configuración aparece con múltiples campos.

### **Nombre de la regla**
Define un nombre descriptivo y significativo para la regla.

---

### **Ajustes de condición**

#### 1. Seleccionar interfaz
Especifique la interfaz donde se aplica la regla. Puede seleccionar uno o más de los siguientes:

- WEB 
- API 
- SMPP 
- Todas las interfaces 

![Interface Selection](images/mbn3.png)

Esto permite la aplicación de reglas específicas dependiendo de la interfaz operacional.

---

#### 2. Usuario
Elija si la regla se aplica a:
- A specific **Usuario**o 
- **CUALQUIER** (aplica a todos los usuarios).

---

#### 3. ID de remitente
Configure Sender ID conditions based on specific matching patterns:

- **Igualdad** – Coincide exactamente con el ID de remitente especificado 
- **Empieza con** – Trucos si el ID del remitente comienza con una palabra clave específica 
- **Fin con** – Aplica si el ID del remitente termina con una palabra clave específica 
- **Contains** – Aplica si la palabra clave se encuentra en cualquier lugar del ID del remitente 

![Sender ID Condition](images/mbn4.png)

---

#### 4. Dirección de destino
Funciones similares a **ID del remitente**, permitiendo las mismas condiciones *Igualdad*, *Empieza con*, *Fin con*, *Contains* — aplicar reglas basadas en el formato de dirección de destino.

---

#### 5. Mensaje
Las mismas opciones condicionales que arriba se pueden aplicar al contenido de mensajes, permitiendo un control preciso de formato.

---

## Medidas: Explicación detallada

In **Power SMPP**, el **Medida** sección ofrece tres métodos configurables para manipular el contenido del mensaje antes de sumisión a la puerta de entrada:

1. **Código de Extracción** 
2. **Encontrar y reemplazar** 
3. **Apéndice y prependimiento**

Cada uno sirve un caso de uso específico. Vamos a explorar cada uno en detalle.

---

### 1⃣ Código de Extracción

El **Código de Extracción** acción permite que los administradores tiren OTPs o códigos de mensajes.

#### a) De la plantilla fija
Si el mensaje tiene un patrón fijo, puede utilizar <span data-ph="0"></span> para definir el conteo de caracteres para la extracción.

**Ejemplo:**

- Mensaje: <span data-ph="0"></span> 
- Configuración: <span data-ph="0"></span> 
- Producto: <span data-ph="0"></span> 

![Extract Code - Fixed Template](images/mbn6.png)

---

#### b) Por su índice de incidencia
Use esto cuando los mensajes contienen múltiples códigos, y desea extraer uno por su índice.

**Ejemplo:**
- Mensaje: <span data-ph="0"></span> 
- Configuración: 
  - Duración: <span data-ph="0"></span> 
  - Índice: <span data-ph="0"></span> 
- Producto: <span data-ph="0"></span>

![Extract Code - Occurrence Index](images/mbn7.png)

---

### 2⃣ Encontrar y reemplazar

Utilice esto para reemplazar palabras o frases específicas en el mensaje.

**Ejemplo:**
- Mensaje: <span data-ph="0"></span> 
- Configuración: 
  - Encontrar: <span data-ph="0"></span> 
  - Reemplazar: <span data-ph="0"></span> 
- Producto: <span data-ph="0"></span>

![Find and Replace](images/mbn8.png)

---

### 3⃣ Append and Prepend

Esto permite añadir texto personalizado antes (prepend) o después (apéndice) del mensaje, o ambos.

#### a) Apéndice  
Añade texto al **final** del mensaje. 
**Ejemplo:** 
- Mensaje: <span data-ph="0"></span> 
- Apéndice: <span data-ph="0"></span> 
- Producto: <span data-ph="0"></span> 

![Append Example](images/mbn10.png)

---

#### b) Prependientes  
Añade texto al **Comienzo** del mensaje. 
**Ejemplo:** 
- Mensaje: <span data-ph="0"></span> 
- Prependiendo: <span data-ph="0"></span> 
- Producto: <span data-ph="0"></span> 

![Prepend Example](images/mbn11.png)

---

#### c) Ambos  
Añade un prefijo y sufijo. 
**Ejemplo:** 
- Mensaje: <span data-ph="0"></span> 
- Prependiendo: <span data-ph="0"></span> 
- Apéndice: <span data-ph="0"></span> 
- Producto: <span data-ph="0"></span> 

![Append and Prepend Both](images/mbn12.png)

---

## Combinando múltiples acciones

Los administradores pueden aplicar múltiples acciones dentro de una sola regla.

**Ejemplo:**
- Mensaje: <span data-ph="0"></span> 
- Acciones: 
  - Código de Extracto (De Plantilla fija) 
  - Apéndice y Prependimiento (Tantos) 

Esto extrae el OTP y aplica formato de texto adicional como configurado.

![Combined Actions](images/mbn13.png)

---

## Prioridad y compatibilidad

- **Normalización del cuerpo del mensaje** ejecutadas **antes** el **OA/DA Normalización**. 
- Esto asegura que el contenido de mensajes se optimiza y formatea primero, evitando conflictos de reglas. 
- Ambas reglas de normalización funcionan en capas para la presentación precisa de la puerta de entrada.

---

## Resumen

**Normalización del cuerpo del mensaje** en Power SMPP permite a los administradores:
- Extraer OTPs o códigos, 
- Añadir prefijos/suffixes, 
- Sustitúyase palabras o frases, 
- Combine múltiples reglas, y 
- Aplica reglas por usuario, remitente o interfaz. 

Esta característica garantiza que todos los mensajes mantengan un formato coherente y cumplan con los requisitos de gateway: mejorar la fiabilidad y profesionalidad en la entrega de mensajes.
