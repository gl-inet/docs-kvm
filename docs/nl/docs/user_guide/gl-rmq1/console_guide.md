# Comet Q (GL-RMQ1) – consolehandleiding {#comet-q-gl-rmq1-console-guide}

## Instellingen {#settings}

Ga in de console naar **Settings**. De instellingenpagina bestaat uit vier onderdelen:

- [Video](#video)
- [Audio, toetsenbord en muis](#audiokeyboardmouse)
- [Systeem](#system)
- [Netwerk](#network)

### Snel zoeken {#quick-search}

U kunt snel de gewenste instellingen vinden door bovenaan de pagina Settings trefwoorden in te voeren.

![Snel zoeken](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/quick-search.png){class="glboxshadow"}

### Video {#video}

U kunt de video-instellingen in de console aanpassen, zoals EDID, de videokwaliteit, de videoverzending en de schermstand.

![Video-instellingen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-video.png){class="glboxshadow"}

- **Type**: selecteer het type van uw bestuurde apparaat.

    Het systeem past automatisch de aanbevolen muismodus en EDID-instellingen toe voor de beste beeldverhouding en bedieningsnauwkeurigheid. Wijzig deze optie als het apparaat niet correct wordt herkend of als u een aangepast type wilt gebruiken.

- **EDID**: afkorting van Extended Display Identification Data. Hiermee worden automatisch de optimale weergaveparameters gekozen.

    De standaardinstelling is geschikt voor de meeste situaties en hoeft doorgaans niet te worden gewijzigd. Zie [hier](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} voor meer informatie. Als het scherm na het aanpassen van EDID niet wordt vernieuwd, start u het bestuurde apparaat opnieuw op.

- **Mode**: schakel naar behoefte tussen de modus Smart en Normal. De modus Smart helpt het bandbreedtegebruik te verminderen, vooral bij zwakke netwerken.

- **Quality**: stel de videokwaliteit in op Low/Medium/High/Ultra-high/Lossless, afhankelijk van uw netwerkomgeving en de gewenste resolutie.

- **Transfer**: hiermee kiest u de methode voor videoverzending: WebRTC, WebRTC (FEC) of Direct. Let op: bij Direct wordt geen geluid verzonden.

    !!! note "Wat is het verschil tussen WebRTC, WebRTC (FEC) en Direct?"

        - **WebRTC**: zorgt voor een balans tussen vloeiend beeld en stabiel geluid bij realtime bediening op afstand.
        
        - **WebRTC (FEC)**: voegt voorwaartse foutcorrectie toe om de verbinding stabieler te maken bij een slecht of onstabiel netwerk. Als deze optie is geselecteerd, worden verloren datapakketten automatisch hersteld door een kleine hoeveelheid redundante gegevens mee te sturen. Dit vermindert flikkeren en haperingen van het beeld.
        
        - **Direct**: biedt de laagste latentie en verliesvrije beeldkwaliteit, maar ondersteunt geen audioverzending.

- **Orientation**: hiermee stelt u de draaihoek van de console in op 0°/90°/180°/270°.

- **View**: deze instelling bepaalt hoe het beeld wordt geschaald wanneer u het browservenster van grootte verandert. Beschikbare opties: Adaptive, Best Picture Quality, Original Pixel.

### Audio, toetsenbord en muis {#audiokeyboardmouse}

U kunt de instellingen voor audio, toetsenbord en muis aanpassen.

![Audio, toetsenbord en muis](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/audio-keyboard-mouse.png){class="glboxshadow"}

- **Speaker**: hiermee regelt u de audio-uitvoer van het bestuurde apparaat (bijvoorbeeld systeemgeluiden of het geluid van video's).

- **Microphone**: hiermee verzendt u lokale audio (bijvoorbeeld uw stem) van het besturende apparaat naar de externe kant. De microfoon kan met één klik worden gedempt en met een sneltoets die u ingedrukt houdt worden geactiveerd (Press To Speak).

    ![Microfooninstellingen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/mic-settings.png){class="glboxshadow"}

    ![Press To Speak](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/press-to-speak.png){class="glboxshadow"}

- **Keyboard**: hiermee schakelt u het toetsenbord van het bestuurde apparaat in of uit.

- **Bad Link Mode**: oftewel toetsen direct loslaten. Elke toetsaanslag wordt verzonden als één snelle druk-en-loslaatactie. Zo voorkomt u vastzittende toetsen of onbedoelde herhaalde invoer tijdens bediening op afstand.

- **Show Virtual Keyboard**: hiermee toont en gebruikt u het virtuele toetsenbord in de console.

    ![Virtueel toetsenbord weergeven](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: deze functie verwisselt de toetsen Cmd en Ctrl om de toetsenbordcompatibiliteit tussen verschillende besturingssystemen te garanderen.

- **Mouse**: hiermee schakelt u de muis van het bestuurde apparaat in of uit.

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

### Systeem {#system}

U kunt de systeemweergave-instellingen van de console aanpassen of het apparaat met één klik resetten.

![Systeeminstellingen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-system.png){class="glboxshadow"}

- **Device Identity**: hiermee past u de identiteit van de KVM aan zoals die door het bestuurde apparaat wordt herkend. Let op: EDID en apparaatidentiteit blijven gesynchroniseerd. Als u een van beide wijzigt, wordt de andere automatisch bijgewerkt, zodat het apparaat correct wordt herkend.

    ![Apparaatidentiteit](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/device-identity.png){class="glboxshadow"}

- **Language**: stel de taal van de console in op Chinees of Engels.

- **Color Mode**: stel het kleurthema in op de lichte of donkere modus.

- **Time Zone**: stel de tijdzone van de KVM-console in.

- **Reset KVM**: zet uw KVM met één klik terug naar de fabrieksinstellingen.

### Netwerk {#network}

U kunt de netwerkgegevens van de Comet Q bekijken en wijzigen, zoals de hostnaam en het IP-adres.

![Netwerkinstellingen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-network.png){class="glboxshadow"}

- **Hostname**: u kunt de hostnaam van het apparaat rechtstreeks in de console wijzigen.

    ![Hostnaam wijzigen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/hostname.png){class="glboxshadow"}

- **Wi-Fi**: wanneer de Comet Q met een wifinetwerk is verbonden, wordt hier het wifi-IP-adres weergegeven. Klik op de wifi-SSID of op de pijl naar rechts om de wifigegevens te bekijken, waaronder de SSID, het toegewezen IP-adres, de gateway en het MAC-adres waarmee uw Comet Q verbinding maakt.

    ![Wifi-configuratie](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/wifi-config.png){class="glboxshadow"}

    Als u verbinding wilt maken met een ander wifinetwerk, klikt u op **Switch Wi-Fi** en selecteert u een wifinetwerk uit de lijst met beschikbare netwerken.

## Toolbox {#toolbox}

Ga in de console naar **Toolbox**. De Toolbox-pagina bestaat uit drie onderdelen:

- [Klembord](#clipboard)
- [Sneltoetsen](#shortcut)
- [Terminal](#terminal)

### Klembord {#clipboard}

Met het klembord kunt u eenvoudig tekst van het besturende apparaat in het bestuurde apparaat plakken, zonder bestanden over te zetten.

![Toolbox – klembord](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-clipboard.png){class="glboxshadow"}

### Sneltoetsen {#shortcut}

Met sneltoetsen voert u handelingen sneller uit zonder het virtuele toetsenbord te gebruiken. Zo werkt u efficiënter en bespaart u tijd bij dagelijkse taken. Hier vindt u enkele veelgebruikte sneltoetsen.

![Toolbox – sneltoetsen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut1.png){class="glboxshadow"}

Klik op **Modify** om de sneltoetsopties naar wens aan te passen.

![Toolbox – sneltoetsen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut2.png){class="glboxshadow"}  

### Terminal {#terminal}

U kunt de terminal van de Comet Q openen om geavanceerde instellingen uit te voeren. Klik op **Access**.

![Toolbox – terminal 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal1.png){class="glboxshadow"}

U wordt doorgestuurd naar de GLKVM-terminal.

![Toolbox – terminal 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal2.png){class="glboxshadow"}

## Virtuele media {#virtual-media}

Ga in de console naar **Virtual Media**. De Comet Q kan een USB-stick met lees- en schrijftoegang emuleren, zodat u bestanden kunt delen en beheren tussen het besturende en het bestuurde apparaat.

![Virtuele media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-media.png){class="glboxshadow"}

### Bestanden delen {#file-sharing}

**Volg de onderstaande stappen om bestanden van het besturende apparaat met het bestuurde apparaat te delen.**

1. Sleep bestanden naar het vak of klik op het vak om bestanden van uw besturende apparaat te uploaden, of upload ze via een URL.

    Na het uploaden worden de bestanden als volgt weergegeven.

    ![Bestanden delen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing1.png){class="glboxshadow"}

2. Klik op **Mount To Remote** -> **File Sharing**.

    ![Bestanden delen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing2.png){class="glboxshadow"}

3. In de console verschijnt een venster met de stappen voor het delen van bestanden, zoals hieronder weergegeven.
    
    ![Bestanden delen 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing3.png){class="glboxshadow"}

4. Even later kan er automatisch een station met de naam **"GLKVM"** op het scherm verschijnen. U ziet dat de bestanden die u eerder van het besturende apparaat naar de Comet Q hebt geüpload, nu met het bestuurde apparaat zijn gedeeld. U kunt de bestanden in dit station nu op het bestuurde apparaat bekijken, verplaatsen of verwijderen.

    ![Bestanden delen 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing4.png){class="glboxshadow"}

    **Tips**: Als het station niet automatisch verschijnt, gaat u op het bestuurde apparaat naar **This PC**.

    ![Deze pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/thispc.png){class="glboxshadow"}
    
    Zoek daar het station met de naam **GLKVM**. U kunt de bestanden in dit station nu bekijken, verplaatsen of verwijderen.

5. Als u wilt stoppen met delen, klikt u in de werkbalk op **Virtual Media** en vervolgens op **Stop Sharing**.

    ![Delen stoppen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing1.png){class="glboxshadow"}

**Volg de onderstaande stappen om bestanden van het bestuurde apparaat met het besturende apparaat te delen.**

1. Verplaats of kopieer op het bestuurde apparaat de bestanden die u wilt delen naar het station **GLKVM**.

    In dit voorbeeld is een pdf-bestand met de naam "gl-rm10_datasheet" van het bureaublad van het bestuurde apparaat naar het station **GLKVM** verplaatst.

    ![Bestanden delen 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing5.png){class="glboxshadow"}
    
2. Ga naar de console van de Comet Q, klik in de werkbalk op **Virtual Media** en klik op **Stop Sharing**.

    ![Delen stoppen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing2.png){class="glboxshadow"}
    
3. Het bestand wordt dan onder **Virtual Media** weergegeven, zoals hieronder te zien is. U kunt dit bestand nu van de Comet Q naar uw besturende apparaat downloaden.

    ![Bestanden delen 6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing6.png){class="glboxshadow"}

### Schijf formatteren {#format-disk}

U kunt de schijf met één klik formatteren of de virtuele media uitschakelen.

![Schijf formatteren](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/format-disable.png){class="glboxshadow"}

- **Format**: wist alle gegevens op de schijf en initialiseert de bestandssysteemstructuur opnieuw.

- **Disable**: als u de virtuele media uitschakelt, wordt het KVM-apparaat direct opnieuw opgestart.

## Apps Center {#apps-center}

Ga in de console naar **Apps Center**. Hier vindt u de geïntegreerde toepassingen.

![Apps Center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} is een mesh-VPN-dienst op basis van WireGuard die versleutelde peer-to-peer privénetwerken tussen apparaten opzet, zonder port forwarding of ingewikkelde firewallconfiguratie.

De Comet Q is geïntegreerd met Tailscale, zodat u het apparaat op afstand kunt openen via het virtuele netwerk van Tailscale.

Koppel de Comet Q en uw besturende apparaat aan hetzelfde Tailscale-account. Daarna kunt u uw Comet Q op afstand openen door het **Tailscale virtual IP** ervan in te voeren in een webbrowser op het besturende apparaat, zonder de GLKVM-app te installeren. Zie [hier](../../faq/remote_access_via_tailscale.md){target="_blank"} voor meer informatie.

Na het koppelen toont de console het gekoppelde Tailscale-account en worden geavanceerde functies zoals Exit Node en Subnet Routes beschikbaar.

![Tailscale ingeschakeld](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} maakt versleutelde virtuele overlaynetwerken die verspreide apparaten wereldwijd met elkaar verbinden alsof ze zich in hetzelfde lokale netwerk bevinden.

De Comet Q is geïntegreerd met ZeroTier, zodat u het apparaat op afstand kunt openen via het virtuele netwerk van ZeroTier.

Voeg de Comet Q en uw besturende apparaat toe aan hetzelfde ZeroTier-netwerk. Daarna kunt u uw Comet Q op afstand openen door het **ZeroTier IP** ervan in te voeren in een webbrowser op het besturende apparaat, zonder de GLKVM-app te installeren. Zie [hier](../../faq/remote_access_via_zerotier.md){target="_blank"} voor meer informatie.

Na het koppelen toont de console de ZeroTier-netwerk-ID en het virtuele IP-adres.

![ZeroTier ingeschakeld](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-zerotier-enabled.png){class="glboxshadow"}

## Help {#help}

Ga in de console naar **Help**. Hier vindt u meer informatie over de GL.iNet KVM en de helpdocumentatie, en kunt u logboeken exporteren voor probleemoplossing.

![Help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/help.png){class="glboxshadow"}

## Werkbalk {#toolbar}

Rechtsboven in de console vindt u de volgende hulpmiddelen:

- [Werkbalk samenvouwen](#collapse)
- [Volledig scherm](#fullscreen)
- [Upgrade](#upgrade)
- [Cloudservice](#cloud-service)
- [Beveiliging](#security)
- Opnieuw opstarten
- Afmelden

### Samenvouwen {#collapse}

Klik rechtsboven op het pictogram met de pijl omhoog om de werkbalk samen te vouwen.

![Samenvouwen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse1.png){class="glboxshadow"}

Als de werkbalk is samengevouwen, klikt u bovenaan op het pictogram met de pijl omlaag om deze weer uit te vouwen.

![Samenvouwen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse2.png){class="glboxshadow"}

### Volledig scherm {#fullscreen}

Klik rechtsboven op het pictogram voor volledig scherm (een vierkant) om naar de modus voor volledig scherm over te schakelen.

![Volledig scherm 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen1.png){class="glboxshadow"}

Als u het volledige scherm wilt afsluiten, houdt u de toets **Esc** ingedrukt of klikt u rechtsboven op het pictogram voor het afsluiten van volledig scherm (een raster).

![Volledig scherm 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen2.png){class="glboxshadow"}

### Upgrade {#upgrade}

Klik rechtsboven op de firmwareversie om te controleren op updates.

![Firmware-upgrade 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade1.png){class="glboxshadow"}

In het pop-upvenster kunt u een online upgrade uitvoeren als er nieuwere firmware beschikbaar is. U kunt ook de nieuwste firmware downloaden via het [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} en naar behoefte een lokale upgrade uitvoeren.

![Firmware-upgrade 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade2.png){class="glboxshadow"}

### Cloudservice {#cloud-service}

Met GL.iNet KVM Cloud kunt u het bestuurde apparaat op afstand openen. Zie [hier](../../faq/remote_access_via_cloud.md){target="_blank"} voor meer informatie.

Zodra uw Comet Q aan de cloud is gekoppeld, toont de console de cloudstatus als volgt.

![Cloudservice](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/cloud.png){class="glboxshadow"}

### Beveiliging {#security}

Onder Security kunt u het beheerderswachtwoord wijzigen, tweestapsverificatie inschakelen en een eigen TLS-certificaat instellen.

![Beveiliging](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/security.png){class="glboxshadow"}

- Beheerderswachtwoord wijzigen

    ![Beheerderswachtwoord wijzigen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/admin-password.png){class="glboxshadow" width="434"}

- 2FA: schakel tweestapsverificatie in om uw account te beschermen.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/2fa.png){class="glboxshadow"}

- TLS-certificaat

    Het systeem gebruikt het vooraf geïnstalleerde standaardcertificaat voor toegang via de browser. Als u een eigen TLS-certificaat wilt gebruiken voor toegang via de webbrowser, klikt u rechtsboven in de console op **TLS Certificate**, selecteert u **Custom Certificate** en uploadt u uw **certificaatbestand en privésleutelbestand**.

    ![Eigen TLS-certificaat](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/tls-certificate.png){class="glboxshadow"}
