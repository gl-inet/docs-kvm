# Cosa fare se l'associazione del dispositivo all'app GLKVM non riesce {#what-should-i-do-if-i-failed-to-bind-device-to-the-glkvm-app}

L'[app GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} consente di accedere al dispositivo controllato da remoto tramite il dispositivo di controllo. Installa l'app sul dispositivo di controllo e associa il KVM GL.iNet per accedere al dispositivo controllato da qualsiasi luogo e in qualsiasi momento.

L'associazione del dispositivo può tuttavia non riuscire per diversi motivi.

Fai clic sul messaggio di errore corrispondente per visualizzare le soluzioni.

??? "Binding failed, unable to obtain basic KVM device information."

    ![binding failed device info error](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_device_info_error.png){class="glboxshadow"}

    1. Controlla lo stato del LED. Assicurati che sia bianco fisso e che il dispositivo KVM sia connesso a Internet.
    2. Riavvia il dispositivo KVM, attendi 2 minuti e prova ad associarlo di nuovo.
    3. Se aggiungi il dispositivo tramite il codice S/N, verifica di aver inserito il valore corretto.
    4. Segui i passaggi indicati di seguito per controllare la rete tramite il comando **Ping**.

        1. Collega il dispositivo di controllo alla stessa rete del KVM.

        2. Apri un browser sul dispositivo di controllo, preferibilmente Chrome o Edge, e digita `glkvm.local` nella barra degli indirizzi. Inserisci la password di amministratore per accedere.

            ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. Dopo l'accesso, vai su **Toolbox** -> **Terminal** e fai clic su **Access** per accedere al terminale.

            ![access terminal](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Esegui un ping a `google.com` per verificare lo stato della rete.

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Se la rete funziona correttamente, otterrai il risultato mostrato di seguito.

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Se la rete è instabile o non disponibile, contatta il tuo fornitore di servizi Internet o l'assistenza del router.

??? "Device network error, binding failed."

    ![binding failed network error](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_network_error.png){class="glboxshadow"}

    1. Controlla lo stato del LED. Assicurati che sia bianco fisso e che il dispositivo KVM sia connesso a Internet.
    2. Riavvia il dispositivo KVM, attendi 2 minuti e prova ad associarlo di nuovo.
    3. Assicurati che il servizio cloud sia attivo.

        Il servizio cloud è attivo per impostazione predefinita, ma se lo hai disattivato manualmente, non potrai associare nuovamente il dispositivo all'app GLKVM. Accedi localmente al dispositivo KVM tramite nome di dominio o indirizzo IP per riattivare il servizio cloud.

    4. Segui i passaggi indicati di seguito per controllare la rete tramite il comando **Ping**.

        1. Collega il dispositivo di controllo alla stessa rete del KVM.

        2. Apri un browser sul dispositivo di controllo, preferibilmente Chrome o Edge, e digita `glkvm.local` nella barra degli indirizzi. Inserisci la password di amministratore per accedere.

            ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. Dopo l'accesso, vai su **Toolbox** -> **Terminal** e fai clic su **Access** per accedere al terminale.

            ![access terminal](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Esegui un ping a `google.com` per verificare lo stato della rete.

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Se la rete funziona correttamente, otterrai il risultato mostrato di seguito.

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Se la rete è instabile o non disponibile, contatta il tuo fornitore di servizi Internet o l'assistenza del router.

??? "Binding failed, KVM is already bound by others."

    ![binding failed bound by others](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_bound_by_others.png){class="glboxshadow"}

    Questo messaggio indica che il dispositivo KVM è già associato a un altro account.

    1. Verifica se lo hai associato a un altro tuo indirizzo e-mail. Se hai altri account, prova ad accedere con quelli.

    2. Se aggiungi il dispositivo tramite il codice S/N, verifica di aver inserito il valore corretto.

??? "Incorrect Dynamic Binding Code. You have 4 attempts remaining."

    ![incorrect binding code](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_binding_code.png){class="glboxshadow"}

    Questo messaggio indica che hai inserito un codice di associazione non valido o scaduto.

    1. Accedi localmente alla console di amministrazione del KVM, vai su **Cloud Service** nell'angolo in alto a destra e fai clic su **Bind with Code** per ottenere un codice di associazione dinamico.

    2. Sul modello GL-RM10 (Comet Pro), puoi ottenere il codice anche dal touchscreen. Scorri fino alla schermata **Cloud Service** e tocca **Generate Binding Code** per visualizzare un codice di associazione dinamico. Inseriscilo nell'app GLKVM per completare l'associazione.

        ![generate binding code](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_code_screen.png){class="glboxshadow"}

    3. Se il codice di associazione scade, fai clic su **Regenerate** per ottenerne uno nuovo.

??? "Incorrect Device ID. You have 4 attempts remaining."

    ![incorrect device id](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_device_id.png){class="glboxshadow"}

    Questo messaggio indica che hai inserito un Device ID errato.

    1. Controlla l'etichetta sul fondo del dispositivo per trovare il Device ID corretto.

    2. Se non puoi controllare l'etichetta sul fondo, prova ad associare il dispositivo tramite accesso locale.

        Accedi localmente alla console di amministrazione del KVM, vai su **Cloud Service** nell'angolo in alto a destra e fai clic su **Bind To KVM Cloud**. Verrai reindirizzato alla pagina di associazione con un token univoco. Accedi con il tuo account cloud e conferma le informazioni del dispositivo per completare l'associazione.

??? "Altro"

    Verifica se è attiva una VPN sul dispositivo di controllo su cui è installata l'app GLKVM.

    Disattiva qualsiasi software VPN o proxy, inclusi AstroWarp, Tailscale e ZeroTier, quindi prova ad associare nuovamente il KVM all'app GLKVM.

Se il problema persiste, contattaci all'indirizzo [support@gl-inet.com](mailto:support@gl-inet.com) indicando il modello del dispositivo, la versione del firmware e l'indirizzo MAC.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
