# KVM-Geraeteidentitaet aendern

## Was ist die KVM-Geraeteidentitaet?

Die Geraeteidentitaet eines GL.iNet KVM ist die Kennung, ueber die das KVM bei der Kommunikation vom verbundenen Geraet erkannt und unterschieden wird.

Da GL.iNet KVM fuer die Benutzerinteraktion mehrere Geraete kombiniert emuliert, wird es beim Anschluss an das gesteuerte Geraet als Gruppe mehrerer Geraete erkannt. Dazu gehoeren ein Monitor, mehrere USB-Geraete wie Maus und Tastatur sowie ein USB-Laufwerk.

Standardmaessig lautet die Geraeteidentitaet **GLKVM**. Sie finden sie in der KVM-Konsole unter **Settings** -> **System**.

![device identity](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/device_identity.png){class="glboxshadow"}

In der Regel ist das KVM mit einem Type-C-Port ausgestattet, wie unten dargestellt. Dieser Port wird mit dem USB-Port des gesteuerten Geraets verbunden, um Peripheriegeraete wie Tastatur, Maus, USB-Laufwerk und Mikrofon sowie ein CD-ROM-Laufwerk zu simulieren.

![gl-rm1 type-c](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

Wenn der Benutzer auf dem steuernden Geraet mit der Maus klickt, auf der Tastatur tippt oder das Mikrofon verwendet, werden diese Signale per Fernzugriff an das physische KVM-Geraet uebertragen. Das KVM leitet sie anschliessend ueber seinen Type-C-Port an das gesteuerte Geraet weiter. Daher wird das KVM normalerweise als zusammengesetztes Geraet betrachtet, das mehrere an den USB-Ports des gesteuerten Geraets angeschlossene Peripheriegeraete emuliert.

!!! Note

    Wenn Eingabemethode oder Tastaturlayout des steuernden Geraets nicht mit dem gesteuerten Geraet uebereinstimmen, koennen einige Symbole oder Buchstaben auf anderen Tasten liegen. Dadurch kann die Ausgabe auf dem gesteuerten Geraet von der Eingabe auf dem steuernden Geraet abweichen. Weitere Informationen finden Sie [hier](../faq/keyboard_does_not_input_output_as_expected.md).

Da die Geraeteidentitaet von GL.iNet KVM standardmaessig GLKVM lautet, wird es in den Systemeinstellungen des gesteuerten Geraets, z. B. unter Bluetooth & devices, als GLKVM oder Glinet Composite Device angezeigt.

![device identity default](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}

## Warum die Geraeteidentitaet aendern?

Standardmaessig wird GL.iNet KVM vom gesteuerten Geraet als zusammengesetztes Geraet erkannt, das Peripheriegeraete wie Tastatur, Maus, Mikrofon und Monitor emuliert. Normalerweise verursacht dies keine Einschraenkungen, da diese Einstellungen nur fuer den Benutzer selbst sichtbar sind.

![mic settings](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/mic.png){class="glboxshadow"}
<small>(Mikrofoneinstellungen)</small>

![speaker settings](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(Lautsprechereinstellungen)</small>

In den folgenden Szenarien kann es jedoch erforderlich sein, die KVM-Geraeteidentitaet zu aendern.

??? "Szenario 1: Warnungen von Ueberwachungssoftware auf einem Buero-Computer vermeiden"

    Wenn das gesteuerte Geraet ein Buero-Computer ist, kann darauf integrierte oder installierte Ueberwachungssoftware ausgefuehrt werden. Solche Tools koennen KVM-Fernzugriff als ungewoehnliche Aktivitaet markieren, Warnungen ausloesen oder sogar Meldungen an IT-Systeme senden.

    Das Aendern der KVM-Geraeteidentitaet kann helfen, solche unnoetigen Benachrichtigungen zu vermeiden, waehrend die normale Fernsteuerungsfunktion erhalten bleibt.

??? "Szenario 2: KVM-Fernnutzung bei Bildschirmfreigaben in Online-Meetings verbergen"

    Bei Online-Meetings mit Bildschirmfreigabe koennen die Systemeinstellungen des gesteuerten Geraets, z. B. Bluetooth & devices, die standardmaessige Identitaet des KVM anzeigen. Dadurch kann fuer Meeting-Teilnehmer sichtbar werden, dass Sie KVM-Fernzugriff verwenden, was in manchen Situationen unerwuenscht sein kann.

    Durch das Aendern der Geraeteidentitaet bleibt das KVM auf freigegebenen Bildschirmen verborgen.

    ![screen sharing](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/screen_sharing.png){class="glboxshadow"}
    <small>(Bildschirmfreigabe)</small>

??? "Szenario 3: Nicht reagierende Maus- oder Tastatursteuerung auf dem gesteuerten Geraet beheben"

    Wenn Sie Maus und Tastatur auf dem gesteuerten Geraet nicht ueber KVM steuern koennen, versuchen Sie, die KVM-Geraeteidentitaet zu aendern. Dadurch lassen sich Kompatibilitaetsprobleme vermeiden und die Signaluebertragung zwischen KVM und gesteuertem Geraet kann reibungsloser funktionieren.

## Einschraenkungen der Anpassung der Geraeteidentitaet

!!! Warning "Verhaltensbasierte Erkennungssoftware kann KVM weiterhin identifizieren"

    Unabhaengig davon, wie Sie die USB-Geraeteidentitaet anpassen, kann die USB-**Struktur** der virtualisierten Geraete wie Tastatur, Maus, Mikrofon oder Kamera fuer verhaltensbasierte Erkennungssoftware weiterhin auffaellig wirken.

    Der grundlegende Punkt ist, dass all diese virtualisierten Peripheriegeraete zu einem **einzigen zusammengesetzten USB-Geraet** gehoeren. Ein zusammengesetztes Geraet, das nur Tastatur und Maus enthaelt, ist vergleichsweise ueblich. Viele drahtlose Tastatur-/Mausempfaenger, etwa Logitech Unifying, verwenden eine aehnliche Struktur. Ein einzelnes zusammengesetztes USB-Geraet, das gleichzeitig **Tastatur, Maus und Mikrofon** umfasst, ist in der Praxis jedoch sehr selten.

    Daher reicht das Aendern der Geraeteidentitaet allein **moeglicherweise nicht aus**, um von fortgeschrittener Monitoring- oder verhaltensbasierter Analysesoftware unentdeckt zu bleiben.

## KVM-Geraeteidentitaet aendern

1. Melden Sie sich bei Ihrem KVM an und navigieren Sie zu **Settings** -> **System** -> **Device Identity**. Waehlen Sie in der Dropdown-Liste eine voreingestellte Identitaet aus.

    ![customize1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    Oder klicken Sie auf **Customize** und geben Sie im Pop-up-Fenster die gewuenschten Parameter ein.

    ![customize2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. Nach der Auswahl erscheint ein Pop-up-Fenster, das zum Neustart auffordert. Klicken Sie auf **Confirm**, um neu zu starten.

    ![customize3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. Nach dem Neustart ist die Device Identity in der KVM-Konsole auf die geaenderte Identitaet gesetzt.

    ![customize4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

    Greifen Sie ueber KVM auf Ihr gesteuertes Geraet zu und navigieren Sie zu **Settings** -> **Bluetooth & devices**. Im Beispiel wird Windows 10 Pro verwendet. Die Eingabegeraete (Tastatur und Maus), das Audiogeraet (Mikrofon) und die Anzeige (Monitor) werden nun als die von Ihnen festgelegten benutzerdefinierten Geraete erkannt, nicht mehr als standardmaessiges GLKVM.

    ![customize5](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
