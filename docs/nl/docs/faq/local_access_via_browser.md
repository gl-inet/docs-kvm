# De KVM lokaal openen via een browser {#how-to-access-the-kvm-locally-via-browser}

Zorg er voordat u begint voor dat het besturende apparaat en de KVM zich in hetzelfde LAN bevinden.

U kunt de KVM op twee manieren lokaal openen via een webbrowser: met een domeinnaam of met een IP-adres.

## Lokale toegang via de domeinnaam {#local-access-via-domain}

1. Open een browser op het besturende apparaat. Voor een betere compatibiliteit wordt Chrome of Edge aanbevolen.

2. Voer `glkvm.local` in de adresbalk in. U wordt naar de aanmeldpagina van GLKVM geleid. Voer uw beheerderswachtwoord in.

    ![Lokale toegang via domeinnaam](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    U kunt de console van uw KVM nu lokaal openen en zo toegang krijgen tot het bestuurde apparaat.

    ![Lokale toegang via domeinnaam](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

## Lokale toegang via het IP-adres {#local-access-via-ip-address}

Zoek het IP-adres van uw KVM op in het bovenliggende netwerk (bijvoorbeeld in uw router) en voer dit IP-adres in de browser in. Daarna kunt u uw KVM lokaal openen en zo toegang krijgen tot het bestuurde apparaat.

We nemen de **GL-AXT1800** (de router) en de **GL-RM1 Comet** (de KVM) als voorbeeld: de Comet is met een ethernetkabel aangesloten op de LAN-poort van de GL-AXT1800-router. Het bestuurde apparaat is correct met een HD-kabel en een USB-kabel op de Comet aangesloten.

Volg de onderstaande stappen om de KVM-console te openen.

1. Meld u aan bij het webbeheerpaneel van de GL-AXT1800. De router moet zijn geconfigureerd voor internettoegang.

    ![Aanmelden bij de router](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/log_in_router.png){class="glboxshadow"}

2. Ga in het beheerpaneel van de router naar **Client** en zoek het IP-adres van de Comet op in de lijst met clients. Zoals hieronder te zien is, is het IP-adres van de Comet **192.168.8.197**.

    ![IP-adres van de GLKVM zoeken](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

3. Open een nieuw tabblad in de browser en voer het IP-adres van de Comet, **192.168.8.197**, in de adresbalk in.

    U wordt naar de aanmeldpagina van GLKVM geleid. Voer uw beheerderswachtwoord in.

    ![Lokale toegang via IP-adres](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    U kunt de console van uw KVM nu lokaal openen en zo toegang krijgen tot het bestuurde apparaat.

    ![Lokale toegang via IP-adres](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
