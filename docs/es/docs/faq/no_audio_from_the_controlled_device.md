# Qué hacer si no se escucha el audio del dispositivo controlado {#what-should-i-do-if-theres-no-audio-from-the-controlled-device}

Si, después de conectar el KVM y el dispositivo controlado, no escucha su audio, por ejemplo al reproducir vídeos, pruebe las siguientes soluciones:

1. Asegúrese de que Speaker esté activado en la consola KVM.

    En la consola, vaya a **Settings** -> **Remote Device Settings** -> **Speaker** y active el altavoz. Compruebe también que el icono de la esquina inferior derecha esté iluminado, lo que indica que está activo.

    ![Altavoz](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/speaker.png){class="glboxshadow"}

2. Asegúrese de que todos los cables entre el KVM y el dispositivo controlado estén bien conectados. Una conexión floja puede afectar a la salida de audio.

3. Compruebe si hay un convertidor HDMI conectado. Algunos convertidores no admiten audio.

    Se recomienda utilizar el cable HDMI incluido, ya que algunos cables HDMI de estándares antiguos pueden no admitir la transmisión de audio.

4. Compruebe si el dispositivo de control y el dispositivo controlado están silenciados.

5. Compruebe los ajustes de salida del dispositivo controlado y seleccione **GLKVM** como dispositivo de salida.

    ??? "macOS"

        En el dispositivo controlado, vaya a **Settings** -> **Sound** -> **Output & Input** -> **Output** y seleccione **GLKVM** como dispositivo de salida.

        ![Salida de audio en macOS](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/mac_output_settings.png){class="glboxshadow"}

    ??? "Windows"

        En el dispositivo controlado, vaya a **Settings** -> **Sound** -> **Output** y seleccione **GLKVM** como dispositivo de salida.

        ![Salida de audio en Windows](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_1.png){class="glboxshadow"}

        ![Seleccionar salida GLKVM en Windows](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_2.png){class="glboxshadow"}

        También puede hacer clic en el icono de sonido de la esquina inferior derecha del dispositivo controlado y seleccionar **GLKVM** como dispositivo de reproducción.

        ![Dispositivo de reproducción en Windows](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_3.png){class="glboxshadow"}

6. Compruebe el controlador de la tarjeta gráfica del dispositivo controlado. Sin este controlador, el dispositivo no podrá emitir audio y no se escuchará sonido en el dispositivo de control.

7. Compruebe los ajustes avanzados de sonido del dispositivo de control y asegúrese de que el navegador tenga una salida de audio activa.

    A continuación se muestra un ejemplo de Windows 10 Pro.

    Vaya a **Settings** -> **Sound** -> **Advanced sound options**.

    ![Opciones avanzadas de sonido](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/advanced_sound_options.png){class="glboxshadow"}

    Ajuste el volumen de las aplicaciones y de los sonidos del sistema.

    ![Volumen de las aplicaciones](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/app_volume.png){class="glboxshadow"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
