# Come accedere al KVM da remoto tramite Tailscale {#how-to-access-kvm-remotely-via-tailscale}

Il KVM GL.iNet integra Tailscale e può essere associato alla sua rete virtuale per l'accesso remoto, senza installare l'app GLKVM né usare il servizio cloud. Questa soluzione è particolarmente utile quando il dispositivo di controllo non esegue Windows, macOS, Android o iOS e quindi non può installare l'app GLKVM, oppure quando non vuoi usare l'app o il servizio cloud.

Segui questi passaggi per accedere da remoto al KVM GL.iNet tramite Tailscale.

## Associare il KVM a Tailscale {#bind-kvm-to-tailscale}

**Prima di iniziare, collega il KVM e il dispositivo di controllo alla stessa rete locale.**

1. Apri un browser sul dispositivo di controllo. Per una migliore compatibilità, è consigliato Chrome o Edge.

2. Accedi localmente alla console del KVM tramite nome di dominio o indirizzo IP. In questo esempio useremo il dominio predefinito.

    Digita `glkvm.local` nella barra degli indirizzi. Verrai indirizzato alla pagina di accesso di GLKVM. Inserisci la password di amministratore.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

3. Dopo l'accesso, vai su **Apps Center** -> **Tailscale**. Attiva Tailscale e fai clic su **Bind Device**.

    ![enable tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enable_tailscale.png){class="glboxshadow"}

4. Verrai indirizzato alla pagina di accesso di Tailscale. Inserisci il tuo indirizzo e-mail per accedere.

    ![log in tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

5. Dopo l'accesso, la pagina indica che stai per collegare il dispositivo glkvm alla tua tailnet. Fai clic su **Connect**.

    ![connect kvm to tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_kvm_to_tailscale.png){class="glboxshadow"}

    Il dispositivo KVM verrà associato alla tua tailnet.

    ![bind kvm successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_kvm_successful.png){class="glboxshadow"}

6. Verrai reindirizzato alla console di Tailscale, dove il dispositivo **glkvm** comparirà nella sezione **Machines**.

    ![tailscale console 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_1.png){class="glboxshadow"}

## Associare il dispositivo di controllo {#bind-the-controlling-device}

L'esempio seguente mostra come associare alla rete Tailscale un portatile Windows usato come dispositivo di controllo.

1. Installa Tailscale sul portatile da [qui](https://tailscale.com/download){target="_blank"}.

2. Avvia Tailscale sul portatile e accedi con lo stesso indirizzo e-mail.

    ![log in tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

3. Dopo l'accesso, la pagina indica che stai per collegare il portatile, cioè il dispositivo di controllo, alla tua tailnet. Fai clic su **Connect**.

    ![connect pc to tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_pc_to_tailscale.png){class="glboxshadow"}

    Il portatile verrà associato alla tua tailnet.

    ![bind pc successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_pc_successful.png){class="glboxshadow"}

4. Verrai reindirizzato alla console di Tailscale, dove anche il dispositivo di controllo comparirà nella sezione **Machines**.

    ![tailscale console 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_2.png){class="glboxshadow"}

## Accesso remoto tramite Tailscale {#remote-access-via-tailscale}

Nella console di Tailscale, fai clic su **Address** di glkvm, `100.104.185.26` in questo esempio.

![get vittual ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/get_vitual_ip.png){class="glboxshadow"}

Vedrai quattro valori:

- glkvm, nome del dispositivo
- glkvm.tail1fd0.ts.net, dominio assegnato da Tailscale
- fd7a:115c:a1e0:301:b92f, IPv6 virtuale
- 100.104.185.26, IPv4 virtuale.

Questi valori vengono assegnati da Tailscale per identificare il dispositivo e consentire la comunicazione sulla rete virtuale. Puoi accedere al dispositivo KVM da remoto usando il dominio assegnato da Tailscale, l'IPv4 virtuale o l'IPv6 virtuale.

Prendiamo come esempio l'IPv4 virtuale.

1. Copia l'indirizzo IPv4 virtuale del dispositivo KVM.

2. Apri una nuova scheda e incolla l'indirizzo IP nella barra degli indirizzi.

    ![access vitual ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enter_vitual_ip.png){class="glboxshadow"}

    Potrebbe comparire un errore di privacy. [Perché viene visualizzato questo errore?](privacy_error_from_your_browser.md){target="_blank"}

    ![privacy error](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/privacy_error.png){class="glboxshadow"}

    Fai clic su **Advanced**, quindi su **Proceed to 100.104.185.26**. Verrai reindirizzato alla pagina di accesso di GLKVM.

    ![proceed](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/proceed.png){class="glboxshadow"}

3. Inserisci la password di amministratore per accedere. Ora puoi accedere al KVM GL.iNet e al dispositivo controllato tramite l'IP virtuale Tailscale.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/remote_access_via_tailscale.png){class="glboxshadow"}

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
