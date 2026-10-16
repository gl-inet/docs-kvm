# Guía de la consola de Comet Pro (GL-RM10) {#comet-pro-gl-rm10-console-guide}

## Sesión {#session}

En la consola, vaya a **Session**. La página de ajustes incluye cuatro secciones:

- [Vídeo](#video)
- [Audio y cámara](#audio-camera)
- [Teclado](#keyboard)
- [Ratón](#mouse)

### Vídeo {#video}

Puede personalizar los ajustes de vídeo de Session, como el modo de visualización, la calidad de vídeo, la transmisión de vídeo, la orientación de la pantalla y el EDID.

![Ajustes de vídeo](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session-video.png){class="glboxshadow"}

- **Transfer**: Cambie el método de transmisión de vídeo entre WebRTC, WebRTC (FEC), WebRTC (Native) y Direct. Tenga en cuenta que la transmisión Direct no tiene sonido.

    !!! note "¿Qué diferencia hay entre WebRTC, WebRTC (FEC), WebRTC (Native) y Direct?"

        - **WebRTC**: Equilibra la fluidez del vídeo y la estabilidad del audio para el control remoto en tiempo real.

        - **WebRTC (FEC)**: Añade corrección de errores hacia delante para mejorar la estabilidad de la conexión cuando la red es deficiente o inestable. Al seleccionarlo, repara automáticamente los paquetes de datos perdidos mediante la transmisión de una pequeña cantidad de datos redundantes, lo que reduce los parpadeos de la pantalla y los retrasos.

        - **WebRTC (Native)**: Utiliza la biblioteca Google WebRTC para mejorar el rendimiento de la transmisión y ofrecer una experiencia de control remoto en tiempo real más fluida. Este modo de transmisión se incorporó en el firmware v1.10.0.

        - **Direct**: Ofrece la menor latencia y una calidad de vídeo sin pérdida, pero no admite la transmisión de audio.

- **Mode**: Alterne entre los modos Smart y Normal según sea necesario. El modo Smart ayuda a reducir el consumo de ancho de banda, especialmente en redes de baja calidad.

- **Latency Mode**: Puede elegir entre Lowest Latency y Smooth Display para el dispositivo. Esta función se incorporó en el firmware v1.9.0.

    !!! note "¿Qué diferencia hay entre Lowest Latency y Smooth Display?"

        - **Lowest Latency**: Minimiza la latencia de entrada para que el teclado y el ratón respondan más rápido.

        - **Smooth Display**: Optimiza el rendimiento visual para eliminar los tirones y la pérdida de fotogramas y mantener una reproducción estable.

- **Quality**: Ajuste la calidad de vídeo a Auto/Low/Medium/High/Ultra-high/Lossless según las condiciones de la red y sus requisitos de resolución.

- **FEC Packets**: Cuando la red es inestable, repara automáticamente los paquetes de datos perdidos mediante el envío de una pequeña cantidad de datos redundantes, lo que reduce los parpadeos de la pantalla y los retrasos. Puede ajustar la proporción FEC a 5%/10%/15%/20%.

- **Orientation**: Ajuste el ángulo de rotación de la consola a 0°/90°/180°/270°.

- **EDID**: Abreviatura de Extended Display Identification Data (datos de identificación de pantalla extendidos); permite seleccionar automáticamente los parámetros de visualización óptimos.

    El ajuste predeterminado es adecuado para la mayoría de los casos y, por lo general, no necesita modificarse. Consulte los detalles [aquí](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. Si la pantalla no se actualiza después de ajustar el EDID, reinicie el dispositivo controlado.

- **View**: Este ajuste determina cómo se escala la pantalla al cambiar el tamaño de la ventana del navegador. Opciones disponibles: Adaptive, Best Picture Quality y Original Pixel. Esta función se incorporó en el firmware v1.8.0.

- **Screen Privacy**: Cuando se activa la privacidad de pantalla, el monitor externo HDMI-OUT deja de mostrar contenido para garantizar la privacidad de las operaciones remotas.

### Audio y cámara {#audio-camera}

Puede ajustar las opciones de audio y cámara del dispositivo controlado.

![Audio y cámara](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_audio_camera.png){class="glboxshadow"}

- **Speaker**: Controle la salida de audio del dispositivo controlado, como los sonidos del sistema o el audio de los vídeos.

- **Microphone**: Transmita audio local, como su voz, desde el dispositivo de control al extremo remoto. Permite silenciar el micrófono con un clic y activarlo manteniendo pulsado un atajo de teclado (Press To Speak).

    **Nota**: Antes de utilizarlo, debe configurar manualmente el atajo en [Settings](#usb-devices).

- **Camera**: Cuando se activa la cámara en el dispositivo de control, los fotogramas de vídeo locales se transmiten directamente al equipo remoto, donde se emula una cámara USB virtual. Las aplicaciones del equipo remoto, como las herramientas de videoconferencia y FaceTime, pueden utilizar este vídeo y ofrecer la misma experiencia que una cámara física conectada directamente al equipo remoto.

    **Nota**: Esta función se incorporó en el firmware v1.10.0 y solo se admite en el modo WebRTC (FEC). Actualmente, solo está disponible a través de un navegador web; todavía no está disponible en la aplicación ni en el cliente de escritorio.

### Teclado {#keyboard}

La sección Keyboard permite configurar el uso del teclado en el dispositivo controlado.

![Teclado](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_keyboard.png){class="glboxshadow"}

- **Bad Link Mode**: Libera las teclas inmediatamente. Cada pulsación se envía como una única acción rápida de pulsar y soltar, lo que evita teclas bloqueadas o entradas repetidas involuntarias durante el control remoto.

- **Show Virtual Keyboard**: Muestre y utilice el teclado virtual en la consola.

    ![Mostrar el teclado virtual](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_show_virtual_keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: Intercambia las teclas Cmd y Ctrl para garantizar la compatibilidad del teclado entre distintos sistemas operativos.

### Ratón {#mouse}

Puede ajustar las opciones del ratón para mejorar la experiencia en el dispositivo controlado.

![Ratón](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_mouse.png){class="glboxshadow"}

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

- **Primary Button**: Seleccione el botón izquierdo o derecho como botón principal. Esta función se incorporó en el firmware v1.9.0.

## Herramientas {#toolbox}

En la consola, vaya a **Toolbox**. La página de herramientas incluye cinco secciones:

- [Portapapeles](#clipboard)
- [OCR](#ocr)
- [Atajos](#shortcut)
- [Wake on LAN](#wake-on-lan)
- [Terminal](#terminal)

### Portapapeles {#clipboard}

El portapapeles permite pegar fácilmente texto del dispositivo de control en el dispositivo controlado sin tener que transferir archivos.

![Portapapeles de las herramientas](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_clipboard.png){class="glboxshadow"}

### OCR {#ocr}

OCR es una función de reconocimiento de texto que permite seleccionar un área de la pantalla remota y extraer su texto fácilmente. Esta función se incorporó en el firmware v1.9.0.

Para utilizarla, haga clic en la flecha hacia abajo y seleccione el idioma de reconocimiento que prefiera, como chino, inglés o bilingüe (Zh/En).

![Idioma de reconocimiento](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_ocr.png){class="glboxshadow"}

A continuación, haga clic en **Capture** y la pantalla remota se oscurecerá. Dibuje un recuadro alrededor del texto que desea extraer y el sistema lo reconocerá automáticamente. Después podrá copiar el texto reconocido según sea necesario.

![Copiar texto](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/ocr_copy_text.png){class="glboxshadow"}

Con esta función, puede capturar fácilmente texto de la pantalla remota (el dispositivo controlado) y copiarlo en el dispositivo de control local.

### Atajos {#shortcut}

Los atajos permiten realizar acciones con mayor rapidez sin utilizar el teclado virtual, lo que mejora la eficiencia y ahorra tiempo en las tareas cotidianas. Aquí encontrará algunos atajos habituales.

![Atajos de las herramientas 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_shorcut.png){class="glboxshadow"}

Haga clic en **Modify** para ajustar las opciones de los atajos según sea necesario.

![Atajos de las herramientas 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_shorcut_modify.png){class="glboxshadow"}  

### Wake-on-LAN {#wake-on-lan}

Wake-on-LAN (WOL) es una tecnología que permite encender el dispositivo controlado de forma remota o activarlo desde un estado de bajo consumo.

Haga clic en **Add Device** y elija un dispositivo de la misma LAN.

![Wake-on-LAN de las herramientas](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_wake_on_lan.png){class="glboxshadow"}

![Añadir dispositivo Wake-on-LAN](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/wol-add-device.png){class="glboxshadow"}

Si el dispositivo que desea añadir no aparece en la lista, haga clic en **Add Manually** e introduzca su nombre y dirección MAC.

![Añadir Wake-on-LAN manualmente](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/wol-add-manually.png){class="glboxshadow"}

### Terminal {#terminal}

Puede acceder al terminal de Comet Pro para realizar ajustes avanzados. Haga clic en **Access**.

![Terminal de las herramientas 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_terminal.png){class="glboxshadow"}

Se le redirigirá al terminal de GLKVM.

![Terminal de las herramientas 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox-terminal-2.png){class="glboxshadow"}

## Accesorios {#accessories}

GL.iNet ofrece accesorios KVM opcionales para encender y apagar el dispositivo de forma remota.

Primero, consulte la guía de usuario correspondiente para conectar el accesorio al dispositivo controlado.

- [Guía de usuario de Fingerbot (FGB-01)](../gl-fgb-01/index.md){target="_blank"}

- [Guía de usuario de la placa ATX (GL-ATXPC)](../gl-atx-board/index.md){target="_blank"}

Después, inicie sesión en la consola KVM y vaya a **Accessories**. Los ajustes del accesorio solo están disponibles una vez instalado.

### Fingerbot {#fingerbot}

Fingerbot se adhiere al botón físico de encendido del dispositivo controlado para controlar su alimentación de forma remota.

Funciona de acuerdo con los ajustes de la consola.

![Accesorio Fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/accessories-fgb.png){class="glboxshadow"}

- **Time**: Duración de la pulsación de Fingerbot. Puede establecerla en 0.5s/3s/8s.

- **Strength**: Hay dos niveles de fuerza de pulsación: Lightly Press y Firmly Press.

    - **Lightly Press**: Ideal para botones cortos o de pulsación suave.

    - **Firmly Press**: Ideal para botones profundos o duros.

    ![Modo de pulsación](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### Alimentación ATX {#atx-power}

La placa ATX se instala en la caja del ordenador para encender, apagar o reiniciar el dispositivo de forma remota.

Funciona de acuerdo con los ajustes de la consola.

![Alimentación ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/accessories-atx.png){class="glboxshadow"}

- **Power (Short Press)**: Se utiliza para el encendido normal o la activación del sistema.

- **Power (Long Press)**: Fuerza el apagado.

- **Restart**: Reinicie el dispositivo.

## Medios virtuales {#virtual-media}

En la consola, vaya a **Virtual Media**. Aquí puede realizar las siguientes operaciones:

- [Compartir archivos](#file-sharing)
- [Montar imágenes](#image-mounting)
- [Sustituir la unidad de almacenamiento](#replace-storage-drive)
- [Formatear el disco](#format-disk)

![Medios virtuales](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/virtual-media.png){class="glboxshadow"}

### Compartir archivos {#file-sharing}

Comet Pro emula una unidad USB de lectura y escritura para compartir y gestionar archivos entre el dispositivo de control y el dispositivo controlado.

**Para compartir archivos del dispositivo de control con el dispositivo controlado, siga estos pasos.**

1. Arrastre archivos al recuadro o haga clic en él para cargarlos desde el dispositivo de control; también puede cargarlos desde una URL.

    Una vez cargados, los archivos aparecerán como se muestra a continuación.

    ![Cargar archivos](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-uploaded.png){class="glboxshadow"}

2. Haga clic en **Mount To Remote** -> **File Sharing**.

    ![Compartir archivos](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount1.png){class="glboxshadow"}

3. Aparecerá una ventana en la consola con los pasos para compartir archivos, como se muestra a continuación.

    ![Indicaciones para compartir archivos](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount2-prompt.png){class="glboxshadow"}

4. Espere un momento y aparecerá automáticamente en la pantalla una unidad llamada **"GLKVM"**. Los archivos que cargó previamente del dispositivo de control a Comet Pro se habrán compartido con el dispositivo controlado. Ahora puede ver, mover o eliminar los archivos de esta unidad desde el dispositivo controlado.

    ![Unidad GLKVM para compartir archivos](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount3.png){class="glboxshadow"}

    **Consejo**: Si la unidad no aparece automáticamente, vaya a **This PC** en el dispositivo controlado.

    ![This PC](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-thispc.png){class="glboxshadow"}

    Busque una unidad llamada **GLKVM**. Ahora puede ver, mover o eliminar los archivos de esta unidad.

5. Para dejar de compartir, haga clic en **Virtual Media** en la barra de herramientas y, a continuación, en **Stop Sharing**.

    ![Dejar de compartir](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/stop-sharing1.png){class="glboxshadow"}

**Para compartir archivos del dispositivo controlado con el dispositivo de control, siga estos pasos.**

1. En el dispositivo controlado, mueva o copie los archivos que desea compartir a la unidad **GLKVM**.

    Por ejemplo, se ha movido una imagen llamada "slate7-pro_gl-be10000" del escritorio del dispositivo controlado a la unidad **GLKVM**.

    ![Mover el archivo a la unidad](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-copy.png){class="glboxshadow"}

2. Vuelva a la consola de Comet Pro, haga clic en **Virtual Media** en la barra de herramientas y, a continuación, en **Stop Sharing**.

    ![Dejar de compartir](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/stop-sharing2.png){class="glboxshadow"}

3. El archivo aparecerá en **Virtual Media**, como se muestra a continuación. Ahora puede descargarlo desde Comet Pro al dispositivo de control.

    ![Archivo compartido](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-shared.png){class="glboxshadow"}

### Montar imágenes {#image-mounting}

Comet Pro puede simular una unidad virtual de CD/DVD o de disco de solo lectura en el dispositivo controlado. Puede acceder a esta unidad durante el arranque de la BIOS o UEFI.

Esta función permite reinstalar el sistema operativo, montar una ISO para instalar aplicaciones en el dispositivo controlado o realizar otras tareas.

1. Arrastre archivos al recuadro o haga clic en él para cargarlos. **Asegúrese de que el archivo pueda montarse en formato ISO**.

    Una vez cargados, los archivos aparecerán como se muestra a continuación.

    ![Montar una imagen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount1.png){class="glboxshadow"}

2. Haga clic en **Mount To Remote** -> **Image Mounting**.

    ![Montar una imagen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount2.png){class="glboxshadow"}

3. En la ventana emergente, seleccione el archivo y haga clic en **Mount Image**.

    ![Montar una imagen 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount3.png){class="glboxshadow"}

4. Ahora puede utilizar el archivo desde la unidad de CD del dispositivo controlado.

    ![Montar una imagen 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount4.png){class="glboxshadow"}

### Sustituir la unidad de almacenamiento {#replace-storage-drive}

Puede insertar un dispositivo de almacenamiento USB en el puerto USB del KVM para sustituir el almacenamiento interno.

![Sustituir la unidad de almacenamiento](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/replace-storage.png){class="glboxshadow"}

### Formatear el disco {#format-disk}

Puede formatear el disco o desactivar los medios virtuales con un clic.

![Formatear el disco](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/format-storage.png){class="glboxshadow"}

- **Format**: Borre todos los datos del disco y reinicialice la estructura de su sistema de archivos.

- **Disable**: Al desactivar los medios virtuales, el dispositivo KVM se reiniciará inmediatamente.

## Centro de aplicaciones {#apps-center}

En la consola, vaya a **Apps Center**. Aquí encontrará las aplicaciones integradas.

![Centro de aplicaciones](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} es un servicio VPN de malla basado en WireGuard que crea redes privadas cifradas entre dispositivos sin necesidad de redireccionar puertos ni configurar complejas reglas de cortafuegos.

Comet Pro integra Tailscale, lo que permite acceder a él de forma remota a través de la red virtual de Tailscale.

Solo tiene que vincular Comet Pro y el dispositivo de control a la misma cuenta de Tailscale. Después podrá acceder a Comet Pro de forma remota introduciendo su **IP virtual de Tailscale** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM. Consulte los detalles [aquí](../../faq/remote_access_via_tailscale.md){target="_blank"}.

Después de la vinculación, la consola muestra la cuenta de Tailscale vinculada y habilita funciones avanzadas como Exit Node y Subnet Routes.

![Tailscale activado](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} crea redes virtuales superpuestas cifradas para conectar dispositivos distribuidos por todo el mundo como si estuvieran en la misma red local.

Comet Pro integra ZeroTier, lo que permite acceder a él de forma remota a través de la red virtual de ZeroTier.

Solo tiene que unir Comet Pro y el dispositivo de control a la misma red de ZeroTier. Después podrá acceder a Comet Pro de forma remota introduciendo su **IP de ZeroTier** en un navegador web del dispositivo de control, sin instalar la aplicación GLKVM. Consulte los detalles [aquí](../../faq/remote_access_via_zerotier.md){target="_blank"}.

Después de la vinculación, la consola muestra el Network ID y la IP virtual de ZeroTier.

![ZeroTier activado](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/zerotier-enabled.png){class="glboxshadow"}

### NetBird {#netbird}

[NetBird](https://netbird.io/){target="_blank"} es una plataforma de redes de confianza cero de código abierto que permite crear redes privadas seguras para uso doméstico y empresarial. Como red superpuesta basada en WireGuard®, NetBird permite acceder de forma segura a sus dispositivos en cualquier momento y lugar.

Comet Pro integra NetBird, lo que permite acceder a él de forma remota a través de la red virtual de NetBird. Consulte los detalles [aquí](../../faq/remote_access_via_netbird.md){target="_blank"}.

Después de la vinculación, la consola muestra la IP virtual de NetBird.

![NetBird activado](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/netbird-enabled.png){class="glboxshadow"}

## Ayuda {#help}

En la consola, vaya a **Help**. Aquí encontrará más información sobre GL.iNet KVM y documentación de ayuda; también podrá exportar registros para solucionar problemas.

![Ayuda](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/help.png){class="glboxshadow"}

## Barra de herramientas {#toolbar}

En la consola, vaya a la esquina superior derecha para acceder a las siguientes herramientas:

- [Contraer la barra de herramientas](#collapse)
- [Pantalla completa](#fullscreen)
- [Actualizar](#upgrade)
- [Estadísticas de conexión](#connection-stats)
- [Servicio en la nube](#cloud-service)
- [Cerrar sesión](#logout)

### Contraer {#collapse}

Haga clic en el icono de flecha hacia arriba de la esquina superior derecha para contraer la barra de herramientas.

![Contraer](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/collapse_1.png){class="glboxshadow"}

Cuando la barra esté contraída, haga clic en el icono de flecha hacia abajo de la parte superior para expandirla.

![Contraer](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/collapse_2.png){class="glboxshadow"}

### Pantalla completa {#fullscreen}

Haga clic en el icono de pantalla completa (con forma de cuadrado) de la esquina superior derecha para activar el modo de pantalla completa.

![Pantalla completa](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/fullscreen_1.png){class="glboxshadow"}

Para salir de la pantalla completa, mantenga pulsada la tecla **Esc** o haga clic en el icono para salir de la pantalla completa (con forma de cuadrícula) de la esquina superior derecha.

![Pantalla completa](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/fullscreen_2.png){class="glboxshadow"}

### Actualizar {#upgrade}

Haga clic en la versión del firmware de la esquina superior derecha para buscar actualizaciones.

![Actualizar el firmware 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade_1.png){class="glboxshadow"}

En la ventana emergente, puede hacer clic en **Local Upgrade** para cargar un archivo de firmware.

![Actualizar el firmware 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade_2.png){class="glboxshadow"}

![Actualizar el firmware 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade_3.png){class="glboxshadow" width=350}

Descargue el firmware más reciente del [centro de descarga de firmware](https://dl.gl-inet.com/kvm){target="_blank"} antes de realizar una actualización local.

### Estadísticas de conexión {#connection-stats}

Connection Stats incluye un panel de datos que supervisa la latencia, la variación de latencia y otras métricas en tiempo real.

Haga clic en el icono de lista para mostrar el estado del dispositivo y los datos en tiempo real.

![Panel de datos 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/data_dashboard_1.png){class="glboxshadow"}

Haga clic en el icono de gráfico para ver las estadísticas, como la latencia de red, la variación de latencia, la tasa de pérdida de paquetes, la tasa de fotogramas en tiempo real y el retraso de reproducción.

![Panel de datos 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/data_dashboard_2.png){class="glboxshadow"}

### Servicio en la nube {#cloud-service}

GL.iNet KVM Cloud permite acceder al dispositivo controlado de forma remota. Consulte los detalles [aquí](../../faq/remote_access_via_cloud.md){target="_blank"}.

Una vez que Comet Pro esté vinculado a la nube, la consola mostrará el estado de la nube como se indica a continuación.

![Servicio en la nube](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/cloud.png){class="glboxshadow"}

### Cerrar sesión {#logout}

Para cerrar sesión, haga clic en el icono Logout.
![Cerrar sesión](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/logout.png){class="glboxshadow"}

## Ajustes {#settings}
En la consola, haga clic en el icono Settings de la barra de navegación para abrir la siguiente página de ajustes. Esta función se incorporó en el firmware v1.10.0.

- [Dispositivos USB](#usb-devices)
- [Preferencias](#preferences)
- [Red](#network)
- [Seguridad](#security)
- [Nube](#cloud)
- [Sistema](#system)

![Ajustes](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting.png){class="glboxshadow"}

### Dispositivos USB {#usb-devices}

USB Device permite gestionar de forma centralizada todos los dispositivos USB emulados. Desde esta página, puede activar o desactivar los periféricos virtuales para mejorar la compatibilidad con el equipo controlado.

![Dispositivos USB emulados](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_usb_devices.png){class="glboxshadow"}

- **Microphone**

    Cuando el micrófono esté silenciado, puede hacer clic en Settings para personalizar los atajos según sus preferencias. Mantenga pulsado el atajo asignado para empezar a hablar; al soltarlo, el micrófono se silenciará de nuevo.

    ![Ajustes del micrófono 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mic_setting_1.png){class="glboxshadow" width=600}

    ![Ajustes del micrófono 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mic_setting_2.png){class="glboxshadow" width=434}

  - **Device Identity**

    Personalice o modifique la identidad con la que el dispositivo controlado reconoce al KVM. Tenga en cuenta que el EDID y la identificación del dispositivo permanecen sincronizados. Al cambiar uno de ellos, el otro se actualiza automáticamente para garantizar el reconocimiento correcto del dispositivo.

    ![Identidad del dispositivo](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/device_identification.png){class="glboxshadow" width=350}

### Preferencias {#preferences}

Preferences permite gestionar los ajustes de Layout Preferences, System Settings y Device Screen.

![Preferencias](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_preference.png){class="glboxshadow"}

- **Layout Preferences**: Puede configurar la visualización de la barra de herramientas en pantalla completa y de la barra de estado en modo de ventana según sea necesario.

- **System Settings**: Para personalizar los ajustes del sistema, seleccione Tab Title (título de la pestaña del navegador), Language (chino, inglés o japonés), Color Mode (Light o Dark) y Timezone según su región.

- **Device Screen**: Puede gestionar y previsualizar la pantalla del dispositivo. Los ajustes disponibles incluyen el modo Lock Screen (World Clock, Clock Only o Wallpaper Only), Time Format, Date Format y Wallpaper.

### Red {#network}

Puede consultar y modificar los datos de red de Comet Pro, como el nombre de host y la dirección IP.

![Red](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network.png){class="glboxshadow"}

- **Hostname**: Puede modificar el nombre de host del dispositivo directamente en la consola. Esta función se incorporó en el firmware v1.7.0.

    ![Modificar el nombre de host](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_hostname.png){class="glboxshadow" width=600}

- **Ethernet Settings**: Cuando Comet Pro se conecte a un dispositivo de red superior mediante un cable Ethernet, sus datos de Ethernet aparecerán aquí.

    Si el protocolo es DHCP, la página se mostrará como se indica a continuación.

    ![Ethernet con DHCP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_dhcp.png){class="glboxshadow" width=600}

    Para establecer una dirección IP estática, cambie el protocolo a **Static** e introduzca los parámetros de red necesarios, como la dirección IP, la máscara de red y la puerta de enlace.

    ![Ethernet con IP estática](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_static.png){class="glboxshadow" width=600}

- **Wireless**: Cuando Comet Pro se conecte a una red Wi-Fi, su dirección IP, puerta de enlace y dirección MAC aparecerán aquí.

    ![Configuración de Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_wifi.png){class="glboxshadow" width=600}

    Para conectarlo a otra red Wi-Fi, haga clic en **Switch Wi-Fi** y seleccione una red de la lista de redes disponibles.

    ![Conectarse a Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_switch_network.png){class="glboxshadow" width=500}

### Seguridad {#security}

Security permite cambiar la contraseña de administrador, activar la autenticación de dos factores y personalizar el certificado TLS.

![Seguridad](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_security.png){class="glboxshadow"}

- Change Admin Password

    ![Cambiar la contraseña de administrador](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/change-password.png){class="glboxshadow" width="434"}

- 2FA: Active la autenticación de dos factores para proteger su cuenta.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/2fa.png){class="glboxshadow"}

- TLS Certificate

    El sistema utiliza el certificado predeterminado preinstalado para el acceso desde el navegador. Para personalizar el certificado TLS utilizado en ese acceso, haga clic en **Custom**, en TLS Certificate, y cargue su **archivo de certificado y su archivo de clave privada**.

    ![Certificado TLS personalizado](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_security_custom.png){class="glboxshadow"}

### Nube {#cloud}

Cloud permite acceder a su dispositivo y gestionarlo de forma remota a través de servicios en la nube.

Puede vincular el dispositivo a la nube mediante una URL. En **More Settings**, encontrará otras opciones como Bind With Code y App Download. También puede utilizar Disable si es necesario.

![Nube 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_cloud_1.png){class="glboxshadow"}

Una vez vinculado correctamente, podrá consultar la información de la cuenta en la nube vinculada. Haga clic en **Access Cloud** para gestionar los dispositivos o en **More Settings** para desactivar el servicio o desvincular el dispositivo según sea necesario.

![Nube 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_cloud_2.png){class="glboxshadow"}

También puede realizar estas operaciones de gestión mediante Cloud Service en la barra de herramientas superior.

### Sistema {#system}

En los ajustes de System, puede configurar lo siguiente:

![Sistema](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_system.png){class="glboxshadow"}

- **System**: Haga clic en **Reboot** para reiniciar el dispositivo o en **Reset** para borrar su configuración actual y volver a configurarlo.

- **Upgrade**: Puede activar Beta Center para recibir actualizaciones de firmware beta o utilizar Local Upgrade para instalarlas manualmente desde un archivo local.

    ![Actualización local](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setthing_system_local_update.png){class="glboxshadow" width=400}

- **Help & Support**: Export Log Files permite guardar los registros de funcionamiento del dispositivo para solucionar problemas y recibir asistencia posventa. Help Document proporciona acceso a guías de usuario, preguntas frecuentes y documentación de solución de problemas.
