# Cómo acceder al KVM de forma remota mediante la aplicación GLKVM {#how-to-access-kvm-remotely-via-glkvm-app}

Antes de empezar, asegúrese de que el dispositivo controlado esté conectado correctamente al KVM GL.iNet y de que el KVM tenga una conexión de red estable.

Siga estos pasos para acceder de forma remota al KVM y al dispositivo controlado mediante la aplicación GLKVM.

## Instalar e iniciar sesión {#install-and-log-in}

1. Instale la [aplicación GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} en el dispositivo de control.

2. Abra la aplicación e inicie sesión con su cuenta GL.iNet.

    ![Iniciar sesión](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Si no tiene una cuenta GL.iNet, regístrese y después inicie sesión.

    ![Registrarse](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

## Vincular el KVM {#bind-your-kvm}

Después de iniciar sesión, verá la siguiente página. Haga clic en **Add Device**.

Puede vincular el KVM de tres maneras: Auto Discover, S/N Code y Dynamic Binding Code.

![Añadir un dispositivo](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

### Detección automática {#auto-discover}

Este procedimiento debe realizarse desde la red local. Asegúrese de que el KVM y el dispositivo de control estén en la misma LAN.

1. Haga clic en **Auto Discover** para buscar automáticamente los dispositivos KVM disponibles.

    ![Detección automática](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

2. Busque su KVM e introduzca su **Device ID** para vincularlo a su cuenta.

    ![Vinculación del dispositivo detectado](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

### Código S/N {#sn-code}

Utilice este método si no se detecta el KVM o no está en la misma LAN, pero dispone de su número de serie (S/N).

1. Haga clic en **S/N Code**.

2. En la ventana emergente, asigne un nombre al dispositivo e introduzca su S/N, impreso en la etiqueta inferior del KVM.

    ![Código S/N](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

### Código de vinculación dinámico {#dynamic-binding-code}

Actualice el firmware del KVM a v1.7 antes de utilizar esta función.

Este procedimiento debe realizarse desde la red local. Asegúrese de que el KVM y el dispositivo de control estén en la misma LAN.

1. Acceda al KVM de forma local mediante su dominio o dirección IP. Consulte los detalles [aquí](../faq/local_access_via_browser.md).

2. Vaya a **Cloud Service**, en la esquina superior derecha, y haga clic en **Bind With Code**.

    ![Vincular con código](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Se generará un código dinámico aleatorio de 8 dígitos para la vinculación, válido durante 60 segundos. Haga clic en él para copiarlo.

    ![Código dinámico generado](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Vuelva a la aplicación GLKVM, introduzca el código dinámico y haga clic en **Bind**.

    ![Introducir el código dinámico](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

## Acceso remoto {#remote-access}

Una vez vinculado a su cuenta, el KVM aparecerá como "Online" en la aplicación.

![Dispositivo en línea](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

Haga clic en el KVM. Se abrirá una nueva ventana y comenzará la conexión.

![Conectando](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

Cuando se conecte, introduzca la contraseña de administrador para iniciar sesión.

![Iniciar sesión tras la conexión](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

Ya puede acceder al KVM y, desde él, al dispositivo controlado.

![Acceso establecido](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
