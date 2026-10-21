# Vad gör jag om fjärrskärmen bara visar skrivbordsbakgrunden? {#what-should-i-do-if-the-remote-screen-only-displays-the-desktop-wallpaper}

Om du bara ser skrivbordsbakgrunden och inga åtgärder ger respons när du kommer åt den styrda enheten via KVM-enheten använder den styrda enheten troligen flera skärmar i läget **Extend Displays** (utökade skärmar).

Lös problemet genom att växla den styrda enhetens visningsläge till **Duplicate display** (Windows) eller **Mirror display** (macOS).

Välj lösningen för ditt operativsystem.

=== "Windows"
    Vi tar Windows 10 som exempel. Om **Extend these displays** är aktiverat följer du stegen nedan för att växla till **Duplicate display**.

    ![Utökade skärmar](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/extend_displays.jpg){class="glboxshadow"}

    1. Gå till **Settings** -> **System** -> **Display** på den styrda enheten.

        ![Systeminställningar i Windows 10](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/win10_system_settings.png){class="glboxshadow"}

    2. Rulla nedåt på sidan Display till **Multiple displays**.

    3. Växla från Extend Displays till **Duplicate display**.

        ![Duplicerade skärmar](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/duplicate_displays.jpg){class="glboxshadow"}

    4. Klicka på **Keep changes**.

        ![Behåll ändringarna](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/keep_changes.png){class="glboxshadow"}

    Kontrollera sedan om du kan komma åt den styrda enheten som vanligt.

=== "macOS"
    1. Klicka på Apple-menyn i skärmens övre vänstra hörn och välj **System Settings**.

    2. Rulla nedåt i sidofältet och välj **Displays**.

        ![Systeminställningar i macOS](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-system-settings.png){class="glboxshadow"}

    3. Klicka på **External display** i layoutvyn. Du ser då MacBook-skärmen och alla anslutna skärmar.

    4. Klicka på listrutan **Use as** och välj **Mirror mode**, vanligtvis Mirror for Built-in Display.

        ![Spegla skärmen i macOS](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-mirror-display.png){class="glboxshadow"}

    Efter konfigurationen kan du komma åt hela skrivbordet och alla programfönster på den styrda enheten på distans.

!!! Note "Obs!"
    Lösningen gäller bara visningsproblem som orsakas av läget för utökade skärmar. Om problemet kvarstår efter att du har aktiverat spegling ska du kontrollera att den lokala användarinloggningen på enheten är slutförd och att enheten inte har fastnat på systemets inloggningsskärm.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
