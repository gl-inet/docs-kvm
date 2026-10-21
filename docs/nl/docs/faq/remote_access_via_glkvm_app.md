# De KVM op afstand openen via de GLKVM-app {#how-to-access-kvm-remotely-via-glkvm-app}

Zorg er voordat u begint voor dat het bestuurde apparaat correct op de GL.iNet KVM is aangesloten en dat de KVM met een stabiel netwerk is verbonden.

Volg de onderstaande stappen om uw KVM en het bestuurde apparaat op afstand te openen via de GLKVM-app.

## Installeren en aanmelden {#install-and-log-in}

1. Installeer de [GLKVM-app](https://www.gl-inet.com/app-rm/){target="_blank"} op uw besturende apparaat.

2. Open de GLKVM-app en meld u aan met uw GL.iNet-account.

    ![Aanmelden](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Als u nog geen GL.iNet-account hebt, registreert u zich eerst en meldt u zich daarna aan.
    
    ![Registreren](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

## Uw KVM koppelen {#bind-your-kvm}

Na het aanmelden wordt de volgende pagina weergegeven. Klik op **Add Device**.

U kunt uw KVM op drie manieren koppelen: Auto Discover, S/N Code en Dynamic Binding Code.

![Apparaat toevoegen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

### Auto Discover {#auto-discover}

Dit moet in het lokale netwerk gebeuren. Zorg ervoor dat uw KVM en het besturende apparaat zich in hetzelfde LAN bevinden.

1. Klik op **Auto Discover**. Er wordt automatisch gezocht naar beschikbare KVM-apparaten.

    ![Automatisch zoeken 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

2. Zoek uw KVM en voer de **Device ID** in om het apparaat aan uw account te koppelen.

    ![Automatisch zoeken 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

### S/N Code {#sn-code}

Deze methode is bedoeld voor situaties waarin uw KVM niet wordt gevonden of zich niet in hetzelfde LAN bevindt, maar u wel het serienummer (S/N) hebt.

1. Klik op **S/N Code**.

2. Geef in het pop-upvenster een naam op voor uw apparaat en voer het serienummer in dat op het label aan de onderkant van uw KVM-apparaat staat.

    ![Serienummer](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

### Dynamic Binding Code {#dynamic-binding-code}

Voer een upgrade uit van de firmware van uw KVM naar v1.7 voordat u deze functie gebruikt.

Dit moet in het lokale netwerk gebeuren. Zorg ervoor dat uw KVM en het besturende apparaat zich in hetzelfde LAN bevinden.

1. Meld u lokaal aan bij uw KVM via de domeinnaam of het IP-adres. Klik [hier](../faq/local_access_via_browser.md) voor meer informatie.

2. Ga na het aanmelden rechtsboven naar **Cloud Service** en klik op **Bind With Code**.

    ![Koppelen met code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Er wordt willekeurig een dynamische code van 8 cijfers voor de apparaatkoppeling gegenereerd, die 60 seconden geldig is. Klik op de code om deze te kopiëren.

    ![Koppelen met code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Ga terug naar de GLKVM-app, voer de dynamische koppelingscode in en klik op **Bind**.

    ![Dynamische code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

## Externe toegang {#remote-access}

Zodra uw KVM-apparaat aan uw account is gekoppeld, wordt het in de app als "Online" weergegeven.

![Apparaat online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

Klik op uw KVM-apparaat. Er wordt een nieuw venster geopend en de verbinding wordt tot stand gebracht.

![Verbinding maken](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

Voer na het verbinden uw beheerderswachtwoord in om u aan te melden.

![Aanmelden na verbinding](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

U hebt nu toegang tot uw KVM-apparaat en via dit apparaat tot het bestuurde apparaat.

![Verbonden](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
