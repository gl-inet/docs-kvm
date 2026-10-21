# Een statisch IP-adres instellen voor de KVM {#how-to-set-a-static-ip-for-kvm}

In deze handleiding leest u hoe u rechtstreeks in de console een statisch IP-adres instelt voor uw GL.iNet KVM wanneer de bovenliggende router er geen kan toewijzen.

Kies de stappen die bij uw firmwareversie passen.

## Firmware v1.9 en eerder {#firmware-v19-and-earlier}

In de volgende stappen wordt de Comet (GL-RM1) als voorbeeld gebruikt.

1. Meld u aan bij de console van de Comet en ga naar **Settings** -> **Network**. Klik op het IP-adres of op het pictogram met de pijl naar rechts.

    ![Netwerkinstellingen](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/settings-network.png){class="glboxshadow"}

2. Schakel over naar **Static**. Voer een IP-adres binnen de subnetpool in, samen met het netmasker, de gateway en de DNS-servers voor uw Comet, en klik op **Confirm**.

    ![Statische ethernetinstellingen](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/ethernet-settings-static.png){class="glboxshadow"}

## Firmware v1.10 en hoger {#firmware-v110-and-above}

In de volgende stappen wordt de Comet Pro (GL-RM10) als voorbeeld gebruikt.

1. Meld u aan bij de console van de Comet Pro en klik in de navigatiebalk op het pictogram Settings om de instellingenpagina te openen.

    ![Netwerkinstellingen](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/setting_network.png){class="glboxshadow"}

2. Ga naar **Network** en klik onder Ethernet Settings op de knop **Static**. Voer een IP-adres binnen de subnetpool in, samen met het netmasker, de gateway en de DNS-servers voor uw Comet Pro, en klik op **Confirm**.

    ![Statische ethernetinstellingen](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/ethernet_settings_static.png){class="glboxshadow"}

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
