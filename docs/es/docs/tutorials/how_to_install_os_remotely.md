# Cómo instalar un sistema operativo de forma remota mediante Virtual Media {#how-to-install-an-os-on-the-controlled-computer-remotely-using-virtual-media}

Este tutorial explica cómo instalar de forma remota un sistema operativo en el equipo controlado mediante Virtual Media, una función del KVM GL.iNet.

1. Inicie sesión en el KVM GL.iNet y vaya a **Virtual Media**.

2. Cargue el archivo ISO del sistema operativo en Virtual Media.

    ![Cargar el archivo](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/upload_file.png){class="glboxshadow"}

3. Haga clic en **Mount To Remote** y seleccione **Image mounting** para montar la imagen ISO.

    ![Montaje de imagen](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-1.png){class="glboxshadow"}

    Seleccione la imagen y haga clic en **Mount Image**.

    ![Montar la imagen seleccionada](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-2.png){class="glboxshadow"}

4. Reinicie el equipo controlado y **pulse inmediatamente la tecla correspondiente** durante el arranque para entrar en BIOS/UEFI; en este ejemplo se utiliza DEL.

    ![Entrar en la BIOS](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/enter_bios.png){class="glboxshadow"}

5. En el menú de arranque, establezca **"Glinet Flash Drive 1.00"** como Boot Option #1.

    ![Establecer la prioridad de arranque](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/set_boot_option_priority.png){class="glboxshadow"}

6. Guarde los cambios y salga de la BIOS. El sistema arrancará desde la ISO montada para iniciar la instalación.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
