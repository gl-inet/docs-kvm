# Configuración rápida de Comet 5G (GL-RM10RC) {#comet-5g-gl-rm10rc-quick-setup}

Vea este vídeo o siga los pasos que se indican a continuación para configurar Comet 5G.

<iframe width="560" height="315" src="https://www.youtube.com/embed/whAUMBcIIZs" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Conectar los dispositivos {#connect-devices}

Para mayor claridad, el dispositivo A es el dispositivo de control y el dispositivo B es el dispositivo controlado.

![Conectar los dispositivos](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/connect_device.png){class="glboxshadow"}

1. Inserte una tarjeta SIM en Comet 5G y enciéndalo.

    ![Insertar la SIM y encender](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/01-insert-sim-power-on.jpg){class="glboxshadow"}

2. Conecte el puerto HDMI IN de Comet 5G al puerto HDMI del dispositivo B. Si es necesario, utilice otro cable HDMI para conectar el puerto HDMI OUT de Comet 5G a un monitor externo.

    ![Conectar el cable HDMI](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/02-hdmi-cable.jpg){class="glboxshadow"}

3. Conecte el puerto Type-C de Comet 5G a la interfaz Type-C del dispositivo B mediante un cable USB-C.

    ![Conectar el cable USB](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/03-usb-cable.jpg){class="glboxshadow"}

4. Conecte Comet 5G a una conexión de red.

    - 5G: Con la tarjeta SIM insertada, la conexión 5G se establecerá automáticamente al iniciar el sistema.

    - Wi-Fi: Deslice el dedo hacia la izquierda en la pantalla táctil y conecte Comet 5G a una red Wi-Fi existente (se admite 2.4G y 5G).

        ![Conectar mediante Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/04-network-wifi.png){class="glboxshadow"}

    - Ethernet: Conecte el puerto Ethernet de Comet 5G a una conexión de red.

        ![Conectar mediante Ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/04-network-ethernet.png){class="glboxshadow"}

    !!! Note "Nota"
        La prioridad de conexión es **Ethernet** > **Wi-Fi** > **5G**. Consulte la lógica completa de detección de redes WAN y conmutación por error [**aquí**](../../faq/wan_network_detection_and_failover_logic_of_comet5g.md).

5. La conexión de los dispositivos está completa. Ahora puede acceder a la consola de Comet 5G mediante el control de proximidad, el acceso local o el acceso remoto.

## Control de proximidad {#nearby-control}

El control de proximidad es ideal para configurar y gestionar Comet 5G rápidamente cuando se encuentre cerca.

En la pantalla táctil, cambie el modo de red Wi-Fi a **AP Mode** para generar un SSID Wi-Fi exclusivo. Los datos de la red aparecerán en la pantalla.

![Acceso de proximidad](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/nearby_access1.png){class="glboxshadow gl-80-desktop"}

Conecte un dispositivo a este SSID Wi-Fi. Después podrá acceder a la consola de Comet 5G desde un navegador web mediante la dirección IP predeterminada (192.168.8.1).

![Acceso de proximidad](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/nearby_access2.png){class="glboxshadow"}

## Acceso local {#local-access}

Hay dos formas de acceder a Comet 5G en la red local: mediante un nombre de dominio o una dirección IP.

Antes de acceder, asegúrese de que el dispositivo de control esté en la misma LAN que Comet 5G.

### Dominio {#domain}

1. Abra un navegador en el dispositivo de control. Se recomienda Chrome o Edge para una mayor compatibilidad.

2. Introduzca `glkvm.local` en la barra de direcciones. Se le dirigirá a la página de inicio de sesión de GLKVM. Introduzca la contraseña de administrador.

    ![Acceso local mediante dominio](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Nota**: Deberá establecer la contraseña de administrador la primera vez que acceda.

3. A continuación, podrá acceder localmente a la consola de Comet 5G y al dispositivo controlado.

    ![Acceso local mediante dominio](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### Dirección IP {#ip-address}

1. Busque la dirección IP de Comet 5G en la pantalla táctil. En este ejemplo, la dirección IP de Comet 5G es `192.168.8.197`.

2. Abra un navegador e introduzca esta IP en la barra de direcciones. Se le dirigirá a la página de inicio de sesión de GLKVM. Introduzca la contraseña de administrador.

    ![Acceso local mediante IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Nota**: Deberá establecer la contraseña de administrador la primera vez que acceda.

3. A continuación, podrá acceder localmente a la consola de Comet 5G y al dispositivo controlado.

    ![Acceso local mediante IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Acceso remoto {#remote-access}

Hay varias formas de acceder a Comet 5G de forma remota: mediante el servicio en la nube, la aplicación GLKVM, Tailscale, ZeroTier y NetBird.

### Servicio en la nube {#cloud-service}

1. Vincule su dispositivo a KVM Cloud. Esta operación debe realizarse en la red local.

    Hay dos formas de vincular su KVM a la nube: Regular Binding o Dynamic Code Binding. En este ejemplo se utiliza Regular Binding. Si prefiere Dynamic Code Binding, consulte los detalles [aquí](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}.

    Primero, acceda a Comet 5G de forma local y vaya a **Cloud Service** en la esquina superior derecha. Haga clic en **Bind To Cloud**.

    ![Vincular a la nube](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    Se le redirigirá a una página de inicio de sesión. Inicie sesión con su cuenta de glinet en la nube.

    ![Iniciar sesión para vincular el dispositivo](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Después, confirme la información de su dispositivo y haga clic en **Bind**.

    ![Confirmar la vinculación del dispositivo](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Espere un momento a que Comet 5G se vincule correctamente a su cuenta. Haga clic en **Done**.

    ![Dispositivo vinculado correctamente](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Acceda de forma remota mediante el servicio en la nube.

    Abra un navegador, como Google Chrome, e introduzca `glkvm.com` en la barra de direcciones. Aparecerá una página de inicio de sesión. Inicie sesión con su cuenta de glinet.

    ![Inicio de sesión para acceso remoto](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Después de iniciar sesión, verá los dispositivos vinculados a su cuenta. Haga clic en el dispositivo al que desee acceder de forma remota.

    ![Seleccionar el dispositivo para acceso remoto](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    En la nueva página web, introduzca su contraseña de administrador para iniciar sesión.

    ![Acceso remoto como administrador](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    A continuación, podrá acceder de forma remota a Comet 5G y al dispositivo controlado a través de la nube, sin instalar la aplicación.

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

        Esta operación debe realizarse en la red local. Asegúrese de que el dispositivo de control esté en la misma LAN que Comet 5G.

        Haga clic en **Auto Discover**. La búsqueda comenzará automáticamente.

        ![Detección automática 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

        Localice su KVM e introduzca su Device ID para vincularlo a su cuenta.

        ![Detección automática 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

    ??? "S/N Code"

        Esta opción se utiliza cuando no se detecta el KVM o no está en la misma LAN, pero dispone de su número de serie (S/N).

        Haga clic en **S/N Code**. En la ventana emergente, personalice el nombre del dispositivo e introduzca el S/N, que figura en la etiqueta de la parte inferior del KVM.

        ![Código S/N](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Esta operación debe realizarse en la red local. Asegúrese de que el dispositivo de control esté en la misma LAN que Comet 5G.

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

Comet 5G integra Tailscale, lo que permite acceder a él de forma remota a través de la red virtual de Tailscale.

En la consola, vaya a **Apps Center** -> **Tailscale**, actívelo y vincule Comet 5G a su cuenta de Tailscale.

Después, vincule el dispositivo de control a la misma cuenta. Podrá acceder a Comet 5G de forma remota introduciendo su **IP virtual de Tailscale** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM.

Consulte los detalles [aquí](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier {#zerotier}

Comet 5G integra ZeroTier, lo que permite acceder a él de forma remota a través de la red virtual de ZeroTier.

En la consola, vaya a **Apps Center** -> **ZeroTier** y actívelo.

Después, una Comet 5G y el dispositivo de control a la misma red de ZeroTier utilizando un Network ID alfanumérico de 16 caracteres. Podrá acceder a Comet 5G de forma remota introduciendo su **IP de ZeroTier** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM.

Consulte los detalles [aquí](../../faq/remote_access_via_zerotier.md){target="_blank"}.

### NetBird {#netbird}

Comet 5G integra NetBird, lo que permite acceder a él de forma remota a través de la red virtual de NetBird.

En la consola, vaya a **Apps Center** -> **NetBird**, actívelo y vincule Comet 5G a su cuenta de NetBird.

Después, vincule el dispositivo de control a la misma cuenta. Podrá acceder a Comet 5G de forma remota introduciendo su **IP virtual de NetBird** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM.

Consulte los detalles [aquí](../../faq/remote_access_via_netbird.md){target="_blank"}.
