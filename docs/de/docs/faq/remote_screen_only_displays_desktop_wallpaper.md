# Was tun, wenn der Remote-Bildschirm nur das Desktop-Hintergrundbild anzeigt

Wenn Sie beim Zugriff auf das gesteuerte Gerät über KVM nur das Desktop-Hintergrundbild sehen und keine Bedienung reagiert, verwendet Ihr gesteuertes Gerät wahrscheinlich mehrere Monitore im Modus **Extend Displays**.

![extend display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/extend_displays.jpg){class="glboxshadow"}

Um das Problem zu beheben, schalten Sie den Anzeigemodus des gesteuerten Geräts auf **Duplicate display** um.

Beispiel mit Windows 10.

Gehen Sie auf dem gesteuerten Gerät zu **Settings** -> **System** -> **Display**.

![win10 system settings](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/win10_system_settings.png){class="glboxshadow"}

Scrollen Sie auf der Seite Display nach unten zu **Multiple displays**.

Wechseln Sie von Extend Displays zu **Duplicate display**.

![duplicate display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/duplicate_displays.jpg){class="glboxshadow"}

Klicken Sie auf **Keep changes**.

![keep changes](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/keep_changes.png){class="glboxshadow"}

Prüfen Sie anschließend, ob Sie normal auf das gesteuerte Gerät zugreifen können.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
