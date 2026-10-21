# Guida alla console di Comet Pro (GL-RM10) {#comet-pro-gl-rm10-console-guide}

## Sessione { #session }

Nella console web, aprire **Session**. La pagina delle impostazioni comprende quattro sezioni:

- [Video](#video)
- [Audio e videocamera](#audio-camera)
- [Tastiera](#keyboard)
- [Mouse](#mouse)

### Video {#video}

In Session è possibile personalizzare le impostazioni video, tra cui modalità di visualizzazione, qualità e trasmissione video, orientamento dello schermo ed EDID.

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session-video.png){class="glboxshadow"}

- **Transfer**: Selezionare il metodo di trasmissione video tra WebRTC, WebRTC (FEC), WebRTC (Native) e Direct. La trasmissione Direct non supporta l'audio.

    !!! note "Qual è la differenza tra WebRTC, WebRTC (FEC), WebRTC (Native) e Direct?"

        - **WebRTC**: Offre un equilibrio tra fluidità video e stabilità audio per il controllo remoto in tempo reale.

        - **WebRTC (FEC)**: Aggiunge la correzione degli errori in avanti per migliorare la stabilità della connessione su reti di scarsa qualità o instabili. Quando è selezionata, questa modalità recupera automaticamente i pacchetti persi trasmettendo una piccola quantità di dati ridondanti, riducendo sfarfallio e ritardi.

        - **WebRTC (Native)**: Utilizza la libreria Google WebRTC per migliorare le prestazioni dello streaming e rendere più fluido il controllo remoto in tempo reale. Questa modalità di trasmissione è stata introdotta nel firmware v1.10.0.

        - **Direct**: Offre la latenza più bassa e una qualità video senza perdita, ma non supporta la trasmissione audio.

- **Mode**: Passare dalla modalità Smart a Normal secondo necessità. La modalità Smart aiuta a ridurre il consumo di banda, soprattutto sulle reti di scarsa qualità.

- **Latency Mode**: È possibile scegliere tra Lowest Latency e Smooth Display. Questa funzione è stata introdotta nel firmware v1.9.0.

    !!! note "Qual è la differenza tra Lowest Latency e Smooth Display?"

        - **Lowest Latency**: Riduce al minimo la latenza di input per rendere più reattivi tastiera e mouse.

        - **Smooth Display**: Ottimizza le prestazioni video per eliminare scatti e perdita di fotogrammi, offrendo una riproduzione regolare.

- **Quality**: Impostare la qualità video su Auto/Low/Medium/High/Ultra-high/Lossless in base alla rete e alla risoluzione richiesta.

- **FEC Packets**: Quando la rete è instabile, recupera automaticamente i pacchetti persi inviando una piccola quantità di dati ridondanti, riducendo sfarfallio e ritardi. È possibile impostare il rapporto FEC su 5%/10%/15%/20%.

- **Orientation**: Impostare l'angolo di rotazione della console su 0°/90°/180°/270°.

- **EDID**: Acronimo di Extended Display Identification Data, consente di selezionare automaticamente i parametri di visualizzazione ottimali.

    L'impostazione predefinita è adatta alla maggior parte dei casi e in genere non richiede modifiche. Per i dettagli, consultare [questa guida](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. Se lo schermo non si aggiorna dopo aver modificato l'EDID, riavviare il dispositivo controllato.

- **View**: Determina il ridimensionamento dello schermo quando si modifica la dimensione della finestra del browser. Le opzioni disponibili sono Adaptive, Best Picture Quality e Original Pixel. Questa funzione è stata introdotta nel firmware v1.8.0.

- **Screen Privacy**: Quando è abilitata la protezione dello schermo, il monitor esterno collegato a HDMI-OUT non mostra più alcun contenuto, garantendo la riservatezza delle operazioni da remoto.

### Audio e videocamera {#audio-camera}

È possibile modificare le impostazioni audio e della videocamera per il dispositivo controllato.

![Audio_Camera](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_audio_camera.png){class="glboxshadow"}

- **Speaker**: Controlla l'uscita audio del dispositivo controllato, ad esempio i suoni di sistema e l'audio dei video.

- **Microphone**: Trasmette l'audio locale, ad esempio la propria voce, dal dispositivo di controllo a quello remoto. Supporta la disattivazione dell'audio con un clic e una scorciatoia da tenere premuta per attivare il microfono (Press To Speak).

    **Nota**: Prima dell'uso, configurare manualmente la scorciatoia in [Settings](#usb-devices).

- **Camera**: Quando la videocamera è abilitata sul dispositivo di controllo, i fotogrammi video locali vengono inoltrati al dispositivo remoto, dove viene emulata una videocamera USB virtuale. Le applicazioni in esecuzione sul dispositivo remoto, ad esempio i programmi per videoconferenze e FaceTime, possono usare questo flusso video come se fosse presente una videocamera fisica collegata direttamente.

    **Nota**: Questa funzione è stata introdotta nel firmware v1.10.0 ed è supportata esclusivamente in modalità WebRTC (FEC). Attualmente è disponibile solo tramite browser web; l'app e il client desktop non la supportano ancora.

### Tastiera { #keyboard }

La sezione Keyboard consente di configurare l'uso della tastiera sul dispositivo controllato.

![keyboard image ](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_keyboard.png){class="glboxshadow"}

- **Bad Link Mode**: Rilascia immediatamente i tasti. Ogni pressione viene inviata come un'unica azione rapida di pressione e rilascio, evitando tasti bloccati o ripetizioni involontarie durante il controllo remoto.

- **Show Virtual Keyboard**: Mostra la tastiera virtuale e ne consente l'uso nella console.

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_show_virtual_keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: Inverte i tasti Cmd e Ctrl per garantire la compatibilità della tastiera tra sistemi operativi diversi.

### Mouse {#mouse}

È possibile modificare le impostazioni del mouse per migliorare l'uso del dispositivo controllato.

![mouse image](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_mouse.png){class="glboxshadow"}

- **Show Local Cursor**: Mostra sullo schermo il cursore del dispositivo corrente.

- **Mouse Jiggle**: Simula piccoli movimenti periodici del mouse per impedire che il dispositivo controllato entri in sospensione a causa di un'inattività prolungata, ad esempio durante riunioni da remoto o la gestione di server.

- **Scroll Rate**: Imposta la velocità di scorrimento della rotellina o il numero di righe/unità percorse a ogni rotazione, determinando la velocità di scorrimento dei contenuti sul dispositivo remoto.

- **Scroll Direction**: Determina se la rotazione della rotellina verso l'alto o il basso sposta i contenuti dello schermo remoto nella stessa direzione (scorrimento naturale) o in quella opposta (scorrimento tradizionale).

    Sono disponibili quattro modalità: Standard, Vertical Invert, Horizontal Invert e Both Invert.

- **Mouse Mode**: Consente di scegliere tra Absolute Mode e Relative Mode per controllare il cursore in modo fluido e preciso nei diversi scenari di controllo remoto.

    !!! note "Qual è la differenza tra Absolute Mode e Relative Mode?"

        - **Relative Mode**: La posizione del mouse viene calcolata in base al movimento, anziché a coordinate fisse sullo schermo. Per controllare il mouse è necessario fare clic all'interno della finestra remota. Il cursore resta bloccato nello schermo remoto e non può uscirne liberamente. Questa modalità offre una migliore compatibilità con BIOS, sistemi meno recenti e dispositivi embedded.

        - **Absolute Mode**: La posizione del mouse corrisponde a coordinate precise sullo schermo. Il cursore remoto segue quello locale in modo fluido e accurato, permettendo di passare liberamente dallo schermo locale a quello remoto. È ideale per l'uso quotidiano del desktop e le operazioni di precisione, anche se la trasmissione di rete può causare un lieve ritardo.

        Usare Absolute per un controllo fluido nell'uso quotidiano; scegliere Relative per accedere al BIOS, per i dispositivi meno recenti che non supportano il posizionamento assoluto o per evitare movimenti accidentali del cursore.

- **Relative Sensitivity**: Disponibile quando Mouse Mode è impostato su Relative.

- **Primary Button**: Selezionare il pulsante sinistro o destro come pulsante principale. Questa funzione è stata introdotta nel firmware v1.9.0.

## Strumenti { #toolbox }

Nella console web, aprire **Toolbox**. La pagina comprende cinque sezioni:

- [Appunti](#clipboard)
- [OCR](#ocr)
- [Scorciatoie](#shortcut)
- [Wake-on-LAN](#wake-on-lan)
- [Terminale](#terminal)

### Appunti { #clipboard }

Gli appunti consentono di incollare facilmente testo dal dispositivo di controllo al dispositivo controllato, senza trasferire file.

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_clipboard.png){class="glboxshadow"}

### OCR {#ocr}

La funzione OCR riconosce il testo e consente di estrarlo facilmente da un'area selezionata dello schermo remoto. Questa funzione è stata introdotta nel firmware v1.9.0.

Per usarla, fare clic sulla freccia rivolta verso il basso e selezionare la lingua di riconoscimento desiderata, ad esempio cinese, inglese o bilingue (Zh/En).

![recognition language](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_ocr.png){class="glboxshadow"}

Fare quindi clic su **Capture**: lo schermo remoto si oscurerà. Disegnare un riquadro attorno al testo da estrarre; il sistema lo riconoscerà automaticamente. Sarà quindi possibile copiare il testo riconosciuto.

![copy text](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/ocr_copy_text.png){class="glboxshadow"}

Questa funzione consente di acquisire facilmente il testo dallo schermo remoto, cioè dal dispositivo controllato, e copiarlo sul dispositivo di controllo locale.

### Scorciatoie { #shortcut }

Le scorciatoie permettono di eseguire le azioni più rapidamente senza usare la tastiera virtuale, risparmiando tempo nelle attività quotidiane. Qui sono disponibili alcune scorciatoie comuni.

![toolbox-shortcut1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_shorcut.png){class="glboxshadow"}

Fare clic su **Modify** per modificare le opzioni delle scorciatoie secondo necessità.

![toolbox-shortcut2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_shorcut_modify.png){class="glboxshadow"}

### Wake-on-LAN { #wake-on-lan }

Wake-on-LAN (WOL) è una tecnologia che consente di accendere il dispositivo controllato da remoto o riattivarlo da uno stato a basso consumo.

Fare clic su **Add Device** e scegliere un dispositivo sulla stessa LAN.

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_wake_on_lan.png){class="glboxshadow"}

![wol-add-device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/wol-add-device.png){class="glboxshadow"}

Se il dispositivo da aggiungere non è presente nell'elenco, fare clic su **Add Manually** e inserire il nome del dispositivo e il suo indirizzo MAC.

![wol-add-manually](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/wol-add-manually.png){class="glboxshadow"}

### Terminale { #terminal }

È possibile accedere al terminale di Comet Pro per eseguire configurazioni avanzate. Fare clic su **Access**.

![toolbox-terminal1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_terminal.png){class="glboxshadow"}

Si aprirà il terminale GLKVM.

![toolbox-terminal2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox-terminal-2.png){class="glboxshadow"}

## Accessori { #accessories }

GL.iNet offre accessori KVM opzionali per controllare da remoto l'accensione e lo spegnimento del dispositivo.

Per prima cosa, consultare la guida corrispondente per collegare l'accessorio al dispositivo controllato.

- [Guida utente di Fingerbot (FGB-01)](../gl-fgb-01/index.md){target="_blank"}

- [Guida utente della scheda ATX (GL-ATXPC)](../gl-atx-board/index.md){target="_blank"}

Accedere quindi alla console KVM e aprire **Accessories**. Le impostazioni dell'accessorio sono disponibili solo dopo la sua installazione.

### Fingerbot {#fingerbot}

Fingerbot viene fissato al pulsante fisico di accensione del dispositivo controllato per consentirne il controllo da remoto.

Funziona in base alle impostazioni della console.

![accessories fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/accessories-fgb.png){class="glboxshadow"}

- **Time**: Durata della pressione di Fingerbot. È possibile impostarla su 0.5s/3s/8s.

- **Strength**: Sono disponibili due livelli di forza: Lightly Press e Firmly Press.

    - **Lightly Press**: Adatto a pulsanti con corsa breve o sensibili al tocco.

    - **Firmly Press**: Ideale per pulsanti con corsa lunga o che richiedono più forza.

    ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### Alimentazione ATX { #atx-power }

La scheda ATX si installa nel case del computer e consente di accendere, spegnere e riavviare il dispositivo da remoto.

Funziona in base alle impostazioni della console.

![accessories atxpower](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/accessories-atx.png){class="glboxshadow"}

- **Power (Short Press)**: Per l'accensione normale o la riattivazione del sistema.

- **Power (Long Press)**: Esegue uno spegnimento forzato.

- **Restart**: Riavvia il dispositivo.

## Supporti virtuali { #virtual-media }

Nella console web, aprire **Virtual Media**. Qui è possibile eseguire le seguenti operazioni:

- [Condivisione di file](#file-sharing)
- [Montaggio di immagini](#image-mounting)
- [Sostituire l'unità di archiviazione](#replace-storage-drive)
- [Formattare il disco](#format-disk)

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/virtual-media.png){class="glboxshadow"}

### Condivisione di file { #file-sharing }

Comet Pro emula un'unità USB di lettura e scrittura, consentendo di condividere e gestire file tra il dispositivo di controllo e quello controllato.

**Per condividere file dal dispositivo di controllo al dispositivo controllato, seguire questi passaggi.**

1. Trascinare i file nel riquadro o fare clic al suo interno per caricarli dal dispositivo di controllo, oppure caricarli tramite URL.

    Dopo il caricamento, i file verranno visualizzati come segue.

    ![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-uploaded.png){class="glboxshadow"}

2. Fare clic su **Mount To Remote** -> **File Sharing**.

    ![file sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount1.png){class="glboxshadow"}

3. Nella console comparirà una finestra con le istruzioni per la condivisione dei file, come mostrato di seguito.

    ![file sharing prompt](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount2-prompt.png){class="glboxshadow"}

4. Attendere un momento: sullo schermo comparirà automaticamente un'unità denominata **"GLKVM"**. I file caricati in precedenza dal dispositivo di controllo su Comet Pro saranno ora condivisi con il dispositivo controllato. Da quest'ultimo sarà possibile visualizzare, spostare o eliminare i file presenti nell'unità.

    ![file sharing glkvm drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount3.png){class="glboxshadow"}

    **Suggerimento**: Se l'unità non compare automaticamente, aprire **This PC** sul dispositivo controllato.

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-thispc.png){class="glboxshadow"}

    Individuare quindi l'unità denominata **GLKVM**. Da qui è possibile visualizzare, spostare o eliminare i file presenti nell'unità.

5. Per interrompere la condivisione, fare clic su **Virtual Media** nella barra degli strumenti, quindi su **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/stop-sharing1.png){class="glboxshadow"}

**Per condividere file dal dispositivo controllato al dispositivo di controllo, seguire questi passaggi.**

1. Sul dispositivo controllato, spostare o copiare i file da condividere nell'unità **GLKVM**.

    Nell'esempio, un'immagine denominata "slate7-pro_gl-be10000" è stata spostata dal desktop del dispositivo controllato all'unità **GLKVM**.

    ![move file to drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-copy.png){class="glboxshadow"}

2. Tornare alla console di Comet Pro, fare clic su **Virtual Media** nella barra degli strumenti, quindi su **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/stop-sharing2.png){class="glboxshadow"}

3. Il file verrà visualizzato in **Virtual Media**, come mostrato di seguito. Sarà quindi possibile scaricarlo da Comet Pro sul dispositivo di controllo.

    ![file shared](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-shared.png){class="glboxshadow"}

### Montaggio di immagini { #image-mounting }

Comet Pro può simulare un'unità CD/DVD o disco virtuale di sola lettura sul dispositivo controllato. È possibile accedervi durante l'avvio del BIOS o UEFI.

Questa funzione permette di reinstallare il sistema operativo, montare un'immagine ISO per installare applicazioni sul dispositivo controllato o eseguire altre attività.

1. Trascinare i file nel riquadro o fare clic al suo interno per caricarli. **Assicurarsi che il file possa essere montato come immagine ISO**.

    Dopo il caricamento, i file verranno visualizzati come segue.

    ![image mount1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount1.png){class="glboxshadow"}

2. Fare clic su **Mount To Remote** -> **Image Mounting**.

    ![image mount2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount2.png){class="glboxshadow"}

3. Nella finestra che si apre, selezionare il file e fare clic su **Mount Image**.

    ![image mount3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount3.png){class="glboxshadow"}

4. Ora è possibile usare il file dall'unità CD del dispositivo controllato.

    ![image mount4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount4.png){class="glboxshadow"}

### Sostituzione dell'unità di archiviazione { #replace-storage-drive }

È possibile collegare un dispositivo di archiviazione USB alla porta USB del KVM per sostituire la memoria interna.

![replace storage drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/replace-storage.png){class="glboxshadow"}

### Formattazione del disco { #format-disk }

È possibile formattare il disco o disabilitare i supporti virtuali con un clic.

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/format-storage.png){class="glboxshadow"}

- **Format**: Cancella tutti i dati sul disco e reinizializza la struttura del file system.

- **Disable**: Disabilitare i supporti virtuali riavvia immediatamente il dispositivo KVM.

## Centro applicazioni { #apps-center }

Nella console web, aprire **Apps Center** per accedere alle applicazioni integrate.

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} è un servizio VPN mesh basato su WireGuard che crea reti private peer-to-peer crittografate tra dispositivi, senza port forwarding o configurazioni complesse del firewall.

Comet Pro integra Tailscale e consente l'accesso remoto tramite la sua rete virtuale.

È sufficiente associare Comet Pro e il dispositivo di controllo allo stesso account Tailscale. Si potrà quindi accedere a Comet Pro da remoto inserendo il suo **IP virtuale Tailscale** nel browser del dispositivo di controllo, senza installare l'app GLKVM. Per i dettagli, consultare [questa guida](../../faq/remote_access_via_tailscale.md){target="_blank"}.

Dopo l'associazione, la console mostra l'account Tailscale collegato e rende disponibili funzioni avanzate, tra cui Exit Node e Subnet Routes.

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} crea reti virtuali overlay crittografate che collegano dispositivi distribuiti in tutto il mondo come se fossero sulla stessa rete locale.

Comet Pro integra ZeroTier e consente l'accesso remoto tramite la sua rete virtuale.

È sufficiente collegare Comet Pro e il dispositivo di controllo alla stessa rete ZeroTier. Si potrà quindi accedere a Comet Pro da remoto inserendo il suo **IP ZeroTier** nel browser del dispositivo di controllo, senza installare l'app GLKVM. Per i dettagli, consultare [questa guida](../../faq/remote_access_via_zerotier.md){target="_blank"}.

Dopo l'associazione, la console mostra il Network ID e l'IP virtuale ZeroTier.

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/zerotier-enabled.png){class="glboxshadow"}

### NetBird {#netbird}

[NetBird](https://netbird.io/){target="_blank"} è una piattaforma di rete open source zero trust che permette di creare reti private sicure per uso domestico e aziendale. Grazie a una rete overlay basata su WireGuard®, NetBird consente di accedere in sicurezza ai propri dispositivi in qualsiasi momento e da qualsiasi luogo.

Comet Pro integra NetBird e consente l'accesso remoto tramite la sua rete virtuale. Per i dettagli, consultare [questa guida](../../faq/remote_access_via_netbird.md){target="_blank"}.

Dopo l'associazione, la console mostra l'IP virtuale NetBird.

![netbird enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/netbird-enabled.png){class="glboxshadow"}

## Assistenza { #help }

Nella console web, aprire **Help**. Qui sono disponibili ulteriori informazioni su GL.iNet KVM e la documentazione di assistenza; è inoltre possibile esportare i log per la risoluzione dei problemi.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/help.png){class="glboxshadow"}

## Barra degli strumenti { #toolbar }

Nella console web, accedere all'angolo superiore destro per usare i seguenti strumenti:

- [Comprimere la barra degli strumenti](#collapse)
- [Schermo intero](#fullscreen)
- [Aggiornamento](#upgrade)
- [Statistiche della connessione](#connection-stats)
- [Servizio cloud](#cloud-service)
- [Disconnessione](#logout)

### Compressione della barra { #collapse }

Fare clic sull'icona della freccia rivolta verso l'alto nell'angolo superiore destro per comprimere la barra degli strumenti.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/collapse_1.png){class="glboxshadow"}

Quando la barra degli strumenti è compressa, fare clic sulla freccia rivolta verso il basso in alto per espanderla.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/collapse_2.png){class="glboxshadow"}

### Schermo intero { #fullscreen }

Fare clic sull'icona a forma di quadrato nell'angolo superiore destro per passare alla modalità a schermo intero.

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/fullscreen_1.png){class="glboxshadow"}

Per uscire dalla modalità a schermo intero, tenere premuto il tasto **Esc** oppure fare clic sull'icona di uscita a forma di griglia nell'angolo superiore destro.

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/fullscreen_2.png){class="glboxshadow"}

### Aggiornamento { #upgrade }

Fare clic sulla versione del firmware nell'angolo superiore destro per verificare la disponibilità di aggiornamenti.

![firmware upgrade 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade_1.png){class="glboxshadow"}

Nella finestra che si apre, fare clic su **Local Upgrade** per caricare un file del firmware.

![firmware upgrade 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade_2.png){class="glboxshadow"}

![firmware upgrade 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade_3.png){class="glboxshadow" width=350}

Prima di eseguire un aggiornamento locale, scaricare il firmware più recente dal [centro download del firmware](https://dl.gl-inet.com/kvm){target="_blank"}.

### Statistiche della connessione { #connection-stats }

Connection Stats include un pannello dati che monitora latenza, jitter e altre metriche in tempo reale.

Fare clic sull'icona dell'elenco per visualizzare lo stato del dispositivo e i dati in tempo reale.

![data dashboard 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/data_dashboard_1.png){class="glboxshadow"}

Fare clic sull'icona del grafico per visualizzare le statistiche, tra cui latenza e jitter di rete, tasso di perdita dei pacchetti, frequenza dei fotogrammi in tempo reale e ritardo di riproduzione.

![data dashboard 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/data_dashboard_2.png){class="glboxshadow"}

### Servizio cloud { #cloud-service }

GL.iNet KVM Cloud consente di accedere al dispositivo controllato da remoto. Per i dettagli, consultare [questa guida](../../faq/remote_access_via_cloud.md){target="_blank"}.

Dopo aver associato Comet Pro al cloud, la console mostrerà lo stato del cloud come segue.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/cloud.png){class="glboxshadow"}

### Disconnessione { #logout }

Per disconnettersi, fare clic sull'icona Logout.
![layout](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/logout.png){class="glboxshadow"}

## Impostazioni { #settings }
Nella console web, fare clic sull'icona Settings nella barra di navigazione per aprire la pagina delle impostazioni mostrata di seguito. Questa funzione è stata introdotta nel firmware v1.10.0.

- [Dispositivi USB](#usb-devices)
- [Preferenze](#preferences)
- [Rete](#network)
- [Sicurezza](#security)
- [Cloud](#cloud)
- [Sistema](#system)

![Settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting.png){class="glboxshadow"}

### Dispositivi USB { #usb-devices }

La sezione USB Devices centralizza la gestione di tutti i dispositivi USB emulati. Da questa pagina è possibile attivare o disattivare le periferiche virtuali per migliorare la compatibilità con il dispositivo controllato.

![USB Emulated Devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_usb_devices.png){class="glboxshadow"}

- **Microphone**

    Quando il microfono è disattivato, fare clic su Settings per personalizzare le scorciatoie in base alle proprie abitudini. Tenere premuto il tasto assegnato per parlare; rilasciandolo, il microfono verrà nuovamente disattivato.

    ![mic settings 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mic_setting_1.png){class="glboxshadow" width=600}

    ![mic settings 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mic_setting_2.png){class="glboxshadow" width=434}

  - **Device Identity**

    Consente di personalizzare o modificare l'identità del KVM riconosciuta dal dispositivo controllato. EDID e identificazione del dispositivo restano sincronizzati: modificando uno dei due, l'altro si aggiorna automaticamente per garantire il corretto riconoscimento del dispositivo.

    ![Device Identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/device_identification.png){class="glboxshadow" width=350}

### Preferenze { #preferences }

La sezione Preferences consente di gestire Layout Preferences, System Settings e le impostazioni dello schermo del dispositivo.

![Preferences](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_preference.png){class="glboxshadow"}

- **Layout Preferences**: Consente di scegliere se mostrare la barra degli strumenti a schermo intero e la barra di stato in modalità finestra.

- **System Settings**: Per personalizzare le impostazioni di sistema, scegliere Tab Title del browser, Language (cinese, inglese o giapponese), Color Mode (Light o Dark) e Timezone in base alla propria area geografica.

- **Device Screen**: Consente di gestire e visualizzare in anteprima lo schermo del dispositivo. Le impostazioni disponibili includono la modalità Lock Screen (World Clock, Clock Only o Wallpaper Only), Time Format, Date Format e Wallpaper.

### Rete { #network }

È possibile verificare e modificare i parametri di rete di Comet Pro, come il nome host e l'indirizzo IP.

![network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network.png){class="glboxshadow"}

- **Hostname**: Consente di modificare il nome host del dispositivo direttamente nella console. Questa funzione è stata introdotta nel firmware v1.7.0.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_hostname.png){class="glboxshadow" width=600}

- **Ethernet Settings**: Quando Comet Pro si connette a un dispositivo di rete a monte tramite un cavo Ethernet, i dettagli della connessione Ethernet vengono visualizzati qui.

    Se il protocollo è DHCP, la pagina viene visualizzata come segue.

    ![ethernet dhcp](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_dhcp.png){class="glboxshadow" width=600}

    Per impostare un indirizzo IP statico, selezionare il protocollo **Static** e inserire i parametri di rete richiesti, ad esempio indirizzo IP, maschera di rete e gateway.

    ![ethernet static](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_static.png){class="glboxshadow" width=600}

- **Wireless**: Quando Comet Pro si connette a una rete Wi-Fi, qui vengono visualizzati il suo indirizzo IP, il gateway e l'indirizzo MAC.

    ![wifi config](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_wifi.png){class="glboxshadow" width=600}

    Per collegarlo a un'altra rete Wi-Fi, fare clic su **Switch Wi-Fi** e selezionare una rete dall'elenco di quelle disponibili.

    ![join wifi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_switch_network.png){class="glboxshadow" width=500}

### Sicurezza { #security }

La sezione Security consente di modificare la password di amministrazione, abilitare l'autenticazione a due fattori e personalizzare il certificato TLS.

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_security.png){class="glboxshadow"}

- Change Admin Password

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/change-password.png){class="glboxshadow" width="434"}

- 2FA: Abilitare l'autenticazione a due fattori per proteggere l'account.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/2fa.png){class="glboxshadow"}

- TLS Certificate

    Per l'accesso tramite browser, il sistema utilizza il certificato predefinito preinstallato. Per personalizzare il certificato TLS, fare clic su **Custom** in TLS Certificate, quindi caricare il **file del certificato e il file della chiave privata**.

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_security_custom.png){class="glboxshadow"}

### Cloud {#cloud}

La sezione Cloud consente di accedere al dispositivo e gestirlo da remoto tramite i servizi cloud.

È possibile associare il dispositivo al cloud tramite URL. In **More Settings** sono disponibili altre opzioni, come Bind With Code e App Download. Se necessario, è disponibile anche Disable.

![Cloud 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_cloud_1.png){class="glboxshadow"}

Dopo l'associazione, è possibile visualizzare le informazioni dell'account cloud collegato. Fare clic su **Access Cloud** per gestire i dispositivi oppure su **More Settings** per disabilitare il servizio o annullare l'associazione secondo necessità.

![Cloud 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_cloud_2.png){class="glboxshadow"}

Le stesse operazioni sono disponibili anche tramite Cloud Service nella barra degli strumenti superiore.

### Sistema { #system }

Nelle impostazioni System è possibile configurare quanto segue:

![system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_system.png){class="glboxshadow"}

- **System**: Fare clic su **Reboot** per riavviare il dispositivo oppure su **Reset** per cancellare la configurazione corrente e configurarlo nuovamente.

- **Upgrade**: Abilitare Beta Center per ricevere aggiornamenti firmware beta oppure usare Local Upgrade per installare manualmente il firmware da un file locale.

    ![local Upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setthing_system_local_update.png){class="glboxshadow" width=400}

- **Help & Support**: Export Log Files consente di salvare i log di funzionamento del dispositivo per la risoluzione dei problemi e l'assistenza postvendita. Help Document permette di accedere a guide utente, domande frequenti e documentazione per la risoluzione dei problemi.
