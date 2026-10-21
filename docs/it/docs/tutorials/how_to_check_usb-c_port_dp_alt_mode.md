# Come verificare se la porta USB-C del dispositivo supporta DP Alt Mode {#how-to-check-if-your-devices-usb-c-port-supports-dp-alt-mode}

## Che cos'è DP Alt Mode {#what-is-dp-alt-mode}

DP Alt Mode (DisplayPort Alternate Mode) è una funzionalità integrata in alcune porte USB-C che permette di trasmettere un segnale video di alta qualità, oltre ai dati e all'alimentazione normalmente gestiti.

In pratica, un solo cavo USB-C può trasmettere il video da smartphone, tablet o computer portatile direttamente a un monitor, un televisore o un proiettore, senza adattatori speciali o docking station. Senza DP Alt Mode, la porta può solo trasferire dati e fornire alimentazione; non può inviare video a uno schermo esterno.

## Perché è importante {#why-it-matters}

DP Alt Mode è importante per **Comet Q**, che si basa su questa funzionalità per ricevere il video dal dispositivo. Il dispositivo controllato deve supportare l'uscita video nativa tramite la propria porta USB-C. Un adattatore DisplayLink potrebbe non aggiungere questa capacità per un collegamento diretto a Comet Q.

Le porte USB-C non offrono tutte le stesse funzionalità. Alcune trasportano solo dati e alimentazione; altre possono anche trasmettere video. Il connettore ha la stessa forma, ma le funzionalità possono essere diverse. Due porte USB-C possono sembrare identiche e comportarsi in modo molto diverso: per questo è utile verificarle prima di acquistare un accessorio video USB-C.

## Metodi generali per verificare DP Alt Mode {#general-methods-to-verify-dp-alt-mode}

1. **Consulta la scheda tecnica**.

    Cerca il modello esatto sul sito del produttore. Cerca parole chiave come DisplayPort, DP Alt Mode, video output o Thunderbolt.

2. **Controlla i simboli vicino alla porta**.

    Un logo DisplayPort a forma di D o il simbolo del fulmine Thunderbolt accanto alla porta USB-C indica la possibilità di trasmettere video.

3. **Controlla le impostazioni di sistema**.

    Le impostazioni di sistema possono aiutare a identificare uno schermo collegato, ma non sempre permettono di stabilire se una specifica porta USB-C supporta DP Alt Mode nativo. Combina questi controlli con le specifiche del produttore e una prova di collegamento diretto. Consulta le istruzioni per ciascuna piattaforma riportate di seguito.

    - [Verifica su Windows](#how-to-check-on-windows)
    - [Verifica su Mac](#how-to-check-on-mac)
    - [Verifica su Android](#how-to-check-on-android)
    - [Verifica su iPhone e iPad](#how-to-check-on-iphone-and-ipad)
    - [Console portatili, tablet e altri dispositivi](#handhelds-tablets-and-other-devices)

4. **Esegui una prova rapida**.

    Collega il dispositivo a un monitor o a un televisore utilizzando un cavo o un adattatore da USB-C a HDMI / DisplayPort che richieda esplicitamente DP Alt Mode. Se lo schermo viene duplicato o esteso, l'uscita video nativa della porta funziona. Non utilizzare un adattatore DisplayLink per questa prova.

---

## Verifica su Windows {#how-to-check-on-windows}

1. Premi `Win + X` e apri **Device Manager**.
2. Cerca le voci che menzionano *"USB4"* o *"Thunderbolt"*. Possono aiutare a identificare l'hardware, ma Device Manager da solo non conferma il supporto di DP Alt Mode su una specifica porta.
3. Consulta il manuale del computer portatile o la pagina del prodotto sul sito del produttore per la porta specifica, cercando *"DisplayPort over USB-C"* o *"DP Alt Mode"*.
4. Collega direttamente Comet Q oppure collega uno schermo con un adattatore che richieda esplicitamente DP Alt Mode. Apri **Settings** > **System** > **Display** > **Multiple displays** per verificare se lo schermo viene rilevato.

**Nota**:

1. **DisplayLink non dimostra il supporto di DP Alt Mode.** DisplayLink trasmette video tramite dati USB e può funzionare anche con USB-A. Una voce DisplayLink in Device Manager, o uno schermo funzionante collegato tramite un dock DisplayLink, non dimostra la presenza di un'uscita video USB-C nativa. Consulta [Synaptics: USB-C con DisplayLink](https://www.synaptics.com/products/displaylink-graphics/usb-c){target="_blank"}.

2. Se il computer portatile ha più porte USB-C, solo alcune potrebbero supportare l'uscita video. Verifica ciascuna porta separatamente.

## Verifica su Mac {#how-to-check-on-mac}

1. Fai clic su **Apple menu** > **About This Mac** > **More Info**.
2. Scorri verso il basso e fai clic su **System Report**.
3. In **Hardware**, seleziona **Thunderbolt / USB4** o **USB**.
4. Qualsiasi porta USB-C elencata in Thunderbolt / USB4 supporta DisplayPort Alt Mode per impostazione predefinita.

**Suggerimento**: tutti i Mac moderni con porte USB-C / Thunderbolt supportano DisplayPort Alt Mode senza configurazioni aggiuntive.

!!! note "Modelli supportati"

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
        - MacBook Pro 13-in. (Intel, due porte, 2020)
        - MacBook Pro 13-in. (Intel, quattro porte, 2020)
        - MacBook Pro 14-in. (M4 Max)
        - MacBook Pro 14-in. (M4 Pro)
        - MacBook Pro 14-in. (M4)
        - MacBook Pro 14-in. (M3)
        - MacBook Pro 14-in. (M3 Pro o M3 Max)
        - MacBook Pro 14-in. (M2 Pro o M2 Max, 2023)
        - MacBook Pro 14-in. (M1 Pro o M1 Max, 2021)
        - MacBook Pro 16-in. (M4 Max)
        - MacBook Pro 16-in. (M4 Pro)
        - MacBook Pro 16-in. (M3 Pro o M3 Max)
        - MacBook Pro 16-in. (M2 Pro o M2 Max, 2023)
        - MacBook Pro 16-in. (M1 Pro o M1 Max, 2021)
        - MacBook Pro 16-in. (Intel, 2019)
    - iMac
        - iMac (M4, due porte)
        - iMac (M4, quattro porte)
        - iMac (M3, due porte)
        - iMac (M3, quattro porte)
        - iMac 21.5-in. (Intel, 2019)
        - iMac 21.5-in. (Intel, 2017)
        - iMac 24-in. (M1, due porte, 2021)
        - iMac 24-in. (M1, quattro porte, 2021)
        - iMac 27-in. (Intel, 2020)
        - iMac Pro (Intel, 2017)
    - Mac mini
        - Mac mini (M4)
        - Mac mini (M4 Pro)
        - Mac mini (M2 o M2 Pro)
        - Mac mini (M1, 2020)
        - Mac mini (Intel, 2018)
    - Mac Studio
        - Mac Studio (M4 Max)
        - Mac Studio (M3 Ultra)
        - Mac Studio (M2 Max o M2 Ultra)
        - Mac Studio (M1 Max o M1 Ultra, 2022)
    - Mac Pro
        - Mac Pro (M2 Ultra)
        - Mac Pro (Intel, 2019)

## Verifica su Android {#how-to-check-on-android}

1. Apri le **Settings** dello smartphone e cerca *"display"*, *"HDMI"* o *"desktop mode"*.
2. Cerca funzionalità come **Samsung DeX**, **Motorola Ready For**, **Huawei EasyProjection** o *"External display"*. Consulta la documentazione del produttore per confermare che il modello esatto supporti un **collegamento cablato a uno schermo tramite USB-C**; una funzionalità di visualizzazione wireless da sola non dimostra il supporto di DP Alt Mode.
3. Se lo smartphone lo supporta, in genere comparirà una notifica come *"External display connected"* quando lo colleghi a un monitor.
4. Conferma l'uscita video collegando direttamente Comet Q oppure uno schermo con un adattatore che richieda DP Alt Mode. Le sole app di informazioni USB non permettono di determinare in modo affidabile il supporto dell'uscita video nativa.

**Nota**: molti smartphone Android economici non supportano DP Alt Mode pur avendo una porta USB-C. Verifica sempre prima di acquistare Comet Q.

!!! note "Esempi di dispositivi Samsung con uscita video cablata"

    I dispositivi Samsung elencati di seguito sono stati verificati rispetto alle [informazioni di compatibilità di Samsung DeX](https://www.samsung.com/us/support/answer/ANS10001955/){target="_blank"}.

    - Galaxy A90 5G
    - Galaxy Book
    - Galaxy Fold
    - Galaxy Note
        - Galaxy Note 8
        - Galaxy Note 9
        - Galaxy Note 10 (serie)
        - Galaxy Note20 (serie)
    - Galaxy S
        - Galaxy Tab S7 / 7+
        - Galaxy Tab S8 / 8+ / S8 Ultra
        - Galaxy S8 e S8+
        - Galaxy S9 e S9+
        - Galaxy S10 (serie)
        - Galaxy S20 (serie)
        - Galaxy S21 (serie)
        - Galaxy S22 (serie)
        - Galaxy S23 (serie)
        - Galaxy S24 (serie)
        - Galaxy S25 (serie)
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

## Verifica su iPhone e iPad {#how-to-check-on-iphone-and-ipad}

1. La serie iPhone 15 e successive (tranne iPhone 16e e iPhone 17e) supportano DisplayPort Alt Mode tramite la porta USB-C. Consulta la [documentazione Apple sul collegamento degli schermi](https://support.apple.com/en-ie/105099#displays){target="_blank"} per il modello esatto.
2. iPhone 14 e precedenti utilizzano Lightning e non sono compatibili.
3. Tutti i modelli di iPad con USB-C (iPad Pro, iPad Air dalla 4ª generazione, iPad mini dalla 6ª generazione e iPad dalla 10ª generazione) supportano l'uscita video.
4. Gli iPad con la vecchia porta Lightning non sono compatibili.

!!! note "Esempi di modelli con uscita video USB-C"

    Gli iPhone elencati di seguito sono stati verificati rispetto alla [documentazione Apple sugli schermi esterni](https://support.apple.com/en-ie/105099#displays){target="_blank"}.

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
        - iPad (10ª generazione)
    - iPad mini
        - iPad mini (6ª generazione)
        - iPad mini (A17 Pro)
    - iPad Air
        - iPad Air (5ª generazione)
        - iPad Air (4ª generazione)
        - iPad Air 11-inch (M4)
        - iPad Air 11-inch (M3)
        - iPad Air 11-inch (M2)
        - iPad Air 13-inch (M4)
        - iPad Air 13‑inch (M3)
        - iPad Air 13-inch (M2)
    - iPad Pro
        - iPad Pro 11‑inch (M5)
        - iPad Pro 11‑inch (M4)
        - iPad Pro 11-inch (4ª generazione)
        - iPad Pro 11-inch (3ª generazione)
        - iPad Pro 12.9-inch (5ª generazione)
        - iPad Pro 12.9-inch (6ª generazione)
        - iPad Pro 13‑inch (M5)
        - iPad Pro 13‑inch (M4)

## Console portatili, tablet e altri dispositivi {#handhelds-tablets-and-other-devices}

1. **Steam Deck**, **ROG Ally** e **Lenovo Legion Go** supportano tutti DP Alt Mode.
2. È supportata **la maggior parte dei tablet Windows** con USB-C (Surface Pro 8 e successivi, ecc.).
3. Per gli altri dispositivi, consulta la pagina ufficiale delle specifiche e cerca le parole chiave *"DisplayPort"*, *"Alt Mode"*, *"video output"* o *"Thunderbolt"*.

---

Hai ancora domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
