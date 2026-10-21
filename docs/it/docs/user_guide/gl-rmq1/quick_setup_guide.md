# Configurazione rapida di Comet Q (GL-RMQ1) {#comet-q-gl-rmq1-quick-setup}

Guardare questo video o seguire i passaggi riportati di seguito per configurare Comet Q.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6-f-XFkgYoU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Collegamento dei dispositivi { #connect-devices }

Per chiarezza, il dispositivo A indica il dispositivo di controllo e il dispositivo B quello controllato.

![connect 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect1.png){class="glboxshadow"}

1. Collegare il cavo Type-C di Comet Q alla porta Type-C del dispositivo B.

    ![connect 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect2.png){class="glboxshadow"}

2. Se il dispositivo B è un dispositivo mobile con touchscreen, come uno smartphone o un tablet, abilitare prima i controlli di accessibilità. In questo modo Comet Q potrà usare il touchscreen.

    - iOS: **Settings** > **Accessibility** > **Touch** > Abilitare **AssistiveTouch**.

    - Android: Cercare **Mouse** o **Accessibility** in Settings. I percorsi dei menu variano in base alla marca e al modello del dispositivo.

    ![connect 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect3.png){class="glboxshadow" width="600"}

3. Seguire le istruzioni sullo schermo per completare la configurazione iniziale. Per i dettagli, consultare [questa guida](../gl-rmq1/product_overview.md#touchscreen).

    ![connect 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect4.png){class="glboxshadow"}

## Accesso locale { #local-access }

È possibile accedere a Comet Q sulla rete locale in due modi: tramite nome di dominio o indirizzo IP.

Prima dell'accesso, verificare che il dispositivo di controllo si trovi sulla stessa LAN di Comet Q.

### Dominio { #domain }

1. Aprire un browser sul dispositivo di controllo. Per una migliore compatibilità, si consiglia Chrome o Edge.

2. Inserire `glkvm.local` nella barra degli indirizzi. Si aprirà la pagina di accesso GLKVM. Inserire la password di amministrazione.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Nota**: Al primo accesso è necessario impostare la password di amministrazione.

3. Sarà quindi possibile accedere alla console di Comet Q in locale e al dispositivo controllato.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### Indirizzo IP { #ip-address }

1. Collegare Comet Q a una rete Wi-Fi e individuare il suo indirizzo IP sul touchscreen. In questo esempio, l'indirizzo IP è `192.168.8.197`.

2. Aprire un browser e inserire questo IP nella barra degli indirizzi. Si aprirà la pagina di accesso GLKVM. Inserire la password di amministrazione.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Nota**: Al primo accesso è necessario impostare la password di amministrazione.

3. Sarà quindi possibile accedere alla console di Comet Q in locale e al dispositivo controllato.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Accesso remoto { #remote-access }

È possibile accedere a Comet Q da remoto in diversi modi: tramite il servizio cloud, l'app GLKVM, Tailscale e ZeroTier.

### Servizio cloud { #cloud-service }

1. Associare il dispositivo a KVM Cloud. Questa operazione deve essere eseguita sulla rete locale.

    È possibile associare il KVM al cloud in due modi: associazione normale o tramite codice dinamico. Qui viene illustrata l'associazione normale. Per usare il codice dinamico, consultare [questa guida](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}.

    Per prima cosa, accedere a Comet Q in locale e aprire **Cloud Service** nell'angolo superiore destro. Fare clic su **Bind To Cloud**.

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    Si aprirà una pagina di accesso. Accedere con il proprio account cloud glinet.

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Confermare quindi le informazioni del dispositivo e fare clic su **Bind**.

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Attendere un momento per completare l'associazione di Comet Q all'account. Fare clic su **Done**.

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Accedere da remoto tramite il servizio cloud.

    Aprire un browser, ad esempio Google Chrome, e inserire `glkvm.com` nella barra degli indirizzi. Comparirà una pagina di accesso. Accedere con il proprio account glinet.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Dopo l'accesso compariranno i dispositivi associati all'account. Fare clic sul dispositivo a cui si desidera accedere da remoto.

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    Nella nuova pagina web, inserire la password di amministrazione per accedere.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Sarà quindi possibile accedere a Comet Q e al dispositivo controllato da remoto tramite il cloud, senza installare l'app.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

### App GLKVM { #glkvm-app }

1. Installare l'[app GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} sul dispositivo di controllo.

2. Accedere con il proprio account GL.iNet.

    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Se non si dispone di un account, registrarsi e poi accedere.

    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

3. Associare il dispositivo.

    Dopo l'accesso, la pagina apparirà come mostrato di seguito. Fare clic su **Add Device**.

    ![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

    È possibile associare il dispositivo in tre modi: Auto Discover, S/N Code e Dynamic Binding Code.

    ??? "Auto Discover"

        Questa operazione deve essere eseguita sulla rete locale. Verificare che il dispositivo di controllo si trovi sulla stessa LAN di Comet Q.

        Fare clic su **Auto Discover** per avviare la ricerca automatica.

        ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

        Individuare il KVM e inserire il suo Device ID per associarlo all'account.

        ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

    ??? "S/N Code"

        Usare questo metodo se il KVM non viene rilevato o non si trova sulla stessa LAN, ma si dispone del suo numero di serie (S/N).

        Fare clic su **S/N Code**. Nella finestra che si apre, personalizzare il nome del dispositivo e inserire il numero di serie riportato sull'etichetta nella parte inferiore del KVM.

        ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Questa operazione deve essere eseguita sulla rete locale. Verificare che il dispositivo di controllo si trovi sulla stessa LAN di Comet Q.

        1. Accedere al KVM in locale tramite il dominio o l'indirizzo IP. Per i dettagli, consultare [questa guida](../../faq/local_access_via_browser.md).

        2. Aprire **Cloud Service** nell'angolo superiore destro e fare clic su **Bind With Code**.

            ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

        3. Verrà generato casualmente un codice dinamico di 8 cifre per associare il dispositivo, valido per 60 secondi. Fare clic sul codice per copiarlo.

            ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

        4. Tornare all'app GLKVM, inserire il codice di associazione dinamico e fare clic su **Bind**.

            ![dynamic code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

4. Accedere da remoto tramite l'app GLKVM.

    Dopo l'associazione all'account, il dispositivo KVM apparirà come "Online" nell'app.

    ![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

    Fare clic sul dispositivo KVM: si aprirà una nuova finestra e verrà avviata la connessione.

    ![connecting](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

    Una volta connesso, inserire la password di amministrazione per accedere al dispositivo.

    ![connected log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

    Si accederà così al dispositivo KVM e, tramite questo, al dispositivo controllato.

    ![connected access](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

### Tailscale {#tailscale}

Comet Q integra Tailscale e consente l'accesso remoto tramite la sua rete virtuale.

Nella console web, aprire **Apps Center** -> **Tailscale**, abilitarlo e associare Comet Q al proprio account Tailscale.

Associare quindi il dispositivo di controllo allo stesso account. Sarà possibile accedere a Comet Q da remoto inserendo il suo **IP virtuale Tailscale** nel browser del dispositivo di controllo, senza installare l'app GLKVM.

Per i dettagli, consultare [questa guida](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier {#zerotier}

Comet Q integra ZeroTier e consente l'accesso remoto tramite la sua rete virtuale.

Nella console web, aprire **Apps Center** -> **ZeroTier** e abilitarlo.

Collegare quindi Comet Q e il dispositivo di controllo alla stessa rete ZeroTier, usando un Network ID alfanumerico di 16 caratteri. Sarà possibile accedere a Comet Q da remoto inserendo il suo **IP ZeroTier** nel browser del dispositivo di controllo, senza installare l'app GLKVM.

Per i dettagli, consultare [questa guida](../../faq/remote_access_via_zerotier.md){target="_blank"}.
