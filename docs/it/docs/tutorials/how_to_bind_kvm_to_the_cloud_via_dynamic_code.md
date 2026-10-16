# Come associare il KVM al cloud tramite codice dinamico {#how-to-bind-kvm-to-the-cloud-via-dynamic-code}

> Nota: aggiorna il firmware del KVM alla versione 1.7 prima di usare questa funzione.

Questo tutorial spiega come associare facilmente il KVM GL.iNet al cloud tramite un codice dinamico.

## Procedura di associazione {#binding-steps}

1. Accedi localmente al KVM GL.iNet tramite nome di dominio o indirizzo IP. Fai clic [qui](../faq/local_access_via_browser.md) per i dettagli.

2. Dopo l'accesso, vai su **Cloud Service** nell'angolo in alto a destra e fai clic su **Bind With Code**.

    ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Verrà generato casualmente un codice dinamico di 8 cifre per l'associazione, valido per 60 secondi. Fai clic sul codice per copiarlo.

    ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Visita [https://glkvm.com/](https://glkvm.com/){target="_blank"} e accedi con il tuo account cloud GL.iNet.

    ![bind with code 3](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. Dopo l'accesso, la pagina apparirà come mostrato di seguito.

    ![bind with code 4](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Fai clic su **Add Device** e seleziona **Bind with Code**.

    ![bind with code 5](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. Nella finestra visualizzata, inserisci il codice dinamico di 8 cifre e fai clic su **Bind**.

    ![bind with code 6](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Nota**: il codice dinamico è valido per 60 secondi. Se scade, torna alla console del KVM e fai clic su **Regenerate Code** per ottenerne uno nuovo.

    ![regenerate code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

7. Il dispositivo verrà associato al tuo account cloud. Fai clic su **Done**.

    ![bind with code 7](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_7.png){class="glboxshadow"}

    Vedrai il KVM nell'elenco dei dispositivi. Ora puoi accedervi da remoto tramite il servizio cloud.

    ![bind with code 8](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_8.png){class="glboxshadow"}

8. Fai clic sul dispositivo a cui vuoi accedere da remoto. Nella nuova pagina web, inserisci la password di amministratore per accedere.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Potrai quindi accedere da remoto al KVM e al dispositivo controllato tramite il cloud.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

## Domande frequenti {#faq}

1. **D: Per quanto tempo è valido il codice dinamico? Cosa devo fare se scade?**

    R: il codice dinamico è valido per 60 secondi. Se scade, torna alla console del KVM e fai clic su **Regenerate Code** per ottenerne uno nuovo.

    ![regenerate code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

2. **D: Cosa fare se non è possibile generare il codice dinamico?**

    R: la mancata generazione del codice dinamico potrebbe dipendere da una rete instabile o dalla configurazione DNS a monte.

    - Verifica che la rete sia stabile oppure passa a un'altra rete e riprova.

    - Modifica le impostazioni DNS a monte e genera nuovamente il codice.

    Se il problema persiste, contatta l'assistenza all'indirizzo [support@gl-inet.com](mailto:support@gl-inet.com).

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
