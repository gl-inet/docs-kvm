# Cómo acceder al KVM de forma remota mediante Tailscale {#how-to-access-kvm-remotely-via-tailscale}

Los KVM GL.iNet integran Tailscale para vincularse a su red virtual y permitir el acceso remoto sin instalar la aplicación GLKVM ni utilizar el servicio de nube. Resulta especialmente útil si el dispositivo de control no utiliza Windows, macOS, Android o iOS y no puede instalar la aplicación GLKVM, o si prefiere no utilizar la aplicación ni el servicio de nube.

Siga estos pasos para acceder de forma remota al KVM GL.iNet mediante Tailscale.

## Vincular el KVM a Tailscale {#bind-kvm-to-tailscale}

**Antes de empezar, conecte el KVM y el dispositivo de control a la misma red local.**

1. Abra un navegador en el dispositivo de control. Se recomienda Chrome o Edge para una mayor compatibilidad.

2. Acceda de forma local a la consola KVM mediante su dominio o dirección IP. En este ejemplo se utiliza el dominio predeterminado.

    Introduzca `glkvm.local` en la barra de direcciones. Se abrirá la página de inicio de sesión de GLKVM. Introduzca la contraseña de administrador.

    ![Acceso local mediante el dominio](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

3. Vaya a **Apps Center** -> **Tailscale**. Active Tailscale y haga clic en **Bind Device**.

    ![Activar Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enable_tailscale.png){class="glboxshadow"}

4. Se abrirá la página de inicio de sesión de Tailscale. Introduzca su correo electrónico para iniciar sesión.

    ![Iniciar sesión en Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

5. La página indicará que va a conectar el dispositivo glkvm a su tailnet. Haga clic en **Connect**.

    ![Conectar el KVM a la tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_kvm_to_tailscale.png){class="glboxshadow"}

    El KVM quedará vinculado a su tailnet.

    ![KVM vinculado](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_kvm_successful.png){class="glboxshadow"}

6. Se abrirá la consola de Tailscale, donde aparecerá un dispositivo llamado **glkvm** en **Machines**.

    ![Consola de Tailscale con el KVM](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_1.png){class="glboxshadow"}

## Vincular el dispositivo de control {#bind-the-controlling-device}

Este ejemplo muestra cómo vincular un portátil Windows, que actuará como dispositivo de control, a la red Tailscale.

1. Instale Tailscale en el portátil desde [aquí](https://tailscale.com/download){target="_blank"}.

2. Ejecute Tailscale en el portátil e inicie sesión con el mismo correo electrónico.

    ![Iniciar sesión en Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

3. La página indicará que va a conectar el portátil, es decir, el dispositivo de control, a su tailnet. Haga clic en **Connect**.

    ![Conectar el equipo a la tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_pc_to_tailscale.png){class="glboxshadow"}

    El portátil quedará vinculado a su tailnet.

    ![Portátil vinculado](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_pc_successful.png){class="glboxshadow"}

4. Se abrirá la consola de Tailscale, donde el dispositivo de control también aparecerá en **Machines**.

    ![Consola de Tailscale con ambos dispositivos](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_2.png){class="glboxshadow"}

## Acceso remoto mediante Tailscale {#remote-access-via-tailscale}

En la consola de Tailscale, haga clic en **Address** del dispositivo glkvm; en este ejemplo es `100.104.185.26`.

![Obtener la IP virtual](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/get_vitual_ip.png){class="glboxshadow"}

Aparecerán cuatro valores:

- glkvm: nombre del dispositivo.
- glkvm.tail1fd0.ts.net: dominio asignado por Tailscale.
- fd7a:115c:a1e0:301:b92f: IPv6 virtual.
- 100.104.185.26: IPv4 virtual.

Tailscale los asigna para identificar el dispositivo y permitir la comunicación por la red virtual. Puede acceder al KVM de forma remota mediante el dominio asignado por Tailscale, la IPv4 virtual o la IPv6 virtual.

A continuación se utiliza la IPv4 virtual como ejemplo.

1. Copie la dirección IPv4 virtual del KVM.

2. Abra una nueva pestaña y pegue la IP en la barra de direcciones.

    ![Acceder a la IP virtual](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enter_vitual_ip.png){class="glboxshadow"}

    Puede aparecer una advertencia de privacidad. [¿Por qué aparece esta advertencia?](privacy_error_from_your_browser.md){target="_blank"}

    ![Advertencia de privacidad](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/privacy_error.png){class="glboxshadow"}

    Haga clic en **Advanced** y después en **Proceed to 100.104.185.26**. Se abrirá la página de inicio de sesión de GLKVM.

    ![Continuar al KVM](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/proceed.png){class="glboxshadow"}

3. Introduzca la contraseña de administrador. Ya puede acceder al KVM GL.iNet y al dispositivo controlado mediante la IP virtual de Tailscale.

    ![Acceso remoto establecido](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/remote_access_via_tailscale.png){class="glboxshadow"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
