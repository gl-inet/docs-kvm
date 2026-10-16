# Firmware v1.9

Questa versione introduce nuove funzionalità, migliora l'interazione, rafforza la protezione della privacy e rende le connessioni di rete più affidabili, per un'esperienza KVM remota più completa, stabile e sicura.

Scarica il firmware più recente dal [centro download del firmware](https://dl.gl-inet.com/kvm){target="_blank"}

## Modalità di latenza

Questo firmware introduce **Latency Mode**, che bilancia la reattività dei comandi e la fluidità del video. Puoi impostarla su Lowest Latency o Smooth Display per ottimizzare le prestazioni del controllo remoto.

![Modalità di latenza](https://static.gl-inet.com/docs/kvm/features_update/1.9/latency_mode.png){class="glboxshadow" width="360"}

- Lowest Latency: riduce al minimo la latenza dei comandi per una risposta più rapida di tastiera e mouse.
- Smooth Display: ottimizza la visualizzazione per eliminare scatti e perdita di fotogrammi e garantire una riproduzione fluida.

## Usabilità del mouse

La nuova opzione **Primary Button** migliora l'usabilità del mouse. Puoi impostare il pulsante sinistro o destro come pulsante principale in base alle tue abitudini.

![Pulsante principale](https://static.gl-inet.com/docs/kvm/features_update/1.9/primary_button.png){class="glboxshadow" width="360"}

## Schermo del dispositivo

Puoi personalizzare le impostazioni **Screen Display** del KVM tramite il touchscreen, tra cui blocco schermo, sfondo, formato dell'ora (24 ore / 12 ore) e formato della data. Questa funzionalità è disponibile esclusivamente sui modelli dotati di touchscreen.

Inoltre, puoi configurare rapidamente strumenti per reti overlay come Tailscale e NetBird direttamente dal touchscreen con pochi tocchi, una possibilità non disponibile nelle versioni precedenti del firmware.

![Schermo del dispositivo](https://static.gl-inet.com/docs/kvm/features_update/1.9/screen_display.png){class="glboxshadow" width="360"}

## Lingua

Le versioni precedenti del firmware supportavano solo cinese e inglese; questa versione aggiunge il supporto nativo del **giapponese** per migliorare l'accessibilità per gli utenti giapponesi.

![Lingua](https://static.gl-inet.com/docs/kvm/features_update/1.9/language.png){class="glboxshadow" width="360"}

## Estensioni

Questa versione integra [NetBird](https://netbird.io/){target="_blank"}, una piattaforma di rete zero trust open source per creare reti private sicure in ambito domestico e aziendale. Basata su WireGuard®, questa soluzione overlay consente di accedere in modo sicuro al KVM da qualsiasi luogo tramite reti virtuali NetBird. Consulta [questa guida](../faq/remote_access_via_netbird.md){target="_blank"} per le istruzioni di configurazione.

![NetBird](https://static.gl-inet.com/docs/kvm/features_update/1.9/netbird.png){class="glboxshadow"}

## Altri miglioramenti

- Programma firmware beta: gli utenti possono aderire al programma beta per provare le funzionalità prima del rilascio.

- Riconoscimento del testo: grazie al riconoscimento ottico dei caratteri (OCR), questo strumento permette di acquisire il testo da qualsiasi area selezionata dello schermo remoto. Le lingue supportate sono cinese, inglese e modalità bilingue cinese-inglese. Consulta [questa guida](../tutorials/how_to_capture_text_from_remote_screen.md) per i dettagli.

- Fuso orario basato sulla città: imposta il fuso orario selezionando una città.

- Sicurezza delle sessioni di accesso: i token di accesso scadono ora 12 ore dopo la fine della sessione (in precedenza erano permanenti).

- Sicurezza dei log di sistema: è stato introdotto il mascheramento dei dati sensibili in tutti i log di sistema.

---

Hai ancora domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
