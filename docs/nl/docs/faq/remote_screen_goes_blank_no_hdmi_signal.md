# Wat moet ik doen als het externe scherm zwart wordt of geen HDMI-signaal toont? {#what-should-i-do-if-the-remote-screen-goes-blank-or-shows-no-hdmi-signal}

Als het externe scherm bij toegang tot het bestuurde apparaat via de KVM leeg blijft of geen HDMI-signaal toont, volgt u de onderstaande stappen om het probleem op te lossen.

![Wit scherm](https://static.gl-inet.com/docs/kvm/faq/blank_screen/white_screen.png){class="glboxshadow"}
<small>(Wit scherm)</small>

![Zwart scherm](https://static.gl-inet.com/docs/kvm/faq/blank_screen/black_screen.png){class="glboxshadow"}
<small>(Zwart scherm)</small>

Controleer eerst of het probleem met de videoverzending te maken heeft. Meld u aan bij uw KVM, ga naar **Settings** -> **Video** -> **Transfer** en stel de verzendmodus in op **Direct**.

![Verzendmodus wijzigen](https://static.gl-inet.com/docs/kvm/faq/blank_screen/change_transfer.png){class="glboxshadow" width="360"}

Als het probleem zich blijft voordoen, controleert u de onderstaande mogelijke oorzaken een voor een.

## De hardwareverbinding controleren {#check-hardware-connection}

1. **Defecte HDMI-kabel**

    Verouderde HDMI-kabels, geoxideerde connectoren of interne breuken kunnen de signaaloverdracht onderbreken. Vervang de kabel door een HDMI-kabel van goede kwaliteit.

    U kunt de status van het HDMI-signaal ook in de KVM-console controleren. Zoek rechtsonder het monitorpictogram en controleer of daar "No HDMI signal" staat.

    ![Geen HDMI-signaal](https://static.gl-inet.com/docs/kvm/faq/blank_screen/no_hdmi_signal.png){class="glboxshadow"}

2. **Onjuiste aansluiting**

    Als uw bestuurde apparaat een desktop-pc is, controleer dan of de **HDMI IN**-poort van de KVM is aangesloten op de HDMI OUT-poort van de grafische kaart of het moederbord van de desktop. Zorg ervoor dat de stekker volledig en stevig is ingestoken. Probeer bij apparaten met meerdere HDMI-uitgangen (bijvoorbeeld een aparte GPU en een uitgang op het moederbord) een andere poort.

    Als uw bestuurde apparaat een laptop is, controleer dan of de **HDMI IN**-poort van de KVM is aangesloten op de HDMI OUT-poort van de laptop.

    Tip: sommige KVM-modellen (zoals de Comet Pro en Comet 5G) hebben twee HDMI-poorten. Zorg ervoor dat de HDMI-kabel van het bestuurde apparaat in de HDMI IN-poort van de KVM zit. Als de kabel op HDMI OUT is aangesloten, wordt er in de KVM-console geen HDMI-signaal gedetecteerd.

3. **Onjuist gebruik van adapters**

    Als er een HDMI-adapter nodig is, gebruikt u een **VGA-naar-HDMI**-adapter om het bestuurde apparaat aan te sluiten op de HDMI IN-poort van de GL.iNet KVM.
    
    Met een HDMI-naar-VGA-adapter worden de videosignalen bij deze aansluiting niet correct overgedragen en blijft het scherm leeg.

    ![Vergelijking van adapters](https://static.gl-inet.com/docs/kvm/faq/blank_screen/adapter_comparison.png){class="glboxshadow"}

## De browserinstellingen controleren {#check-browser-settings}

Als u het bestuurde apparaat via een browser opent en het scherm leeg blijft, probeert u de volgende methoden:

1. **Test met meerdere browsers.** Probeer Chrome, Firefox, Edge enzovoort om vast te stellen of het probleem aan een specifieke browser ligt.

2. **Schakel extensies voor WebRTC-lekbescherming of -beheer uit.** Als u extensies of plug-ins in uw webbrowser hebt geïnstalleerd die WebRTC-verbindingen kunnen beïnvloeden, schakelt u deze uit en test u opnieuw. U kunt ook in de browser naar Settings -> Privacy & Security gaan om te controleren of de webbrowser WebRTC-verbindingen toestaat.

    ![WebRTC](https://static.gl-inet.com/docs/kvm/faq/blank_screen/webrtc.png){class="glboxshadow"}

## Status en instellingen van het bestuurde apparaat controleren {#check-controlled-device-status-and-settings}

1. **Apparaat niet ingeschakeld of in de slaapstand**

    Controleer of het bestuurde apparaat volledig is ingeschakeld en niet door energiebeheerinstellingen in de slaapstand of sluimerstand staat (wek het apparaat indien nodig met de knoppen ter plaatse).

2. **Afwijkende stuurprogramma's van de grafische kaart op het bestuurde apparaat**

    Niet-geïnstalleerde of beschadigde stuurprogramma's van de grafische kaart kunnen ervoor zorgen dat er geen videosignaal wordt uitgevoerd. Werk de stuurprogramma's van de grafische kaart op het bestuurde apparaat bij of installeer ze opnieuw (terwijl u lokaal bent aangemeld).

3. **Onjuiste aansluiting bij aparte en geïntegreerde grafische kaart**

    Als het bestuurde apparaat zowel een aparte als een geïntegreerde grafische kaart heeft, controleer dan of de HDMI-kabel op de juiste grafische poort is aangesloten (sluit de HDMI-kabel bijvoorbeeld aan op de poort van de aparte grafische kaart als die is geïnstalleerd).

4. **Afwijkende weergave-instellingen op het bestuurde apparaat (kleine kans)**

    Wanneer de GL.iNet KVM op het bestuurde apparaat wordt aangesloten, past de KVM de beelduitvoer automatisch aan door de EDID van de monitor uit te lezen voor optimale prestaties. De standaard-EDID-configuratie is in de meeste gevallen geschikt en hoeft niet te worden gewijzigd.

    Als het bestuurde apparaat compatibel is met standaardmonitoren, is de kans klein dat er bij toegang via GLKVM een leeg scherm of weergaveproblemen optreden. Enkele specifieke compatibiliteitsproblemen (bijvoorbeeld een Linux-systeem met een ASUS-monitor) kunnen echter een leeg scherm veroorzaken bij gebruik van GLKVM.

    Controleer of uw bestuurde apparaat compatibel is met standaardmonitoren en of het compatibiliteitsproblemen heeft met een specifieke monitor.

5. **Probleem met de resolutie**
   
    Wanneer GLKVM is aangesloten op bepaalde besturingssystemen (bijvoorbeeld Proxmox VE Hypervisor), kan het voorkomen dat de beschikbare beeldschermresolutie niet correct wordt afgestemd, wat tot weergaveproblemen leidt. Dit kunt u oplossen door de resolutie op het bestuurde apparaat handmatig aan te passen.

    Hieronder vindt u ter referentie een handleiding voor het wijzigen van de systeemresolutie in Proxmox VE Hypervisor.
    
    1. Open de PVE-terminal en voer de onderstaande opdracht in om het bestand `/etc/default/grub` te bewerken.

        ```
        nano /etc/default/grub
        ```

    2. Voeg de volgende regel toe.

        ```
        GRUB_CMDLINE_LINUX_DEFAULT="quiet gfxpayload=text nomodeset"
        ```

    3. Verwijder het commentaarteken voor de regel `GRUB_GFXMODE` door de `#` te verwijderen en stel de gewenste resolutie in, bijvoorbeeld `1024x768`.

        ```
        GRUB_GFXMODE=1024x768
        ```

    4. Druk op `Ctrl + O` en op Enter om de configuratie op te slaan.

    5. Druk op `Ctrl + X` om de nano-editor af te sluiten.

    6. Voer de onderstaande opdracht in om de configuratie toe te passen.

        ```
        update-grub
        ```
        
---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
