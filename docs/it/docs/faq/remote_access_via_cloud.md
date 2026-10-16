# Come accedere al KVM da remoto tramite il cloud {#how-to-access-kvm-remotely-via-cloud}

Prima di iniziare, assicurati che:

- Il dispositivo controllato sia collegato correttamente al KVM.

- Il KVM sia collegato a una rete stabile.

- Tu possa accedere al KVM localmente, perché l'associazione al cloud deve essere eseguita all'interno della rete locale.

Segui i passaggi indicati di seguito per accedere da remoto al KVM e al dispositivo controllato tramite il servizio cloud.

## Associare il KVM al cloud {#bind-your-kvm-to-the-cloud}

Puoi associare il KVM al cloud in due modi: associazione standard o associazione tramite codice dinamico.

- **Associazione standard**: fai clic su "Bind To KVMCloud" nella console del KVM per essere reindirizzato alla pagina di associazione con il token. Accedi al tuo account cloud e conferma le informazioni del dispositivo per completare l'associazione.

- **Associazione tramite codice dinamico**: fai clic su "Bind With Code" nella console del KVM per generare casualmente un codice dinamico di 8 cifre. Accedi al tuo account cloud e inserisci il codice per completare l'associazione.

### Associazione standard {#regular-binding}

Accedi localmente al KVM tramite indirizzo IP o nome di dominio e vai su **Cloud Service** nell'angolo in alto a destra. Fai clic su **Bind To Cloud**.

![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

Verrai reindirizzato a una pagina di accesso. Inserisci le credenziali del tuo account GL.iNet e fai clic su **Log In**.

![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

Conferma le informazioni del dispositivo e fai clic su **Bind**.

![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

Attendi un momento affinché il dispositivo venga associato al tuo account, quindi fai clic su **Done**.

![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

### Associazione tramite codice dinamico {#dynamic-code-binding}

Nota: aggiorna il firmware del KVM alla versione 1.7 prima di usare questa funzione.

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

    Il dispositivo verrà quindi associato al tuo account cloud.

## Accesso remoto tramite il cloud {#remote-access-via-cloud}

Apri un browser, ad esempio Google Chrome, e digita `glkvm.com` nella barra degli indirizzi. Nella pagina di accesso, accedi con il tuo account GL.iNet.

![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

Dopo l'accesso, vedrai i dispositivi associati al tuo account. Fai clic sul dispositivo a cui vuoi accedere da remoto.

![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

Nella nuova pagina web, inserisci la password di amministratore per accedere.

![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

Ora puoi accedere da remoto al KVM e al dispositivo controllato tramite il cloud.

![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
