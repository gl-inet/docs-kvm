# Cómo acceder al KVM de forma remota mediante la nube {#how-to-access-kvm-remotely-via-cloud}

Antes de empezar, asegúrese de que:

- El dispositivo controlado esté conectado correctamente al KVM.

- El KVM esté conectado a una red estable.

- Pueda acceder al KVM de forma local, ya que la vinculación con la nube debe realizarse desde la red local.

Siga estos pasos para acceder de forma remota al KVM y al dispositivo controlado mediante el servicio de nube.

## Vincular el KVM a la nube {#bind-your-kvm-to-the-cloud}

Puede vincular el KVM mediante vinculación normal o mediante un código dinámico.

- **Vinculación normal**: haga clic en "Bind To KVMCloud" en la consola KVM. Se abrirá la página de vinculación con el token. Inicie sesión con su cuenta de la nube y confirme los datos del dispositivo para completar la vinculación.

- **Vinculación con código dinámico**: haga clic en "Bind With Code" en la consola KVM para generar un código dinámico aleatorio de 8 dígitos. Inicie sesión con su cuenta de la nube e introduzca el código para completar la vinculación.

### Vinculación normal {#regular-binding}

Acceda al KVM de forma local mediante su dirección IP o dominio y vaya a **Cloud Service**, en la esquina superior derecha. Haga clic en **Bind To Cloud**.

![Vincular a la nube](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

Se abrirá una página de inicio de sesión. Introduzca su cuenta GL.iNet y haga clic en **Log In**.

![Iniciar sesión para vincular](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

Confirme los datos del dispositivo y haga clic en **Bind**.

![Confirmar el dispositivo](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

Espere un momento hasta que el dispositivo se vincule a su cuenta. Haga clic en **Done**.

![Dispositivo vinculado](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

### Vinculación con código dinámico {#dynamic-code-binding}

Nota: actualice el firmware del KVM a la versión 1.7 antes de utilizar esta función.

1. Acceda al KVM GL.iNet de forma local mediante su dominio o dirección IP. Consulte los detalles [aquí](../faq/local_access_via_browser.md).

2. Vaya a **Cloud Service**, en la esquina superior derecha, y haga clic en **Bind With Code**.

    ![Vincular con código](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Se generará un código dinámico aleatorio de 8 dígitos, válido durante 60 segundos. Haga clic en él para copiarlo.

    ![Código dinámico generado](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Abra [https://glkvm.com/](https://glkvm.com/){target="_blank"} e inicie sesión con su cuenta de la nube GL.iNet.

    ![Iniciar sesión en la nube](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. La página tendrá el siguiente aspecto después de iniciar sesión.

    ![Página de dispositivos](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Haga clic en **Add Device** y seleccione **Bind with Code**.

    ![Añadir un dispositivo con código](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. Introduzca el código dinámico de 8 dígitos en la ventana emergente y haga clic en **Bind**.

    ![Introducir el código dinámico](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Nota**: el código es válido durante 60 segundos. Si caduca, vuelva a la consola KVM y haga clic en **Regenerate Code** para obtener uno nuevo.

    ![Generar un código nuevo](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

    El dispositivo quedará vinculado a su cuenta de la nube.

## Acceso remoto mediante la nube {#remote-access-via-cloud}

Abra un navegador, por ejemplo Google Chrome, e introduzca `glkvm.com` en la barra de direcciones. Inicie sesión con su cuenta GL.iNet en la página que aparece.

![Inicio de sesión para acceso remoto](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

Verá los dispositivos vinculados a su cuenta. Haga clic en el dispositivo al que desee acceder de forma remota.

![Seleccionar un dispositivo](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

En la nueva página, introduzca la contraseña de administrador para iniciar sesión.

![Contraseña de administrador](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

Ya puede acceder de forma remota al KVM y al dispositivo controlado mediante la nube.

![Acceso remoto establecido](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
