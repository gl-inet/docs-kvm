# Configuración rápida de Comet X (GL-RM4PE) {#comet-x-gl-rm4pe-quick-setup}

## Conectar los dispositivos {#connect-devices}

Para mayor claridad, el dispositivo A es el dispositivo de control y el dispositivo B es el dispositivo controlado.

![Conexión 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect1.png){class="glboxshadow"}

1. Conecte Comet X a un switch PoE mediante un cable Ethernet o aliméntelo con un adaptador de alimentación de 5V/3A.

    ![Conexión 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect2.png){class="glboxshadow"}

    ***Nota**: Si utiliza un adaptador de alimentación, conecte Comet X a un dispositivo de red, como un router, mediante un cable Ethernet para acceder a Internet.*

2. Conecte el puerto **HDMI IN** de Comet X al dispositivo B mediante un cable HDMI. Esto permite transmitir la señal de vídeo.

    ![Conexión 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect3.png){class="glboxshadow"}

3. Conecte el puerto **USB-C** de Comet X al dispositivo B mediante un cable USB. Este puerto USB-C debe emparejarse con el puerto HDMI IN correspondiente para transmitir correctamente las señales de teclado y ratón.

    ![Conexión 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect4.png){class="glboxshadow"}

4. (Opcional) Conecte el puerto **HDMI OUT** de Comet X a un monitor externo para duplicar la pantalla mediante la salida de vídeo en bucle. Consulte los detalles en [Control local](#local-control).

5. La conexión está completa. Ahora puede acceder a la consola de Comet X de forma local o remota.

## Montaje en rack {#rack-mounting}

Monte Comet X en los rieles del rack de servidores según sea necesario.

1. Utilice los tornillos incluidos para fijar los soportes de montaje a Comet X.

    ![Instalación 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install1.png){class="glboxshadow"}

2. Fije Comet X a los rieles del rack con tornillos para rack. **Los tornillos para rack no están incluidos**.

    ![Instalación 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install2.png){class="glboxshadow"}

## Control local {#local-control}

Controle el dispositivo directamente mediante cables físicos, sin necesidad de red, dirección IP ni nombre de dominio.

Comet X dispone de un puerto HDMI OUT y dos puertos USB adicionales, ideales para solucionar problemas, configurar e instalar sistemas operativos de forma local. Solo tiene que conectar el monitor, el ratón y el teclado para controlar el equipo localmente de inmediato.

1. Conecte el puerto **HDMI OUT** del panel trasero de Comet X a un monitor externo para duplicar la pantalla mediante la salida de vídeo en bucle.

    ![Control local 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control1.png){class="glboxshadow"}

2. Conecte un teclado y un ratón a los puertos USB del panel frontal de Comet X.

    ![Control local 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control2.png){class="glboxshadow"}

3. Ahora puede controlar los dispositivos conectados con el teclado y el ratón locales mientras las señales de vídeo se retransmiten al monitor local.

## Acceso por LAN {#lan-access}

Hay dos formas de acceder a Comet X en la red local: mediante un nombre de dominio o una dirección IP.

Antes de acceder, asegúrese de que el dispositivo de control esté en la misma LAN que Comet X.

### Dominio {#domain}

1. Abra un navegador en el dispositivo de control. Se recomienda Chrome o Edge para una mayor compatibilidad.

2. Introduzca `glkvm.local` en la barra de direcciones. Se le dirigirá a la página de inicio de sesión de GLKVM. Introduzca la contraseña de administrador.

    ![Acceso local mediante dominio](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain1.png){class="glboxshadow"}

    ***Nota**: Deberá establecer la contraseña de administrador la primera vez que acceda.*

3. A continuación, podrá acceder localmente a la consola de Comet X y al dispositivo controlado.

    ![Acceso local mediante dominio](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain2.png){class="glboxshadow"}

### Dirección IP {#ip-address}

1. Busque la dirección IP de Comet X en la pantalla táctil. En este ejemplo, la dirección IP de Comet X es `192.168.8.197`.

2. Abra un navegador e introduzca esta IP en la barra de direcciones. Se le dirigirá a la página de inicio de sesión de GLKVM. Introduzca la contraseña de administrador.

    ![Acceso local mediante IP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip1.png){class="glboxshadow"}

    ***Nota**: Deberá establecer la contraseña de administrador la primera vez que acceda.*

3. A continuación, podrá acceder localmente a la consola de Comet X y al dispositivo controlado.

    ![Acceso local mediante IP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip2.png){class="glboxshadow"}

## Acceso remoto {#remote-access}

Hay varias formas de acceder a Comet X de forma remota: mediante el servicio en la nube, la aplicación GLKVM, Tailscale y ZeroTier.

### Servicio en la nube {#cloud-service}

1. Vincule su dispositivo a KVM Cloud. Esta operación debe realizarse en la red local.

    Hay dos formas de vincular su KVM a la nube: Regular Binding o Dynamic Code Binding. En este ejemplo se utiliza Regular Binding. Si prefiere Dynamic Code Binding, consulte los detalles [aquí](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}.

    Primero, acceda a Comet X de forma local y vaya a **Cloud Service** en la esquina superior derecha. Haga clic en **Bind To KVMCloud**.

    ![Vincular a la nube](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_to_cloud.png){class="glboxshadow"}

    Se le redirigirá a una página de inicio de sesión. Inicie sesión con su cuenta de glinet en la nube.

    ![Vincular el dispositivo a la nube 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind1.png){class="glboxshadow"}

    Después, confirme la información de su dispositivo y haga clic en **Bind**.

    ![Vincular el dispositivo a la nube 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind2.png){class="glboxshadow"}

    Espere un momento a que Comet X se vincule a su cuenta. Haga clic en **Done**.

    ![Dispositivo vinculado a la nube correctamente](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind_success.png){class="glboxshadow"}

2. Acceda de forma remota mediante el servicio en la nube.

    Después de hacer clic en Done, se le redirigirá a un sitio con el dominio `glkvm.com`, donde podrá ver su dispositivo.

    ![Lista de dispositivos en la nube](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_devices.png){class="glboxshadow"}

    ***Consejo**: Si no se le redirige, introduzca `glkvm.com` manualmente en la barra de direcciones e inicie sesión en su cuenta de glinet. Después de iniciar sesión, verá el dispositivo vinculado a su cuenta.*

    Haga clic en el dispositivo al que desee acceder de forma remota.

    ![Acceso desde la nube](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access.png){class="glboxshadow"}

    Se abrirá una página web nueva. Introduzca su contraseña de administrador para iniciar sesión.

    ![Acceso desde la nube 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access1.png){class="glboxshadow"}

    A continuación, podrá acceder de forma remota a Comet X y al dispositivo controlado a través de la nube.

    ![Acceso desde la nube 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access2.png){class="glboxshadow"}

### Aplicación GLKVM {#glkvm-app}

1. Instale la [aplicación GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} en el dispositivo de control.

2. Inicie sesión con su cuenta de GL.iNet.

    ![Iniciar sesión](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_login.jpg){class="glboxshadow"}

    Si no tiene una cuenta, regístrese primero e inicie sesión.

    ![Registrarse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_signup.png){class="glboxshadow"}

3. Vincule su dispositivo.

    Después de iniciar sesión, aparecerá la siguiente página. Haga clic en **Add Device**.

    ![Añadir dispositivo](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_add_device.png){class="glboxshadow"}

    Puede vincular el dispositivo de tres formas: Auto Discover, S/N Code y Dynamic Binding Code.

    ??? "Auto Discover"

        Esta operación debe realizarse en la red local. Asegúrese de que el dispositivo de control esté en la misma LAN que Comet X y tenga a mano el ID de su dispositivo KVM.

        Haga clic en **Auto Discover**. Comenzará la búsqueda.

        ![Detección automática 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover1.png){class="glboxshadow"}

        Busque su KVM e introduzca su **Device ID** para vincularlo a su cuenta.

        ![Detección automática 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover2.png){class="glboxshadow"}

        ![Detección automática 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover3.png){class="glboxshadow"}

    ??? "S/N Code"

        Esta opción se utiliza cuando no se detecta el KVM o no está en la misma LAN, pero dispone de su número de serie (S/N).

        Haga clic en **S/N Code**. En la ventana emergente, establezca un nombre para el dispositivo e introduzca el S/N, que figura en la parte inferior del dispositivo KVM.

        ![Código S/N](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/add_sncode.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Esta operación debe realizarse en la red local. Asegúrese de que el dispositivo de control esté en la misma LAN que Comet X.

        1. Inicie sesión en su KVM de forma local mediante el dominio o la dirección IP. Consulte los detalles [aquí](#lan-access).

        2. Vaya a **Cloud Service** en la esquina superior derecha y haga clic en **Bind With Code**.

            ![Vincular con código 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code1.png){class="glboxshadow"}

        3. Se generará aleatoriamente un código dinámico de 8 dígitos para vincular el dispositivo, válido durante 60 segundos. Haga clic en el código para copiarlo.

            ![Vincular con código 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code2.png){class="glboxshadow"}

        4. Vuelva a la aplicación GLKVM, introduzca el código dinámico de vinculación y haga clic en **Bind**.

            ![Código dinámico](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code3.png){class="glboxshadow"}

4. Acceda de forma remota mediante la aplicación GLKVM.

    Una vez que el dispositivo KVM esté vinculado a su cuenta, aparecerá como "Online" en la aplicación.

    ![Dispositivo conectado en la aplicación](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_devices.png){class="glboxshadow"}

    Haga clic en su dispositivo KVM. Se abrirá una ventana nueva y comenzará la conexión.

    ![Conexión desde la aplicación](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_connecting.png){class="glboxshadow"}

    Una vez conectado, introduzca su contraseña de administrador para iniciar sesión en el dispositivo.

    ![Acceso desde la aplicación 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access1.png){class="glboxshadow"}

    A continuación, accederá al dispositivo KVM, a través del cual podrá acceder al dispositivo controlado.

    ![Acceso desde la aplicación 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access2.png){class="glboxshadow"}

### Tailscale {#tailscale}

Comet X integra Tailscale, lo que permite acceder a él de forma remota a través de la red virtual de Tailscale.

En la consola, vaya a **Apps Center** -> **Tailscale**, actívelo y vincule Comet X a su cuenta de Tailscale.

Después, vincule el dispositivo de control a la misma cuenta. Podrá acceder a Comet X de forma remota introduciendo su **IP virtual de Tailscale** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM.

Consulte los detalles [aquí](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier {#zerotier}

Comet X integra ZeroTier, lo que permite acceder a él de forma remota a través de la red virtual de ZeroTier.

En la consola, vaya a **Apps Center** -> **ZeroTier** y actívelo.

Después, una Comet X y el dispositivo de control a la misma red de ZeroTier utilizando un Network ID alfanumérico de 16 caracteres. Podrá acceder a Comet X de forma remota introduciendo su **IP de ZeroTier** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM.

Consulte los detalles [aquí](../../faq/remote_access_via_zerotier.md){target="_blank"}.
