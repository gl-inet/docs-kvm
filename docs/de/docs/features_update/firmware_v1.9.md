# Firmware v1.9

Diese Version bringt neue Funktionserweiterungen, verbesserte Interaktivitaet, staerkeren Datenschutz und zuverlaessigere Netzwerkverbindungen. Alles ist darauf ausgelegt, ein umfassenderes, stabileres und sichereres Remote-KVM-Erlebnis zu bieten.

Laden Sie die neueste Firmware im [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} herunter.

## Latency Mode

Diese Firmware fuehrt den **Latency Mode** ein, der Eingabereaktionszeit und Videofluessigkeit ausbalanciert. Sie koennen den Latency Mode entweder auf Lowest Latency oder Smooth Display setzen, um die Leistung der Fernsteuerung zu optimieren.

![latency mode](https://static.gl-inet.com/docs/kvm/features_update/1.9/latency_mode.png){class="glboxshadow" width="360"}
    
- Lowest Latency: Minimiert die Eingabelatenz fuer eine direktere Reaktion von Tastatur und Maus.
- Smooth Display: Optimiert die visuelle Ausgabe, um Ruckler und ausgelassene Frames fuer eine stabile Wiedergabe zu vermeiden.

## Mausbedienung

Zur besseren Mausbedienung wurde die neue Option **Primary Button** zum Tauschen der primaeren Maustaste hinzugefuegt. Sie koennen entweder die linke oder die rechte Taste als primaeren Klick festlegen, passend zu Ihren Nutzungsgewohnheiten.

![primary button](https://static.gl-inet.com/docs/kvm/features_update/1.9/primary_button.png){class="glboxshadow" width="360"}

## Bildschirmanzeige

Sie koennen die **Screen Display**-Einstellungen des KVM ueber den Touchscreen anpassen, einschliesslich Bildschirmsperre, Hintergrundbild, Zeitformat (24 Stunden / 12 Stunden) und Datumsformat. Diese Funktion ist ausschliesslich fuer Modelle mit Touchscreen verfuegbar.

Ausserdem koennen Sie Overlay-Tools wie Tailscale und NetBird mit wenigen Fingertipps direkt ueber den Touchscreen konfigurieren. Diese Funktion war in frueheren Firmware-Versionen nicht verfuegbar.

![screen display](https://static.gl-inet.com/docs/kvm/features_update/1.9/screen_display.png){class="glboxshadow" width="360"}

## Sprache

Fruehere Firmware-Versionen unterstuetzten nur Chinesisch und Englisch. Diese Version fuegt native Unterstuetzung fuer **Japanisch** hinzu, um die Nutzbarkeit fuer japanische Anwender zu verbessern.

![language](https://static.gl-inet.com/docs/kvm/features_update/1.9/language.png){class="glboxshadow" width="360"}

## Erweiterungen

Diese Version integriert [**NetBird**](https://netbird.io/){target="_blank"}, eine Open-Source-Zero-Trust-Netzwerkplattform zum Aufbau sicherer privater Heim- und Unternehmensnetzwerke. Diese auf WireGuard® basierende Overlay-Loesung ermoeglicht sicheren Fernzugriff auf Ihr KVM von ueberall ueber virtuelle NetBird-Netzwerke.
Eine Einrichtungsanleitung finden Sie [hier](../faq/remote_access_via_netbird.md){target="_blank"}.

![netbird](https://static.gl-inet.com/docs/kvm/features_update/1.9/nerbird.png){class="glboxshadow"}

## Weitere Verbesserungen

- Beta-Firmware-Programm: Benutzer koennen am Beta-Programm teilnehmen, um Vorabfunktionen zu testen.

- Text Recognition: Dieses auf Optical Character Recognition (OCR) basierende Tool erfasst Text aus einem ausgewaehlten Bereich der Remote-Anzeige. Unterstuetzt werden Chinesisch, Englisch und ein zweisprachiger Chinesisch-Englisch-Modus. Einzelheiten finden Sie [hier](../tutorials/how_to_capture_text_from_remote_screen.md).

- Stadtbasierte Zeitzone: Legen Sie Ihre Zeitzone fest, indem Sie eine Zielstadt auswaehlen.

- Sicherheit von Anmeldesitzungen: Login-Token laufen jetzt 12 Stunden nach Beendigung der Sitzung ab; zuvor waren Token dauerhaft gueltig.

- Sicherheit der Systemprotokolle: Fuer alle Systemprotokolle wurde eine Maskierung sensibler Daten implementiert.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
