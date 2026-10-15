# Preguntas frecuentes sobre Comet Q {#frequently-asked-questions-about-comet-q}

## General {#general}

1. **P: ¿Qué debo hacer si la pantalla de control KVM muestra "Unable to Display" al conectar Comet Q al dispositivo controlado?**

    R: Esto se debe a que el dispositivo controlado no admite **USB-C DisplayPort Alt Mode**, lo que impide la salida de vídeo.

    Consulte [aquí](../../tutorials/how_to_check_usb-c_port_dp_alt_mode.md) cómo comprobar si su dispositivo admite DisplayPort Alt Mode.

2. **P: ¿Por qué el dispositivo de control no muestra el teclado para introducir la contraseña cuando la pantalla del dispositivo controlado está bloqueada?**

    R: Debido a las restricciones de seguridad de iOS/Android, el sistema bloquea la página de introducción de contraseña durante la duplicación de pantalla o el control remoto. Puede introducir directamente la contraseña de desbloqueo desde el dispositivo de control para desbloquear el dispositivo.

3. **P: ¿Por qué no se transmite el sonido al dispositivo de control cuando el dispositivo controlado está realizando una llamada de voz?**

    R: Este problema es habitual en iPhones y algunos dispositivos Android. Cuando se utilizan aplicaciones de comunicación por voz, como WhatsApp o Microsoft Teams, para realizar llamadas en el dispositivo controlado, las restricciones de iOS/Android solo permiten emitir el audio por los altavoces locales del dispositivo controlado e impiden transmitirlo al dispositivo de control mediante KVM.

    **Consejo**: El audio multimedia, como vídeos, música o juegos, puede transmitirse normalmente al dispositivo de control mediante KVM cuando las aplicaciones de comunicación por voz están inactivas.

## iOS {#ios}

1. **P: ¿Por qué no puedo ajustar el volumen del sistema en los dispositivos iOS después de conectarlos a Comet Q?**

    R: Debido a las restricciones de iOS, cuando un iPhone/iPad se conecta a un dispositivo de duplicación de pantalla, como GL.iNet KVM, que se establece como salida de audio, el control de volumen nativo del sistema deja de estar disponible.

2. **P: ¿Por qué el dispositivo iOS no muestra el vídeo localmente al reproducirlo desde aplicaciones de vídeo?**

    R: Cuando un dispositivo iOS se conecta a un dispositivo de duplicación de pantalla, como GL.iNet KVM, algunas aplicaciones de vídeo, como YouTube o Netflix, utilizan **AirPlay** como salida de vídeo de forma predeterminada, por lo que el dispositivo iOS no muestra el vídeo localmente. Este comportamiento no puede desactivarse en el sistema.

    Para que el dispositivo controlado reproduzca vídeos localmente mientras se duplica su pantalla, reproduzca los vídeos desde un navegador web.

3. **P: ¿Qué debo hacer si el teclado en pantalla del dispositivo iOS desaparece después de conectarlo a Comet Q?**

    R: Es probable que iOS reconozca Comet Q como un teclado físico externo y oculte automáticamente el teclado nativo en pantalla. En ese caso, utilice el teclado del dispositivo de control o el teclado virtual integrado en la consola KVM.

    Si necesita utilizar el teclado en pantalla de iOS, vaya a **Settings** > **Accessibility** > **Touch** > **AssistiveTouch** y active **Show Onscreen Keyboard**.

    ![AssistiveTouch](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/assistive_touch.png){class="glboxshadow" width="360"}

4. **P: Al duplicar la pantalla de un iPhone/iPad en orientación vertical u horizontal, el ratón del dispositivo de control sigue desalineado incluso después de ajustar la orientación en la consola KVM. ¿Qué debo hacer?**

    R: El seguimiento preciso del cursor en un iPhone o iPad requiere que la orientación del giroscopio del dispositivo coincida exactamente con la orientación de la pantalla mostrada. Durante el control remoto, puede que el sistema no detecte correctamente el estado actual del giroscopio, lo que provoca un desplazamiento del cursor.

    Para resolverlo, active **Portrait Orientation Lock**/**Rotation Lock** en el iPhone/iPad para garantizar un seguimiento preciso del cursor.

    ![Bloqueo de orientación vertical](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/portrait_lock.png){class="glboxshadow" width="360"}  
    <small>(Portrait Orientation Lock en iPhone)</small>

5. **P: ¿Por qué el teclado no funciona correctamente en los dispositivos iOS, con algunas teclas que no responden o el cursor del ratón que se desplaza?**

    R: Este problema suele deberse a que la función **Mouse Keys** está activada en el dispositivo iOS. Mouse Keys permite mover el cursor del ratón mediante un teclado o teclado numérico.

    Para resolverlo, vaya a **Settings** -> **Accessibility** -> **AssistiveTouch** -> **Mouse Keys** y desactive Mouse Keys.

## Android {#android}

1. **P: ¿Por qué no puedo controlar el dispositivo en el modo de ratón absoluto?**

    R: Debido a las restricciones del sistema operativo Android, los dispositivos Android solo pueden controlarse en el modo de ratón relativo.

    Al controlar el dispositivo desde la aplicación móvil GLKVM, cubra completamente el cursor del ratón con el dedo para realizar las operaciones.

2. **P: ¿Qué debo hacer si la pantalla que se muestra en el dispositivo de control no está sincronizada con la del teléfono Android controlado?**

    R: Algunos teléfonos Android reconocen Comet Q como una pantalla extendida en lugar de una pantalla duplicada. Para resolverlo, cambie el ajuste de pantalla del teléfono al modo **Screen Mirroring**.

    Por ejemplo, en la serie Samsung S:

    Vaya a **Settings** > **Device Connections** > **Samsung DeX** > **Connected Display** y seleccione el modo **Screen Mirroring**.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
