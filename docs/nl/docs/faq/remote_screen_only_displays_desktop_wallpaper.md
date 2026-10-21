# Wat moet ik doen als het externe scherm alleen de bureaubladachtergrond toont? {#what-should-i-do-if-the-remote-screen-only-displays-the-desktop-wallpaper}

Als u bij toegang tot het bestuurde apparaat via de KVM alleen de bureaubladachtergrond ziet en geen enkele handeling reageert, gebruikt uw bestuurde apparaat waarschijnlijk meerdere beeldschermen in de modus **Extend Displays**.

Om het probleem op te lossen, moet de weergavemodus van het bestuurde apparaat worden gewijzigd in **Duplicate display** (Windows) of **Mirror display** (macOS).

Kies de oplossing die bij uw besturingssysteem past.

=== "Windows"
    We nemen Windows 10 als voorbeeld. Als **Extend these displays** is ingeschakeld, volgt u de onderstaande stappen om over te schakelen naar **Duplicate display**.

    ![Beeldschermen uitbreiden](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/extend_displays.jpg){class="glboxshadow"}

    1. Ga op het bestuurde apparaat naar **Settings** -> **System** -> **Display**.

        ![Systeeminstellingen van Windows 10](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/win10_system_settings.png){class="glboxshadow"}

    2. Scrol op de pagina Display omlaag naar **Multiple displays**.

    3. Schakel over van Extend Displays naar **Duplicate display**.

        ![Beeldschermen dupliceren](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/duplicate_displays.jpg){class="glboxshadow"}

    4. Klik op **Keep changes**.

        ![Wijzigingen behouden](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/keep_changes.png){class="glboxshadow"}

    Controleer vervolgens of u het bestuurde apparaat normaal kunt openen.

=== "macOS"
    1. Klik linksboven in het scherm op het Apple-menu en selecteer **System Settings**.

    2. Scrol in de zijbalk omlaag en kies **Displays**.

        ![Systeeminstellingen van de Mac](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-system-settings.png){class="glboxshadow"}
 
    3. Klik in de indelingsweergave op het **External display**; u ziet het scherm van de MacBook en alle aangesloten monitoren.

    4. Klik op het vervolgkeuzemenu **Use as** en selecteer **Mirror mode**, meestal Mirror for Built-in Display.

        ![Beeldscherm spiegelen op de Mac](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-mirror-display.png){class="glboxshadow"}

    Na deze instelling zijn het volledige bureaublad en alle toepassingsvensters op het bestuurde apparaat op afstand toegankelijk.
    
!!! Note "Opmerking"
    Deze oplossing geldt alleen voor weergaveproblemen die worden veroorzaakt door de modus voor uitgebreide weergave. Als het probleem zich na het inschakelen van spiegelen blijft voordoen, controleer dan of op uw apparaat de lokale gebruikersaanmelding is voltooid en of het niet vastzit op het aanmeldscherm van het systeem.
      
---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
