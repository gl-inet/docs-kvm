# Come accedere al KVM localmente tramite browser {#how-to-access-the-kvm-locally-via-browser}

Prima di iniziare, assicurati che il dispositivo di controllo e il KVM si trovino sulla stessa LAN.

Puoi accedere al KVM localmente tramite un browser web in due modi: usando un nome di dominio o un indirizzo IP.

## Accesso locale tramite nome di dominio {#local-access-via-domain}

1. Apri un browser sul dispositivo di controllo. Per una migliore compatibilità, è consigliato Chrome o Edge.

2. Digita `glkvm.local` nella barra degli indirizzi. Verrai indirizzato alla pagina di accesso di GLKVM. Inserisci la password di amministratore.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    Ora puoi accedere localmente alla console del KVM e, quindi, al dispositivo controllato.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

## Accesso locale tramite indirizzo IP {#local-access-via-ip-address}

Trova l'indirizzo IP del KVM nella rete a monte, ad esempio sul router, e inseriscilo nel browser. Potrai accedere localmente al KVM e, quindi, al dispositivo controllato.

Prendiamo come esempio il router **GL-AXT1800** e il KVM **GL-RM1 Comet**: Comet è collegato alla porta LAN del router GL-AXT1800 tramite un cavo Ethernet. Il dispositivo controllato è collegato correttamente a Comet tramite il cavo HD e il cavo USB.

Segui i passaggi indicati di seguito per accedere alla console del KVM.

1. Accedi al pannello di amministrazione web di GL-AXT1800. Il router deve essere configurato per l'accesso a Internet.

    ![log in router](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/log_in_router.png){class="glboxshadow"}

2. Nel pannello di amministrazione del router, vai su **Client** e trova l'indirizzo IP di Comet nell'elenco dei client. Nell'esempio seguente, l'indirizzo IP di Comet è **192.168.8.197**.

    ![find glkvm ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

3. Apri una nuova scheda nel browser e digita l'indirizzo IP di Comet, **192.168.8.197**, nella barra degli indirizzi.

    Verrai indirizzato alla pagina di accesso di GLKVM. Inserisci la password di amministratore.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    Ora puoi accedere localmente alla console del KVM e, quindi, al dispositivo controllato.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
