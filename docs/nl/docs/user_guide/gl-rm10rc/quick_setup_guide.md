# Comet 5G (GL-RM10RC) – snelle installatie {#comet-5g-gl-rm10rc-quick-setup}

Bekijk deze video of volg de onderstaande stappen om uw Comet 5G in te stellen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/whAUMBcIIZs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Apparaten aansluiten {#connect-devices}

Voor de duidelijkheid: apparaat A is het besturende apparaat en apparaat B het bestuurde apparaat.

![Apparaten aansluiten](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/connect_device.png){class="glboxshadow"}

1. Plaats een simkaart in uw Comet 5G en schakel het apparaat in.

    ![Simkaart plaatsen en inschakelen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/01-insert-sim-power-on.jpg){class="glboxshadow"}

2. Verbind de HDMI IN-poort van de Comet 5G met de HDMI-poort van apparaat B. Sluit indien nodig de HDMI OUT-poort van de Comet 5G met een tweede HDMI-kabel aan op een externe monitor.

    ![De HDMI-kabel aansluiten](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/02-hdmi-cable.jpg){class="glboxshadow"}

3. Verbind de Type-C-poort van de Comet 5G met een USB-C-kabel met de Type-C-aansluiting van apparaat B.

    ![De USB-kabel aansluiten](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/03-usb-cable.jpg){class="glboxshadow"}

4. Verbind de Comet 5G met een netwerkbron.

    - 5G: als er een simkaart is geplaatst, wordt de 5G-verbinding automatisch tot stand gebracht bij het opstarten van het systeem.

    - Wifi: veeg op het touchscreen naar links en verbind de Comet 5G met een bestaand wifinetwerk (2.4G en 5G ondersteund).

        ![Verbinden via wifi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/04-network-wifi.png){class="glboxshadow"}

    - Ethernet: sluit de ethernetpoort van de Comet 5G aan op een netwerkbron.

        ![Verbinden via ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/04-network-ethernet.png){class="glboxshadow"}

    !!! Note "Opmerking"
        De verbindingsprioriteit is **Ethernet** > **Wi-Fi** > **5G**. Zie [**hier**](../../faq/wan_network_detection_and_failover_logic_of_comet5g.md) voor de volledige logica van WAN-netwerkdetectie en failover.

5. De apparaten zijn aangesloten. U kunt de console van de Comet 5G nu openen via bediening in de buurt, lokale toegang of externe toegang.

## Bediening in de buurt {#nearby-control}

Bediening in de buurt is ideaal voor snelle installatie en beheer wanneer u zich in de buurt van de Comet 5G bevindt.

Zet op het touchscreen de wifinetwerkmodus op **AP Mode**. Er wordt dan een unieke wifi-SSID gegenereerd en de netwerkgegevens worden op het scherm weergegeven.

![Toegang in de buurt](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/nearby_access1.png){class="glboxshadow gl-80-desktop"}

Verbind een apparaat met deze wifi-SSID. Daarna kunt u de console van de Comet 5G in een webbrowser openen via het standaard-IP-adres (192.168.8.1).

![Toegang in de buurt](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/nearby_access2.png){class="glboxshadow"}

## Lokale toegang {#local-access}

U kunt de Comet 5G op twee manieren in het lokale netwerk openen: via de domeinnaam of via het IP-adres.

Zorg er vooraf voor dat uw besturende apparaat zich in hetzelfde LAN bevindt als de Comet 5G.

### Domeinnaam {#domain}

1. Open een browser op het besturende apparaat. Voor een betere compatibiliteit wordt Chrome of Edge aanbevolen.

2. Voer `glkvm.local` in de adresbalk in. U wordt naar de aanmeldpagina van GLKVM geleid. Voer het beheerderswachtwoord in.

    ![Lokale toegang via domeinnaam](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Opmerking**: Bij de eerste toegang moet u een beheerderswachtwoord instellen.

3. Daarna kunt u de console van de Comet 5G lokaal openen en krijgt u toegang tot het bestuurde apparaat.

    ![Lokale toegang via domeinnaam](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### IP-adres {#ip-address}

1. Zoek het IP-adres van de Comet 5G op het touchscreen op. In dit voorbeeld is het IP-adres van de Comet 5G `192.168.8.197`.

2. Open een browser en voer dit IP-adres in de adresbalk in. U wordt naar de aanmeldpagina van GLKVM geleid. Voer het beheerderswachtwoord in.

    ![Lokale toegang via IP-adres](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Opmerking**: Bij de eerste toegang moet u een beheerderswachtwoord instellen.

3. Daarna kunt u de console van de Comet 5G lokaal openen en krijgt u toegang tot het bestuurde apparaat.

    ![Lokale toegang via IP-adres](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Externe toegang {#remote-access}

U kunt de Comet 5G op verschillende manieren op afstand openen: via de cloudservice, de GLKVM-app, Tailscale, ZeroTier en NetBird.

### Cloudservice {#cloud-service}

1. Koppel uw apparaat aan KVM Cloud. Dit moet in het lokale netwerk gebeuren.

    U kunt uw KVM op twee manieren aan de cloud koppelen: via reguliere koppeling of via koppeling met een dynamische code. Hier gebruiken we de reguliere koppeling als voorbeeld. Als u liever een dynamische code gebruikt, klikt u [hier](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} voor meer informatie.
    
    Open eerst lokaal uw Comet 5G en ga rechtsboven naar **Cloud Service**. Klik op **Bind To Cloud**.

    ![Aan de cloud koppelen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    U wordt doorgestuurd naar een aanmeldpagina. Meld u aan met uw GL.iNet-cloudaccount.

    ![Aanmelden om het apparaat te koppelen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Controleer vervolgens de apparaatgegevens en klik op **Bind**.

    ![Apparaatkoppeling bevestigen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Even later is uw Comet 5G aan uw account gekoppeld. Klik op **Done**.

    ![Apparaat gekoppeld](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}
    
2. Externe toegang via de cloudservice.

    Open een browser (bijvoorbeeld Google Chrome) en voer `glkvm.com` in de adresbalk in. Er verschijnt een aanmeldpagina. Meld u aan met uw GL.iNet-account.

    ![Aanmelden voor externe toegang](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Na het aanmelden ziet u de apparaten die aan uw account zijn gekoppeld. Klik op het apparaat dat u op afstand wilt openen.

    ![Apparaat kiezen voor externe toegang](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    Voer op de nieuw geopende webpagina uw beheerderswachtwoord in om u aan te melden.

    ![Beheerderswachtwoord voor externe toegang](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Daarna kunt u via de cloud op afstand toegang krijgen tot uw Comet 5G en het bestuurde apparaat, zonder de app te installeren.

    ![Externe toegang gelukt](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

### GLKVM-app {#glkvm-app}

1. Installeer de [GLKVM-app](https://www.gl-inet.com/app-rm/){target="_blank"} op uw besturende apparaat.

2. Meld u aan met uw GL.iNet-account.

    ![Aanmelden](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Als u nog geen account hebt, registreert u zich eerst en meldt u zich daarna aan.
    
    ![Registreren](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

3. Koppel uw apparaat.

    Na het aanmelden wordt de volgende pagina weergegeven. Klik op **Add Device**.

    ![Apparaat toevoegen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

    U kunt uw apparaat op drie manieren koppelen: Auto Discover, S/N Code en Dynamic Binding Code.

    ??? "Auto Discover"
    
        Dit moet in het lokale netwerk gebeuren. Zorg ervoor dat uw besturende apparaat zich in hetzelfde LAN bevindt als de Comet 5G.
    
        Klik op **Auto Discover**. Het zoeken start automatisch.
    
        ![Automatisch zoeken 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}
        
        Zoek uw KVM en voer de apparaat-ID in om het apparaat aan uw account te koppelen.
    
        ![Automatisch zoeken 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}
    
    ??? "S/N Code"
    
        Deze methode is bedoeld voor situaties waarin uw KVM niet wordt gevonden of zich niet in hetzelfde LAN bevindt, maar u wel het serienummer (S/N) hebt.
        
        Klik op **S/N Code**. Geef in het pop-upvenster een apparaatnaam op en voer het serienummer in dat op het label aan de onderkant van uw KVM-apparaat staat.
    
        ![Serienummer](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}
    
    ??? "Dynamic Binding Code"
    
        Dit moet in het lokale netwerk gebeuren. Zorg ervoor dat uw besturende apparaat zich in hetzelfde LAN bevindt als de Comet 5G.
    
        1. Meld u lokaal aan bij uw KVM via de domeinnaam of het IP-adres. Klik [hier](../../faq/local_access_via_browser.md) voor meer informatie.
    
        2. Ga rechtsboven naar **Cloud Service** en klik op **Bind With Code**.
    
            ![Koppelen met code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}
    
        3. Er wordt willekeurig een dynamische code van 8 cijfers voor de apparaatkoppeling gegenereerd, die 60 seconden geldig is. Klik op de code om deze te kopiëren.
    
            ![Koppelen met code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}
    
        4. Ga terug naar de GLKVM-app, voer de dynamische koppelingscode in en klik op **Bind**.
    
            ![Dynamische code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

4. Externe toegang via de GLKVM-app.

    Zodra uw KVM-apparaat aan uw account is gekoppeld, wordt het in de app als "Online" weergegeven.

    ![Apparaat online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

    Klik op uw KVM-apparaat. Er wordt een nieuw venster geopend en de verbinding wordt tot stand gebracht.

    ![Verbinding maken](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

    Voer na het verbinden het beheerderswachtwoord in om u bij uw apparaat aan te melden.

    ![Aanmelden na verbinding](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

    Daarna hebt u toegang tot uw KVM-apparaat en via dit apparaat tot het bestuurde apparaat.

    ![Verbonden](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

### Tailscale {#tailscale}

De Comet 5G is geïntegreerd met Tailscale, zodat u het apparaat op afstand kunt openen via het virtuele netwerk van Tailscale.

Ga in de console naar **Apps Center** -> **Tailscale**, schakel de functie in en koppel uw Comet 5G aan uw Tailscale-account.

Koppel vervolgens uw besturende apparaat aan hetzelfde account. Daarna kunt u uw Comet 5G op afstand openen door het **Tailscale virtual IP** ervan in te voeren in een webbrowser op het besturende apparaat, zonder de GLKVM-app te installeren.

Zie [hier](../../faq/remote_access_via_tailscale.md){target="_blank"} voor meer informatie.

### ZeroTier {#zerotier}

De Comet 5G is geïntegreerd met ZeroTier, zodat u het apparaat op afstand kunt openen via het virtuele netwerk van ZeroTier.

Ga in de console naar **Apps Center** -> **ZeroTier** en schakel de functie in.

Voeg vervolgens zowel de Comet 5G als uw besturende apparaat toe aan hetzelfde ZeroTier-netwerk (met een alfanumerieke netwerk-ID van 16 tekens). Daarna kunt u uw Comet 5G op afstand openen door het **ZeroTier IP** ervan in te voeren in een webbrowser op het besturende apparaat, zonder de GLKVM-app te installeren.

Zie [hier](../../faq/remote_access_via_zerotier.md){target="_blank"} voor meer informatie.

### NetBird {#netbird}

De Comet 5G is geïntegreerd met NetBird, zodat u het apparaat op afstand kunt openen via het virtuele netwerk van NetBird.

Ga in de console naar **Apps Center** -> **NetBird**, schakel de functie in en koppel uw Comet 5G aan uw NetBird-account.

Koppel vervolgens uw besturende apparaat aan hetzelfde account. Daarna kunt u uw Comet 5G op afstand openen door het **NetBird virtual IP** ervan in te voeren in een webbrowser op het besturende apparaat, zonder de GLKVM-app te installeren.

Zie [hier](../../faq/remote_access_via_netbird.md){target="_blank"} voor meer informatie.
