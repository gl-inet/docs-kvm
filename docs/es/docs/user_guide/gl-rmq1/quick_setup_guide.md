# Configuración rápida de Comet Q (GL-RMQ1) {#comet-q-gl-rmq1-quick-setup}

Vea este vídeo o siga los pasos que se indican a continuación para configurar Comet Q.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6-f-XFkgYoU" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Conectar los dispositivos {#connect-devices}

Para mayor claridad, el dispositivo A es el dispositivo de control y el dispositivo B es el dispositivo controlado.

![Conexión 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect1.png){class="glboxshadow"}

1. Conecte el cable Type-C de Comet Q al puerto Type-C del dispositivo B.

    ![Conexión 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect2.png){class="glboxshadow"}

2. Si el dispositivo B es un dispositivo móvil con pantalla táctil, como un teléfono o una tableta, active primero los controles de accesibilidad. Esto permite que Comet Q maneje la pantalla táctil.

    - iOS: **Settings** > **Accessibility** > **Touch** > active **AssistiveTouch**.

    - Android: Busque **Mouse** o **Accessibility** en Settings. Las rutas de los menús varían según la marca y el modelo del dispositivo.

    ![Conexión 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect3.png){class="glboxshadow" width="600"}

3. Siga las instrucciones en pantalla para completar la configuración inicial. Consulte los detalles [aquí](../gl-rmq1/product_overview.md#touchscreen).

    ![Conexión 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect4.png){class="glboxshadow"}

## Acceso local {#local-access}

Hay dos formas de acceder a Comet Q en la red local: mediante un nombre de dominio o una dirección IP.

Antes de acceder, asegúrese de que el dispositivo de control esté en la misma LAN que Comet Q.

### Dominio {#domain}

1. Abra un navegador en el dispositivo de control. Se recomienda Chrome o Edge para una mayor compatibilidad.

2. Introduzca `glkvm.local` en la barra de direcciones. Se le dirigirá a la página de inicio de sesión de GLKVM. Introduzca la contraseña de administrador.

    ![Acceso local mediante dominio](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Nota**: Deberá establecer la contraseña de administrador la primera vez que acceda.

3. A continuación, podrá acceder localmente a la consola de Comet Q y al dispositivo controlado.

    ![Acceso local mediante dominio](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### Dirección IP {#ip-address}

1. Conecte Comet Q a una red Wi-Fi y busque su dirección IP en la pantalla táctil. En este ejemplo, la dirección IP de Comet Q es `192.168.8.197`.

2. Abra un navegador e introduzca esta IP en la barra de direcciones. Se le dirigirá a la página de inicio de sesión de GLKVM. Introduzca la contraseña de administrador.

    ![Acceso local mediante IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Nota**: Deberá establecer la contraseña de administrador la primera vez que acceda.

3. A continuación, podrá acceder localmente a la consola de Comet Q y al dispositivo controlado.

    ![Acceso local mediante IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Acceso remoto {#remote-access}

Hay varias formas de acceder a Comet Q de forma remota: mediante el servicio en la nube, la aplicación GLKVM, Tailscale y ZeroTier.

### Servicio en la nube {#cloud-service}

1. Vincule su dispositivo a KVM Cloud. Esta operación debe realizarse en la red local.

    Hay dos formas de vincular su KVM a la nube: Regular Binding o Dynamic Code Binding. En este ejemplo se utiliza Regular Binding. Si prefiere Dynamic Code Binding, consulte los detalles [aquí](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}.

    Primero, acceda a Comet Q de forma local y vaya a **Cloud Service** en la esquina superior derecha. Haga clic en **Bind To Cloud**.

    ![Vincular a la nube](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    Se le redirigirá a una página de inicio de sesión. Inicie sesión con su cuenta de glinet en la nube.

    ![Iniciar sesión para vincular el dispositivo](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Después, confirme la información de su dispositivo y haga clic en **Bind**.

    ![Confirmar la vinculación del dispositivo](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Espere un momento a que Comet Q se vincule correctamente a su cuenta. Haga clic en **Done**.

    ![Dispositivo vinculado correctamente](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Acceda de forma remota mediante el servicio en la nube.

    Abra un navegador, como Google Chrome, e introduzca `glkvm.com` en la barra de direcciones. Aparecerá una página de inicio de sesión. Inicie sesión con su cuenta de glinet.

    ![Inicio de sesión para acceso remoto](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Después de iniciar sesión, verá los dispositivos vinculados a su cuenta. Haga clic en el dispositivo al que desee acceder de forma remota.

    ![Seleccionar el dispositivo para acceso remoto](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    En la nueva página web, introduzca su contraseña de administrador para iniciar sesión.

    ![Acceso remoto como administrador](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    A continuación, podrá acceder de forma remota a Comet Q y al dispositivo controlado a través de la nube, sin instalar la aplicación.

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

        Esta operación debe realizarse en la red local. Asegúrese de que el dispositivo de control esté en la misma LAN que Comet Q.

        Haga clic en **Auto Discover**. La búsqueda comenzará automáticamente.

        ![Detección automática 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

        Localice su KVM e introduzca su Device ID para vincularlo a su cuenta.

        ![Detección automática 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

    ??? "S/N Code"

        Esta opción se utiliza cuando no se detecta el KVM o no está en la misma LAN, pero dispone de su número de serie (S/N).

        Haga clic en **S/N Code**. En la ventana emergente, personalice el nombre del dispositivo e introduzca el S/N, que figura en la etiqueta de la parte inferior del KVM.

        ![Código S/N](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Esta operación debe realizarse en la red local. Asegúrese de que el dispositivo de control esté en la misma LAN que Comet Q.

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

Comet Q integra Tailscale, lo que permite acceder a él de forma remota a través de la red virtual de Tailscale.

En la consola, vaya a **Apps Center** -> **Tailscale**, actívelo y vincule Comet Q a su cuenta de Tailscale.

Después, vincule el dispositivo de control a la misma cuenta. Podrá acceder a Comet Q de forma remota introduciendo su **IP virtual de Tailscale** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM.

Consulte los detalles [aquí](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier {#zerotier}

Comet Q integra ZeroTier, lo que permite acceder a él de forma remota a través de la red virtual de ZeroTier.

En la consola, vaya a **Apps Center** -> **ZeroTier** y actívelo.

Después, una Comet Q y el dispositivo de control a la misma red de ZeroTier utilizando un Network ID alfanumérico de 16 caracteres. Podrá acceder a Comet Q de forma remota introduciendo su **IP de ZeroTier** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM.

Consulte los detalles [aquí](../../faq/remote_access_via_zerotier.md){target="_blank"}.
