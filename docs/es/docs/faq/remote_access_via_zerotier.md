# Cómo acceder al KVM de forma remota mediante ZeroTier {#how-to-access-kvm-remotely-via-zerotier}

> Nota: actualice el firmware del KVM a v1.8.0 antes de utilizar esta función.

Los KVM GL.iNet integran ZeroTier para vincularse a su red y permitir el acceso remoto sin instalar la aplicación GLKVM ni utilizar el servicio de nube.

Siga estos pasos para acceder de forma remota al KVM GL.iNet mediante ZeroTier.

## Activar ZeroTier {#enable-zerotier}

**Antes de empezar, conecte el KVM y el dispositivo de control a la misma red local.**

1. Abra un navegador en el dispositivo de control. Se recomienda Chrome o Edge para una mayor compatibilidad.

2. Acceda de forma local a la consola KVM mediante su dominio o IP. En este ejemplo se utiliza la dirección IP local.

    Introduzca la **IP de LAN** del KVM, que encontrará en su pantalla táctil o en el router, en la barra de direcciones. Se abrirá la página de inicio de sesión de GLKVM. Introduzca la contraseña de administrador.

    ![Acceso local mediante la IP](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/1_local_access.png){class="glboxshadow"}

3. Vaya a **Apps Center** -> **ZeroTier**. Active ZeroTier y aparecerá el aviso amarillo que se muestra a continuación.

    Haga clic en el enlace del aviso o [aquí](https://my.zerotier.com/){target="_blank"} para iniciar sesión en ZeroTier Central y crear su red ZeroTier.

    ![Activar ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/2_enable_zerotier.png){class="glboxshadow"}

## Vincular el KVM a ZeroTier {#bind-kvm-to-zerotier}

1. Al iniciar sesión en [ZeroTier](https://my.zerotier.com/){target="_blank"} por primera vez, puede que deba seleccionar una versión de ZeroTier Central.

    ![Seleccionar Central](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/3_select_central.png){class="glboxshadow"}

    Seleccione la versión adecuada para continuar. En este ejemplo se utiliza **New Central**.

    Inicie sesión con su correo electrónico y contraseña. Si no tiene cuenta, regístrese primero.

    ![Iniciar sesión en ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/4_zerotier_signin.png){class="glboxshadow"}

2. Después de iniciar sesión, cree una organización.

    ![Crear una organización](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/5_create_org.png){class="glboxshadow"}

3. Seleccione un plan. En este ejemplo se utiliza **Personal**, que incluye 10 dispositivos, 1 administrador de red y 1 red. Si necesita más redes o dispositivos, rutas personalizadas o DNS, elija Essential o Scale.

    ![Seleccionar un plan](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/6_select_plan.png){class="glboxshadow"}

4. Su red ZeroTier ya está creada. Copie el **Network ID**, una cadena alfanumérica de 16 caracteres que necesitará para añadir dispositivos a la red. Mantenga abierta esta pestaña.

    ![Identificador de red](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/7_copy_network_id.png){class="glboxshadow"}

5. Vuelva a la consola KVM y vaya a **Apps Center** -> **ZeroTier**. Busque **Network ID** y haga clic en **Set**.

    ![Establecer el identificador de red](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id1.png){class="glboxshadow"}

    Pegue el **Network ID** en la ventana emergente y haga clic en **Confirm**.

    ![Confirmar el identificador de red](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id2.png){class="glboxshadow"}

    Un aviso amarillo indicará que debe autorizar el dispositivo.

    ![Autorización pendiente](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize1.png){class="glboxshadow"}

6. Vuelva a ZeroTier Central. Verá el KVM pendiente de aprobación. Haga clic en **Authorize**.

    ![Autorizar el KVM](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize2.png){class="glboxshadow"}

    Una vez autorizado, el estado cambiará a Authorized en verde.

    ![KVM autorizado](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized1.png){class="glboxshadow"}

    También podrá consultar **Network ID** y **Virtual IP** en la consola KVM.

    ![Información de ZeroTier en la consola KVM](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized2.png){class="glboxshadow"}

## Vincular el dispositivo de control {#bind-the-controlling-device}

Este ejemplo muestra cómo vincular un portátil Windows, que actuará como dispositivo de control, a la red ZeroTier.

1. Instale ZeroTier en el portátil desde [aquí](https://www.zerotier.com/download/){target="_blank"}.

2. Ejecute ZeroTier en el portátil y añádalo a la misma red ZeroTier.

    ZeroTier no muestra una ventana o interfaz independiente en el escritorio; solo aparece como un icono en la bandeja del sistema, en la esquina inferior derecha. Todas las operaciones se realizan desde su menú contextual.

    Haga clic con el botón derecho en el icono de ZeroTier y seleccione **Join New Network**. Introduzca el mismo **Network ID** en la ventana emergente para añadir el equipo a esa red.

    ![Unirse a la red](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/11_pc_join_network.jpg){class="glboxshadow"}

    Después vaya a ZeroTier Central, busque el dispositivo Pending y autorícelo.

    ![Autorizar el portátil](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/12_authorize.png){class="glboxshadow"}

2. Una vez autorizado, el estado cambiará a Authorized en verde.

    ![Portátil autorizado](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/13_authorized.png){class="glboxshadow"}

3. El KVM y el portátil ya pertenecen a la misma red ZeroTier. Puede comprobarlo comparando sus Network ID, como se muestra a continuación.

    ![Ambos dispositivos en la misma red ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/14_same_zt_network.png){class="glboxshadow"}

## Acceso remoto mediante ZeroTier {#remote-access-via-zerotier}

Este ejemplo muestra cómo acceder de forma remota a la consola KVM mediante la dirección IP de ZeroTier.

1. En el portátil, inicie sesión en ZeroTier Central con su cuenta, busque el KVM y haga clic en su **ZT IP** para copiarla.

    ![IP de ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/15_zerotier_ip.png){class="glboxshadow"}

2. Abra una nueva pestaña del navegador, pegue la IP de ZeroTier en la barra de direcciones y pulse Intro. Se abrirá la página de inicio de sesión de GLKVM.

    Introduzca la contraseña de administrador. Ya puede acceder al KVM GL.iNet y al dispositivo controlado mediante la IP de ZeroTier.

    ![Acceso remoto mediante ZeroTier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/16_remote_access.png){class="glboxshadow"}

    **Consejo**: puede aparecer una advertencia de privacidad al acceder a esta IP por primera vez. Haga clic en **Advanced** -> **Proceed** para continuar. Consulte [Advertencia de privacidad en el navegador](privacy_error_from_your_browser.md){target="_blank"}.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
