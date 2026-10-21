# Controleren of de USB-C-poort van uw apparaat DP Alt Mode ondersteunt {#how-to-check-if-your-devices-usb-c-port-supports-dp-alt-mode}

## Wat is DP Alt Mode? {#what-is-dp-alt-mode}

DP Alt Mode (of DisplayPort Alternate Mode) is een functie van bepaalde USB-C-poorten waarmee ze naast de gebruikelijke gegevens en stroom ook een videosignaal van hoge kwaliteit kunnen overdragen.

Eenvoudig gezegd: met één USB-C-kabel kunt u video rechtstreeks van uw telefoon, tablet of laptop naar een monitor, tv of projector sturen, zonder speciale adapter of dockingstation. Zonder DP Alt Mode kan de poort alleen gegevens overdragen en stroom leveren; er kan dan geen video naar een extern beeldscherm worden uitgevoerd.

## Waarom is dit belangrijk? {#why-it-matters}

DP Alt Mode is belangrijk voor de **Comet Q**, omdat de Comet Q hiermee de video van uw apparaat ontvangt. Het bestuurde apparaat moet native video-uitvoer via de USB-C-poort ondersteunen. Let op: een DisplayLink-adapter voegt deze mogelijkheid mogelijk niet toe voor een rechtstreekse verbinding met de Comet Q.

Niet elke USB-C-poort is hetzelfde. Sommige poorten dragen alleen gegevens en stroom over; andere kunnen ook video uitvoeren. De vorm van de connector is gelijk, maar de mogelijkheden verschillen. Twee USB-C-poorten kunnen er hetzelfde uitzien en toch heel anders werken – daarom is het verstandig dit te controleren voordat u een USB-C-beeldschermaccessoire koopt.

## Algemene methoden om DP Alt Mode te controleren {#general-methods-to-verify-dp-alt-mode}

1. **Raadpleeg het specificatieblad**.

    Zoek uw exacte model op de website van de fabrikant op. Zoek naar trefwoorden zoals DisplayPort, DP Alt Mode, video-uitvoer of Thunderbolt.

2. **Let op markeringen bij de poort**.

    Een D-vormig DisplayPort-logo of een Thunderbolt-bliksemschichtpictogram naast de USB-C-poort geeft aan dat de poort video kan uitvoeren.

3. **Controleer de systeeminstellingen**.

    Met de systeeminstellingen kunt u een aangesloten beeldscherm herkennen, maar ze laten niet altijd zien of een specifieke USB-C-poort native DP Alt Mode ondersteunt. Combineer deze controles met de specificaties van de fabrikant en een test met een rechtstreekse verbinding. Zie de instructies per platform hieronder.

    - [Controleren in Windows](#how-to-check-on-windows)
    - [Controleren op een Mac](#how-to-check-on-mac)
    - [Controleren op Android](#how-to-check-on-android)
    - [Controleren op iPhone en iPad](#how-to-check-on-iphone-and-ipad)
    - [Handhelds, tablets en andere apparaten](#handhelds-tablets-and-other-devices)

4. **Voer een snelle test uit**.

    Sluit uw apparaat aan op een monitor of tv met een USB-C-naar-HDMI/DisplayPort-kabel of -adapter die uitdrukkelijk DP Alt Mode vereist. Als het scherm uw beeld spiegelt of uitbreidt, werkt native video-uitvoer op die poort. Gebruik voor deze test geen DisplayLink-adapter.

---

## Controleren in Windows {#how-to-check-on-windows}

1. Druk op `Win + X` en open **Device Manager**.
2. Zoek naar items met *"USB4"* of *"Thunderbolt"*. Deze helpen de hardware te herkennen, maar Apparaatbeheer alleen bevestigt niet dat een specifieke poort DP Alt Mode ondersteunt.
3. Raadpleeg de gebruikershandleiding van uw laptop of de productpagina van de fabrikant voor de exacte poort – zoek naar *"DisplayPort over USB-C"* of *"DP Alt Mode"*.
4. Sluit de Comet Q rechtstreeks aan, of sluit een beeldscherm aan met een adapter die uitdrukkelijk DP Alt Mode vereist. Open **Settings** > **System** > **Display** > **Multiple displays** om te controleren of het beeldscherm wordt gedetecteerd.

**Opmerking**:

1. **DisplayLink is geen bewijs van ondersteuning voor DP Alt Mode.** DisplayLink verzendt video via USB-gegevens en kan ook via USB-A werken. Een DisplayLink-item in Apparaatbeheer of een werkend beeldscherm via een DisplayLink-dock bewijst geen native video-uitvoer via USB-C. Zie [Synaptics: USB-C with DisplayLink](https://www.synaptics.com/products/displaylink-graphics/usb-c){target="_blank"}.

2. Als uw laptop meerdere USB-C-poorten heeft, ondersteunen mogelijk niet alle poorten video-uitvoer. Controleer elke poort afzonderlijk.

## Controleren op een Mac {#how-to-check-on-mac}

1. Klik op **Apple menu** > **About This Mac** > **More Info**.
2. Scrol omlaag en klik op **System Report**.
3. Selecteer onder **Hardware** de optie **Thunderbolt / USB4** of **USB**.
4. Elke USB-C-poort die onder Thunderbolt / USB4 wordt vermeld, ondersteunt standaard DisplayPort Alt Mode.

**Tip**: Alle moderne Macs met USB-C-/Thunderbolt-poorten ondersteunen DisplayPort Alt Mode standaard.

!!! note "Ondersteunde modellen"

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
        - MacBook Pro 13-in. (Intel, twee poorten, 2020)
        - MacBook Pro 13-in. (Intel, vier poorten, 2020)
        - MacBook Pro 14-in. (M4 Max)
        - MacBook Pro 14-in. (M4 Pro)
        - MacBook Pro 14-in. (M4)
        - MacBook Pro 14-in. (M3)
        - MacBook Pro 14-in. (M3 Pro of M3 Max)
        - MacBook Pro 14-in. (M2 Pro of M2 Max, 2023)
        - MacBook Pro 14-in. (M1 Pro of M1 Max, 2021)
        - MacBook Pro 16-in. (M4 Max)
        - MacBook Pro 16-in. (M4 Pro)
        - MacBook Pro 16-in. (M3 Pro of M3 Max)
        - MacBook Pro 16-in. (M2 Pro of M2 Max, 2023)
        - MacBook Pro 16-in. (M1 Pro of M1 Max, 2021)
        - MacBook Pro 16-in. (Intel, 2019)
    - iMac
        - iMac (M4, twee poorten)
        - iMac (M4, vier poorten)
        - iMac (M3, twee poorten)
        - iMac (M3, vier poorten)
        - iMac 21.5-in. (Intel, 2019)
        - iMac 21.5-in. (Intel, 2017)
        - iMac 24-in. (M1, twee poorten, 2021)
        - iMac 24-in. (M1, vier poorten, 2021)
        - iMac 27-in. (Intel, 2020)
        - iMac Pro (Intel, 2017)
    - Mac mini
        - Mac mini (M4)
        - Mac mini (M4 Pro)
        - Mac mini (M2 of M2 Pro)
        - Mac mini (M1, 2020)
        - Mac mini (Intel, 2018)
    - Mac Studio
        - Mac Studio (M4 Max)
        - Mac Studio (M3 Ultra)
        - Mac Studio (M2 Max of M2 Ultra)
        - Mac Studio (M1 Max of M1 Ultra, 2022)
    - Mac Pro
        - Mac Pro (M2 Ultra)
        - Mac Pro (Intel, 2019)

## Controleren op Android {#how-to-check-on-android}

1. Open de **Settings** van uw telefoon en zoek naar *"display"*, *"HDMI"* of *"desktop mode"*.
2. Zoek naar functies zoals **Samsung DeX**, **Motorola Ready For**, **Huawei EasyProjection** of *"External display"*. Controleer in de documentatie van de fabrikant of het exacte model een **bekabelde USB-C-beeldschermverbinding** ondersteunt; een functie voor draadloze weergave alleen is geen bewijs van ondersteuning voor DP Alt Mode.
3. Als uw telefoon dit ondersteunt, ziet u meestal een melding zoals *"External display connected"* wanneer u een monitor aansluit.
4. Bevestig de video-uitvoer met een rechtstreekse verbinding met de Comet Q of met een beeldscherm via een adapter die DP Alt Mode vereist. Apps die alleen USB-informatie tonen, kunnen niet betrouwbaar vaststellen of native video-uitvoer wordt ondersteund.

**Opmerking**: Veel goedkope Android-telefoons hebben wel USB-C, maar geen DP Alt Mode. Controleer dit altijd voordat u een Comet Q koopt.

!!! note "Voorbeelden van Samsung-apparaten met bekabelde beelduitvoer"

    De onderstaande Samsung-apparaten zijn gecontroleerd aan de hand van [Samsung's DeX compatibility information](https://www.samsung.com/us/support/answer/ANS10001955/){target="_blank"}.

    - Galaxy A90 5G
    - Galaxy Book
    - Galaxy Fold
    - Galaxy Note
        - Galaxy Note 8
        - Galaxy Note 9
        - Galaxy Note 10-serie
        - Galaxy Note20-serie
    - Galaxy S
        - Galaxy Tab S7 / 7+
        - Galaxy Tab S8 / 8+ / S8 Ultra
        - Galaxy S8 en S8+
        - Galaxy S9 en S9+
        - Galaxy S10-serie
        - Galaxy S20-serie
        - Galaxy S21-serie
        - Galaxy S22-serie
        - Galaxy S23-serie
        - Galaxy S24-serie
        - Galaxy S25-serie
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

## Controleren op iPhone en iPad {#how-to-check-on-iphone-and-ipad}

1. De iPhone 15-serie en nieuwer (behalve iPhone 16e en iPhone 17e) ondersteunen DisplayPort Alt Mode via de USB-C-poort. Raadpleeg [Apple's display connection documentation](https://support.apple.com/en-ie/105099#displays){target="_blank"} voor uw exacte model.
2. iPhone 14 en eerder gebruiken Lightning en zijn niet compatibel.
3. Alle iPad-modellen met USB-C (iPad Pro, iPad Air 4e generatie en nieuwer, iPad mini 6e generatie en nieuwer, iPad 10e generatie en nieuwer) ondersteunen video-uitvoer.
4. iPads met de oudere Lightning-poort zijn niet compatibel.

!!! note "Voorbeelden van modellen met video-uitvoer via USB-C"

    De onderstaande iPhones zijn gecontroleerd aan de hand van [Apple's external-display documentation](https://support.apple.com/en-ie/105099#displays){target="_blank"}.

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
        - iPad (10e generatie)
    - iPad mini
        - iPad mini (6e generatie)
        - iPad mini (A17 Pro)
    - iPad Air
        - iPad Air (5e generatie)
        - iPad Air (4e generatie)
        - iPad Air 11-inch (M4)
        - iPad Air 11-inch (M3)
        - iPad Air 11-inch (M2)
        - iPad Air 13-inch (M4)
        - iPad Air 13‑inch (M3)
        - iPad Air 13-inch (M2)
    - iPad Pro
        - iPad Pro 11‑inch (M5)
        - iPad Pro 11‑inch (M4)
        - iPad Pro 11-inch (4e generatie)
        - iPad Pro 11-inch (3e generatie)
        - iPad Pro 12.9-inch (5e generatie)
        - iPad Pro 12.9-inch (6e generatie)
        - iPad Pro 13‑inch (M5)
        - iPad Pro 13‑inch (M4)

## Handhelds, tablets en andere apparaten {#handhelds-tablets-and-other-devices}

1. **Steam Deck**, **ROG Ally**, **Lenovo Legion Go** – ondersteunen allemaal DP Alt Mode.
2. **De meeste Windows-tablets** met USB-C (Surface Pro 8 en nieuwer enzovoort) – ondersteund.
3. Controleer voor andere apparaten de officiële specificatiepagina en zoek naar de trefwoorden *"DisplayPort"*, *"Alt Mode"*, *"video output"* of *"Thunderbolt"*.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
