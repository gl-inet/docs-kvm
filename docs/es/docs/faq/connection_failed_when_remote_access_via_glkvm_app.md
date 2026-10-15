# Error de conexión al acceder de forma remota mediante la aplicación GLKVM {#connection-failed-when-remote-access-via-glkvm-app}

Al acceder de forma remota mediante la aplicación GLKVM, puede ocurrir que el dispositivo KVM aparezca como Online, pero al hacer clic en él se quede en "Connecting".

![Dispositivo en línea](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/device_online.png){class="glboxshadow"}

![Conectando](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connecting.png){class="glboxshadow"}

Guía de solución de problemas:

1. Asegúrese de que la conexión de red sea estable.

    Compruebe que el KVM tenga una conexión estable a Internet. Un LED blanco fijo indica que la conexión de red funciona normalmente.

2. Compruebe las reglas del cortafuegos de la red.

    Desactive temporalmente el cortafuegos local o añada los dominios relacionados con GL.iNet (por ejemplo, glkvm.com) a su lista de permitidos. Vuelva a intentar la conexión después de aplicar los cambios.

    A continuación se muestra cómo modificar las reglas del cortafuegos de Sky Network.

    ??? note "Sky Network (por ejemplo, Sky Max Hub)"

        El mecanismo de seguridad de Sky Network puede identificar el dominio `glkvm.com` como sospechoso y bloquear su acceso. Puede eliminar las restricciones mediante la aplicación de Sky.<br>

        1. Abra la aplicación MySky, vaya a **Broadband** -> **Advanced Security** y compruebe si hay dominios relacionados con GL.iNet restringidos.

            ![MySky: comprobación de dominios](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-1.png){class="glboxshadow"}

        2. Si el dominio está bloqueado, haga clic en la flecha hacia abajo para ver los detalles y seleccione **Allow Access** para desbloquearlo.

            ![MySky: permitir acceso](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-2.png){class="glboxshadow" width="300"}

3. Desactive la VPN o el proxy en el dispositivo de control.

    Asegúrese de que el dispositivo que ejecuta la aplicación GLKVM no tenga servicios VPN o proxy activados, ya que pueden interferir en la conexión.

4. Reinicie el KVM si es posible.

    Si es posible, reinicie físicamente el dispositivo KVM para resolver problemas temporales de red o software.

    Si no se encuentra cerca del KVM, puede reiniciarlo de forma remota desde la aplicación GLKVM:

    1. En la lista de dispositivos, haga clic en **Manage**, en la esquina superior derecha de su dispositivo.

        ![Aplicación: administrar dispositivo](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_1.png){class="glboxshadow"}

    2. Haga clic en **More** y seleccione **Reboot**.

        ![Aplicación: reiniciar dispositivo](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_2.png){class="glboxshadow"}

Notas técnicas adicionales:

1. Compruebe que la resolución DNS de los dominios funcione.

2. Confirme que no se bloquee el tráfico saliente hacia los puertos habituales de KVM y acceso remoto.

3. En redes empresariales, consulte con los administradores de TI las posibles políticas de filtrado de tráfico.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
