# Konsolguide för Comet (GL-RM1) V1/V2 {#comet-gl-rm1-v1v2-console-guide}

## Session {#session}

Gå till **Session** i konsolen. Inställningssidan består av fyra avsnitt:

- [Video](#video)
- [Ljud](#audio)
- [Tangentbord](#keyboard)
- [Mus](#mouse)

### Video {#video}

Under Session kan du anpassa videoinställningar som visningsläge, videokvalitet, videoöverföring, skärmorientering och EDID.

![Videoinställningar](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/session-video.png){class="glboxshadow"}

- **Transfer**: växla metod för videoöverföring mellan WebRTC, WebRTC (FEC), WebRTC (Native) och Direct. Observera att överföring med Direct saknar ljud.

    !!! note "Vad är skillnaden mellan WebRTC, WebRTC (FEC), WebRTC (Native) och Direct?"

        - **WebRTC**: balanserar smidig video och stabilt ljud för fjärrstyrning i realtid.

        - **WebRTC (FEC)**: lägger till framåtriktad felkorrigering för att förbättra anslutningens stabilitet vid dåliga eller instabila nätverksförhållanden. När alternativet är valt reparerar det automatiskt förlorade datapaket genom att skicka en liten mängd redundanta data, vilket minskar skärmflimmer och fördröjning.

        - **WebRTC (Native)**: drivs av Google WebRTC-biblioteket och ger bättre strömningsprestanda och en smidigare fjärrstyrning i realtid. Detta överföringsläge introducerades i firmware v1.10.0.

        - **Direct**: ger lägst latens och förlustfri videokvalitet, men stöder inte ljudöverföring.

- **Mode**: växla mellan läget Smart och Normal efter behov. Smart-läget hjälper till att minska bandbreddsförbrukningen, särskilt i svaga nätverk.

- **Latency Mode**: du kan välja mellan Lowest Latency och Smooth Display för enheten. Funktionen introducerades i firmware v1.9.0.

    !!! note "Vad är skillnaden mellan Lowest Latency och Smooth Display?"

        - **Lowest Latency**: minimerar inmatningslatensen för snabbare respons från tangentbord och mus.

        - **Smooth Display**: optimerar bildprestandan för att eliminera hack och tappade bildrutor, vilket ger jämn uppspelning.

- **Quality**: justera videokvaliteten till Auto/Low/Medium/High/Ultra-high/Lossless beroende på din nätverksmiljö och dina krav på upplösning.

- **FEC Packets**: när nätverket är instabilt reparerar funktionen automatiskt förlorade datapaket genom att skicka en liten mängd redundanta data, vilket minskar skärmflimmer och fördröjning. Du kan ställa in FEC-andelen till 5 %/10 %/15 %/20 %.

- **Orientation**: justera konsolens rotationsvinkel till 0°/90°/180°/270°.

- **EDID**: förkortning för Extended Display Identification Data. Den matchar automatiskt de optimala visningsparametrarna.

    Standardinställningen passar de flesta scenarier och behöver i regel inte ändras. Mer information finns [här](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. Om skärmen inte uppdateras efter att du har justerat EDID startar du om den styrda enheten.

- **View**: inställningen avgör hur bilden skalas när du ändrar storlek på webbläsarfönstret. Tillgängliga alternativ: Adaptive, Best Picture Quality, Original Pixel. Funktionen introducerades i firmware v1.8.0.

### Ljud {#audio}
Du kan justera inställningarna för ljud och kamera för den styrda enheten.

![Ljud](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/session-audio.png){class="glboxshadow"}

- **Speaker**: styr ljudutgången från den styrda enheten (t.ex. systemljud, ljud från video).

- **Microphone**: överför lokalt ljud (t.ex. din röst) från den styrande enheten till fjärrsidan. Den har stöd för avstängning av ljudet med ett klick och ett kortkommando som aktiverar mikrofonen medan det hålls intryckt (dvs. Press To Speak).

    **Obs!** Kortkommandot måste konfigureras manuellt under [Inställningar](#usb-devices) innan det kan användas.

### Tangentbord {#keyboard}

Under Keyboard kan du konfigurera inställningarna för tangentbordsanvändning på den styrda enheten.

![Tangentbord](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/session-keyboard.png){class="glboxshadow"}

- **Bad Link Mode**: det vill säga att tangenterna släpps omedelbart. Varje tangenttryckning skickas som ett enda snabbt tryck och släpp, vilket förhindrar fastnade tangenter eller oavsiktlig upprepad inmatning vid fjärrstyrning.

- **Show Virtual Keyboard**: visa och använd det virtuella tangentbordet i konsolen.

    ![Visa virtuellt tangentbord](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/session_show_virtual_keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: funktionen byter plats på Cmd- och Ctrl-tangenterna för att säkerställa tangentbordskompatibilitet mellan olika operativsystem.

### Mus {#mouse}

Du kan justera musinställningarna för en bättre upplevelse på den styrda enheten.

![Mus](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/session_mouse.png){class="glboxshadow"}

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

- **Primary Button**: välj vänster eller höger knapp som primär klickknapp. Funktionen introducerades i firmware v1.9.0.

## Verktygslåda {#toolbox}

Gå till **Toolbox** i konsolen. Sidan Toolbox består av fem avsnitt:

- [Urklipp](#clipboard)
- [OCR](#ocr)
- [Kortkommandon](#shortcut)
- [Wake on LAN](#wake-on-lan)
- [Terminal](#terminal)

### Urklipp {#clipboard}

Med urklippet kan du enkelt klistra in text från den styrande enheten till den styrda enheten, utan att behöva överföra filer.

![Urklipp i verktygslådan](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-clipboard.png){class="glboxshadow"}

### OCR {#ocr}

OCR är en funktion för textigenkänning som låter dig markera ett område på fjärrskärmen och enkelt extrahera text från det. Funktionen introducerades i firmware v1.9.0.

Klicka på nedåtpilen för att välja önskat igenkänningsspråk, till exempel kinesiska, engelska eller tvåspråkigt (Zh/En).

![Igenkänningsspråk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox_ocr.png){class="glboxshadow"}

Klicka sedan på **Capture**, så tonas fjärrskärmen ned. Rita en ruta runt texten som du vill extrahera, så identifierar systemet den automatiskt. Därefter kan du kopiera den igenkända texten efter behov.

![Kopiera text](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/ocr_copy_text.png){class="glboxshadow"}

Med den här funktionen kan du enkelt fånga text från fjärrskärmen (dvs. den styrda enheten) och kopiera den till den lokala styrande enheten.

### Kortkommandon {#shortcut}

Med kortkommandon kan du utföra åtgärder snabbare utan att använda det virtuella tangentbordet, så att du arbetar effektivare och sparar tid i det dagliga arbetet. Här finns några vanliga kortkommandon.

![Kortkommandon i verktygslådan 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-shortcut.png){class="glboxshadow"}

Klicka på **Modify** för att ändra kortkommandona efter behov.

![Kortkommandon i verktygslådan 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox_shorcut_modify.png){class="glboxshadow"}

### Wake-on-LAN {#wake-on-lan}

Wake-on-LAN (WOL) är en teknik som gör det möjligt att starta den styrda enheten på distans eller väcka den från ett energisparläge.

Klicka på **Add Device** och välj en enhet i samma LAN.

![Wake-on-LAN i verktygslådan](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox_wake_on_lan.png){class="glboxshadow"}

![Lägg till enhet för WOL](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/wol-add-device.png){class="glboxshadow" width=400}

Om enheten som du vill lägga till inte finns i listan klickar du på **Add Manually** och anger enhetens namn och MAC-adress.

![Lägg till WOL-enhet manuellt](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/wol-add-manually.png){class="glboxshadow" width=400}

### Terminal {#terminal}

Du kan öppna Comets terminal för att göra avancerade inställningar. Klicka på **Access**.

![Terminal i verktygslådan 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox_terminal.png){class="glboxshadow"}

Du omdirigeras till GLKVM-terminalen.

![Terminal i verktygslådan 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-terminal-2.png){class="glboxshadow"}

## Tillbehör {#accessories}

GL.iNet erbjuder valfria KVM-tillbehör för att fjärrstyra start och avstängning av enheten.

Läs först respektive användarhandbok för att ansluta tillbehöret till den styrda enheten.

- [Användarhandbok för Fingerbot (FGB-01)](../gl-fgb-01/index.md){target="_blank"}

- [Användarhandbok för ATX-kort (GL-ATXPC)](../gl-atx-board/index.md){target="_blank"}

Logga sedan in på KVM-konsolen och gå till **Accessories**. Tillbehörsinställningarna är bara tillgängliga när tillbehöret har installerats.

### Fingerbot {#fingerbot}

Fingerbot fästs på den styrda enhetens fysiska strömknapp för att möjliggöra fjärrstyrning av strömförsörjningen till den styrda enheten.

Den fungerar enligt inställningarna i konsolen.

![Fingerbot under Accessories](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/accessories-fgb.png){class="glboxshadow"}

- **Time**: hur länge Fingerbot trycker. Du kan ställa in 0,5 s/3 s/8 s.

- **Strength**: det finns två nivåer av tryckstyrka: Lightly Press och Firmly Press.

    - **Lightly Press**: perfekt för korta eller lättryckta knappar.

    - **Firmly Press**: idealiskt för djupa eller tröga knappar.

    ![Tryckläge](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### ATX-ström {#atx-power}

ATX-kortet monteras i datorchassit för att fjärrstyra start, avstängning och omstart av enheten.

Det fungerar enligt inställningarna i konsolen.

![ATX-ström under Accessories](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/accessories-atx.png){class="glboxshadow"}

- **Power (Short Press)**: används för normal start eller för att väcka systemet.

- **Power (Long Press)**: utför en tvingad avstängning.

- **Restart**: startar om enheten.

## Virtuella medier {#virtual-media}

Gå till **Virtual Media** i konsolen. Här kan du utföra följande åtgärder:

- [Dela filer](#file-sharing)
- [Montera avbildningar](#image-mounting)
- [Byta lagringsenhet](#replace-storage-drive)
- [Formatera disken](#format-disk)

![Virtuella medier](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/virtual-media.png){class="glboxshadow"}

### Fildelning {#file-sharing}

Comet kan emulera en USB-enhet med läs- och skrivåtkomst, så att du kan dela och hantera filer mellan den styrande och den styrda enheten.

**Följ stegen nedan för att dela filer från den styrande enheten till den styrda enheten.**

1. Dra filer till rutan eller klicka på den för att ladda upp filer från den styrande enheten, eller ladda upp från en URL.

    När filerna har laddats upp visas de enligt nedan.

    ![Ladda upp filer](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing1.png){class="glboxshadow"}

2. Klicka på **Mount To Remote** -> **File Sharing**.

    ![Fildelning](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing2.png){class="glboxshadow"}

3. Ett fönster med stegen för fildelning visas i konsolen, enligt bilden nedan.

    ![Tips om fildelning](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing3.png){class="glboxshadow"}

4. Vänta ett ögonblick, så visas en enhet med namnet **"GLKVM"** automatiskt på skärmen. Du ser då att filerna som du tidigare laddade upp från den styrande enheten till Comet har delats med den styrda enheten. Nu kan du visa, flytta eller ta bort filerna på den här enheten från den styrda enheten.

    ![GLKVM-disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing4.png){class="glboxshadow"}

    **Tips!** Om enheten inte visas automatiskt öppnar du **This PC** på den styrda enheten.

    ![Den här datorn](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/thispc.png){class="glboxshadow"}

    Leta sedan upp enheten med namnet **GLKVM**. Nu kan du visa, flytta eller ta bort filerna på den här enheten.

5. Om du vill sluta dela klickar du på **Virtual Media** i verktygsfältet och klickar på **Stop Sharing**.

    ![Sluta dela 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/stop-sharing1.png){class="glboxshadow"}

**Följ stegen nedan för att dela filer från den styrda enheten till den styrande enheten.**

1. Flytta eller kopiera filerna som du vill dela till enheten **GLKVM** på den styrda enheten.

    I det här exemplet har en PDF-fil med namnet "slate7pro_datasheet" kopierats från den styrda enhetens skrivbord till disken **GLKVM**.

    ![Flytta filen till disken](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing5.png){class="glboxshadow"}

2. Gå till Comets konsol, klicka på **Virtual Media** i verktygsfältet och klicka på **Stop Sharing**.

    ![Sluta dela 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/stop-sharing2.png){class="glboxshadow"}

3. Filen visas sedan under **Virtual Media**, enligt bilden nedan. Nu kan du ladda ned filen från Comet till den styrande enheten.

    ![Filen har delats](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing6.png){class="glboxshadow"}

### Montering av avbildningar {#image-mounting}

Comet kan simulera en skrivskyddad virtuell cd/dvd- eller diskenhet på den styrda enheten. Du kan komma åt enheten under start av BIOS eller UEFI.

Funktionen hjälper dig att installera om operativsystemet, montera en ISO-fil för att installera program på den styrda enheten eller utföra andra uppgifter.

1. Dra filer till rutan eller klicka på den för att ladda upp filer. **Kontrollera att filen kan monteras i ISO-format**.

    När filerna har laddats upp visas de enligt nedan.

    ![Montering av avbildning 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting1.png){class="glboxshadow"}

2. Klicka på **Mount To Remote** -> **Image Mounting**.

    ![Montering av avbildning 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting2.png){class="glboxshadow"}

3. Välj filen i popup-fönstret och klicka på **Mount Image**.

    ![Montering av avbildning 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting3.png){class="glboxshadow"}

4. Ett fönster med stegen för monteringen visas i konsolen, enligt bilden nedan.

    ![Montering av avbildning 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting4.png){class="glboxshadow"}

5. Nu kan du använda filen från cd-enheten på den styrda enheten.

    ![Montering av avbildning 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting5.png){class="glboxshadow"}

### Byta lagringsenhet {#replace-storage-drive}

Du kan ansluta en USB-lagringsenhet till KVM-enhetens USB-port för att ersätta den interna lagringen.

![Byt lagringsenhet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/replace-storage.png){class="glboxshadow"}

### Formatera disken {#format-disk}

Du kan formatera disken eller inaktivera de virtuella medierna med ett klick.

![Formatera disken](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/format-disable.png){class="glboxshadow"}

- **Format**: raderar alla data på disken och initierar om dess filsystemstruktur.

- **Disable**: om du inaktiverar de virtuella medierna startas KVM-enheten om omedelbart.

## Appcenter {#apps-center}

Gå till **Apps Center** i konsolen. Här finns de integrerade programmen.

![Appcenter](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/app_center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} är en WireGuard-baserad mesh-VPN-tjänst som bygger krypterade privata peer-to-peer-nätverk mellan enheter utan portvidarebefordran eller komplicerad brandväggskonfiguration.

Comet är integrerad med Tailscale, så att du kan komma åt den på distans via det virtuella Tailscale-nätverket.

Koppla bara Comet och den styrande enheten till samma Tailscale-konto. Därefter kan du komma åt din Comet på distans genom att ange dess **Tailscale virtual IP** i en webbläsare på den styrande enheten, utan att installera GLKVM-appen. Mer information finns [här](../../faq/remote_access_via_tailscale.md){target="_blank"}.

Efter kopplingen visar konsolen det länkade Tailscale-kontot och låser upp avancerade funktioner som Exit Node och Subnet Routes.

![Tailscale aktiverat](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} skapar krypterade virtuella overlay-nätverk som förbinder utspridda enheter över hela världen som om de fanns i samma lokala nätverk.

Comet är integrerad med ZeroTier, så att du kan komma åt den på distans via det virtuella ZeroTier-nätverket.

Anslut bara Comet och den styrande enheten till samma ZeroTier-nätverk. Därefter kan du komma åt din Comet på distans genom att ange dess **ZeroTier IP** i en webbläsare på den styrande enheten, utan att installera GLKVM-appen. Mer information finns [här](../../faq/remote_access_via_zerotier.md){target="_blank"}.

Efter anslutningen visar konsolen ZeroTier-nätverkets ID och den virtuella IP-adressen.

![ZeroTier aktiverat](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/apps-zerotier-enabled.png){class="glboxshadow"}

### NetBird {#netbird}

[NetBird](https://netbird.io/){target="_blank"} är en nätverksplattform med öppen källkod baserad på nolltillit (zero trust) som låter dig bygga säkra privata nätverk för hem- och företagsbruk. Som ett WireGuard®-baserat overlay-nätverk ger NetBird säker åtkomst till dina enheter när som helst och var som helst.

Comet är integrerad med NetBird, så att du kan komma åt den på distans via det virtuella NetBird-nätverket. Mer information finns [här](../../faq/remote_access_via_netbird.md){target="_blank"}.

Efter kopplingen visar konsolen den virtuella NetBird-IP-adressen.

![NetBird aktiverat](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/apps-netbird-enabled.png){class="glboxshadow"}

## Hjälp {#help}

Gå till **Help** i konsolen. Här hittar du mer information om GL.iNet KVM och hjälpdokumentation, och du kan exportera loggar för felsökning.

![Hjälp](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/help.png){class="glboxshadow"}

## Verktygsfält {#toolbar}

I konsolens övre högra hörn finns följande verktyg:

- [Dölj verktygsfältet](#collapse)
- [Helskärm](#fullscreen)
- [Uppgradering](#upgrade)
- [Anslutningsstatistik](#connection-stats)
- [Molntjänst](#cloud-service)
- [Logga ut](#logout)

### Dölj {#collapse}

Klicka på uppåtpilen i det övre högra hörnet för att dölja verktygsfältet.

![Dölj 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/collapse_1.png){class="glboxshadow"}

När verktygsfältet är dolt klickar du på nedåtpilen högst upp för att visa det igen.

![Dölj 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/collapse_2.png){class="glboxshadow"}

### Helskärm {#fullscreen}

Klicka på helskärmsikonen (fyrkantig) i det övre högra hörnet för att växla till helskärmsläge.

![Helskärm 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/fullscreen_1.png){class="glboxshadow"}

Lämna helskärmsläget genom att hålla ned **Esc**-tangenten eller klicka på ikonen för att avsluta helskärm (rutnätsformad) i det övre högra hörnet.

![Helskärm 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/fullscreen_2.png){class="glboxshadow"}

### Uppgradering {#upgrade}

Klicka på firmwareversionen i det övre högra hörnet för att söka efter uppdateringar.

![Firmwareuppgradering 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/upgrade_1.png){class="glboxshadow"}

I popup-fönstret kan du klicka på **Local Upgrade** för att ladda upp en firmwarefil.

![Firmwareuppgradering 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/upgrade_2.png){class="glboxshadow"}

![Firmwareuppgradering 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/upgrade_3.png){class="glboxshadow" width=350}

Ladda ned den senaste firmwaren från [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} innan du gör en lokal uppgradering.

### Anslutningsstatistik {#connection-stats}

Connection Stats innehåller en datapanel som övervakar latens, jitter och andra mätvärden i realtid.

Klicka på listikonen för att visa enhetens status och realtidsdata.

![Datapanel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/connection_stats_1.png){class="glboxshadow"}

Klicka på diagramikonen för att visa statistik, bland annat nätverkslatens, nätverksjitter, paketförlust, bildfrekvens i realtid och uppspelningsfördröjning.

![Datapanel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/connection_stats_2.png){class="glboxshadow"}

### Molntjänst {#cloud-service}

Med GL.iNet KVM Cloud kan du komma åt den styrda enheten på distans. Mer information finns [här](../../faq/remote_access_via_cloud.md){target="_blank"}.

När din Comet har kopplats till molnet visar konsolen molnstatusen enligt nedan.

![Molntjänst](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/cloud.png){class="glboxshadow"}

### Logga ut {#logout}

Klicka på utloggningsikonen för att logga ut.
![Logga ut](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/logout.png){class="glboxshadow"}

## Inställningar {#settings}
Klicka på inställningsikonen i navigeringsfältet i konsolen för att öppna inställningssidan nedan. Funktionen introducerades i firmware v1.10.0.

- [USB-enheter](#usb-devices)
- [Preferenser](#preferences)
- [Nätverk](#network)
- [Säkerhet](#security)
- [Moln](#cloud)
- [System](#system)

![Inställningar](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setting.png){class="glboxshadow"}

### USB-enheter {#usb-devices}

USB Devices ger central hantering av alla emulerade USB-enheter. På den här sidan kan du slå på eller av virtuell kringutrustning för bättre kompatibilitet med den styrda värden.

![Emulerade USB-enheter](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setting_usb_devices.png){class="glboxshadow"}

- **Microphone**

    När mikrofonen är avstängd kan du klicka på Settings för att anpassa kortkommandon efter dina vanor. Håll ned det tilldelade kortkommandot för att börja tala. När du släpper det stängs mikrofonen av igen.

    ![Mikrofoninställningar 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/mic_setting_1.png){class="glboxshadow" width=600}

    ![Mikrofoninställningar 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/mic_setting_2.png){class="glboxshadow" width=434}

  - **Device Identity**

    Anpassa eller ändra den KVM-identitet som den styrda enheten identifierar. Observera att EDID och enhetsidentiteten hålls synkroniserade. Om du ändrar den ena uppdateras den andra automatiskt, så att enheten identifieras korrekt.

    ![Enhetsidentitet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/device_identification.png){class="glboxshadow" width=350}

### Preferenser {#preferences}

Under Preferences hanterar du layoutinställningar, systeminställningar och inställningar för enhetens skärm.

![Preferenser](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setting_preference.png){class="glboxshadow"}

- **Layout Preferences**: du kan välja om verktygsfältet ska visas i helskärmsläge och om statusfältet ska visas i fönsterläge.

- **System Settings**: anpassa systeminställningarna genom att välja flikrubrik i webbläsaren, språk (kinesiska, engelska eller japanska), färgläge (ljust eller mörkt) och tidszon för din region.

### Nätverk {#network}

Du kan kontrollera och ändra Comets nätverksinformation, till exempel värdnamn och IP-adress.

![Nätverk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setting_network.png){class="glboxshadow"}

- **Hostname**: du kan ändra enhetens värdnamn direkt i konsolen. Funktionen introducerades i firmware v1.7.0.

    ![Ändra värdnamn](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setting_network_hostname.png){class="glboxshadow" width=600}

- **Ethernet Settings**: när Comet är ansluten till en överordnad nätverksenhet med en Ethernet-kabel visas Ethernet-informationen här.

    Om protokollet är DHCP visas sidan enligt nedan.

    ![Ethernet med DHCP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setting_network_dhcp.png){class="glboxshadow" width=600}

    Om du vill ange en statisk IP-adress växlar du protokollet till **Static** och anger de nätverksparametrar som krävs (t.ex. IP-adress, nätmask, gateway).

    ![Statisk Ethernet-adress](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setting_network_static.png){class="glboxshadow" width=600}

### Säkerhet {#security}

Under Security kan du ändra administratörslösenordet, aktivera tvåfaktorsautentisering och anpassa TLS-certifikatet.

![Säkerhet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setting_security.png){class="glboxshadow"}

- Ändra administratörslösenordet

    ![Ändra administratörslösenordet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/change-password.png){class="glboxshadow" width="434"}

- 2FA: aktivera tvåfaktorsautentisering för att skydda ditt konto.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/2fa.png){class="glboxshadow"}

- TLS-certifikat

    Systemet använder det förinstallerade standardcertifikatet för åtkomst via webbläsare. Om du vill använda ett eget TLS-certifikat för webbläsaråtkomst klickar du på **Custom** under TLS Certificate och laddar sedan upp din **certifikatfil och privata nyckelfil**.

    ![Anpassat TLS-certifikat](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setting_security_custom.png){class="glboxshadow"}

### Moln {#cloud}

Under Cloud kan du komma åt och hantera enheten på distans via molntjänster.

Du kan koppla enheten till molnet via en URL. Under **More Settings** finns andra alternativ som Bind With Code och App Download. Du kan även välja Disable vid behov.

![Moln 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setting_cloud_1.png){class="glboxshadow"}

När kopplingen är klar kan du se informationen om det kopplade molnkontot. Klicka på **Access Cloud** för att hantera enheter eller på **More Settings** för att inaktivera eller koppla från vid behov.

![Moln 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setting_cloud_2.png){class="glboxshadow"}

Du kan också utföra ovanstående hanteringsåtgärder via Cloud Service i det övre verktygsfältet.

### System {#system}

I systeminställningarna kan du konfigurera följande:

![System](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setting_system.png){class="glboxshadow"}

- **System**: klicka på **Reboot** för att starta om enheten, eller på **Reset** för att rensa enhetens aktuella konfiguration och konfigurera enheten på nytt.

- **Upgrade**: du kan aktivera Beta Center för att få betaversioner av firmware, eller använda Local Upgrade för att installera manuellt från en lokal fil.

    ![Lokal uppgradering](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/setthing_system_local_update.png){class="glboxshadow" width=400}

- **Help & Support**: Export Log Files låter dig spara enhetens körloggar för felsökning och eftermarknadssupport. Help Document ger åtkomst till användarhandböcker, vanliga frågor och felsökningsdokumentation.
