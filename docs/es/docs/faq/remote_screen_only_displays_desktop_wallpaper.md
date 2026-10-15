# Qué hacer si la pantalla remota solo muestra el fondo de escritorio {#what-should-i-do-if-the-remote-screen-only-displays-the-desktop-wallpaper}

Si al acceder al dispositivo controlado mediante KVM solo ve el fondo de escritorio y las operaciones no responden, es probable que el equipo utilice varios monitores en modo **Extend Displays**.

Para resolverlo, cambie el modo de pantalla del dispositivo controlado a **Duplicate display** en Windows o **Mirror display** en macOS.

Seleccione la solución correspondiente a su sistema operativo.

=== "Windows"
    En este ejemplo se utiliza Windows 10. Si está activado **Extend these displays**, siga estos pasos para cambiar a **Duplicate display**.

    ![Pantallas extendidas](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/extend_displays.jpg){class="glboxshadow"}

    1. En el dispositivo controlado, vaya a **Settings** -> **System** -> **Display**.

        ![Ajustes del sistema en Windows 10](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/win10_system_settings.png){class="glboxshadow"}

    2. Desplácese por la página Display hasta **Multiple displays**.

    3. Cambie de Extend Displays a **Duplicate display**.

        ![Duplicar pantallas](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/duplicate_displays.jpg){class="glboxshadow"}

    4. Haga clic en **Keep changes**.

        ![Conservar los cambios](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/keep_changes.png){class="glboxshadow"}

    Compruebe si ya puede acceder al dispositivo controlado con normalidad.

=== "macos"
    1. Haga clic en el menú Apple de la esquina superior izquierda y seleccione **System Settings**.

    2. Desplácese por la barra lateral y seleccione **Displays**.

        ![Ajustes del sistema en macOS](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-system-settings.png){class="glboxshadow"}

    3. En la vista de disposición, haga clic en **External display**. Verá la pantalla del MacBook y los monitores conectados.

    4. Abra el desplegable **Use as** y seleccione **Mirror mode**, normalmente Mirror for Built-in Display.

        ![Duplicación de pantalla en macOS](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-mirror-display.png){class="glboxshadow"}

    Una vez configurado, podrá acceder de forma remota a todo el escritorio y a todas las ventanas de aplicaciones del dispositivo controlado.

!!! Note "Nota"
    Esta solución solo se aplica a problemas provocados por el modo de pantalla extendida. Si el problema persiste después de activar la duplicación, compruebe que se haya iniciado sesión de forma local y que el dispositivo no esté detenido en la pantalla de inicio de sesión del sistema.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
