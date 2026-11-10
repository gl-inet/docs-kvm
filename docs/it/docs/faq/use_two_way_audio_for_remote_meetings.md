# Come usare l'audio bidirezionale nelle riunioni a distanza? {#how-can-i-use-two-way-audio-for-remote-meetings}

Quando lavori da casa, puoi usare il KVM per accedere al computer dell'ufficio e partecipare a riunioni audio con Zoom, Microsoft Teams o un'app simile. La funzionalità audio bidirezionale del KVM di GL.iNet ti permette di parlare tramite il microfono del computer locale e di ascoltare gli altri partecipanti tramite i suoi altoparlanti o le cuffie.

## Configurazione rapida {#quick-setup}

Segui questi passaggi per usare il microfono e l'altoparlante del dispositivo locale nelle riunioni a distanza. L'esempio usa Zoom.

1. Prima di partecipare alla riunione, accedi al KVM dal computer di controllo e vai su **Session** -> **Audio & Camera**. Attiva **Speaker** e **Microphone**. Verifica che entrambe le icone in basso a destra siano attive.

    ![Attivare altoparlante e microfono](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/enable-speaker-and-microphone.png){class="glboxshadow"}

    Per esempio, quando attivi **Microphone**, il browser potrebbe chiederti di accedere al microfono. Seleziona il microfono che vuoi usare e consenti l'accesso.

    ![Richiesta di accesso al microfono](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/microphone-permission-popup.png){class="glboxshadow"}

2. Apri Zoom e partecipa alla riunione dal computer controllato. Fai clic sulla freccia accanto al pulsante dell'audio e seleziona i dispositivi seguenti, come nell'esempio:

    - **Microphone**: Microphone (6-Comet Microphone)

    - **Speaker**: EPSON PJ (HD Audio Driver for Display Audio)

    ![Selezionare microfono e altoparlante](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/select-microphone-and-speaker.png){class="glboxshadow"}

    Riattiva quindi il microfono per parlare con gli altri partecipanti. Puoi ascoltarli tramite gli altoparlanti o le cuffie del computer di controllo.

    Se vuoi condividere con i partecipanti anche il video della videocamera locale, consulta la [guida all'uso della videocamera locale](../faq/use_camera_passthrough_for_remote_meetings.md).

## Risoluzione dei problemi {#troubleshooting}

??? note "Cosa fare se gli altri partecipanti non mi sentono?"

    Sul computer controllato, vai su **Settings** -> **System** -> **Sound** e cerca in **Input** il microfono virtuale del KVM, indicato come **Comet Microphone** nell'esempio. Verifica che lo stesso microfono sia selezionato anche nell'app per le riunioni.

    ![Controllare l'ingresso](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-input.png){class="glboxshadow"}

    - Se il microfono virtuale del KVM non compare, controlla il collegamento dati USB tra il KVM e il computer controllato. Questo collegamento trasmette l'audio del microfono al computer controllato.

    - Se il microfono virtuale del KVM compare ed è selezionato ma non arriva alcun segnale audio, verifica che il microfono sia attivo sia sul computer di controllo sia nell'app per le riunioni sul computer controllato. Controlla le autorizzazioni del microfono nel sistema e nel browser del computer di controllo, quindi chiudi le altre app o schede del browser che potrebbero usarlo.

??? note "Cosa fare se non sento gli altri partecipanti?"

    Sul computer controllato, vai su **Settings** -> **System** -> **Sound** e cerca in **Output** l'uscita audio HDMI collegata al KVM, indicata come **EPSON PJ** nell'esempio. Verifica che nell'app per le riunioni sia selezionato lo stesso dispositivo come altoparlante.

    ![Controllare l'uscita](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-output.png){class="glboxshadow"}

    - Se l'uscita audio HDMI non compare, controlla il collegamento HDMI tra il computer controllato e il KVM. Questo collegamento trasmette l'audio dal computer controllato. Se usi un adattatore HDMI, verifica che supporti l'audio.

    - Se l'uscita audio HDMI compare ed è selezionata ma non senti ancora gli altri partecipanti, verifica che l'audio sia attivo sul computer di controllo, nella scheda del browser e sugli altoparlanti o sulle cuffie.

    Per ulteriori informazioni, consulta [Cosa fare se il dispositivo controllato non riproduce audio](../faq/no_audio_from_the_controlled_device.md).

??? note "Cosa fare se l'audio si interrompe dopo aver ricaricato la pagina o essersi riconnessi?"

    Controlla di nuovo **Speaker** e **Microphone** nella console KVM. Dopo che hai ricaricato la pagina o ti sei riconnesso, le regole di sicurezza del browser possono disattivare la riproduzione dagli altoparlanti o silenziare il microfono.

    Per ulteriori informazioni, consulta [Perché le impostazioni di altoparlante e microfono non vengono mantenute](../faq/speaker_microphone_settings_cannot_be_retained.md).

??? note "Cosa fare se compare il messaggio «Microphone Access Denied»?"

    Controlla quanto segue sul computer di controllo:

    - **Autorizzazioni di sistema**: in Windows 11, vai su **Settings** -> **Privacy & security** -> **Microphone**. Attiva **Microphone access**, **Let apps access your microphone** e **Let desktop apps access your microphone**.

    - **Autorizzazioni del browser**: consenti al sito web del KVM di accedere al microfono. Se in precedenza hai bloccato l'accesso, aggiorna le autorizzazioni del microfono per il sito e ricarica la pagina.

    - **Uso del microfono**: chiudi le altre app o schede del browser che potrebbero usare il microfono.

    Dopo questi controlli, attiva di nuovo **Microphone** nella console KVM.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
