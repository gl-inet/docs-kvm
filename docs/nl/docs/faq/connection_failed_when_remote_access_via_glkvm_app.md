# Verbinding mislukt bij externe toegang via de GLKVM-app {#connection-failed-when-remote-access-via-glkvm-app}

Bij externe toegang via de GLKVM-app kan het voorkomen dat het KVM-apparaat in de GLKVM-app als Online wordt weergegeven, maar dat het na het klikken blijft hangen op "Connecting".

![Apparaat online](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/device_online.png){class="glboxshadow"}

![Verbinding maken](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connecting.png){class="glboxshadow"}

Probleemoplossing:

1. Zorg voor een stabiele netwerkverbinding.

    Controleer of de KVM met een stabiele internetverbinding is verbonden. Een continu brandende witte led geeft aan dat de netwerkverbinding normaal is.

2. Controleer de firewallregels van het netwerk.

    Schakel de lokale firewall tijdelijk uit of voeg domeinen van GL.iNet (bijvoorbeeld glkvm.com) toe aan de lijst met toegestane adressen van de firewall. Probeer na het doorvoeren van de wijzigingen opnieuw verbinding te maken.

    Hieronder vindt u ter referentie de stappen om de firewallregels in het netwerk van Sky aan te passen.

    ??? note "Sky-netwerk (bijvoorbeeld Sky Max Hub)"

        Het beveiligingsmechanisme van het Sky-netwerk kan de domeinnaam `glkvm.com` als verdachte site aanmerken en de toegang blokkeren. U kunt de beperking opheffen via de Sky-app.<br>

        1. Open de MySky-app, ga naar **Broadband** -> **Advanced Security** en controleer of er domeinen van GL.iNet worden beperkt.

            ![MySky 1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-1.png){class="glboxshadow"}
        
        2. Als het domein wordt geblokkeerd, klikt u op de pijl omlaag om de details te bekijken en selecteert u **Allow Access** om de blokkering op te heffen.
 
            ![MySky 2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-2.png){class="glboxshadow" width="300"}

3. Schakel VPN/proxy uit op het besturende apparaat.

    Zorg ervoor dat er op het apparaat waarop de GLKVM-app draait geen VPN- of proxyservices zijn ingeschakeld, omdat deze de verbinding kunnen verstoren.

4. Start de KVM indien mogelijk opnieuw op.

    Voer indien mogelijk een hardwarematige herstart van het KVM-apparaat uit om tijdelijke netwerk- of softwareproblemen te verhelpen.

    Als u niet in de buurt van het KVM-apparaat bent, kunt u het op afstand opnieuw opstarten via de GLKVM-app:

    1. Klik in de apparatenlijst rechtsboven bij uw apparaat op **Manage**.

        ![Opnieuw opstarten via de app 1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_1.png){class="glboxshadow"}

    2. Klik op **More** en selecteer **Reboot**.

        ![Opnieuw opstarten via de app 2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_2.png){class="glboxshadow"}

Aanvullende technische opmerkingen:

1. Zorg ervoor dat de DNS-omzetting voor de domeinen werkt.

2. Controleer of uitgaand verkeer naar de standaardpoorten voor KVM/externe toegang niet wordt geblokkeerd.

3. Overleg bij bedrijfsnetwerken met de IT-beheerders over mogelijke beleidsregels voor het filteren van verkeer.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
