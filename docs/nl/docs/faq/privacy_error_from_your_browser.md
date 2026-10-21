# Privacyfout bij toegang tot de KVM via een browser {#privacy-error-when-accessing-kvm-via-browser}

Wanneer u de GL.iNet KVM via een browser opent, kan uw browser een waarschuwing tonen: **Your connection isn't private**.

![Privacyfout](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

Deze waarschuwing betekent dat de browser het SSL/TLS-certificaat van de KVM niet kan valideren. Het certificaat is bijvoorbeeld niet uitgegeven door een certificeringsinstantie die uw browser vertrouwt, of het komt niet overeen met het IP-adres of de hostnaam waarmee u de console opent.

## Waarom krijg ik deze waarschuwing? {#why-do-i-get-this-warning}

In het bovenstaande voorbeeld is **192.168.8.11** het lokale IP-adres van de KVM, dat de bovenliggende router dynamisch via DHCP heeft toegewezen.

!!! Note "Opmerking"

    Als de gateway van de router waarop uw GL.iNet KVM is aangesloten "192.168.x.1" is (waarbij x in privénetwerken doorgaans 0, 1 of 8 is), dan is het lokale IP-adres van uw KVM "192.168.x.y" (waarbij y een geldig hostadres in het subnet is).

Dit lokale IP-adres wordt gebruikt om de console van de GL.iNet KVM te openen, niet een openbare website.

De KVM gebruikt een standaard-TLS-certificaat voor HTTPS-toegang via de browser. Browsers valideren certificaten voor lokale consoles op dezelfde manier als voor openbare websites: het certificaat moet vertrouwd en geldig zijn en overeenkomen met het adres dat wordt geopend.

Als uw browser het standaardcertificaat niet vertrouwt, of als het certificaat niet geldt voor het lokale IP-adres of de hostnaam die u hebt ingevoerd, toont de browser een waarschuwing. De waarschuwing betekent niet dat de KVM geen certificaat heeft. HTTPS kan de verbinding nog steeds versleutelen, maar de browser kan de identiteit van de KVM niet verifiëren.

## Hoe los ik de waarschuwing op? {#how-to-resolve-the-warning}

Controleer bij lokale toegang eerst of het adres bij uw KVM hoort. Klik vervolgens op **Advanced** en **Continue to "192.168.8.11"** (de exacte tekst verschilt per browser).

![Doorgaan naar 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

U wordt dan doorgestuurd naar de console van de GL.iNet KVM.

![Lokale toegang tot de KVM-beheerpagina](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## Kan ik mijn eigen certificaat gebruiken? {#can-i-use-my-own-certificate}

Ja. U kunt uw eigen SSL/TLS-certificaat op de KVM installeren en gebruiken. Volg de onderstaande stappen.

1. Verkrijg een SSL/TLS-certificaat dat geldt voor de hostnaam of het IP-adres waarmee u de KVM opent. Om browserwaarschuwingen te voorkomen, moet het certificaat geldig zijn en zijn uitgegeven door een certificeringsinstantie die uw browser vertrouwt. Een zelfondertekend certificaat leidt nog steeds tot een waarschuwing, tenzij u uw besturende apparaat expliciet zo configureert dat het dit certificaat vertrouwt.

2. Meld u aan bij de console van uw KVM. Klik rechtsboven op het schildpictogram om naar **Security** -> **TLS Certificate** te gaan.

    ![Eigen certificaat 1](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert1.png){class="glboxshadow"}

    Selecteer in het pop-upvenster **Custom Certificate** en upload uw certificaatbestand en privésleutel. Deze functie is beschikbaar vanaf firmware v1.8.0.

    ![Eigen certificaat 2](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert2.png){class="glboxshadow"}

    U kunt het certificaat en de privésleutel op de KVM ook vervangen via een SSH-terminal of WinSCP. Het certificaat en de sleutel staan in de volgende map:

    `/etc/kvmd/user/ssl`

    Vervang ze door uw nieuwe SSL-certificaat en privésleutel.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
