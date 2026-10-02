# Firmware v1.10

Diese Version führt natives WebRTC, Echtzeit-Datenüberwachung, eine zentrale Verwaltung von USB-Geräten und ein neues Settings Center ein. Zudem verbessert sie die Startleistung, die Sicherheit und die Mikrofonstabilität für ein flüssigeres und zuverlässigeres Remote-KVM-Erlebnis.

Laden Sie die neueste Firmware im [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} herunter.

## WebRTC (Native) Mode
Diese Firmware führt den **WebRTC (Native) Mode** ein. Er nutzt die Google WebRTC Library, um die Streaming-Leistung zu verbessern und eine flüssigere Fernsteuerung in Echtzeit zu ermöglichen.

![webrtc mode](https://static.gl-inet.com/docs/kvm/features_update/1.10/webrtc_native_mode.png){class="glboxshadow" width=400}

## Connection Stats

**Connection Stats** zeigt Verbindungsinformationen und Verlaufsdiagramme in Echtzeit an, darunter Netzwerklatenz, Jitter, Paketverlustrate, Bitrate, Bildrate und Wiedergabeverzögerung.

- Klicken Sie auf das Listensymbol, um Verbindungsdaten in Echtzeit und den Gerätestatus anzuzeigen.

    ![Connection Stats 1](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_1.png){class="glboxshadow"}

- Klicken Sie auf das Diagrammsymbol, um Verlaufsdiagramme für Netzwerklatenz, Jitter und Paketverlustrate anzuzeigen.

    ![Connection Stats 2](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_2.png){class="glboxshadow"}

## Settings Center

Diese Version ergänzt ein neues **Settings Center**, das Einstellungen für USB-Geräte, persönliche Präferenzen, Netzwerk, Sicherheit, Cloud und System zentral zusammenfasst. Bestehende Optionen wie die Hostnamenkonfiguration, die Cloud-Verwaltung und Firmware-Upgrades sind nun leichter an einem zentralen Ort zugänglich.

### USB Devices

Unter **USB Devices** werden emulierte USB-Geräte zentral verwaltet. Auf dieser Seite können Sie virtuelle Peripheriegeräte aktivieren oder deaktivieren, um die Kompatibilität mit dem gesteuerten Gerät zu verbessern.

![usb devices](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_usb_devices.png){class="glboxshadow"}

- **USB Emulated Devices**: Aktivieren oder deaktivieren Sie emulierte USB-Geräte, darunter Maus, Tastatur, Mikrofon, Kamera und virtuelle Medien. Einige Geräte können nicht gleichzeitig aktiviert werden. Die Verfügbarkeit wird automatisch aktualisiert.

- **Device Identity**: Passen Sie die Identität des KVM an, die das gesteuerte Gerät erkennt. Beachten Sie, dass EDID und Geräteidentifikation synchron bleiben. Wenn Sie einen der beiden Werte ändern, wird der andere automatisch aktualisiert, um eine korrekte Geräteerkennung sicherzustellen.

### Preferences

Unter **Preferences** können Sie Layout-Präferenzen, Systemeinstellungen und Einstellungen für den Gerätebildschirm verwalten.

![preferences](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences**: Konfigurieren Sie die Symbolleiste im Vollbildmodus und die Statusleiste im Fenstermodus.

- **System Settings**: Legen Sie den Titel des Browser-Tabs, die Sprache der Benutzeroberfläche, den Farbmodus und die Zeitzone fest.

- **Device Screen**: Zeigen Sie eine Vorschau des integrierten Gerätebildschirms an und konfigurieren Sie ihn, einschließlich Bildschirmsperre, Zeitformat, Datumsformat und Hintergrundbild.

    **Hinweis**: Diese Funktion ist nur bei Modellen mit integriertem Display verfügbar.

### Network

Sie können die Netzwerkeinstellungen des Geräts anzeigen und verwalten, einschließlich Hostname, Ethernet-Verbindung und Informationen zum drahtlosen Netzwerk.

![network](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_network.png){class="glboxshadow"}

- **Hostname**: Ändern Sie den Hostnamen des Geräts direkt über die Konsole. Diese Funktion wurde mit Firmware v1.7.0 eingeführt.

- **Ethernet Settings**: Zeigen Sie die Ethernet-Verbindung an und konfigurieren Sie sie. Sie können DHCP verwenden, um die Netzwerkeinstellungen automatisch zu beziehen, oder **Static** auswählen, um IP-Adresse, Netzmaske, Gateway und weitere erforderliche Parameter manuell einzugeben.

- **Wireless**: IP-Adresse, Gateway und MAC-Adresse werden angezeigt, sobald das Gerät mit einem WLAN verbunden ist.

    **Hinweis**: Die Funktion Wireless ist nur bei unterstützten Modellen verfügbar.

### Security

Unter **Security** können Sie das Administratorpasswort ändern, die Zwei-Faktor-Authentifizierung aktivieren und das TLS-Zertifikat anpassen.

![security](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_security.png){class="glboxshadow"}

- **Access Password**: Verwalten Sie das Administratorpasswort oder aktivieren Sie die Zwei-Faktor-Authentifizierung (2FA), um den Gerätezugriff abzusichern.

- **TLS Certificate**: Verwenden Sie das Standardzertifikat oder laden Sie ein benutzerdefiniertes Zertifikat und einen privaten Schlüssel für den Browserzugriff hoch.

### Cloud

Geräte können per URL oder Code an Cloud-Dienste gebunden werden, um Fernzugriff und Verwaltung zu ermöglichen. Sie können außerdem die mobile App herunterladen, die Verbindung verwalten oder bei Bedarf die Bindung des Geräts aufheben.

![cloud](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_cloud.png){class="glboxshadow"}

### System

Unter **System** finden Sie Optionen zur Systemverwaltung, zum Firmware-Upgrade und zum Support.

![system](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_system.png){class="glboxshadow"}

- **System**: Starten Sie das Gerät neu oder setzen Sie es auf die Werkseinstellungen zurück.

- **Upgrade**: Aktivieren Sie Beta Center, um Beta-Firmware-Updates zu erhalten, oder verwenden Sie **Local Upgrade**, um Firmware aus einer lokalen Datei zu installieren.

- **Help & Support**: Exportieren Sie Geräteprotokolle zur Fehlerbehebung und greifen Sie auf Benutzerhandbücher, FAQs und weitere Supportdokumente zu.

## Weitere Verbesserungen

- **Startup Performance**: Die Startgeschwindigkeit des Geräts wurde verbessert.

- **Password Policy**: Die Passwortrichtlinie wurde zur Verbesserung der Sicherheit verschärft: mindestens 10 Zeichen aus mindestens zwei Zeichentypen.

- **Caps Lock Indicator**: Eine Anzeige für den Status der Feststelltaste des gesteuerten Geräts wurde hinzugefügt.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
