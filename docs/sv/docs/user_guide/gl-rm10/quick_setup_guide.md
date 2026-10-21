# Snabbinstallation av Comet Pro (GL-RM10) {#comet-pro-gl-rm10-quick-setup}

Se den här videon eller följ stegen nedan för att konfigurera din Comet Pro.

<iframe width="560" height="315" src="https://www.youtube.com/embed/onxj5EEf9Ys" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Anslut enheterna {#connect-devices}

För tydlighetens skull avser enhet A den styrande enheten och enhet B den styrda enheten.

![Anslut enheterna](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/connect-devices.png){class="glboxshadow"}

1. Anslut Comet Pro till strömförsörjningen.

    ![Slå på strömmen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/01-power-on.png){class="glboxshadow"}

2. Anslut Comet Pro:s HD IN-port till enhet B:s HD OUT-port med en HDMI-kabel. Använd vid behov ytterligare en HD-kabel för att ansluta Comet Pro:s HD OUT-port till en extern skärm.

    ![Anslut HD-kabeln](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/02-hd-cable.png){class="glboxshadow"}

3. Anslut Comet Pro:s USB Type-C-port till enhet B:s USB-port med en USB-kabel.

    ![Anslut USB-kabeln](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/03-usb-cable.png){class="glboxshadow"}

4. Anslut Comet Pro till en nätverkskälla med en Ethernet-kabel eller via Wi-Fi.

    - Ethernet: anslut Comet Pro:s Ethernet-port till en nätverkskälla.

        ![Anslut via Ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/04-ethernet.png){class="glboxshadow"}

    - Wi-Fi: svep åt vänster på pekskärmen och anslut Comet Pro till ett befintligt Wi-Fi-nätverk (2,4G/5G stöds).

        ![Anslut via Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/04-wifi.png){class="glboxshadow"}

5. Enheterna är nu anslutna. Du kan nu komma åt Comet Pro:s konsol lokalt eller på distans.

## Lokal åtkomst {#local-access}

Det finns två sätt att komma åt Comet Pro i det lokala nätverket: via domännamn eller IP-adress.

Kontrollera före åtkomsten att den styrande enheten finns i samma LAN som Comet Pro.

### Domän {#domain}

1. Starta en webbläsare på den styrande enheten. Chrome eller Edge rekommenderas för bättre kompatibilitet.

2. Ange `glkvm.local` i adressfältet. Du kommer till inloggningssidan för GLKVM. Ange administratörslösenordet.

    ![Lokal åtkomst via domän](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Obs!** Du behöver ange ett administratörslösenord första gången du loggar in.

3. Du kan sedan komma åt Comet Pro:s konsol lokalt och få åtkomst till den styrda enheten.

    ![Lokal åtkomst via domän](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### IP-adress {#ip-address}

1. Ta reda på Comet Pro:s IP-adress på pekskärmen. I det här exemplet är Comet Pro:s IP-adress `192.168.8.197`.

2. Starta en webbläsare och ange den här IP-adressen i adressfältet. Du kommer till inloggningssidan för GLKVM. Ange administratörslösenordet.

    ![Lokal åtkomst via IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Obs!** Du behöver ange ett administratörslösenord första gången du loggar in.

3. Du kan sedan komma åt Comet Pro:s konsol lokalt och få åtkomst till den styrda enheten.

    ![Lokal åtkomst via IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Fjärråtkomst {#remote-access}

Det finns flera sätt att komma åt Comet Pro på distans: via molntjänsten, GLKVM-appen, Tailscale, ZeroTier och NetBird.

### Molntjänst {#cloud-service}

1. Koppla din enhet till KVM Cloud. Detta måste göras i det lokala nätverket.

    Det finns två sätt att koppla din KVM till molnet: vanlig koppling eller koppling med dynamisk kod. Här används vanlig koppling som exempel. Om du föredrar koppling med dynamisk kod kan du klicka [här](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} för mer information.

    Öppna först Comet Pro lokalt och gå till **Cloud Service** i det övre högra hörnet. Klicka på **Bind To Cloud**.

    ![Koppla till molnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    Du omdirigeras till en inloggningssida. Logga in med ditt GL.iNet-molnkonto.

    ![Inloggning för att koppla enheten](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Bekräfta sedan enhetsinformationen och klicka på **Bind**.

    ![Bekräfta koppling av enheten](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Vänta ett ögonblick så kopplas din Comet Pro till ditt konto. Klicka på **Done**.

    ![Enheten har kopplats](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Fjärråtkomst via molntjänsten.

    Öppna en webbläsare (här används Google Chrome som exempel) och ange `glkvm.com` i adressfältet. En inloggningssida visas. Logga in med ditt GL.iNet-konto.

    ![Inloggning för fjärråtkomst](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    När du har loggat in visas de enheter som är kopplade till ditt konto. Klicka på den enhet som du vill komma åt på distans.

    ![Välj enhet för fjärråtkomst](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    Ange administratörslösenordet på den nya webbsidan för att logga in.

    ![Administratörsinloggning vid fjärråtkomst](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Du kan sedan komma åt din Comet Pro och den styrda enheten på distans via molnet, utan att installera appen.

    ![Fjärråtkomst lyckades](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

### GLKVM-appen {#glkvm-app}

1. Installera [GLKVM-appen](https://www.gl-inet.com/app-rm/){target="_blank"} på den styrande enheten.

2. Logga in med ditt GL.iNet-konto.

    ![Logga in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Om du inte har något konto registrerar du dig först och loggar sedan in.

    ![Registrera dig](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

3. Koppla din enhet.

    När du har loggat in visas sidan nedan. Klicka på **Add Device**.

    ![Lägg till enhet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

    Du kan koppla enheten på tre sätt: Auto Discover, S/N Code och Dynamic Binding Code.

    ??? "Auto Discover"

        Detta måste göras i det lokala nätverket. Kontrollera att den styrande enheten finns i samma LAN som Comet Pro.

        Klicka på **Auto Discover**. Sökningen startar automatiskt.

        ![Automatisk identifiering 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

        Leta upp din KVM och ange dess enhets-ID för att koppla den till ditt konto.

        ![Automatisk identifiering 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

    ??? "S/N Code"

        Detta gäller om din KVM inte hittas eller inte finns i samma LAN, men du har dess serienummer (S/N).

        Klicka på **S/N Code**. I popup-fönstret anger du ett eget enhetsnamn och serienumret, som finns tryckt på etiketten på undersidan av KVM-enheten.

        ![Serienummer](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Detta måste göras i det lokala nätverket. Kontrollera att den styrande enheten finns i samma LAN som Comet Pro.

        1. Logga in på din KVM lokalt via domännamn eller IP-adress. Klicka [här](../../faq/local_access_via_browser.md) för mer information.

        2. Gå till **Cloud Service** i det övre högra hörnet och klicka på **Bind With Code**.

            ![Koppla med kod 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

        3. En slumpmässig, åttasiffrig dynamisk kod för koppling av enheten genereras. Den är giltig i 60 sekunder. Klicka på koden för att kopiera den.

            ![Koppla med kod 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

        4. Gå tillbaka till GLKVM-appen, ange den dynamiska kopplingskoden och klicka på **Bind**.

            ![Dynamisk kod](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

4. Fjärråtkomst via GLKVM-appen.

    När KVM-enheten har kopplats till ditt konto visas den som "Online" i appen.

    ![Enheten är online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

    Klicka på din KVM-enhet. Ett nytt fönster öppnas och anslutningen startar.

    ![Ansluter](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

    När anslutningen är upprättad anger du administratörslösenordet för att logga in på enheten.

    ![Inloggning efter anslutning](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

    Du kommer sedan åt KVM-enheten och via den den styrda enheten.

    ![Ansluten åtkomst](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

### Tailscale {#tailscale}

Comet Pro är integrerad med Tailscale, så att du kan komma åt den på distans via det virtuella Tailscale-nätverket.

Gå till **Apps Center** -> **Tailscale** i konsolen, aktivera funktionen och koppla din Comet Pro till ditt Tailscale-konto.

Koppla sedan den styrande enheten till samma konto. Därefter kan du komma åt din Comet Pro på distans genom att ange dess **Tailscale virtual IP** i en webbläsare på den styrande enheten, utan att installera GLKVM-appen.

Mer information finns [här](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier {#zerotier}

Comet Pro är integrerad med ZeroTier, så att du kan komma åt den på distans via det virtuella ZeroTier-nätverket.

Gå till **Apps Center** -> **ZeroTier** i konsolen och aktivera funktionen.

Anslut sedan både Comet Pro och den styrande enheten till samma ZeroTier-nätverk (med ett alfanumeriskt nätverks-ID på 16 tecken). Därefter kan du komma åt din Comet Pro på distans genom att ange dess **ZeroTier IP** i en webbläsare på den styrande enheten, utan att installera GLKVM-appen.

Mer information finns [här](../../faq/remote_access_via_zerotier.md){target="_blank"}.

### NetBird {#netbird}

Comet Pro är integrerad med NetBird, så att du kan komma åt den på distans via det virtuella NetBird-nätverket.

Gå till **Apps Center** -> **NetBird** i konsolen, aktivera funktionen och koppla din Comet Pro till ditt NetBird-konto.

Koppla sedan den styrande enheten till samma konto. Därefter kan du komma åt din Comet Pro på distans genom att ange dess **NetBird virtual IP** i en webbläsare på den styrande enheten, utan att installera GLKVM-appen.

Mer information finns [här](../../faq/remote_access_via_netbird.md){target="_blank"}.
