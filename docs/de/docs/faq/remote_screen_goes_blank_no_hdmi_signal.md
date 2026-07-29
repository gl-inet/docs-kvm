# Was tun, wenn der Remote-Bildschirm leer bleibt oder kein HDMI-Signal angezeigt wird

Wenn beim Zugriff auf das gesteuerte Gerät über KVM der Remote-Bildschirm leer bleibt oder kein HDMI-Signal angezeigt wird, führen Sie die folgenden Schritte zur Fehlerbehebung aus.

![white screen](https://static.gl-inet.com/docs/kvm/faq/blank_screen/white_screen.png){class="glboxshadow"}
<small>(Weißer Bildschirm)</small>

![black screen](https://static.gl-inet.com/docs/kvm/faq/blank_screen/black_screen.png){class="glboxshadow"}
<small>(Schwarzer Bildschirm)</small>

Prüfen Sie zuerst, ob das Problem mit der Videoübertragung zusammenhängt. Melden Sie sich an Ihrem KVM an, gehen Sie zu **Settings** -> **Video** -> **Transfer** und stellen Sie den Übertragungsmodus auf **Direct**.

![change transfer](https://static.gl-inet.com/docs/kvm/faq/blank_screen/change_transfer.png){class="glboxshadow" width="360"}

Wenn das Problem weiterhin besteht, prüfen Sie die folgenden möglichen Ursachen nacheinander.

## Hardwareverbindung prüfen

1. **Defektes HDMI-Kabel**

    Gealterte HDMI-Kabel, oxidierte Steckverbinder oder interne Kabelbrüche können die Signalübertragung unterbrechen. Ersetzen Sie das Kabel durch ein hochwertiges HDMI-Kabel.

    Sie können den HDMI-Signalstatus auch in der KVM-Konsole prüfen. Suchen Sie das Monitorsymbol unten rechts und prüfen Sie, ob "No HDMI signal" angezeigt wird.

    ![no HDMI signal](https://static.gl-inet.com/docs/kvm/faq/blank_screen/no_hdmi_signal.png){class="glboxshadow"}

2. **Falsche Verbindung**

    Wenn Ihr gesteuertes Gerät ein Desktop-PC ist, stellen Sie sicher, dass der **HDMI IN**-Anschluss des KVM mit dem HDMI-OUT-Anschluss der Grafikkarte oder des Mainboards des Desktops verbunden ist. Stellen Sie sicher, dass der Stecker vollständig und fest eingesteckt ist. Bei Geräten mit mehreren HDMI-Ausgängen (z. B. dedizierte GPU + Mainboard-Ausgang) versuchen Sie, auf einen anderen Anschluss zu wechseln.

    Wenn Ihr gesteuertes Gerät ein Laptop ist, stellen Sie sicher, dass der **HDMI IN**-Anschluss des KVM mit dem HDMI-OUT-Anschluss des Laptops verbunden ist.

    Tipp: Einige KVM-Modelle (z. B. Comet Pro und Comet 5G) haben zwei HDMI-Anschlüsse. Stellen Sie sicher, dass das HDMI-Kabel vom gesteuerten Gerät am HDMI IN-Anschluss des KVM eingesteckt ist. Wenn es mit HDMI OUT verbunden ist, wird in der KVM-Konsole kein HDMI-Signal erkannt.

3. **Unsachgemäße Verwendung von Adaptern**

    Wenn ein HDMI-Adapter erforderlich ist, verwenden Sie einen **VGA-to-HDMI**-Adapter, um das gesteuerte Gerät mit dem HDMI IN-Anschluss des GL.iNet KVM zu verbinden.

    Wird für diese Verbindung ein HDMI-to-VGA-Adapter verwendet, können Videosignale nicht korrekt übertragen werden. Das Ergebnis ist ein leerer Bildschirm.

    ![adapter comparison](https://static.gl-inet.com/docs/kvm/faq/blank_screen/adapter_comparison.png){class="glboxshadow"}

## Browsereinstellungen prüfen

Wenn Sie über einen Browser auf das gesteuerte Gerät zugreifen und ein leerer Bildschirm angezeigt wird, versuchen Sie die folgenden Methoden:

1. **Mit mehreren Browsern testen.** Testen Sie Chrome, Firefox, Edge usw., um festzustellen, ob das Problem browserspezifisch ist.

2. **WebRTC Leak Protection/Control-Erweiterungen deaktivieren.** Wenn Sie Erweiterungen/Plug-ins in Ihrem Webbrowser installiert haben, die WebRTC-Verbindungen beeinflussen könnten, deaktivieren Sie diese und testen Sie erneut. Sie können außerdem in den Einstellungen des Browsers unter Settings -> Privacy & Security prüfen, ob der Webbrowser WebRTC-Verbindungen erlaubt.

    ![webrtc](https://static.gl-inet.com/docs/kvm/faq/blank_screen/webrtc.png){class="glboxshadow"}

## Status und Einstellungen des gesteuerten Geräts prüfen

1. **Gerät ist nicht eingeschaltet oder im Energiesparmodus**

    Stellen Sie sicher, dass das gesteuerte Gerät vollständig eingeschaltet ist und sich aufgrund von Energieverwaltungseinstellungen nicht im Energiespar- oder Ruhezustand befindet. Wecken Sie es bei Bedarf über lokale Tasten auf.

2. **Fehlerhafte Grafikkartentreiber auf dem gesteuerten Gerät**

    Nicht installierte oder beschädigte Grafikkartentreiber können dazu führen, dass kein Video ausgegeben wird. Aktualisieren oder installieren Sie die Grafikkartentreiber auf dem gesteuerten Gerät neu, wenn Sie lokal angemeldet sind.

3. **Falscher Anschluss bei dedizierter und integrierter Grafik**

    Wenn das gesteuerte Gerät sowohl eine dedizierte als auch eine integrierte Grafikkarte hat, stellen Sie sicher, dass das HDMI-Kabel mit dem richtigen Grafikanschluss verbunden ist, z. B. mit dem Anschluss der dedizierten Grafikkarte, falls diese installiert ist.

4. **Ungewöhnliche Anzeigeeinstellungen auf dem gesteuerten Gerät (geringe Wahrscheinlichkeit)**

    Wenn das GL.iNet KVM mit dem gesteuerten Gerät verbunden wird, passt es die Anzeigeausgabe automatisch an, indem es für optimale Leistung die EDID des Monitors ausliest. In den meisten Fällen ist die Standard-EDID-Konfiguration für die meisten Szenarien geeignet und muss nicht geändert werden.

    Wenn das gesteuerte Gerät mit Standardmonitoren kompatibel ist, sind leere Bildschirme oder Anzeigeprobleme beim Zugriff über GLKVM unwahrscheinlich. Einige spezifische Kompatibilitätsprobleme (z. B. Linux-System + ASUS-Monitor) können jedoch bei Verwendung von GLKVM zu leeren Bildschirmen führen.

    Bitte prüfen Sie, ob Ihr gesteuertes Gerät mit Standardmonitoren kompatibel ist und ob es Kompatibilitätsprobleme mit einem bestimmten Monitor hat.

5. **Auflösungsproblem**

    Wenn GLKVM mit bestimmten Betriebssystemen verbunden ist (z. B. Proxmox VE Hypervisor), kann die Aushandlung der verfügbaren Anzeigeauflösung fehlschlagen, was zu Anzeigeproblemen führt. Dies lässt sich beheben, indem die Auflösung auf dem gesteuerten Gerät manuell angepasst wird.

    Unten finden Sie als Referenz eine Anleitung zum Ändern der Systemauflösung auf Proxmox VE Hypervisor.

    1. Öffnen Sie das PVE-Terminal und geben Sie den folgenden Befehl ein, um die Datei `/etc/default/grub` zu bearbeiten.

        ```
        nano /etc/default/grub
        ```

    2. Fügen Sie die folgende Zeile hinzu.

        ```
        GRUB_CMDLINE_LINUX_DEFAULT="quiet gfxpayload=text nomodeset
        ```

    3. Kommentieren Sie die Zeile `GRUB_GFXMODE` aus, indem Sie das `#` entfernen, und legen Sie die gewünschte Auflösung fest, z. B. `1024x768`.

        ```
        GRUB_GFXMODE=1024x768
        ```

    4. Drücken Sie `Ctrl + O` und anschließend Enter, um die Konfiguration zu speichern.

    5. Drücken Sie `Ctrl + X`, um den nano-Editor zu verlassen.

    6. Geben Sie den folgenden Befehl ein, um die Konfiguration anzuwenden.

        ```
        update-grub
        ```

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
