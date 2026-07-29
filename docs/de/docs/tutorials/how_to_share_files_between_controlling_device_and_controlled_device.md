# Dateien zwischen steuerndem und gesteuertem Geraet freigeben

GL.iNet KVM emuliert ein beschreibbares USB-Laufwerk, mit dem Sie Dateien zwischen dem steuernden und dem gesteuerten Geraet freigeben und verwalten koennen.

In den folgenden Schritten verwenden wir Comet (GL-RM1) als Beispiel. 

## Dateien an das gesteuerte Geraet senden

Fuehren Sie die folgenden Schritte aus, um Dateien vom steuernden Geraet fuer das gesteuerte Geraet freizugeben.

1. Navigieren Sie in der Konsole zu **Virtual Media**. Ziehen Sie Dateien in das Feld oder klicken Sie darauf, um Dateien von Ihrem steuernden Geraet hochzuladen, oder laden Sie sie ueber eine URL hoch. 

    Nach dem Hochladen werden die Dateien wie folgt angezeigt.

    ![upload files](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing1.png){class="glboxshadow"}

2. Klicken Sie auf **Mount To Remote** -> **File Sharing**. 

    ![file sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing2.png){class="glboxshadow"}

3. In der Konsole erscheint ein Fenster mit den Schritten zur Dateifreigabe, wie unten gezeigt. 
    
    ![file sharing tips](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing3.png){class="glboxshadow"}

4. Warten Sie einen Moment. Ein Laufwerk mit dem Namen **"GLKVM"** erscheint automatisch auf dem Bildschirm. Der Comet emuliert nun ein beschreibbares USB-Laufwerk auf dem gesteuerten Geraet. Die zuvor hochgeladenen Dateien sind jetzt fuer das gesteuerte Geraet freigegeben. 

    Sie koennen die Dateien in diesem Laufwerk auf dem gesteuerten Geraet nun anzeigen, verschieben oder loeschen.

    ![file shared](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing4.png){class="glboxshadow"}
    
    **Tipp**: Wenn das Laufwerk nicht automatisch erscheint, oeffnen Sie **This PC** auf Ihrem gesteuerten Geraet.

    ![this pc](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/thispc.png){class="glboxshadow"}

    Suchen Sie ein Laufwerk mit dem Namen **"GLKVM"**. Nun koennen Sie die Dateien in diesem Laufwerk anzeigen, verschieben oder loeschen.

5. Wenn Sie die Freigabe beenden moechten, klicken Sie in der Symbolleiste auf **Virtual Media** und dann auf **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing1.png){class="glboxshadow"}

## Dateien vom gesteuerten Geraet abrufen

Fuehren Sie die folgenden Schritte aus, um Dateien vom gesteuerten Geraet zu empfangen.

1. Verschieben oder kopieren Sie auf dem gesteuerten Geraet die Dateien, die Sie freigeben moechten, in das Laufwerk **GLKVM**.

    Wie unten gezeigt, wurde eine Datei vom Desktop des gesteuerten Geraets auf das Laufwerk **GLKVM** verschoben.

    ![copy file to disk](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing5.png){class="glboxshadow"}
    
2. Wechseln Sie zur Comet-Konsole, klicken Sie in der Symbolleiste auf **Virtual Media** und dann auf **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing2.png){class="glboxshadow"}
    
3. Diese Datei wird anschliessend wie folgt unter **Virtual Media** angezeigt. Nun koennen Sie die Datei vom Comet auf Ihr steuerndes Geraet herunterladen.

    ![file shared](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing6.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
