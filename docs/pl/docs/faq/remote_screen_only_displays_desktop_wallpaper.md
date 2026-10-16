# Co zrobić, jeśli na ekranie zdalnym widać tylko tapetę pulpitu {#what-should-i-do-if-the-remote-screen-only-displays-the-desktop-wallpaper}

Jeśli podczas dostępu do urządzenia docelowego przez KVM widać jedynie tapetę pulpitu i nie można wykonać żadnych operacji, prawdopodobnie urządzenie korzysta z wielu monitorów w trybie **Extend Displays**.

Aby rozwiązać problem, zmień tryb wyświetlania urządzenia docelowego na **Duplicate display** (Windows) lub **Mirror display** (macOS).

Wybierz rozwiązanie odpowiednie dla swojego systemu operacyjnego.

=== "Windows"
    Poniższy przykład dotyczy Windows 10. Jeśli włączono **Extend these displays**, wykonaj poniższe czynności, aby przełączyć na **Duplicate display**.

    ![Rozszerzony pulpit](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/extend_displays.jpg){class="glboxshadow"}

    1. Na urządzeniu docelowym przejdź do **Settings** -> **System** -> **Display**.

        ![Ustawienia systemu Windows 10](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/win10_system_settings.png){class="glboxshadow"}

    2. Na stronie Display przewiń w dół do sekcji **Multiple displays**.

    3. Zmień Extend Displays na **Duplicate display**.

        ![Powielanie ekranu](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/duplicate_displays.jpg){class="glboxshadow"}

    4. Kliknij **Keep changes**.

        ![Zachowanie zmian](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/keep_changes.png){class="glboxshadow"}

    Następnie sprawdź, czy możesz normalnie korzystać z urządzenia docelowego.

=== "macos"
    1. Kliknij menu Apple w lewym górnym rogu ekranu i wybierz **System Settings**.

    2. Przewiń pasek boczny w dół i wybierz **Displays**.

        ![Ustawienia systemowe macOS](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-system-settings.png){class="glboxshadow"}

    3. W widoku układu kliknij **External display**; zobaczysz ekran MacBooka i wszystkie podłączone monitory.

    4. Rozwiń menu **Use as** i wybierz **Mirror mode**, zwykle Mirror for Built-in Display.

        ![Klonowanie ekranu w macOS](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-mirror-display.png){class="glboxshadow"}

    Po skonfigurowaniu pełny pulpit i wszystkie okna aplikacji urządzenia docelowego będą dostępne zdalnie.

!!! Note
    To rozwiązanie dotyczy tylko problemów z obrazem spowodowanych trybem rozszerzonego pulpitu. Jeśli po włączeniu powielania problem nadal występuje, upewnij się, że użytkownik zalogował się lokalnie na urządzeniu i że nie pozostaje ono na ekranie logowania do systemu.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
