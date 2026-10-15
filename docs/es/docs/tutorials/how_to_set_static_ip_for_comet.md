# Cómo configurar una IP estática para el KVM {#how-to-set-a-static-ip-for-kvm}

Este tutorial explica cómo establecer una IP estática para el KVM GL.iNet directamente en la consola cuando el router al que está conectado no puede asignarle una.

Seleccione los pasos correspondientes a su versión de firmware.

## Firmware v1.9 y anteriores {#firmware-v19-and-earlier}

En este ejemplo se utiliza Comet (GL-RM1).

1. Inicie sesión en la consola de Comet y vaya a **Settings** -> **Network**. Haga clic en la dirección IP o en la flecha hacia la derecha.

    ![Ajustes de red](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/settings-network.png){class="glboxshadow"}

2. Cambie a **Static**. Introduzca una IP dentro del rango de la subred, la máscara de red, la puerta de enlace y los servidores DNS de Comet. Después haga clic en **Confirm**.

    ![Configuración de Ethernet estática](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/ethernet-settings-static.png){class="glboxshadow"}

## Firmware v1.10 y posteriores {#firmware-v110-and-above}

En este ejemplo se utiliza Comet Pro (GL-RM10).

1. Inicie sesión en la consola de Comet Pro y haga clic en el icono Settings de la barra de navegación para abrir los ajustes.

    ![Abrir los ajustes de red](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/setting_network.png){class="glboxshadow"}

2. Vaya a **Network** y haga clic en **Static**, en Ethernet Settings. Introduzca una IP dentro del rango de la subred, la máscara de red, la puerta de enlace y los servidores DNS de Comet Pro. Después haga clic en **Confirm**.

    ![Ajustes estáticos de Ethernet](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/ethernet_settings_static.png){class="glboxshadow"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
