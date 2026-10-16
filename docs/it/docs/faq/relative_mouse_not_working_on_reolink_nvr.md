# Cosa fare se la modalità mouse relativo non funziona su Reolink NVR {#what-should-i-do-if-relative-mouse-mode-doesnt-work-on-reolink-nvr}

Quando usi il KVM GL.iNet per controllare un Reolink NVR, soprattutto un modello che non supporta due mouse, o alcuni computer datati, ad esempio quelli privi di interfacce USB, la modalità mouse relativo potrebbe non funzionare. I problemi più comuni sono il mancato funzionamento completo della modalità oppure il movimento del puntatore senza risposta ai clic.

La causa principale è un problema di compatibilità tra l'emulazione del mouse del KVM e le capacità limitate di dispositivi come Reolink NVR:

- **Prima del firmware v1.4.0**: il KVM era progettato per simulare un solo mouse. Il passaggio tra le modalità relativa e assoluta richiedeva il riavvio del KVM, ma funzionava correttamente con la maggior parte dei dispositivi datati o specializzati.

- **Dopo il firmware v1.4.0**: per consentire il passaggio immediato tra le modalità senza riavvio, il comportamento predefinito è stato modificato per simulare due mouse contemporaneamente, uno per la modalità relativa e l'altro per quella assoluta. Reolink NVR e alcuni computer datati non supportano due mouse, causando due problemi comuni:

    - La modalità mouse relativo non funziona affatto;
    - Il puntatore si muove, ma i clic non producono alcuna risposta.

Per risolvere il problema, puoi forzare la modalità mouse relativo dal terminale. Segui questi passaggi:

1. Accedi alla console del KVM e vai su **Toolbox** -> **Terminal**. Fai clic su **Access** per entrare nel terminale del KVM.

2. Apri il file di configurazione con il seguente comando:

    `vi /etc/kvmd/override.yaml`

3. Inserisci la seguente configurazione per forzare la modalità mouse relativo:

    ```
    kvmd:
        hid:
            mouse:
                absolute: false
    ```

4. Salva il file ed esci dall'editor.

5. Riavvia il dispositivo KVM per applicare le modifiche.

!!! note "Nota"

    1. Se il metodo precedente non funziona, prova a ripristinare una versione del firmware precedente alla v1.4, se disponibile, che supporti l'emulazione di un solo mouse e sia compatibile con i dispositivi meno recenti.

    2. L'app GLKVM per macOS non supporta la modalità mouse relativo a causa di limitazioni del motore del browser, che non supporta l'API requestPointerLock. Usa la console web.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
