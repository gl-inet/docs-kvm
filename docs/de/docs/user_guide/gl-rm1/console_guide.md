# Comet (GL-RM1) V1/V2 Konsolenhandbuch

## Settings

Navigieren Sie in der Konsole zu **Settings**. Die Einstellungsseite umfasst vier Bereiche:

- [Video](#video)
- [Remote Device Settings](#remote-device-settings)
- [System](#system)
- [Network](#network)

### Quick Search

Sie können die gewünschten Einstellungen schnell finden, indem Sie oben auf der Seite **Settings** Schlüsselwörter eingeben.

![quick search](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/quick-search.png){class="glboxshadow"}

### Video

Sie können die Videoeinstellungen in der Konsole anpassen, z. B. Anzeigemodus, Videoqualität, Videoübertragung, Bildschirmausrichtung und EDID.

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/settings-video.png){class="glboxshadow"}

- **Mode**: Wechseln Sie je nach Bedarf zwischen Smart mode und Normal mode. Smart mode hilft, den Bandbreitenverbrauch zu reduzieren, insbesondere bei schwachen Netzwerken.

- **Latency Mode**: Sie können für das Gerät zwischen Lowest Latency und Smooth Display wählen. Diese Funktion wurde mit Firmware v1.9.0 eingeführt.

    !!! note "Worin unterscheiden sich Lowest Latency und Smooth Display?"

        - **Lowest Latency**: Minimiert die Eingabelatenz, um eine direktere Reaktion von Tastatur und Maus zu ermöglichen.

        - **Smooth Display**: Optimiert die visuelle Leistung, um Ruckeln und Frameverluste zu vermeiden und eine gleichmäßige Wiedergabe zu ermöglichen.

- **Quality**: Passen Sie die Videoqualität entsprechend Ihrer Netzwerkumgebung und den Anforderungen an die Auflösung auf Auto/Low/Medium/High/Ultra-high/Lossless an.

- **Transfer**: Wechseln Sie die Videoübertragungsmethode je nach Bedarf zwischen WebRTC, WebRTC (FEC) und Direct. Beachten Sie, dass Direct keine Tonübertragung bietet.

    !!! note "Worin unterscheiden sich WebRTC, WebRTC (FEC) und Direct?"

        - **WebRTC**: Bietet ein ausgewogenes Verhältnis zwischen flüssigem Video und stabilem Audio für die Echtzeit-Fernsteuerung.

        - **WebRTC (FEC)**: Fügt Forward Error Correction hinzu, um die Verbindungsstabilität bei schlechten oder instabilen Netzwerkbedingungen zu verbessern. Bei Auswahl dieser Option werden verlorene Datenpakete automatisch durch die Übertragung einer kleinen Menge redundanter Daten repariert, wodurch Bildschirmflackern und Verzögerungen reduziert werden.

        - **Direct**: Bietet die geringste Latenz und verlustfreie Videoqualität, unterstützt jedoch keine Audioübertragung.

- **Orientation**: Stellen Sie den Drehwinkel der Konsole auf 0°/90°/180°/270° ein.

- **EDID**: Kurz für Extended Display Identification Data. Diese Funktion wählt automatisch die optimalen Anzeigeparameter aus.

    Die Standardeinstellung ist für die meisten Szenarien geeignet und muss in der Regel nicht geändert werden. Details finden Sie [hier](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. Wenn der Bildschirm nach der EDID-Anpassung nicht aktualisiert wird, starten Sie das gesteuerte Gerät neu.

- **View**: Diese Einstellung bestimmt die Bildschirmskalierung beim Ändern der Größe des Browserfensters. Verfügbare Optionen: Adaptive, Best Picture Quality, Original Pixel. Diese Funktion wurde mit Firmware v1.8.0 eingeführt.

### Remote Device Settings

Sie können die relevanten Einstellungen des gesteuerten Geräts anpassen.

![settings-remote device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/settings-remote-device.png){class="glboxshadow"}

- **Speaker**: Steuert die Audioausgabe des gesteuerten Geräts (z. B. Systemtöne, Videoaudio).

- **Microphone**: Überträgt lokales Audio (z. B. Ihre Stimme) vom steuernden Gerät an die Gegenstelle. Es unterstützt eine Ein-Klick-Stummschaltung sowie eine Shortcut-Funktion durch langes Drücken zum Aktivieren des Mikrofons (d. h. Press To Speak).

    ![mic settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/mic-settings.png){class="glboxshadow"}

    ![press to speak](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/press-to-speak.png){class="glboxshadow"}

- **Keyboard**: Schalten Sie die Tastatur des gesteuerten Geräts ein oder aus.

- **Bad Link Mode**: Bedeutet, dass Tasten sofort losgelassen werden. Jeder Tastendruck wird als einzelne schnelle Drücken-und-Loslassen-Aktion gesendet, wodurch während der Fernsteuerung hängende Tasten oder unbeabsichtigte wiederholte Eingaben verhindert werden.

- **Show Virtual Keyboard**: Zeigen Sie die virtuelle Tastatur in der Konsole an und verwenden Sie sie.

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/show-virtual-keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: Diese Funktion vertauscht die Tasten Cmd und Ctrl, um die Tastaturkompatibilität zwischen verschiedenen Betriebssystemen sicherzustellen.

- **Mouse**: Schalten Sie die Maus des gesteuerten Geräts ein oder aus.

- **Show Local Cursor**: Zeigt die Maus des steuernden Geräts auf dem Bildschirm an.

- **Mouse Jiggle**: Die Funktion Mouse Jiggler simuliert dezente, periodische Mausbewegungen, um zu verhindern, dass der Computer (d. h. das gesteuerte Gerät) aufgrund längerer Inaktivität in den Ruhezustand wechselt, beispielsweise während Remote-Meetings oder bei der Serververwaltung.

- **Scroll Rate**: Bezeichnet die Geschwindigkeit, mit der das Mausrad scrollt, bzw. die Anzahl der Zeilen/Einheiten pro Mausradbewegung. Dies beeinflusst, wie schnell sich Inhalte auf der Gegenstelle bewegen.

- **Scroll Direction**: Legt fest, ob das Scrollen des Mausrads nach oben/unten Inhalte auf dem Remote-Bildschirm in dieselbe Richtung (natürliches Scrollen) oder in die entgegengesetzte Richtung (traditionelles Scrollen) bewegt.

    Es stehen vier Richtungsmodi zur Verfügung: Standard, Vertical Invert, Horizontal Invert und Both Invert.

- **Mouse Mode**: Ermöglicht das Umschalten zwischen Absolute Mode und Relative Mode, um in verschiedenen Fernsteuerungsszenarien eine flüssige und präzise Cursorsteuerung sicherzustellen.

    !!! note "Worin unterscheiden sich Absolute Mode und Relative Mode?"

        - **Relative Mode**: Die Mausposition wird anhand der Bewegung und nicht anhand fester Bildschirmkoordinaten berechnet. Sie müssen in das Remote-Fenster klicken, um die Maus zu steuern. Der Cursor ist innerhalb des Remote-Bildschirms gesperrt und kann sich nicht reibungslos herausbewegen. Dieser Modus bietet eine bessere Kompatibilität mit BIOS, älteren Systemen und eingebetteten Geräten.

        - **Absolute Mode**: Die Mausposition entspricht exakten Bildschirmkoordinaten. Der Remote-Cursor folgt dem lokalen Cursor flüssig und präzise, sodass ein nahtloser Wechsel zwischen Ihrem lokalen Bildschirm und dem Remote-Bildschirm möglich ist. Dieser Modus eignet sich ideal für die tägliche Desktop-Steuerung und präzise Aktionen, auch wenn es durch die Netzwerkübertragung zu einer leichten Verzögerung kommen kann.

        Kurz gesagt: Verwenden Sie Absolute für eine flüssige tägliche Steuerung; verwenden Sie Relative für BIOS-Zugriff, für einige ältere Geräte, die keine absolute Positionierung unterstützen, oder um versehentliche Cursorbewegungen zu vermeiden.

- **Relative Sensitivity**: Ist verfügbar, wenn Mouse Mode auf Relative eingestellt ist.

- **Primary Button**: Wählen Sie die linke oder rechte Taste als primäre Klicktaste aus. Diese Funktion wurde mit Firmware v1.9.0 eingeführt.

### System

Sie können die Anzeigeeinstellungen des Konsolensystems anpassen oder das Gerät mit einem Klick zurücksetzen.

![settings-system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/settings-system.png){class="glboxshadow"}

- **Device Identity**: Passen Sie die Identität des KVM an oder ändern Sie sie, wie sie vom gesteuerten Gerät erkannt wird. Beachten Sie, dass EDID und Geräteidentifikation synchronisiert bleiben. Wenn eines von beiden geändert wird, wird das andere automatisch aktualisiert, um eine korrekte Geräteerkennung sicherzustellen.

    ![device identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/device-identity.png){class="glboxshadow"}

- **Language**: Stellen Sie die Sprache der Konsole auf Chinesisch, Englisch oder Japanisch ein.

- **Color Mode**: Passen Sie die Designfarbe auf Light oder Dark mode an.

- **Time Zone**: Passen Sie die Zeitzone der KVM-Konsole an.

- **Reset KVM**: Setzen Sie Ihren KVM mit nur einem Klick auf die Werkseinstellungen zurück.

### Network

Hier können Sie die Netzwerkdetails des Comet prüfen, z. B. Hostname und IP-Adresse.

![settings-network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/settings-network.png){class="glboxshadow"}

- **Hostname**: Sie können den Geräte-Hostnamen direkt in der Konsole ändern. Diese Funktion wurde mit Firmware v1.7.0 eingeführt.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/modify-hostname.png){class="glboxshadow"}

- **Ethernet**: Wenn Comet über ein Ethernet-Kabel mit einem Upstream-Netzwerkgerät verbunden ist, wird seine Ethernet-IP-Adresse hier angezeigt. Sie können auf die IP-Adresse oder den Pfeil nach rechts klicken, um die Ethernet-Details anzuzeigen.

    Wenn das Protokoll DHCP ist, wird die Seite wie folgt angezeigt.

    ![ethernet dhcp](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/eth-dhcp.png){class="glboxshadow"}

    Wenn Sie eine statische IP-Adresse festlegen möchten, stellen Sie das Protokoll auf **Static** um und geben Sie die erforderlichen Netzwerkparameter (z. B. IP-Adresse, Netzmaske, Gateway) entsprechend ein.

    ![ethernet static](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/eth-static.png){class="glboxshadow"}

## Toolbox

Navigieren Sie in der Konsole zu **Toolbox**. Die Toolbox-Seite umfasst vier Bereiche:

- [Clipboard](#clipboard)
- [Shortcut](#shortcut)
- [Wake On Lan](#wake-on-lan)
- [Terminal](#terminal)

### Clipboard

Die Zwischenablage ermöglicht es Ihnen, Text einfach vom steuernden Gerät auf das gesteuerte Gerät einzufügen, ohne Dateien übertragen zu müssen.

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-clipboard.png){class="glboxshadow"}

### Shortcut

Mit Shortcuts können Sie Aktionen schneller ausführen, ohne die virtuelle Tastatur zu verwenden. So arbeiten Sie effizienter und sparen Zeit bei alltäglichen Aufgaben. Hier finden Sie einige häufig verwendete Shortcuts.

![toolbox-shortcut](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-shortcut1.png){class="glboxshadow"}

Klicken Sie auf **Modify**, um die Shortcut-Optionen nach Bedarf anzupassen.

![toolbox-shortcut-modify](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-shortcut2.png){class="glboxshadow"}

### Wake-on-Lan

Wake-on-LAN (WOL) ist eine Technologie, mit der das gesteuerte Gerät aus der Ferne eingeschaltet oder aus einem Energiesparzustand geweckt werden kann.

Klicken Sie auf **Add Device**, um ein Gerät aus demselben LAN auszuwählen.

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-wol.png){class="glboxshadow"}

![wol add device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/wol-add-device.png){class="glboxshadow"}

Wenn das Gerät, das Sie hinzufügen möchten, nicht in der Liste enthalten ist, klicken Sie auf **Add Manually** und geben Sie Gerätenamen und MAC-Adresse ein.

![wol add manually](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/wol-add-manually.png){class="glboxshadow"}

### Terminal

Sie können auf das Terminal des Comet zugreifen, um erweiterte Einstellungen vorzunehmen. Klicken Sie auf **Access**.

![toolbox-terminal-1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-terminal1.png){class="glboxshadow"}

Sie werden zum GLKVM-Terminal weitergeleitet.

![toolbox-terminal-2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-terminal2.png){class="glboxshadow"}

## Accessories

GL.iNet bietet optionales KVM-Zubehör an, um das Ein-/Ausschalten des Geräts aus der Ferne zu steuern.

Lesen Sie zuerst die entsprechende Bedienungsanleitung, um das Zubehör mit dem gesteuerten Gerät zu verbinden.

- [Fingerbot (FGB-01) Benutzerhandbuch](../gl-fgb-01/index.md){target="_blank"}

- [ATX Board (GL-ATXPC) Benutzerhandbuch](../gl-atx-board/index.md){target="_blank"}

Melden Sie sich anschließend bei der KVM-Konsole an und navigieren Sie zu **Accessories**. Die Zubehöreinstellungen sind erst verfügbar, nachdem das Zubehör installiert wurde.

### Fingerbot

Der Fingerbot wird am physischen Ein-/Aus-Schalter des gesteuerten Geräts befestigt, um die Stromversorgung des gesteuerten Geräts aus der Ferne zu steuern.

Er arbeitet entsprechend den Einstellungen in der Konsole.

![accessories fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/fingerbot.png){class="glboxshadow"}

- **Time**: Die Druckdauer des Fingerbot. Sie können sie auf 0.5s/3s/8s einstellen.

- **Strength**: Es gibt zwei Stufen der Druckstärke: Lightly Press und Firmly Press.

    - **Lightly Press**: Ideal für kurze oder leichtgängige Tasten.

    - **Firmly Press**: Ideal für tiefe oder schwergängige Tasten.

    ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### ATX Power

Das ATX Board wird im Computergehäuse installiert, um das Ein-/Ausschalten/Neustarten des Geräts aus der Ferne zu steuern.

Er arbeitet entsprechend den Einstellungen in der Konsole.

![accessories atxpower](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/atx-board.png){class="glboxshadow"}

- **Power (Short Press)**: Wird zum normalen Einschalten oder Aufwecken des Systems verwendet.

- **Power (Long Press)**: Führt ein erzwungenes Herunterfahren aus.

- **Restart**: Startet das Gerät neu.

## Virtual Media

Navigieren Sie in der Konsole zu **Virtual Media**. Hier können Sie die folgenden Vorgänge ausführen:

- [Share Files](#file-sharing)
- [Mount Images](#image-mounting)
- [Replace Storage Drive](#replace-storage-drive)
- [Format Disk](#format-disk)

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/virtual-media.png){class="glboxshadow"}

### File Sharing

Comet kann ein les- und beschreibbares USB-Laufwerk emulieren, sodass Sie Dateien zwischen dem steuernden Gerät und dem gesteuerten Gerät freigeben und verwalten können.

**Um Dateien vom steuernden Gerät für das gesteuerte Gerät freizugeben, führen Sie die folgenden Schritte aus.**

1. Ziehen Sie Dateien in das Feld oder klicken Sie darauf, um Dateien von Ihrem steuernden Gerät hochzuladen oder per URL hochzuladen.

    Nach dem Hochladen werden die Dateien wie folgt angezeigt.

    ![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing1.png){class="glboxshadow"}

2. Klicken Sie auf **Mount To Remote** -> **File Sharing**.

    ![file sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing2.png){class="glboxshadow"}

3. In der Konsole wird ein Fenster eingeblendet, das die Schritte für die Dateifreigabe wie unten dargestellt anzeigt.

    ![file sharing tips](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing3.png){class="glboxshadow"}

4. Warten Sie einen Moment. Ein Laufwerk mit dem Namen **"GLKVM"** wird automatisch auf dem Bildschirm angezeigt. Anschließend sehen Sie, dass die Dateien, die Sie zuvor vom steuernden Gerät auf Comet hochgeladen haben, für das gesteuerte Gerät freigegeben wurden. Jetzt können Sie die Dateien in diesem Laufwerk auf dem gesteuerten Gerät anzeigen, verschieben oder löschen.

    ![glkvm disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing4.png){class="glboxshadow"}

    **Tipps**: Wenn das Laufwerk nicht automatisch angezeigt wird, öffnen Sie **This PC** auf Ihrem gesteuerten Gerät.

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/thispc.png){class="glboxshadow"}

    Suchen Sie anschließend ein Laufwerk mit dem Namen **GLKVM**. Jetzt können Sie die Dateien in diesem Laufwerk anzeigen, verschieben oder löschen.

5. Wenn Sie die Freigabe beenden möchten, klicken Sie in der Symbolleiste auf **Virtual Media** und anschließend auf **Stop Sharing**.

    ![stop sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/stop-sharing1.png){class="glboxshadow"}

**Um Dateien vom gesteuerten Gerät für das steuernde Gerät freizugeben, führen Sie die folgenden Schritte aus.**

1. Verschieben oder kopieren Sie auf dem gesteuerten Gerät die Dateien, die Sie freigeben möchten, in das Laufwerk **GLKVM**.

    Beispielsweise wurde eine PDF-Datei mit dem Namen "slate7pro_datasheet" vom Desktop des gesteuerten Geräts auf den Datenträger **GLKVM** kopiert.

    ![move file to disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing5.png){class="glboxshadow"}

2. Wechseln Sie zur Konsole des Comet, klicken Sie in der Symbolleiste auf **Virtual Media** und anschließend auf **Stop Sharing**.

    ![stop sharing 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/stop-sharing2.png){class="glboxshadow"}

3. Diese Datei wird anschließend wie unten dargestellt unter **Virtual Media** angezeigt. Jetzt können Sie diese Datei von Comet auf Ihr steuerndes Gerät herunterladen.

    ![file shared](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing6.png){class="glboxshadow"}

### Image Mounting

Comet kann ein schreibgeschütztes virtuelles CD/DVD- oder Festplattenlaufwerk auf dem gesteuerten Gerät simulieren. Sie können während des BIOS- oder UEFI-Startvorgangs auf dieses Laufwerk zugreifen.

Diese Funktion kann Ihnen helfen, das Betriebssystem neu zu installieren, ein ISO zur Installation von Anwendungen auf dem gesteuerten Gerät einzubinden oder andere Aufgaben auszuführen.

1. Ziehen Sie Dateien in das Feld oder klicken Sie darauf, um Dateien hochzuladen. **Stellen Sie sicher, dass diese Datei als iso-Format eingebunden werden kann**.

    Nach dem Hochladen werden die Dateien wie folgt angezeigt.

    ![image mounting 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting1.png){class="glboxshadow"}

2. Klicken Sie auf **Mount To Remote** -> **Image Mounting**.

    ![image mounting 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting2.png){class="glboxshadow"}

3. Wählen Sie im Pop-up-Fenster die Datei aus und klicken Sie auf **Mount Image**.

    ![image mounting 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting3.png){class="glboxshadow"}

4. In der Konsole wird ein Fenster eingeblendet, das die Schritte zum Einbinden wie unten dargestellt anzeigt.

    ![image mounting 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting4.png){class="glboxshadow"}

5. Jetzt können Sie diese Datei über das CD-Laufwerk auf dem gesteuerten Gerät verwenden.

    ![image mounting 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting5.png){class="glboxshadow"}

### Replace Storage Drive

Sie können ein USB-Speichergerät in den KVM-USB-Anschluss einstecken, um den internen Speicher zu ersetzen.

![replace storage drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/replace-storage.png){class="glboxshadow"}

### Format Disk

Sie können den Datenträger formatieren oder virtuelle Medien mit einem Klick deaktivieren.

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/format-disable.png){class="glboxshadow"}

- **Format**: Löscht alle Daten auf dem Datenträger und initialisiert dessen Dateisystemstruktur neu.

- **Disable**: Durch das Deaktivieren der virtuellen Medien wird das KVM-Gerät sofort neu gestartet.

## Apps Center

Navigieren Sie in der Konsole zu **Apps Center**. Die integrierten Anwendungen finden Sie hier.

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/apps-center.png){class="glboxshadow"}

### Tailscale

[Tailscale](https://tailscale.com/){target="_blank"} ist ein auf WireGuard basierender Mesh-VPN-Dienst, der verschlüsselte Peer-to-Peer-Privatnetzwerke zwischen Geräten erstellt, ohne Portweiterleitung oder komplexe Firewall-Einrichtung.

Comet ist in Tailscale integriert und ermöglicht Ihnen den Fernzugriff über das virtuelle Tailscale-Netzwerk.

Binden Sie einfach Comet und Ihr steuerndes Gerät an dasselbe Tailscale-Konto. Anschließend können Sie aus der Ferne auf Ihren Comet zugreifen, indem Sie seine **Tailscale virtual IP** in einem Webbrowser auf dem steuernden Gerät eingeben, ohne die GLKVM App zu installieren. Details finden Sie [hier](../../faq/remote_access_via_tailscale.md){target="_blank"}.

Nach dem Binden zeigt die Konsole das verknüpfte Tailscale-Konto an und schaltet erweiterte Funktionen wie Exit Node und Subnet Routes frei.

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier

[ZeroTier](https://www.zerotier.com/){target="_blank"} erstellt verschlüsselte virtuelle Overlay-Netzwerke, um verteilte Geräte weltweit so zu verbinden, als befänden sie sich im selben lokalen Netzwerk.

Comet ist in ZeroTier integriert und ermöglicht Ihnen den Fernzugriff über das virtuelle ZeroTier-Netzwerk.

Treten Sie einfach mit Comet und Ihrem steuernden Gerät demselben ZeroTier-Netzwerk bei. Anschließend können Sie aus der Ferne auf Ihren Comet zugreifen, indem Sie seine **ZeroTier IP** in einem Webbrowser auf dem steuernden Gerät eingeben, ohne die GLKVM App zu installieren. Details finden Sie [hier](../../faq/remote_access_via_zerotier.md){target="_blank"}.

Nach dem Binden zeigt die Konsole die ZeroTier Network ID und Virtual IP an.

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/apps-zerotier-enabled.png){class="glboxshadow"}

### NetBird

[NetBird](https://netbird.io/){target="_blank"} ist eine Open-Source-Zero-Trust-Networking-Plattform, mit der Sie sichere private Netzwerke für den Einsatz zu Hause und im Unternehmen aufbauen können. Als WireGuard®-basiertes Overlay-Netzwerk ermöglicht NetBird sicheren Zugriff auf Ihre Geräte jederzeit und überall.

Comet ist in NetBird integriert und ermöglicht Ihnen den Fernzugriff über das virtuelle NetBird-Netzwerk. Details finden Sie [hier](../../faq/remote_access_via_netbird.md){target="_blank"}.

Nach dem Binden zeigt die Konsole die NetBird Virtual IP an.

![netbird enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/apps-netbird-enabled.png){class="glboxshadow"}

## Help

Navigieren Sie in der Konsole zu **Help**. Hier finden Sie weitere Informationen zu GL.iNet KVM und Hilfedokumentation. Außerdem können Sie Protokolle zur Fehlerbehebung exportieren.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/help.png){class="glboxshadow"}

## Toolbar

Navigieren Sie in der Konsole in die obere rechte Ecke, um auf die folgenden Werkzeuge zuzugreifen:

- [Text Recognition](#text-recognition)
- [Collapse Toolbar](#collapse)
- [Fullscreen](#fullscreen)
- [Upgrade](#upgrade)
- [Cloud Service](#cloud-service)
- [Security](#security)
- Reboot
- Logout

### Text Recognition

Mit der Funktion Text Recognition können Sie einen Bereich auf dem Remote-Bildschirm auswählen und Text daraus einfach extrahieren. Sie basiert auf Optical Character Recognition (OCR) und wurde mit Firmware v1.9.0 eingeführt.

Um sie zu verwenden, klicken Sie auf den Abwärtspfeil, um Ihre bevorzugte Erkennungssprache auszuwählen, z. B. Chinesisch, Englisch oder zweisprachig (Zh/En).

![recognition language](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/ocr_function.png){class="glboxshadow"}

Klicken Sie anschließend auf das Symbol "T". Der Remote-Bildschirm wird abgedunkelt. Ziehen Sie einen Rahmen um den Text, den Sie extrahieren möchten, und das System erkennt ihn automatisch. Anschließend können Sie den erkannten Text bei Bedarf kopieren.

Mit dieser Funktion können Sie Text einfach vom Remote-Bildschirm (d. h. dem gesteuerten Gerät) erfassen und zur weiteren Verwendung auf das steuernde Gerät kopieren.

### Collapse

Klicken Sie oben rechts auf das Symbol mit dem Aufwärtspfeil, um die Symbolleiste einzuklappen.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/collapse1.png){class="glboxshadow"}

Wenn die Symbolleiste eingeklappt ist, klicken Sie oben auf das Symbol mit dem Abwärtspfeil, um sie auszuklappen.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/collapse2.png){class="glboxshadow"}

### Fullscreen

Klicken Sie oben rechts auf das Vollbildsymbol (quadratisch), um in den Vollbildmodus zu wechseln.

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/fullscreen1.png){class="glboxshadow"}

Um den Vollbildmodus zu verlassen, halten Sie die Taste **Esc** gedrückt oder klicken Sie oben rechts auf das Symbol zum Beenden des Vollbildmodus (gitterförmig).

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/fullscreen2.png){class="glboxshadow"}

### Upgrade

Klicken Sie oben rechts auf die Firmware-Version, um nach Updates zu suchen.

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/upgrade1.png){class="glboxshadow"}

Im Pop-up-Fenster können Sie auf **Update Settings** klicken, um ein lokales Upgrade durchzuführen, am Beta-Programm teilzunehmen oder die aktuelle Konfiguration zu speichern.

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/upgrade2.png){class="glboxshadow"}

Laden Sie vor einem lokalen Upgrade die neueste Firmware aus dem [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} herunter.

### Cloud Service

GL.iNet KVM Cloud ermöglicht Ihnen den Fernzugriff auf das gesteuerte Gerät. Details finden Sie [hier](../../faq/remote_access_via_cloud.md){target="_blank"}.

Sobald Ihr Comet an die Cloud gebunden ist, zeigt die Konsole den Cloud-Status wie folgt an.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/cloud.png){class="glboxshadow"}

### Security

Unter Security können Sie das Admin-Passwort ändern, die Zwei-Faktor-Authentifizierung aktivieren und ein TLS-Zertifikat anpassen.

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/security.png){class="glboxshadow"}

- Admin-Passwort ändern.

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/admin-password.png){class="glboxshadow" width="434"}

- 2FA: Aktivieren Sie die Zwei-Faktor-Authentifizierung, um Ihr Konto zu schützen.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/2fa.png){class="glboxshadow"}

- TLS Certificate

    Das System verwendet das vorinstallierte Standardzertifikat für den Browserzugriff. Wenn Sie das TLS-Zertifikat für den Webbrowser-Zugriff anpassen möchten, klicken Sie oben rechts in der Konsole auf **TLS Certificate**, wählen Sie **Custom Certificate** aus und laden Sie anschließend Ihre **certificate file & private key file** hoch.

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/tls-certificate.png){class="glboxshadow"}
