# Was tun, wenn Maus und Tastatur nicht gesteuert werden können

Wenn Sie Maus und Tastatur auf dem gesteuerten Gerät über KVM nicht steuern können, obwohl alle Kabel korrekt angeschlossen sind, helfen möglicherweise die folgenden Schritte.

1. Prüfen Sie die Verkabelung.

    Beispiel Comet (GL-RM1): Das Gerät hat zwei USB Type-C-Anschlüsse:

    - Der Anschluss an der Seite ist mit "5V 2A" gekennzeichnet und dient der Stromversorgung (Verbindung mit einem Netzteil).
    - Der andere Anschluss auf der Rückseite trägt Symbole für Maus und Tastatur. Er wird mit dem USB-Anschluss des gesteuerten Geräts verbunden, um Tastatur- und Maussignale zu übertragen.

    Wenn diese beiden Anschlüsse verwechselt werden, startet das KVM-Gerät nicht und Maus sowie Tastatur reagieren nicht.

    Bitte prüfen Sie, ob diese beiden Type-C-Schnittstellen korrekt verbunden sind.

    ![gl-rm1 ports](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/gl-rm1-ports.png){class="glboxshadow gl-80-desktop"}

2. Prüfen Sie das USB-Kabel.

    Verwenden Sie das mitgelieferte USB-Kabel. Stellen Sie sicher, dass es den USB-Anschluss des gesteuerten Geräts mit dem USB-Anschluss des KVM verbindet und Datenübertragung unterstützt.

    Nur Kabel mit Datenübertragung ermöglichen die Tastatur- und Maussteuerung des entfernten Geräts.

    Schließen Sie das USB-Kabel erneut an und starten Sie das gesteuerte Gerät neu.

3. Wechseln Sie den Mausmodus in den relativen Modus.

    Melden Sie sich an Ihrem KVM an, navigieren Sie zu Settings -> Mouse Mode, stellen Sie den Modus auf Relative um und prüfen Sie, ob das Problem dadurch behoben wird.

    ![mouse mode](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/mouse_mode.jpg){class="glboxshadow"}

4. Deaktivieren Sie die virtuellen Medien.

    Melden Sie sich an Ihrem KVM an, navigieren Sie zu Virtual Media, klicken Sie auf das Drei-Punkte-Symbol und deaktivieren Sie die Funktion.

    ![disable virtual media](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/disable_virtual_media.png){class="glboxshadow" width="422"}

    Wenn virtuelle Medien aktiviert sind, kann KVM ein am gesteuerten Gerät angeschlossenes USB-Speicherlaufwerk simulieren. Einige Geräte deaktivieren jedoch alle USB-Eingaben, wenn sie ein unbekanntes USB-Speicherlaufwerk erkennen. Dadurch können Maus und Tastatur nicht mehr reagieren.

5. Ändern Sie die Geräteidentität.

    Melden Sie sich an Ihrem KVM an, navigieren Sie zu Settings -> System -> Device Identity und ändern Sie die Identität, unter der Ihr KVM vom gesteuerten Gerät erkannt wird.

    ![change device identity](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/change_device_identity.png){class="glboxshadow"}

6. Aktualisieren Sie die Firmware des KVM auf die neueste Version. [KVM Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"}

7. Prüfen Sie im Geräte-Manager des gesteuerten Computers, ob Treiber fehlerhaft sind.

8. Prüfen Sie, ob das gesteuerte Gerät durch IT-Sicherheitssoftware blockiert wird.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
