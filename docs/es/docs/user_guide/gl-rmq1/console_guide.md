# Guía de la consola de Comet Q (GL-RMQ1) {#comet-q-gl-rmq1-console-guide}

## Ajustes {#settings}

En la consola, vaya a **Settings**. La página de ajustes incluye cuatro secciones:

- [Vídeo](#video)
- [Audio, teclado y ratón](#audiokeyboardmouse)
- [Sistema](#system)
- [Red](#network)

### Búsqueda rápida {#quick-search}

Puede encontrar rápidamente los ajustes que necesite introduciendo palabras clave en la parte superior de la página Settings.

![Búsqueda rápida](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/quick-search.png){class="glboxshadow"}

### Vídeo {#video}

Puede personalizar los ajustes de vídeo de la consola, como el EDID, la calidad de vídeo, la transmisión de vídeo y la orientación de la pantalla.

![Ajustes de vídeo](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-video.png){class="glboxshadow"}

- **Type**: Seleccione el tipo de dispositivo controlado.

    El sistema aplica automáticamente el modo de ratón y los ajustes EDID recomendados para ofrecer la mejor relación de aspecto y precisión de control. Cambie esta opción si el dispositivo no se reconoce correctamente o necesita utilizar un tipo personalizado.

- **EDID**: Abreviatura de Extended Display Identification Data (datos de identificación de pantalla extendidos); permite seleccionar automáticamente los parámetros de visualización óptimos.

    El ajuste predeterminado es adecuado para la mayoría de los casos y, por lo general, no necesita modificarse. Consulte los detalles [aquí](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. Si la pantalla no se actualiza después de ajustar el EDID, reinicie el dispositivo controlado.

- **Mode**: Alterne entre los modos Smart y Normal según sea necesario. El modo Smart ayuda a reducir el consumo de ancho de banda, especialmente en redes de baja calidad.

- **Quality**: Ajuste la calidad de vídeo a Low/Medium/High/Ultra-high/Lossless según las condiciones de la red y sus requisitos de resolución.

- **Transfer**: Cambie el método de transmisión de vídeo entre WebRTC, WebRTC (FEC) y Direct. Tenga en cuenta que la transmisión Direct no tiene sonido.

    !!! note "¿Qué diferencia hay entre WebRTC, WebRTC (FEC) y Direct?"

        - **WebRTC**: Equilibra la fluidez del vídeo y la estabilidad del audio para el control remoto en tiempo real.

        - **WebRTC (FEC)**: Añade corrección de errores hacia delante para mejorar la estabilidad de la conexión cuando la red es deficiente o inestable. Al seleccionarlo, repara automáticamente los paquetes de datos perdidos mediante la transmisión de una pequeña cantidad de datos redundantes, lo que reduce los parpadeos de la pantalla y los retrasos.

        - **Direct**: Ofrece la menor latencia y una calidad de vídeo sin pérdida, pero no admite la transmisión de audio.

- **Orientation**: Ajuste el ángulo de rotación de la consola a 0°/90°/180°/270°.

- **View**: Este ajuste determina cómo se escala la pantalla al cambiar el tamaño de la ventana del navegador. Opciones disponibles: Adaptive, Best Picture Quality y Original Pixel.

### Audio, teclado y ratón {#audiokeyboardmouse}

Puede ajustar las opciones de audio, teclado y ratón.

![Audio, teclado y ratón](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/audio-keyboard-mouse.png){class="glboxshadow"}

- **Speaker**: Controle la salida de audio del dispositivo controlado, como los sonidos del sistema o el audio de los vídeos.

- **Microphone**: Transmita audio local, como su voz, desde el dispositivo de control al extremo remoto. Permite silenciar el micrófono con un clic y activarlo manteniendo pulsado un atajo de teclado (Press To Speak).

    ![Ajustes del micrófono](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/mic-settings.png){class="glboxshadow"}

    ![Pulsar para hablar](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/press-to-speak.png){class="glboxshadow"}

- **Keyboard**: Active o desactive el teclado del dispositivo controlado.

- **Bad Link Mode**: Libera las teclas inmediatamente. Cada pulsación se envía como una única acción rápida de pulsar y soltar, lo que evita teclas bloqueadas o entradas repetidas involuntarias durante el control remoto.

- **Show Virtual Keyboard**: Muestre y utilice el teclado virtual en la consola.

    ![Mostrar el teclado virtual](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: Intercambia las teclas Cmd y Ctrl para garantizar la compatibilidad del teclado entre distintos sistemas operativos.

- **Mouse**: Active o desactive el ratón del dispositivo controlado.

- **Show Local Cursor**: Muestre el cursor del dispositivo actual en la pantalla.

- **Mouse Jiggle**: Simula movimientos leves y periódicos del ratón para evitar que el dispositivo controlado entre en suspensión por una inactividad prolongada, por ejemplo, durante reuniones remotas o la administración de servidores.

- **Scroll Rate**: Es la velocidad de desplazamiento de la rueda del ratón o el número de líneas o unidades que se desplazan por cada giro. Determina la rapidez con la que se mueve el contenido en el dispositivo remoto.

- **Scroll Direction**: Determina si, al girar la rueda del ratón hacia arriba o abajo, el contenido de la pantalla remota se mueve en la misma dirección (desplazamiento natural) o en la dirección opuesta (desplazamiento tradicional).

    Hay cuatro modos de dirección: Standard, Vertical Invert, Horizontal Invert y Both Invert.

- **Mouse Mode**: Permite alternar entre Absolute Mode y Relative Mode para garantizar un control fluido y preciso del cursor en distintas situaciones de control remoto.

    !!! note "¿Qué diferencia hay entre Absolute Mode y Relative Mode?"

        - **Relative Mode**: La posición del ratón se calcula a partir del movimiento en lugar de coordenadas fijas de la pantalla. Debe hacer clic dentro de la ventana remota para controlar el ratón. El cursor queda bloqueado dentro de la pantalla remota y no puede salir de ella de forma fluida. Este modo ofrece mayor compatibilidad con BIOS, sistemas antiguos y dispositivos integrados.

        - **Absolute Mode**: La posición del ratón corresponde a coordenadas exactas de la pantalla. El cursor remoto sigue al local con fluidez y precisión, lo que permite pasar sin interrupciones entre la pantalla local y la remota. Es ideal para el control habitual del escritorio y las operaciones precisas, aunque la transmisión por red puede ocasionar un ligero retraso.

        Utilice Absolute para el control cotidiano con fluidez; utilice Relative para acceder a la BIOS, controlar dispositivos antiguos que no admitan posicionamiento absoluto o evitar movimientos involuntarios del cursor.

- **Relative Sensitivity**: Está disponible cuando Mouse Mode está configurado en Relative.

### Sistema {#system}

Puede personalizar los ajustes de visualización del sistema de la consola o restablecer el dispositivo con un clic.

![Ajustes del sistema](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-system.png){class="glboxshadow"}

- **Device Identity**: Personalice o modifique la identidad con la que el dispositivo controlado reconoce al KVM. Tenga en cuenta que el EDID y la identificación del dispositivo permanecen sincronizados. Al cambiar uno de ellos, el otro se actualiza automáticamente para garantizar el reconocimiento correcto del dispositivo.

    ![Identidad del dispositivo](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/device-identity.png){class="glboxshadow"}

- **Language**: Establezca el idioma de la consola en chino o inglés.

- **Color Mode**: Personalice el tema con el modo Light o Dark.

- **Time Zone**: Personalice la zona horaria de la consola KVM.

- **Reset KVM**: Restablezca los valores de fábrica del KVM con un solo clic.

### Red {#network}

Puede consultar y modificar los datos de red de Comet Q, como el nombre de host y la dirección IP.

![Ajustes de red](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-network.png){class="glboxshadow"}

- **Hostname**: Puede modificar el nombre de host del dispositivo directamente en la consola.

    ![Modificar el nombre de host](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/hostname.png){class="glboxshadow"}

- **Wi-Fi**: La dirección IP Wi-Fi de Comet Q aparecerá aquí cuando se conecte a una red Wi-Fi. Haga clic en el SSID Wi-Fi o en la flecha derecha para consultar los datos de Wi-Fi, como el SSID, la dirección IP asignada, la puerta de enlace y la dirección MAC que Comet Q utiliza para conectarse.

    ![Configuración de Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/wifi-config.png){class="glboxshadow"}

    Para conectarlo a otra red Wi-Fi, haga clic en **Switch Wi-Fi** y seleccione una red de la lista de redes disponibles.

## Herramientas {#toolbox}

En la consola, vaya a **Toolbox**. La página de herramientas incluye tres secciones:

- [Portapapeles](#clipboard)
- [Atajos](#shortcut)
- [Terminal](#terminal)

### Portapapeles {#clipboard}

El portapapeles permite pegar fácilmente texto del dispositivo de control en el dispositivo controlado sin tener que transferir archivos.

![Portapapeles de las herramientas](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-clipboard.png){class="glboxshadow"}

### Atajos {#shortcut}

Los atajos permiten realizar acciones con mayor rapidez sin utilizar el teclado virtual, lo que mejora la eficiencia y ahorra tiempo en las tareas cotidianas. Aquí encontrará algunos atajos habituales.

![Atajos de las herramientas 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut1.png){class="glboxshadow"}

Haga clic en **Modify** para ajustar las opciones de los atajos según sea necesario.

![Atajos de las herramientas 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut2.png){class="glboxshadow"}  

### Terminal {#terminal}

Puede acceder al terminal de Comet Q para realizar ajustes avanzados. Haga clic en **Access**.

![Terminal de las herramientas 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal1.png){class="glboxshadow"}

Se le redirigirá al terminal de GLKVM.

![Terminal de las herramientas 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal2.png){class="glboxshadow"}

## Medios virtuales {#virtual-media}

En la consola, vaya a **Virtual Media**. Comet Q puede emular una unidad USB de lectura y escritura para compartir y gestionar archivos entre el dispositivo de control y el dispositivo controlado.

![Medios virtuales](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-media.png){class="glboxshadow"}

### Compartir archivos {#file-sharing}

**Para compartir archivos del dispositivo de control con el dispositivo controlado, siga estos pasos.**

1. Arrastre archivos al recuadro o haga clic en él para cargarlos desde el dispositivo de control; también puede cargarlos desde una URL.

    Una vez cargados, los archivos aparecerán como se muestra a continuación.

    ![Compartir archivos 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing1.png){class="glboxshadow"}

2. Haga clic en **Mount To Remote** -> **File Sharing**.

    ![Compartir archivos 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing2.png){class="glboxshadow"}

3. Aparecerá una ventana en la consola con los pasos para compartir archivos, como se muestra a continuación.

    ![Compartir archivos 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing3.png){class="glboxshadow"}

4. Espere un momento; puede que aparezca automáticamente en la pantalla una unidad llamada **"GLKVM"**. Los archivos que cargó previamente del dispositivo de control a Comet Q se habrán compartido con el dispositivo controlado. Ahora puede ver, mover o eliminar los archivos de esta unidad desde el dispositivo controlado.

    ![Compartir archivos 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing4.png){class="glboxshadow"}

    **Consejo**: Si la unidad no aparece automáticamente, vaya a **This PC** en el dispositivo controlado.

    ![This PC](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/thispc.png){class="glboxshadow"}

    Busque una unidad llamada **GLKVM**. Ahora puede ver, mover o eliminar los archivos de esta unidad.

5. Para dejar de compartir, haga clic en **Virtual Media** en la barra de herramientas y, a continuación, en **Stop Sharing**.

    ![Dejar de compartir 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing1.png){class="glboxshadow"}

**Para compartir archivos del dispositivo controlado con el dispositivo de control, siga estos pasos.**

1. En el dispositivo controlado, mueva o copie los archivos que desea compartir a la unidad **GLKVM**.

    Por ejemplo, se ha movido un archivo PDF llamado "gl-rm10_datasheet" del escritorio del dispositivo controlado a la unidad **GLKVM**.

    ![Compartir archivos 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing5.png){class="glboxshadow"}

2. Vuelva a la consola de Comet Q, haga clic en **Virtual Media** en la barra de herramientas y, a continuación, en **Stop Sharing**.

    ![Dejar de compartir 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing2.png){class="glboxshadow"}

3. El archivo aparecerá en **Virtual Media**, como se muestra a continuación. Ahora puede descargarlo desde Comet Q al dispositivo de control.

    ![Compartir archivos 6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing6.png){class="glboxshadow"}

### Formatear el disco {#format-disk}

Puede formatear el disco o desactivar los medios virtuales con un clic.

![Formatear el disco](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/format-disable.png){class="glboxshadow"}

- **Format**: Borre todos los datos del disco y reinicialice la estructura de su sistema de archivos.

- **Disable**: Al desactivar los medios virtuales, el dispositivo KVM se reiniciará inmediatamente.

## Centro de aplicaciones {#apps-center}

En la consola, vaya a **Apps Center**. Aquí encontrará las aplicaciones integradas.

![Centro de aplicaciones](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} es un servicio VPN de malla basado en WireGuard que crea redes privadas cifradas entre dispositivos sin necesidad de redireccionar puertos ni configurar complejas reglas de cortafuegos.

Comet Q integra Tailscale, lo que permite acceder a él de forma remota a través de la red virtual de Tailscale.

Solo tiene que vincular Comet Q y el dispositivo de control a la misma cuenta de Tailscale. Después podrá acceder a Comet Q de forma remota introduciendo su **IP virtual de Tailscale** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM. Consulte los detalles [aquí](../../faq/remote_access_via_tailscale.md){target="_blank"}.

Después de la vinculación, la consola muestra la cuenta de Tailscale vinculada y habilita funciones avanzadas como Exit Node y Subnet Routes.

![Tailscale activado](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} crea redes virtuales superpuestas cifradas para conectar dispositivos distribuidos por todo el mundo como si estuvieran en la misma red local.

Comet Q integra ZeroTier, lo que permite acceder a él de forma remota a través de la red virtual de ZeroTier.

Solo tiene que unir Comet Q y el dispositivo de control a la misma red de ZeroTier. Después podrá acceder a Comet Q de forma remota introduciendo su **IP de ZeroTier** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM. Consulte los detalles [aquí](../../faq/remote_access_via_zerotier.md){target="_blank"}.

Después de la vinculación, la consola muestra el Network ID y la IP virtual de ZeroTier.

![ZeroTier activado](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-zerotier-enabled.png){class="glboxshadow"}

## Ayuda {#help}

En la consola, vaya a **Help**. Aquí encontrará más información sobre GL.iNet KVM y documentación de ayuda; también podrá exportar registros para solucionar problemas.

![Ayuda](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/help.png){class="glboxshadow"}

## Barra de herramientas {#toolbar}

En la consola, vaya a la esquina superior derecha para acceder a las siguientes herramientas:

- [Contraer la barra de herramientas](#collapse)
- [Pantalla completa](#fullscreen)
- [Actualizar](#upgrade)
- [Servicio en la nube](#cloud-service)
- [Seguridad](#security)
- Reboot
- Logout

### Contraer {#collapse}

Haga clic en el icono de flecha hacia arriba de la esquina superior derecha para contraer la barra de herramientas.

![Contraer](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse1.png){class="glboxshadow"}

Cuando la barra esté contraída, haga clic en el icono de flecha hacia abajo de la parte superior para expandirla.

![Contraer](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse2.png){class="glboxshadow"}

### Pantalla completa {#fullscreen}

Haga clic en el icono de pantalla completa (con forma de cuadrado) de la esquina superior derecha para activar el modo de pantalla completa.

![Pantalla completa](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen1.png){class="glboxshadow"}

Para salir de la pantalla completa, mantenga pulsada la tecla **Esc** o haga clic en el icono para salir de la pantalla completa (con forma de cuadrícula) de la esquina superior derecha.

![Pantalla completa](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen2.png){class="glboxshadow"}

### Actualizar {#upgrade}

Haga clic en la versión del firmware de la esquina superior derecha para buscar actualizaciones.

![Actualizar el firmware](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade1.png){class="glboxshadow"}

En la ventana emergente, puede realizar una actualización en línea si hay un firmware más reciente disponible. También puede descargar el firmware más reciente del [centro de descarga de firmware](https://dl.gl-inet.com/kvm){target="_blank"} y realizar una actualización local según sea necesario.

![Actualizar el firmware](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade2.png){class="glboxshadow"}

### Servicio en la nube {#cloud-service}

GL.iNet KVM Cloud permite acceder al dispositivo controlado de forma remota. Consulte los detalles [aquí](../../faq/remote_access_via_cloud.md){target="_blank"}.

Una vez que Comet Q esté vinculado a la nube, la consola mostrará el estado de la nube como se indica a continuación.

![Servicio en la nube](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/cloud.png){class="glboxshadow"}

### Seguridad {#security}

Security permite cambiar la contraseña de administrador, activar la autenticación de dos factores y personalizar el certificado TLS.

![Seguridad](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/security.png){class="glboxshadow"}

- Change Admin Password

    ![Cambiar la contraseña de administrador](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/admin-password.png){class="glboxshadow" width="434"}

- 2FA: Active la autenticación de dos factores para proteger su cuenta.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/2fa.png){class="glboxshadow"}

- TLS Certificate

    El sistema utiliza el certificado predeterminado preinstalado para el acceso desde el navegador. Para personalizar el certificado TLS utilizado en ese acceso, haga clic en **TLS Certificate** en la esquina superior derecha de la consola, seleccione **Custom Certificate** y cargue su **archivo de certificado y su archivo de clave privada**.

    ![Certificado TLS personalizado](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/tls-certificate.png){class="glboxshadow"}
