# ¿Cómo puedo usar el audio bidireccional en reuniones remotas? {#how-can-i-use-two-way-audio-for-remote-meetings}

Si trabaja desde casa, puede usar el KVM para acceder al ordenador de la oficina y participar en reuniones de audio mediante Zoom, Microsoft Teams o una aplicación similar. La función de audio bidireccional del KVM de GL.iNet le permite hablar por el micrófono de su ordenador local y escuchar a los demás participantes por sus altavoces o auriculares.

## Configuración rápida {#quick-setup}

Siga estos pasos para usar el micrófono y el altavoz del dispositivo local en reuniones remotas. Se utiliza una reunión de Zoom como ejemplo.

1. Antes de unirse a una reunión, inicie sesión en el KVM desde el ordenador de control y vaya a **Session** -> **Audio & Camera**. Active **Speaker** y **Microphone**. Compruebe que los dos iconos de la esquina inferior derecha estén activos.

    ![Activar el altavoz y el micrófono](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/enable-speaker-and-microphone.png){class="glboxshadow"}

    Por ejemplo, al activar **Microphone**, es posible que el navegador solicite acceso al micrófono. Seleccione el micrófono que quiera usar y permita el acceso.

    ![Solicitud de acceso al micrófono](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/microphone-permission-popup.png){class="glboxshadow"}

2. Abra Zoom y únase a la reunión desde el ordenador controlado. Haga clic en la flecha junto al botón de audio y seleccione los siguientes dispositivos, como se muestra en el ejemplo:

    - **Microphone**: Microphone (6-Comet Microphone)

    - **Speaker**: EPSON PJ (HD Audio Driver for Display Audio)

    ![Seleccionar el micrófono y el altavoz](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/select-microphone-and-speaker.png){class="glboxshadow"}

    A continuación, desactive el silencio del micrófono para hablar con los demás participantes. Podrá oírlos por los altavoces o auriculares del ordenador de control.

    Si también quiere compartir la imagen de su cámara local con los participantes, consulte la [guía para usar la cámara local](../faq/use_camera_passthrough_for_remote_meetings.md).

## Solución de problemas {#troubleshooting}

??? note "¿Qué hago si los demás participantes no me oyen?"

    En el ordenador controlado, vaya a **Settings** -> **System** -> **Sound** y busque el micrófono virtual del KVM en **Input**. En el ejemplo aparece como **Comet Microphone**. Compruebe que ese micrófono también esté seleccionado en la aplicación de reuniones.

    ![Comprobar la entrada](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-input.png){class="glboxshadow"}

    - Si el micrófono virtual del KVM no aparece, compruebe la conexión de datos USB entre el KVM y el ordenador controlado. Esta conexión transmite el audio del micrófono al ordenador controlado.

    - Si el micrófono virtual del KVM aparece y está seleccionado, pero no recibe audio, compruebe que el micrófono no esté silenciado en el ordenador de control ni en la aplicación de reuniones del ordenador controlado. Revise los permisos del micrófono en el sistema y el navegador del ordenador de control, y cierre las demás aplicaciones o pestañas del navegador que puedan estar usando el micrófono.

??? note "¿Qué hago si no oigo a los demás participantes?"

    En el ordenador controlado, vaya a **Settings** -> **System** -> **Sound** y busque en **Output** la salida de audio HDMI conectada al KVM. En el ejemplo aparece como **EPSON PJ**. Compruebe que ese mismo dispositivo esté seleccionado como altavoz en la aplicación de reuniones.

    ![Comprobar la salida](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-output.png){class="glboxshadow"}

    - Si la salida de audio HDMI no aparece, compruebe la conexión HDMI entre el ordenador controlado y el KVM. Esta conexión transmite el audio del ordenador controlado. Si utiliza un adaptador HDMI, compruebe que sea compatible con audio.

    - Si la salida de audio HDMI aparece y está seleccionada, pero sigue sin oír a los demás participantes, compruebe que el ordenador de control, la pestaña del navegador y los altavoces o auriculares no estén silenciados.

    Para más información, consulte [Qué hacer si no se escucha el audio del dispositivo controlado](../faq/no_audio_from_the_controlled_device.md).

??? note "¿Qué hago si el audio deja de funcionar al recargar la página o volver a conectarme?"

    Vuelva a comprobar **Speaker** y **Microphone** en la consola del KVM. Las políticas de seguridad del navegador pueden impedir la reproducción por el altavoz o silenciar el micrófono después de recargar la página o volver a conectarse.

    Para más información, consulte [Por qué no se conservan los ajustes del altavoz y del micrófono](../faq/speaker_microphone_settings_cannot_be_retained.md).

??? note "¿Qué hago si aparece el mensaje «Microphone Access Denied»?"

    Compruebe lo siguiente en el ordenador de control:

    - **Permisos del sistema**: en Windows 11, vaya a **Settings** -> **Privacy & security** -> **Microphone**. Active **Microphone access**, **Let apps access your microphone** y **Let desktop apps access your microphone**.

    - **Permisos del navegador**: permita que el sitio web del KVM acceda al micrófono. Si antes había bloqueado el acceso, actualice los permisos del micrófono para ese sitio y recargue la página.

    - **Uso del micrófono**: cierre las demás aplicaciones o pestañas del navegador que puedan estar usando el micrófono.

    Tras estas comprobaciones, vuelva a activar **Microphone** en la consola del KVM.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
