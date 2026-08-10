# Pruefen, ob der USB-C-Port Ihres Geraets DP Alt Mode unterstuetzt

## Was ist DP Alt Mode?

DP Alt Mode, oder DisplayPort Alternate Mode, ist eine Funktion bestimmter USB-C-Ports. Sie ermoeglicht es, zusaetzlich zu den normalerweise uebertragenen Daten und der Stromversorgung ein hochwertiges Videosignal auszugeben.

Einfach gesagt: Ein einzelnes USB-C-Kabel kann Video von Ihrem Smartphone, Tablet oder Laptop direkt an einen Monitor, Fernseher oder Projektor uebertragen, ohne speziellen Adapter oder Dockingstation. Ohne DP Alt Mode kann der Port nur Daten uebertragen und Strom liefern. Eine Videoausgabe an ein externes Display ist dann nicht moeglich.

## Warum das wichtig ist

DP Alt Mode ist fuer **Comet Q** wichtig, da Comet Q darueber das Videosignal von Ihrem Geraet empfaengt. Wenn Ihr USB-C-Port DP Alt Mode unterstuetzt, funktioniert Comet Q direkt per Plug and Play. Wenn nicht, kann auch kein externer Display-Adapter diese Einschraenkung umgehen.

Nicht jeder USB-C-Port bietet dieselben Funktionen. Einige Ports uebertragen nur Daten und Strom, andere koennen auch Video ausgeben. Der Anschluss sieht gleich aus, die dahinterliegenden Funktionen koennen sich jedoch unterscheiden. Zwei USB-C-Ports koennen identisch aussehen und sich voellig unterschiedlich verhalten. Deshalb sollten Sie dies pruefen, bevor Sie USB-C-Display-Zubehoer kaufen.

## Allgemeine Methoden zum Pruefen von DP Alt Mode

1. **Datenblatt pruefen**.

    Suchen Sie Ihr genaues Modell auf der Website des Herstellers. Suchen Sie nach Begriffen wie DisplayPort, DP Alt Mode, video output oder Thunderbolt.

2. **Port-Markierungen pruefen**.

    Ein D-foermiges DisplayPort-Logo oder ein Thunderbolt-Blitzsymbol neben dem USB-C-Port weist auf Videoausgabe hin.

3. **Systemeinstellungen pruefen**.

    Ihr Betriebssystem kann erkennen, ob der USB-C-Port externe Displayausgabe unterstuetzt. Beachten Sie die plattformspezifischen Anweisungen unten.

    - [Auf Windows pruefen](#auf-windows-pruefen)
    - [Auf Mac pruefen](#auf-mac-pruefen)
    - [Auf Android pruefen](#auf-android-pruefen)
    - [Auf iPhone und iPad pruefen](#auf-iphone-und-ipad-pruefen)
    - [Handhelds, Tablets und andere Geraete](#handhelds-tablets-und-andere-geraete)

4. **Schnelltest durchfuehren**.

    Verbinden Sie Ihr Geraet ueber ein USB-C-auf-HDMI- oder USB-C-auf-DisplayPort-Kabel mit einem Monitor oder Fernseher. Wenn der Bildschirm gespiegelt oder erweitert wird, funktioniert DP Alt Mode ordnungsgemaess.

---

## Auf Windows pruefen

1. Druecken Sie `Win + X` und oeffnen Sie den **Device Manager**.
2. Erweitern Sie **Universal Serial Bus controllers** und suchen Sie nach Eintraegen, die *"USB4"*, *"Thunderbolt"* oder *"DisplayLink"* enthalten.
3. Alternativ oeffnen Sie **Settings** > **System** > **Display** > **Multiple displays**. Wenn Comet Q oder ein anderes Display angeschlossen ist, sollte Ihr Monitor angezeigt werden.
4. Sie koennen auch das Benutzerhandbuch Ihres Laptops oder die Produktseite des Herstellers pruefen. Suchen Sie nach *"DisplayPort over USB-C"* oder *"DP Alt Mode"*.

**Hinweis**: Wenn Ihr Laptop mehrere USB-C-Ports hat, unterstuetzen moeglicherweise nur einige davon Videoausgabe. Pruefen Sie jeden Port einzeln.

## Auf Mac pruefen

1. Klicken Sie auf das **Apple menu** > **About This Mac** > **More Info**.
2. Scrollen Sie nach unten und klicken Sie auf **System Report**.
3. Waehlen Sie unter **Hardware** die Option **Thunderbolt / USB4** oder **USB** aus.
4. Jeder unter Thunderbolt / USB4 aufgefuehrte USB-C-Port unterstuetzt DisplayPort Alt Mode standardmaessig.

**Tipp**: Alle aktuellen Macs mit USB-C- oder Thunderbolt-Ports unterstuetzen DisplayPort Alt Mode ohne zusaetzliche Konfiguration.

!!! note "Unterstuetzte Modelle"

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
        - iMac27-in. (Intel,2020)
        - iMac Pro (Intel, 2017)
    - Mac mini
        - Mac mini (M4)
        - Mac mini (M4 Pro)
        - Mac mini (M2 or M2 Pro)
        - Mac mini (M1, 2020)
        - Mac mini (Intel, 2018)
    - Mac Studio
        - Mac Studio (M4 Max)
        - Mac Studio (M3 UIitra)
        - Mac Studio (M2 Max or M2 UItra)
        - Mac Studio (M1 Max or M1 UItra, 2022)
    - Mac Pro
        - Mac Pro (M2 UItra)
        - Mac Pro (Intel, 2019)

## Auf Android pruefen

1. Oeffnen Sie die **Settings** Ihres Smartphones und suchen Sie nach *"display"*, *"HDMI"* oder *"desktop mode"*.
2. Suchen Sie nach Funktionen wie **Samsung DeX**, **Motorola Ready For**, **Huawei EasyProjection** oder *"External display"*. Wenn eine dieser Funktionen vorhanden ist, unterstuetzt der USB-C-Port Ihres Geraets DP Alt Mode.
3. Wenn Ihr Smartphone DP Alt Mode unterstuetzt, sehen Sie beim Anschliessen an einen Monitor in der Regel eine Benachrichtigung wie *"External display connected"*.
4. Sie koennen auch eine kostenlose App wie *USB Device Info* installieren, um die Port-Faehigkeiten zu pruefen.

**Hinweis**: Viele guenstige Android-Smartphones haben zwar USB-C, unterstuetzen aber keinen DP Alt Mode. Bestaetigen Sie die Unterstuetzung immer, bevor Sie Comet Q kaufen.

!!! note "Unterstuetzte Modelle am Beispiel Samsung:"

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
        - Galaxy Z Flip
        - Galaxy Z Fold2
        - Galaxy Z Fold3
        - Galaxy Z Fold4
        - Galaxy Z Fold7

## Auf iPhone und iPad pruefen

1. Die iPhone 15 Serie und neuere Modelle unterstuetzen DisplayPort Alt Mode ueber ihren USB-C-Port.
2. iPhone 14 und aeltere Modelle verwenden Lightning und sind nicht kompatibel.
3. Alle iPad-Modelle mit USB-C, einschliesslich iPad Pro, iPad Air ab der 4. Generation, iPad mini ab der 6. Generation und iPad ab der 10. Generation, unterstuetzen Videoausgabe.
4. iPads mit aelterem Lightning-Port sind nicht kompatibel.

!!! note "Unterstuetzte Modelle"

    - iPhone
        - iPhone 17 Pro
        - iPhone 17 Pro Max
        - iPhone 17
        - iPhone 16 Pro
        - iPhone 16 Pro Max
        - iPhone 16
        - iPhone 16 Plus
        - iPhone 15 Pro
        - iPhone 15 ProMax
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

## Handhelds, Tablets und andere Geraete

1. **Steam Deck**, **ROG Ally** und **Lenovo Legion Go** unterstuetzen alle DP Alt Mode.
2. **Nintendo Switch / Switch 2** unterstuetzt DP Alt Mode. So gibt das Dock das Bild an Ihren Fernseher aus.
3. **Die meisten Windows-Tablets** mit USB-C, z. B. Surface Pro 8 und neuer, werden unterstuetzt.
4. Pruefen Sie bei allen anderen Geraeten die offizielle Spezifikationsseite und suchen Sie nach Begriffen wie *"DisplayPort"*, *"Alt Mode"*, *"video output"* oder *"Thunderbolt"*.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
