# EDID instellen voor de GL.iNet KVM {#how-to-set-edid-for-glinet-kvm}

## Wat is EDID? {#what-is-edid}

EDID (Extended Display Identification Data) is een standaardgegevensformaat dat is opgesteld door de Video Electronics Standards Association (VESA). Het is opgeslagen in het niet-vluchtige geheugen van het beeldscherm en bevat belangrijke informatie over het beeldscherm, zoals de fabrikant, de maximale resolutie en de verversingsfrequentie. Apparaten zoals computers kunnen de parameters van het uitgangssignaal automatisch aanpassen door de EDID uit te lezen, zodat het beeldscherm de beelden optimaal weergeeft.

Wanneer apparaten zoals computers, laptops en gameconsoles op een beeldscherm worden aangesloten, lezen ze over het algemeen automatisch de EDID uit om geschikte weergaveparameters in te stellen. Zo worden problemen zoals wazige beelden en flikkeren voorkomen en krijgt de gebruiker een helder en stabiel beeld.

De EDID-instellingen van de GL.iNet KVM zijn bedoeld om automatisch de optimale parameters van het beeldscherm te kiezen. Wanneer een GL.iNet KVM op het bestuurde apparaat wordt aangesloten, kan deze door de EDID van het beeldscherm uit te lezen de beelduitvoer automatisch aanpassen voor het beste beeld.

## Vooraf ingestelde EDID {#preset-edid}

Ga in de console van de GL.iNet KVM naar **Settings** -> **Video** -> **EDID**. Hier vindt u enkele vooraf ingestelde EDID-instellingen.

![Vooraf ingestelde EDID](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_preset.jpg){class="glboxshadow"}

**De standaard-EDID van de GL.iNet KVM is al geschikt voor de meeste situaties en hoeft doorgaans niet te worden gewijzigd**.

In bijzondere situaties, bijvoorbeeld om UEFI/BIOS te configureren of de resolutie/verversingsfrequentie aan te passen, kunt u een vooraf ingestelde waarde selecteren, zoals 1920×1280/AUO/60HZ.

## Aangepaste EDID {#custom-edid}

Als u geen geschikte EDID-code kunt vinden, kunt u [deze link](https://github.com/linuxhw/EDID){target="blank"} raadplegen of de onderstaande stappen volgen om een aangepaste EDID-configuratie te maken.

!!! Tip "Tip"

    Het kan lastig zijn een EDID te vinden die precies overeenkomt met de gewenste resolutie en verversingsfrequentie. U kunt EDID-bewerkingstools zoals **RTDtool** of **EEditZ** gebruiken om een bestaande EDID naar uw specifieke wensen aan te passen.

1. Zoek [hier](https://github.com/linuxhw/EDID){target="blank"} een geschikte EDID en kopieer deze.

2. Meld u aan bij de console van de GL.iNet KVM en ga naar **Settings** -> **EDID**. Schakel over naar de modus **Customize**, plak de parameters in het invoervak en klik op **Set Custom** om de instellingen toe te passen.

    ![Aangepaste EDID](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_customize.png){class="glboxshadow"}

!!! Note "Opmerking"

    1. De resolutie mag niet hoger zijn dan 2560×1440@60Hz. Een resolutie van 2560×1600@60Hz wordt bijvoorbeeld niet ondersteund.
    2. De maximaal ondersteunde verversingsfrequentie is 60Hz. Voor resoluties hoger dan 1920x1080 wordt een framesnelheid van 60FPS of lager aanbevolen.
    3. Neem geen interlaced resoluties op, omdat het beeld dan niet correct wordt weergegeven.
    4. De ingevoerde EDID-code mag uit niet meer dan twee blokken bestaan.
    5. Basale audio-ondersteuning is vereist. Anders kan de geluidskaart op het bestuurde apparaat mogelijk niet worden geselecteerd en is er geen geluid.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
