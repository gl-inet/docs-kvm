# Comet X (GL-RM4PE) Konsolenhandbuch

## Session

Klicken Sie in der Konsole auf das Symbol Session, um **Session Settings** zu öffnen. Diese Seite umfasst vier Bereiche:

- [Video](#video)
- [Audio & Camera](#audio--camera)
- [Keyboard](#keyboard)
- [Mouse](#mouse)

### Video

Sie können unter Session Settings Videoeinstellungen wie Anzeigemodus, Videoqualität, Videoübertragung, Bildschirmausrichtung und EDID anpassen.

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/session_video.png){class="glboxshadow"}

- **Transfer**: Wechseln Sie die Videoübertragungsmethode zwischen WebRTC, WebRTC (FEC), WebRTC (Native) und Direct. Beachten Sie, dass Direct keine Tonübertragung bietet.

    !!! note "Worin unterscheiden sich WebRTC, WebRTC (FEC), WebRTC (Native) und Direct?"

        - **WebRTC**: Bietet ein ausgewogenes Verhältnis zwischen flüssigem Video und stabilem Audio für die Echtzeit-Fernsteuerung.

        - **WebRTC (FEC)**: Fügt Forward Error Correction hinzu, um die Verbindungsstabilität bei schlechten oder instabilen Netzwerkbedingungen zu verbessern. Bei Auswahl dieser Option werden verlorene Datenpakete automatisch durch die Übertragung einer kleinen Menge redundanter Daten repariert, wodurch Bildschirmflackern und Verzögerungen reduziert werden.

        - **WebRTC (Native)**: Verwendet die Google WebRTC Library, um eine bessere Streaming-Leistung und eine flüssigere Echtzeit-Fernsteuerung zu bieten. Dieser Übertragungsmodus wurde mit Firmware v1.10.0 eingeführt.

        - **Direct**: Bietet die geringste Latenz und verlustfreie Videoqualität, unterstützt jedoch keine Audioübertragung.

- **Mode**: Wechseln Sie je nach Bedarf zwischen Smart mode und Normal mode. Smart mode hilft, den Bandbreitenverbrauch zu reduzieren, insbesondere bei schwachen Netzwerken.

- **Latency Mode**: Sie können für das Gerät zwischen Lowest Latency und Smooth Display wählen. Diese Funktion wurde mit Firmware v1.9.0 eingeführt.

    !!! note "Worin unterscheiden sich Lowest Latency und Smooth Display?"

        - **Lowest Latency**: Minimiert die Eingabelatenz, um eine direktere Reaktion von Tastatur und Maus zu ermöglichen.

        - **Smooth Display**: Optimiert die visuelle Leistung, um Ruckeln und Frameverluste zu vermeiden und eine gleichmäßige Wiedergabe zu ermöglichen.

- **Quality**: Passen Sie die Videoqualität entsprechend Ihrer Netzwerkumgebung und den Anforderungen an die Auflösung auf Auto/Low/Medium/High/Ultra-high/Lossless an.

- **FEC Packets**: Bei einem instabilen Netzwerk werden verlorene Datenpakete automatisch durch das Senden einer kleinen Menge redundanter Daten repariert, wodurch Bildschirmflackern und Verzögerungen reduziert werden. Sie können den FEC-Anteil auf 5 %/10 %/15 %/20 % einstellen.

- **Orientation**: Stellen Sie den Drehwinkel der Konsole auf 0°/90°/180°/270° ein.

- **EDID**: Kurz für Extended Display Identification Data. Diese Funktion wählt automatisch die optimalen Anzeigeparameter aus.

    Die Standardeinstellung ist für die meisten Szenarien geeignet und muss in der Regel nicht geändert werden. Details finden Sie [hier](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. Wenn der Bildschirm nach der EDID-Anpassung nicht aktualisiert wird, starten Sie das gesteuerte Gerät neu.

- **View**: Diese Einstellung bestimmt die Bildschirmskalierung beim Ändern der Größe des Browserfensters. Verfügbare Optionen: Adaptive, Best Picture Quality, Original Pixel. Diese Funktion wurde mit Firmware v1.8.0 eingeführt.

- **Screen Privacy**: Wenn der Sichtschutz aktiviert ist, zeigt der externe HDMI-OUT-Bildschirm keine Inhalte mehr an. Dadurch bleibt die Privatsphäre bei Fernzugriffen gewahrt.

### Audio & Camera

Sie können die Audio- und Kameraeinstellungen für das gesteuerte Gerät anpassen.

![Audio_Camera](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/session_audio_camera.png){class="glboxshadow"}

- **Speaker**: Steuert die Audioausgabe des gesteuerten Geräts (z. B. Systemtöne, Videoaudio).

- **Microphone**: Überträgt lokales Audio (z. B. Ihre Stimme) vom steuernden Gerät an die Gegenstelle. Es unterstützt eine Ein-Klick-Stummschaltung sowie eine Shortcut-Funktion durch langes Drücken zum Aktivieren des Mikrofons (d. h. Press To Speak).

    **Hinweis**: Der Shortcut muss vor der Verwendung manuell unter [Settings](#usb-devices) konfiguriert werden.

- **Camera**: Wenn die Kamera auf dem steuernden Gerät aktiviert ist, werden die lokalen Videobilder per Passthrough an den Remote-Host übertragen, auf dem eine virtuelle USB-Kamera emuliert wird. Anwendungen auf dem Remote-Host, beispielsweise Konferenzprogramme und FaceTime, können diesen Videostream verwenden und bieten damit dieselbe Nutzererfahrung wie eine direkt angeschlossene physische Kamera.

    **Hinweis**: Diese Funktion wurde mit Firmware v1.10.0 eingeführt und wird ausschließlich im Modus WebRTC (FEC) unterstützt. Derzeit ist sie nur über einen Webbrowser verfügbar; App und Desktop-Client werden noch nicht unterstützt.

### Keyboard

Unter Keyboard können Sie die Einstellungen für die Tastaturbedienung des gesteuerten Geräts konfigurieren.

![keyboard image](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/session_keyboard.png){class="glboxshadow"}

- **Bad Link Mode**: Bedeutet, dass Tasten sofort losgelassen werden. Jeder Tastendruck wird als einzelne schnelle Drücken-und-Loslassen-Aktion gesendet, wodurch während der Fernsteuerung hängende Tasten oder unbeabsichtigte wiederholte Eingaben verhindert werden.

- **Show Virtual Keyboard**: Zeigen Sie die virtuelle Tastatur in der Konsole an und verwenden Sie sie.

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/session_virtual_keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: Diese Funktion vertauscht die Tasten Cmd und Ctrl, um die Tastaturkompatibilität zwischen verschiedenen Betriebssystemen sicherzustellen.

### Mouse

Sie können die Mauseinstellungen anpassen, um das gesteuerte Gerät komfortabler zu bedienen.

![mouse image](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/session_mouse.png){class="glboxshadow"}

- **Show Local Cursor**: Zeigt die Maus des aktuellen Geräts auf dem Bildschirm an.

- **Mouse Jiggle**: Die Funktion Mouse Jiggle simuliert dezente, periodische Mausbewegungen, um zu verhindern, dass das gesteuerte Gerät aufgrund längerer Inaktivität in den Ruhezustand wechselt, beispielsweise während Remote-Meetings oder bei der Serververwaltung.

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

## Toolbox

Navigieren Sie in der Konsole zu **Toolbox**. Die Toolbox-Seite umfasst fünf Bereiche:

- [Clipboard](#clipboard)
- [OCR](#ocr)
- [Shortcut](#shortcut)
- [Wake on Lan](#wake-on-lan)
- [Terminal](#terminal)

### Clipboard

Die Zwischenablage ermöglicht es Ihnen, Text einfach vom steuernden Gerät auf das gesteuerte Gerät einzufügen, ohne Dateien übertragen zu müssen.

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_clipboard.png){class="glboxshadow"}

### OCR

OCR ist eine Texterkennungsfunktion, mit der Sie einen Bereich auf dem Remote-Bildschirm auswählen und den darin enthaltenen Text einfach extrahieren können. Diese Funktion wurde mit Firmware v1.9.0 eingeführt.

Klicken Sie zur Verwendung auf den Abwärtspfeil und wählen Sie die gewünschte Erkennungssprache aus, beispielsweise Chinesisch, Englisch oder zweisprachig (Zh/En).

![recognition language](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_ocr_language.png){class="glboxshadow"}

Klicken Sie anschließend auf **Capture**. Der Remote-Bildschirm wird abgedunkelt. Ziehen Sie einen Rahmen um den Text, den Sie extrahieren möchten; das System erkennt ihn automatisch. Anschließend können Sie den erkannten Text nach Bedarf kopieren.

![copy text](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_ocr_copy_text.png){class="glboxshadow"}

Mit dieser Funktion können Sie Text einfach vom Remote-Bildschirm, also dem gesteuerten Gerät, erfassen und auf das lokale steuernde Gerät kopieren.

### Shortcut

Mit Shortcuts können Sie Aktionen schneller ausführen, ohne die virtuelle Tastatur zu verwenden. So arbeiten Sie effizienter und sparen Zeit bei alltäglichen Aufgaben. Hier finden Sie einige häufig verwendete Shortcuts.

![toolbox-shortcut1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_shortcut_1.png){class="glboxshadow"}

Klicken Sie auf **Modify**, um die Shortcut-Optionen nach Bedarf anzupassen.

![toolbox-shortcut2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_shortcut_2.png){class="glboxshadow"}

### Wake-on-Lan

Wake-on-LAN (WOL) ist eine Technologie, mit der das gesteuerte Gerät aus der Ferne eingeschaltet oder aus einem Energiesparzustand geweckt werden kann.

Klicken Sie auf **Add Device** und wählen Sie ein Gerät aus demselben LAN aus.

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_wol.png){class="glboxshadow"}

![wol-add-device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_wol_add_devices.png){class="glboxshadow" width=500}

Wenn das Gerät, das Sie hinzufügen möchten, nicht in der Liste enthalten ist, klicken Sie auf **Add Manually** und geben Sie Gerätenamen und MAC-Adresse ein.

![wol-add-manually](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_add_manually.png){class="glboxshadow" width=500}

### Terminal

Sie können auf das Terminal des Comet X zugreifen, um erweiterte Einstellungen vorzunehmen. Klicken Sie auf **Access**.

![toolbox-terminal1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox-terminal_1.png){class="glboxshadow"}

Sie werden zum GLKVM-Terminal weitergeleitet.

![toolbox-terminal2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox-terminal_2.png){class="glboxshadow"}

## Accessories

GL.iNet bietet optionales KVM-Zubehör an, um das Ein-/Ausschalten des Geräts aus der Ferne zu steuern.

Lesen Sie zuerst die entsprechende Bedienungsanleitung, um das Zubehör mit Ihrem gesteuerten Gerät zu verbinden. Beachten Sie, dass Comet X gleichzeitig mit vier Fingerbots oder ATX Boards verbunden werden kann, jedoch immer nur eines davon gesteuert werden kann.

- [Fingerbot (FGB-01) Benutzerhandbuch](../gl-fgb-01/index.md){target="_blank"}

- [ATX Board (GL-ATXPC) Benutzerhandbuch](../gl-atx-board/index.md){target="_blank"}

Melden Sie sich anschließend bei der KVM-Konsole an und navigieren Sie zu **Accessories**. Die Zubehöreinstellungen sind erst verfügbar, nachdem das Zubehör installiert wurde.

### Fingerbot

Der Fingerbot wird am physischen Ein-/Aus-Schalter des gesteuerten Geräts befestigt, um die Stromversorgung des gesteuerten Geräts aus der Ferne zu steuern.

Er arbeitet entsprechend den Einstellungen in der Konsole.

![accessories fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/accessories_fingerbot.png){class="glboxshadow"}

- **Time**: Die Druckdauer des Fingerbot. Sie können sie auf 0.5s/3s/8s einstellen.

- **Strength**: Es gibt zwei Stufen der Druckstärke: Lightly Press und Firmly Press.

    - **Lightly Press**: Ideal für kurze oder leichtgängige Tasten.

    - **Firmly Press**: Ideal für tiefe oder schwergängige Tasten.

    ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### ATX Power

Das ATX Board wird im Computergehäuse installiert, um das Ein-/Ausschalten/Neustarten des Geräts aus der Ferne zu steuern.

Er arbeitet entsprechend den Einstellungen in der Konsole.

- **Power (Short Press)**: Wird zum normalen Einschalten oder Aufwecken des Systems verwendet.

- **Power (Long Press)**: Führt ein erzwungenes Herunterfahren aus.

- **Restart**: Startet das Gerät neu.

## Virtual Media

Navigieren Sie in der Konsole zu **Virtual Media**. Hier können Sie die folgenden Vorgänge ausführen:

- [File Sharing](#file-sharing)
- [Image Mounting](#image-mounting)
- [Format Disk](#format-disk)

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/virtual_media.png){class="glboxshadow"}

### File Sharing

Comet X kann ein les- und beschreibbares USB-Laufwerk emulieren, sodass Sie Dateien zwischen dem steuernden Gerät und dem gesteuerten Gerät freigeben und verwalten können.

**Um Dateien vom steuernden Gerät für das gesteuerte Gerät freizugeben, führen Sie die folgenden Schritte aus.**

1. Ziehen Sie Dateien in das Feld oder klicken Sie darauf, um Dateien von Ihrem steuernden Gerät hochzuladen oder per URL hochzuladen.

    Nach dem Hochladen werden die Dateien wie folgt angezeigt.

    ![file sharing1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file_sharing_1.png){class="glboxshadow"}

2. Klicken Sie auf **Mount To Remote** -> **File Sharing**.

    ![file sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file_sharing_2.png){class="glboxshadow"}

3. In der Konsole wird ein Fenster eingeblendet, das die Schritte für die Dateifreigabe wie unten dargestellt anzeigt.

    ![file sharing3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file_sharing_3.png){class="glboxshadow"}

4. Warten Sie einen Moment. Ein Laufwerk mit dem Namen **"GLKVM"** wird möglicherweise automatisch auf dem Bildschirm angezeigt. Anschließend sehen Sie, dass die Dateien, die Sie zuvor vom steuernden Gerät auf Comet X hochgeladen haben, für das gesteuerte Gerät freigegeben wurden. Jetzt können Sie die Dateien in diesem Laufwerk auf dem gesteuerten Gerät anzeigen, verschieben oder löschen.

    ![file sharing4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file_sharing_4.png){class="glboxshadow"}

    **Tipps**: Wenn das Laufwerk nicht automatisch angezeigt wird, öffnen Sie **This PC** auf Ihrem gesteuerten Gerät.

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/this_pc.png){class="glboxshadow"}

    Suchen Sie anschließend ein Laufwerk mit dem Namen **GLKVM**. Jetzt können Sie die Dateien in diesem Laufwerk anzeigen, verschieben oder löschen.

5. Wenn Sie die Freigabe beenden möchten, klicken Sie in der Symbolleiste auf **Virtual Media** und anschließend auf **Stop Sharing**.

    ![stop sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/stop_sharing_1.png){class="glboxshadow"}

**Um Dateien vom gesteuerten Gerät für das steuernde Gerät freizugeben, führen Sie die folgenden Schritte aus.**

1. Verschieben oder kopieren Sie auf dem gesteuerten Gerät die Dateien, die Sie freigeben möchten, in das Laufwerk **GLKVM**.

    Beispielsweise wurde ein Image mit dem Namen "gl-rm10_datasheet" vom Desktop des gesteuerten Geräts auf das Laufwerk **GLKVM** verschoben.

    ![file sharing5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file_sharing_5.png){class="glboxshadow"}

2. Wechseln Sie zur Konsole des Comet X, klicken Sie in der Symbolleiste auf **Virtual Media** und anschließend auf **Stop Sharing**.

    ![stop sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/stop_sharing_2.png){class="glboxshadow"}

3. Diese Datei wird anschließend wie unten dargestellt unter **Virtual Media** angezeigt. Jetzt können Sie diese Datei von Comet X auf Ihr steuerndes Gerät herunterladen.

    ![file sharing6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file_sharing_6.png){class="glboxshadow"}

### Image Mounting

Comet X kann ein schreibgeschütztes virtuelles CD/DVD- oder Festplattenlaufwerk auf dem gesteuerten Gerät simulieren. Sie können während des BIOS- oder UEFI-Startvorgangs auf dieses Laufwerk zugreifen.

Diese Funktion kann Ihnen helfen, das Betriebssystem neu zu installieren, ein ISO zur Installation von Anwendungen auf dem gesteuerten Gerät einzubinden oder andere Aufgaben auszuführen.

1. Ziehen Sie Dateien in das Feld oder klicken Sie darauf, um Dateien hochzuladen. **Stellen Sie sicher, dass diese Datei als iso-Format eingebunden werden kann**.

    Nach dem Hochladen werden die Dateien wie folgt angezeigt.

    ![image mount1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/image-mount1.png){class="glboxshadow"}

2. Klicken Sie auf **Mount To Remote** -> **Image Mounting**.

    ![image mount2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/image-mount2.png){class="glboxshadow"}

3. Wählen Sie im Pop-up-Fenster die Datei aus und klicken Sie auf **Mount Image**.

    ![image mount3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/image-mount3.png){class="glboxshadow"}

4. Jetzt können Sie diese Datei über das CD-Laufwerk auf dem gesteuerten Gerät verwenden.

    ![image mount4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/image-mount4.png){class="glboxshadow"}

### Format Disk

Sie können den Datenträger formatieren oder virtuelle Medien mit einem Klick deaktivieren.

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/format_disk.png){class="glboxshadow"}

- **Format**: Löscht alle Daten auf dem Datenträger und initialisiert dessen Dateisystemstruktur neu.

- **Disable**: Durch das Deaktivieren der virtuellen Medien wird das KVM-Gerät sofort neu gestartet.

## Apps Center

Navigieren Sie in der Konsole zu **Apps Center**. Die integrierten Anwendungen finden Sie hier.

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/app_center.png){class="glboxshadow"}

### Tailscale

[Tailscale](https://tailscale.com/){target="_blank"} ist ein auf WireGuard basierender Mesh-VPN-Dienst, der verschlüsselte Peer-to-Peer-Privatnetzwerke zwischen Geräten erstellt, ohne Portweiterleitung oder komplexe Firewall-Einrichtung.

Comet X ist in Tailscale integriert und ermöglicht Ihnen den Fernzugriff über das virtuelle Tailscale-Netzwerk.

Binden Sie einfach Comet X und Ihr steuerndes Gerät an dasselbe Tailscale-Konto. Anschließend können Sie aus der Ferne auf Ihren Comet X zugreifen, indem Sie seine **Tailscale virtual IP** in einem Webbrowser auf dem steuernden Gerät eingeben, ohne die GLKVM App zu installieren. Details finden Sie [hier](../../faq/remote_access_via_tailscale.md){target="_blank"}.

Nach dem Binden zeigt die Konsole das verknüpfte Tailscale-Konto an und schaltet erweiterte Funktionen wie Exit Node und Subnet Routes frei.

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier

[ZeroTier](https://www.zerotier.com/){target="_blank"} erstellt verschlüsselte virtuelle Overlay-Netzwerke, um verteilte Geräte weltweit so zu verbinden, als befänden sie sich im selben lokalen Netzwerk.

Comet X ist in ZeroTier integriert und ermöglicht Ihnen den Fernzugriff über das virtuelle ZeroTier-Netzwerk.

Treten Sie einfach mit Comet X und Ihrem steuernden Gerät demselben ZeroTier-Netzwerk bei. Anschließend können Sie aus der Ferne auf Ihren Comet X zugreifen, indem Sie seine **ZeroTier IP** in einem Webbrowser auf dem steuernden Gerät eingeben, ohne die GLKVM App zu installieren. Details finden Sie [hier](../../faq/remote_access_via_zerotier.md){target="_blank"}.

Nach dem Binden zeigt die Konsole die ZeroTier Network ID und Virtual IP an.

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/apps-zerotier-enabled.png){class="glboxshadow"}

### NetBird

[NetBird](https://netbird.io/){target="_blank"} ist eine Open-Source-Zero-Trust-Networking-Plattform, mit der Sie sichere private Netzwerke für den Einsatz zu Hause und im Unternehmen aufbauen können. Als WireGuard®-basiertes Overlay-Netzwerk ermöglicht NetBird sicheren Zugriff auf Ihre Geräte jederzeit und überall.

Comet X ist in NetBird integriert und ermöglicht Ihnen den Fernzugriff über das virtuelle NetBird-Netzwerk. Details finden Sie [hier](../../faq/remote_access_via_netbird.md){target="_blank"}.

Nach dem Binden zeigt die Konsole die NetBird Virtual IP an.

![netbird enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/apps-netbird-enabled.png){class="glboxshadow"}

## Help

Navigieren Sie in der Konsole zu **Help**. Hier finden Sie weitere Informationen zu GL.iNet KVM und Hilfedokumentation. Außerdem können Sie Protokolle zur Fehlerbehebung exportieren.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/help.png){class="glboxshadow"}

## Toolbar

Navigieren Sie in der Konsole in die obere rechte Ecke, um auf die folgenden Werkzeuge zuzugreifen:

- [Switch Signal](#switch-signal)
- [Collapse Toolbar](#collapse)
- [Fullscreen](#fullscreen)
- [Upgrade](#upgrade)
- [Connection Stats](#connection-stats)
- [Cloud Service](#cloud-service)
- [Logout](#logout)

### Switch Signal

Comet X kann für lokale oder Remote-Steuerung mit bis zu 4 Servern verbunden werden. Es kann immer nur ein Server gleichzeitig gesteuert werden, während alle anderen verbundenen Server im Standby-Modus bleiben.

Sie können Signalquellen schnell über den Touchscreen oder die KVM-Konsole wechseln. Nachfolgend finden Sie die Schritte zum Wechseln der Signalquelle in der KVM-Konsole.

1. Klicken Sie oben rechts auf die Schaltfläche **Port**.

2. Wählen Sie die Ziel-Signalquelle aus. Beachten Sie, dass Funktionen während des Umschaltvorgangs nicht verfügbar sind.

    ![switch signal](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/switch-signal.png){class="glboxshadow"}

3. (Optional) Passen Sie den Portnamen nach Bedarf an.

    ![port edit 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/port_edit1.png){class="glboxshadow"}

    ![port edit 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/port_edit2.png){class="glboxshadow" width=500}

### Collapse

Klicken Sie oben rechts auf das Symbol mit dem Aufwärtspfeil, um die Symbolleiste einzuklappen.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_collapse_1.png){class="glboxshadow"}

Wenn die Symbolleiste eingeklappt ist, klicken Sie oben auf das Symbol mit dem Abwärtspfeil, um sie auszuklappen.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_collapse_2.png){class="glboxshadow"}

### Fullscreen

Klicken Sie oben rechts auf das Vollbildsymbol (quadratisch), um in den Vollbildmodus zu wechseln.

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_fullscreen_1.png){class="glboxshadow"}

Um den Vollbildmodus zu verlassen, halten Sie die Taste **Esc** gedrückt oder klicken Sie oben rechts auf das Symbol zum Beenden des Vollbildmodus (gitterförmig).

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_fullscreen_2.png){class="glboxshadow"}

### Upgrade

Klicken Sie oben rechts auf die Firmware-Version, um nach Updates zu suchen.

![firmware upgrade 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_upgrade_1.png){class="glboxshadow"}

Im Pop-up-Fenster können Sie auf **Local Upgrade** klicken, um eine Firmwaredatei hochzuladen.

![firmware upgrade 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_upgrade_2.png){class="glboxshadow"}

![firmware upgrade 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_upgrade_3.png){class="glboxshadow" width=350}

Laden Sie vor einem lokalen Upgrade die neueste Firmware aus dem [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} herunter.

### Connection Stats

Connection Stats enthält ein Data Dashboard, das Latenz, Jitter und weitere Echtzeitmesswerte überwacht.

Klicken Sie auf das Listensymbol, um den Gerätestatus und die Echtzeitdaten anzuzeigen.

![data dashboard 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/data_dashboard_1.png){class="glboxshadow"}

Klicken Sie auf das Diagrammsymbol, um statistische Daten wie Netzwerklatenz, Netzwerk-Jitter, Paketverlustrate, Echtzeit-Bildrate und Wiedergabeverzögerung anzuzeigen.

![data dashboard 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/data_dashboard_2.png){class="glboxshadow"}

### Cloud Service

GL.iNet KVM Cloud ermöglicht Ihnen den Fernzugriff auf das gesteuerte Gerät. Details finden Sie [hier](../../faq/remote_access_via_cloud.md){target="_blank"}.

Sobald Ihr Comet X an die Cloud gebunden ist, zeigt die Konsole den Cloud-Status wie folgt an.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_cloud_service.png){class="glboxshadow"}

### Logout

Klicken Sie zum Abmelden auf das Symbol Logout.

![layout](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_layout.png){class="glboxshadow"}

## Settings

Klicken Sie in der Konsole in der Navigationsleiste auf das Symbol Settings, um die folgende Einstellungsseite zu öffnen. Diese Funktion wurde mit Firmware v1.10.0 eingeführt.

- [USB Devices](#usb-devices)
- [Preferences](#preferences)
- [Network](#network)
- [Security](#security)
- [Cloud](#cloud)
- [System](#system)

![Settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings.png){class="glboxshadow"}

### USB Devices

Unter USB Device werden alle emulierten USB-Geräte zentral verwaltet. Auf dieser Seite können Sie virtuelle Peripheriegeräte ein- oder ausschalten, um die Kompatibilität mit dem gesteuerten Host zu verbessern.

![USB Emulated Devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_usb_devices.png){class="glboxshadow"}

- **Microphone**

    Wenn das Mikrofon stummgeschaltet ist, können Sie auf Settings klicken und die Shortcuts an Ihre Nutzungsgewohnheiten anpassen. Halten Sie die zugewiesene Shortcut-Taste gedrückt, um zu sprechen; beim Loslassen wird das Mikrofon wieder stummgeschaltet.

    ![mic settings 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_microphone_1.png){class="glboxshadow" width=600}

    ![mic settings 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_microphone_2.png){class="glboxshadow" width=434}

  - **Device Identity**

    Passen Sie die Identität des KVM an oder ändern Sie sie, wie sie vom gesteuerten Gerät erkannt wird. Beachten Sie, dass EDID und Geräteidentifikation synchronisiert bleiben. Wenn eines von beiden geändert wird, wird das andere automatisch aktualisiert, um eine korrekte Geräteerkennung sicherzustellen.

    ![Device Identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_device_identity.png){class="glboxshadow" width=350}

### Preferences

Unter Preferences verwalten Sie Layout Preferences, System Settings und Device Screen.

![Preferences](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences**: Sie können nach Bedarf festlegen, ob die Symbolleiste im Vollbildmodus und die Statusleiste im Fenstermodus angezeigt werden.

- **System Settings**: Passen Sie die Systemeinstellungen an, indem Sie den Tab Title des Browsers, die Language (Chinesisch, Englisch oder Japanisch), den Color Mode (Light oder Dark) und die Timezone entsprechend Ihrer Region auswählen.

- **Device Screen**: Sie können den Gerätebildschirm verwalten und in der Vorschau anzeigen. Zu den verfügbaren Einstellungen gehören der Lock Screen-Modus (World Clock, Clock Only oder Wallpaper Only), Time Format, Date Format und Wallpaper.

### Network

Hier können Sie die Netzwerkdetails des Comet X prüfen und ändern, z. B. Hostname und IP-Adresse.

![network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_network.png){class="glboxshadow"}

- **Hostname**: Sie können den Geräte-Hostnamen direkt in der Konsole ändern. Diese Funktion wurde mit Firmware v1.7.0 eingeführt.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_network_hostname.png){class="glboxshadow" width=600}

- **Ethernet Settings**: Wenn Comet X über ein Ethernet-Kabel mit einem Upstream-Netzwerkgerät verbunden ist, werden hier die Ethernet-Details angezeigt.

    Wenn das Protokoll DHCP ist, wird die Seite wie folgt angezeigt.

    ![ethernet dhcp](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_network_dhcp.png){class="glboxshadow" width=600}

    Wenn Sie eine statische IP-Adresse festlegen möchten, stellen Sie das Protokoll auf **Static** um und geben Sie die erforderlichen Netzwerkparameter (z. B. IP-Adresse, Netzmaske, Gateway) entsprechend ein.

    ![ethernet static](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_network_static.png){class="glboxshadow" width=600}

### Security

Unter Security können Sie das Admin-Passwort ändern, die Zwei-Faktor-Authentifizierung aktivieren und das TLS-Zertifikat anpassen.

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/setting_security.png){class="glboxshadow"}

- Admin-Passwort ändern

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_change_password.png){class="glboxshadow" width="434"}

- 2FA: Aktivieren Sie die Zwei-Faktor-Authentifizierung, um Ihr Konto zu schützen.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_security_2fa.png){class="glboxshadow"}

- TLS Certificate

    Das System verwendet das vorinstallierte Standardzertifikat für den Browserzugriff. Wenn Sie das TLS-Zertifikat für den Webbrowser-Zugriff anpassen möchten, klicken Sie unter TLS Certificate auf **Custom** und laden Sie anschließend Ihre **certificate file & private key file** hoch.

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_tls_certificate.png){class="glboxshadow" width=600}

### Cloud

Über Cloud können Sie per Cloud-Dienst aus der Ferne auf Ihr Gerät zugreifen und es verwalten.

Sie können Ihr Gerät über eine URL an die Cloud binden. Unter **More Settings** finden Sie weitere Optionen wie Bind With Code und App Download. Bei Bedarf ist auch Disable verfügbar.

![Cloud 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_cloud_1.png){class="glboxshadow"}

Nach erfolgreicher Bindung können Sie die Informationen zum gebundenen Cloud-Konto anzeigen. Klicken Sie auf **Access Cloud**, um Devices zu verwalten, oder auf **More Settings**, um den Dienst nach Bedarf zu deaktivieren oder die Bindung aufzuheben.

![Cloud 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_cloud_2.png){class="glboxshadow"}

Alternativ können Sie die oben genannten Verwaltungsvorgänge auch über Cloud Service in der oberen Symbolleiste ausführen.

### System

Unter System können Sie Folgendes konfigurieren:

![system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/setting_system.png){class="glboxshadow"}

- **System**: Klicken Sie auf **Reboot**, um das Gerät neu zu starten, oder auf **Reset**, um die aktuelle Gerätekonfiguration zu löschen und das Gerät erneut einzurichten.

- **Upgrade**: Sie können Beta Center aktivieren, um Beta-Firmwareupdates zu erhalten, oder über Local Upgrade eine lokale Datei manuell installieren.

    ![local Upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/setthing_system_local_update.png){class="glboxshadow" width=400}

- **Help & Support**: Mit Export Log Files können Sie die Laufzeitprotokolle des Geräts zur Fehlerbehebung und für den Kundendienst speichern. Help Document bietet Zugriff auf Benutzerhandbücher, FAQs und Dokumentation zur Fehlerbehebung.
