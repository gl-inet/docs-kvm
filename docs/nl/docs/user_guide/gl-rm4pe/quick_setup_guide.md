# Comet X (GL-RM4PE) – snelle installatie {#comet-x-gl-rm4pe-quick-setup}

## Apparaten aansluiten {#connect-devices}

Voor de duidelijkheid: apparaat A is het besturende apparaat en apparaat B het bestuurde apparaat.

![Aansluiten 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect1.png){class="glboxshadow"}

1. Sluit de Comet X met een ethernetkabel aan op een PoE-switch of voorzie het apparaat van stroom met een voedingsadapter van 5V/3A.

    ![Aansluiten 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect2.png){class="glboxshadow"}

    ***Opmerking**: Als u een voedingsadapter gebruikt, sluit u de Comet X voor internettoegang met een ethernetkabel aan op een netwerkapparaat (zoals een router).*

2. Verbind de **HDMI IN**-poort van de Comet X met een HDMI-kabel met apparaat B. Hiermee wordt het videosignaal overgedragen.

    ![Aansluiten 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect3.png){class="glboxshadow"}

3. Verbind de **USB-C**-poort van de Comet X met een USB-kabel met apparaat B. Deze USB-C-poort moet bij de bijbehorende HDMI IN-poort horen om toetsenbord- en muissignalen correct over te dragen.

    ![Aansluiten 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect4.png){class="glboxshadow"}

4. (Optioneel) Sluit de **HDMI OUT**-poort van de Comet X aan op een externe monitor om het beeld te dupliceren (video-loopout). Zie [Lokale bediening](#local-control) voor meer informatie.

5. De aansluiting is voltooid. U kunt de console van de Comet X nu lokaal of op afstand openen.

## Montage in een rack {#rack-mounting}

Monteer de Comet X naar behoefte op de rails van een serverrack.

1. Bevestig de montagebeugels met de meegeleverde schroeven aan de Comet X.

    ![Installatie 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install1.png){class="glboxshadow"}

2. Zet de Comet X met rackschroeven vast op de rackrails. **Rackschroeven worden niet meegeleverd**.

    ![Installatie 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install2.png){class="glboxshadow"}

## Lokale bediening {#local-control}

Bedien het apparaat rechtstreeks via fysieke kabels, zonder netwerk, IP-adres of domeinnaam.

De Comet X heeft een HDMI OUT-poort en twee extra USB-poorten, ideaal voor lokale probleemoplossing, configuratie en installatie van een besturingssysteem. Sluit eenvoudig uw monitor, muis en toetsenbord aan voor plug-and-play lokale bediening van de hardware.

1. Sluit de **HDMI OUT**-poort op het achterpaneel van de Comet X aan op een externe monitor om het beeld te dupliceren (video-loopout).

    ![Lokale bediening 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control1.png){class="glboxshadow"}

2. Sluit een toetsenbord en muis aan op de USB-poorten op het voorpaneel van de Comet X.

    ![Lokale bediening 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control2.png){class="glboxshadow"}

3. U kunt de aangesloten apparaten nu bedienen met uw lokale toetsenbord en muis, terwijl de videosignalen worden doorgegeven aan de lokale monitor.

## Toegang via het LAN {#lan-access}

U kunt de Comet X op twee manieren in het lokale netwerk openen: via de domeinnaam of via het IP-adres.

Zorg er vooraf voor dat uw besturende apparaat zich in hetzelfde LAN bevindt als de Comet X.

### Domeinnaam {#domain}

1. Open een browser op het besturende apparaat. Voor een betere compatibiliteit wordt Chrome of Edge aanbevolen.

2. Voer `glkvm.local` in de adresbalk in. U wordt naar de aanmeldpagina van GLKVM geleid. Voer het beheerderswachtwoord in.

    ![Lokale toegang via domeinnaam](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain1.png){class="glboxshadow"}

    ***Opmerking**: Bij de eerste toegang moet u een beheerderswachtwoord instellen.*

3. Daarna kunt u de console van de Comet X lokaal openen en krijgt u toegang tot het bestuurde apparaat.

    ![Lokale toegang via domeinnaam](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain2.png){class="glboxshadow"}

### IP-adres {#ip-address}

1. Zoek het IP-adres van de Comet X op het touchscreen op. In dit voorbeeld is het IP-adres van de Comet X `192.168.8.197`.

2. Open een browser en voer dit IP-adres in de adresbalk in. U wordt naar de aanmeldpagina van GLKVM geleid. Voer het beheerderswachtwoord in.

    ![Lokale toegang via IP-adres](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip1.png){class="glboxshadow"}

    ***Opmerking**: Bij de eerste toegang moet u een beheerderswachtwoord instellen.*

3. Daarna kunt u de console van de Comet X lokaal openen en krijgt u toegang tot het bestuurde apparaat.

    ![Lokale toegang via IP-adres](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip2.png){class="glboxshadow"}

## Externe toegang {#remote-access}

U kunt de Comet X op verschillende manieren op afstand openen: via de cloudservice, de GLKVM-app, Tailscale en ZeroTier.

### Cloudservice {#cloud-service}

1. Koppel uw apparaat aan KVM Cloud. Dit moet in het lokale netwerk gebeuren.

    U kunt uw KVM op twee manieren aan de cloud koppelen: via reguliere koppeling of via koppeling met een dynamische code. Hier gebruiken we de reguliere koppeling als voorbeeld. Als u liever een dynamische code gebruikt, klikt u [hier](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} voor meer informatie.

    Open eerst lokaal uw Comet X en ga rechtsboven naar **Cloud Service**. Klik op **Bind To KVMCloud**.

    ![Aan de cloud koppelen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_to_cloud.png){class="glboxshadow"}

    U wordt doorgestuurd naar een aanmeldpagina. Meld u aan met uw GL.iNet-cloudaccount.

    ![Apparaat koppelen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind1.png){class="glboxshadow"}

    Controleer vervolgens de apparaatgegevens en klik op **Bind**.

    ![Apparaat koppelen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind2.png){class="glboxshadow"}

    Wacht even. Uw Comet X wordt aan uw account gekoppeld. Klik op **Done**.

    ![Apparaat gekoppeld](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind_success.png){class="glboxshadow"}

2. Externe toegang via de cloudservice.

    Nadat u op Done hebt geklikt, wordt u doorgestuurd naar een website met het domein `glkvm.com`, waar u uw apparaat ziet.

    ![Lijst met cloudapparaten](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_devices.png){class="glboxshadow"}

    ***Tip**: Als u niet wordt doorgestuurd, voert u `glkvm.com` handmatig in de adresbalk in en meldt u zich aan met uw GL.iNet-account. Na het aanmelden ziet u het apparaat dat aan uw account is gekoppeld.*
    
    Klik op het apparaat dat u op afstand wilt openen.
    
    ![Toegang via de cloud](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access.png){class="glboxshadow"}
    
    Er wordt een nieuwe webpagina geopend. Voer uw beheerderswachtwoord in om u aan te melden.

    ![Toegang via de cloud 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access1.png){class="glboxshadow"}
    
    Daarna kunt u via de cloud op afstand toegang krijgen tot uw Comet X en het bestuurde apparaat.

    ![Toegang via de cloud 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access2.png){class="glboxshadow"}

### GLKVM-app {#glkvm-app}

1. Installeer de [GLKVM-app](https://www.gl-inet.com/app-rm/){target="_blank"} op uw besturende apparaat.

2. Meld u aan met uw GL.iNet-account.

    ![Aanmelden](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_login.jpg){class="glboxshadow"}

    Als u nog geen account hebt, registreert u zich eerst en meldt u zich daarna aan.
    
    ![Registreren](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_signup.png){class="glboxshadow"}

3. Koppel uw apparaat.

    Na het aanmelden wordt de volgende pagina weergegeven. Klik op **Add Device**.

    ![Apparaat toevoegen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_add_device.png){class="glboxshadow"}

    U kunt uw apparaat op drie manieren koppelen: Auto Discover, S/N Code en Dynamic Binding Code.

    ??? "Auto Discover"
    
        Dit moet in het lokale netwerk gebeuren. Zorg ervoor dat uw besturende apparaat zich in hetzelfde LAN bevindt als de Comet X en houd de apparaat-ID van uw KVM bij de hand.
    
        Klik op **Auto Discover**. Het zoeken wordt gestart.
    
        ![Automatisch zoeken 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover1.png){class="glboxshadow"}
        
        Zoek uw KVM en voer de **Device ID** in om het apparaat aan uw account te koppelen.
    
        ![Automatisch zoeken 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover2.png){class="glboxshadow"}

        ![Automatisch zoeken 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover3.png){class="glboxshadow"}
    
    ??? "S/N Code"
    
        Deze methode is bedoeld voor situaties waarin uw KVM niet wordt gevonden of zich niet in hetzelfde LAN bevindt, maar u wel het serienummer (S/N) hebt.
        
        Klik op **S/N Code**. Geef in het pop-upvenster een apparaatnaam op en voer het serienummer in dat op de onderkant van het KVM-apparaat staat.
    
        ![Serienummer](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/add_sncode.png){class="glboxshadow"}
    
    ??? "Dynamic Binding Code"
    
        Dit moet in het lokale netwerk gebeuren. Zorg ervoor dat uw besturende apparaat zich in hetzelfde LAN bevindt als de Comet X.
    
        1. Meld u lokaal aan bij uw KVM via de domeinnaam of het IP-adres. Klik [hier](#lan-access) voor meer informatie.
    
        2. Ga rechtsboven naar **Cloud Service** en klik op **Bind With Code**.
    
            ![Koppelen met code 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code1.png){class="glboxshadow"}
    
        3. Er wordt willekeurig een dynamische code van 8 cijfers voor de apparaatkoppeling gegenereerd, die 60 seconden geldig is. Klik op de code om deze te kopiëren.
    
            ![Koppelen met code 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code2.png){class="glboxshadow"}
    
        4. Ga terug naar de GLKVM-app, voer de dynamische koppelingscode in en klik op **Bind**.
    
            ![Dynamische code](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code3.png){class="glboxshadow"}

4. Externe toegang via de GLKVM-app.

    Zodra uw KVM-apparaat aan uw account is gekoppeld, wordt het in de app als "Online" weergegeven.

    ![Apparaat online in de app](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_devices.png){class="glboxshadow"}

    Klik op uw KVM-apparaat. Er wordt een nieuw venster geopend en de verbinding wordt tot stand gebracht.

    ![Verbinding maken in de app](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_connecting.png){class="glboxshadow"}

    Voer na het verbinden uw beheerderswachtwoord in om u bij uw apparaat aan te melden.

    ![Toegang via de app 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access1.png){class="glboxshadow"}

    Daarna hebt u toegang tot uw KVM-apparaat en via dit apparaat tot het bestuurde apparaat.

    ![Toegang via de app 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access2.png){class="glboxshadow"}

### Tailscale {#tailscale}

De Comet X is geïntegreerd met Tailscale, zodat u het apparaat op afstand kunt openen via het virtuele netwerk van Tailscale.

Ga in de console naar **Apps Center** -> **Tailscale**, schakel de functie in en koppel uw Comet X aan uw Tailscale-account.

Koppel vervolgens uw besturende apparaat aan hetzelfde account. Daarna kunt u uw Comet X op afstand openen door het **Tailscale virtual IP** ervan in te voeren in een webbrowser op het besturende apparaat, zonder de GLKVM-app te installeren.

Zie [hier](../../faq/remote_access_via_tailscale.md){target="_blank"} voor meer informatie.

### ZeroTier {#zerotier}

De Comet X is geïntegreerd met ZeroTier, zodat u het apparaat op afstand kunt openen via het virtuele netwerk van ZeroTier.

Ga in de console naar **Apps Center** -> **ZeroTier** en schakel de functie in.

Voeg vervolgens zowel de Comet X als uw besturende apparaat toe aan hetzelfde ZeroTier-netwerk (met een alfanumerieke netwerk-ID van 16 tekens). Daarna kunt u uw Comet X op afstand openen door het **ZeroTier IP** ervan in te voeren in een webbrowser op het besturende apparaat, zonder de GLKVM-app te installeren.

Zie [hier](../../faq/remote_access_via_zerotier.md){target="_blank"} voor meer informatie.
