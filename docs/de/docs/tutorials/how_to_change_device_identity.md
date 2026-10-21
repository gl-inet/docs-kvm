# KVM-Geräteidentität ändern {#how-to-change-kvm-device-identity}

## Was ist die KVM-Geräteidentität? {#what-is-kvm-device-identity}

Die Geräteidentität eines GL.iNet KVM ist die Kennung, über die das KVM bei der Kommunikation vom verbundenen Gerät erkannt und unterschieden wird.

In der Regel ist das KVM mit einem Type-C-Port ausgestattet, wie unten dargestellt. Dieser Port wird mit dem USB-Port des gesteuerten Geräts verbunden, um Peripheriegeräte wie Tastatur, Maus, USB-Laufwerk und Mikrofon sowie ein CD-ROM-Laufwerk zu simulieren.

![gl-rm1 type-c](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

Wenn Sie auf dem steuernden Gerät mit der Maus klicken, auf der Tastatur tippen oder das Mikrofon verwenden, werden diese Signale per Fernzugriff an das physische KVM-Gerät übertragen. Das KVM leitet sie anschließend über seinen Type-C-Port an das gesteuerte Gerät weiter.

Daher wird das KVM normalerweise als zusammengesetztes Gerät betrachtet, das mehrere an den USB-Ports des gesteuerten Geräts angeschlossene Peripheriegeräte emuliert.

![device identity principle](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/principle.png){class="glboxshadow"}

!!! Note

    Wenn Eingabemethode oder Tastaturlayout des steuernden Geräts nicht mit dem gesteuerten Gerät übereinstimmen, können einige Symbole oder Buchstaben auf anderen Tasten liegen. Dadurch kann die Ausgabe auf dem gesteuerten Gerät von der Eingabe auf dem steuernden Gerät abweichen. Weitere Informationen finden Sie [hier](../faq/keyboard_does_not_input_output_as_expected.md).

## Warum die Geräteidentität ändern? {#why-change-device-identity}

Da GL.iNet KVM für die Benutzerinteraktion mehrere Geräte kombiniert emuliert, wird es beim Anschluss an das gesteuerte Gerät als Gruppe mehrerer Geräte erkannt. Dazu gehören ein Monitor, mehrere USB-Geräte wie Maus und Tastatur sowie ein USB-Laufwerk.

Standardmäßig lautet die Geräteidentität **GLKVM**. Daher wird das KVM in den Systemeinstellungen des gesteuerten Geräts als GLKVM oder Glinet Composite Device angezeigt. Normalerweise verursacht dies keine Einschränkungen, da diese Einstellungen nur für den Benutzer selbst sichtbar sind.

![device identity default](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}
<small>(Einstellungen unter Bluetooth & devices)</small>

![speaker settings](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(Lautsprechereinstellungen)</small>

In den folgenden Szenarien kann es jedoch erforderlich sein, die KVM-Geräteidentität zu ändern.

??? "Szenario 1: Warnungen von Überwachungssoftware auf einem Büro-Computer vermeiden"

    Wenn das gesteuerte Gerät ein Büro-Computer ist, kann darauf integrierte oder installierte Überwachungssoftware ausgeführt werden. Solche Tools können KVM-Fernzugriff als ungewöhnliche Aktivität markieren, Warnungen auslösen oder sogar Meldungen an IT-Systeme senden.

    Das Ändern der KVM-Geräteidentität kann helfen, solche unnötigen Benachrichtigungen zu vermeiden, während die normale Fernsteuerungsfunktion erhalten bleibt.

??? "Szenario 2: KVM-Fernnutzung bei Bildschirmfreigaben in Online-Meetings verbergen"

    Bei Online-Meetings mit Bildschirmfreigabe können die Systemeinstellungen des gesteuerten Geräts, z. B. Bluetooth & devices, die standardmäßige Identität des KVM anzeigen. Dadurch kann für Meeting-Teilnehmer sichtbar werden, dass Sie KVM-Fernzugriff verwenden, was in manchen Situationen unerwünscht sein kann.

    Durch das Ändern der Geräteidentität bleibt das KVM auf freigegebenen Bildschirmen verborgen.

    ![screen sharing](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/screen_sharing.png){class="glboxshadow"}
    <small>(Bildschirmfreigabe)</small>

??? "Szenario 3: Nicht reagierende Maus- oder Tastatursteuerung auf dem gesteuerten Gerät beheben"

    Wenn Sie Maus und Tastatur auf dem gesteuerten Gerät nicht über KVM steuern können, versuchen Sie, die KVM-Geräteidentität zu ändern. Dadurch lassen sich Kompatibilitätsprobleme vermeiden und die Signalübertragung zwischen KVM und gesteuertem Gerät kann reibungsloser funktionieren.

## Einschränkungen der Anpassung der Geräteidentität {#limitations-of-device-identity-customization}

!!! Warning "Verhaltensbasierte Erkennungssoftware kann KVM weiterhin identifizieren"

    Unabhängig davon, wie Sie die USB-Geräteidentität anpassen, kann die USB-**Struktur** der virtualisierten Geräte wie Tastatur, Maus, Mikrofon oder Kamera für verhaltensbasierte Erkennungssoftware weiterhin auffällig wirken.

    Der grundlegende Punkt ist, dass all diese virtualisierten Peripheriegeräte zu einem **einzigen zusammengesetzten USB-Gerät** gehören. Ein zusammengesetztes Gerät, das nur Tastatur und Maus enthält, ist vergleichsweise üblich. Viele drahtlose Tastatur-/Mausempfänger, etwa Logitech Unifying, verwenden eine ähnliche Struktur. Ein einzelnes zusammengesetztes USB-Gerät, das gleichzeitig **Tastatur, Maus und Mikrofon** umfasst, ist in der Praxis jedoch sehr selten.

    Daher reicht das Ändern der Geräteidentität allein **möglicherweise nicht aus**, um von fortgeschrittener Monitoring- oder verhaltensbasierter Analysesoftware unentdeckt zu bleiben.

## KVM-Geräteidentität ändern {#how-to-change-device-identity}

### Firmware v1.10 und neuer {#firmware-v110-and-above}

1. Melden Sie sich bei Ihrem KVM an und navigieren Sie oben rechts zu **Settings**. Suchen Sie unter **USB Devices** nach **Device Identity** und passen Sie die Identität an.

    ![identity customize1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize1.png){class="glboxshadow"}

2. Klicken Sie im Pop-up-Fenster auf **Confirm**, um das Gerät neu zu starten.

    ![identity customize2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize2.png){class="glboxshadow"}

3. Nach dem Neustart ist die Device Identity in der KVM-Konsole geändert.

    ![identity customize3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize3.png){class="glboxshadow"}

4. Überprüfen Sie die Geräteidentität. Im folgenden Beispiel wird Windows 11 Pro als gesteuertes Gerät verwendet.

    Navigieren Sie auf dem gesteuerten Gerät zu **Settings** -> **Bluetooth & devices**. Die Eingabe- und Audiogeräte werden nun mit den von Ihnen festgelegten Identitäten erkannt.

    ![identity customize4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize4.png){class="glboxshadow"}

### Firmware v1.9 und älter {#firmware-v19-and-earlier}

1. Melden Sie sich bei Ihrem KVM an und navigieren Sie zu **Settings** -> **System** -> **Device Identity**. Wählen Sie in der Dropdown-Liste eine voreingestellte Identität aus.

    ![identity customize1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    Oder klicken Sie auf **Customize** und geben Sie im Pop-up-Fenster die gewünschten Parameter ein.

    ![identity customize2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. Klicken Sie im Pop-up-Fenster auf **Confirm**, um das Gerät neu zu starten.

    ![identity customize3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. Nach dem Neustart ist die Device Identity in der KVM-Konsole geändert.

    ![identity customize4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

4. Überprüfen Sie die Geräteidentität. Im folgenden Beispiel wird Windows 10 Pro als gesteuertes Gerät verwendet.

    Navigieren Sie auf dem gesteuerten Gerät zu **Settings** -> **Bluetooth & devices**. Die Eingabe- und Audiogeräte werden nun mit den von Ihnen festgelegten Identitäten erkannt.

    ![identity customize5](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
