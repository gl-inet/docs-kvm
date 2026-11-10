# Hoe gebruikt u tweerichtingsaudio tijdens vergaderingen op afstand? {#how-can-i-use-two-way-audio-for-remote-meetings}

Als u thuiswerkt, kunt u via de KVM toegang krijgen tot uw kantoorcomputer en deelnemen aan audiovergaderingen in Zoom, Microsoft Teams of een vergelijkbare app. Met tweerichtingsaudio op de GL.iNet KVM spreekt u via de microfoon van uw lokale computer en hoort u de andere deelnemers via de luidsprekers of hoofdtelefoon van die computer.

## Snelle installatie {#quick-setup}

Volg de onderstaande stappen om de microfoon en luidspreker van uw lokale apparaat te gebruiken tijdens vergaderingen op afstand. In dit voorbeeld gebruikt u Zoom.

1. Meld u vóór deelname aan de vergadering op de besturende computer aan bij uw KVM en ga naar **Session** -> **Audio & Camera**. Schakel **Speaker** en **Microphone** in. Controleer of beide pictogrammen rechtsonder actief zijn.

    ![Luidspreker en microfoon inschakelen](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/enable-speaker-and-microphone.png){class="glboxshadow"}

    Wanneer u bijvoorbeeld **Microphone** inschakelt, kan uw browser om toegang tot de microfoon vragen. Selecteer de microfoon die u wilt gebruiken en sta toegang toe.

    ![Verzoek om microfoontoegang](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/microphone-permission-popup.png){class="glboxshadow"}

2. Open Zoom en neem deel aan de vergadering op de bestuurde computer. Klik op de pijl naast de audioknop en selecteer de volgende apparaten, zoals in dit voorbeeld:

    - **Microphone**: Microphone (6-Comet Microphone)

    - **Speaker**: EPSON PJ (HD Audio Driver for Display Audio)

    ![Microfoon en luidspreker selecteren](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/select-microphone-and-speaker.png){class="glboxshadow"}

    Hef vervolgens de demping van uw microfoon op om met de andere deelnemers te praten. U hoort hen via de luidsprekers of hoofdtelefoon van de besturende computer.

    Wilt u ook beelden van uw lokale camera met de deelnemers delen? Raadpleeg dan de [handleiding voor het doorsturen van camerabeelden](../faq/use_camera_passthrough_for_remote_meetings.md).

## Probleemoplossing {#troubleshooting}

??? note "Wat doet u als andere deelnemers u niet horen?"

    Ga op de bestuurde computer naar **Settings** -> **System** -> **Sound** en zoek onder **Input** de virtuele microfoon van de KVM, in dit voorbeeld **Comet Microphone**. Controleer of deze microfoon ook in uw vergaderapp is geselecteerd.

    ![Invoer controleren](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-input.png){class="glboxshadow"}

    - Als de virtuele microfoon van de KVM niet wordt weergegeven, controleer dan de USB-dataverbinding tussen de KVM en de bestuurde computer. Deze verbinding stuurt het microfoongeluid naar de bestuurde computer.

    - Als de virtuele microfoon van de KVM zichtbaar en geselecteerd is maar er geen geluid binnenkomt, controleer dan of de microfoon op de besturende computer en in de vergaderapp op de bestuurde computer niet is gedempt. Controleer op de besturende computer de microfoonmachtigingen van het systeem en de browser. Sluit andere apps of browsertabbladen die de microfoon mogelijk gebruiken.

??? note "Wat doet u als u andere deelnemers niet hoort?"

    Ga op de bestuurde computer naar **Settings** -> **System** -> **Sound** en zoek onder **Output** de HDMI-audio-uitgang die met de KVM is verbonden, in dit voorbeeld **EPSON PJ**. Controleer of hetzelfde apparaat in uw vergaderapp als luidspreker is geselecteerd.

    ![Uitvoer controleren](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-output.png){class="glboxshadow"}

    - Als de HDMI-audio-uitgang niet wordt weergegeven, controleer dan de HDMI-verbinding tussen de bestuurde computer en de KVM. Deze verbinding stuurt het geluid van de bestuurde computer door. Gebruikt u een HDMI-adapter, controleer dan of deze audio ondersteunt.

    - Als de HDMI-audio-uitgang zichtbaar en geselecteerd is maar u andere deelnemers nog steeds niet hoort, controleer dan of het geluid op de besturende computer, in het browsertabblad en op de luidsprekers of hoofdtelefoon niet is gedempt.

    Raadpleeg voor meer informatie [Geen geluid van het bestuurde apparaat](../faq/no_audio_from_the_controlled_device.md).

??? note "Wat doet u als het geluid wegvalt na het vernieuwen van de pagina of het opnieuw verbinden?"

    Controleer **Speaker** en **Microphone** opnieuw in de KVM-console. Het beveiligingsbeleid van de browser kan na het vernieuwen van de pagina of het opnieuw verbinden de luidsprekerweergave uitschakelen of de microfoon dempen.

    Raadpleeg voor meer informatie [Luidspreker- en microfooninstellingen blijven niet bewaard](../faq/speaker_microphone_settings_cannot_be_retained.md).

??? note "Wat doet u als de melding 'Microphone Access Denied' verschijnt?"

    Controleer het volgende op de besturende computer:

    - **Systeemmachtigingen**: Ga in Windows 11 naar **Settings** -> **Privacy & security** -> **Microphone**. Schakel **Microphone access**, **Let apps access your microphone** en **Let desktop apps access your microphone** in.

    - **Browsermachtigingen**: Geef de KVM-website toegang tot uw microfoon. Als toegang eerder is geblokkeerd, werkt u de microfoonmachtigingen van de website bij en vernieuwt u de pagina.

    - **Microfoongebruik**: Sluit andere apps of browsertabbladen die de microfoon mogelijk gebruiken.

    Schakel **Microphone** na deze controles opnieuw in de KVM-console in.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
