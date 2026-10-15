# Configuración rápida de Comet (GL-RM1) V1/V2 {#comet-gl-rm1-v1v2-quick-setup}

Vea este vídeo o siga los pasos que se indican a continuación para configurar Comet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/JDgflRaIHw0" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Conectar los dispositivos {#connect-devices}

Para mayor claridad, el dispositivo A es el dispositivo de control y el dispositivo B es el dispositivo controlado.

![Conectar los dispositivos](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/01_device_distinction.jpg){class="glboxshadow"}

1. Conecte Comet a la fuente de alimentación.

    ![Encender](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/02_power-on.jpg){class="glboxshadow"}

2. Conecte el puerto HD IN de Comet al puerto HD OUT del dispositivo B mediante un cable HDMI.

    ![Conectar el cable HD](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/03_hdmi.jpg){class="glboxshadow"}

3. Conecte el puerto USB-Device de Comet al puerto USB del dispositivo B mediante un cable USB.

    ![Conectar el puerto USB](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/04_usb-cable.jpg){class="glboxshadow"}

4. Conecte el puerto Ethernet de Comet a una conexión de red.

    ![Conectar a la red](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/05_ethernet.jpg){class="glboxshadow"}

5. La conexión de los dispositivos está completa. Ahora puede acceder a la consola de Comet de forma local o remota.

## Acceso local {#local-access}

Hay dos formas de acceder a Comet en la red local: mediante un nombre de dominio o una dirección IP.

Antes de acceder, asegúrese de que el dispositivo de control esté en la misma LAN que Comet.

### Dominio {#domain}

1. Abra un navegador en el dispositivo de control. Se recomienda Chrome o Edge para una mayor compatibilidad.

2. Introduzca `glkvm.local` en la barra de direcciones. Se le dirigirá a la página de inicio de sesión de GLKVM. Introduzca la contraseña de administrador.

    ![Acceso local mediante dominio](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Nota**: Deberá establecer la contraseña de administrador la primera vez que acceda.

3. A continuación, podrá acceder localmente a la consola de Comet y al dispositivo controlado.

    ![Acceso local mediante dominio](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### Dirección IP {#ip-address}

1. Busque la dirección IP de Comet en el router al que está conectado.

    Por ejemplo, Comet está conectado al puerto LAN de un router GL.iNet GL-AXT1800 mediante un cable Ethernet.

    Inicie sesión en el panel de administración web del GL-AXT1800 y busque la dirección IP de Comet en la lista Client, como se muestra a continuación.

    ![Acceso local mediante IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

2. Abra una pestaña nueva en el navegador e introduzca la IP de Comet en la barra de direcciones. Se le dirigirá a la página de inicio de sesión de GLKVM. Introduzca la contraseña de administrador.

    ![Acceso local mediante IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Nota**: Deberá establecer la contraseña de administrador la primera vez que acceda.

3. A continuación, podrá acceder localmente a la consola de Comet y al dispositivo controlado.

    ![Acceso local mediante IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Acceso remoto {#remote-access}

Hay varias formas de acceder a Comet de forma remota: mediante el servicio en la nube, la aplicación GLKVM, Tailscale, ZeroTier y NetBird.

### Servicio en la nube {#cloud-service}

1. Vincule su dispositivo a KVM Cloud. Esta operación debe realizarse en la red local.

    Hay dos formas de vincular su KVM a la nube: Regular Binding o Dynamic Code Binding. En este ejemplo se utiliza Regular Binding. Si prefiere Dynamic Code Binding, consulte los detalles [aquí](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}.

    Primero, acceda a Comet de forma local y vaya a **Cloud Service** en la esquina superior derecha. Haga clic en **Bind To Cloud**.

    ![Vincular a la nube](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    Se le redirigirá a una página de inicio de sesión. Inicie sesión con su cuenta de glinet en la nube.

    ![Iniciar sesión para vincular el dispositivo](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Después, confirme la información de su dispositivo y haga clic en **Bind**.

    ![Confirmar la vinculación del dispositivo](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Espere un momento a que el dispositivo se vincule correctamente a su cuenta. Haga clic en **Done**.

    ![Dispositivo vinculado correctamente](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Acceda de forma remota mediante el servicio en la nube.

    Abra un navegador, como Google Chrome, e introduzca `glkvm.com` en la barra de direcciones. Aparecerá una página de inicio de sesión. Inicie sesión con su cuenta de glinet.

    ![Inicio de sesión para acceso remoto](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Después de iniciar sesión, verá los dispositivos vinculados a su cuenta. Haga clic en el dispositivo al que desee acceder de forma remota.

    ![Seleccionar el dispositivo para acceso remoto](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    En la nueva página web, introduzca su contraseña de administrador para iniciar sesión.

    ![Acceso remoto como administrador](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    A continuación, podrá acceder de forma remota al KVM y al dispositivo controlado a través de la nube, sin instalar la aplicación.

    ![Acceso remoto correcto](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

### Aplicación GLKVM {#glkvm-app}

1. Instale la [aplicación GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} en el dispositivo de control.

2. Inicie sesión con su cuenta de GL.iNet.

    ![Iniciar sesión](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Si no tiene una cuenta, regístrese primero e inicie sesión.

    ![Registrarse](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

3. Vincule su dispositivo.

    Después de iniciar sesión, aparecerá la siguiente página. Haga clic en **Add Device**.

    ![Añadir dispositivo](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

    Puede vincular el dispositivo de tres formas: Auto Discover, S/N Code y Dynamic Binding Code.

    ??? "Auto Discover"

        Esta operación debe realizarse en la red local. Asegúrese de que el dispositivo de control esté en la misma LAN que Comet.

        Haga clic en **Auto Discover**. La búsqueda comenzará automáticamente.

        ![Detección automática 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

        Localice su KVM e introduzca su Device ID para vincularlo a su cuenta.

        ![Detección automática 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

    ??? "S/N Code"

        Esta opción se utiliza cuando no se detecta el KVM o no está en la misma LAN, pero dispone de su número de serie (S/N).

        Haga clic en **S/N Code**. En la ventana emergente, personalice el nombre del dispositivo e introduzca el S/N, que figura en la etiqueta de la parte inferior del KVM.

        ![Código S/N](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Esta operación debe realizarse en la red local. Asegúrese de que el dispositivo de control esté en la misma LAN que Comet.

        1. Inicie sesión en su KVM de forma local mediante el dominio o la dirección IP. Consulte los detalles [aquí](../../faq/local_access_via_browser.md).

        2. Vaya a **Cloud Service** en la esquina superior derecha y haga clic en **Bind With Code**.

            ![Vincular con código 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

        3. Se generará aleatoriamente un código dinámico de 8 dígitos para vincular el dispositivo, válido durante 60 segundos. Haga clic en el código para copiarlo.

            ![Vincular con código 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

        4. Vuelva a la aplicación GLKVM, introduzca el código dinámico de vinculación y haga clic en **Bind**.

            ![Código dinámico](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

4. Acceda de forma remota mediante la aplicación GLKVM.

    Una vez que el dispositivo KVM esté vinculado a su cuenta, aparecerá como "Online" en la aplicación.

    ![Dispositivo conectado](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

    Haga clic en su dispositivo KVM. Se abrirá una ventana nueva y comenzará la conexión.

    ![Conectando](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

    Una vez conectado, introduzca la contraseña de administrador para iniciar sesión en el dispositivo.

    ![Iniciar sesión en el dispositivo conectado](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

    A continuación, accederá al dispositivo KVM, a través del cual podrá acceder al dispositivo controlado.

    ![Acceso al dispositivo conectado](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

### Tailscale {#tailscale}

Comet integra Tailscale, lo que permite acceder a él de forma remota a través de la red virtual de Tailscale.

En la consola de Comet, vaya a **Apps Center** -> **Tailscale**, actívelo y vincule Comet a su cuenta de Tailscale.

Después, vincule el dispositivo de control a la misma cuenta. Podrá acceder a Comet de forma remota introduciendo su **IP virtual de Tailscale** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM.

Consulte los detalles [aquí](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier {#zerotier}

Comet integra ZeroTier, lo que permite acceder a él de forma remota a través de la red virtual de ZeroTier.

En la consola de Comet, vaya a **Apps Center** -> **ZeroTier** y actívelo.

Después, una Comet y el dispositivo de control a la misma red de ZeroTier utilizando un Network ID alfanumérico de 16 caracteres. Podrá acceder a Comet de forma remota introduciendo su **IP de ZeroTier** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM.

Consulte los detalles [aquí](../../faq/remote_access_via_zerotier.md){target="_blank"}.

### NetBird {#netbird}

Comet integra NetBird, lo que permite acceder a él de forma remota a través de la red virtual de NetBird.

En la consola de Comet, vaya a **Apps Center** -> **NetBird**, actívelo y vincule Comet a su cuenta de NetBird.

Después, vincule el dispositivo de control a la misma cuenta. Podrá acceder a Comet de forma remota introduciendo su **IP virtual de NetBird** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM.

Consulte los detalles [aquí](../../faq/remote_access_via_netbird.md){target="_blank"}.
