# Verbindung beim Fernzugriff über die GLKVM App fehlgeschlagen

Beim Fernzugriff über die GLKVM App kann es vorkommen, dass das KVM-Gerät in der GLKVM App als Online angezeigt wird, nach dem Anklicken jedoch bei "Connecting" hängen bleibt.

![device online](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/device_online.png){class="glboxshadow"}

![connecting](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connecting.png){class="glboxshadow"}

Anleitung zur Fehlerbehebung:

1. Stellen Sie eine stabile Netzwerkverbindung sicher.

    Stellen Sie sicher, dass das KVM mit einem stabilen Internetzugang verbunden ist. Eine dauerhaft weiß leuchtende LED zeigt eine normale Netzwerkverbindung an.

2. Prüfen Sie die Firewall-Regeln im Netzwerk.

    Deaktivieren Sie die lokale Firewall vorübergehend oder fügen Sie GL.iNet-bezogene Domains (z. B. glkvm.com) zur Firewall-Zulassungsliste hinzu. Versuchen Sie die Verbindung anschließend erneut.

    Unten finden Sie als Referenz die Schritte zum Anpassen der Firewall-Regeln bei Sky Network.

    ??? note "Sky Network (e.g., Sky Max Hub)"

        Der Sicherheitsmechanismus von Sky Network kann den Domainnamen `glkvm.com` als verdächtige Website erkennen und den Zugriff blockieren. Sie können die Einschränkung über die Sky App aufheben.<br>

        1. Öffnen Sie die MySky App, navigieren Sie zu **Broadband** -> **Advanced Security** und prüfen Sie, ob GL.iNet-bezogene Domains eingeschränkt sind.

            ![mysky-1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-1.png){class="glboxshadow"}

        2. Wenn Sie feststellen, dass die Domain blockiert ist, klicken Sie auf den Pfeil nach unten, um die Details anzuzeigen, und wählen Sie anschließend **Allow Access**, um die Sperre aufzuheben.

            ![mysky-2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-2.png){class="glboxshadow" width="300"}

3. Deaktivieren Sie VPN/Proxy auf dem steuernden Gerät.

    Stellen Sie sicher, dass auf dem Gerät, auf dem die GLKVM App ausgeführt wird, kein VPN- oder Proxy-Dienst aktiviert ist, da diese die Verbindung beeinträchtigen können.

4. Starten Sie das KVM nach Möglichkeit neu.

    Führen Sie nach Möglichkeit einen Hardware-Neustart des KVM-Geräts durch, um vorübergehende Netzwerk- oder Softwareprobleme zu beheben.

    Wenn Sie sich nicht in der Nähe des KVM-Geräts befinden, können Sie es über die GLKVM App remote neu starten:

    1. Klicken Sie in der Geräteliste oben rechts bei Ihrem Gerät auf **Manage**.

        ![app reboot 1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_1.png){class="glboxshadow"}

    2. Klicken Sie auf **More** und wählen Sie **Reboot**.

        ![app reboot 2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_2.png){class="glboxshadow"}

Zusätzliche technische Hinweise:

1. Stellen Sie sicher, dass die DNS-Auflösung für die Domains funktioniert.

2. Vergewissern Sie sich, dass ausgehender Datenverkehr über die Standardports für KVM/Fernzugriff nicht blockiert wird.

3. Wenden Sie sich in Unternehmensnetzwerken an die IT-Administratoren, um mögliche Richtlinien zur Datenverkehrsfilterung zu prüfen.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
