# ¿Qué hacer si el cursor local y el remoto no coinciden? {#what-should-i-do-if-the-local-and-remote-cursors-dont-match}

Si el cursor local (en el dispositivo de control) no coincide con el cursor remoto (en el dispositivo controlado), siga estos pasos para resolver el problema.

![Cursores desalineados](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/mouse_cursor.png){class="glboxshadow"}

1. Si los cursores coinciden cuando el ratón está quieto, pero se desincronizan al moverlo, compruebe la red en ambos extremos y asegúrese de que la conexión sea estable.

    También puede ocultar el cursor local para que en la pantalla de control solo aparezca el remoto y evitar la desalineación visual.

    En la consola KVM, vaya a **Settings** -> **Remote Device Settings** -> **Show Local Cursor** y desactive la opción.

    ![Ocultar el cursor local](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/hide_local_cursor.jpg){class="glboxshadow"}

2. Si los cursores tampoco coinciden cuando el ratón está quieto y su KVM es un Comet Q (GL-RMQ1), vuelva a seleccionar el tipo de dispositivo en la consola KVM. Si el problema persiste, continúe con el siguiente paso.

    ![Tipo de dispositivo](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/device_type.png){class="glboxshadow"}

3. Si el dispositivo controlado es un portátil, probablemente la resolución de pantalla sea incorrecta.

    Compruebe la relación de aspecto de su pantalla. Después ajuste la resolución del portátil controlado o modifique los ajustes EDID del KVM.

    ??? note "Ajustar la resolución del portátil controlado"

        **En macOS**:

        1. Vaya a **Settings** -> **Displays** -> **Optimize for**.

            ![Pantallas en macOS](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos1.png){class="glboxshadow" width="582"}

        2. Seleccione **GLKVM**.

            ![Seleccionar GLKVM](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos2.png){class="glboxshadow" width="582"}

        3. Elija la resolución correspondiente y compruebe si los cursores coinciden.

            ![Resolución de pantalla](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos3.png){class="glboxshadow"}

        **En Windows**:

        1. Vaya a **Settings** -> **System** -> **Displays**.

            ![Pantalla en Windows](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows1.png){class="glboxshadow"}

        2. Desplácese hasta **Display resolution** y haga clic en el cuadro de la derecha.

            ![Resolución de pantalla](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows2.png){class="glboxshadow"}

        3. Seleccione la resolución adecuada y haga clic en **Keep changes** en la ventana emergente para aplicarla.

            ![Seleccionar resolución](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows3.png){class="glboxshadow"}

            ![Conservar los cambios de resolución](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows4.png){class="glboxshadow"}

    ??? note "Modificar los ajustes EDID del KVM"

        EDID significa Extended Display Identification Data y permite seleccionar automáticamente los parámetros de visualización óptimos. El EDID predeterminado es adecuado para la mayoría de los casos y normalmente no necesita modificarse. Consulte [Cómo configurar el EDID para GL.iNet KVM](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}.

        Si modifica el EDID y la pantalla no se actualiza, pruebe a reiniciar el dispositivo controlado.

4. Si el dispositivo controlado no es un portátil, por ejemplo un equipo de escritorio con monitor externo, compruebe la relación de aspecto de su pantalla principal y cambie el EDID del KVM según corresponda. Consulte [Cómo configurar el EDID para GL.iNet KVM](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
