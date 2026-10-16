# Firmware v1.10

Questa versione introduce WebRTC nativo, il monitoraggio dei dati in tempo reale, la gestione centralizzata dei dispositivi USB e un nuovo Settings Center. Migliora inoltre le prestazioni all'avvio, la sicurezza e la stabilità del microfono, per un'esperienza KVM remota più fluida e affidabile.

Scarica il firmware più recente dal [centro download del firmware](https://dl.gl-inet.com/kvm){target="_blank"}

## Modalità WebRTC (Native)

Questo firmware introduce la modalità **WebRTC (Native) Mode**. Utilizza la libreria Google WebRTC per migliorare le prestazioni dello streaming e offrire un controllo remoto in tempo reale più fluido.

![Modalità WebRTC](https://static.gl-inet.com/docs/kvm/features_update/1.10/webrtc_native_mode.png){class="glboxshadow" width=400}

## Statistiche di connessione

**Connection Stats** mostra le informazioni sulla connessione in tempo reale e i grafici dell'andamento, tra cui latenza di rete, jitter, percentuale di pacchetti persi, bitrate, frequenza dei fotogrammi e ritardo di riproduzione.

Fai clic sull'icona dell'elenco per visualizzare i dati della connessione in tempo reale e lo stato del dispositivo.

![Statistiche di connessione 1](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_1.png){class="glboxshadow"}

Fai clic sull'icona del grafico per visualizzare l'andamento di latenza di rete, jitter e percentuale di pacchetti persi.

![Statistiche di connessione 2](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_2.png){class="glboxshadow"}

## Centro impostazioni

Questa versione aggiunge un nuovo **Settings Center** che riunisce le impostazioni dei dispositivi USB, delle preferenze, della rete, della sicurezza, del cloud e del sistema. Le opzioni esistenti, come la configurazione del nome host, la gestione del cloud e gli aggiornamenti del firmware, sono ora più facili da trovare in un unico punto.

### Dispositivi USB

La pagina **USB Devices** offre la gestione centralizzata dei dispositivi USB emulati. Da questa pagina puoi attivare o disattivare le periferiche virtuali per migliorare la compatibilità con il computer controllato.

![Dispositivi USB](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_usb_devices.png){class="glboxshadow"}

- **USB Emulated Devices**: attiva o disattiva i dispositivi USB emulati, tra cui mouse, tastiera, microfono, videocamera e supporti virtuali. Alcuni dispositivi non possono essere attivati contemporaneamente. La disponibilità viene aggiornata automaticamente.

- **Device Identity**: personalizza o modifica l'identità con cui il KVM viene riconosciuto dal dispositivo controllato. L'EDID e l'identificazione del dispositivo rimangono sincronizzati: modificando uno dei due, l'altro viene aggiornato automaticamente per garantire il corretto riconoscimento del dispositivo.

### Preferenze

La pagina **Preferences** consente di gestire le preferenze di visualizzazione, le impostazioni di sistema e quelle dello schermo del dispositivo.

![Preferenze](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences**: configura la barra degli strumenti in modalità a schermo intero e la barra di stato in modalità finestra.

- **System Settings**: imposta il titolo della scheda del browser, la lingua dell'interfaccia, la modalità colore e il fuso orario.

- **Device Screen**: visualizza l'anteprima e configura lo schermo integrato del dispositivo, tra cui modalità di blocco schermo, formato dell'ora, formato della data e sfondo.

    **Nota**: questa funzionalità è disponibile solo sui modelli con schermo integrato.

### Rete

Puoi visualizzare e gestire le impostazioni di rete del dispositivo, tra cui nome host, connessione Ethernet e informazioni sulla rete wireless.

![Rete](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_network.png){class="glboxshadow"}

- **Hostname**: modifica il nome host del dispositivo direttamente dalla console. Questa funzionalità è stata introdotta nel firmware v1.7.0.

- **Ethernet Settings**: visualizza e configura la connessione Ethernet. Puoi usare DHCP per ottenere automaticamente le impostazioni di rete oppure selezionare **Static** per inserire manualmente l'indirizzo IP, la maschera di rete, il gateway e gli altri parametri richiesti.

- **Wireless**: indirizzo IP, gateway e indirizzo MAC vengono mostrati dopo che il dispositivo si è connesso a una rete Wi-Fi.

    **Nota**: la funzionalità Wireless è disponibile solo sui modelli supportati.

### Sicurezza

La pagina **Security** consente di modificare la password di amministratore, attivare l'autenticazione a due fattori e personalizzare il certificato TLS.

![Sicurezza](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_security.png){class="glboxshadow"}

- **Access Password**: gestisci la password di amministratore oppure attiva l'autenticazione a due fattori (2FA) per proteggere l'accesso al dispositivo.

- **TLS Certificate**: utilizza il certificato predefinito oppure carica un certificato personalizzato e la relativa chiave privata per l'accesso tramite browser.

### Cloud

I dispositivi possono essere associati ai servizi cloud tramite URL o codice per l'accesso e la gestione da remoto. Puoi anche scaricare l'app mobile, gestire la connessione o rimuovere l'associazione del dispositivo secondo necessità.

![Cloud](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_cloud.png){class="glboxshadow"}

### Sistema

In **System** puoi accedere alle opzioni di gestione del sistema, aggiornamento del firmware e assistenza.

![Sistema](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_system.png){class="glboxshadow"}

- **System**: riavvia il dispositivo o ripristina le impostazioni di fabbrica.

- **Upgrade**: attiva Beta Center per ricevere aggiornamenti beta del firmware oppure utilizza **Local Upgrade** per installare il firmware da un file locale.

- **Help & Support**: esporta i log del dispositivo per la risoluzione dei problemi e accedi a guide utente, domande frequenti e altri documenti di supporto.

## Altri miglioramenti

- **Prestazioni all'avvio**: avvio del dispositivo più rapido.

- **Criteri per le password**: requisiti rafforzati (almeno 10 caratteri di almeno due tipi diversi) per migliorare la sicurezza.

- **Indicatore Bloc Maiusc**: aggiunto un indicatore dello stato di Bloc Maiusc sul dispositivo controllato.

---

Hai ancora domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
