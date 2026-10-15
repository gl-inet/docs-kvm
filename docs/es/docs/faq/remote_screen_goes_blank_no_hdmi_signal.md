# Qué hacer si la pantalla remota queda en blanco o no muestra señal HDMI {#what-should-i-do-if-the-remote-screen-goes-blank-or-shows-no-hdmi-signal}

Si al acceder al dispositivo controlado mediante KVM la pantalla remota queda en blanco o no muestra señal HDMI, siga estos pasos para identificar el problema.

![Pantalla blanca](https://static.gl-inet.com/docs/kvm/faq/blank_screen/white_screen.png){class="glboxshadow"}
<small>(Pantalla blanca)</small>

![Pantalla negra](https://static.gl-inet.com/docs/kvm/faq/blank_screen/black_screen.png){class="glboxshadow"}
<small>(Pantalla negra)</small>

Primero compruebe si el problema está relacionado con la transmisión de vídeo. Inicie sesión en el KVM, vaya a **Settings** -> **Video** -> **Transfer** y seleccione **Direct**.

![Cambiar el modo de transmisión](https://static.gl-inet.com/docs/kvm/faq/blank_screen/change_transfer.png){class="glboxshadow" width="360"}

Si el problema persiste, compruebe una por una las posibles causas siguientes.

## Comprobar las conexiones físicas {#check-hardware-connection}

1. **Cable HDMI defectuoso**

    El desgaste del cable HDMI, los conectores oxidados o las roturas internas pueden interrumpir la señal. Sustituya el cable por uno HDMI de buena calidad.

    También puede comprobar el estado de la señal HDMI en la consola KVM. Busque el icono de monitor de la esquina inferior derecha y compruebe si indica "No HDMI signal".

    ![Sin señal HDMI](https://static.gl-inet.com/docs/kvm/faq/blank_screen/no_hdmi_signal.png){class="glboxshadow"}

2. **Conexión incorrecta**

    Si el dispositivo controlado es un equipo de escritorio, conecte el puerto **HDMI IN** del KVM al puerto HDMI OUT de la tarjeta gráfica o placa base. Asegúrese de que los conectores estén completamente insertados y firmes. Si hay varias salidas HDMI, por ejemplo una en la GPU dedicada y otra en la placa base, pruebe otro puerto.

    Si es un portátil, conecte el puerto **HDMI IN** del KVM al HDMI OUT del portátil.

    Consejo: algunos modelos, como Comet Pro y Comet 5G, tienen dos puertos HDMI. El cable procedente del dispositivo controlado debe conectarse a HDMI IN del KVM. Si se conecta a HDMI OUT, la consola KVM no detectará señal HDMI.

3. **Uso incorrecto de adaptadores**

    Si necesita un adaptador HDMI, utilice uno de **VGA a HDMI** para conectar el dispositivo controlado al puerto HDMI IN del KVM GL.iNet.

    Un adaptador de HDMI a VGA no transmitirá correctamente la señal en esta conexión y la pantalla quedará en blanco.

    ![Comparación de adaptadores](https://static.gl-inet.com/docs/kvm/faq/blank_screen/adapter_comparison.png){class="glboxshadow"}

## Comprobar los ajustes del navegador {#check-browser-settings}

Si accede mediante un navegador y la pantalla queda en blanco, pruebe estos métodos:

1. **Pruebe varios navegadores.** Utilice Chrome, Firefox, Edge u otros para determinar si el problema depende del navegador.

2. **Desactive las extensiones de protección o control de fugas WebRTC.** Si tiene extensiones o complementos que puedan afectar a las conexiones WebRTC, desactívelos y vuelva a probar. También puede ir a Settings -> Privacy & Security del navegador para comprobar que permita conexiones WebRTC.

    ![Configuración de WebRTC](https://static.gl-inet.com/docs/kvm/faq/blank_screen/webrtc.png){class="glboxshadow"}

## Comprobar el estado y los ajustes del dispositivo controlado {#check-controlled-device-status-and-settings}

1. **Dispositivo apagado o en suspensión**

    Asegúrese de que esté completamente encendido y no se encuentre en suspensión o hibernación por los ajustes de energía. Si es necesario, reactívelo mediante sus botones físicos.

2. **Problemas con los controladores de la tarjeta gráfica**

    La ausencia o corrupción de estos controladores puede impedir la salida de vídeo. Actualícelos o reinstálelos en el dispositivo controlado mediante una sesión local.

3. **Conexión incorrecta entre gráficos dedicados e integrados**

    Si el dispositivo tiene gráficos dedicados e integrados, conecte el cable HDMI al puerto correcto; por ejemplo, al de la tarjeta gráfica dedicada si está instalada.

4. **Ajustes de pantalla incorrectos en el dispositivo controlado, poco frecuente**

    Cuando el KVM GL.iNet se conecta al dispositivo controlado, ajusta automáticamente la salida de pantalla leyendo el EDID del monitor para obtener un rendimiento óptimo. El EDID predeterminado suele ser adecuado y no necesita modificarse.

    Si el dispositivo funciona con monitores estándar, es poco probable que aparezcan pantallas en blanco u otros problemas de imagen al acceder mediante GLKVM. Sin embargo, algunas incompatibilidades específicas, por ejemplo un sistema Linux con un monitor ASUS, pueden provocar pantallas en blanco.

    Compruebe si el dispositivo controlado es compatible con monitores estándar y si presenta incompatibilidades con algún monitor concreto.

5. **Problemas de resolución**

    Al conectarse a determinados sistemas operativos, como Proxmox VE Hypervisor, GLKVM puede no negociar correctamente la resolución disponible y provocar problemas de imagen. Puede resolverlo ajustando manualmente la resolución del dispositivo controlado.

    A continuación se muestra cómo modificarla en Proxmox VE Hypervisor.

    1. Abra el terminal de PVE y ejecute este comando para editar `/etc/default/grub`.

        ```
        nano /etc/default/grub
        ```

    2. Añada la siguiente línea.

        ```
        GRUB_CMDLINE_LINUX_DEFAULT="quiet gfxpayload=text nomodeset"
        ```

    3. Quite el `#` de la línea `GRUB_GFXMODE` para activarla y establezca la resolución deseada, por ejemplo `1024x768`.

        ```
        GRUB_GFXMODE=1024x768
        ```

    4. Pulse `Ctrl + O` y después Intro para guardar la configuración.

    5. Pulse `Ctrl + X` para salir del editor nano.

    6. Ejecute este comando para aplicar la configuración.

        ```
        update-grub
        ```

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
