# De hostnaam van de KVM wijzigen {#how-to-change-kvm-hostname}

De standaardhostnaam van een GL.iNet KVM is **glkvm**. Dit betekent dat u de KVM in hetzelfde netwerk lokaal kunt openen via de domeinnaam `glkvm.local`.

In deze handleiding worden twee methoden beschreven om de hostnaam te wijzigen: via de KVM-console of via terminalopdrachten.

## Methode 1. KVM-console {#method-1-kvm-console}

> **Opmerking**: Deze functie is beschikbaar vanaf firmwareversie 1.7.0.

### Firmware v1.10 en hoger {#firmware-v110-and-above}

1.  Meld u aan bij uw KVM en klik in de navigatiebalk op het pictogram Settings om de instellingenpagina te openen.

    ![Netwerkinstellingen](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings-network.png){class="glboxshadow"}

2. Ga naar **Network** en voer de gewenste hostnaam in; de wijziging wordt dan van kracht.

    ![Hostnaam wijzigen](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify-hostname.png){class="glboxshadow"}

### Firmware v1.9 en eerder {#firmware-v19-and-earlier}

1. Meld u aan bij uw KVM en ga naar **Settings** -> **Network**. Klik op de hostnaam of op het pictogram met de pijl naar rechts.

    ![Netwerkinstellingen](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings_network.png){class="glboxshadow"}

2. Geef de gewenste hostnaam op en klik op **Apply**.

    ![Hostnaam wijzigen](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify_hostname.png){class="glboxshadow"}

## Methode 2. Terminalopdrachten {#method-2-terminal-commands}

1. Meld u aan bij uw KVM en ga naar **Toolbox** -> **Terminal**. Klik op **Access**.

    ![Terminal openen](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_terminal.png){class="glboxshadow"}

2. Voer in de terminal de volgende opdracht in en druk op Enter (vervang "example" door de gewenste hostnaam). Uw KVM wordt daarna opnieuw opgestart.

    `echo example > /etc/hostname && reboot`

    ![Opdracht invoeren](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/input_command.png){class="glboxshadow"}

3. Wacht tot de KVM opnieuw is opgestart. Daarna kunt u uw KVM openen met de nieuwe hostnaam.

    ![Openen met de nieuwe hostnaam](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_new_hostname.png){class="glboxshadow"}

    Als u de hostnaam bent vergeten of wilt controleren of de wijziging is doorgevoerd, voert u de volgende opdracht in de terminal in om de huidige hostnaam te bekijken.

    `cat /etc/hostname`

    ![Hostnaam controleren](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/verify_hostname.png){class="glboxshadow"}

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
