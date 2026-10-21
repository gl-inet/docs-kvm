# Comet 5G (GL-RM10RC) – consolehandleiding {#comet-5g-gl-rm10rc-console-guide}

## Sessie {#session}

Ga in de console naar **Session**. De instellingenpagina bestaat uit vier onderdelen:

- [Video](#video)
- [Audio en camera](#audio-camera)
- [Toetsenbord](#keyboard)
- [Muis](#mouse)

### Video {#video}

In Session kunt u de video-instellingen aanpassen, zoals de weergavemodus, de videokwaliteit, de videoverzending, de schermstand en EDID.

![Video-instellingen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session-video.png){class="glboxshadow"}

- **Transfer**: hiermee kiest u de methode voor videoverzending: WebRTC, WebRTC (FEC), WebRTC (Native) of Direct. Let op: bij Direct wordt geen geluid verzonden.

    !!! note "Wat is het verschil tussen WebRTC, WebRTC (FEC), WebRTC (Native) en Direct?"

        - **WebRTC**: zorgt voor een balans tussen vloeiend beeld en stabiel geluid bij realtime bediening op afstand.
        
        - **WebRTC (FEC)**: voegt voorwaartse foutcorrectie toe om de verbinding stabieler te maken bij een slecht of onstabiel netwerk. Als deze optie is geselecteerd, worden verloren datapakketten automatisch hersteld door een kleine hoeveelheid redundante gegevens mee te sturen. Dit vermindert flikkeren en haperingen van het beeld.
  
        - **WebRTC (Native)**: gebaseerd op de Google WebRTC Library voor betere streamingprestaties en een soepelere realtime bediening op afstand. Deze verzendmodus is geïntroduceerd in firmware v1.10.0.
        
        - **Direct**: biedt de laagste latentie en verliesvrije beeldkwaliteit, maar ondersteunt geen audioverzending.

- **Mode**: schakel naar behoefte tussen de modus Smart en Normal. De modus Smart helpt het bandbreedtegebruik te verminderen, vooral bij zwakke netwerken.

- **Latency Mode**: u kunt voor het apparaat kiezen tussen Lowest Latency en Smooth Display. Deze functie is geïntroduceerd in firmware v1.9.0.

    !!! note "Wat is het verschil tussen Lowest Latency en Smooth Display?"

        - **Lowest Latency**: minimaliseert de invoerlatentie voor een snellere reactie van toetsenbord en muis.

        - **Smooth Display**: optimaliseert de beeldweergave om haperingen en framedrops te voorkomen en zorgt voor een stabiele weergave.

- **Quality**: stel de videokwaliteit in op Auto/Low/Medium/High/Ultra-high/Lossless, afhankelijk van uw netwerkomgeving en de gewenste resolutie.

- **FEC Packets**: bij een onstabiel netwerk worden verloren datapakketten automatisch hersteld door een kleine hoeveelheid redundante gegevens mee te sturen. Dit vermindert flikkeren en haperingen van het beeld. U kunt de FEC-verhouding instellen op 5%/10%/15%/20%.

- **Orientation**: hiermee stelt u de draaihoek van de console in op 0°/90°/180°/270°.

- **EDID**: afkorting van Extended Display Identification Data. Hiermee worden automatisch de optimale weergaveparameters gekozen.

    De standaardinstelling is geschikt voor de meeste situaties en hoeft doorgaans niet te worden gewijzigd. Zie [hier](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} voor meer informatie. Als het scherm na het aanpassen van EDID niet wordt vernieuwd, start u het bestuurde apparaat opnieuw op.

- **View**: deze instelling bepaalt hoe het beeld wordt geschaald wanneer u het browservenster van grootte verandert. Beschikbare opties: Adaptive, Best Picture Quality, Original Pixel. Deze functie is geïntroduceerd in firmware v1.8.0.

### Audio en camera {#audio-camera}

U kunt de audio- en camera-instellingen voor het bestuurde apparaat aanpassen.

![Audio](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session-audio-camera.png){class="glboxshadow"}

- **Speaker**: hiermee regelt u de audio-uitvoer van het bestuurde apparaat (bijvoorbeeld systeemgeluiden of het geluid van video's).

- **Microphone**: hiermee verzendt u lokale audio (bijvoorbeeld uw stem) van het besturende apparaat naar de externe kant. De microfoon kan met één klik worden gedempt en met een sneltoets die u ingedrukt houdt worden geactiveerd (Press To Speak).

    **Opmerking**: De sneltoets moet vóór gebruik handmatig worden ingesteld in [Instellingen](#usb-devices).

- **Camera**: wanneer de camera op het besturende apparaat is ingeschakeld, worden lokale videobeelden via passthrough naar de externe host verzonden, waar een virtuele USB-camera wordt geëmuleerd. Toepassingen op de externe host (bijvoorbeeld vergadertools en FaceTime) kunnen deze videofeed gebruiken, met dezelfde gebruikerservaring als een fysieke camera die rechtstreeks op de externe host is aangesloten.
    
    **Opmerking**: Deze functie is geïntroduceerd in firmware v1.10.0 en wordt uitsluitend ondersteund in de modus WebRTC (FEC). Momenteel is de functie alleen beschikbaar via een webbrowser; de app en de desktopclient worden nog niet ondersteund.

### Toetsenbord {#keyboard}

Onder Keyboard kunt u instellingen configureren voor het gebruik van het toetsenbord op het bestuurde apparaat.

![Toetsenbord](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session_keyboard.png){class="glboxshadow"}

- **Bad Link Mode**: oftewel toetsen direct loslaten. Elke toetsaanslag wordt verzonden als één snelle druk-en-loslaatactie. Zo voorkomt u vastzittende toetsen of onbedoelde herhaalde invoer tijdens bediening op afstand.

- **Show Virtual Keyboard**: hiermee toont en gebruikt u het virtuele toetsenbord in de console.

    ![Virtueel toetsenbord weergeven](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session_show_virtual_keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: deze functie verwisselt de toetsen Cmd en Ctrl om de toetsenbordcompatibiliteit tussen verschillende besturingssystemen te garanderen.

### Muis {#mouse}

U kunt de muisinstellingen aanpassen voor een betere ervaring op het bestuurde apparaat.

![Muis](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session_mouse.png){class="glboxshadow"}

- **Show Local Cursor**: hiermee wordt de muisaanwijzer van het huidige apparaat op het scherm weergegeven.

- **Mouse Jiggle**: de functie Mouse Jiggle simuleert subtiele, periodieke muisbewegingen om te voorkomen dat het bestuurde apparaat bij langdurige inactiviteit in de slaapstand gaat, bijvoorbeeld tijdens online vergaderingen of serverbeheer.

- **Scroll Rate**: de snelheid waarmee het muiswiel scrolt, oftewel het aantal regels/eenheden per wielomwenteling. Dit bepaalt hoe snel de inhoud op het externe scherm beweegt.

- **Scroll Direction**: bepaalt of de inhoud op het externe scherm bij het omhoog/omlaag draaien van het muiswiel in dezelfde richting beweegt (natuurlijk scrollen) of in de tegenovergestelde richting (traditioneel scrollen).

    Er zijn vier richtingsmodi beschikbaar: Standard, Vertical Invert, Horizontal Invert en Both Invert.

- **Mouse Mode**: hiermee schakelt u tussen Absolute Mode en Relative Mode voor een soepele en nauwkeurige aanwijzerbesturing in verschillende situaties bij bediening op afstand.

    !!! note "Wat is het verschil tussen Absolute Mode en Relative Mode?"

        - **Relative Mode**: de muispositie wordt berekend op basis van de beweging in plaats van vaste schermcoördinaten. U moet in het externe venster klikken om de muis te bedienen. De aanwijzer is vergrendeld binnen het externe scherm en kan er niet soepel uit worden bewogen. Deze modus biedt een betere compatibiliteit met BIOS, oudere systemen en embedded apparaten.

        - **Absolute Mode**: de muispositie komt overeen met exacte schermcoördinaten. De externe aanwijzer volgt de lokale aanwijzer soepel en nauwkeurig, zodat u naadloos tussen uw lokale scherm en het externe scherm kunt bewegen. Deze modus is ideaal voor dagelijkse bediening van een bureaublad en voor nauwkeurige handelingen, al kan er door de netwerkoverdracht een lichte vertraging optreden.

        Kortom: gebruik de absolute muismodus voor soepele dagelijkse bediening en de relatieve muismodus voor toegang tot het BIOS, voor oudere apparaten die geen absolute positionering ondersteunen of om onbedoelde bewegingen van de aanwijzer te voorkomen.

- **Relative Sensitivity**: beschikbaar wanneer Mouse Mode is ingesteld op Relative.

- **Primary Button**: hiermee kiest u de linker- of rechterknop als primaire knop. Deze functie is geïntroduceerd in firmware v1.9.0.

## Toolbox {#toolbox}

Ga in de console naar **Toolbox**. De Toolbox-pagina bestaat uit vijf onderdelen:

- [Klembord](#clipboard)
- [OCR](#ocr)
- [Sneltoetsen](#shortcut)
- [Wake-on-LAN](#wake-on-lan)
- [Terminal](#terminal)

### Klembord {#clipboard}

Met het klembord kunt u eenvoudig tekst van het besturende apparaat in het bestuurde apparaat plakken, zonder bestanden over te zetten.

![Toolbox – klembord](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_clipboard.png){class="glboxshadow"}

### OCR {#ocr}

OCR is een functie voor tekstherkenning waarmee u een gebied op het externe scherm kunt selecteren en er eenvoudig tekst uit kunt halen. Deze functie is geïntroduceerd in firmware v1.9.0.

Klik hiervoor op de pijl omlaag en kies de gewenste herkenningstaal, zoals Chinees, Engels of tweetalig (Zh/En).

![Herkenningstaal](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_ocr.png){class="glboxshadow"}

Klik vervolgens op **Capture**; het externe scherm wordt dan gedimd. Trek een kader rond de tekst die u wilt overnemen; het systeem herkent de tekst automatisch. Daarna kunt u de herkende tekst naar behoefte kopiëren.

![Tekst kopiëren](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/ocr_copy_text.png){class="glboxshadow"}

Met deze functie kunt u eenvoudig tekst van het externe scherm (dus van het bestuurde apparaat) overnemen en naar het lokale besturende apparaat kopiëren.

### Sneltoetsen {#shortcut}

Met sneltoetsen voert u handelingen sneller uit zonder het virtuele toetsenbord te gebruiken. Zo werkt u efficiënter en bespaart u tijd bij dagelijkse taken. Hier vindt u enkele veelgebruikte sneltoetsen.

![Toolbox – sneltoetsen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_shorcut.png){class="glboxshadow"}

Klik op **Modify** om de sneltoetsopties naar wens aan te passen.

![Toolbox – sneltoetsen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_shorcut_modify.png){class="glboxshadow"}  

### Wake-on-LAN {#wake-on-lan}

Wake-on-LAN (WOL) is een technologie waarmee het bestuurde apparaat op afstand kan worden ingeschakeld of uit een energiebesparende stand kan worden gewekt.

Klik op **Add Device** en kies een apparaat uit hetzelfde LAN.

![Toolbox – WOL](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_wake_on_lan.png){class="glboxshadow"}

![WOL – apparaat toevoegen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/wol-add-device.png){class="glboxshadow" width=400}

Als het apparaat dat u wilt toevoegen niet in de lijst staat, klikt u op **Add Manually** en voert u de apparaatnaam en het MAC-adres in.

![WOL – handmatig toevoegen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/wol-add-manually.png){class="glboxshadow" width=400}

### Terminal {#terminal}

U kunt de terminal van de Comet 5G openen om geavanceerde instellingen uit te voeren. Klik op **Access**.

![Toolbox – terminal 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_terminal_1.png){class="glboxshadow"}

U wordt doorgestuurd naar de GLKVM-terminal.

![Toolbox – terminal 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_terminal_2.png){class="glboxshadow"}

## Accessoires {#accessories}

GL.iNet biedt optionele KVM-accessoires waarmee u het apparaat op afstand kunt in- en uitschakelen.

Sluit het accessoire eerst aan op uw bestuurde apparaat volgens de bijbehorende gebruikershandleiding.

- [Fingerbot (FGB-01) – gebruikershandleiding](../gl-fgb-01/index.md){target="_blank"}

- [ATX Board (GL-ATXPC) – gebruikershandleiding](../gl-atx-board/index.md){target="_blank"}

Meld u vervolgens aan bij de KVM-console en ga naar **Accessories**. De instellingen voor accessoires zijn pas beschikbaar nadat het accessoire is geïnstalleerd.

### Fingerbot {#fingerbot}
    
De Fingerbot wordt op de fysieke aan/uit-knop van het bestuurde apparaat geplakt, zodat u de voeding van het bestuurde apparaat op afstand kunt bedienen.
    
De Fingerbot werkt volgens de instellingen in de console.

![Accessoires – Fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/fingerbot.png){class="glboxshadow"}

- **Time**: de duur waarmee de Fingerbot drukt. U kunt deze instellen op 0,5s/3s/8s.

- **Strength**: er zijn twee niveaus van drukkracht: Lightly Press en Firmly Press.

    - **Lightly Press**: ideaal voor korte of licht indrukbare knoppen.
    
    - **Firmly Press**: ideaal voor diepe of stevige knoppen.

    ![Drukmodus](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/press_mode.png){class="glboxshadow gl-70-desktop"}

### ATX-voeding {#atx-power}

Het ATX Board wordt in de computerbehuizing geïnstalleerd om het apparaat op afstand in te schakelen, uit te schakelen of opnieuw op te starten.

Het werkt volgens de instellingen in de console.

![Accessoires – ATX-voeding](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/atxboard.png){class="glboxshadow"}

- **Power (Short Press)**: voor normaal inschakelen of het wekken van het systeem.

- **Power (Long Press)**: voert een geforceerde uitschakeling uit.

- **Restart**: start het apparaat opnieuw op.

## Virtuele media {#virtual-media}

Ga in de console naar **Virtual Media**. Hier kunt u de volgende handelingen uitvoeren:

- [Bestanden delen](#file-sharing)
- [Images koppelen](#image-mounting)
- [Opslagstation vervangen](#replace-storage-drive)
- [Schijf formatteren](#format-disk)

![Virtuele media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/virtual-media.png){class="glboxshadow"}
    
### Bestanden delen {#file-sharing}

De Comet 5G kan een USB-stick met lees- en schrijftoegang emuleren, zodat u bestanden kunt delen en beheren tussen het besturende en het bestuurde apparaat.

**Volg de onderstaande stappen om bestanden van het besturende apparaat met het bestuurde apparaat te delen.**

1. Sleep bestanden naar het vak of klik op het vak om bestanden van uw besturende apparaat te uploaden, of upload ze via een URL.

    Na het uploaden worden de bestanden als volgt weergegeven.

    ![Bestanden uploaden](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing1.png){class="glboxshadow"}

2. Klik op **Mount To Remote** -> **File Sharing**.

    ![Bestanden delen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing2.png){class="glboxshadow"}

3. In de console verschijnt een venster met de stappen voor het delen van bestanden, zoals hieronder weergegeven.
    
    ![Tips voor het delen van bestanden](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing3.png){class="glboxshadow"}

4. Even later verschijnt automatisch een station met de naam **"GLKVM"** op het scherm. U ziet dat de bestanden die u eerder van het besturende apparaat naar de Comet 5G hebt geüpload, nu met het bestuurde apparaat zijn gedeeld. U kunt de bestanden in dit station nu op het bestuurde apparaat bekijken, verplaatsen of verwijderen.

    ![GLKVM-schijf](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing4.png){class="glboxshadow"}

    **Tips**: Als het station niet automatisch verschijnt, gaat u op het bestuurde apparaat naar **This PC**.

    ![Deze pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/thispc.png){class="glboxshadow"}
    
    Zoek daar het station met de naam **GLKVM**. U kunt de bestanden in dit station nu bekijken, verplaatsen of verwijderen.

5. Als u wilt stoppen met delen, klikt u in de werkbalk op **Virtual Media** en vervolgens op **Stop Sharing**.

    ![Delen stoppen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/stop-sharing1.png){class="glboxshadow"}

**Volg de onderstaande stappen om bestanden van het bestuurde apparaat met het besturende apparaat te delen.**

1. Verplaats of kopieer op het bestuurde apparaat de bestanden die u wilt delen naar het station **GLKVM**.

    In dit voorbeeld is een pdf-bestand met de naam "slate7pro_datasheet" van het bureaublad van het bestuurde apparaat naar de schijf **GLKVM** verplaatst.

    ![Bestand naar schijf verplaatsen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing5.png){class="glboxshadow"}
    
2. Ga naar de console van de Comet 5G, klik in de werkbalk op **Virtual Media** en klik op **Stop Sharing**.

    ![Delen stoppen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/stop-sharing2.png){class="glboxshadow"}
    
3. Het bestand wordt dan onder **Virtual Media** weergegeven, zoals hieronder te zien is. U kunt dit bestand nu van de Comet 5G naar uw besturende apparaat downloaden.

    ![Bestand gedeeld](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing6.png){class="glboxshadow"}

### Images koppelen {#image-mounting}

De Comet 5G kan op het bestuurde apparaat een virtueel cd/dvd-station of schijfstation met alleen-lezentoegang simuleren. U kunt dit station gebruiken tijdens het opstarten van het BIOS of UEFI.
    
Met deze functie kunt u bijvoorbeeld het besturingssysteem opnieuw installeren, een ISO koppelen om toepassingen op het bestuurde apparaat te installeren of andere taken uitvoeren.
    
1. Sleep bestanden naar het vak of klik op het vak om bestanden te uploaden. **Zorg ervoor dat dit bestand als ISO-bestand kan worden gekoppeld**.

    Na het uploaden worden de bestanden als volgt weergegeven.

    ![Image koppelen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting1.png){class="glboxshadow"}
    
2. Klik op **Mount To Remote** -> **Image Mounting**.

    ![Image koppelen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting2.png){class="glboxshadow"}

3. Selecteer in het pop-upvenster het bestand en klik op **Mount Image**.

    ![Image koppelen 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting3.png){class="glboxshadow"}

4. In de console verschijnt een venster met de stappen voor het koppelen, zoals hieronder weergegeven.

    ![Image koppelen 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting4.png){class="glboxshadow"}

5. U kunt dit bestand nu vanaf het cd-station op het bestuurde apparaat gebruiken.

    ![Image koppelen 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting5.png){class="glboxshadow"}

### Opslagstation vervangen {#replace-storage-drive}

U kunt een USB-opslagapparaat in de USB-poort van de KVM steken om de interne opslag te vervangen.

![Opslagstation vervangen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/replace-storage.png){class="glboxshadow"}

### Schijf formatteren {#format-disk}

U kunt de schijf met één klik formatteren of de virtuele media uitschakelen.

![Schijf formatteren](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/format-storage.png){class="glboxshadow"}

- **Format**: wist alle gegevens op de schijf en initialiseert de bestandssysteemstructuur opnieuw.

- **Disable**: als u de virtuele media uitschakelt, wordt het KVM-apparaat direct opnieuw opgestart.

## Apps Center {#apps-center}

Ga in de console naar **Apps Center**. Hier vindt u de geïntegreerde toepassingen.

![Apps Center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} is een mesh-VPN-dienst op basis van WireGuard die versleutelde peer-to-peer privénetwerken tussen apparaten opzet, zonder port forwarding of ingewikkelde firewallconfiguratie.

De Comet 5G is geïntegreerd met Tailscale, zodat u het apparaat op afstand kunt openen via het virtuele netwerk van Tailscale.

Koppel de Comet 5G en uw besturende apparaat aan hetzelfde Tailscale-account. Daarna kunt u uw Comet 5G op afstand openen door het **Tailscale virtual IP** ervan in te voeren in een webbrowser op het besturende apparaat, zonder de GLKVM-app te installeren. Zie [hier](../../faq/remote_access_via_tailscale.md){target="_blank"} voor meer informatie.

Na het koppelen toont de console het gekoppelde Tailscale-account en worden geavanceerde functies zoals Exit Node en Subnet Routes beschikbaar.

![Tailscale ingeschakeld](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} maakt versleutelde virtuele overlaynetwerken die verspreide apparaten wereldwijd met elkaar verbinden alsof ze zich in hetzelfde lokale netwerk bevinden.

De Comet 5G is geïntegreerd met ZeroTier, zodat u het apparaat op afstand kunt openen via het virtuele netwerk van ZeroTier.

Voeg de Comet 5G en uw besturende apparaat toe aan hetzelfde ZeroTier-netwerk. Daarna kunt u uw Comet 5G op afstand openen door het **ZeroTier IP** ervan in te voeren in een webbrowser op het besturende apparaat, zonder de GLKVM-app te installeren. Zie [hier](../../faq/remote_access_via_zerotier.md){target="_blank"} voor meer informatie.

Na het koppelen toont de console de ZeroTier-netwerk-ID en het virtuele IP-adres.

![ZeroTier ingeschakeld](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/apps-zerotier-enabled.png){class="glboxshadow"}

### NetBird {#netbird}

[NetBird](https://netbird.io/){target="_blank"} is een opensource zero-trust-netwerkplatform waarmee u veilige privénetwerken kunt opzetten voor thuis- en zakelijk gebruik. Als overlaynetwerk op basis van WireGuard® biedt NetBird altijd en overal veilige toegang tot uw apparaten.

De Comet 5G is geïntegreerd met NetBird, zodat u het apparaat op afstand kunt openen via het virtuele netwerk van NetBird. Zie [hier](../../faq/remote_access_via_netbird.md){target="_blank"} voor meer informatie.

Na het koppelen toont de console het virtuele IP-adres van NetBird.

![NetBird ingeschakeld](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/apps-netbird-enabled.png){class="glboxshadow"}

## Help {#help}

Ga in de console naar **Help**. Hier vindt u meer informatie over de GL.iNet KVM en de helpdocumentatie, en kunt u logboeken exporteren voor probleemoplossing.

![Help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/help.png){class="glboxshadow"}

## Werkbalk {#toolbar}

Rechtsboven in de console vindt u de volgende hulpmiddelen:

- [Werkbalk samenvouwen](#collapse)
- [Volledig scherm](#fullscreen)
- [Upgrade](#upgrade)
- [Verbindingsstatistieken](#connection-stats)
- [Cloudservice](#cloud-service)
- [Afmelden](#logout)

### Samenvouwen {#collapse}

Klik rechtsboven op het pictogram met de pijl omhoog om de werkbalk samen te vouwen.

![Samenvouwen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_collapse_1.png){class="glboxshadow"}

Als de werkbalk is samengevouwen, klikt u bovenaan op het pictogram met de pijl omlaag om deze weer uit te vouwen.

![Samenvouwen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_collapse_2.png){class="glboxshadow"}

### Volledig scherm {#fullscreen}

Klik rechtsboven op het pictogram voor volledig scherm (een vierkant) om naar de modus voor volledig scherm over te schakelen.

![Volledig scherm 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_fullscreen_1.png){class="glboxshadow"}

Als u het volledige scherm wilt afsluiten, houdt u de toets **Esc** ingedrukt of klikt u rechtsboven op het pictogram voor het afsluiten van volledig scherm (een raster).

![Volledig scherm 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_fullscreen_2.png){class="glboxshadow"}

### Upgrade {#upgrade}

Klik rechtsboven op de firmwareversie om te controleren op updates.

![Firmware-upgrade 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_upgrade_1.png){class="glboxshadow"}

In het pop-upvenster kunt u op **Local Upgrade** klikken om een firmwarebestand te uploaden.

![Firmware-upgrade 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_upgrade_2.png){class="glboxshadow" width=400}

![Firmware-upgrade 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_upgrade_3.png){class="glboxshadow" width=400}

Download de nieuwste firmware via het [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} voordat u een lokale upgrade uitvoert.

### Verbindingsstatistieken {#connection-stats}

Connection Stats bevat een dashboard dat latentie, jitter en andere realtime meetwaarden bijhoudt.

Klik op het lijstpictogram om de apparaatstatus en realtime gegevens weer te geven.

![Gegevensdashboard 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/data_dashboard_1.png){class="glboxshadow"}

Klik op het grafiekpictogram om statistische gegevens te bekijken, waaronder netwerklatentie, netwerkjitter, pakketverlies, realtime framesnelheid en afspeelvertraging.

![Gegevensdashboard 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/data_dashboard_2.png){class="glboxshadow"}

### Cloudservice {#cloud-service}

Met GL.iNet KVM Cloud kunt u het bestuurde apparaat op afstand openen. Zie [hier](../../faq/remote_access_via_cloud.md){target="_blank"} voor meer informatie.

Zodra uw Comet 5G aan de cloud is gekoppeld, toont de console de cloudstatus als volgt.

![Cloudservice](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/cloud-services.png){class="glboxshadow"}

### Afmelden {#logout}

Klik op het pictogram Logout om u af te melden.
![Afmelden](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/logout.png){class="glboxshadow"}

## Instellingen {#settings}
Klik in de console op het pictogram Settings in de navigatiebalk om de volgende instellingenpagina te openen. Deze functie is geïntroduceerd in firmware v1.10.0.

- [USB-apparaten](#usb-devices)
- [Voorkeuren](#preferences)
- [Netwerk](#network)
- [Beveiliging](#security)
- [Cloud](#cloud)
- [Systeem](#system)

![Instellingen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting.png){class="glboxshadow"}

### USB-apparaten {#usb-devices}

USB Devices biedt centraal beheer van alle geëmuleerde USB-apparaten. Op deze pagina kunt u virtuele randapparaten in- of uitschakelen voor een betere compatibiliteit met de bestuurde host.

![Geëmuleerde USB-apparaten](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_usb_devices.png){class="glboxshadow"}

- **Microphone**
        
    Wanneer de microfoon is gedempt, kunt u op Settings klikken om sneltoetsen naar uw eigen voorkeur in te stellen. Houd de toegewezen sneltoets ingedrukt om te spreken; wanneer u de toets loslaat, wordt de microfoon weer gedempt.

    ![Microfooninstellingen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/mic_setting_1.png){class="glboxshadow" width=600}

    ![Microfooninstellingen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/mic_setting_2.png){class="glboxshadow" width=434}

- **Device Identity**

    Hiermee past u de identiteit van de KVM aan zoals die door het bestuurde apparaat wordt herkend. Let op: EDID en apparaatidentiteit blijven gesynchroniseerd. Als u een van beide wijzigt, wordt de andere automatisch bijgewerkt, zodat het apparaat correct wordt herkend.

    ![Apparaatidentiteit](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/settings_device_identity.png){class="glboxshadow" width=350}

### Voorkeuren {#preferences}

Onder Preferences beheert u de instellingen voor Layout Preferences, System Settings en Device Screen.

![Voorkeuren](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_preference.png){class="glboxshadow"}

- **Layout Preferences**: hier stelt u naar behoefte in of de werkbalk in de modus voor volledig scherm en de statusbalk in de venstermodus worden weergegeven.
  
- **System Settings**: hier stelt u de systeeminstellingen in, zoals de titel van het browsertabblad, de taal (Chinees, Engels of Japans), de kleurmodus (licht of donker) en de tijdzone voor uw regio.

- **Device Screen**: hier beheert u het scherm van het apparaat en kunt u een voorbeeld ervan bekijken. Beschikbare instellingen zijn onder meer de vergrendelschermmodus (World Clock, Clock Only of Wallpaper Only), Time Format, Date Format en Wallpaper.

### Netwerk {#network}

U kunt de netwerkgegevens van de Comet 5G bekijken en wijzigen, zoals de hostnaam en het IP-adres.

![Netwerk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network.png){class="glboxshadow"}

- **Hostname**: u kunt de hostnaam van het apparaat rechtstreeks in de console wijzigen. Deze functie is geïntroduceerd in firmware v1.7.0.

    ![Hostnaam wijzigen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_hostname.png){class="glboxshadow" width=600}

- **Ethernet Settings**: wanneer de Comet 5G via een ethernetkabel is verbonden met een bovenliggend netwerkapparaat, worden de ethernetgegevens hier weergegeven.

    Als het protocol DHCP is, ziet de pagina er als volgt uit.

    ![Ethernet DHCP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_dhcp.png){class="glboxshadow" width=600}

    Als u een statisch IP-adres wilt instellen, zet u het protocol op **Static** en voert u de vereiste netwerkparameters in (bijvoorbeeld IP-adres, netmasker en gateway).

    ![Ethernet statisch](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_static.png){class="glboxshadow" width=600}

- **Wireless**: de Comet 5G ondersteunt twee draadloze werkmodi, **Station Mode** en **AP Mode**, voor verschillende eisen aan netwerktoegang.

    Klik op **Modify** om de netwerkmodus te wijzigen of het IP-adres, de gateway en het MAC-adres te bekijken.

    ![Wifi wijzigen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_modify_wifi.png){class="glboxshadow" width=600} 

    - **Station Mode**

        Deze modus is geschikt wanneer er een bestaand draadloos netwerk beschikbaar is waarmee uw Comet 5G verbinding kan maken.
        
        In deze modus werkt de Comet 5G als draadloze client die een bovenliggende wifi-hotspot (bijvoorbeeld een router) kan zoeken en er verbinding mee kan maken om netwerktoegang te krijgen.

        ![Wifi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_wifi.png){class="glboxshadow"}

        Als u verbinding wilt maken met een ander wifinetwerk, klikt u onderaan op **Switch Wi-Fi**.

        ![Wifi wisselen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/switch_wifi_1.png){class="glboxshadow"}

        Selecteer vervolgens een wifinetwerk uit de lijst met beschikbare netwerken.

        ![Wifi wisselen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/switch-wifi2.png){class="glboxshadow"}

    - **AP Mode**

        Deze modus is ideaal voor het opzetten van een lokaal netwerk, zodat u uw KVM offline en van dichtbij kunt bedienen zonder extern netwerk.
    
        In deze modus fungeert de Comet 5G zelf als wifi-hotspot die een signaal uitzendt waarmee eindapparaten zoals smartphones en laptops verbinding kunnen maken. Het apparaat kan dan echter geen verbinding meer maken met het bovenliggende netwerk via wifi.
    
        ![Wifi-AP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/wifi-ap-mode.png){class="glboxshadow"}

- **Cellular**: de Comet 5G heeft een ingebouwde mobiele module die via een simkaart toegang geeft tot mobiele netwerken.

    Nadat de simkaart is gedetecteerd, kunt u op **Modify** klikken om de gegevens van de mobiele verbinding te bekijken (bijvoorbeeld providergegevens, telefoonnummer, ICCID en het huidige APN-profiel).

    ![Mobiel netwerk wijzigen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/celluar_modify.png){class="glboxshadow" width=600} 

    ![Mobiel netwerk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_cellular.png){class="glboxshadow"}
    
    - Met **SIM Settings** beheert u de configuratie van het mobiele netwerk (bijvoorbeeld APN en MTU aanpassen).
    
    - Met **AT command** kunt u AT-commando's uitvoeren om modemgerelateerde uitvoer op te vragen.
    
    - Met **Cellular Firewall** stelt u firewallregels in voor mobiele netwerken.

    Kortom: de mobiele verbinding is een betrouwbare back-upoptie wanneer er geen ethernet- of wifiverbinding beschikbaar is.

### Beveiliging {#security}

Onder Security kunt u het beheerderswachtwoord wijzigen, tweestapsverificatie inschakelen en een eigen TLS-certificaat instellen.

![Beveiliging](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_security.png){class="glboxshadow"}

- Beheerderswachtwoord wijzigen

    ![Beheerderswachtwoord wijzigen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/change-password.png){class="glboxshadow" width="434"}

- 2FA: schakel tweestapsverificatie in om uw account te beschermen.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/2fa.png){class="glboxshadow"}

- TLS-certificaat

    Het systeem gebruikt het vooraf geïnstalleerde standaardcertificaat voor toegang via de browser. Als u een eigen TLS-certificaat wilt gebruiken voor toegang via de webbrowser, klikt u onder TLS Certificate op **Custom** en uploadt u uw **certificaatbestand en privésleutelbestand**.

    ![Eigen TLS-certificaat](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_security_custom.png){class="glboxshadow"} 

### Cloud {#cloud}

Met Cloud kunt u uw apparaat op afstand openen en beheren via clouddiensten.

U kunt uw apparaat via een URL aan de cloud koppelen. Onder **More Settings** vindt u andere opties, zoals Bind With Code en App Download. Indien nodig is ook Disable beschikbaar.

![Cloud 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_cloud_1.png){class="glboxshadow"} 

Na een geslaagde koppeling kunt u de gegevens van het gekoppelde cloudaccount bekijken. Klik op **Access Cloud** om apparaten te beheren of klik op **More Settings** om de cloud naar behoefte uit te schakelen of het apparaat te ontkoppelen.

![Cloud 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_cloud_2.png){class="glboxshadow"} 

U kunt deze beheerhandelingen ook uitvoeren via Cloud Service in de werkbalk bovenaan.

### Systeem {#system}

In de systeeminstellingen kunt u het volgende configureren:

![Systeem](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_system.png){class="glboxshadow"} 

- **System**: klik op **Reboot** om het apparaat opnieuw op te starten, of klik op **Reset** om de huidige apparaatconfiguratie te wissen en het apparaat opnieuw in te stellen.

- **Upgrade**: u kunt Beta Center inschakelen om bètafirmware-updates te ontvangen, of Local Upgrade gebruiken om handmatig te installeren vanuit een lokaal bestand.
  
    ![Lokale upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setthing_system_local_update.png){class="glboxshadow" width=400} 

- **Help & Support**: met Export Log Files slaat u runtimelogboeken van het apparaat op voor probleemoplossing en after-salesondersteuning. Help Document biedt toegang tot gebruikershandleidingen, veelgestelde vragen en documentatie voor probleemoplossing.
