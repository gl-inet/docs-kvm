# Comet Q (GL-RMQ1) – snelle installatie {#comet-q-gl-rmq1-quick-setup}

Bekijk deze video of volg de onderstaande stappen om uw Comet Q in te stellen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6-f-XFkgYoU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Apparaten aansluiten {#connect-devices}

Voor de duidelijkheid: apparaat A is het besturende apparaat en apparaat B het bestuurde apparaat.

![Aansluiten 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect1.png){class="glboxshadow"}

1. Sluit de Type-C-kabel van de Comet Q aan op de Type-C-poort van apparaat B.

    ![Aansluiten 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect2.png){class="glboxshadow"}

2. Als apparaat B een mobiel apparaat met touchscreen is, zoals een smartphone of tablet, schakelt u eerst de toegankelijkheidsbediening in. Hierdoor kan de Comet Q het touchscreen bedienen.

    - iOS: **Settings** > **Accessibility** > **Touch** > schakel **AssistiveTouch** in.

    - Android: zoek in de instellingen naar **Mouse** of **Accessibility**. De menupaden verschillen per merk en model.

    ![Aansluiten 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect3.png){class="glboxshadow" width="600"}

3. Volg de instructies op het scherm om de eerste configuratie te voltooien. Zie [hier](../gl-rmq1/product_overview.md#touchscreen) voor meer informatie.

    ![Aansluiten 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect4.png){class="glboxshadow"}

## Lokale toegang {#local-access}

U kunt de Comet Q op twee manieren in het lokale netwerk openen: via de domeinnaam of via het IP-adres.

Zorg er vooraf voor dat uw besturende apparaat zich in hetzelfde LAN bevindt als de Comet Q.

### Domeinnaam {#domain}

1. Open een browser op het besturende apparaat. Voor een betere compatibiliteit wordt Chrome of Edge aanbevolen.

2. Voer `glkvm.local` in de adresbalk in. U wordt naar de aanmeldpagina van GLKVM geleid. Voer het beheerderswachtwoord in.

    ![Lokale toegang via domeinnaam](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Opmerking**: Bij de eerste toegang moet u een beheerderswachtwoord instellen.

3. Daarna kunt u de console van de Comet Q lokaal openen en krijgt u toegang tot het bestuurde apparaat.

    ![Lokale toegang via domeinnaam](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### IP-adres {#ip-address}

1. Verbind de Comet Q met een wifinetwerk en zoek het IP-adres op het touchscreen op. In dit voorbeeld is het IP-adres van de Comet Q `192.168.8.197`.

2. Open een browser en voer dit IP-adres in de adresbalk in. U wordt naar de aanmeldpagina van GLKVM geleid. Voer het beheerderswachtwoord in.

    ![Lokale toegang via IP-adres](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Opmerking**: Bij de eerste toegang moet u een beheerderswachtwoord instellen.

3. Daarna kunt u de console van de Comet Q lokaal openen en krijgt u toegang tot het bestuurde apparaat.

    ![Lokale toegang via IP-adres](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Externe toegang {#remote-access}

U kunt de Comet Q op verschillende manieren op afstand openen: via de cloudservice, de GLKVM-app, Tailscale en ZeroTier.

### Cloudservice {#cloud-service}

1. Koppel uw apparaat aan KVM Cloud. Dit moet in het lokale netwerk gebeuren.

    U kunt uw KVM op twee manieren aan de cloud koppelen: via reguliere koppeling of via koppeling met een dynamische code. Hier gebruiken we de reguliere koppeling als voorbeeld. Als u liever een dynamische code gebruikt, klikt u [hier](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} voor meer informatie.
    
    Open eerst lokaal uw Comet Q en ga rechtsboven naar **Cloud Service**. Klik op **Bind To Cloud**.

    ![Aan de cloud koppelen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    U wordt doorgestuurd naar een aanmeldpagina. Meld u aan met uw GL.iNet-cloudaccount.

    ![Aanmelden om het apparaat te koppelen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Controleer vervolgens de apparaatgegevens en klik op **Bind**.

    ![Apparaatkoppeling bevestigen](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Even later is uw Comet Q aan uw account gekoppeld. Klik op **Done**.

    ![Apparaat gekoppeld](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}
    
2. Externe toegang via de cloudservice.

    Open een browser (bijvoorbeeld Google Chrome) en voer `glkvm.com` in de adresbalk in. Er verschijnt een aanmeldpagina. Meld u aan met uw GL.iNet-account.

    ![Aanmelden voor externe toegang](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Na het aanmelden ziet u de apparaten die aan uw account zijn gekoppeld. Klik op het apparaat dat u op afstand wilt openen.

    ![Apparaat kiezen voor externe toegang](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    Voer op de nieuw geopende webpagina uw beheerderswachtwoord in om u aan te melden.

    ![Beheerderswachtwoord voor externe toegang](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Daarna kunt u via de cloud op afstand toegang krijgen tot uw Comet Q en het bestuurde apparaat, zonder de app te installeren.

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
    
        Dit moet in het lokale netwerk gebeuren. Zorg ervoor dat uw besturende apparaat zich in hetzelfde LAN bevindt als de Comet Q.
    
        Klik op **Auto Discover**. Het zoeken start automatisch.
    
        ![Automatisch zoeken 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}
        
        Zoek uw KVM en voer de apparaat-ID in om het apparaat aan uw account te koppelen.
    
        ![Automatisch zoeken 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}
    
    ??? "S/N Code"
    
        Deze methode is bedoeld voor situaties waarin uw KVM niet wordt gevonden of zich niet in hetzelfde LAN bevindt, maar u wel het serienummer (S/N) hebt.
        
        Klik op **S/N Code**. Geef in het pop-upvenster een apparaatnaam op en voer het serienummer in dat op het label aan de onderkant van uw KVM-apparaat staat.
    
        ![Serienummer](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}
    
    ??? "Dynamic Binding Code"
    
        Dit moet in het lokale netwerk gebeuren. Zorg ervoor dat uw besturende apparaat zich in hetzelfde LAN bevindt als de Comet Q.
    
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

De Comet Q is geïntegreerd met Tailscale, zodat u het apparaat op afstand kunt openen via het virtuele netwerk van Tailscale.

Ga in de console naar **Apps Center** -> **Tailscale**, schakel de functie in en koppel uw Comet Q aan uw Tailscale-account.

Koppel vervolgens uw besturende apparaat aan hetzelfde account. Daarna kunt u uw Comet Q op afstand openen door het **Tailscale virtual IP** ervan in te voeren in een webbrowser op het besturende apparaat, zonder de GLKVM-app te installeren.

Zie [hier](../../faq/remote_access_via_tailscale.md){target="_blank"} voor meer informatie.

### ZeroTier {#zerotier}

De Comet Q is geïntegreerd met ZeroTier, zodat u het apparaat op afstand kunt openen via het virtuele netwerk van ZeroTier.

Ga in de console naar **Apps Center** -> **ZeroTier** en schakel de functie in.

Voeg vervolgens zowel de Comet Q als uw besturende apparaat toe aan hetzelfde ZeroTier-netwerk (met een alfanumerieke netwerk-ID van 16 tekens). Daarna kunt u uw Comet Q op afstand openen door het **ZeroTier IP** ervan in te voeren in een webbrowser op het besturende apparaat, zonder de GLKVM-app te installeren.

Zie [hier](../../faq/remote_access_via_zerotier.md){target="_blank"} voor meer informatie.
