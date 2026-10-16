# Come accedere al KVM da remoto tramite NetBird {#how-to-access-kvm-remotely-via-netbird}

> Nota: aggiorna il firmware del KVM alla v1.9.0 prima di usare questa funzione.

[NetBird](https://netbird.io/){target="_blank"} è una piattaforma di rete zero trust open source che consente di creare reti private sicure per uso domestico e aziendale. Basato su una rete overlay WireGuard®, NetBird permette di accedere in modo sicuro ai dispositivi da qualsiasi luogo e in qualsiasi momento.

Il KVM GL.iNet integra NetBird e può essere associato alla sua rete virtuale per l'accesso remoto, senza installare l'app GLKVM né usare il servizio cloud.

Segui questi passaggi per accedere da remoto al KVM GL.iNet tramite NetBird.

## Associare il KVM a NetBird {#bind-kvm-to-netbird}

**Prima di iniziare, collega il KVM e il dispositivo di controllo alla stessa rete locale.**

1. Accedi localmente alla console del KVM tramite nome di dominio o indirizzo IP, quindi vai su **Apps Center** -> **NetBird**. Attiva NetBird e fai clic su **Bind Device**.

    ![bind device](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/1-bind-device.png){class="glboxshadow"}

2. Verrai reindirizzato alla pagina di conferma del dispositivo. Fai clic su **Confirm**.

    ![confirm device](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/2-confirm.png){class="glboxshadow"}

3. Accedi al tuo account NetBird. Se non hai un account, creane prima uno.

    ![netbird sign in](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/3-signin.png){class="glboxshadow"}

4. Dopo l'accesso, il dispositivo KVM verrà associato automaticamente al tuo account.

    ![kvm connected](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/4-connected.png){class="glboxshadow"}

    Nella dashboard di NetBird, il KVM sarà visibile anche nella pagina **Peers**.

    ![netbird dashboard](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/5-dashboard.png){class="glboxshadow"}

## Associare il dispositivo di controllo {#bind-the-controlling-device}

L'esempio seguente mostra come associare alla rete NetBird un portatile Windows usato come dispositivo di controllo.

1. Installa NetBird sul portatile da [qui](https://app.netbird.io/install){target="_blank"}.

    ![install netbird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/6-install.png){class="glboxshadow"}

2. Avvia NetBird sul portatile e aggiungilo alla stessa rete NetBird.

    NetBird non mostra una finestra separata sul desktop, ma solo un'icona nell'area di notifica, nell'angolo in basso a destra. Tutte le operazioni si eseguono tramite il menu del pulsante destro del mouse.

    Fai clic con il pulsante destro del mouse sull'icona di NetBird e seleziona **Connect**.

    ![pc connect](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/7-pc-connect.png){class="glboxshadow gl-50-desktop"}

3. Nella finestra visualizzata, fai clic su **Accept** per autorizzare l'operazione.

    ![authorize](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/8-authorize.png){class="glboxshadow"}

    Il portatile verrà associato automaticamente al tuo account e aggiunto alla stessa rete NetBird.

    ![pc connected](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/9-login-success.png){class="glboxshadow"}

4. Nella dashboard di NetBird, la pagina **Peers** mostrerà due dispositivi: il KVM e il portatile di controllo.

    ![netbird dashboard](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/10-dashboard.png){class="glboxshadow"}

## Accesso remoto tramite NetBird {#remote-access-via-netbird}

L'esempio seguente mostra come accedere da remoto alla console del KVM tramite l'indirizzo IP virtuale NetBird.

1. Sul portatile, accedi alla dashboard di NetBird e vai su **Peers**.

    Trova il dispositivo KVM e fai clic sul suo **NetBird IP**, `100.100.141.229` in questo esempio, per copiare l'IP virtuale.

    ![kvm netbird ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/11-kvm-netbird-ip.png){class="glboxshadow"}

    Passa il puntatore sull'indirizzo IP per visualizzare altri dettagli, come IP pubblico, dominio e area geografica.

2. Apri una nuova scheda del browser, incolla l'IP NetBird copiato nella barra degli indirizzi e premi Invio. Verrai reindirizzato alla pagina di accesso di GLKVM.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-login.png){class="glboxshadow"}

    Inserisci la password di amministratore per accedere. Ora puoi accedere al KVM GL.iNet e al dispositivo controllato tramite l'IP NetBird.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-access.png){class="glboxshadow"}

    **Suggerimento**: al primo accesso a questo IP NetBird potrebbe comparire un errore di privacy. Fai clic su **Advanced** -> **Proceed** per continuare. Consulta [Errore di privacy nel browser](privacy_error_from_your_browser.md){target="_blank"} per i dettagli.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
