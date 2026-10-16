# Datenschutzwarnung beim Zugriff auf KVM per Browser

Beim Zugriff auf das GL.iNet KVM per Browser kann eine Browserwarnung angezeigt werden: **Your connection isn't private**.

![privacy error](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

Diese Warnung bedeutet, dass der Browser das vom KVM bereitgestellte SSL/TLS-Zertifikat nicht validieren kann. Beispielsweise wurde es möglicherweise nicht von einer Zertifizierungsstelle ausgestellt, der Ihr Browser vertraut, oder es stimmt nicht mit der IP-Adresse oder dem Hostnamen überein, über den Sie auf die Konsole zugreifen.

## Warum wird diese Warnung angezeigt?

Im obigen Beispiel ist **192.168.8.11** die lokale IP-Adresse des KVM, die vom vorgeschalteten Router dynamisch per DHCP zugewiesen wurde.

!!! Note

    Wenn das Gateway des Routers, mit dem Ihr GL.iNet KVM verbunden ist, "192.168.x.1" lautet (wobei x in privaten Netzwerken typischerweise 0, 1 oder 8 ist), sollte die lokale IP Ihres KVM "192.168.x.y" lauten (wobei y eine gültige Hostadresse im Subnetz ist).

Diese lokale IP-Adresse wird verwendet, um auf die GL.iNet KVM-Konsole zuzugreifen, nicht auf eine öffentliche Website.

Das KVM verwendet für den HTTPS-Zugriff per Browser ein Standard-TLS-Zertifikat. Browser prüfen Zertifikate lokaler Konsolen genauso wie die öffentlicher Websites: Das Zertifikat muss vertrauenswürdig und gültig sein und zur aufgerufenen Adresse passen.

Wenn Ihr Browser dem Standardzertifikat nicht vertraut oder dieses die eingegebene lokale IP-Adresse bzw. den Hostnamen nicht abdeckt, zeigt er eine Warnung an. Diese bedeutet nicht, dass das KVM kein Zertifikat besitzt. HTTPS kann die Verbindung weiterhin verschlüsseln, aber der Browser kann die Identität des KVM nicht überprüfen.

## Wie lässt sich die Warnung beheben?

Prüfen Sie beim lokalen Zugriff zunächst, ob die Adresse zu Ihrem KVM gehört. Klicken Sie anschließend auf **Advanced** und **Continue to "192.168.8.11"** (der genaue Wortlaut hängt vom Browser ab).

![Continue to 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

Danach werden Sie zur GL.iNet KVM-Konsole weitergeleitet.

![local access to kvm admin](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## Kann ich mein eigenes Zertifikat verwenden?

Ja. Sie können auf dem KVM Ihr eigenes SSL/TLS-Zertifikat installieren und verwenden. Führen Sie die folgenden Schritte aus.

1. Besorgen Sie ein SSL/TLS-Zertifikat, das den Hostnamen oder die IP-Adresse abdeckt, über die Sie auf das KVM zugreifen. Um Browserwarnungen zu vermeiden, muss das Zertifikat gültig sein und von einer Zertifizierungsstelle stammen, der Ihr Browser vertraut. Ein selbstsigniertes Zertifikat löst weiterhin eine Warnung aus, sofern Sie Ihr steuerndes Gerät nicht ausdrücklich so konfigurieren, dass es diesem Zertifikat vertraut.

2. Melden Sie sich an Ihrer KVM-Konsole an. Klicken Sie oben rechts auf das Schildsymbol, um zu **Security** -> **TLS Certificate** zu wechseln.

    ![custom cert 1](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert1.png){class="glboxshadow"}

    Wählen Sie im Popup-Fenster **Custom Certificate** aus und laden Sie anschließend Ihre Zertifikatsdatei und den privaten Schlüssel hoch. Diese Funktion ist seit Firmware v1.8.0 verfügbar.

    ![custom cert 2](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert2.png){class="glboxshadow"}

    Alternativ können Sie das Zertifikat und den privaten Schlüssel auf dem KVM per SSH-Terminal oder WinSCP ersetzen. Beide werden in folgendem Verzeichnis gespeichert:

    `/etc/kvmd/user/ssl`

    Ersetzen Sie sie durch Ihr neues SSL-Zertifikat und Ihren privaten Schlüssel.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
