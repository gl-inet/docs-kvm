# Configurazione rapida di Comet X (GL-RM4PE)

## Collegamento dei dispositivi { #connect-devices }

Per chiarezza, il dispositivo A indica il dispositivo di controllo e il dispositivo B quello controllato.

![connect1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect1.png){class="glboxshadow"}

1. Collegare Comet X a uno switch PoE con un cavo Ethernet oppure alimentarlo con un alimentatore da 5V/3A.

    ![connect2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect2.png){class="glboxshadow"}

    ***Nota**: Se si usa un alimentatore, collegare Comet X a un dispositivo di rete, ad esempio un router, tramite un cavo Ethernet per accedere a Internet.*

2. Collegare la porta **HDMI IN** di Comet X al dispositivo B con un cavo HDMI per trasmettere il segnale video.

    ![connect3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect3.png){class="glboxshadow"}

3. Collegare la porta **USB-C** di Comet X al dispositivo B con un cavo USB. La porta USB-C deve essere abbinata alla corrispondente porta HDMI IN per trasmettere correttamente i segnali di tastiera e mouse.

    ![connect4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect4.png){class="glboxshadow"}

4. (Facoltativo) Collegare la porta **HDMI OUT** di Comet X a un monitor esterno per duplicare lo schermo (uscita video loopout). Per i dettagli, consultare [Controllo locale](#local-control).

5. Il collegamento è completo. Ora è possibile accedere alla console di Comet X in locale o da remoto.

## Montaggio su rack { #rack-mounting }

Se necessario, montare Comet X sulle guide del rack server.

1. Usare le viti in dotazione per fissare le staffe di montaggio a Comet X.

    ![install1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install1.png){class="glboxshadow"}

2. Fissare Comet X alle guide del rack con apposite viti. **Le viti per rack non sono incluse**.

    ![install2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install2.png){class="glboxshadow"}

## Controllo locale { #local-control }

Controllare il dispositivo direttamente tramite cavi fisici, senza bisogno di una rete, un indirizzo IP o un nome di dominio.

Comet X dispone di una porta HDMI OUT e di due porte USB aggiuntive, ideali per la risoluzione dei problemi, la configurazione e l'installazione del sistema operativo in locale. È sufficiente collegare monitor, mouse e tastiera per controllare immediatamente l'hardware in locale.

1. Collegare la porta **HDMI OUT** sul pannello posteriore di Comet X a un monitor esterno per duplicare lo schermo (uscita video loopout).

    ![local control1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control1.png){class="glboxshadow"}

2. Collegare una tastiera e un mouse alle porte USB sul pannello anteriore di Comet X.

    ![local control2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control2.png){class="glboxshadow"}

3. Ora è possibile controllare i dispositivi collegati con la tastiera e il mouse locali, mentre il segnale video viene inoltrato al monitor locale.

## Accesso LAN { #lan-access }

È possibile accedere a Comet X sulla rete locale in due modi: tramite nome di dominio o indirizzo IP.

Prima dell'accesso, verificare che il dispositivo di controllo si trovi sulla stessa LAN di Comet X.

### Dominio { #domain }

1. Aprire un browser sul dispositivo di controllo. Per una migliore compatibilità, si consiglia Chrome o Edge.

2. Inserire `glkvm.local` nella barra degli indirizzi. Si aprirà la pagina di accesso GLKVM. Inserire la password di amministrazione.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain1.png){class="glboxshadow"}

    ***Nota**: Al primo accesso è necessario impostare la password di amministrazione.*

3. Sarà quindi possibile accedere alla console di Comet X in locale e al dispositivo controllato.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain2.png){class="glboxshadow"}

### Indirizzo IP { #ip-address }

1. Individuare l'indirizzo IP di Comet X sul touchscreen. In questo esempio, l'indirizzo IP è `192.168.8.197`.

2. Aprire un browser e inserire questo IP nella barra degli indirizzi. Si aprirà la pagina di accesso GLKVM. Inserire la password di amministrazione.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip1.png){class="glboxshadow"}

    ***Nota**: Al primo accesso è necessario impostare la password di amministrazione.*

3. Sarà quindi possibile accedere alla console di Comet X in locale e al dispositivo controllato.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip2.png){class="glboxshadow"}

## Accesso remoto { #remote-access }

È possibile accedere a Comet X da remoto in diversi modi: tramite il servizio cloud, l'app GLKVM, Tailscale e ZeroTier.

### Servizio cloud { #cloud-service }

1. Associare il dispositivo a KVM Cloud. Questa operazione deve essere eseguita sulla rete locale.

    È possibile associare il KVM al cloud in due modi: associazione normale o tramite codice dinamico. Qui viene illustrata l'associazione normale. Per usare il codice dinamico, consultare [questa guida](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}.

    Per prima cosa, accedere a Comet X in locale e aprire **Cloud Service** nell'angolo superiore destro. Fare clic su **Bind To KVMCloud**.

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_to_cloud.png){class="glboxshadow"}

    Si aprirà una pagina di accesso. Accedere con il proprio account cloud glinet.

    ![cloud bind device1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind1.png){class="glboxshadow"}

    Confermare quindi le informazioni del dispositivo e fare clic su **Bind**.

    ![cloud bind device2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind2.png){class="glboxshadow"}

    Attendere un momento: Comet X verrà associato all'account. Fare clic su **Done**.

    ![cloud bind device success](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind_success.png){class="glboxshadow"}

2. Accedere da remoto tramite il servizio cloud.

    Dopo aver fatto clic su Done, si aprirà il sito `glkvm.com`, dove sarà possibile visualizzare il dispositivo.

    ![cloud devices list](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_devices.png){class="glboxshadow"}

    ***Suggerimento**: Se il reindirizzamento non avviene, inserire manualmente `glkvm.com` nella barra degli indirizzi e accedere all'account glinet. Dopo l'accesso sarà visibile il dispositivo associato all'account.*

    Fare clic sul dispositivo a cui si desidera accedere da remoto.

    ![cloud access](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access.png){class="glboxshadow"}

    Si aprirà una nuova pagina web. Inserire la password di amministrazione per accedere.

    ![cloud access1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access1.png){class="glboxshadow"}

    Sarà quindi possibile accedere a Comet X e al dispositivo controllato da remoto tramite il cloud.

    ![cloud access2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access2.png){class="glboxshadow"}

### App GLKVM { #glkvm-app }

1. Installare l'[app GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} sul dispositivo di controllo.

2. Accedere con il proprio account GL.iNet.

    ![log in](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_login.jpg){class="glboxshadow"}

    Se non si dispone di un account, registrarsi e poi accedere.

    ![sign up](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_signup.png){class="glboxshadow"}

3. Associare il dispositivo.

    Dopo l'accesso, la pagina apparirà come mostrato di seguito. Fare clic su **Add Device**.

    ![add device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_add_device.png){class="glboxshadow"}

    È possibile associare il dispositivo in tre modi: Auto Discover, S/N Code e Dynamic Binding Code.

    ??? "Auto Discover"

        Questa operazione deve essere eseguita sulla rete locale. Verificare che il dispositivo di controllo si trovi sulla stessa LAN di Comet X e tenere a portata di mano il Device ID del KVM.

        Fare clic su **Auto Discover** per avviare la ricerca.

        ![auto discover 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover1.png){class="glboxshadow"}

        Individuare il KVM e inserire il suo **Device ID** per associarlo all'account.

        ![auto discover 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover2.png){class="glboxshadow"}

        ![auto discover 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover3.png){class="glboxshadow"}

    ??? "S/N Code"

        Usare questo metodo se il KVM non viene rilevato o non si trova sulla stessa LAN, ma si dispone del suo numero di serie (S/N).

        Fare clic su **S/N Code**. Nella finestra che si apre, impostare un nome per il dispositivo e inserire il numero di serie riportato nella parte inferiore del KVM.

        ![sn code](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/add_sncode.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Questa operazione deve essere eseguita sulla rete locale. Verificare che il dispositivo di controllo si trovi sulla stessa LAN di Comet X.

        1. Accedere al KVM in locale tramite il dominio o l'indirizzo IP. Per i dettagli, consultare [Accesso LAN](#lan-access).

        2. Aprire **Cloud Service** nell'angolo superiore destro e fare clic su **Bind With Code**.

            ![bind with code 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code1.png){class="glboxshadow"}

        3. Verrà generato casualmente un codice dinamico di 8 cifre per associare il dispositivo, valido per 60 secondi. Fare clic sul codice per copiarlo.

            ![bind with code 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code2.png){class="glboxshadow"}

        4. Tornare all'app GLKVM, inserire il codice di associazione dinamico e fare clic su **Bind**.

            ![dynamic code](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code3.png){class="glboxshadow"}

4. Accedere da remoto tramite l'app GLKVM.

    Dopo l'associazione all'account, il dispositivo KVM apparirà come "Online" nell'app.

    ![app device online](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_devices.png){class="glboxshadow"}

    Fare clic sul dispositivo KVM: si aprirà una nuova finestra e verrà avviata la connessione.

    ![app connecting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_connecting.png){class="glboxshadow"}

    Una volta connesso, inserire la password di amministrazione per accedere al dispositivo.

    ![app access1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access1.png){class="glboxshadow"}

    Si accederà così al dispositivo KVM e, tramite questo, al dispositivo controllato.

    ![app access2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access2.png){class="glboxshadow"}

### Tailscale

Comet X integra Tailscale e consente l'accesso remoto tramite la sua rete virtuale.

Nella console web, aprire **Apps Center** -> **Tailscale**, abilitarlo e associare Comet X al proprio account Tailscale.

Associare quindi il dispositivo di controllo allo stesso account. Sarà possibile accedere a Comet X da remoto inserendo il suo **IP virtuale Tailscale** nel browser del dispositivo di controllo, senza installare l'app GLKVM.

Per i dettagli, consultare [questa guida](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier

Comet X integra ZeroTier e consente l'accesso remoto tramite la sua rete virtuale.

Nella console web, aprire **Apps Center** -> **ZeroTier** e abilitarlo.

Collegare quindi Comet X e il dispositivo di controllo alla stessa rete ZeroTier, usando un Network ID alfanumerico di 16 caratteri. Sarà possibile accedere a Comet X da remoto inserendo il suo **IP ZeroTier** nel browser del dispositivo di controllo, senza installare l'app GLKVM.

Per i dettagli, consultare [questa guida](../../faq/remote_access_via_zerotier.md){target="_blank"}.
