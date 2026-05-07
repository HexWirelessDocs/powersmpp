

# Permisos

## Función de la cuenta Premios ejecutivos en iTextPRO

In **iTextPRO**, administradores y revendedores pueden otorgar privilegios específicos **Función de la cuenta**, adaptando su acceso a áreas de trabajo designadas. 
Se pueden crear múltiples funciones ejecutivas para atender diversas responsabilidades.

### Funciones de ejemplo

**Función del Equipo de Finanzas**
- 📊 Acceso a la Sección de Facturación
- 📈 Acceso a la Sección de Informes
- Otros privilegios pertinentes

**Función del equipo de NOC**
- 📜 Monitoring Log Access
- 📊 Acceso a la Sección de Informes
- Opciones de administración
- Otros privilegios pertinentes

**Procedimientos de iniciación:**
- **Ejecutivo de Admin:** Utilice la URL de inicio de sesión de Admin y Puerto.
- **Ejecutivo de Reseller:** Utilice la URL de inicio de sesión del revendedor y el puerto.

Esta segregación garantiza una experiencia de acceso segura y específica para los ejecutivos, racionalizando el acceso a las funcionalidades acordes con sus responsabilidades.

![Permission Example](images/permission1.png)

---

## Categorías de permisos

Las permisos para usuarios ejecutivos en iTextPRO se clasifican según el nivel de acceso y las acciones dentro de los módulos.

### Categorías

**Vista** 
- Puede ver contenidos dentro del módulo especificado. 
- *No se permiten modificaciones ni eliminaciones.*

**Añadir** 
- Puede añadir nuevas entradas al módulo. 
- *No se puede editar o eliminar las entradas existentes.*

**Editar** 
- Puede editar/actualizar las entradas existentes. 
- *Sin derechos de eliminación.*

**Suprimir** 
- Puede eliminar las entradas del módulo. 
- *Sin derechos de edición.*

**Control completo** 
- Grants ver, añadir, editar y eliminar derechos para el módulo especificado. 
- Acceso sin restricciones.

![Permission Categories](images/permission2.png)

---

## Control completo " Jerarquía

In **iTextPRO**, **Control completo** proporciona acceso integral.

**Escenarios de activación:**
1. Activar el control completo en el **nivel superior** automáticamente se lo concede a todos los submódulos.
2. Habilitarlo para un **módulo específico** cubre Vista, Añadir, Editar y Eliminar.

**Jerarquía:**
- Los niveles representan diferentes secciones, funcionalidades o categorías de datos.
- Control completo en cascadas de nivel superior a todos los sub-nivel.

**Explicit Disabling:**
- Los permisos específicos en los submódulos pueden desactivarse manualmente, incluso con el control completo.

![Permission Hierarchy](images/permission3.png)

---

## Tipos de permiso

### Permisos de usuario individuales
- concede permisos a un usuario ejecutivo específico.

**Procedimiento:**
1. Ve. **Gestion Permission** página.
2. Seleccione **Individual** como tipo de permiso.
3. Elija un usuario de la desplegable.
4. Haga clic **Show** para ver / gestionar permisos.

![Individual Permissions](images/permission4.png)

---

### Permisos del Grupo Ejecutivo de Usuario
- concede permisos a un grupo; heredado por todos los miembros del grupo.

**Procedimiento:**
1. Ve. **Gestionar grupos de usuarios ejecutivos** página.
2. Haga clic **Agregar Grupo de Usuarios**.
3. Introduzca el nombre del grupo " select users.
4. Guarda el grupo.
5. Uso **Total Users** para ver a los miembros.
6. Editar o eliminar grupos según sea necesario.

📌 *Si un ejecutivo tiene permisos de usuario específicos y de grupo, consigue ambos.*

![Group Permissions](images/permission5.png)

---

## Módulo Visibilidad

- Si un Ejecutivo carece de permisos, verá un **"Access Denied"** página al iniciar sesión.
- Si los permisos se revocan mientras se registran, las acciones mostrarán **"Access Denied"**.
- Los módulos se muestran secuencialmente basados en permisos concedidos.

Ejemplo: 
- Si **Configuración** y **Facturación** se conceden, sólo esos módulos aparecen.

![All Modules](images/permission6.png) 
![Filtered Modules](images/permission7.png)