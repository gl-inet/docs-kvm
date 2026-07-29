# Datenschutzwarnung beim Zugriff auf KVM per Browser

Beim Zugriff auf das GL.iNet KVM per Browser kann eine Browserwarnung angezeigt werden: **Your connection isn't private**.

![privacy error](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

Dies ist eine übliche Sicherheitswarnung, die Browser anzeigen, wenn sie eine Website ohne SSL/TLS-Zertifikat erkennen. HTTPS-Verbindungen verwenden Zertifikate, um die Serveridentität zu prüfen und Daten zu verschlüsseln.

## Warum wird diese Warnung angezeigt?

Im obigen Beispiel ist **192.168.8.11** die lokale IP-Adresse des KVM, die vom vorgeschalteten Router dynamisch per DHCP zugewiesen wurde.

!!! Note

    Wenn das Gateway des Routers, mit dem Ihr GL.iNet KVM verbunden ist, "192.168.x.1" lautet (wobei x in privaten Netzwerken typischerweise 0, 1 oder 8 ist), sollte die lokale IP Ihres KVM "192.168.x.y" lauten (wobei y eine gültige Hostadresse im Subnetz ist).

Diese lokale IP-Adresse wird verwendet, um auf die GL.iNet KVM-Konsole zuzugreifen, nicht auf eine öffentliche Website.

Browser unterscheiden jedoch normalerweise nicht zwischen einer lokalen Konsole und normalen öffentlichen Websites. Sie behandeln alle IP-Adressen als Websites und erwarten, dass HTTPS-Verbindungen durch SSL/TLS-Zertifikate abgesichert sind.

Eine tatsächlich sichere Website verwendet ein SSL/TLS-Zertifikat. Wenn Browser daher auf eine lokale Konsole ohne Zertifikat zugreifen, lösen sie wegen des fehlenden Zertifikats eine Sicherheitswarnung aus.

## Wie lässt sich die Warnung beheben?

Klicken Sie auf **Advanced** und **Continue to "192.168.8.11"**.

![Continue to 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

Danach werden Sie zur GL.iNet KVM-Konsole weitergeleitet.

![local access to kvm admin](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## Kann ich mein eigenes Zertifikat verwenden?

Ja. Sie können auf dem KVM Ihr eigenes SSL/TLS-Zertifikat installieren und verwenden. Führen Sie die folgenden Schritte aus.

1. Beantragen Sie ein SSL/TLS-Zertifikat oder verwenden Sie ein selbstsigniertes Zertifikat.

2. Melden Sie sich an Ihrer KVM-Konsole an. Klicken Sie oben rechts auf das Schildsymbol, um zu **Security** -> **TLS Certificate** zu wechseln.

    ![custom cert 1](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert1.png){class="glboxshadow"}

    Wählen Sie im Popup-Fenster **Custom Certificate** aus und laden Sie anschließend Ihre Zertifikatsdatei und den privaten Schlüssel hoch. Diese Funktion ist seit Firmware v1.8.0 verfügbar.

    ![custom cert 2](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert2.png){class="glboxshadow"}

    Alternativ können Sie die Konfigurationsdateien auf dem KVM per SSH-Terminal oder WinSCP bearbeiten. Das automatisch erzeugte Zertifikat und der Schlüssel werden unter folgendem Pfad gespeichert:

    `/etc/kvmd/user/ssl`

    Ersetzen Sie sie durch Ihr neues SSL-Zertifikat und Ihren privaten Schlüssel.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
