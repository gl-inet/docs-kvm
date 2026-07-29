# Comet Q (GL-RMQ1) Konsolenhandbuch

## Settings

Navigieren Sie in der Konsole zu **Settings**. Die Einstellungsseite umfasst vier Bereiche:

- [Video](#video)
- [Audio&Keyboard&Mouse](#audiokeyboardmouse)
- [System](#system)
- [Network](#network)

### Quick Search

Sie können die gewünschten Einstellungen schnell finden, indem Sie oben auf der Seite **Settings** Schlüsselwörter eingeben.

![quick search](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/quick-search.png){class="glboxshadow"}

### Video

Sie können die Videoeinstellungen in der Konsole anpassen, z. B. EDID, Videoqualität, Videoübertragung und Bildschirmausrichtung.

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-video.png){class="glboxshadow"}

- **Type**: Wählen Sie den Typ Ihres gesteuerten Geräts aus.

    Das System wendet automatisch den empfohlenen Mausmodus und die empfohlenen EDID-Einstellungen an, um das beste Anzeige-Seitenverhältnis und eine hohe Steuerungsgenauigkeit bereitzustellen. Wechseln Sie diese Option, wenn das Gerät nicht korrekt erkannt wird oder Sie einen benutzerdefinierten Typ verwenden müssen.

- **EDID**: Kurz für Extended Display Identification Data. Diese Funktion wählt automatisch die optimalen Anzeigeparameter aus.

    Die Standardeinstellung ist für die meisten Szenarien geeignet und muss in der Regel nicht geändert werden. Details finden Sie [hier](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. Wenn der Bildschirm nach der EDID-Anpassung nicht aktualisiert wird, starten Sie das gesteuerte Gerät neu.

- **Mode**: Wechseln Sie je nach Bedarf zwischen Smart mode und Normal mode. Smart mode hilft, den Bandbreitenverbrauch zu reduzieren, insbesondere bei schwachen Netzwerken.

- **Quality**: Passen Sie die Videoqualität entsprechend Ihrer Netzwerkumgebung und den Anforderungen an die Auflösung auf Low/Medium/High/Ultra-high/Lossless an.

- **Transfer**: Wechseln Sie die Videoübertragungsmethode zwischen WebRTC, WebRTC (FEC) und Direct. Beachten Sie, dass Direct keine Tonübertragung bietet.

    !!! note "Worin unterscheiden sich WebRTC, WebRTC (FEC) und Direct?"

        - **WebRTC**: Bietet ein ausgewogenes Verhältnis zwischen flüssigem Video und stabilem Audio für die Echtzeit-Fernsteuerung.

        - **WebRTC (FEC)**: Fügt Forward Error Correction hinzu, um die Verbindungsstabilität bei schlechten oder instabilen Netzwerkbedingungen zu verbessern. Bei Auswahl dieser Option werden verlorene Datenpakete automatisch durch die Übertragung einer kleinen Menge redundanter Daten repariert, wodurch Bildschirmflackern und Verzögerungen reduziert werden.

        - **Direct**: Bietet die geringste Latenz und verlustfreie Videoqualität, unterstützt jedoch keine Audioübertragung.

- **Orientation**: Stellen Sie den Drehwinkel der Konsole auf 0°/90°/180°/270° ein.

- **View**: Diese Einstellung bestimmt die Bildschirmskalierung beim Ändern der Größe des Browserfensters. Verfügbare Optionen: Adaptive, Best Picture Quality, Original Pixel.

### Audio&Keyboard&Mouse

Sie können die relevanten Einstellungen für Audio, Tastatur und Maus anpassen.

![audio keyboard mouse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/audio-keyboard-mouse.png){class="glboxshadow"}

- **Speaker**: Steuert die Audioausgabe des gesteuerten Geräts (z. B. Systemtöne, Videoaudio).

- **Microphone**: Überträgt lokales Audio (z. B. Ihre Stimme) vom steuernden Gerät an die Gegenstelle. Es unterstützt eine Ein-Klick-Stummschaltung sowie eine Shortcut-Funktion durch langes Drücken zum Aktivieren des Mikrofons (d. h. Press To Speak).

    ![mic settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/mic-settings.png){class="glboxshadow"}

    ![press to speak](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/press-to-speak.png){class="glboxshadow"}

- **Keyboard**: Schalten Sie die Tastatur des gesteuerten Geräts ein oder aus.

- **Bad Link Mode**: Bedeutet, dass Tasten sofort losgelassen werden. Jeder Tastendruck wird als einzelne schnelle Drücken-und-Loslassen-Aktion gesendet, wodurch während der Fernsteuerung hängende Tasten oder unbeabsichtigte wiederholte Eingaben verhindert werden.

- **Show Virtual Keyboard**: Zeigen Sie die virtuelle Tastatur in der Konsole an und verwenden Sie sie.

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: Diese Funktion vertauscht die Tasten Cmd und Ctrl, um die Tastaturkompatibilität zwischen verschiedenen Betriebssystemen sicherzustellen.

- **Mouse**: Schalten Sie die Maus des gesteuerten Geräts ein oder aus.

- **Show Local Cursor**: Zeigt die Maus des aktuellen Geräts auf dem Bildschirm an.

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

### System

Sie können die Anzeigeeinstellungen des Konsolensystems anpassen oder das Gerät mit einem Klick zurücksetzen.

![settings-system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-system.png){class="glboxshadow"}

- **Device Identity**: Passen Sie die Identität des KVM an oder ändern Sie sie, wie sie vom gesteuerten Gerät erkannt wird. Beachten Sie, dass EDID und Geräteidentifikation synchronisiert bleiben. Wenn eines von beiden geändert wird, wird das andere automatisch aktualisiert, um eine korrekte Geräteerkennung sicherzustellen.

    ![device identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/device-identity.png){class="glboxshadow"}

- **Language**: Stellen Sie die Sprache der Konsole auf Chinesisch oder Englisch ein.

- **Color Mode**: Passen Sie die Designfarbe auf Light oder Dark mode an.

- **Time Zone**: Passen Sie die Zeitzone der KVM-Konsole an.

- **Reset KVM**: Setzen Sie Ihren KVM mit nur einem Klick auf die Werkseinstellungen zurück.

### Network

Hier können Sie die Netzwerkdetails des Comet Q prüfen und ändern, z. B. Hostname und IP-Adresse.

![settings-network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-network.png){class="glboxshadow"}

- **Hostname**: Sie können den Geräte-Hostnamen direkt in der Konsole ändern.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/hostname.png){class="glboxshadow"}

- **Wi-Fi**: Die Wi-Fi-IP-Adresse des Comet Q wird hier angezeigt, wenn er mit einem Wi-Fi-Netzwerk verbunden ist. Klicken Sie auf die Wi-Fi-SSID oder den Pfeil nach rechts, um die Wi-Fi-Details anzuzeigen, einschließlich SSID, zugewiesener IP-Adresse, Gateway und der MAC-Adresse, die Ihr Comet Q für die Verbindung verwendet.

    ![wifi config](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/wifi-config.png){class="glboxshadow"}

    Wenn Sie ihn mit einem anderen Wi‑Fi-Netzwerk verbinden möchten, klicken Sie auf **Switch Wi-Fi** und wählen Sie ein Wi-Fi aus der Liste der verfügbaren Netzwerke aus.

## Toolbox

Navigieren Sie in der Konsole zu **Toolbox**. Die Toolbox-Seite umfasst drei Bereiche:

- [Clipboard](#clipboard)
- [Shortcut](#shortcut)
- [Terminal](#terminal)

### Clipboard

Die Zwischenablage ermöglicht es Ihnen, Text einfach vom steuernden Gerät auf das gesteuerte Gerät einzufügen, ohne Dateien übertragen zu müssen.

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-clipboard.png){class="glboxshadow"}

### Shortcut

Mit Shortcuts können Sie Aktionen schneller ausführen, ohne die virtuelle Tastatur zu verwenden. So arbeiten Sie effizienter und sparen Zeit bei alltäglichen Aufgaben. Hier finden Sie einige häufig verwendete Shortcuts.

![toolbox-shortcut1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut1.png){class="glboxshadow"}

Klicken Sie auf **Modify**, um die Shortcut-Optionen nach Bedarf anzupassen.

![toolbox-shortcut2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut2.png){class="glboxshadow"}

### Terminal

Sie können auf das Terminal des Comet Q zugreifen, um erweiterte Einstellungen vorzunehmen. Klicken Sie auf **Access**.

![toolbox-terminal1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal1.png){class="glboxshadow"}

Sie werden zum GLKVM-Terminal weitergeleitet.

![toolbox-terminal2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal2.png){class="glboxshadow"}

## Virtual Media

Navigieren Sie in der Konsole zu **Virtual Media**. Comet Q kann ein les- und beschreibbares USB-Laufwerk emulieren, sodass Sie Dateien zwischen dem steuernden Gerät und dem gesteuerten Gerät freigeben und verwalten können.

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-media.png){class="glboxshadow"}

### File Sharing

**Um Dateien vom steuernden Gerät für das gesteuerte Gerät freizugeben, führen Sie die folgenden Schritte aus.**

1. Ziehen Sie Dateien in das Feld oder klicken Sie darauf, um Dateien von Ihrem steuernden Gerät hochzuladen oder per URL hochzuladen.

    Nach dem Hochladen werden die Dateien wie folgt angezeigt.

    ![file-sharing1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing1.png){class="glboxshadow"}

2. Klicken Sie auf **Mount To Remote** -> **File Sharing**.

    ![file-sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing2.png){class="glboxshadow"}

3. In der Konsole wird ein Fenster eingeblendet, das die Schritte für die Dateifreigabe wie unten dargestellt anzeigt.

    ![file-sharing3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing3.png){class="glboxshadow"}

4. Warten Sie einen Moment. Ein Laufwerk mit dem Namen **"GLKVM"** wird möglicherweise automatisch auf dem Bildschirm angezeigt. Anschließend sehen Sie, dass die Dateien, die Sie zuvor vom steuernden Gerät auf Comet Q hochgeladen haben, für das gesteuerte Gerät freigegeben wurden. Jetzt können Sie die Dateien in diesem Laufwerk auf dem gesteuerten Gerät anzeigen, verschieben oder löschen.

    ![file-sharing4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing4.png){class="glboxshadow"}

    **Tipps**: Wenn das Laufwerk nicht automatisch angezeigt wird, öffnen Sie **This PC** auf Ihrem gesteuerten Gerät.

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/thispc.png){class="glboxshadow"}

    Suchen Sie anschließend ein Laufwerk mit dem Namen **GLKVM**. Jetzt können Sie die Dateien in diesem Laufwerk anzeigen, verschieben oder löschen.

5. Wenn Sie die Freigabe beenden möchten, klicken Sie in der Symbolleiste auf **Virtual Media** und anschließend auf **Stop Sharing**.

    ![stop sharing1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing1.png){class="glboxshadow"}

**Um Dateien vom gesteuerten Gerät für das steuernde Gerät freizugeben, führen Sie die folgenden Schritte aus.**

1. Verschieben oder kopieren Sie auf dem gesteuerten Gerät die Dateien, die Sie freigeben möchten, in das Laufwerk **GLKVM**.

    Beispielsweise wurde eine PDF-Datei mit dem Namen "gl-rm10_datasheet" vom Desktop des gesteuerten Geräts auf das Laufwerk **GLKVM** verschoben.

    ![file-sharing5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing5.png){class="glboxshadow"}

2. Wechseln Sie zur Konsole des Comet Q, klicken Sie in der Symbolleiste auf **Virtual Media** und anschließend auf **Stop Sharing**.

    ![stop sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing2.png){class="glboxshadow"}

3. Diese Datei wird anschließend wie unten dargestellt unter **Virtual Media** angezeigt. Jetzt können Sie diese Datei von Comet Q auf Ihr steuerndes Gerät herunterladen.

    ![file sharing6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing6.png){class="glboxshadow"}

### Format Disk

Sie können den Datenträger formatieren oder virtuelle Medien mit einem Klick deaktivieren.

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/format-disable.png){class="glboxshadow"}

- **Format**: Löscht alle Daten auf dem Datenträger und initialisiert dessen Dateisystemstruktur neu.

- **Disable**: Durch das Deaktivieren der virtuellen Medien wird das KVM-Gerät sofort neu gestartet.

## Apps Center

Navigieren Sie in der Konsole zu **Apps Center**. Die integrierten Anwendungen finden Sie hier.

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-center.png){class="glboxshadow"}

### Tailscale

[Tailscale](https://tailscale.com/){target="_blank"} ist ein auf WireGuard basierender Mesh-VPN-Dienst, der verschlüsselte Peer-to-Peer-Privatnetzwerke zwischen Geräten erstellt, ohne Portweiterleitung oder komplexe Firewall-Einrichtung.

Comet Q ist in Tailscale integriert und ermöglicht Ihnen den Fernzugriff über das virtuelle Tailscale-Netzwerk.

Binden Sie einfach Comet Q und Ihr steuerndes Gerät an dasselbe Tailscale-Konto. Anschließend können Sie aus der Ferne auf Ihren Comet Q zugreifen, indem Sie seine **Tailscale virtual IP** in einem Webbrowser auf dem steuernden Gerät eingeben, ohne die GLKVM App zu installieren. Details finden Sie [hier](../../faq/remote_access_via_tailscale.md){target="_blank"}.

Nach dem Binden zeigt die Konsole das verknüpfte Tailscale-Konto an und schaltet erweiterte Funktionen wie Exit Node und Subnet Routes frei.

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier

[ZeroTier](https://www.zerotier.com/){target="_blank"} erstellt verschlüsselte virtuelle Overlay-Netzwerke, um verteilte Geräte weltweit so zu verbinden, als befänden sie sich im selben lokalen Netzwerk.

Comet Q ist in ZeroTier integriert und ermöglicht Ihnen den Fernzugriff über das virtuelle ZeroTier-Netzwerk.

Treten Sie einfach mit Comet Q und Ihrem steuernden Gerät demselben ZeroTier-Netzwerk bei. Anschließend können Sie aus der Ferne auf Ihren Comet Q zugreifen, indem Sie seine **ZeroTier IP** in einem Webbrowser auf dem steuernden Gerät eingeben, ohne die GLKVM App zu installieren. Details finden Sie [hier](../../faq/remote_access_via_zerotier.md){target="_blank"}.

Nach dem Binden zeigt die Konsole die ZeroTier Network ID und Virtual IP an.

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-zerotier-enabled.png){class="glboxshadow"}

## Help

Navigieren Sie in der Konsole zu **Help**. Hier finden Sie weitere Informationen zu GL.iNet KVM und Hilfedokumentation. Außerdem können Sie Protokolle zur Fehlerbehebung exportieren.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/help.png){class="glboxshadow"}

## Toolbar

Navigieren Sie in der Konsole in die obere rechte Ecke, um auf die folgenden Werkzeuge zuzugreifen:

- [Collapse Toolbar](#collapse)
- [Fullscreen](#fullscreen)
- [Upgrade](#upgrade)
- [Cloud Service](#cloud-service)
- [Security](#security)
- Reboot
- Logout

### Collapse

Klicken Sie oben rechts auf das Symbol mit dem Aufwärtspfeil, um die Symbolleiste einzuklappen.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse1.png){class="glboxshadow"}

Wenn die Symbolleiste eingeklappt ist, klicken Sie oben auf das Symbol mit dem Abwärtspfeil, um sie auszuklappen.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse2.png){class="glboxshadow"}

### Fullscreen

Klicken Sie oben rechts auf das Vollbildsymbol (quadratisch), um in den Vollbildmodus zu wechseln.

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen1.png){class="glboxshadow"}

Um den Vollbildmodus zu verlassen, halten Sie die Taste **Esc** gedrückt oder klicken Sie oben rechts auf das Symbol zum Beenden des Vollbildmodus (gitterförmig).

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen2.png){class="glboxshadow"}

### Upgrade

Klicken Sie oben rechts auf die Firmware-Version, um nach Updates zu suchen.

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade1.png){class="glboxshadow"}

Im Pop-up-Fenster können Sie ein Online-Upgrade durchführen, wenn eine neuere Firmware verfügbar ist. Alternativ können Sie die neueste Firmware aus dem [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} herunterladen und bei Bedarf ein lokales Upgrade durchführen.

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade2.png){class="glboxshadow"}

### Cloud Service

GL.iNet KVM Cloud ermöglicht Ihnen den Fernzugriff auf das gesteuerte Gerät. Details finden Sie [hier](../../faq/remote_access_via_cloud.md){target="_blank"}.

Sobald Ihr Comet Q an die Cloud gebunden ist, zeigt die Konsole den Cloud-Status wie folgt an.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/cloud.png){class="glboxshadow"}

### Security

Unter Security können Sie das Admin-Passwort ändern, die Zwei-Faktor-Authentifizierung aktivieren und ein TLS-Zertifikat anpassen.

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/security.png){class="glboxshadow"}

- Admin-Passwort ändern

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/admin-password.png){class="glboxshadow" width="434"}

- 2FA: Aktivieren Sie die Zwei-Faktor-Authentifizierung, um Ihr Konto zu schützen.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/2fa.png){class="glboxshadow"}

- TLS Certificate

    Das System verwendet das vorinstallierte Standardzertifikat für den Browserzugriff. Wenn Sie das TLS-Zertifikat für den Webbrowser-Zugriff anpassen möchten, klicken Sie oben rechts in der Konsole auf **TLS Certificate**, wählen Sie **Custom Certificate** aus und laden Sie anschließend Ihre **certificate file & private key file** hoch.

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/tls-certificate.png){class="glboxshadow"}
