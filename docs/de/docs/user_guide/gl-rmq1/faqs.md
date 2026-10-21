# Häufig gestellte Fragen zu Comet Q {#frequently-asked-questions-about-comet-q}

## Allgemein {#general}

1. **F: Was soll ich tun, wenn der KVM-Steuerbildschirm "Unable to Display" anzeigt, wenn Comet Q mit dem gesteuerten Gerät verbunden ist?**

    A: Das liegt daran, dass Ihr gesteuertes Gerät **USB-C DisplayPort Alt Mode** nicht unterstützt. Dadurch kann kein Videostream ausgegeben werden.

    Lesen Sie [hier](../../tutorials/how_to_check_usb-c_port_dp_alt_mode.md), wie Sie prüfen, ob Ihr Gerät DisplayPort Alt Mode unterstützt.

2. **F: Warum kann das steuernde Gerät die Tastatur für die Passworteingabe nicht anzeigen, wenn der Bildschirm des gesteuerten Geräts gesperrt ist?**

    A: Aufgrund von Sicherheitsbeschränkungen von iOS/Android blockiert das System die Seite zur Passworteingabe während der Bildschirmspiegelung oder Fernsteuerung. Sie können das Entsperrpasswort direkt am steuernden Ende eingeben, um Ihr Gerät zu entsperren.

3. **F: Warum kann der Ton nicht an das steuernde Gerät übertragen werden, wenn auf dem gesteuerten Gerät ein Sprachanruf läuft?**

    A: Dieses Problem tritt häufig bei iPhones und einigen Android-Geräten auf. Wenn auf dem gesteuerten Gerät Sprachkommunikationssoftware (z. B. WhatsApp, Microsoft Teams) für Sprachanrufe ausgeführt wird, kann der Ton aufgrund von iOS/Android-Systembeschränkungen nur über die lokalen Lautsprecher des gesteuerten Geräts ausgegeben und nicht über KVM an das steuernde Ende übertragen werden.

    **Tipp**: Medienaudio (Videos, Musik, Spiele usw.) kann normalerweise über KVM an das steuernde Ende übertragen werden, wenn keine Sprachkommunikations-Apps aktiv sind.

## iOS {#ios}

1. **F: Warum kann ich die Systemlautstärke auf iOS-Geräten nach dem Verbinden mit Comet Q nicht anpassen?**

    A: Aufgrund von iOS-Systembeschränkungen ist die native Systemlautstärkeregelung nicht mehr verfügbar, sobald ein iPhone/iPad mit einem Bildschirmspiegelungsgerät wie GL.iNet KVM verbunden ist und dieses als Audioausgabe festgelegt wurde.

2. **F: Warum zeigt das iOS-Gerät beim Streamen von Videos über Video-Apps kein lokales Videobild an?**

    A: Wenn ein iOS-Gerät mit einem Bildschirmspiegelungsgerät wie GL.iNet KVM verbunden ist, geben einige Video-Apps (z. B. YouTube, Netflix) Videos standardmäßig über **AirPlay** aus. Daher zeigt das iOS-Gerät kein lokales Videobild an. Dieses Verhalten kann auf Systemebene nicht deaktiviert werden.

    Wenn das gesteuerte Gerät Videos lokal wiedergeben soll, während es gespiegelt wird, spielen Sie die Videos stattdessen bitte über einen Webbrowser ab.

3. **F: Was soll ich tun, wenn die Bildschirmtastatur auf dem iOS-Gerät nach dem Verbinden mit Comet Q verschwindet?**

    A: Wahrscheinlich erkennt iOS Comet Q als externe physische Tastatur und blendet die native Bildschirmtastatur automatisch aus. Verwenden Sie in diesem Fall bitte die Tastatur am steuernden Gerät oder die virtuelle Tastatur in der KVM-Konsole.

    Wenn Sie die iOS-Bildschirmtastatur weiterhin verwenden müssen, navigieren Sie zu **Settings** > **Accessibility** > **Touch** > **AssistiveTouch** und aktivieren Sie dann **Show Onscreen Keyboard**.

    ![AssistiveTouch](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/assistive_touch.png){class="glboxshadow" width="360"}

4. **F: Wenn ein iPhone/iPad im Hoch- oder Querformat gespiegelt wird, weicht die Maus am steuernden Ende auch nach dem Anpassen der Bildschirmausrichtung in der KVM-Konsole weiterhin ab. Was soll ich tun?**

    A: Eine präzise Cursorverfolgung auf dem iPhone oder iPad erfordert eine perfekte Übereinstimmung zwischen der Gyroskopausrichtung des Geräts und der angezeigten Bildschirmausrichtung. Bei der Fernsteuerung kann es vorkommen, dass das System den aktuellen Gyroskopstatus nicht korrekt erkennt, wodurch ein Mausversatz entsteht.

    Um dies zu beheben, aktivieren Sie die **Portrait Orientation Lock**/**Rotation Lock** auf Ihrem iPhone/iPad, damit der Cursor präzise verfolgt wird.

    ![Portrait Lock](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/portrait_lock.png){class="glboxshadow" width="360"}
    <small>(Portrait Orientation Lock auf dem iPhone)</small>

5. **F: Warum funktioniert die Tastatur auf iOS-Geräten nicht richtig, sodass einige Tasten nicht reagieren oder sich der Mauszeiger unbeabsichtigt bewegt?**

    A: Meist ist auf dem iOS-Gerät die Funktion **Mouse Keys** aktiviert. Damit lässt sich der Mauszeiger über die Tastatur oder den Ziffernblock bewegen.

    Öffnen Sie **Settings** > **Accessibility** > **Touch** > **AssistiveTouch** > **Mouse Keys** und deaktivieren Sie Mouse Keys.

## Android {#android}

1. **F: Warum kann ich das Gerät nicht im absoluten Mausmodus steuern?**

    A: Aufgrund von Beschränkungen des Android-Betriebssystems können Android-Geräte nur im relativen Mausmodus gesteuert werden.

    Wenn Sie über die glkvm mobile APP steuern, bedecken Sie den Mauszeiger vollständig mit Ihrem Finger, um Aktionen auszuführen.

2. **F: Was soll ich tun, wenn der am steuernden Ende angezeigte Bildschirm nicht mit dem Bildschirm des gesteuerten Android-Telefons synchron ist?**

    A: Einige Android-Telefone erkennen Comet Q als erweitertes Display statt als gespiegelten Bildschirm. Ändern Sie zur Behebung bitte die Anzeigeeinstellung auf Ihrem Telefon in den Modus **Screen Mirroring**.

    Beispiel Samsung S Series:

    Navigieren Sie zu **Settings** > **Device Connections** > **Samsung DeX** > **Connected Display** und wählen Sie dann den Modus **Screen Mirroring**.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
