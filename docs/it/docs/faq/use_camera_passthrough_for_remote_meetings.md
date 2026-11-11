# Come trasmettere il video della videocamera locale nelle riunioni a distanza? {#how-can-i-use-camera-passthrough-for-remote-meetings}

**Nota**: Questa funzionalità è stata introdotta nel firmware v1.10.0 ed è supportata solo in modalità WebRTC (FEC). Attualmente è disponibile tramite browser web e client desktop, ma non è ancora supportata nell'app mobile.

---

Quando lavori da casa, puoi usare il KVM per accedere al computer in ufficio e partecipare a una videoconferenza su Zoom, Microsoft Teams o un'app simile. Tuttavia, la videocamera potrebbe mostrare solo l'ufficio e non te.

La funzionalità **Camera** del KVM GL.iNet ti consente di trasmettere il video della videocamera del computer di casa al computer in ufficio come videocamera USB virtuale. Seleziona questa videocamera nell'app per le riunioni, così gli altri partecipanti potranno vederti mentre condividi file o applicazioni dal computer in ufficio.

## Configurazione rapida {#quick-setup}

Segui i passaggi qui sotto per usare la funzionalità Camera, prendendo come esempio una videoconferenza Zoom.

1. Prima di partecipare alla riunione, accedi al KVM dal computer di controllo e vai su **Session** -> **Audio & Camera**. Abilita Camera, poi fai clic sull'icona della videocamera per iniziare.

    ![enable camera 1](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera.png){class="glboxshadow"}

    Se compare un messaggio sul limite delle risorse USB quando abiliti Camera, vai su **Settings** -> **USB Devices** e disabilita i dispositivi USB emulati inutilizzati per liberare risorse. Quindi abilita Camera e riprova.

    ![enable camera 3](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-3.png){class="glboxshadow"}

    Il browser potrebbe richiedere l'accesso alla videocamera. Seleziona la videocamera da usare, controlla l'anteprima video e consenti l'accesso.

    ![enable camera 2](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-2.png){class="glboxshadow"}

2. Apri Zoom e partecipa a una riunione sul computer controllato. Fai clic sulla freccia accanto al pulsante del video e seleziona **UVC camera**.

    ![uvc-camera](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/uvc-camera.png){class="glboxshadow"}

    Poi attiva il video, così gli altri partecipanti potranno vedere le immagini della videocamera del dispositivo di controllo.

    **Nota**: Assicurati di avere una connessione di rete stabile per ottenere un video fluido e nitido durante la riunione.

## Risoluzione dei problemi {#troubleshooting}

??? note "Cosa fare se le immagini della videocamera non arrivano al computer controllato?"

    Verifica se il computer controllato riconosce la videocamera virtuale del KVM.

    Sul computer controllato, vai su **Settings** -> **Bluetooth & devices** -> **Cameras** e cerca UVC Camera in Connected cameras.

    ![check camera settings](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/check-camera-settings.png){class="glboxshadow"}

    Se non compare, il collegamento dati USB tra il KVM e il computer controllato potrebbe essere scollegato o allentato.

??? note "Cosa fare se compare il messaggio 'Camera Access Denied' quando abiliti Camera nella console KVM?"

    ![camera access denied](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/camera-access-denied.png){class="glboxshadow"}

    Controlla quanto segue sul computer di controllo:

    - **Disponibilità della videocamera**: Assicurati che la videocamera sia collegata e funzionante. Provala con l'app della videocamera del sistema, poi chiudi l'app prima di riprovare.

    - **Autorizzazioni di sistema**: In Windows 11, vai su Settings -> Privacy & security -> Camera e attiva le seguenti opzioni: Camera access, Let apps access your camera e Let desktop apps access your camera.

    - **Autorizzazioni del browser**: Consenti al sito web del KVM di accedere alla videocamera. Se l'accesso era stato bloccato, aggiorna le autorizzazioni della videocamera per il sito e ricarica la pagina.

    - **Uso della videocamera**: Chiudi le altre app o schede del browser che potrebbero usare la videocamera, come Zoom o Microsoft Teams.

    Dopo questi controlli, abilita nuovamente Camera nella console KVM.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
