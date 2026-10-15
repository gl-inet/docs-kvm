# Cómo cambiar el nombre de equipo del KVM {#how-to-change-kvm-hostname}

El nombre de equipo predeterminado del KVM GL.iNet es **glkvm**, por lo que puede acceder de forma local mediante el dominio `glkvm.local` si está conectado a la misma red.

Este tutorial explica dos métodos para cambiarlo: mediante la consola KVM o mediante comandos de terminal.

## Método 1. Consola KVM {#method-1-kvm-console}

> **Nota**: esta función está disponible desde el firmware 1.7.0.

### Firmware v1.10 y posteriores {#firmware-v110-and-above}

1. Inicie sesión en el KVM y haga clic en el icono Settings de la barra de navegación para abrir la página de ajustes.

    ![Ajustes de red](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings-network.png){class="glboxshadow"}

2. Vaya a **Network** e introduzca el nombre de equipo personalizado. El cambio se aplicará.

    ![Modificar el nombre de equipo](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify-hostname.png){class="glboxshadow"}

### Firmware v1.9 y anteriores {#firmware-v19-and-earlier}

1. Inicie sesión en el KVM y vaya a **Settings** -> **Network**. Haga clic en el nombre de equipo o en la flecha hacia la derecha.

    ![Ajustes de red](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings_network.png){class="glboxshadow"}

2. Personalice el nombre y haga clic en **Apply**.

    ![Aplicar el nombre de equipo](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify_hostname.png){class="glboxshadow"}

## Método 2. Comandos de terminal {#method-2-terminal-commands}

1. Inicie sesión en el KVM y vaya a **Toolbox** -> **Terminal**. Haga clic en **Access**.

    ![Acceder al terminal](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_terminal.png){class="glboxshadow"}

2. Introduzca el siguiente comando y pulse Intro. Sustituya "example" por el nombre deseado. El KVM se reiniciará.

    `echo example > /etc/hostname && reboot`

    ![Introducir el comando](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/input_command.png){class="glboxshadow"}

3. Espere a que se reinicie. Después podrá acceder al KVM mediante el nuevo nombre de equipo.

    ![Acceder mediante el nuevo nombre](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_new_hostname.png){class="glboxshadow"}

    Si olvida el nombre o desea comprobar el cambio, ejecute este comando en el terminal para ver el nombre actual.

    `cat /etc/hostname`

    ![Comprobar el nombre de equipo](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/verify_hostname.png){class="glboxshadow"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
