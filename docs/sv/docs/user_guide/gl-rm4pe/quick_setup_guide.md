# Snabbinstallation av Comet X (GL-RM4PE) {#comet-x-gl-rm4pe-quick-setup}

## Anslut enheterna {#connect-devices}

För tydlighetens skull avser enhet A den styrande enheten och enhet B den styrda enheten.

![Anslutning 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect1.png){class="glboxshadow"}

1. Anslut Comet X till en PoE-switch med en Ethernet-kabel, eller strömförsörj den med en nätadapter på 5V/3A.

    ![Anslutning 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect2.png){class="glboxshadow"}

    ***Obs!** Om du använder en nätadapter för strömförsörjningen ansluter du Comet X till en nätverksenhet (till exempel en router) med en Ethernet-kabel för internetåtkomst.*

2. Anslut Comet X:s **HDMI IN**-port till enhet B med en HDMI-kabel. Detta möjliggör överföring av videosignalen.

    ![Anslutning 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect3.png){class="glboxshadow"}

3. Anslut Comet X:s **USB-C**-port till enhet B med en USB-kabel. USB-C-porten måste höra ihop med motsvarande HDMI IN-port för att tangentbords- och mussignalerna ska överföras korrekt.

    ![Anslutning 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect4.png){class="glboxshadow"}

4. (Valfritt) Anslut Comet X:s **HDMI OUT**-port till en extern skärm för att spegla bilden (videovidarekoppling). Mer information finns i [Lokal styrning](#local-control).

5. Anslutningen är klar. Du kan nu komma åt Comet X:s konsol lokalt eller på distans.

## Rackmontering {#rack-mounting}

Montera vid behov Comet X på serverrackets skenor.

1. Fäst monteringsfästena på Comet X med de medföljande skruvarna.

    ![Montering 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install1.png){class="glboxshadow"}

2. Fäst Comet X på rackskenorna med rackskruvar. **Rackskruvar ingår inte**.

    ![Montering 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install2.png){class="glboxshadow"}

## Lokal styrning {#local-control}

Styr enheten direkt via fysiska kablar – inget nätverk, ingen IP-adress och inget domännamn krävs.

Comet X har en HDMI OUT-port och två extra USB-portar, vilket är idealiskt för lokal felsökning, konfiguration och OS-installation. Anslut bara skärm, mus och tangentbord för lokal hårdvarustyrning med plug-and-play.

1. Anslut **HDMI OUT**-porten på Comet X:s baksida till en extern skärm för att spegla bilden (videovidarekoppling).

    ![Lokal styrning 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control1.png){class="glboxshadow"}

2. Anslut ett tangentbord och en mus till USB-portarna på Comet X:s frontpanel.

    ![Lokal styrning 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control2.png){class="glboxshadow"}

3. Nu kan du styra de anslutna enheterna med ditt lokala tangentbord och din lokala mus, medan videosignalen vidarekopplas till den lokala skärmen.

## LAN-åtkomst {#lan-access}

Det finns två sätt att komma åt Comet X i det lokala nätverket: via domännamn eller IP-adress.

Kontrollera före åtkomsten att den styrande enheten finns i samma LAN som Comet X.

### Domän {#domain}

1. Starta en webbläsare på den styrande enheten. Chrome eller Edge rekommenderas för bättre kompatibilitet.

2. Ange `glkvm.local` i adressfältet. Du kommer till inloggningssidan för GLKVM. Ange administratörslösenordet.

    ![Lokal åtkomst via domän](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain1.png){class="glboxshadow"}

    ***Obs!** Du behöver ange ett administratörslösenord första gången du loggar in.*

3. Du kan sedan komma åt Comet X:s konsol lokalt och få åtkomst till den styrda enheten.

    ![Lokal åtkomst via domän](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain2.png){class="glboxshadow"}

### IP-adress {#ip-address}

1. Ta reda på Comet X:s IP-adress på pekskärmen. I det här exemplet är Comet X:s IP-adress `192.168.8.197`.

2. Starta en webbläsare och ange den här IP-adressen i adressfältet. Du kommer till inloggningssidan för GLKVM. Ange administratörslösenordet.

    ![Lokal åtkomst via IP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip1.png){class="glboxshadow"}

    ***Obs!** Du behöver ange ett administratörslösenord första gången du loggar in.*

3. Du kan sedan komma åt Comet X:s konsol lokalt och få åtkomst till den styrda enheten.

    ![Lokal åtkomst via IP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip2.png){class="glboxshadow"}

## Fjärråtkomst {#remote-access}

Det finns flera sätt att komma åt Comet X på distans: via molntjänsten, GLKVM-appen, Tailscale och ZeroTier.

### Molntjänst {#cloud-service}

1. Koppla din enhet till KVM Cloud. Detta måste göras i det lokala nätverket.

    Det finns två sätt att koppla din KVM till molnet: vanlig koppling eller koppling med dynamisk kod. Här används vanlig koppling som exempel. Om du föredrar koppling med dynamisk kod kan du klicka [här](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} för mer information.

    Öppna först Comet X lokalt och gå till **Cloud Service** i det övre högra hörnet. Klicka på **Bind To KVMCloud**.

    ![Koppla till molnet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_to_cloud.png){class="glboxshadow"}

    Du omdirigeras till en inloggningssida. Logga in med ditt GL.iNet-molnkonto.

    ![Koppla enheten i molnet 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind1.png){class="glboxshadow"}

    Bekräfta sedan enhetsinformationen och klicka på **Bind**.

    ![Koppla enheten i molnet 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind2.png){class="glboxshadow"}

    Vänta ett ögonblick så kopplas din Comet X till ditt konto. Klicka på **Done**.

    ![Enheten har kopplats i molnet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind_success.png){class="glboxshadow"}

2. Fjärråtkomst via molntjänsten.

    När du har klickat på **Done** omdirigeras du till en webbplats med domänen `glkvm.com`, där du kan se din enhet.

    ![Enhetslista i molnet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_devices.png){class="glboxshadow"}

    ***Tips!** Om du inte omdirigeras anger du `glkvm.com` manuellt i adressfältet och loggar in på ditt GL.iNet-konto. När du har loggat in visas enheten som är kopplad till ditt konto.*

    Klicka på den enhet som du vill komma åt på distans.

    ![Molnåtkomst](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access.png){class="glboxshadow"}

    En ny webbsida öppnas. Ange administratörslösenordet för att logga in.

    ![Molnåtkomst 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access1.png){class="glboxshadow"}

    Du kan sedan komma åt din Comet X och den styrda enheten på distans via molnet.

    ![Molnåtkomst 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access2.png){class="glboxshadow"}

### GLKVM-appen {#glkvm-app}

1. Installera [GLKVM-appen](https://www.gl-inet.com/app-rm/){target="_blank"} på den styrande enheten.

2. Logga in med ditt GL.iNet-konto.

    ![Logga in](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_login.jpg){class="glboxshadow"}

    Om du inte har något konto registrerar du dig först och loggar sedan in.

    ![Registrera dig](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_signup.png){class="glboxshadow"}

3. Koppla din enhet.

    När du har loggat in visas sidan nedan. Klicka på **Add Device**.

    ![Lägg till enhet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_add_device.png){class="glboxshadow"}

    Du kan koppla enheten på tre sätt: Auto Discover, S/N Code och Dynamic Binding Code.

    ??? "Auto Discover"

        Detta måste göras i det lokala nätverket. Kontrollera att den styrande enheten finns i samma LAN som Comet X och ha KVM-enhetens enhets-ID till hands.

        Klicka på **Auto Discover**. Sökningen startar.

        ![Automatisk identifiering 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover1.png){class="glboxshadow"}

        Leta upp din KVM och ange dess **Device ID** för att koppla den till ditt konto.

        ![Automatisk identifiering 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover2.png){class="glboxshadow"}

        ![Automatisk identifiering 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover3.png){class="glboxshadow"}

    ??? "S/N Code"

        Detta gäller om din KVM inte hittas eller inte finns i samma LAN, men du har dess serienummer (S/N).

        Klicka på **S/N Code**. I popup-fönstret anger du ett enhetsnamn och serienumret, som finns tryckt på undersidan av KVM-enheten.

        ![Serienummer](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/add_sncode.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Detta måste göras i det lokala nätverket. Kontrollera att den styrande enheten finns i samma LAN som Comet X.

        1. Logga in på din KVM lokalt via domännamn eller IP-adress. Klicka [här](#lan-access) för mer information.

        2. Gå till **Cloud Service** i det övre högra hörnet och klicka på **Bind With Code**.

            ![Koppla med kod 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code1.png){class="glboxshadow"}

        3. En slumpmässig, åttasiffrig dynamisk kod för koppling av enheten genereras. Den är giltig i 60 sekunder. Klicka på koden för att kopiera den.

            ![Koppla med kod 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code2.png){class="glboxshadow"}

        4. Gå tillbaka till GLKVM-appen, ange den dynamiska kopplingskoden och klicka på **Bind**.

            ![Dynamisk kod](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code3.png){class="glboxshadow"}

4. Fjärråtkomst via GLKVM-appen.

    När KVM-enheten har kopplats till ditt konto visas den som "Online" i appen.

    ![Enheten är online i appen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_devices.png){class="glboxshadow"}

    Klicka på din KVM-enhet. Ett nytt fönster öppnas och anslutningen startar.

    ![Appen ansluter](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_connecting.png){class="glboxshadow"}

    När anslutningen är upprättad anger du administratörslösenordet för att logga in på enheten.

    ![Åtkomst via appen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access1.png){class="glboxshadow"}

    Du kommer sedan åt KVM-enheten och via den den styrda enheten.

    ![Åtkomst via appen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access2.png){class="glboxshadow"}

### Tailscale {#tailscale}

Comet X är integrerad med Tailscale, så att du kan komma åt den på distans via det virtuella Tailscale-nätverket.

Gå till **Apps Center** -> **Tailscale** i konsolen, aktivera funktionen och koppla din Comet X till ditt Tailscale-konto.

Koppla sedan den styrande enheten till samma konto. Därefter kan du komma åt din Comet X på distans genom att ange dess **Tailscale virtual IP** i en webbläsare på den styrande enheten, utan att installera GLKVM-appen.

Mer information finns [här](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier {#zerotier}

Comet X är integrerad med ZeroTier, så att du kan komma åt den på distans via det virtuella ZeroTier-nätverket.

Gå till **Apps Center** -> **ZeroTier** i konsolen och aktivera funktionen.

Anslut sedan både Comet X och den styrande enheten till samma ZeroTier-nätverk (med ett alfanumeriskt nätverks-ID på 16 tecken). Därefter kan du komma åt din Comet X på distans genom att ange dess **ZeroTier IP** i en webbläsare på den styrande enheten, utan att installera GLKVM-appen.

Mer information finns [här](../../faq/remote_access_via_zerotier.md){target="_blank"}.
