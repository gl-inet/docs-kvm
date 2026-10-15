# Cómo acceder al KVM de forma remota mediante NetBird {#how-to-access-kvm-remotely-via-netbird}

> Nota: actualice el firmware del KVM a v1.9.0 antes de utilizar esta función.

[NetBird](https://netbird.io/){target="_blank"} es una plataforma de redes de confianza cero y código abierto que permite crear redes privadas seguras para uso doméstico y empresarial. Su red superpuesta basada en WireGuard® permite acceder a los dispositivos de forma segura desde cualquier lugar y en cualquier momento.

Los KVM GL.iNet integran NetBird para vincularse a su red virtual y permitir el acceso remoto, sin instalar la aplicación GLKVM ni utilizar el servicio de nube.

Siga estos pasos para acceder de forma remota al KVM GL.iNet mediante NetBird.

## Vincular el KVM a NetBird {#bind-kvm-to-netbird}

**Antes de empezar, conecte el KVM y el dispositivo de control a la misma red local.**

1. Acceda a la consola KVM de forma local mediante su dominio o IP y vaya a **Apps Center** -> **NetBird**. Active NetBird y haga clic en **Bind Device**.

    ![Vincular el dispositivo](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/1-bind-device.png){class="glboxshadow"}

2. Se abrirá la página de confirmación del dispositivo. Haga clic en **Confirm**.

    ![Confirmar el dispositivo](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/2-confirm.png){class="glboxshadow"}

3. Inicie sesión con su cuenta de NetBird. Si no tiene una, regístrese primero.

    ![Iniciar sesión en NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/3-signin.png){class="glboxshadow"}

4. El KVM se vinculará automáticamente a su cuenta.

    ![KVM conectado](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/4-connected.png){class="glboxshadow"}

    También aparecerá en la página **Peers** del panel de NetBird.

    ![Panel de NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/5-dashboard.png){class="glboxshadow"}

## Vincular el dispositivo de control {#bind-the-controlling-device}

Este ejemplo muestra cómo vincular un portátil Windows, que actuará como dispositivo de control, a la red NetBird.

1. Instale NetBird en el portátil desde [aquí](https://app.netbird.io/install){target="_blank"}.

    ![Instalar NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/6-install.png){class="glboxshadow"}

2. Ejecute NetBird en el portátil y añádalo a la misma red NetBird.

    NetBird no muestra una ventana o interfaz independiente en el escritorio; solo aparece como un icono en la bandeja del sistema, en la esquina inferior derecha. Todas las operaciones se realizan desde su menú contextual.

    Haga clic con el botón derecho en el icono de NetBird y seleccione **Connect**.

    ![Conectar el equipo](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/7-pc-connect.png){class="glboxshadow gl-50-desktop"}

3. En la ventana emergente, haga clic en **Accept** para autorizarlo.

    ![Autorizar](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/8-authorize.png){class="glboxshadow"}

    El portátil se vinculará automáticamente a su cuenta y se añadirá a la misma red NetBird.

    ![Equipo conectado](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/9-login-success.png){class="glboxshadow"}

4. La página **Peers** del panel de NetBird mostrará dos dispositivos: el KVM y el portátil de control.

    ![Dispositivos del panel de NetBird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/10-dashboard.png){class="glboxshadow"}

## Acceso remoto mediante NetBird {#remote-access-via-netbird}

Este ejemplo muestra cómo acceder de forma remota a la consola KVM mediante la dirección IP virtual de NetBird.

1. En el portátil, inicie sesión en el panel de NetBird y vaya a **Peers**.

    Busque el KVM y haga clic en su **NetBird IP**, `100.100.141.229` en este ejemplo, para copiar la IP virtual.

    ![IP de NetBird del KVM](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/11-kvm-netbird-ip.png){class="glboxshadow"}

    Sitúe el cursor sobre la IP para ver otros datos, como la IP pública, el dominio y la región.

2. Abra una nueva pestaña del navegador, pegue la IP de NetBird en la barra de direcciones y pulse Intro. Se abrirá la página de inicio de sesión de GLKVM.

    ![Inicio de sesión para acceso remoto](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-login.png){class="glboxshadow"}

    Introduzca la contraseña de administrador. Ya puede acceder al KVM GL.iNet y al dispositivo controlado mediante la IP de NetBird.

    ![Acceso remoto establecido](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-access.png){class="glboxshadow"}

    **Consejo**: puede aparecer una advertencia de privacidad al acceder a esta IP de NetBird por primera vez. Haga clic en **Advanced** -> **Proceed** para continuar. Consulte [Advertencia de privacidad en el navegador](privacy_error_from_your_browser.md){target="_blank"}.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
