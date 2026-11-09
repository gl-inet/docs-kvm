# Wie kann ich die lokale Kamera für Remote-Meetings freigeben? (Camera Passthrough) {#how-can-i-share-the-local-camera-with-remote-meetings-camera-passthrough}

**Hinweis**: Diese Funktion wurde mit Firmware v1.10.0 eingeführt und wird nur im Modus WebRTC (FEC) unterstützt. Sie ist derzeit über Webbrowser und den Desktop-Client verfügbar, wird aber in der mobilen App noch nicht unterstützt.

---

Wenn Sie von zu Hause arbeiten, können Sie per KVM auf Ihren Bürocomputer zugreifen und dort an einer Videokonferenz über Zoom, Microsoft Teams oder eine ähnliche App teilnehmen. Die Kamera zeigt jedoch möglicherweise nur Ihr Büro und nicht Sie.

Mit der Funktion **Camera** von GL.iNet KVM können Sie das Video Ihrer Kamera am Heimcomputer als virtuelle USB-Kamera an Ihren Bürocomputer übertragen. Wählen Sie diese Kamera in der Konferenz-App aus, damit andere Teilnehmer Sie sehen können, während Sie Dateien oder Anwendungen Ihres Bürocomputers teilen.

## Schnelle Einrichtung {#quick-setup}

Führen Sie die folgenden Schritte aus, um die Funktion Camera zu verwenden. Als Beispiel dient eine Zoom-Videokonferenz.

1. Melden Sie sich vor der Teilnahme am Meeting auf dem steuernden Computer bei Ihrem KVM an und öffnen Sie **Session** -> **Audio & Camera**. Aktivieren Sie Camera und klicken Sie auf das Kamerasymbol, um zu starten.

    ![enable camera 1](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera.png){class="glboxshadow"}

    Wenn beim Aktivieren von Camera eine Meldung zum USB-Ressourcenlimit erscheint, öffnen Sie **Settings** -> **USB Devices** und deaktivieren Sie nicht verwendete emulierte USB-Geräte, um Ressourcen freizugeben. Aktivieren Sie anschließend Camera und versuchen Sie es erneut.

    ![enable camera 3](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-3.png){class="glboxshadow"}

    Ihr Browser fordert möglicherweise den Zugriff auf die Kamera an. Wählen Sie die gewünschte Kamera aus, prüfen Sie die Videovorschau und erlauben Sie den Zugriff.

    ![enable camera 2](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-2.png){class="glboxshadow"}

2. Öffnen Sie Zoom auf dem gesteuerten Computer und treten Sie einem Meeting bei. Klicken Sie auf den Pfeil neben der Videoschaltfläche und wählen Sie **UVC camera** aus.

    ![uvc-camera](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/uvc-camera.png){class="glboxshadow"}

    Aktivieren Sie anschließend das Video, damit andere Teilnehmer das Bild der Kamera des steuernden Geräts sehen können.

    **Hinweis**: Sorgen Sie für eine stabile Netzwerkverbindung, damit das Video während des Meetings flüssig und klar ist.

## Fehlerbehebung {#troubleshooting}

??? note "Was soll ich tun, wenn das Kamerabild den gesteuerten Computer nicht erreicht?"

    Prüfen Sie, ob der gesteuerte Computer die virtuelle Kamera des KVM erkennt.

    Öffnen Sie auf dem gesteuerten Computer **Settings** -> **Bluetooth & devices** -> **Cameras** und suchen Sie unter Connected cameras nach UVC Camera.

    ![check camera settings](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/check-camera-settings.png){class="glboxshadow"}

    Wenn sie nicht angezeigt wird, ist die USB-Datenverbindung zwischen KVM und gesteuertem Computer möglicherweise getrennt oder locker.

??? note "Was soll ich tun, wenn beim Aktivieren von Camera in der KVM-Konsole die Meldung 'Camera Access Denied' erscheint?"

    ![camera access denied](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/camera-access-denied.png){class="glboxshadow"}

    Prüfen Sie auf dem steuernden Computer Folgendes:

    - **Kameraverfügbarkeit**: Stellen Sie sicher, dass die Kamera angeschlossen und funktionsfähig ist. Testen Sie sie mit der Kamera-App des Systems und schließen Sie diese App vor einem erneuten Versuch.

    - **Systemberechtigungen**: Öffnen Sie unter Windows 11 Settings -> Privacy & security -> Camera und aktivieren Sie Camera access, Let apps access your camera und Let desktop apps access your camera.

    - **Browserberechtigungen**: Erlauben Sie der KVM-Website den Zugriff auf Ihre Kamera. Falls der Zugriff zuvor blockiert war, aktualisieren Sie die Kameraberechtigungen der Website und laden Sie die Seite neu.

    - **Kameranutzung**: Schließen Sie andere Apps oder Browser-Tabs, die die Kamera möglicherweise verwenden, etwa Zoom oder Microsoft Teams.

    Aktivieren Sie nach diesen Prüfungen Camera erneut in der KVM-Konsole.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
