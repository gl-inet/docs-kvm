# Guida alla console di Comet Q (GL-RMQ1) {#comet-q-gl-rmq1-console-guide}

## Impostazioni { #settings }

Nella console web, aprire **Settings**. La pagina delle impostazioni comprende quattro sezioni:

- [Video](#video)
- [Audio, tastiera e mouse](#audiokeyboardmouse)
- [Sistema](#system)
- [Rete](#network)

### Ricerca rapida { #quick-search }

Per trovare rapidamente le impostazioni desiderate, inserire parole chiave nella parte superiore della pagina Settings.

![quick search](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/quick-search.png){class="glboxshadow"}

### Video {#video}

Nella console è possibile personalizzare le impostazioni video, come EDID, qualità e trasmissione video e orientamento dello schermo.

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-video.png){class="glboxshadow"}

- **Type**: Selezionare il tipo di dispositivo controllato.

    Il sistema applica automaticamente la modalità del mouse e le impostazioni EDID consigliate per offrire proporzioni dello schermo e precisione di controllo ottimali. Modificare questa opzione se il dispositivo non viene riconosciuto correttamente o se occorre usare un tipo personalizzato.

- **EDID**: Acronimo di Extended Display Identification Data, consente di selezionare automaticamente i parametri di visualizzazione ottimali.

    L'impostazione predefinita è adatta alla maggior parte dei casi e in genere non richiede modifiche. Per i dettagli, consultare [questa guida](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. Se lo schermo non si aggiorna dopo aver modificato l'EDID, riavviare il dispositivo controllato.

- **Mode**: Passare dalla modalità Smart a Normal secondo necessità. La modalità Smart aiuta a ridurre il consumo di banda, soprattutto sulle reti di scarsa qualità.

- **Quality**: Impostare la qualità video su Low/Medium/High/Ultra-high/Lossless in base alla rete e alla risoluzione richiesta.

- **Transfer**: Selezionare il metodo di trasmissione video tra WebRTC, WebRTC (FEC) e Direct. La trasmissione Direct non supporta l'audio.

    !!! note "Qual è la differenza tra WebRTC, WebRTC (FEC) e Direct?"

        - **WebRTC**: Offre un equilibrio tra fluidità video e stabilità audio per il controllo remoto in tempo reale.

        - **WebRTC (FEC)**: Aggiunge la correzione degli errori in avanti per migliorare la stabilità della connessione su reti di scarsa qualità o instabili. Quando è selezionata, questa modalità recupera automaticamente i pacchetti persi trasmettendo una piccola quantità di dati ridondanti, riducendo sfarfallio e ritardi.

        - **Direct**: Offre la latenza più bassa e una qualità video senza perdita, ma non supporta la trasmissione audio.

- **Orientation**: Impostare l'angolo di rotazione della console su 0°/90°/180°/270°.

- **View**: Determina il ridimensionamento dello schermo quando si modifica la dimensione della finestra del browser. Le opzioni disponibili sono Adaptive, Best Picture Quality e Original Pixel.

### Audio, tastiera e mouse { #audiokeyboardmouse }

È possibile modificare le impostazioni di audio, tastiera e mouse.

![audio keyboard mouse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/audio-keyboard-mouse.png){class="glboxshadow"}

- **Speaker**: Controlla l'uscita audio del dispositivo controllato, ad esempio i suoni di sistema e l'audio dei video.

- **Microphone**: Trasmette l'audio locale, ad esempio la propria voce, dal dispositivo di controllo a quello remoto. Supporta la disattivazione dell'audio con un clic e una scorciatoia da tenere premuta per attivare il microfono (Press To Speak).

    ![mic settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/mic-settings.png){class="glboxshadow"}

    ![press to speak](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/press-to-speak.png){class="glboxshadow"}

- **Keyboard**: Abilita o disabilita la tastiera del dispositivo controllato.

- **Bad Link Mode**: Rilascia immediatamente i tasti. Ogni pressione viene inviata come un'unica azione rapida di pressione e rilascio, evitando tasti bloccati o ripetizioni involontarie durante il controllo remoto.

- **Show Virtual Keyboard**: Mostra la tastiera virtuale e ne consente l'uso nella console.

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: Inverte i tasti Cmd e Ctrl per garantire la compatibilità della tastiera tra sistemi operativi diversi.

- **Mouse**: Abilita o disabilita il mouse del dispositivo controllato.

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

### Sistema { #system }

È possibile personalizzare le impostazioni di visualizzazione del sistema nella console oppure ripristinare il dispositivo con un clic.

![settings-system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-system.png){class="glboxshadow"}

- **Device Identity**: Consente di personalizzare o modificare l'identità del KVM riconosciuta dal dispositivo controllato. EDID e identificazione del dispositivo restano sincronizzati: modificando uno dei due, l'altro si aggiorna automaticamente per garantire il corretto riconoscimento del dispositivo.

    ![device identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/device-identity.png){class="glboxshadow"}

- **Language**: Imposta la lingua della console su cinese o inglese.

- **Color Mode**: Imposta il tema su Light o Dark.

- **Time Zone**: Personalizza il fuso orario della console KVM.

- **Reset KVM**: Ripristina le impostazioni di fabbrica del KVM con un clic.

### Rete { #network }

È possibile verificare e modificare i parametri di rete di Comet Q, come il nome host e l'indirizzo IP.

![settings-network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-network.png){class="glboxshadow"}

- **Hostname**: Consente di modificare il nome host del dispositivo direttamente nella console.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/hostname.png){class="glboxshadow"}

- **Wi-Fi**: Quando Comet Q si connette a una rete Wi-Fi, il suo indirizzo IP Wi-Fi viene visualizzato qui. Fare clic sull'SSID Wi-Fi o sulla freccia a destra per visualizzare i dettagli della connessione, tra cui SSID, indirizzo IP assegnato, gateway e indirizzo MAC usato da Comet Q.

    ![wifi config](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/wifi-config.png){class="glboxshadow"}

    Per collegarlo a un'altra rete Wi-Fi, fare clic su **Switch Wi-Fi** e selezionare una rete dall'elenco di quelle disponibili.

## Strumenti { #toolbox }

Nella console web, aprire **Toolbox**. La pagina comprende tre sezioni:

- [Appunti](#clipboard)
- [Scorciatoie](#shortcut)
- [Terminale](#terminal)

### Appunti { #clipboard }

Gli appunti consentono di incollare facilmente testo dal dispositivo di controllo al dispositivo controllato, senza trasferire file.

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-clipboard.png){class="glboxshadow"}

### Scorciatoie { #shortcut }

Le scorciatoie permettono di eseguire le azioni più rapidamente senza usare la tastiera virtuale, risparmiando tempo nelle attività quotidiane. Qui sono disponibili alcune scorciatoie comuni.

![toolbox-shortcut1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut1.png){class="glboxshadow"}

Fare clic su **Modify** per modificare le opzioni delle scorciatoie secondo necessità.

![toolbox-shortcut2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut2.png){class="glboxshadow"}

### Terminale { #terminal }

È possibile accedere al terminale di Comet Q per eseguire configurazioni avanzate. Fare clic su **Access**.

![toolbox-terminal1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal1.png){class="glboxshadow"}

Si aprirà il terminale GLKVM.

![toolbox-terminal2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal2.png){class="glboxshadow"}

## Supporti virtuali { #virtual-media }

Nella console web, aprire **Virtual Media**. Comet Q può emulare un'unità USB di lettura e scrittura, consentendo di condividere e gestire file tra il dispositivo di controllo e quello controllato.

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-media.png){class="glboxshadow"}

### Condivisione di file { #file-sharing }

**Per condividere file dal dispositivo di controllo al dispositivo controllato, seguire questi passaggi.**

1. Trascinare i file nel riquadro o fare clic al suo interno per caricarli dal dispositivo di controllo, oppure caricarli tramite URL.

    Dopo il caricamento, i file verranno visualizzati come segue.

    ![file-sharing1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing1.png){class="glboxshadow"}

2. Fare clic su **Mount To Remote** -> **File Sharing**.

    ![file-sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing2.png){class="glboxshadow"}

3. Nella console comparirà una finestra con le istruzioni per la condivisione dei file, come mostrato di seguito.

    ![file-sharing3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing3.png){class="glboxshadow"}

4. Attendere un momento: sullo schermo potrebbe comparire automaticamente un'unità denominata **"GLKVM"**. I file caricati in precedenza dal dispositivo di controllo su Comet Q saranno ora condivisi con il dispositivo controllato. Da quest'ultimo sarà possibile visualizzare, spostare o eliminare i file presenti nell'unità.

    ![file-sharing4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing4.png){class="glboxshadow"}

    **Suggerimento**: Se l'unità non compare automaticamente, aprire **This PC** sul dispositivo controllato.

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/thispc.png){class="glboxshadow"}

    Individuare quindi l'unità denominata **GLKVM**. Da qui è possibile visualizzare, spostare o eliminare i file presenti nell'unità.

5. Per interrompere la condivisione, fare clic su **Virtual Media** nella barra degli strumenti, quindi su **Stop Sharing**.

    ![stop sharing1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing1.png){class="glboxshadow"}

**Per condividere file dal dispositivo controllato al dispositivo di controllo, seguire questi passaggi.**

1. Sul dispositivo controllato, spostare o copiare i file da condividere nell'unità **GLKVM**.

    Nell'esempio, un file PDF denominato "gl-rm10_datasheet" è stato spostato dal desktop del dispositivo controllato all'unità **GLKVM**.

    ![file-sharing5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing5.png){class="glboxshadow"}

2. Tornare alla console di Comet Q, fare clic su **Virtual Media** nella barra degli strumenti, quindi su **Stop Sharing**.

    ![stop sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing2.png){class="glboxshadow"}

3. Il file verrà visualizzato in **Virtual Media**, come mostrato di seguito. Sarà quindi possibile scaricarlo da Comet Q sul dispositivo di controllo.

    ![file sharing6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing6.png){class="glboxshadow"}

### Formattazione del disco { #format-disk }

È possibile formattare il disco o disabilitare i supporti virtuali con un clic.

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/format-disable.png){class="glboxshadow"}

- **Format**: Cancella tutti i dati sul disco e reinizializza la struttura del file system.

- **Disable**: Disabilitare i supporti virtuali riavvia immediatamente il dispositivo KVM.

## Centro applicazioni { #apps-center }

Nella console web, aprire **Apps Center** per accedere alle applicazioni integrate.

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} è un servizio VPN mesh basato su WireGuard che crea reti private peer-to-peer crittografate tra dispositivi, senza port forwarding o configurazioni complesse del firewall.

Comet Q integra Tailscale e consente l'accesso remoto tramite la sua rete virtuale.

È sufficiente associare Comet Q e il dispositivo di controllo allo stesso account Tailscale. Si potrà quindi accedere a Comet Q da remoto inserendo il suo **IP virtuale Tailscale** nel browser del dispositivo di controllo, senza installare l'app GLKVM. Per i dettagli, consultare [questa guida](../../faq/remote_access_via_tailscale.md){target="_blank"}.

Dopo l'associazione, la console mostra l'account Tailscale collegato e rende disponibili funzioni avanzate, tra cui Exit Node e Subnet Routes.

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} crea reti virtuali overlay crittografate che collegano dispositivi distribuiti in tutto il mondo come se fossero sulla stessa rete locale.

Comet Q integra ZeroTier e consente l'accesso remoto tramite la sua rete virtuale.

È sufficiente collegare Comet Q e il dispositivo di controllo alla stessa rete ZeroTier. Si potrà quindi accedere a Comet Q da remoto inserendo il suo **IP ZeroTier** nel browser del dispositivo di controllo, senza installare l'app GLKVM. Per i dettagli, consultare [questa guida](../../faq/remote_access_via_zerotier.md){target="_blank"}.

Dopo l'associazione, la console mostra il Network ID e l'IP virtuale ZeroTier.

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-zerotier-enabled.png){class="glboxshadow"}

## Assistenza { #help }

Nella console web, aprire **Help**. Qui sono disponibili ulteriori informazioni su GL.iNet KVM e la documentazione di assistenza; è inoltre possibile esportare i log per la risoluzione dei problemi.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/help.png){class="glboxshadow"}

## Barra degli strumenti { #toolbar }

Nella console web, accedere all'angolo superiore destro per usare i seguenti strumenti:

- [Comprimere la barra degli strumenti](#collapse)
- [Schermo intero](#fullscreen)
- [Aggiornamento](#upgrade)
- [Servizio cloud](#cloud-service)
- [Sicurezza](#security)
- Reboot
- Logout

### Compressione della barra { #collapse }

Fare clic sull'icona della freccia rivolta verso l'alto nell'angolo superiore destro per comprimere la barra degli strumenti.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse1.png){class="glboxshadow"}

Quando la barra degli strumenti è compressa, fare clic sulla freccia rivolta verso il basso in alto per espanderla.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse2.png){class="glboxshadow"}

### Schermo intero { #fullscreen }

Fare clic sull'icona a forma di quadrato nell'angolo superiore destro per passare alla modalità a schermo intero.

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen1.png){class="glboxshadow"}

Per uscire dalla modalità a schermo intero, tenere premuto il tasto **Esc** oppure fare clic sull'icona di uscita a forma di griglia nell'angolo superiore destro.

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen2.png){class="glboxshadow"}

### Aggiornamento { #upgrade }

Fare clic sulla versione del firmware nell'angolo superiore destro per verificare la disponibilità di aggiornamenti.

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade1.png){class="glboxshadow"}

Nella finestra che si apre è possibile eseguire un aggiornamento online se è disponibile un firmware più recente. In alternativa, scaricare il firmware più recente dal [centro download del firmware](https://dl.gl-inet.com/kvm){target="_blank"} ed eseguire un aggiornamento locale secondo necessità.

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade2.png){class="glboxshadow"}

### Servizio cloud { #cloud-service }

GL.iNet KVM Cloud consente di accedere al dispositivo controllato da remoto. Per i dettagli, consultare [questa guida](../../faq/remote_access_via_cloud.md){target="_blank"}.

Dopo aver associato Comet Q al cloud, la console mostrerà lo stato del cloud come segue.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/cloud.png){class="glboxshadow"}

### Sicurezza { #security }

La sezione Security consente di modificare la password di amministrazione, abilitare l'autenticazione a due fattori e personalizzare il certificato TLS.

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/security.png){class="glboxshadow"}

- Change Admin Password

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/admin-password.png){class="glboxshadow" width="434"}

- 2FA: Abilitare l'autenticazione a due fattori per proteggere l'account.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/2fa.png){class="glboxshadow"}

- TLS Certificate

    Per l'accesso tramite browser, il sistema utilizza il certificato predefinito preinstallato. Per personalizzare il certificato TLS, fare clic su **TLS Certificate** nell'angolo superiore destro della console, selezionare **Custom Certificate** e caricare il **file del certificato e il file della chiave privata**.

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/tls-certificate.png){class="glboxshadow"}
