---
tags:
  - WhatsApp
  - Plugin
  - Configuration
---

# Administración - Módulo WhatsApp

## 1. Descripción del servicio activo
**WhatsApp:** 
Al habilitar este plugin, el usuario podrá:
- Acceso y envío de mensajes a través de WhatsApp.
- Configure chatbots para respuestas automatizadas para sus negocios.

---

## 2. Créditos
- Los usuarios tienen un **saldo de cartera independiente para WhatsApp**.
- El administrador puede ver el saldo de crédito para **Mensajería SMS** y **WhatsApp** por separado.

**Pasos para añadir créditos:**
1. Haga clic **Añadir nuevo** para añadir créditos al saldo del usuario.
2. Seleccione **WhatsApp** de la lista de servicios.
3. Ingrese a **Referencia de pago**.
4. Entra en **Monto**.
5. Haga clic **Agregar créditos** para subir el balance del usuario.

![WhatsApp Admin Credits](images/whatsappadmin1.png)

---

## 3. Plan de tarifas de usuario
En la sección WhatsApp, puede asignar la **Plan de tarifas** para ser aplicado al usuario.

- Seleccione el plan de tarifas del menú desplegable.
- Todos los planes de tarifas configurados en **Facturación** sección aparecerá aquí para la selección.

---

### Planes de tarifas de WhatsApp
Similar a los planes de velocidad de mensaje MT, el administrador debe definir **Planes de tarifas específicos de WhatsApp** para manejar la facturación.

**Acciones disponibles:**
1. **Editar** – Cambiar el nombre del plan de tarifas o activar/desactivar el plan.
2. **Vista** – Ver y modificar todos los precios configurados en el plan de tarifas. Las actualizaciones se aplicarán a todos los usuarios asignados.
3. **Copiado** – Duplicar un plan de tarifas existente con un nuevo nombre.
4. **Suprimir** – Eliminar un plan de tarifas permanentemente. *(No se puede deshacer)*

![WhatsApp Admin Rate Plans](images/whatsappadmin2.png)

---

## Crear un nuevo plan de tarifas

**Paso 1:** 
- Entra en **Nombre del plan de tarifas amigables**.
- Elija **Activo/inactivo** estado.
- Haga clic **Continuar**.

![WhatsApp Admin Step 1](images/whatsappadmin3.png)

---

**Paso 2:** 
- Definir precios para el plan de tarifas.
- Configurar los detalles de facturación para el usuario.

![WhatsApp Admin Step 2](images/whatsappadmin4.png)

**Campos:**
- **Código del país** – Seleccione el país aplicable.
- **Precio del costo** – La cantidad cargada por META por mensaje.
- **Precio de venta** – El precio cargado al usuario por mensaje.
- **Plataforma de carga** – Tarifa opcional para usar su plataforma.

---

### Casos de uso

**Caso 1:** 
- Billing con META manejado por admin. 
- Sin cargo de plataforma. 
- **Créditos deducidos** según *Precio de venta*.

**Caso 2:** 
- Facturación con META manejada por el usuario. 
- Sólo se cobra cuota de plataforma. 
- **Precio de venta** mantenidos <span data-ph="0"></span>.

**Caso 3:** 
- Admin carga tanto el precio de venta como el precio de la plataforma. 
- Créditos deducidos **Precio de venta + tarifa de plataforma**.

---

**Paso 3:** 
- Review the **Resumen del plan de cuotas**.
- Asegúrese de que todos los detalles son correctos.
- Haga clic **Guardar** para finalizar.

---
