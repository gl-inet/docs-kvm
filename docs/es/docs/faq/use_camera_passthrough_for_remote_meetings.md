# ¿Cómo puedo compartir la cámara local en reuniones remotas? (Camera Passthrough) {#how-can-i-share-the-local-camera-with-remote-meetings-camera-passthrough}

**Nota**: Esta función se incorporó en el firmware v1.10.0 y solo se admite en el modo WebRTC (FEC). Actualmente está disponible a través de navegadores web y del cliente de escritorio, pero todavía no se admite en la aplicación móvil.

---

Cuando trabaja desde casa, puede usar KVM para acceder a su ordenador de la oficina y unirse allí a una videoconferencia en Zoom, Microsoft Teams o una aplicación similar. Sin embargo, es posible que la cámara solo muestre su oficina y no a usted.

La función **Camera** de GL.iNet KVM permite transmitir el vídeo de la cámara de su ordenador de casa al ordenador de la oficina como una cámara USB virtual. Seleccione esta cámara en la aplicación de reuniones para que los demás participantes puedan verle mientras comparte archivos o aplicaciones del ordenador de la oficina.

## Configuración rápida {#quick-setup}

Siga los pasos siguientes para usar la función Camera, tomando como ejemplo una videoconferencia de Zoom.

1. Antes de unirse a la reunión, inicie sesión en su KVM desde el ordenador de control y vaya a **Session** -> **Audio & Camera**. Active Camera y haga clic en el icono de la cámara para comenzar.

    ![enable camera 1](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera.png){class="glboxshadow"}

    Si aparece un mensaje sobre el límite de recursos USB al activar Camera, vaya a **Settings** -> **USB Devices** y desactive los dispositivos USB emulados que no utilice para liberar recursos. Después, active Camera e inténtelo de nuevo.

    ![enable camera 3](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-3.png){class="glboxshadow"}

    Es posible que el navegador solicite acceso a la cámara. Seleccione la cámara que desea usar, compruebe la vista previa del vídeo y permita el acceso.

    ![enable camera 2](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-2.png){class="glboxshadow"}

2. Abra Zoom y únase a una reunión en el ordenador controlado. Haga clic en la flecha junto al botón de vídeo y seleccione **UVC camera**.

    ![uvc-camera](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/uvc-camera.png){class="glboxshadow"}

    Después, active el vídeo para que los demás participantes puedan ver la imagen de la cámara del dispositivo de control.

    **Nota**: Asegúrese de contar con una conexión de red estable para obtener un vídeo fluido y nítido durante la reunión.

## Solución de problemas {#troubleshooting}

??? note "¿Qué debo hacer si la imagen de la cámara no llega al ordenador controlado?"

    Compruebe si el ordenador controlado reconoce la cámara virtual del KVM.

    En el ordenador controlado, vaya a **Settings** -> **Bluetooth & devices** -> **Cameras** y busque UVC Camera en Connected cameras.

    ![check camera settings](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/check-camera-settings.png){class="glboxshadow"}

    Si no aparece, es posible que la conexión de datos USB entre el KVM y el ordenador controlado esté desconectada o suelta.

??? note "¿Qué debo hacer si aparece el mensaje 'Camera Access Denied' al activar Camera en la consola KVM?"

    ![camera access denied](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/camera-access-denied.png){class="glboxshadow"}

    Compruebe lo siguiente en el ordenador de control:

    - **Disponibilidad de la cámara**: Asegúrese de que la cámara esté conectada y funcione. Pruébela con la aplicación de cámara del sistema y cierre esa aplicación antes de volver a intentarlo.

    - **Permisos del sistema**: En Windows 11, vaya a Settings -> Privacy & security -> Camera y active las siguientes opciones: Camera access, Let apps access your camera y Let desktop apps access your camera.

    - **Permisos del navegador**: Permita que el sitio web del KVM acceda a la cámara. Si el acceso se bloqueó anteriormente, actualice los permisos de cámara del sitio web y recargue la página.

    - **Uso de la cámara**: Cierre otras aplicaciones o pestañas del navegador que puedan estar usando la cámara, como Zoom o Microsoft Teams.

    Tras realizar estas comprobaciones, vuelva a activar Camera en la consola KVM.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
