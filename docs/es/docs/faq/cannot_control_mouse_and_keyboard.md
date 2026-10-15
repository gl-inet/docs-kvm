# Qué hacer si no puede controlar el ratón y el teclado {#what-should-i-do-if-i-cannot-control-the-mouse-and-keyboard}

Si no puede controlar el ratón y el teclado del dispositivo controlado mediante el KVM, aunque todos los cables estén conectados correctamente, pruebe las siguientes soluciones.

1. Compruebe el cableado.

    Por ejemplo, Comet (GL-RM1) tiene dos puertos USB Type-C:

    - El puerto lateral, con la etiqueta "5V 2A", es la entrada de alimentación y se conecta a un adaptador de corriente.
    - El puerto trasero, con los iconos de un ratón y un teclado, se conecta al puerto USB del dispositivo controlado para recibir las señales del teclado y el ratón.

    Si intercambia estas conexiones, el dispositivo KVM no arrancará y el ratón y el teclado no responderán.

    Compruebe que ambos puertos Type-C estén conectados correctamente.

    ![Puertos del GL-RM1](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/gl-rm1-ports.png){class="glboxshadow gl-80-desktop"}

2. Compruebe el cable USB.

    Utilice el cable USB incluido. Asegúrese de que conecte el puerto USB del dispositivo controlado con el del KVM y admita la transmisión de datos.

    Solo los cables que permiten transferir datos sirven para controlar el teclado y el ratón del dispositivo remoto.

    Vuelva a conectar el cable USB y reinicie el dispositivo controlado.

3. Cambie el modo de ratón a Relative.

    Inicie sesión en el KVM, vaya a Settings -> Mouse Mode, seleccione Relative y compruebe si se resuelve el problema.

    ![Modo de ratón](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/mouse_mode.jpg){class="glboxshadow"}

4. Desactive los medios virtuales.

    Inicie sesión en el KVM, vaya a Virtual Media, haga clic en el icono de tres puntos y desactive la función.

    ![Desactivar los medios virtuales](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/disable_virtual_media.png){class="glboxshadow" width="422"}

    Cuando los medios virtuales están activados, el KVM puede simular una unidad de almacenamiento USB conectada al dispositivo controlado. Sin embargo, algunos dispositivos desactivan todas las entradas USB al detectar una unidad USB desconocida, por lo que el ratón y el teclado dejan de responder.

5. Cambie la identidad del dispositivo.

    Inicie sesión en el KVM, vaya a Settings -> System -> Device Identity y cambie la identidad con la que el dispositivo controlado reconoce al KVM.

    ![Cambiar la identidad del dispositivo](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/change_device_identity.png){class="glboxshadow"}

6. Actualice el firmware del KVM a la versión más reciente. [Centro de descargas de firmware KVM](https://dl.gl-inet.com/kvm){target="_blank"}

7. Compruebe en Device Manager del equipo controlado si hay controladores que funcionen incorrectamente.

8. Compruebe si el software de seguridad informática bloquea el dispositivo controlado.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
