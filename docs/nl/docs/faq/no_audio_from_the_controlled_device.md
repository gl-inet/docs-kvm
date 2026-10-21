# Wat moet ik doen als er geen geluid van het bestuurde apparaat komt? {#what-should-i-do-if-theres-no-audio-from-the-controlled-device}

Als u na het aansluiten van de KVM en het bestuurde apparaat geen geluid van het bestuurde apparaat hoort (bijvoorbeeld geen geluid bij het afspelen van video's op het apparaat), kunt u de volgende tips proberen:

1. Controleer of Speaker is ingeschakeld in de KVM-console.

    Ga in de KVM-console naar **Settings** -> **Remote Device Settings** -> **Speaker** en controleer of de luidspreker is ingeschakeld. Controleer ook of het pictogram rechtsonder oplicht (wat aangeeft dat de luidspreker actief is).

    ![Luidspreker](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/speaker.png){class="glboxshadow"}

2. Controleer of alle kabels tussen de KVM en het bestuurde apparaat stevig zijn aangesloten. Losse bedrading kan de audio-uitvoer beïnvloeden.

3. Controleer of er een HDMI-converter is aangesloten. Sommige converters ondersteunen geen audio.

    Het wordt aanbevolen de meegeleverde HDMI-kabel te gebruiken, omdat sommige HDMI-kabels volgens oudere standaarden geen audio-overdracht ondersteunen.

4. Controleer of het geluid op het hostapparaat en het bestuurde apparaat is gedempt.

5. Controleer de uitvoerinstellingen van uw bestuurde apparaat en zorg ervoor dat **GLKVM** als uitvoerapparaat is ingesteld.

    ??? "macOS"

        Ga op uw bestuurde apparaat naar **Settings** -> **Sound** -> **Output & Input** -> **Output** en stel **GLKVM** in als uitvoerapparaat.

        ![Uitvoerinstellingen op de Mac](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/mac_output_settings.png){class="glboxshadow"}

    ??? "Windows"

        Ga op uw bestuurde apparaat naar **Settings** -> **Sound** -> **Output** en stel **GLKVM** in als uitvoerapparaat.

        ![Uitvoerinstellingen in Windows 1](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_1.png){class="glboxshadow"}

        ![Uitvoerinstellingen in Windows 2](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_2.png){class="glboxshadow"}

        U kunt ook rechtsonder op uw bestuurde apparaat op het geluidspictogram klikken en **GLKVM** als afspeelapparaat selecteren.

        ![Uitvoerinstellingen in Windows 3](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_3.png){class="glboxshadow"}

6. Controleer het stuurprogramma van de grafische kaart van het bestuurde apparaat. Als het bestuurde apparaat geen stuurprogramma voor de grafische kaart heeft, kan het geen audio uitvoeren en is er aan de besturende kant dus geen geluid te horen.

7. Controleer de geavanceerde geluidsinstellingen op uw hostapparaat en zorg ervoor dat uw browser een actieve volume-uitvoer heeft.

    Hieronder ziet u ter referentie een voorbeeld van de geavanceerde geluidsinstellingen in Windows 10 Pro.

    Ga naar **Settings** -> **Sound** -> **Advanced sound options**.

    ![Geavanceerde geluidsopties](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/advanced_sound_options.png){class="glboxshadow"}

    Pas het volume aan voor specifieke apps en systeemgeluiden.

    ![Volume per app](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/app_volume.png){class="glboxshadow"}

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
