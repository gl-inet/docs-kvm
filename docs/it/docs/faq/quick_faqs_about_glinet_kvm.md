# Domande frequenti sul KVM GL.iNet {#quick-faqs-about-glinet-kvm}

Questa raccolta di domande e risposte sul KVM GL.iNet fornisce risposte rapide ad alcuni dei dubbi più comuni.

## Informazioni di base {#basic-information}

**D1. Quali dispositivi può controllare il KVM GL.iNet?**

R1. Il KVM GL.iNet può controllare qualsiasi dispositivo dotato di uscita HDMI e ingresso USB, come portatili, PC desktop, Raspberry Pi, mini PC e altri dispositivi.

Inoltre, Comet Q (GL-RMQ1) può controllare qualsiasi dispositivo la cui porta USB-C supporti DisplayPort Alt Mode per l'uscita video, senza richiedere una porta HDMI. Sono inclusi, tra gli altri, alcuni iPhone, iPad, telefoni Android, MacBook, Mac mini e la maggior parte dei portatili Windows recenti. Fai clic [qui](../user_guide/gl-rmq1/product_overview.md#compatibility) per i dettagli.

---

**D2. Devo installare del software per usare il KVM GL.iNet?**

R2. Non è necessario installare alcun software sul dispositivo controllato, che può eseguire Windows, macOS, ChromeOS, Linux o altri sistemi operativi.

Sul dispositivo di controllo, la necessità di installare un software dipende dal metodo scelto per accedere al KVM.

??? "Nearby Control (solo per Comet 5G)"

    **Nota**: questo metodo è disponibile solo su Comet 5G (GL-RM10RC).

    Comet 5G offre la funzione Wi-Fi Nearby Control, che consente una rapida gestione locale senza collegamenti cablati. Imposta la modalità di rete Wi-Fi di Comet 5G su AP per generare un SSID Wi-Fi univoco. Collegati a questo SSID per accedere in modo sicuro alla console di Comet 5G. Fai clic [qui](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control) per i dettagli.

    L'attivazione della modalità AP disconnette Comet 5G dalla rete Wi-Fi a monte e consente solo l'accesso nelle vicinanze, senza connettività Internet.

??? "Local Control (solo per Comet X)"

    **Nota**: questo metodo è disponibile solo su Comet X (GL-RM4PE).

    Comet X dispone di una porta HDMI OUT e di due porte USB aggiuntive, ideali per la risoluzione dei problemi, la configurazione e l'installazione del sistema operativo in locale. Collega monitor, mouse e tastiera per controllare direttamente l'hardware in locale, senza configurazioni aggiuntive. Fai clic [qui](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control) per i dettagli.

??? "Accesso LAN"

    Se vuoi accedere al KVM dalla stessa rete locale (LAN), non è necessario installare software sul dispositivo di controllo.

    Apri un browser sul dispositivo di controllo e digita l'indirizzo IP del KVM oppure `glkvm.local` nella barra degli indirizzi per accedere localmente al KVM.

    Fai clic [qui](local_access_via_browser.md){target="_blank"} per i dettagli.

??? "Accesso remoto"

    - **App GLKVM**

        Se il dispositivo di controllo esegue Windows, macOS, Android o iOS, puoi installare l'[app GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} per accedere al KVM da remoto e, quindi, al dispositivo controllato.

        Fai clic [qui](remote_access_via_glkvm_app.md){target="_blank"} per i dettagli.

    - **Servizio cloud**

        Questo metodo è adatto a chi non può o non vuole installare l'app GLKVM.

        Associa il KVM al servizio cloud, quindi digita `glkvm.com` in un browser web sul dispositivo di controllo per accedere al KVM da remoto e, quindi, al dispositivo controllato, senza installare l'app GLKVM.

        Fai clic [qui](remote_access_via_cloud.md){target="_blank"} per i dettagli.

    - **Tailscale**

        Questo metodo è adatto a chi non può o non vuole usare l'app GLKVM o il servizio cloud, ma richiede più passaggi.

        Associa il KVM e il dispositivo di controllo allo stesso account Tailscale, quindi digita l'IP virtuale Tailscale del KVM in un browser web sul dispositivo di controllo per accedere al KVM da remoto e, quindi, al dispositivo controllato.

        Fai clic [qui](remote_access_via_tailscale.md){target="_blank"} per i dettagli.

    - **ZeroTier**

        Questo metodo è adatto a chi non può o non vuole usare l'app GLKVM o il servizio cloud, ma richiede più passaggi.

        Aggiungi il KVM e il dispositivo di controllo alla stessa rete ZeroTier, quindi digita l'IP ZeroTier del KVM in un browser web sul dispositivo di controllo per accedere al KVM da remoto e, quindi, al dispositivo controllato.

        Fai clic [qui](remote_access_via_zerotier.md){target="_blank"} per i dettagli.

    - **NetBird**

        Questo metodo è adatto a chi non può o non vuole usare l'app GLKVM o il servizio cloud, ma richiede più passaggi.

        [NetBird](https://netbird.io/){target="_blank"} è una piattaforma di rete zero trust open source che consente di creare reti private sicure per uso domestico e aziendale. Basato su una rete overlay WireGuard®, NetBird permette di accedere in modo sicuro ai dispositivi da qualsiasi luogo e in qualsiasi momento.

        Il KVM GL.iNet integra NetBird e può essere associato alla sua rete virtuale per l'accesso remoto.

        Fai clic [qui](remote_access_via_netbird.md){target="_blank"} per i dettagli.

---

**D3. Come posso accedere al KVM GL.iNet?**

R3. In generale, puoi accedere al KVM GL.iNet localmente o da remoto con diversi metodi:

- [Accesso LAN tramite browser web](local_access_via_browser.md){target="_blank"}
- [Accesso remoto tramite servizio cloud](remote_access_via_cloud.md){target="_blank"}
- [Accesso remoto tramite app GLKVM](remote_access_via_glkvm_app.md){target="_blank"}
- [Accesso remoto tramite Tailscale](remote_access_via_tailscale.md){target="_blank"}
- [Accesso remoto tramite ZeroTier](remote_access_via_zerotier.md){target="_blank"}
- [Accesso remoto tramite NetBird](remote_access_via_netbird.md){target="_blank"}

Alcuni modelli di KVM GL.iNet supportano inoltre Nearby Control o Local Control, che consentono l'accesso sul posto senza collegarsi a un altro router.

- [Nearby Control (solo per Comet 5G)](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control){target="_blank"}
- [Local Control (solo per Comet X)](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control){target="_blank"}

---

**D4. Devo aprire porte esposte alla WAN per accedere da remoto al KVM GL.iNet?**

R4. No. Non occorre aprire porte né disporre di un IP pubblico.

---

**D5. L'app GLKVM supporta ChromeOS/Linux?**

R5. No. Al momento l'app GLKVM non può essere installata su ChromeOS o Linux.

Se il dispositivo di controllo esegue ChromeOS o Linux, non puoi installare l'app GLKVM e quindi non puoi usarla per accedere da remoto al dispositivo controllato.

Puoi tuttavia usare il <u>servizio cloud</u>, <u>Tailscale</u>, <u>ZeroTier</u> o <u>NetBird</u> per l'accesso remoto. Consulta la domanda D3 per i dettagli.

In alternativa, puoi accedere al KVM localmente tramite un browser web. Consulta la domanda D3 per i dettagli.

---

**D6. Comet (GL-RM1) può collegarsi a una rete wireless?**

R6. No. Comet (GL-RM1) non supporta le connessioni di rete wireless.

Per accedere a Internet deve essere collegato a un dispositivo di rete, ad esempio un router, tramite un cavo Ethernet.

Se preferisci un KVM che supporti il Wi-Fi, puoi considerare i seguenti modelli:

* [Comet Pro (GL-RM10)](https://www.gl-inet.com/products/gl-rm10/){target="_blank"}
* [Comet 5G (GL-RM10RC)](https://www.gl-inet.com/products/gl-rm10rc/){target="_blank"}
* [Comet Q (GL-RMQ1)](https://www.gl-inet.com/products/gl-rmq1/){target="_blank"}

---

## Controllo dell'alimentazione {#power-control}

**D1. Un KVM GL.iNet può accendere e spegnere da remoto il dispositivo controllato?**

R1. Il KVM GL.iNet consente di accendere e spegnere da remoto il dispositivo controllato con i seguenti metodi:

- Wake-on-LAN, servizio software integrato

- [Scheda ATX](../user_guide/gl-atx-board/index.md){target="_blank"}, venduta separatamente; non funziona con Comet Q.

- [FingerBot](../user_guide/gl-fgb-01/index.md){target="_blank"}, venduto separatamente; non funziona con Comet Q.

---

**D2. Come si usa la scheda ATX per controllare l'alimentazione da remoto?**

R2. Consulta la [guida utente della scheda ATX](../user_guide/gl-atx-board/index.md){target="_blank"}.

---

## Funzioni {#features}

!!! Tip "Suggerimento"

    Di seguito trovi le domande frequenti su alcune funzioni comuni. Per i dettagli completi, consulta la [guida utente](../user_guide/index.md) del modello corrispondente.

**D1. È obbligatorio usare il servizio cloud KVM?**

R1. No. Il servizio cloud è facoltativo.

Se non vuoi affidarti al cloud per l'accesso remoto, puoi usare strumenti di rete overlay di terze parti, come Tailscale, ZeroTier e NetBird.

---

**D2. Posso usare un solo KVM GL.iNet per controllare più dispositivi?**

R2. I seguenti KVM GL.iNet possono controllare un solo dispositivo:

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)
* Comet Q (GL-RMQ1)

Comet X (GL-RM4PE), invece, può collegarsi a un massimo di quattro dispositivi contemporaneamente, anche se ne può controllare solo uno alla volta. Puoi passare rapidamente da un dispositivo all'altro tramite il pulsante fisico sul pannello anteriore quando sei sul posto oppure tramite la console remota quando sei lontano.

Comet X (GL-RM4PE) dispone di quattro canali indipendenti sul pannello posteriore. Ogni canale include una porta HDMI per la trasmissione video, una porta Type-C per i segnali di tastiera e mouse e una porta USB 2.0 per periferiche USB, ad esempio Fingerbot o la scheda ATX.

---

**D3. Che cos'è Wake-on-LAN?**

R3. Wake-on-LAN (WOL) è una tecnologia che consente di accendere o riattivare da uno stato a basso consumo un computer o un dispositivo tramite la rete. Funziona inviando un "magic packet" contenente l'indirizzo MAC del dispositivo di destinazione, che ne attiva l'avvio. Gli impieghi comuni includono l'amministrazione remota, le configurazioni di standby a risparmio energetico e la gestione centralizzata dei sistemi.

---

**D4. Il KVM GL.iNet supporta Mouse Jiggle?**

R4. Sì. Puoi attivare Mouse Jiggle nella console del KVM.

La funzione Mouse Jiggler simula piccoli movimenti periodici del mouse per impedire al computer, cioè al dispositivo controllato, di andare in sospensione a causa di un'inattività prolungata, ad esempio durante riunioni a distanza o la gestione di server.

---

**D5. Il KVM GL.iNet supporta l'audio bidirezionale?**

R5. Sì. Puoi attivare Speaker e Microphone nella console del KVM per ottenere una trasmissione audio bidirezionale.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
