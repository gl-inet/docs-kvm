# Så kontrollerar du om enhetens USB-C-port stöder DP Alt Mode {#how-to-check-if-your-devices-usb-c-port-supports-dp-alt-mode}

## Vad är DP Alt Mode? {#what-is-dp-alt-mode}

DP Alt Mode (DisplayPort Alternate Mode) är en funktion i vissa USB-C-portar som gör att de kan överföra en videosignal av hög kvalitet – utöver data och ström som de normalt hanterar.

Enkelt uttryckt: med funktionen kan en enda USB-C-kabel överföra video från din telefon, surfplatta eller bärbara dator direkt till en skärm, tv eller projektor – utan någon särskild adapter eller dockningsstation. Utan DP Alt Mode kan porten bara överföra data och leverera ström. Den kan inte mata ut video till en extern skärm.

## Varför det spelar roll {#why-it-matters}

DP Alt Mode är viktigt för **Comet Q**, eftersom Comet Q är beroende av funktionen för att ta emot video från din enhet. Den styrda enheten måste stödja inbyggd videoutgång via sin USB-C-port. Observera att en DisplayLink-adapter inte nödvändigtvis tillför den här funktionen för en direktanslutning till Comet Q.

Alla USB-C-portar är inte likadana. Vissa överför bara data och ström, medan andra även kan mata ut video. Kontakten har samma form, men funktionerna bakom den skiljer sig. Två USB-C-portar kan se identiska ut men fungera helt olika – därför lönar det sig att kontrollera innan du köper ett USB-C-tillbehör för bildvisning.

## Allmänna metoder för att verifiera DP Alt Mode {#general-methods-to-verify-dp-alt-mode}

1. **Kontrollera specifikationerna**.

    Slå upp din exakta modell på tillverkarens webbplats. Sök efter nyckelord som DisplayPort, DP Alt Mode, videoutgång eller Thunderbolt.

2. **Leta efter märkningar vid porten**.

    En D-formad DisplayPort-logotyp eller en Thunderbolt-blixtsymbol bredvid USB-C-porten anger att porten kan mata ut video.

3. **Kontrollera systeminställningarna**.

    Systeminställningarna kan hjälpa dig att identifiera en ansluten skärm, men de visar inte alltid om en viss USB-C-port stöder inbyggt DP Alt Mode. Kombinera kontrollerna med tillverkarens specifikationer och ett test med direktanslutning. Se plattformsspecifika instruktioner nedan.

    - [Så kontrollerar du i Windows](#how-to-check-on-windows)
    - [Så kontrollerar du på Mac](#how-to-check-on-mac)
    - [Så kontrollerar du på Android](#how-to-check-on-android)
    - [Så kontrollerar du på iPhone och iPad](#how-to-check-on-iphone-and-ipad)
    - [Handhållna enheter, surfplattor och andra enheter](#handhelds-tablets-and-other-devices)

4. **Gör ett snabbtest**.

    Anslut enheten till en skärm eller tv med en kabel eller adapter för USB-C till HDMI/DisplayPort som uttryckligen kräver DP Alt Mode. Om skärmen speglar eller utökar din bild fungerar inbyggd videoutgång på den porten. Använd inte en DisplayLink-adapter för det här testet.

---

## Så kontrollerar du i Windows {#how-to-check-on-windows}

1. Tryck på `Win + X` och öppna **Device Manager**.
2. Leta efter poster som nämner *"USB4"* eller *"Thunderbolt"*. De kan hjälpa dig att identifiera maskinvaran, men Enhetshanteraren ensam bekräftar inte stöd för DP Alt Mode på en viss port.
3. Kontrollera den exakta porten i den bärbara datorns bruksanvisning eller på tillverkarens produktsida – sök efter *"DisplayPort over USB-C"* eller *"DP Alt Mode"*.
4. Anslut Comet Q direkt, eller anslut en skärm med en adapter som uttryckligen kräver DP Alt Mode. Öppna **Settings** > **System** > **Display** > **Multiple displays** för att kontrollera om skärmen identifieras.

**Obs!**

1. **DisplayLink bevisar inte stöd för DP Alt Mode.** DisplayLink överför video via USB-data och fungerar även via USB-A. En DisplayLink-post i Enhetshanteraren, eller en skärm som fungerar via en DisplayLink-docka, visar inte att porten har inbyggd USB-C-videoutgång. Se [Synaptics: USB-C with DisplayLink](https://www.synaptics.com/products/displaylink-graphics/usb-c){target="_blank"}.

2. Om den bärbara datorn har flera USB-C-portar kanske bara vissa av dem stöder videoutgång. Kontrollera varje port för sig.

## Så kontrollerar du på Mac {#how-to-check-on-mac}

1. Klicka på **Apple menu** > **About This Mac** > **More Info**.
2. Rulla nedåt och klicka på **System Report**.
3. Välj **Thunderbolt / USB4** eller **USB** under **Hardware**.
4. Alla USB-C-portar som visas under Thunderbolt / USB4 stöder DisplayPort Alt Mode som standard.

**Tips!** Alla moderna Mac-datorer med USB-C-/Thunderbolt-portar stöder DisplayPort Alt Mode direkt.

!!! note "Modeller som stöds"

    - MacBook Neo (A18 Pro)
    - MacBook Air
        - MacBook Air 13 tum (M5)
        - MacBook Air 15 tum (M5)
        - MacBook Air 13 tum (M4)
        - MacBook Air 13 tum (M3)
        - MacBook Air 13 tum (M2)
        - MacBook Air 13 tum (M1, 2020)
        - MacBook Air 15 tum (M4)
        - MacBook Air 15 tum (M3)
        - MacBook Air 15 tum (M2, 2023)
        - MacBook Air (Intel, 2020)
    - MacBook Pro
        - MacBook Pro 14 tum (M5)
        - MacBook Pro 14 tum (M5 Pro)
        - MacBook Pro 14 tum (M5 Max)
        - MacBook Pro 16 tum (M5 Pro)
        - MacBook Pro 16 tum (M5 Max)
        - MacBook Pro 13 tum (M2, 2022)
        - MacBook Pro 13 tum (M1, 2020)
        - MacBook Pro 13 tum (Intel, två portar, 2020)
        - MacBook Pro 13 tum (Intel, fyra portar, 2020)
        - MacBook Pro 14 tum (M4 Max)
        - MacBook Pro 14 tum (M4 Pro)
        - MacBook Pro 14 tum (M4)
        - MacBook Pro 14 tum (M3)
        - MacBook Pro 14 tum (M3 Pro eller M3 Max)
        - MacBook Pro 14 tum (M2 Pro eller M2 Max, 2023)
        - MacBook Pro 14 tum (M1 Pro eller M1 Max, 2021)
        - MacBook Pro 16 tum (M4 Max)
        - MacBook Pro 16 tum (M4 Pro)
        - MacBook Pro 16 tum (M3 Pro eller M3 Max)
        - MacBook Pro 16 tum (M2 Pro eller M2 Max, 2023)
        - MacBook Pro 16 tum (M1 Pro eller M1 Max, 2021)
        - MacBook Pro 16 tum (Intel, 2019)
    - iMac
        - iMac (M4, två portar)
        - iMac (M4, fyra portar)
        - iMac (M3, två portar)
        - iMac (M3, fyra portar)
        - iMac 21,5 tum (Intel, 2019)
        - iMac 21,5 tum (Intel, 2017)
        - iMac 24 tum (M1, två portar, 2021)
        - iMac 24 tum (M1, fyra portar, 2021)
        - iMac 27 tum (Intel, 2020)
        - iMac Pro (Intel, 2017)
    - Mac mini
        - Mac mini (M4)
        - Mac mini (M4 Pro)
        - Mac mini (M2 eller M2 Pro)
        - Mac mini (M1, 2020)
        - Mac mini (Intel, 2018)
    - Mac Studio
        - Mac Studio (M4 Max)
        - Mac Studio (M3 Ultra)
        - Mac Studio (M2 Max eller M2 Ultra)
        - Mac Studio (M1 Max eller M1 Ultra, 2022)
    - Mac Pro
        - Mac Pro (M2 Ultra)
        - Mac Pro (Intel, 2019)

## Så kontrollerar du på Android {#how-to-check-on-android}

1. Öppna telefonens **Settings** och sök efter *"display"*, *"HDMI"* eller *"desktop mode"*.
2. Leta efter funktioner som **Samsung DeX**, **Motorola Ready For**, **Huawei EasyProjection** eller *"External display"*. Kontrollera i tillverkarens dokumentation att den exakta modellen stöder en **trådbunden skärmanslutning via USB-C**. Enbart en funktion för trådlös skärm bevisar inte stöd för DP Alt Mode.
3. Om telefonen stöder funktionen visas vanligtvis ett meddelande som *"External display connected"* när du ansluter den till en skärm.
4. Bekräfta videoutgången med en direktanslutning till Comet Q eller till en skärm via en adapter som kräver DP Alt Mode. Appar som bara visar USB-information kan inte på ett tillförlitligt sätt fastställa stöd för inbyggd videoutgång.

**Obs!** Många Android-telefoner i budgetklassen saknar DP Alt Mode trots att de har USB-C. Kontrollera alltid detta innan du köper Comet Q.

!!! note "Exempel på Samsung-enheter med trådbunden bildutgång"

    Samsung-enheterna nedan har kontrollerats mot [Samsungs information om DeX-kompatibilitet](https://www.samsung.com/us/support/answer/ANS10001955/){target="_blank"}.

    - Galaxy A90 5G
    - Galaxy Book
    - Galaxy Fold
    - Galaxy Note
        - Galaxy Note 8
        - Galaxy Note 9
        - Galaxy Note 10-serien
        - Galaxy Note20-serien
    - Galaxy S
        - Galaxy Tab S7 / 7+
        - Galaxy Tab S8 / 8+ / S8 Ultra
        - Galaxy S8 och S8+
        - Galaxy S9 och S9+
        - Galaxy S10-serien
        - Galaxy S20-serien
        - Galaxy S21-serien
        - Galaxy S22-serien
        - Galaxy S23-serien
        - Galaxy S24-serien
        - Galaxy S25-serien
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

## Så kontrollerar du på iPhone och iPad {#how-to-check-on-iphone-and-ipad}

1. iPhone 15-serien och senare (utom iPhone 16e och iPhone 17e) stöder DisplayPort Alt Mode via USB-C-porten. Se [Apples dokumentation om skärmanslutningar](https://support.apple.com/en-ie/105099#displays){target="_blank"} för din exakta modell.
2. iPhone 14 och tidigare använder Lightning och är inte kompatibla.
3. Alla iPad-modeller med USB-C (iPad Pro, iPad Air 4:e generationen och senare, iPad mini 6:e generationen och senare, iPad 10:e generationen och senare) stöder videoutgång.
4. iPad-modeller med den äldre Lightning-porten är inte kompatibla.

!!! note "Exempel på modeller med videoutgång via USB-C"

    iPhone-modellerna nedan har kontrollerats mot [Apples dokumentation om externa skärmar](https://support.apple.com/en-ie/105099#displays){target="_blank"}.

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
        - iPad (10:e generationen)
    - iPad mini
        - iPad mini (6:e generationen)
        - iPad mini (A17 Pro)
    - iPad Air
        - iPad Air (5:e generationen)
        - iPad Air (4:e generationen)
        - iPad Air 11 tum (M4)
        - iPad Air 11 tum (M3)
        - iPad Air 11 tum (M2)
        - iPad Air 13 tum (M4)
        - iPad Air 13 tum (M3)
        - iPad Air 13 tum (M2)
    - iPad Pro
        - iPad Pro 11 tum (M5)
        - iPad Pro 11 tum (M4)
        - iPad Pro 11 tum (4:e generationen)
        - iPad Pro 11 tum (3:e generationen)
        - iPad Pro 12,9 tum (5:e generationen)
        - iPad Pro 12,9 tum (6:e generationen)
        - iPad Pro 13 tum (M5)
        - iPad Pro 13 tum (M4)

## Handhållna enheter, surfplattor och andra enheter {#handhelds-tablets-and-other-devices}

1. **Steam Deck**, **ROG Ally**, **Lenovo Legion Go** – alla stöder DP Alt Mode.
2. **De flesta Windows-surfplattor** med USB-C (Surface Pro 8 och senare osv.) – stöds.
3. För andra enheter kontrollerar du den officiella specifikationssidan och söker efter nyckelorden *"DisplayPort"*, *"Alt Mode"*, *"video output"* eller *"Thunderbolt"*.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
