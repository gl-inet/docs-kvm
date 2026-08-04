# Was tun, wenn der Remote-Bildschirm nur das Desktop-Hintergrundbild anzeigt

Wenn Sie beim Zugriff auf das gesteuerte Gerät über KVM nur das Desktop-Hintergrundbild sehen und keine Bedienung reagiert, verwendet Ihr gesteuertes Gerät wahrscheinlich mehrere Monitore im Modus **Extend Displays**.

Um das Problem zu beheben, muss der Anzeigemodus des gesteuerten Geräts auf **Duplicate display** (Windows) oder **Mirror display** (macOS) umgestellt werden.

Wählen Sie die passende Lösung für Ihr Betriebssystem aus.

=== "Windows"
    Beispiel mit Windows 10. Wenn **Extend these displays** aktiviert ist, folgen Sie den Schritten unten, um zu **Duplicate display** zu wechseln.

    ![extend display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/extend_displays.jpg){class="glboxshadow"}

    1. Gehen Sie auf dem gesteuerten Gerät zu **Settings** -> **System** -> **Display**.

        ![win10 system settings](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/win10_system_settings.png){class="glboxshadow"}

    2. Scrollen Sie auf der Seite Display nach unten zu **Multiple displays**.

    3. Wechseln Sie von Extend Displays zu **Duplicate display**.

        ![duplicate display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/duplicate_displays.jpg){class="glboxshadow"}

    4. Klicken Sie auf **Keep changes**.

        ![keep changes](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/keep_changes.png){class="glboxshadow"}

    Prüfen Sie anschließend, ob Sie normal auf das gesteuerte Gerät zugreifen können.

=== "macos"
    1. Klicken Sie oben links auf dem Bildschirm auf das Apple-Menü und wählen Sie **System Settings**.

    2. Scrollen Sie in der Seitenleiste nach unten und wählen Sie **Displays**.

        ![mac system settings](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-system-settings.png){class="glboxshadow"}

    3. Klicken Sie in der Layout-Ansicht auf **External display**. Dort sehen Sie den MacBook-Bildschirm und alle verbundenen Monitore.

    4. Klicken Sie auf das Dropdown-Menü **Use as** und wählen Sie **Mirror mode**, in der Regel Mirror for Built-in Display.

        ![mac mirror display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-mirror-display.png){class="glboxshadow"}

    Nach der Einrichtung sind der vollständige Desktop und alle Anwendungsfenster auf dem gesteuerten Gerät per Fernzugriff erreichbar.

!!! Note
    Diese Lösung gilt nur für Anzeigeprobleme, die durch den Modus Extend display verursacht werden. Wenn das Problem nach dem Aktivieren der Spiegelung weiterhin besteht, stellen Sie sicher, dass auf Ihrem Gerät die lokale Benutzeranmeldung abgeschlossen ist und es nicht am System-Anmeldebildschirm hängt.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
