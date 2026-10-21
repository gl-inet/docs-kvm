# Come accedere al KVM da remoto tramite ZeroTier {#how-to-access-kvm-remotely-via-zerotier}

> Nota: aggiorna il firmware del KVM alla v1.8.0 prima di usare questa funzione.

Il KVM GL.iNet integra ZeroTier e può essere associato alla sua rete per l'accesso remoto, senza installare l'app GLKVM né usare il servizio cloud.

Segui questi passaggi per accedere da remoto al KVM GL.iNet tramite ZeroTier.

## Attivare ZeroTier {#enable-zerotier}

**Prima di iniziare, collega il KVM e il dispositivo di controllo alla stessa rete locale.**

1. Apri un browser sul dispositivo di controllo. Per una migliore compatibilità, è consigliato Chrome o Edge.

2. Accedi localmente alla console del KVM tramite nome di dominio o indirizzo IP. In questo esempio useremo l'indirizzo IP locale.

    Digita l'**indirizzo IP LAN** del KVM, reperibile sul touchscreen o sul router, nella barra degli indirizzi. Verrai indirizzato alla pagina di accesso di GLKVM. Inserisci la password di amministratore.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/1_local_access.png){class="glboxshadow"}

3. Dopo l'accesso, vai su **Apps Center** -> **ZeroTier**. Attiva ZeroTier: comparirà un avviso giallo, come mostrato di seguito.

    Fai clic sul collegamento oppure [qui](https://my.zerotier.com/){target="_blank"} per accedere a ZeroTier Central e creare la tua rete ZeroTier.

    ![enable zerotier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/2_enable_zerotier.png){class="glboxshadow"}

## Associare il KVM a ZeroTier {#bind-kvm-to-zerotier}

1. Al primo accesso a [ZeroTier](https://my.zerotier.com/){target="_blank"}, potrebbe essere necessario selezionare la versione di ZeroTier Central.

    ![select central](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/3_select_central.png){class="glboxshadow"}

    Seleziona la versione appropriata per continuare. Qui useremo **New Central** come esempio.

    Accedi con il tuo indirizzo e-mail e la password. Se non hai un account, creane prima uno.

    ![zerotier signin](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/4_zerotier_signin.png){class="glboxshadow"}

2. Dopo l'accesso, crea un'organizzazione.

    ![create organization](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/5_create_org.png){class="glboxshadow"}

3. Seleziona un piano. In questo esempio scegliamo il piano **Personal**, che include 10 dispositivi, 1 amministratore di rete e 1 rete. Se vuoi creare più reti, aggiungere più dispositivi oppure configurare route e DNS personalizzati, scegli il piano Essential o Scale.

    ![select plan](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/6_select_plan.png){class="glboxshadow"}

4. La rete ZeroTier è ora creata. Copia il **Network ID**, una stringa alfanumerica di 16 caratteri. Ti servirà in seguito per aggiungere i dispositivi alla rete ZeroTier. Lascia aperta questa scheda.

    ![network id](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/7_copy_network_id.png){class="glboxshadow"}

5. Torna alla console del KVM e vai su **Apps Center** -> **ZeroTier**. Individua **Network ID** e fai clic su **Set**.

    ![network id](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id1.png){class="glboxshadow"}

    Nella finestra visualizzata, incolla il **Network ID** e fai clic su **Confirm**.

    ![network id](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id2.png){class="glboxshadow"}

    Nella console comparirà un avviso giallo che indica che il dispositivo deve essere autorizzato.

    ![authorize1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize1.png){class="glboxshadow"}

6. Torna a ZeroTier Central. Vedrai un dispositivo, il KVM, in attesa di approvazione. Fai clic su **Authorize**.

    ![authorize2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize2.png){class="glboxshadow"}

    Una volta autorizzato, lo stato passerà a Authorized in verde, come mostrato di seguito.

    ![authorized1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized1.png){class="glboxshadow"}

    Nella console del KVM puoi visualizzare anche **Network ID** e **Virtual IP**, come mostrato di seguito.

    ![authorized2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized2.png){class="glboxshadow"}

## Associare il dispositivo di controllo {#bind-the-controlling-device}

L'esempio seguente mostra come associare alla rete ZeroTier un portatile Windows usato come dispositivo di controllo.

1. Installa ZeroTier sul portatile da [qui](https://www.zerotier.com/download/){target="_blank"}.

2. Avvia ZeroTier sul portatile e aggiungilo alla stessa rete ZeroTier.

    ZeroTier non mostra una finestra separata sul desktop, ma solo un'icona nell'area di notifica, nell'angolo in basso a destra. Tutte le operazioni si eseguono tramite il menu del pulsante destro del mouse.

    Fai clic con il pulsante destro del mouse sull'icona di ZeroTier e seleziona **Join New Network**. Nella finestra visualizzata, inserisci lo stesso **Network ID** per aggiungere il PC alla medesima rete ZeroTier.

    ![join network](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/11_pc_join_network.jpg){class="glboxshadow"}

    Poi vai su ZeroTier Central, trova il dispositivo Pending e autorizzalo.

    ![authorize](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/12_authorize.png){class="glboxshadow"}

3. Una volta autorizzato, lo stato passerà a Authorized in verde, come mostrato di seguito.

    ![authorized](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/13_authorized.png){class="glboxshadow"}

4. Il KVM e il portatile sono ora entrambi nella stessa rete ZeroTier. Puoi verificarlo dal loro Network ID, come mostrato di seguito.

    ![same zt network](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/14_same_zt_network.png){class="glboxshadow"}

## Accesso remoto tramite ZeroTier {#remote-access-via-zerotier}

L'esempio seguente mostra come accedere da remoto alla console del KVM tramite l'indirizzo IP ZeroTier.

1. Sul portatile, accedi a ZeroTier Central con il tuo account, trova il dispositivo KVM e fai clic sul suo **ZT IP** per copiarlo.

    ![zerotier ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/15_zerotier_ip.png){class="glboxshadow"}

2. Apri una nuova scheda del browser, incolla l'IP ZeroTier copiato nella barra degli indirizzi e premi Invio. Verrai reindirizzato alla pagina di accesso di GLKVM.

    Inserisci la password di amministratore per accedere. Ora puoi accedere al KVM GL.iNet e al dispositivo controllato tramite l'IP ZeroTier.

    ![remote access](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/16_remote_access.png){class="glboxshadow"}

    **Suggerimento**: al primo accesso a questo IP ZeroTier potrebbe comparire un errore di privacy. Fai clic su **Advanced** -> **Proceed** per continuare. Consulta [Errore di privacy nel browser](privacy_error_from_your_browser.md){target="_blank"} per i dettagli.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
