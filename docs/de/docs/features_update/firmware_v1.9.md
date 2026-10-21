# Firmware v1.9 {#firmware-v19}

Diese Version bringt neue Funktionserweiterungen, verbesserte Interaktivität, stärkeren Datenschutz und zuverlässigere Netzwerkverbindungen. Alles ist darauf ausgelegt, ein umfassenderes, stabileres und sichereres Remote-KVM-Erlebnis zu bieten.

Laden Sie die neueste Firmware im [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} herunter.

## Latency Mode {#latency-mode}

Diese Firmware führt den **Latency Mode** ein, der Eingabereaktionszeit und Videoflüssigkeit ausbalanciert. Sie können den Latency Mode entweder auf Lowest Latency oder Smooth Display setzen, um die Leistung der Fernsteuerung zu optimieren.

![latency mode](https://static.gl-inet.com/docs/kvm/features_update/1.9/latency_mode.png){class="glboxshadow" width="360"}
    
- Lowest Latency: Minimiert die Eingabelatenz für eine direktere Reaktion von Tastatur und Maus.
- Smooth Display: Optimiert die visuelle Ausgabe, um Ruckler und ausgelassene Frames für eine stabile Wiedergabe zu vermeiden.

## Mausbedienung {#mouse-usability}

Zur besseren Mausbedienung wurde die neue Option **Primary Button** zum Tauschen der primären Maustaste hinzugefügt. Sie können entweder die linke oder die rechte Taste als primären Klick festlegen, passend zu Ihren Nutzungsgewohnheiten.

![primary button](https://static.gl-inet.com/docs/kvm/features_update/1.9/primary_button.png){class="glboxshadow" width="360"}

## Bildschirmanzeige {#screen-display}

Sie können die **Screen Display**-Einstellungen des KVM über den Touchscreen anpassen, einschließlich Bildschirmsperre, Hintergrundbild, Zeitformat (24 Stunden / 12 Stunden) und Datumsformat. Diese Funktion ist ausschließlich für Modelle mit Touchscreen verfügbar.

Außerdem können Sie Overlay-Tools wie Tailscale und NetBird mit wenigen Fingertipps direkt über den Touchscreen konfigurieren. Diese Funktion war in früheren Firmware-Versionen nicht verfügbar.

![screen display](https://static.gl-inet.com/docs/kvm/features_update/1.9/screen_display.png){class="glboxshadow" width="360"}

## Sprache {#language}

Frühere Firmware-Versionen unterstützten nur Chinesisch und Englisch. Diese Version fügt native Unterstützung für **Japanisch** hinzu, um die Nutzbarkeit für japanische Anwender zu verbessern.

![language](https://static.gl-inet.com/docs/kvm/features_update/1.9/language.png){class="glboxshadow" width="360"}

## Erweiterungen {#extensions}

Diese Version integriert [**NetBird**](https://netbird.io/){target="_blank"}, eine Open-Source-Zero-Trust-Netzwerkplattform zum Aufbau sicherer privater Heim- und Unternehmensnetzwerke. Diese auf WireGuard® basierende Overlay-Lösung ermöglicht sicheren Fernzugriff auf Ihr KVM von überall über virtuelle NetBird-Netzwerke.
Eine Einrichtungsanleitung finden Sie [hier](../faq/remote_access_via_netbird.md){target="_blank"}.

![netbird](https://static.gl-inet.com/docs/kvm/features_update/1.9/netbird.png){class="glboxshadow"}

## Weitere Verbesserungen {#other-enhancements}

- Beta-Firmware-Programm: Benutzer können am Beta-Programm teilnehmen, um Vorabfunktionen zu testen.

- Text Recognition: Dieses auf Optical Character Recognition (OCR) basierende Tool erfasst Text aus einem ausgewählten Bereich der Remote-Anzeige. Unterstützt werden Chinesisch, Englisch und ein zweisprachiger Chinesisch-Englisch-Modus. Einzelheiten finden Sie [hier](../tutorials/how_to_capture_text_from_remote_screen.md).

- Stadtbasierte Zeitzone: Legen Sie Ihre Zeitzone fest, indem Sie eine Zielstadt auswählen.

- Sicherheit von Anmeldesitzungen: Login-Token laufen jetzt 12 Stunden nach Beendigung der Sitzung ab; zuvor waren Token dauerhaft gültig.

- Sicherheit der Systemprotokolle: Für alle Systemprotokolle wurde eine Maskierung sensibler Daten implementiert.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
