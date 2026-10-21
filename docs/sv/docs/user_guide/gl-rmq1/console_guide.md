# Konsolguide för Comet Q (GL-RMQ1) {#comet-q-gl-rmq1-console-guide}

## Inställningar {#settings}

Gå till **Settings** i konsolen. Inställningssidan består av fyra avsnitt:

- [Video](#video)
- [Ljud, tangentbord och mus](#audiokeyboardmouse)
- [System](#system)
- [Nätverk](#network)

### Snabbsökning {#quick-search}

Du kan snabbt hitta de inställningar du söker genom att ange nyckelord högst upp på inställningssidan.

![Snabbsökning](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/quick-search.png){class="glboxshadow"}

### Video {#video}

Du kan anpassa videoinställningar i konsolen, till exempel EDID, videokvalitet, videoöverföring och skärmorientering.

![Videoinställningar](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-video.png){class="glboxshadow"}

- **Type**: välj typ av styrd enhet.

    Systemet tillämpar automatiskt rekommenderat musläge och rekommenderade EDID-inställningar för att ge bästa bildförhållande och styrprecision. Ändra det här alternativet om enheten inte identifieras korrekt eller om du behöver använda en anpassad typ.

- **EDID**: förkortning för Extended Display Identification Data. Den matchar automatiskt de optimala visningsparametrarna.

    Standardinställningen passar de flesta scenarier och behöver i regel inte ändras. Mer information finns [här](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. Om skärmen inte uppdateras efter att du har justerat EDID startar du om den styrda enheten.

- **Mode**: växla mellan läget Smart och Normal efter behov. Smart-läget hjälper till att minska bandbreddsförbrukningen, särskilt i svaga nätverk.

- **Quality**: justera videokvaliteten till Low/Medium/High/Ultra-high/Lossless beroende på din nätverksmiljö och dina krav på upplösning.

- **Transfer**: växla metod för videoöverföring mellan WebRTC, WebRTC (FEC) och Direct. Observera att överföring med Direct saknar ljud.

    !!! note "Vad är skillnaden mellan WebRTC, WebRTC (FEC) och Direct?"

        - **WebRTC**: balanserar smidig video och stabilt ljud för fjärrstyrning i realtid.

        - **WebRTC (FEC)**: lägger till framåtriktad felkorrigering för att förbättra anslutningens stabilitet vid dåliga eller instabila nätverksförhållanden. När alternativet är valt reparerar det automatiskt förlorade datapaket genom att skicka en liten mängd redundanta data, vilket minskar skärmflimmer och fördröjning.

        - **Direct**: ger lägst latens och förlustfri videokvalitet, men stöder inte ljudöverföring.

- **Orientation**: justera konsolens rotationsvinkel till 0°/90°/180°/270°.

- **View**: inställningen avgör hur bilden skalas när du ändrar storlek på webbläsarfönstret. Tillgängliga alternativ: Adaptive, Best Picture Quality, Original Pixel.

### Ljud, tangentbord och mus {#audiokeyboardmouse}

Du kan justera inställningarna för ljud, tangentbord och mus.

![Ljud, tangentbord och mus](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/audio-keyboard-mouse.png){class="glboxshadow"}

- **Speaker**: styr ljudutgången från den styrda enheten (t.ex. systemljud, ljud från video).

- **Microphone**: överför lokalt ljud (t.ex. din röst) från den styrande enheten till fjärrsidan. Den har stöd för avstängning av ljudet med ett klick och ett kortkommando som aktiverar mikrofonen medan det hålls intryckt (dvs. Press To Speak).

    ![Mikrofoninställningar](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/mic-settings.png){class="glboxshadow"}

    ![Press To Speak](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/press-to-speak.png){class="glboxshadow"}

- **Keyboard**: slå på eller av den styrda enhetens tangentbord.

- **Bad Link Mode**: det vill säga att tangenterna släpps omedelbart. Varje tangenttryckning skickas som ett enda snabbt tryck och släpp, vilket förhindrar fastnade tangenter eller oavsiktlig upprepad inmatning vid fjärrstyrning.

- **Show Virtual Keyboard**: visa och använd det virtuella tangentbordet i konsolen.

    ![Visa virtuellt tangentbord](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: funktionen byter plats på Cmd- och Ctrl-tangenterna för att säkerställa tangentbordskompatibilitet mellan olika operativsystem.

- **Mouse**: slå på eller av den styrda enhetens mus.

- **Show Local Cursor**: visa den aktuella enhetens muspekare på skärmen.

- **Mouse Jiggle**: funktionen Mouse Jiggle simulerar små, periodiska musrörelser för att förhindra att den styrda enheten går i viloläge efter långvarig inaktivitet, till exempel under fjärrmöten och serverhantering.

- **Scroll Rate**: hastigheten med vilken mushjulet rullar, eller antalet rader/enheter som rullas per hjulvarv, vilket påverkar hur snabbt innehållet rör sig på fjärrskärmen.

- **Scroll Direction**: avgör om innehållet på fjärrskärmen rör sig i samma riktning (naturlig rullning) eller motsatt riktning (traditionell rullning) när du rullar mushjulet uppåt/nedåt.

    Fyra riktningslägen finns: Standard, Vertical Invert, Horizontal Invert och Both Invert.

- **Mouse Mode**: gör det möjligt att växla mellan absolut läge (Absolute) och relativt läge (Relative) för smidig och exakt markörstyrning i olika fjärrstyrningsscenarier.

    !!! note "Vad är skillnaden mellan absolut och relativt musläge?"

        - **Relative Mode**: muspositionen beräknas utifrån rörelser i stället för fasta skärmkoordinater. Du måste klicka i fjärrfönstret för att styra musen. Markören är låst inom fjärrskärmen och kan inte flyttas ut smidigt. Läget ger bättre kompatibilitet med BIOS, äldre system och inbyggda enheter.

        - **Absolute Mode**: muspositionen motsvarar exakta skärmkoordinater. Fjärrmarkören följer den lokala markören smidigt och exakt, så att du sömlöst kan röra dig mellan din lokala skärm och fjärrskärmen. Läget är idealiskt för daglig skrivbordsstyrning och precisionsarbete, även om en viss fördröjning kan uppstå på grund av nätverksöverföringen.

        Kort sagt: använd absolut läge för smidig daglig styrning och relativt läge för BIOS-åtkomst, vissa äldre enheter som inte stöder absolut positionering eller för att undvika oavsiktliga markörrörelser.

- **Relative Sensitivity**: tillgängligt när Mouse Mode är Relative.

### System {#system}

Du kan anpassa konsolens systemvisningsinställningar eller återställa enheten med ett klick.

![Systeminställningar](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-system.png){class="glboxshadow"}

- **Device Identity**: anpassa eller ändra den KVM-identitet som den styrda enheten identifierar. Observera att EDID och enhetsidentiteten hålls synkroniserade. Om du ändrar den ena uppdateras den andra automatiskt, så att enheten identifieras korrekt.

    ![Enhetsidentitet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/device-identity.png){class="glboxshadow"}

- **Language**: ställ in konsolens språk till kinesiska eller engelska.

- **Color Mode**: välj ljust eller mörkt tema.

- **Time Zone**: anpassa KVM-konsolens tidszon.

- **Reset KVM**: återställ din KVM till fabriksinställningarna med ett enda klick.

### Nätverk {#network}

Du kan kontrollera och ändra Comet Q:s nätverksinformation, till exempel värdnamn och IP-adress.

![Nätverksinställningar](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-network.png){class="glboxshadow"}

- **Hostname**: du kan ändra enhetens värdnamn direkt i konsolen.

    ![Ändra värdnamn](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/hostname.png){class="glboxshadow"}

- **Wi-Fi**: Comet Q:s Wi-Fi-IP-adress visas här när den är ansluten till ett Wi-Fi-nätverk. Klicka på Wi-Fi-nätverkets SSID eller högerpilen för att visa Wi-Fi-information, bland annat SSID, tilldelad IP-adress, gateway och den MAC-adress som din Comet Q använder för anslutningen.

    ![Wi-Fi-konfiguration](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/wifi-config.png){class="glboxshadow"}

    Om du vill ansluta den till ett annat Wi-Fi-nätverk klickar du på **Switch Wi-Fi** och väljer ett Wi-Fi-nätverk i listan över tillgängliga nätverk.

## Verktygslåda {#toolbox}

Gå till **Toolbox** i konsolen. Sidan Toolbox består av tre avsnitt:

- [Urklipp](#clipboard)
- [Kortkommandon](#shortcut)
- [Terminal](#terminal)

### Urklipp {#clipboard}

Med urklippet kan du enkelt klistra in text från den styrande enheten till den styrda enheten, utan att behöva överföra filer.

![Urklipp i verktygslådan](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-clipboard.png){class="glboxshadow"}

### Kortkommandon {#shortcut}

Med kortkommandon kan du utföra åtgärder snabbare utan att använda det virtuella tangentbordet, så att du arbetar effektivare och sparar tid i det dagliga arbetet. Här finns några vanliga kortkommandon.

![Kortkommandon i verktygslådan 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut1.png){class="glboxshadow"}

Klicka på **Modify** för att ändra kortkommandona efter behov.

![Kortkommandon i verktygslådan 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut2.png){class="glboxshadow"}

### Terminal {#terminal}

Du kan öppna Comet Q:s terminal för att göra avancerade inställningar. Klicka på **Access**.

![Terminal i verktygslådan 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal1.png){class="glboxshadow"}

Du omdirigeras till GLKVM-terminalen.

![Terminal i verktygslådan 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal2.png){class="glboxshadow"}

## Virtuella medier {#virtual-media}

Gå till **Virtual Media** i konsolen. Comet Q kan emulera en USB-enhet med läs- och skrivåtkomst, så att du kan dela och hantera filer mellan den styrande och den styrda enheten.

![Virtuella medier](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-media.png){class="glboxshadow"}

### Fildelning {#file-sharing}

**Följ stegen nedan för att dela filer från den styrande enheten till den styrda enheten.**

1. Dra filer till rutan eller klicka på den för att ladda upp filer från den styrande enheten, eller ladda upp från en URL.

    När filerna har laddats upp visas de enligt nedan.

    ![Fildelning 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing1.png){class="glboxshadow"}

2. Klicka på **Mount To Remote** -> **File Sharing**.

    ![Fildelning 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing2.png){class="glboxshadow"}

3. Ett fönster med stegen för fildelning visas i konsolen, enligt bilden nedan.

    ![Fildelning 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing3.png){class="glboxshadow"}

4. Vänta ett ögonblick, så kan en enhet med namnet **"GLKVM"** visas automatiskt på skärmen. Du ser då att filerna som du tidigare laddade upp från den styrande enheten till Comet Q har delats med den styrda enheten. Nu kan du visa, flytta eller ta bort filerna på den här enheten från den styrda enheten.

    ![Fildelning 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing4.png){class="glboxshadow"}

    **Tips!** Om enheten inte visas automatiskt öppnar du **This PC** på den styrda enheten.

    ![Den här datorn](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/thispc.png){class="glboxshadow"}

    Leta sedan upp enheten med namnet **GLKVM**. Nu kan du visa, flytta eller ta bort filerna på den här enheten.

5. Om du vill sluta dela klickar du på **Virtual Media** i verktygsfältet och klickar på **Stop Sharing**.

    ![Sluta dela 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing1.png){class="glboxshadow"}

**Följ stegen nedan för att dela filer från den styrda enheten till den styrande enheten.**

1. Flytta eller kopiera filerna som du vill dela till enheten **GLKVM** på den styrda enheten.

    I det här exemplet har en PDF-fil med namnet "gl-rm10_datasheet" flyttats från den styrda enhetens skrivbord till enheten **GLKVM**.

    ![Fildelning 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing5.png){class="glboxshadow"}

2. Gå till Comet Q:s konsol, klicka på **Virtual Media** i verktygsfältet och klicka på **Stop Sharing**.

    ![Sluta dela 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing2.png){class="glboxshadow"}

3. Filen visas sedan under **Virtual Media**, enligt bilden nedan. Nu kan du ladda ned filen från Comet Q till den styrande enheten.

    ![Fildelning 6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing6.png){class="glboxshadow"}

### Formatera disken {#format-disk}

Du kan formatera disken eller inaktivera de virtuella medierna med ett klick.

![Formatera disken](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/format-disable.png){class="glboxshadow"}

- **Format**: raderar alla data på disken och initierar om dess filsystemstruktur.

- **Disable**: om du inaktiverar de virtuella medierna startas KVM-enheten om omedelbart.

## Appcenter {#apps-center}

Gå till **Apps Center** i konsolen. Här finns de integrerade programmen.

![Appcenter](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} är en WireGuard-baserad mesh-VPN-tjänst som bygger krypterade privata peer-to-peer-nätverk mellan enheter utan portvidarebefordran eller komplicerad brandväggskonfiguration.

Comet Q är integrerad med Tailscale, så att du kan komma åt den på distans via det virtuella Tailscale-nätverket.

Koppla bara Comet Q och den styrande enheten till samma Tailscale-konto. Därefter kan du komma åt din Comet Q på distans genom att ange dess **Tailscale virtual IP** i en webbläsare på den styrande enheten, utan att installera GLKVM-appen. Mer information finns [här](../../faq/remote_access_via_tailscale.md){target="_blank"}.

Efter kopplingen visar konsolen det länkade Tailscale-kontot och låser upp avancerade funktioner som Exit Node och Subnet Routes.

![Tailscale aktiverat](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} skapar krypterade virtuella overlay-nätverk som förbinder utspridda enheter över hela världen som om de fanns i samma lokala nätverk.

Comet Q är integrerad med ZeroTier, så att du kan komma åt den på distans via det virtuella ZeroTier-nätverket.

Anslut bara Comet Q och den styrande enheten till samma ZeroTier-nätverk. Därefter kan du komma åt din Comet Q på distans genom att ange dess **ZeroTier IP** i en webbläsare på den styrande enheten, utan att installera GLKVM-appen. Mer information finns [här](../../faq/remote_access_via_zerotier.md){target="_blank"}.

Efter anslutningen visar konsolen ZeroTier-nätverkets ID och den virtuella IP-adressen.

![ZeroTier aktiverat](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-zerotier-enabled.png){class="glboxshadow"}

## Hjälp {#help}

Gå till **Help** i konsolen. Här hittar du mer information om GL.iNet KVM och hjälpdokumentation, och du kan exportera loggar för felsökning.

![Hjälp](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/help.png){class="glboxshadow"}

## Verktygsfält {#toolbar}

I konsolens övre högra hörn finns följande verktyg:

- [Dölj verktygsfältet](#collapse)
- [Helskärm](#fullscreen)
- [Uppgradering](#upgrade)
- [Molntjänst](#cloud-service)
- [Säkerhet](#security)
- Omstart
- Logga ut

### Dölj {#collapse}

Klicka på uppåtpilen i det övre högra hörnet för att dölja verktygsfältet.

![Dölj 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse1.png){class="glboxshadow"}

När verktygsfältet är dolt klickar du på nedåtpilen högst upp för att visa det igen.

![Dölj 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse2.png){class="glboxshadow"}

### Helskärm {#fullscreen}

Klicka på helskärmsikonen (fyrkantig) i det övre högra hörnet för att växla till helskärmsläge.

![Helskärm 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen1.png){class="glboxshadow"}

Lämna helskärmsläget genom att hålla ned **Esc**-tangenten eller klicka på ikonen för att avsluta helskärm (rutnätsformad) i det övre högra hörnet.

![Helskärm 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen2.png){class="glboxshadow"}

### Uppgradering {#upgrade}

Klicka på firmwareversionen i det övre högra hörnet för att söka efter uppdateringar.

![Firmwareuppgradering 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade1.png){class="glboxshadow"}

I popup-fönstret kan du göra en onlineuppgradering om det finns nyare firmware. Du kan också ladda ned den senaste firmwaren från [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} och göra en lokal uppgradering vid behov.

![Firmwareuppgradering 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade2.png){class="glboxshadow"}

### Molntjänst {#cloud-service}

Med GL.iNet KVM Cloud kan du komma åt den styrda enheten på distans. Mer information finns [här](../../faq/remote_access_via_cloud.md){target="_blank"}.

När din Comet Q har kopplats till molnet visar konsolen molnstatusen enligt nedan.

![Molntjänst](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/cloud.png){class="glboxshadow"}

### Säkerhet {#security}

Under Security kan du ändra administratörslösenordet, aktivera tvåfaktorsautentisering och anpassa TLS-certifikatet.

![Säkerhet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/security.png){class="glboxshadow"}

- Ändra administratörslösenordet

    ![Ändra administratörslösenordet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/admin-password.png){class="glboxshadow" width="434"}

- 2FA: aktivera tvåfaktorsautentisering för att skydda ditt konto.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/2fa.png){class="glboxshadow"}

- TLS-certifikat

    Systemet använder det förinstallerade standardcertifikatet för åtkomst via webbläsare. Om du vill använda ett eget TLS-certifikat för webbläsaråtkomst klickar du på **TLS Certificate** i konsolens övre högra hörn, väljer **Custom Certificate** och laddar sedan upp din **certifikatfil och privata nyckelfil**.

    ![Anpassat TLS-certifikat](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/tls-certificate.png){class="glboxshadow"}
