# Dateien zwischen steuerndem und gesteuertem Gerät freigeben {#how-to-share-files-between-controlling-and-controlled-devices}

GL.iNet KVM emuliert ein beschreibbares USB-Laufwerk, mit dem Sie Dateien zwischen dem steuernden und dem gesteuerten Gerät freigeben und verwalten können.

In den folgenden Schritten verwenden wir Comet (GL-RM1) als Beispiel. 

## Dateien an das gesteuerte Gerät senden {#send-files-to-controlled-device}

Führen Sie die folgenden Schritte aus, um Dateien vom steuernden Gerät für das gesteuerte Gerät freizugeben.

1. Navigieren Sie in der Konsole zu **Virtual Media**. Ziehen Sie Dateien in das Feld oder klicken Sie darauf, um Dateien von Ihrem steuernden Gerät hochzuladen, oder laden Sie sie über eine URL hoch. 

    Nach dem Hochladen werden die Dateien wie folgt angezeigt.

    ![upload files](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing1.png){class="glboxshadow"}

2. Klicken Sie auf **Mount To Remote** -> **File Sharing**. 

    ![file sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing2.png){class="glboxshadow"}

3. In der Konsole erscheint ein Fenster mit den Schritten zur Dateifreigabe, wie unten gezeigt. 
    
    ![file sharing tips](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing3.png){class="glboxshadow"}

4. Warten Sie einen Moment. Ein Laufwerk mit dem Namen **"GLKVM"** erscheint automatisch auf dem Bildschirm. Der Comet emuliert nun ein beschreibbares USB-Laufwerk auf dem gesteuerten Gerät. Die zuvor hochgeladenen Dateien sind jetzt für das gesteuerte Gerät freigegeben. 

    Sie können die Dateien in diesem Laufwerk auf dem gesteuerten Gerät nun anzeigen, verschieben oder löschen.

    ![file shared](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing4.png){class="glboxshadow"}
    
    **Tipp**: Wenn das Laufwerk nicht automatisch erscheint, öffnen Sie **This PC** auf Ihrem gesteuerten Gerät.

    ![this pc](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/thispc.png){class="glboxshadow"}

    Suchen Sie ein Laufwerk mit dem Namen **"GLKVM"**. Nun können Sie die Dateien in diesem Laufwerk anzeigen, verschieben oder löschen.

5. Wenn Sie die Freigabe beenden möchten, klicken Sie in der Symbolleiste auf **Virtual Media** und dann auf **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing1.png){class="glboxshadow"}

## Dateien vom gesteuerten Gerät abrufen {#get-files-from-controlled-device}

Führen Sie die folgenden Schritte aus, um Dateien vom gesteuerten Gerät zu empfangen.

1. Verschieben oder kopieren Sie auf dem gesteuerten Gerät die Dateien, die Sie freigeben möchten, in das Laufwerk **GLKVM**.

    Wie unten gezeigt, wurde eine Datei vom Desktop des gesteuerten Geräts auf das Laufwerk **GLKVM** verschoben.

    ![copy file to disk](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing5.png){class="glboxshadow"}
    
2. Wechseln Sie zur Comet-Konsole, klicken Sie in der Symbolleiste auf **Virtual Media** und dann auf **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing2.png){class="glboxshadow"}
    
3. Diese Datei wird anschließend wie folgt unter **Virtual Media** angezeigt. Nun können Sie die Datei vom Comet auf Ihr steuerndes Gerät herunterladen.

    ![file shared](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing6.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
