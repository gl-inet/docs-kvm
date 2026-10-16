# Cosa fare se non si sente l'audio del dispositivo controllato {#what-should-i-do-if-theres-no-audio-from-the-controlled-device}

Se, dopo aver collegato il KVM al dispositivo controllato, non riesci a sentirne l'audio, ad esempio durante la riproduzione di un video, prova le seguenti soluzioni:

1. Assicurati che Speaker sia attivo nella console del KVM.

    Nella console del KVM, vai su **Settings** -> **Remote Device Settings** -> **Speaker** e assicurati che l'altoparlante sia attivo. Verifica anche che l'icona nell'angolo in basso a destra sia illuminata, a indicare che la funzione è attiva.

    ![speaker](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/speaker.png){class="glboxshadow"}

2. Assicurati che tutti i cavi tra il KVM e il dispositivo controllato siano collegati saldamente. Un collegamento allentato può compromettere l'uscita audio.

3. Verifica se è collegato un convertitore HDMI. Alcuni convertitori non supportano l'audio.

    È consigliato usare il cavo HDMI incluso nella confezione, poiché alcuni cavi conformi a standard HDMI meno recenti potrebbero non supportare la trasmissione audio.

4. Verifica che l'audio non sia disattivato sul dispositivo di controllo e sul dispositivo controllato.

5. Controlla le impostazioni di uscita del dispositivo controllato e assicurati che il dispositivo di uscita sia **GLKVM**.

    ??? "macOS"

        Sul dispositivo controllato, vai su **Settings** -> **Sound** -> **Output & Input** -> **Output** e imposta il dispositivo di uscita su **GLKVM**.

        ![mac output settings](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/mac_output_settings.png){class="glboxshadow"}

    ??? "Windows"

        Sul dispositivo controllato, vai su **Settings** -> **Sound** -> **Output** e imposta il dispositivo di uscita su **GLKVM**.

        ![wins output settings 1](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_1.png){class="glboxshadow"}

        ![wins output settings 2](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_2.png){class="glboxshadow"}

        In alternativa, fai clic sull'icona dell'audio nell'angolo in basso a destra del dispositivo controllato e seleziona **GLKVM** come dispositivo di riproduzione.

        ![wins output settings 3](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_3.png){class="glboxshadow"}

6. Controlla il driver della scheda grafica del dispositivo controllato. Se il dispositivo non dispone di tale driver, non potrà trasmettere l'audio e non si sentirà alcun suono sul dispositivo di controllo.

7. Controlla le impostazioni audio avanzate sul dispositivo di controllo e assicurati che il volume del browser sia attivo.

    Di seguito è riportato, come riferimento, un esempio delle impostazioni audio avanzate di Windows 10 Pro.

    Vai su **Settings** -> **Sound** -> **Advanced sound options**.

    ![advanced sound options](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/advanced_sound_options.png){class="glboxshadow"}

    Regola il volume delle singole app e dei suoni di sistema.

    ![app volume](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/app_volume.png){class="glboxshadow"}

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
