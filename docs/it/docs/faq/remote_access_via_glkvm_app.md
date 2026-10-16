# Come accedere al KVM da remoto tramite l'app GLKVM {#how-to-access-kvm-remotely-via-glkvm-app}

Prima di iniziare, assicurati che il dispositivo controllato sia collegato correttamente al KVM GL.iNet e che il KVM sia collegato a una rete stabile.

Segui i passaggi indicati di seguito per accedere da remoto al KVM e al dispositivo controllato tramite l'app GLKVM.

## Installazione e accesso {#install-and-log-in}

1. Installa l'[app GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} sul dispositivo di controllo.

2. Apri l'app GLKVM e accedi con il tuo account GL.iNet.

    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Se non disponi di un account GL.iNet, creane uno e poi accedi.

    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

## Associare il KVM {#bind-your-kvm}

Dopo l'accesso, la pagina apparirà come mostrato di seguito. Fai clic su **Add Device**.

Puoi associare il KVM in tre modi: Auto Discover, S/N Code e Dynamic Binding Code.

![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

### Auto Discover {#auto-discover}

Questa operazione deve essere eseguita all'interno della rete locale. Assicurati che il KVM e il dispositivo di controllo si trovino sulla stessa LAN.

1. Fai clic su **Auto Discover** per avviare la ricerca automatica dei dispositivi KVM disponibili.

    ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

2. Individua il KVM e inserisci il suo **Device ID** per associarlo al tuo account.

    ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

### S/N Code {#sn-code}

Questo metodo è adatto quando il KVM non viene rilevato o non si trova sulla stessa LAN, ma ne conosci il numero di serie (S/N).

1. Fai clic su **S/N Code**.

2. Nella finestra visualizzata, assegna un nome al dispositivo e inserisci il suo S/N, riportato sull'etichetta sul fondo del KVM.

    ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

### Dynamic Binding Code {#dynamic-binding-code}

Aggiorna il firmware del KVM alla v1.7 prima di usare questa funzione.

Questa operazione deve essere eseguita all'interno della rete locale. Assicurati che il KVM e il dispositivo di controllo si trovino sulla stessa LAN.

1. Accedi localmente al KVM tramite nome di dominio o indirizzo IP. Fai clic [qui](../faq/local_access_via_browser.md) per i dettagli.

2. Dopo l'accesso, vai su **Cloud Service** nell'angolo in alto a destra e fai clic su **Bind With Code**.

    ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Verrà generato casualmente un codice dinamico di 8 cifre per l'associazione, valido per 60 secondi. Fai clic sul codice per copiarlo.

    ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Torna all'app GLKVM, inserisci il codice di associazione dinamico e fai clic su **Bind**.

    ![dynamic code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

## Accesso remoto {#remote-access}

Quando il dispositivo KVM è associato al tuo account, nell'app apparirà come "Online".

![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

Fai clic sul dispositivo KVM. Si aprirà una nuova finestra e verrà avviata la connessione.

![connecting](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

Una volta stabilita la connessione, inserisci la password di amministratore per accedere.

![connected log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

Ora puoi accedere al dispositivo KVM e, tramite esso, al dispositivo controllato.

![connected access](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
