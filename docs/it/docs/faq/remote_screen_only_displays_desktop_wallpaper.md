# Cosa fare se lo schermo remoto mostra solo lo sfondo del desktop {#what-should-i-do-if-the-remote-screen-only-displays-the-desktop-wallpaper}

Se, durante l'accesso al dispositivo controllato tramite KVM, vedi solo lo sfondo del desktop e nessuna operazione produce una risposta, probabilmente il dispositivo controllato usa più monitor configurati in modalità **Extend Displays**.

Per risolvere il problema, imposta la modalità di visualizzazione del dispositivo controllato su **Duplicate display** in Windows o **Mirror display** in macOS.

Seleziona la soluzione corrispondente al tuo sistema operativo.

=== "Windows"
    Prendiamo come esempio Windows 10. Se è attiva l'opzione **Extend these displays**, segui i passaggi indicati di seguito per passare a **Duplicate display**.

    ![extend display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/extend_displays.jpg){class="glboxshadow"}

    1. Sul dispositivo controllato, vai su **Settings** -> **System** -> **Display**.

        ![win10 system settings](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/win10_system_settings.png){class="glboxshadow"}

    2. Nella pagina Display, scorri verso il basso fino a **Multiple displays**.

    3. Passa da Extend Displays a **Duplicate display**.

        ![duplicate display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/duplicate_displays.jpg){class="glboxshadow"}

    4. Fai clic su **Keep changes**.

        ![keep changes](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/keep_changes.png){class="glboxshadow"}

    Verifica quindi se riesci ad accedere normalmente al dispositivo controllato.

=== "macos"
    1. Fai clic sul menu Apple nell'angolo in alto a sinistra dello schermo e seleziona **System Settings**.

    2. Scorri la barra laterale e scegli **Displays**.

        ![mac system settings](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-system-settings.png){class="glboxshadow"}

    3. Nella vista della disposizione degli schermi, fai clic su **External display**; vedrai lo schermo del MacBook e gli eventuali monitor collegati.

    4. Fai clic sul menu a discesa **Use as** e seleziona **Mirror mode**, solitamente Mirror for Built-in Display.

        ![mac mirror display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-mirror-display.png){class="glboxshadow"}

    Dopo la configurazione, potrai accedere da remoto all'intero desktop e a tutte le finestre delle applicazioni sul dispositivo controllato.

!!! Note "Nota"
    Questa soluzione si applica solo ai problemi di visualizzazione causati dalla modalità schermo esteso. Se il problema persiste dopo aver attivato la duplicazione, assicurati che il dispositivo abbia completato l'accesso dell'utente locale e non sia fermo alla schermata di accesso del sistema.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
