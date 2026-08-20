# Haeufig gestellte Fragen zu Comet Q

## Allgemein

1. **F: Was soll ich tun, wenn der KVM-Steuerbildschirm "Unable to Display" anzeigt, wenn Comet Q mit dem gesteuerten Geraet verbunden ist?**

    A: Das liegt daran, dass Ihr gesteuertes Geraet **USB-C DisplayPort Alt Mode** nicht unterstuetzt. Dadurch kann kein Videostream ausgegeben werden.

    Lesen Sie [hier](../../tutorials/how_to_check_usb-c_port_dp_alt_mode.md), wie Sie pruefen, ob Ihr Geraet DisplayPort Alt Mode unterstuetzt.

2. **F: Warum kann das steuernde Geraet die Tastatur fuer die Passworteingabe nicht anzeigen, wenn der Bildschirm des gesteuerten Geraets gesperrt ist?**

    A: Aufgrund von Sicherheitsbeschraenkungen von iOS/Android blockiert das System die Seite zur Passworteingabe waehrend der Bildschirmspiegelung oder Fernsteuerung. Sie koennen das Entsperrpasswort direkt am steuernden Ende eingeben, um Ihr Geraet zu entsperren.

3. **F: Warum kann der Ton nicht an das steuernde Geraet uebertragen werden, wenn auf dem gesteuerten Geraet ein Sprachanruf laeuft?**

    A: Dieses Problem tritt haeufig bei iPhones und einigen Android-Geraeten auf. Wenn auf dem gesteuerten Geraet Sprachkommunikationssoftware (z. B. WhatsApp, Microsoft Teams) fuer Sprachanrufe ausgefuehrt wird, kann der Ton aufgrund von iOS/Android-Systembeschraenkungen nur ueber die lokalen Lautsprecher des gesteuerten Geraets ausgegeben und nicht ueber KVM an das steuernde Ende uebertragen werden.

    **Tipp**: Medienaudio (Videos, Musik, Spiele usw.) kann normalerweise ueber KVM an das steuernde Ende uebertragen werden, wenn keine Sprachkommunikations-Apps aktiv sind.

## iOS

1. **F: Warum kann ich die Systemlautstaerke auf iOS-Geraeten nach dem Verbinden mit Comet Q nicht anpassen?**

    A: Aufgrund von iOS-Systembeschraenkungen ist die native Systemlautstaerkeregelung nicht mehr verfuegbar, sobald ein iPhone/iPad mit einem Bildschirmspiegelungsgeraet wie GL.iNet KVM verbunden ist und dieses als Audioausgabe festgelegt wurde.

2. **F: Warum zeigt das iOS-Geraet beim Streamen von Videos ueber Video-Apps kein lokales Videobild an?**

    A: Wenn ein iOS-Geraet mit einem Bildschirmspiegelungsgeraet wie GL.iNet KVM verbunden ist, geben einige Video-Apps (z. B. YouTube, Netflix) Videos standardmaessig ueber **AirPlay** aus. Daher zeigt das iOS-Geraet kein lokales Videobild an. Dieses Verhalten kann auf Systemebene nicht deaktiviert werden.

    Wenn das gesteuerte Geraet Videos lokal wiedergeben soll, waehrend es gespiegelt wird, spielen Sie die Videos stattdessen bitte ueber einen Webbrowser ab.

3. **F: Was soll ich tun, wenn die Bildschirmtastatur auf dem iOS-Geraet nach dem Verbinden mit Comet Q verschwindet?**

    A: Wahrscheinlich erkennt iOS Comet Q als externe physische Tastatur und blendet die native Bildschirmtastatur automatisch aus. Verwenden Sie in diesem Fall bitte die Tastatur am steuernden Geraet oder die virtuelle Tastatur in der KVM-Konsole.

    Wenn Sie die iOS-Bildschirmtastatur weiterhin verwenden muessen, navigieren Sie zu **Settings** > **Accessibility** > **Touch** > **AssistiveTouch** und aktivieren Sie dann **Show Onscreen Keyboard**.

    ![AssistiveTouch](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/assistive_touch.png){class="glboxshadow" width="360"}

4. **F: Wenn ein iPhone/iPad im Hoch- oder Querformat gespiegelt wird, weicht die Maus am steuernden Ende auch nach dem Anpassen der Bildschirmausrichtung in der KVM-Konsole weiterhin ab. Was soll ich tun?**

    A: Eine praezise Cursorverfolgung auf dem iPhone oder iPad erfordert eine perfekte Uebereinstimmung zwischen der Gyroskopausrichtung des Geraets und der angezeigten Bildschirmausrichtung. Bei der Fernsteuerung kann es vorkommen, dass das System den aktuellen Gyroskopstatus nicht korrekt erkennt, wodurch ein Mausversatz entsteht.

    Um dies zu beheben, aktivieren Sie die **Portrait Orientation Lock**/**Rotation Lock** auf Ihrem iPhone/iPad, damit der Cursor praezise verfolgt wird.

    ![Portrait Lock](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/portrait_lock.png){class="glboxshadow" width="360"}
    <small>(Portrait Orientation Lock auf dem iPhone)</small>

## Android

1. **F: Warum kann ich das Geraet nicht im absoluten Mausmodus steuern?**

    A: Aufgrund von Beschraenkungen des Android-Betriebssystems koennen Android-Geraete nur im relativen Mausmodus gesteuert werden.

    Wenn Sie ueber die glkvm mobile APP steuern, bedecken Sie den Mauszeiger vollstaendig mit Ihrem Finger, um Aktionen auszufuehren.

2. **F: Was soll ich tun, wenn der am steuernden Ende angezeigte Bildschirm nicht mit dem Bildschirm des gesteuerten Android-Telefons synchron ist?**

    A: Einige Android-Telefone erkennen Comet Q als erweitertes Display statt als gespiegelten Bildschirm. Aendern Sie zur Behebung bitte die Anzeigeeinstellung auf Ihrem Telefon in den Modus **Screen Mirroring**.

    Beispiel Samsung S Series:

    Navigieren Sie zu **Settings** > **Device Connections** > **Samsung DeX** > **Connected Display** und waehlen Sie dann den Modus **Screen Mirroring**.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
