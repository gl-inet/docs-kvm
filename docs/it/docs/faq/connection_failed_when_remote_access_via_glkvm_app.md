# Connessione non riuscita durante l'accesso remoto tramite l'app GLKVM {#connection-failed-when-remote-access-via-glkvm-app}

Durante l'accesso remoto tramite l'app GLKVM, può capitare che il dispositivo KVM risulti Online nell'app, ma che, facendo clic su di esso, la connessione rimanga bloccata su "Connecting".

![device online](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/device_online.png){class="glboxshadow"}

![connecting](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connecting.png){class="glboxshadow"}

Guida alla risoluzione dei problemi:

1. Assicurati che la connessione di rete sia stabile.

    Verifica che il KVM disponga di una connessione Internet stabile. Il LED bianco fisso indica che la connessione di rete funziona normalmente.

2. Controlla le regole del firewall di rete.

    Disattiva temporaneamente il firewall locale oppure aggiungi i domini di GL.iNet (ad esempio glkvm.com) all'elenco dei domini consentiti dal firewall. Dopo aver applicato le modifiche, riprova a connetterti.

    Di seguito sono riportati, come riferimento, i passaggi per modificare le regole del firewall su una rete Sky.

    ??? note "Rete Sky (ad esempio Sky Max Hub)"

        Il sistema di sicurezza della rete Sky potrebbe identificare il dominio `glkvm.com` come un sito sospetto e bloccarne l'accesso. Puoi rimuovere le restrizioni tramite l'app Sky.<br>

        1. Apri l'app MySky, vai su **Broadband** -> **Advanced Security** e verifica se sono presenti restrizioni sui domini di GL.iNet.

            ![mysky-1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-1.png){class="glboxshadow"}

        2. Se il dominio è bloccato, fai clic sulla freccia verso il basso per visualizzare i dettagli, quindi seleziona **Allow Access** per rimuovere il blocco.

            ![mysky-2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-2.png){class="glboxshadow" width="300"}

3. Disattiva VPN e proxy sul dispositivo di controllo.

    Assicurati che sul dispositivo che esegue l'app GLKVM non siano attivi servizi VPN o proxy, poiché potrebbero interferire con la connessione.

4. Se possibile, riavvia il KVM.

    Se possibile, riavvia fisicamente il dispositivo KVM per risolvere eventuali problemi temporanei di rete o software.

    Se non ti trovi vicino al dispositivo KVM, puoi riavviarlo da remoto tramite l'app GLKVM:

    1. Nell'elenco dei dispositivi, fai clic su **Manage** nell'angolo in alto a destra del dispositivo.

        ![app reboot 1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_1.png){class="glboxshadow"}

    2. Fai clic su **More** e seleziona **Reboot**.

        ![app reboot 2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_2.png){class="glboxshadow"}

Ulteriori indicazioni tecniche:

1. Assicurati che la risoluzione DNS dei domini funzioni correttamente.

2. Verifica che il traffico in uscita verso le porte standard del KVM e dell'accesso remoto non sia bloccato.

3. Per le reti aziendali, consulta gli amministratori IT riguardo a eventuali criteri di filtraggio del traffico.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
