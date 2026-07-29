# Was kann ich tun, wenn sich mein KVM nicht einschaltet

Wenn Ihr KVM-Gerät trotz angeschlossenem Stromkabel nicht startet, verwenden Sie die folgenden Methoden zur Fehlerbehebung.

1. Stellen Sie sicher, dass das Stromkabel am richtigen USB Type-C-Port angeschlossen ist.

    Nehmen wir Comet (GL-RM1) als Beispiel. Es hat zwei USB Type-C-Ports: einen für die Stromversorgung (angeschlossen an ein Netzteil) und einen für die Signalübertragung (per USB-Kabel mit dem gesteuerten Gerät verbunden).

    Wenn die beiden Ports vertauscht werden, wird das KVM nicht mit Strom versorgt und Maus und Tastatur reagieren nicht auf Eingaben.

    Schließen Sie das Stromkabel an den USB Type-C-Port neben dem Ethernet-Port an.

    ![plug in power cable](https://static.gl-inet.com/docs/kvm/faq/power_cable_connected_but_device_unpowered/plug_in_power_cable.jpg){class="glboxshadow"}

2. Verwenden Sie zum Testen ein gängiges 5V-2A-Netzteil und prüfen Sie, ob die LED aufleuchtet.

    Vermeiden Sie Netzteile mit PD-Protokoll.

    Eine dauerhaft blau leuchtende LED zeigt an, dass das Gerät startet.

3. Halten Sie die Reset-Taste länger als 8 Sekunden gedrückt, um die Werkseinstellungen wiederherzustellen.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
