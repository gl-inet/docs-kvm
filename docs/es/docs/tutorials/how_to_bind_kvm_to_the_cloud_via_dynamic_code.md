# Cómo vincular el KVM a la nube mediante un código dinámico {#how-to-bind-kvm-to-the-cloud-via-dynamic-code}

> Nota: actualice el firmware del KVM a la versión 1.7 antes de utilizar esta función.

Este tutorial explica cómo vincular fácilmente un KVM GL.iNet a la nube mediante un código dinámico.

## Pasos de vinculación {#binding-steps}

1. Acceda al KVM GL.iNet de forma local mediante su dominio o IP. Consulte los detalles [aquí](../faq/local_access_via_browser.md).

2. Vaya a **Cloud Service**, en la esquina superior derecha, y haga clic en **Bind With Code**.

    ![Vincular con código](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Se generará un código dinámico aleatorio de 8 dígitos, válido durante 60 segundos. Haga clic en él para copiarlo.

    ![Código dinámico generado](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Abra [https://glkvm.com/](https://glkvm.com/){target="_blank"} e inicie sesión con su cuenta de la nube GL.iNet.

    ![Iniciar sesión en la nube](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. La página tendrá el siguiente aspecto.

    ![Lista de dispositivos](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Haga clic en **Add Device** y seleccione **Bind with Code**.

    ![Añadir un dispositivo con código](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. En la ventana emergente, introduzca el código de 8 dígitos y haga clic en **Bind**.

    ![Introducir el código dinámico](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Nota**: el código es válido durante 60 segundos. Si caduca, vuelva a la consola KVM y haga clic en **Regenerate Code** para obtener uno nuevo.

    ![Generar un código nuevo](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

7. El dispositivo quedará vinculado a su cuenta de la nube. Haga clic en **Done**.

    ![Vinculación completada](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_7.png){class="glboxshadow"}

    El KVM aparecerá en la lista de dispositivos. Ya puede acceder a él de forma remota mediante el servicio de nube.

    ![KVM en la lista de dispositivos](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_8.png){class="glboxshadow"}

8. Haga clic en el dispositivo al que desea acceder. En la nueva página, introduzca la contraseña de administrador para iniciar sesión.

    ![Contraseña de administrador](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Ya puede acceder de forma remota al KVM y al dispositivo controlado mediante la nube.

    ![Acceso remoto establecido](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

## Preguntas frecuentes {#faq}

1. **P: ¿Cuánto tiempo es válido el código dinámico? ¿Qué hago si caduca?**

    R: el código es válido durante 60 segundos. Si caduca, vuelva a la consola KVM y haga clic en **Regenerate Code** para obtener uno nuevo.

    ![Generar un código nuevo](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

2. **P: ¿Qué hago si no se puede generar el código dinámico?**

    R: puede deberse a una red inestable o a la configuración DNS de la red a la que está conectado el KVM.

    - Compruebe que la red sea estable o pruebe con otra red.

    - Modifique los ajustes DNS de la red y vuelva a generar el código.

    Si el problema persiste, contacte con soporte en [support@gl-inet.com](mailto:support@gl-inet.com).

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
