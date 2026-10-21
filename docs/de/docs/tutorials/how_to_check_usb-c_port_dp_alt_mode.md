# Prüfen, ob der USB-C-Port Ihres Geräts DP Alt Mode unterstützt {#how-to-check-if-your-devices-usb-c-port-supports-dp-alt-mode}

## Was ist DP Alt Mode? {#what-is-dp-alt-mode}

DP Alt Mode, oder DisplayPort Alternate Mode, ist eine Funktion bestimmter USB-C-Ports. Sie ermöglicht es, zusätzlich zu den normalerweise übertragenen Daten und der Stromversorgung ein hochwertiges Videosignal auszugeben.

Einfach gesagt: Ein einzelnes USB-C-Kabel kann Video von Ihrem Smartphone, Tablet oder Laptop direkt an einen Monitor, Fernseher oder Projektor übertragen, ohne speziellen Adapter oder Dockingstation. Ohne DP Alt Mode kann der Port nur Daten übertragen und Strom liefern. Eine Videoausgabe an ein externes Display ist dann nicht möglich.

## Warum das wichtig ist {#why-it-matters}

DP Alt Mode ist für **Comet Q** wichtig, da Comet Q darüber das Videosignal von Ihrem Gerät empfängt. Das gesteuerte Gerät muss die native Videoausgabe über seinen USB-C-Port unterstützen. Beachten Sie, dass ein DisplayLink-Adapter diese Fähigkeit für eine direkte Verbindung mit Comet Q möglicherweise nicht bereitstellen kann.

Nicht jeder USB-C-Port bietet dieselben Funktionen. Einige Ports übertragen nur Daten und Strom, andere können auch Video ausgeben. Der Anschluss sieht gleich aus, die dahinterliegenden Funktionen können sich jedoch unterscheiden. Zwei USB-C-Ports können identisch aussehen und sich völlig unterschiedlich verhalten. Deshalb sollten Sie dies prüfen, bevor Sie USB-C-Display-Zubehör kaufen.

## Allgemeine Methoden zum Prüfen von DP Alt Mode {#general-methods-to-verify-dp-alt-mode}

1. **Datenblatt prüfen**.

    Suchen Sie Ihr genaues Modell auf der Website des Herstellers. Suchen Sie nach Begriffen wie DisplayPort, DP Alt Mode, video output oder Thunderbolt.

2. **Port-Markierungen prüfen**.

    Ein D-förmiges DisplayPort-Logo oder ein Thunderbolt-Blitzsymbol neben dem USB-C-Port weist auf Videoausgabe hin.

3. **Systemeinstellungen prüfen**.

    Die Systemeinstellungen können helfen, ein angeschlossenes Display zu erkennen. Sie belegen jedoch nicht immer, ob ein bestimmter USB-C-Port natives DP Alt Mode unterstützt. Ziehen Sie zusätzlich die Herstellerangaben heran und testen Sie eine direkte Verbindung. Beachten Sie die plattformspezifischen Anweisungen unten.

    - [Auf Windows prüfen](#how-to-check-on-windows)
    - [Auf Mac prüfen](#how-to-check-on-mac)
    - [Auf Android prüfen](#how-to-check-on-android)
    - [Auf iPhone und iPad prüfen](#how-to-check-on-iphone-and-ipad)
    - [Handhelds, Tablets und andere Geräte](#handhelds-tablets-and-other-devices)

4. **Schnelltest durchführen**.

    Verbinden Sie Ihr Gerät über ein USB-C-auf-HDMI- oder USB-C-auf-DisplayPort-Kabel bzw. einen Adapter, der ausdrücklich DP Alt Mode voraussetzt, mit einem Monitor oder Fernseher. Wenn der Bildschirm gespiegelt oder erweitert wird, funktioniert die native Videoausgabe an diesem Port. Verwenden Sie für diesen Test keinen DisplayLink-Adapter.

---

## Auf Windows prüfen {#how-to-check-on-windows}

1. Drücken Sie `Win + X` und öffnen Sie den **Device Manager**.
2. Suchen Sie nach Einträgen mit *"USB4"* oder *"Thunderbolt"*. Diese helfen bei der Identifizierung der Hardware, aber der Device Manager allein bestätigt keine DP-Alt-Mode-Unterstützung für einen bestimmten Port.
3. Prüfen Sie im Benutzerhandbuch Ihres Laptops oder auf der Produktseite des Herstellers die Angaben zum jeweiligen Port. Suchen Sie nach *"DisplayPort over USB-C"* oder *"DP Alt Mode"*.
4. Schließen Sie Comet Q direkt an oder verbinden Sie ein Display über einen Adapter, der ausdrücklich DP Alt Mode voraussetzt. Öffnen Sie **Settings** > **System** > **Display** > **Multiple displays**, um zu prüfen, ob das Display erkannt wird.

**Hinweis**:

1. **DisplayLink ist kein Nachweis für DP-Alt-Mode-Unterstützung.** DisplayLink überträgt Video über USB-Daten und funktioniert auch über USB-A. Ein DisplayLink-Eintrag im Device Manager oder ein funktionierendes Display an einem DisplayLink-Dock belegt keine native USB-C-Videoausgabe. Siehe [Synaptics: USB-C mit DisplayLink](https://www.synaptics.com/products/displaylink-graphics/usb-c){target="_blank"}.

2. Wenn Ihr Laptop mehrere USB-C-Ports hat, unterstützen möglicherweise nur einige davon die Videoausgabe. Prüfen Sie jeden Port einzeln.

## Auf Mac prüfen {#how-to-check-on-mac}

1. Klicken Sie auf das **Apple menu** > **About This Mac** > **More Info**.
2. Scrollen Sie nach unten und klicken Sie auf **System Report**.
3. Wählen Sie unter **Hardware** die Option **Thunderbolt / USB4** oder **USB** aus.
4. Jeder unter Thunderbolt / USB4 aufgeführte USB-C-Port unterstützt DisplayPort Alt Mode standardmäßig.

**Tipp**: Alle aktuellen Macs mit USB-C- oder Thunderbolt-Ports unterstützen DisplayPort Alt Mode ohne zusätzliche Konfiguration.

!!! note "Unterstützte Modelle"

    - MacBook Neo (A18 Pro)
    - MacBook Air
        - MacBook Air 13-in. (M5)
        - MacBook Air 15-in. (M5)
        - MacBook Air 13-in. (M4)
        - MacBook Air 13-in. (M3)
        - MacBook Air 13-in. (M2)
        - MacBook Air 13-in. (M1, 2020)
        - MacBook Air 15-in. (M4)
        - MacBook Air 15-in. (M3)
        - MacBook Air 15-in. (M2, 2023)
        - MacBook Air (Intel, 2020)
    - MacBook Pro
        - MacBook Pro 14-in. (M5)
        - MacBook Pro 14-in. (M5 Pro)
        - MacBook Pro 14-in. (M5 Max)
        - MacBook Pro 16-in. (M5 Pro)
        - MacBook Pro 16-in. (M5 Max)
        - MacBook Pro 13-in. (M2, 2022)
        - MacBook Pro 13-in. (M1, 2020)
        - MacBook Pro 13-in. (Intel, two ports, 2020)
        - MacBook Pro 13-in. (Intel, four ports, 2020)
        - MacBook Pro 14-in. (M4 Max)
        - MacBook Pro 14-in. (M4 Pro)
        - MacBook Pro 14-in. (M4)
        - MacBook Pro 14-in. (M3)
        - MacBook Pro 14-in. (M3 Pro or M3 Max)
        - MacBook Pro 14-in. (M2 Pro or M2 Max, 2023)
        - MacBook Pro 14-in. (M1 Pro or M1 Max, 2021)
        - MacBook Pro 16-in. (M4 Max)
        - MacBook Pro 16-in. (M4 Pro)
        - MacBook Pro 16-in. (M3 Pro or M3 Max)
        - MacBook Pro 16-in. (M2 Pro or M2 Max, 2023)
        - MacBook Pro 16-in. (M1 Pro or M1 Max, 2021)
        - MacBook Pro 16-in. (Intel, 2019)
    - iMac
        - iMac (M4, two ports)
        - iMac (M4, four ports)
        - iMac (M3, two ports)
        - iMac (M3, four ports)
        - iMac 21.5-in. (Intel, 2019)
        - iMac 21.5-in. (Intel, 2017)
        - iMac 24-in. (M1, two ports, 2021)
        - iMac 24-in. (M1, four ports, 2021)
        - iMac 27-in. (Intel, 2020)
        - iMac Pro (Intel, 2017)
    - Mac mini
        - Mac mini (M4)
        - Mac mini (M4 Pro)
        - Mac mini (M2 or M2 Pro)
        - Mac mini (M1, 2020)
        - Mac mini (Intel, 2018)
    - Mac Studio
        - Mac Studio (M4 Max)
        - Mac Studio (M3 Ultra)
        - Mac Studio (M2 Max or M2 Ultra)
        - Mac Studio (M1 Max or M1 Ultra, 2022)
    - Mac Pro
        - Mac Pro (M2 Ultra)
        - Mac Pro (Intel, 2019)

## Auf Android prüfen {#how-to-check-on-android}

1. Öffnen Sie die **Settings** Ihres Smartphones und suchen Sie nach *"display"*, *"HDMI"* oder *"desktop mode"*.
2. Suchen Sie nach Funktionen wie **Samsung DeX**, **Motorola Ready For**, **Huawei EasyProjection** oder *"External display"*. Prüfen Sie in der Herstellerdokumentation, ob das genaue Modell eine **kabelgebundene USB-C-Displayverbindung** unterstützt. Eine drahtlose Displayfunktion allein belegt keine DP-Alt-Mode-Unterstützung.
3. Wenn Ihr Smartphone DP Alt Mode unterstützt, sehen Sie beim Anschließen an einen Monitor in der Regel eine Benachrichtigung wie *"External display connected"*.
4. Bestätigen Sie die Videoausgabe durch eine direkte Verbindung mit Comet Q oder einem Display über einen Adapter, der DP Alt Mode voraussetzt. Apps zur Anzeige von USB-Informationen allein können die native Videoausgabe nicht zuverlässig nachweisen.

**Hinweis**: Viele günstige Android-Smartphones haben zwar USB-C, unterstützen aber keinen DP Alt Mode. Bestätigen Sie die Unterstützung immer, bevor Sie Comet Q kaufen.

!!! note "Beispiele für Samsung-Geräte mit kabelgebundener Videoausgabe"

    Die folgenden Samsung-Einträge wurden anhand der [DeX-Kompatibilitätsinformationen von Samsung](https://www.samsung.com/us/support/answer/ANS10001955/){target="_blank"} geprüft.

    - Galaxy A90 5G
    - Galaxy Book
    - Galaxy Fold
    - Galaxy Note
        - Galaxy Note 8
        - Galaxy Note 9
        - Galaxy Note 10 range
        - Galaxy Note20 range
    - Galaxy S
        - Galaxy Tab S7 / 7+
        - Galaxy Tab S8 / 8+ / S8 Ultra
        - Galaxy S8 and S8+
        - Galaxy S9 and S9+
        - Galaxy S10 range
        - Galaxy S20 range
        - Galaxy S21 range
        - Galaxy S22 range
        - Galaxy S23 range
        - Galaxy S24 range
        - Galaxy S25 range
    - Galaxy Tab
        - Galaxy Tab S4
        - Galaxy Tab S5e
        - Galaxy Tab S6
    - Galaxy Z
        - Galaxy Z Flip7
        - Galaxy Z Flip8
        - Galaxy Z Fold2
        - Galaxy Z Fold3
        - Galaxy Z Fold4
        - Galaxy Z Fold7

## Auf iPhone und iPad prüfen {#how-to-check-on-iphone-and-ipad}

1. Die iPhone-15-Serie und neuere Modelle (außer iPhone 16e und iPhone 17e) unterstützen DisplayPort Alt Mode über ihren USB-C-Port. Prüfen Sie die Angaben zu Ihrem genauen Modell in [Apples Dokumentation zum Anschluss von Displays](https://support.apple.com/en-ie/105099#displays){target="_blank"}.
2. iPhone 14 und ältere Modelle verwenden Lightning und sind nicht kompatibel.
3. Alle iPad-Modelle mit USB-C, einschließlich iPad Pro, iPad Air ab der 4. Generation, iPad mini ab der 6. Generation und iPad ab der 10. Generation, unterstützen Videoausgabe.
4. iPads mit älterem Lightning-Port sind nicht kompatibel.

!!! note "Beispiele für Modelle mit USB-C-Videoausgabe"

    Die folgenden iPhone-Einträge wurden anhand von [Apples Dokumentation zu externen Displays](https://support.apple.com/en-ie/105099#displays){target="_blank"} geprüft.

    - iPhone
        - iPhone 18 Pro
        - iPhone 18 Pro Max
        - iPhone 17 Pro
        - iPhone 17 Pro Max
        - iPhone 17
        - iPhone 16 Pro
        - iPhone 16 Pro Max
        - iPhone 16
        - iPhone 16 Plus
        - iPhone 15 Pro
        - iPhone 15 Pro Max
        - iPhone 15
        - iPhone 15 Plus
    - iPad
        - iPad (A16)
        - iPad (10th generation)
    - iPad mini
        - iPad mini (6th generation)
        - iPad mini (A17 Pro)
    - iPad Air
        - iPad Air (5th generation)
        - iPad Air (4th generation)
        - iPad Air 11-inch (M4)
        - iPad Air 11-inch (M3)
        - iPad Air 11-inch (M2)
        - iPad Air 13-inch (M4)
        - iPad Air 13‑inch (M3)
        - iPad Air 13-inch (M2)
    - iPad Pro
        - iPad Pro 11‑inch (M5)
        - iPad Pro 11‑inch (M4)
        - iPad Pro 11-inch (4th generation)
        - iPad Pro 11-inch (3rd generation)
        - iPad Pro 12.9-inch (5th generation)
        - iPad Pro 12.9-inch (6th generation)
        - iPad Pro 13‑inch (M5)
        - iPad Pro 13‑inch (M4)

## Handhelds, Tablets und andere Geräte {#handhelds-tablets-and-other-devices}

1. **Steam Deck**, **ROG Ally** und **Lenovo Legion Go** unterstützen alle DP Alt Mode.
2. **Die meisten Windows-Tablets** mit USB-C, z. B. Surface Pro 8 und neuer, werden unterstützt.
3. Prüfen Sie bei allen anderen Geräten die offizielle Spezifikationsseite und suchen Sie nach Begriffen wie *"DisplayPort"*, *"Alt Mode"*, *"video output"* oder *"Thunderbolt"*.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
