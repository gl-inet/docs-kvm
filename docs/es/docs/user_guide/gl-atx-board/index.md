# Guía del usuario de la placa ATX (GL-ATXPC) {#atx-board-gl-atxpc-user-guide}

La placa ATX es un accesorio opcional para los dispositivos KVM de GL.iNet. Este módulo de gestión inteligente de la alimentación permite controlar de forma remota la alimentación del dispositivo controlado simulando las acciones del botón físico de encendido: encender, apagar y reiniciar.

La placa ATX se instala dentro del chasis del dispositivo controlado, lo que permite gestionar su alimentación de forma más discreta y estable.

**Nota**: Comet Q (GL-RMQ1) no es compatible con la placa ATX.

![Comet GL-RM1 y placa ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/rm1-and-atx-borad.jpg){class="glboxshadow"}

## Contenido de la caja {#package-contents}

![Contenido de la caja](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/inside-the-box.png){class="glboxshadow gl-80-desktop"}

- 1 x Placa ATX principal
- 1 x Juego de cables de 9 pines
- 1 x Juego de tornillos
- 1 x Cable USB-A a Type-C
- 1 x Juego de soportes para la placa ATX

## Distribución de pines {#pin-out}

![Distribución de pines](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/pinout.jpg){class="glboxshadow gl-80-desktop"}

Descripción de las interfaces:

1. Interfaz Type-C: se conecta al dispositivo KVM.
2. Botón de actualización del firmware: actualiza el microcontrolador de la placa ATX principal.
3. Botón de reinicio.
4. Conexión al cableado de control del panel del ordenador.
5. Conexión a la interfaz F_PANEL del ordenador.

!!! note "Nota"

    1. Las interfaces 4 y 5 son intercambiables. Es decir, la interfaz 5 puede conectarse al cableado de control del panel del ordenador y la interfaz 4 a F_PANEL.

    2. La placa ATX tiene dos LED que se comportan como indicadores de alimentación: el azul indica el estado del sistema ATX y el verde, la alimentación del PC. La placa ATX no tiene un LED de actividad del disco duro. El estado de los LED de la placa coincide con el estado del LED de alimentación del panel del ordenador.

Diagrama de las interfaces 4/5:

![Interfaz](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface.png){class="glboxshadow gl-60-desktop"}

## Instalación {#installation}

Vea este vídeo para instalar la placa ATX o siga los pasos que se indican a continuación.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3VEjZgzgI44" title="Reproductor de vídeo de YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Atornille la placa ATX al soporte {#1-screw-atx-board-and-bracket}

Fije la placa ATX al juego de soportes con los tornillos suministrados.

![Fijación con tornillos](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/screwing.jpg){class="glboxshadow gl-90-desktop"}

### 2. Instale la placa ATX en la caja del PC {#2-install-atx-board-into-pc-case}

Conecte las interfaces 4 y 5, respectivamente, al cableado de control y a la interfaz F_PANEL del PC controlado.

![Conexión de las interfaces](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface_connect.jpg){class="glboxshadow gl-90-desktop"}

El juego de cables de 9 pines incluido con la placa ATX permite conectar una de las interfaces 4/5 de la placa al cableado de control o a la interfaz F_PANEL del ordenador controlado.

Utilice el juego de cables de la caja de su ordenador para conectar la otra interfaz 4/5 de la placa ATX al cableado de control o a la interfaz F_PANEL del ordenador controlado.

**Nota**: La polaridad de la interfaz puede variar según la caja del PC. Compruébela cuidadosamente antes de la instalación.

A continuación se muestran algunos ejemplos de conexión de la interfaz 4/5 a la interfaz F_PANEL del ordenador controlado.

??? "Para un PANEL de 10-1 pines"

    Si la fila de pines de la placa base del ordenador controlado que se conecta al panel de control es un PANEL de 10-1 pines, como se muestra a continuación:

    ![10-1 pines: panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_1.png){class="glboxshadow"}

    Consulte el siguiente diagrama para realizar la conexión. Asegúrese de que las inscripciones serigrafiadas (HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) queden visibles hacia fuera y no ocultas hacia dentro.

    ![10-1 pines: panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_2.jpg){class="glboxshadow"}
    <small>Vista frontal</small>

    ![10-1 pines: panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_3.jpg){class="glboxshadow"}
    <small>Vista posterior</small>

    A continuación, utilice el juego de cables de la caja del ordenador para conectar la otra interfaz de la placa ATX al cableado de control del ordenador.

??? "Para un PANEL de 20-5 pines"

    Si la fila de pines de la placa base del ordenador controlado que se conecta al panel de control es un PANEL de 20-5 pines, como se muestra a continuación:

    ![20-5 pines: panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_1.jpg){class="glboxshadow"}

    Consulte el siguiente diagrama para realizar la conexión. Asegúrese de que las inscripciones serigrafiadas (HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) queden visibles hacia fuera y no ocultas hacia dentro.

    ![20-5 pines: panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_2.jpg){class="glboxshadow"}
    <small>Vista frontal</small>

    ![20-5 pines: panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_3.png){class="glboxshadow"}
    <small>Vista posterior</small>

    A continuación, utilice el juego de cables de la caja del ordenador para conectar la otra interfaz de la placa ATX al cableado de control del ordenador.

??? "Para un PANEL de 20-8 pines"

    Si la fila de pines de la placa base del ordenador controlado que se conecta al panel de control es un PANEL de 20-8 pines, como se muestra a continuación:

    ![20-8 pines: panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_1.jpg){class="glboxshadow"}

    Consulte el siguiente diagrama para realizar la conexión. Asegúrese de que las inscripciones serigrafiadas (HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) queden visibles hacia fuera y no ocultas hacia dentro.

    ![20-8 pines: panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_2.png){class="glboxshadow"}

    A continuación, utilice el juego de cables de la caja del ordenador para conectar la otra interfaz de la placa ATX al cableado de control del ordenador.

La placa ATX con todas las conexiones realizadas se muestra a continuación.

![Placa ATX conectada](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected1.png){class="glboxshadow gl-90-desktop"}

![Placa ATX conectada](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected2.png){class="glboxshadow gl-90-desktop"}

A continuación, instale el soporte de la placa ATX en la caja del ordenador.

![Instalación de la placa ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install1.png){class="glboxshadow gl-90-desktop"}

![Instalación de la placa ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install2.png){class="glboxshadow gl-90-desktop"}

### 3. Conecte la placa ATX al KVM {#3-connect-atx-board-and-kvm}

Conecte el puerto Type-C de la placa ATX al puerto USB-A del dispositivo KVM (por ejemplo, Comet GL-RM1) con el cable USB incluido.

![Instalación de la placa ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install3.png){class="glboxshadow gl-90-desktop"}

![Instalación de la placa ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install4.png){class="glboxshadow gl-90-desktop"}

La instalación de la placa ATX ha finalizado.

![Instalación de la placa ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install5.png){class="glboxshadow gl-90-desktop"}

Ahora puede iniciar sesión en su KVM y acceder a **Accessories** para controlar la alimentación mediante la placa ATX.

![Control de alimentación ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/atx_power.png){class="glboxshadow gl-90-desktop"}

## Preguntas frecuentes {#faq}

**P1. ¿Puedo utilizar la placa GL-ATXPC con dispositivos KVM de otras marcas?**

R1. No. La placa GL-ATXPC es un accesorio para los dispositivos KVM de GL.iNet y debe utilizarse con uno de ellos.

---

**P2. Después de instalar la placa ATX, ¿qué debo hacer si no puedo encender o apagar el dispositivo remoto mediante el KVM?**

R2. Pruebe lo siguiente.

- Asegúrese de que el dispositivo controlado se enciende y se apaga con normalidad al pulsar el botón físico de encendido del panel frontal de la caja del PC.

- Compruebe la polaridad del cableado. Pruebe a invertir la orientación del conector POWER SW en la placa base del dispositivo controlado para corregir una posible conexión incorrecta.

    ![Polaridad del conector](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/power-sw-connector.png){class="glboxshadow gl-90-desktop"}

- Al conectar los cables a la interfaz F_PANEL de la placa base del dispositivo controlado, asegúrese de que las inscripciones serigrafiadas (HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) queden visibles hacia fuera y no ocultas hacia dentro.

- Actualice el firmware del KVM.

---

**P3. ¿Puedo utilizar un solo KVM de GL.iNet para controlar varias placas ATX?**

R3. Los siguientes KVM de GL.iNet solo pueden controlar una placa ATX.

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)

Comet X (GL-RM4PE) admite hasta cuatro placas ATX simultáneamente. Comet X dispone de cuatro canales independientes en el panel posterior. Cada canal incluye un puerto HDMI para transmitir la señal de vídeo, un puerto Type-C para transmitir las señales del teclado y el ratón y un puerto USB 2.0 para periféricos USB, como Fingerbot o una placa ATX.

**Nota**: Comet Q (GL-RMQ1) no es compatible con la placa ATX.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contacte con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
