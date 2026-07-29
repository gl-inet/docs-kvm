# Was tun, wenn der Remote-Bildschirm die BIOS-Oberfläche nicht anzeigt

Wenn beim Zugriff auf das gesteuerte Gerät über KVM auf dem Remote-Bildschirm die BIOS-Oberfläche nicht angezeigt wird (z. B. No HDMI Signal), liegt der Grund darin, dass die BIOS-Oberfläche normalerweise nur auf dem primären Monitor ausgegeben wird. Hier einige Vorschläge.

## Laptop

Wenn das gesteuerte Gerät ein Laptop ist, dient der integrierte Bildschirm als primäre Anzeige. Daher kann das externe KVM die BIOS-Oberfläche nicht darstellen.

## Desktop

Verbinden Sie bei Desktop-Geräten den primären Monitor mit dem DisplayPort-Anschluss, sofern vorhanden. Der Grund ist, dass die meisten Grafikkarten und Mainboards beim Start die DP-Ausgabe gegenüber HDMI priorisieren.

Führen Sie die folgenden Methoden aus, damit die BIOS-Oberfläche über KVM sichtbar wird.

- Wechseln Sie zwischen verschiedenen Monitoranschlüssen. Verbinden Sie GL.iNet KVM mit dem Anschluss, der auf Ihrem Computer als primärer Anzeigeausgang festgelegt ist.

- Verwenden Sie einen 1-zu-2-HDMI-Splitter (nicht im Lieferumfang enthalten), um das Signal der primären Anzeige auf das KVM-Gerät zu duplizieren.

> **Hinweis**: Dieses Problem kann auch auftreten, wenn das gesteuerte Gerät in **Windows PE** startet, da BIOS-Signale nur an den primären Monitor übertragen werden und auf dem Remote-KVM-Bildschirm nicht angezeigt werden können.

> Es wird empfohlen, mit einem zusätzlichen Monitor zu testen. Wenn die sekundäre Anzeige weiterhin kein Signal empfängt, kann das KVM den BIOS-Bildschirm nicht erfassen. Sie können die Anzeigetreiber manuell in das WinPE-System integrieren oder installieren, um dieses Problem zu beheben.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
