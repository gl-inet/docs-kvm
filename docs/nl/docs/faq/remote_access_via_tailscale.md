# De KVM op afstand openen via Tailscale {#how-to-access-kvm-remotely-via-tailscale}

De GL.iNet KVM is geïntegreerd met Tailscale, zodat u de KVM voor externe toegang aan het virtuele Tailscale-netwerk kunt koppelen – zonder de GLKVM-app te installeren of de cloudservice te gebruiken. Dit is vooral handig als uw besturende apparaat geen Windows, macOS, Android of iOS gebruikt (en de GLKVM-app er dus niet op kan worden geïnstalleerd), of als u de GLKVM-app of de cloudservice niet wilt gebruiken.

Volg deze stappen om uw GL.iNet KVM op afstand te openen via Tailscale.

## De KVM aan Tailscale koppelen {#bind-kvm-to-tailscale}

**Verbind uw KVM en het besturende apparaat voordat u begint met hetzelfde lokale netwerk.**

1. Open een browser op het besturende apparaat. Voor een betere compatibiliteit wordt Chrome of Edge aanbevolen.
    
2. Meld u lokaal aan bij de console van uw KVM via de domeinnaam of het IP-adres. Hier gebruiken we de standaarddomeinnaam als voorbeeld.

    Voer `glkvm.local` in de adresbalk in. U wordt naar de aanmeldpagina van GLKVM geleid. Voer uw beheerderswachtwoord in.

    ![Lokale toegang via domeinnaam](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

3. Ga na het aanmelden naar **Apps Center** -> **Tailscale**. Schakel Tailscale in en klik op **Bind Device**.

    ![Tailscale inschakelen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enable_tailscale.png){class="glboxshadow"}

4. U wordt naar de aanmeldpagina van Tailscale geleid. Voer uw e-mailadres in om u aan te melden.

    ![Aanmelden bij Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

5. Na het aanmelden meldt de pagina dat u op het punt staat het apparaat glkvm met uw tailnet te verbinden. Klik op **Connect**.

    ![KVM met het tailnet verbinden](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_kvm_to_tailscale.png){class="glboxshadow"}

    Uw KVM-apparaat wordt dan aan uw tailnet gekoppeld.

    ![KVM gekoppeld](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_kvm_successful.png){class="glboxshadow"}
    
6. U wordt doorgestuurd naar uw Tailscale-console, waar onder **Machines** een apparaat met de naam **glkvm** wordt weergegeven.

    ![Tailscale-console 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_1.png){class="glboxshadow"}

## Het besturende apparaat koppelen {#bind-the-controlling-device}

In het onderstaande voorbeeld ziet u hoe u een Windows-laptop (als besturend apparaat) aan het Tailscale-netwerk koppelt.

1. Installeer Tailscale op uw laptop via [deze pagina](https://tailscale.com/download){target="_blank"}.

2. Start Tailscale op de laptop en meld u aan met hetzelfde e-mailadres.

    ![Aanmelden bij Tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

3. Na het aanmelden meldt de pagina dat u op het punt staat de laptop (het besturende apparaat) met uw tailnet te verbinden. Klik op **Connect**.

    ![Pc met het tailnet verbinden](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_pc_to_tailscale.png){class="glboxshadow"}

    Uw laptop wordt dan aan uw tailnet gekoppeld.

    ![Pc gekoppeld](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_pc_successful.png){class="glboxshadow"}

4. U wordt doorgestuurd naar uw Tailscale-console, waar het besturende apparaat nu ook onder **Machines** wordt weergegeven.

    ![Tailscale-console 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_2.png){class="glboxshadow"}

## Externe toegang via Tailscale {#remote-access-via-tailscale}

Klik in de Tailscale-console op het **Address** van glkvm (in dit voorbeeld `100.104.185.26`).

![Virtueel IP-adres opvragen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/get_vitual_ip.png){class="glboxshadow"}

U ziet vier waarden:

- glkvm (apparaatnaam)
- glkvm.tail1fd0.ts.net (door Tailscale toegewezen domeinnaam)
- fd7a:115c:a1e0:301:b92f (virtueel IPv6-adres)
- 100.104.185.26 (virtueel IPv4-adres).

Deze waarden worden door Tailscale toegewezen voor apparaatidentificatie en communicatie binnen het virtuele netwerk. U kunt uw KVM-apparaat op afstand openen via de door Tailscale toegewezen domeinnaam, het virtuele IPv4-adres of het virtuele IPv6-adres.

We nemen het virtuele IPv4-adres als voorbeeld.

1. Kopieer het virtuele IPv4-adres van uw KVM-apparaat.

2. Open een nieuw tabblad en plak het IP-adres in de adresbalk.

    ![Virtueel IP-adres openen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enter_vitual_ip.png){class="glboxshadow"}

    Mogelijk verschijnt er een privacyfout. [Waarom krijg ik deze privacyfout?](privacy_error_from_your_browser.md){target="_blank"}

    ![Privacyfout](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/privacy_error.png){class="glboxshadow"}

    Klik op **Advanced** en vervolgens op **Proceed to 100.104.185.26**. U wordt doorgestuurd naar de aanmeldpagina van GLKVM.

    ![Doorgaan](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/proceed.png){class="glboxshadow"}

3. Voer uw beheerderswachtwoord in om u aan te melden. U kunt uw GL.iNet KVM en het bestuurde apparaat nu openen via het virtuele IP-adres van Tailscale.

    ![Externe toegang gelukt](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/remote_access_via_tailscale.png){class="glboxshadow"}

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
