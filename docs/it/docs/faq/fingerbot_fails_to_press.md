# Cosa fare se compare "Press Failed" quando usi Fingerbot? {#what-should-i-do-if-i-see-press-failed-when-using-fingerbot}

Se la console KVM mostra "Press Failed" quando usi Fingerbot, potrebbe esserci un problema di associazione tra Fingerbot e il dispositivo KVM.

Segui i passaggi qui sotto per rimuovere l'associazione esistente e associare nuovamente Fingerbot.

1. Accedi al KVM e vai su **Toolbox** -> **Terminal** -> **Access Terminal** per aprire il terminale.

2. Esegui i seguenti comandi in sequenza:

    ```
    bluetoothctl
    ```
    ```
    scan on
    ```

    ![open bluetoothctl](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/bluetoothctl.png){class="glboxshadow"}

    Attendi un momento, poi esegui `scan off` per interrompere la scansione.

3. Esegui `devices` per visualizzare tutti i dispositivi Bluetooth rilevati. Trova il tuo Fingerbot (indicato come FGB) e annota il suo indirizzo MAC.

    ![devices](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/devices.png){class="glboxshadow"}

4. Digita `exit` per uscire dalla sessione bluetoothctl. Quindi esegui il comando qui sotto per rimuovere il vecchio record di associazione. Sostituisci questo indirizzo MAC con l'indirizzo MAC effettivo del tuo Fingerbot.

    ```
    bluetoothctl remove E1:2D:B2:75:D5:BC
    ```

5. Associa nuovamente Fingerbot con il seguente comando. Sostituisci questo indirizzo MAC con l'indirizzo MAC effettivo del tuo Fingerbot.

    ```
    fingerbot pair E1:2D:B2:75:D5:BC
    ```

    ![repair fingerbot](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/repair.png){class="glboxshadow"}

    Se l'operazione riesce, nel terminale compare **Done**. Prova quindi a usare nuovamente Fingerbot.

6. Se il problema persiste, contattaci all'indirizzo [support@gl-inet.com](mailto:support@gl-inet.com) e fornisci le informazioni qui sotto per proseguire con la diagnosi.

    - L'output dei seguenti comandi:

        ```
        fingerbot action
        ```
        ```
        ls -l /
        ```

    - I log KVM più recenti, esportati da **Help** > **Export Log Files**.

        ![export logs](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/export_logs.png){class="glboxshadow"}

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
