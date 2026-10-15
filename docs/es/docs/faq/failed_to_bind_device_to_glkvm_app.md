# Qué hacer si no puede vincular el dispositivo a la aplicación GLKVM {#what-should-i-do-if-i-failed-to-bind-device-to-the-glkvm-app}

La [aplicación GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} permite acceder de forma remota al dispositivo controlado desde el dispositivo de control. Instálela en el dispositivo de control y vincule su KVM GL.iNet para acceder al dispositivo controlado en cualquier momento y lugar.

La vinculación puede fallar por diversos motivos.

Haga clic en el mensaje de error correspondiente para consultar las soluciones.

??? "Binding failed, unable to obtain basic KVM device information."

    ![Error de vinculación: información del dispositivo](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_device_info_error.png){class="glboxshadow"}

    1. Compruebe el estado del LED. Debe estar blanco fijo y el KVM debe estar conectado a Internet.
    2. Reinicie el KVM, espere 2 minutos y vuelva a intentar vincularlo.
    3. Si añade el dispositivo mediante su código S/N, compruebe que sea correcto.
    4. Siga estos pasos para comprobar la red mediante el comando **ping**.

        1. Conecte el dispositivo de control a la misma red que el KVM.

        2. Abra un navegador en el dispositivo de control, preferiblemente Chrome o Edge, e introduzca `glkvm.local` en la barra de direcciones. Introduzca la contraseña de administrador para iniciar sesión.

            ![Acceso local mediante el dominio](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. Vaya a **Toolbox** -> **Terminal** y haga clic en **Access** para acceder al terminal.

            ![Acceder al terminal](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Ejecute ping a `google.com` para comprobar el estado de la red.

            ![Comando ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Si la red funciona correctamente, obtendrá un resultado como el siguiente.

            ![Resultado de ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Si la red es inestable o no está disponible, contacte con su proveedor de Internet o con el soporte del router.

??? "Device network error, binding failed."

    ![Error de vinculación: red](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_network_error.png){class="glboxshadow"}

    1. Compruebe el estado del LED. Debe estar blanco fijo y el KVM debe estar conectado a Internet.
    2. Reinicie el KVM, espere 2 minutos y vuelva a intentar vincularlo.
    3. Asegúrese de que el servicio de nube esté activado.

        Este servicio está activado de forma predeterminada. Si lo desactivó manualmente, no podrá volver a vincular el dispositivo a la aplicación GLKVM. Acceda al KVM de forma local mediante su dominio o dirección IP para volver a activar el servicio.

    4. Siga estos pasos para comprobar la red mediante el comando **ping**.

        1. Conecte el dispositivo de control a la misma red que el KVM.

        2. Abra un navegador en el dispositivo de control, preferiblemente Chrome o Edge, e introduzca `glkvm.local` en la barra de direcciones. Introduzca la contraseña de administrador para iniciar sesión.

            ![Acceso local mediante el dominio](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. Vaya a **Toolbox** -> **Terminal** y haga clic en **Access** para acceder al terminal.

            ![Acceder al terminal](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Ejecute ping a `google.com` para comprobar el estado de la red.

            ![Comando ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Si la red funciona correctamente, obtendrá un resultado como el siguiente.

            ![Resultado de ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Si la red es inestable o no está disponible, contacte con su proveedor de Internet o con el soporte del router.

??? "Binding failed, KVM is already bound by others."

    ![Error de vinculación: ya vinculado a otra cuenta](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_bound_by_others.png){class="glboxshadow"}

    Este mensaje significa que el KVM ya está vinculado a otra cuenta.

    1. Compruebe si lo vinculó con otra dirección de correo electrónico. Pruebe sus otras cuentas, si las tiene.

    2. Si añade el dispositivo mediante su código S/N, compruebe que sea correcto.

??? "Incorrect Dynamic Binding Code. You have 4 attempts remaining."

    ![Código de vinculación incorrecto](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_binding_code.png){class="glboxshadow"}

    Este mensaje significa que el código de vinculación introducido no es válido o ha caducado.

    1. Acceda de forma local a la consola de administración del KVM, vaya a **Cloud Service**, en la esquina superior derecha, y haga clic en **Bind with Code** para obtener un código de vinculación dinámico.

    2. En el modelo GL-RM10 (Comet Pro), también puede obtener el código en la pantalla táctil. Deslice hasta **Cloud Service** y pulse **Generate Binding Code**. Introduzca en la aplicación GLKVM el código dinámico que aparece en la pantalla táctil para completar la vinculación.

        ![Generar un código de vinculación](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_code_screen.png){class="glboxshadow"}

    3. Si el código caduca, haga clic en **Regenerate** para obtener uno nuevo.

??? "Incorrect Device ID. You have 4 attempts remaining."

    ![Device ID incorrecto](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_device_id.png){class="glboxshadow"}

    Este mensaje significa que ha introducido un Device ID incorrecto.

    1. Consulte la etiqueta inferior para conocer el Device ID correcto.

    2. Si no puede consultar la etiqueta, pruebe a vincular el dispositivo mediante el acceso local.

        Acceda de forma local a la consola de administración del KVM, vaya a **Cloud Service**, en la esquina superior derecha, y haga clic en **Bind To KVM Cloud**. Se abrirá la página de vinculación con un token único. Inicie sesión con su cuenta de la nube y confirme la información del dispositivo para completar la vinculación.

??? "Otros casos"

    Compruebe si hay una VPN activada en el dispositivo de control donde está instalada la aplicación GLKVM.

    Desactive cualquier software VPN o proxy, incluidos AstroWarp, Tailscale y ZeroTier, y vuelva a intentar vincular el KVM a la aplicación GLKVM.

Si el problema persiste, escriba a [support@gl-inet.com](mailto:support@gl-inet.com) e indique el modelo del dispositivo, la versión de firmware y la dirección MAC.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
