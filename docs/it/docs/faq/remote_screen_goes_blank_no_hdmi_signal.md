# Cosa fare se lo schermo remoto diventa nero o non riceve il segnale HDMI {#what-should-i-do-if-the-remote-screen-goes-blank-or-shows-no-hdmi-signal}

Se, durante l'accesso al dispositivo controllato tramite KVM, lo schermo remoto diventa nero o non mostra alcun segnale HDMI, segui i passaggi indicati di seguito per individuare il problema.

![white screen](https://static.gl-inet.com/docs/kvm/faq/blank_screen/white_screen.png){class="glboxshadow"}
<small>(Schermo bianco)</small>

![black screen](https://static.gl-inet.com/docs/kvm/faq/blank_screen/black_screen.png){class="glboxshadow"}
<small>(Schermo nero)</small>

Per prima cosa, verifica se il problema riguarda la trasmissione video. Accedi al KVM, vai su **Settings** -> **Video** -> **Transfer** e imposta la modalità di trasferimento su **Direct**.

![change transfer](https://static.gl-inet.com/docs/kvm/faq/blank_screen/change_transfer.png){class="glboxshadow" width="360"}

Se il problema persiste, controlla una alla volta le possibili cause elencate di seguito.

## Controllare i collegamenti hardware {#check-hardware-connection}

1. **Cavo HDMI difettoso**

    Cavi HDMI usurati, connettori ossidati o interruzioni interne possono impedire la trasmissione del segnale. Sostituisci il cavo con un cavo HDMI di buona qualità.

    Puoi anche controllare lo stato del segnale HDMI nella console del KVM. Individua l'icona del monitor nell'angolo in basso a destra e verifica se mostra "No HDMI signal".

    ![no HDMI signal](https://static.gl-inet.com/docs/kvm/faq/blank_screen/no_hdmi_signal.png){class="glboxshadow"}

2. **Collegamento errato**

    Se il dispositivo controllato è un PC desktop, assicurati che la porta **HDMI IN** del KVM sia collegata all'uscita HDMI OUT della scheda grafica o della scheda madre. Verifica che il connettore sia inserito completamente e saldamente. Per i dispositivi con più uscite HDMI, ad esempio una sulla scheda grafica dedicata e una sulla scheda madre, prova un'altra porta.

    Se il dispositivo controllato è un portatile, assicurati che la porta **HDMI IN** del KVM sia collegata all'uscita HDMI OUT del portatile.

    Suggerimento: alcuni modelli KVM, come Comet Pro e Comet 5G, dispongono di due porte HDMI. Assicurati che il cavo HDMI proveniente dal dispositivo controllato sia inserito nella porta HDMI IN del KVM. Se è collegato a HDMI OUT, la console del KVM non rileverà alcun segnale HDMI.

3. **Uso errato degli adattatori**

    Se è necessario un adattatore HDMI, usa un adattatore **VGA-to-HDMI** per collegare il dispositivo controllato alla porta HDMI IN del KVM GL.iNet.

    Un adattatore HDMI-to-VGA usato per questo collegamento non trasmetterà correttamente il segnale video e causerà uno schermo vuoto.

    ![adapter comparison](https://static.gl-inet.com/docs/kvm/faq/blank_screen/adapter_comparison.png){class="glboxshadow"}

## Controllare le impostazioni del browser {#check-browser-settings}

Se accedi al dispositivo controllato tramite browser e lo schermo rimane vuoto, prova i metodi seguenti:

1. **Prova diversi browser.** Usa Chrome, Firefox, Edge o altri browser per capire se il problema riguarda un browser specifico.

2. **Disattiva le estensioni di protezione o controllo delle perdite WebRTC.** Se nel browser hai installato estensioni o componenti aggiuntivi che possono influire sulle connessioni WebRTC, disattivali e riprova. Puoi anche andare su Settings -> Privacy & Security del browser per verificare che le connessioni WebRTC siano consentite.

    ![webrtc](https://static.gl-inet.com/docs/kvm/faq/blank_screen/webrtc.png){class="glboxshadow"}

## Controllare lo stato e le impostazioni del dispositivo controllato {#check-controlled-device-status-and-settings}

1. **Dispositivo spento o in sospensione**

    Assicurati che il dispositivo controllato sia completamente acceso e non sia in sospensione o ibernazione a causa delle impostazioni di risparmio energetico. Se necessario, riattivalo con i pulsanti fisici.

2. **Problemi con i driver della scheda grafica del dispositivo controllato**

    Driver grafici mancanti o danneggiati possono impedire l'uscita video. Accedi localmente al dispositivo controllato e aggiorna o reinstalla i driver della scheda grafica.

3. **Collegamento errato tra grafica dedicata e integrata**

    Se il dispositivo controllato dispone sia di grafica dedicata sia integrata, assicurati che il cavo HDMI sia collegato alla porta grafica corretta. Ad esempio, se è installata una scheda grafica dedicata, collega il cavo HDMI alla sua porta.

4. **Impostazioni dello schermo anomale sul dispositivo controllato, caso poco frequente**

    Quando si collega al dispositivo controllato, il KVM GL.iNet regola automaticamente l'uscita video leggendo l'EDID del monitor per ottenere prestazioni ottimali. La configurazione EDID predefinita è adatta alla maggior parte delle situazioni e in genere non richiede modifiche.

    Se il dispositivo controllato è compatibile con i monitor standard, è improbabile che si presentino schermate vuote o problemi di visualizzazione accedendo tramite GLKVM. Alcune combinazioni specifiche, ad esempio un sistema Linux con un monitor ASUS, possono tuttavia causare questi problemi.

    Verifica che il dispositivo controllato sia compatibile con i monitor standard e se presenta problemi di compatibilità con un monitor specifico.

5. **Problema di risoluzione**

    Quando GLKVM è collegato ad alcuni sistemi operativi, ad esempio Proxmox VE Hypervisor, potrebbe non riuscire a negoziare correttamente la risoluzione disponibile, causando problemi di visualizzazione. Puoi risolverli regolando manualmente la risoluzione sul dispositivo controllato.

    Di seguito trovi, come riferimento, una guida per modificare la risoluzione di sistema su Proxmox VE Hypervisor.

    1. Apri il terminale PVE ed esegui il comando seguente per modificare il file `/etc/default/grub`.

        ```
        nano /etc/default/grub
        ```

    2. Aggiungi la riga seguente.

        ```
        GRUB_CMDLINE_LINUX_DEFAULT="quiet gfxpayload=text nomodeset"
        ```

    3. Rimuovi il carattere `#` per decommentare la riga `GRUB_GFXMODE` e imposta la risoluzione desiderata, ad esempio `1024x768`.

        ```
        GRUB_GFXMODE=1024x768
        ```

    4. Premi `Ctrl + O`, poi Invio per salvare la configurazione.

    5. Premi `Ctrl + X` per uscire dall'editor nano.

    6. Esegui il comando seguente per applicare la configurazione.

        ```
        update-grub
        ```

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
