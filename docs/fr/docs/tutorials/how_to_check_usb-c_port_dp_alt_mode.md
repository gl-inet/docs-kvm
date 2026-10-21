# Vérifier si le port USB-C de votre appareil prend en charge le DP Alt Mode {#how-to-check-if-your-devices-usb-c-port-supports-dp-alt-mode}

## Qu’est-ce que le DP Alt Mode ? {#what-is-dp-alt-mode}

Le DP Alt Mode (DisplayPort Alternate Mode) est une fonction de certains ports USB-C qui leur permet de transmettre un signal vidéo de haute qualité, en plus des données et de l’alimentation habituelles.

Un seul câble USB-C permet ainsi de transmettre la vidéo de votre téléphone, tablette ou ordinateur portable directement vers un écran, un téléviseur ou un projecteur, sans adaptateur spécial ni station d’accueil. Sans DP Alt Mode, le port peut uniquement transférer des données et fournir de l’alimentation ; il ne peut pas envoyer de vidéo vers un écran externe.

## Pourquoi est-ce nécessaire ? {#why-it-matters}

Le DP Alt Mode est essentiel pour le **Comet Q**, qui l’utilise pour recevoir la vidéo de votre appareil. L’appareil contrôlé doit prendre en charge une sortie vidéo native via son port USB-C. Un adaptateur DisplayLink ne permet pas nécessairement d’ajouter cette capacité pour une connexion directe au Comet Q.

Les ports USB-C n’offrent pas tous les mêmes fonctions. Certains transmettent uniquement des données et de l’alimentation ; d’autres peuvent aussi envoyer de la vidéo. Leur connecteur a la même forme, mais leurs capacités diffèrent. Il est donc utile de vérifier ces caractéristiques avant d’acheter un accessoire d’affichage USB-C.

## Méthodes générales de vérification du DP Alt Mode {#general-methods-to-verify-dp-alt-mode}

1. **Consultez la fiche technique**.

    Recherchez votre modèle exact sur le site du fabricant, avec des mots-clés comme DisplayPort, DP Alt Mode, sortie vidéo ou Thunderbolt.

2. **Examinez les symboles près du port**.

    Un logo DisplayPort en forme de D ou un éclair Thunderbolt à côté du port USB-C indique une capacité de sortie vidéo.

3. **Consultez les paramètres système**.

    Les paramètres système permettent parfois d’identifier un écran connecté, mais ne suffisent pas toujours à confirmer le DP Alt Mode natif sur un port USB-C précis. Complétez ces vérifications par les caractéristiques du fabricant et un test de connexion directe. Les instructions par plateforme figurent ci-dessous.

    - [Vérification sous Windows](#how-to-check-on-windows)
    - [Vérification sur Mac](#how-to-check-on-mac)
    - [Vérification sous Android](#how-to-check-on-android)
    - [Vérification sur iPhone et iPad](#how-to-check-on-iphone-and-ipad)
    - [Consoles portables, tablettes et autres appareils](#handhelds-tablets-and-other-devices)

4. **Effectuez un test rapide**.

    Connectez l’appareil à un écran ou à un téléviseur avec un câble ou un adaptateur USB-C vers HDMI / DisplayPort qui exige explicitement le DP Alt Mode. Si l’image est dupliquée ou étendue, la sortie vidéo native fonctionne sur ce port. N’utilisez pas d’adaptateur DisplayLink pour ce test.

---

## Vérification sous Windows {#how-to-check-on-windows}

1. Appuyez sur `Win + X` et ouvrez **Device Manager**.
2. Recherchez les entrées mentionnant *« USB4 »* ou *« Thunderbolt »*. Elles aident à identifier le matériel, mais le Gestionnaire de périphériques seul ne confirme pas le DP Alt Mode sur un port précis.
3. Consultez le manuel de l’ordinateur ou la page produit du fabricant pour le port concerné ; recherchez *« DisplayPort over USB-C »* ou *« DP Alt Mode »*.
4. Connectez directement le Comet Q, ou un écran avec un adaptateur qui exige le DP Alt Mode. Ouvrez **Settings** > **System** > **Display** > **Multiple displays** pour vérifier que l’écran est détecté.

**Remarque :**

1. **DisplayLink ne prouve pas la prise en charge du DP Alt Mode.** DisplayLink transmet la vidéo via les données USB et fonctionne aussi avec l’USB-A. Une entrée DisplayLink dans le Gestionnaire de périphériques ou un écran fonctionnant via une station DisplayLink ne confirme pas une sortie vidéo USB-C native. Consultez [Synaptics : USB-C avec DisplayLink](https://www.synaptics.com/products/displaylink-graphics/usb-c){target="_blank"}.

2. Si votre ordinateur dispose de plusieurs ports USB-C, seuls certains peuvent prendre en charge la vidéo. Vérifiez chaque port séparément.

## Vérification sur Mac {#how-to-check-on-mac}

1. Cliquez sur **Apple menu** > **About This Mac** > **More Info**.
2. Faites défiler la page et cliquez sur **System Report**.
3. Sous **Hardware**, sélectionnez **Thunderbolt / USB4** ou **USB**.
4. Tout port USB-C répertorié sous Thunderbolt / USB4 prend en charge le DisplayPort Alt Mode par défaut.

**Conseil :** Tous les Mac récents disposant de ports USB-C / Thunderbolt prennent en charge le DisplayPort Alt Mode sans configuration supplémentaire.

!!! note "Modèles pris en charge"

    - MacBook Neo (A18 Pro)
    - MacBook Air
        - MacBook Air 13 pouces (M5)
        - MacBook Air 15 pouces (M5)
        - MacBook Air 13 pouces (M4)
        - MacBook Air 13 pouces (M3)
        - MacBook Air 13 pouces (M2)
        - MacBook Air 13 pouces (M1, 2020)
        - MacBook Air 15 pouces (M4)
        - MacBook Air 15 pouces (M3)
        - MacBook Air 15 pouces (M2, 2023)
        - MacBook Air (Intel, 2020)
    - MacBook Pro
        - MacBook Pro 14 pouces (M5)
        - MacBook Pro 14 pouces (M5 Pro)
        - MacBook Pro 14 pouces (M5 Max)
        - MacBook Pro 16 pouces (M5 Pro)
        - MacBook Pro 16 pouces (M5 Max)
        - MacBook Pro 13 pouces (M2, 2022)
        - MacBook Pro 13 pouces (M1, 2020)
        - MacBook Pro 13 pouces (Intel, deux ports, 2020)
        - MacBook Pro 13 pouces (Intel, quatre ports, 2020)
        - MacBook Pro 14 pouces (M4 Max)
        - MacBook Pro 14 pouces (M4 Pro)
        - MacBook Pro 14 pouces (M4)
        - MacBook Pro 14 pouces (M3)
        - MacBook Pro 14 pouces (M3 Pro ou M3 Max)
        - MacBook Pro 14 pouces (M2 Pro ou M2 Max, 2023)
        - MacBook Pro 14 pouces (M1 Pro ou M1 Max, 2021)
        - MacBook Pro 16 pouces (M4 Max)
        - MacBook Pro 16 pouces (M4 Pro)
        - MacBook Pro 16 pouces (M3 Pro ou M3 Max)
        - MacBook Pro 16 pouces (M2 Pro ou M2 Max, 2023)
        - MacBook Pro 16 pouces (M1 Pro ou M1 Max, 2021)
        - MacBook Pro 16 pouces (Intel, 2019)
    - iMac
        - iMac (M4, deux ports)
        - iMac (M4, quatre ports)
        - iMac (M3, deux ports)
        - iMac (M3, quatre ports)
        - iMac 21,5 pouces (Intel, 2019)
        - iMac 21,5 pouces (Intel, 2017)
        - iMac 24 pouces (M1, deux ports, 2021)
        - iMac 24 pouces (M1, quatre ports, 2021)
        - iMac 27 pouces (Intel, 2020)
        - iMac Pro (Intel, 2017)
    - Mac mini
        - Mac mini (M4)
        - Mac mini (M4 Pro)
        - Mac mini (M2 ou M2 Pro)
        - Mac mini (M1, 2020)
        - Mac mini (Intel, 2018)
    - Mac Studio
        - Mac Studio (M4 Max)
        - Mac Studio (M3 Ultra)
        - Mac Studio (M2 Max ou M2 Ultra)
        - Mac Studio (M1 Max ou M1 Ultra, 2022)
    - Mac Pro
        - Mac Pro (M2 Ultra)
        - Mac Pro (Intel, 2019)

## Vérification sous Android {#how-to-check-on-android}

1. Ouvrez **Settings** sur le téléphone et recherchez *« display »*, *« HDMI »* ou *« desktop mode »*.
2. Recherchez des fonctions comme **Samsung DeX**, **Motorola Ready For**, **Huawei EasyProjection** ou *« External display »*. Consultez la documentation du fabricant pour vérifier que le modèle exact prend en charge une **connexion filaire à un écran USB-C** ; une fonction d’affichage sans fil ne prouve pas la prise en charge du DP Alt Mode.
3. Sur un téléphone compatible, une notification du type *« External display connected »* apparaît généralement lorsqu’un écran est branché.
4. Confirmez la sortie vidéo par une connexion directe au Comet Q ou à un écran avec un adaptateur exigeant le DP Alt Mode. Les applications d’informations USB ne peuvent pas, à elles seules, établir cette compatibilité de manière fiable.

**Remarque :** De nombreux téléphones Android d’entrée de gamme n’offrent pas le DP Alt Mode malgré leur port USB-C. Vérifiez toujours ce point avant d’acheter un Comet Q.

!!! note "Exemples d’appareils Samsung avec sortie vidéo filaire"

    Les appareils Samsung ci-dessous ont été vérifiés à partir des [informations de compatibilité DeX de Samsung](https://www.samsung.com/us/support/answer/ANS10001955/){target="_blank"}.

    - Galaxy A90 5G
    - Galaxy Book
    - Galaxy Fold
    - Galaxy Note
        - Galaxy Note 8
        - Galaxy Note 9
        - Galaxy Note 10 (gamme)
        - Galaxy Note20 (gamme)
    - Galaxy S
        - Galaxy Tab S7 / 7+
        - Galaxy Tab S8 / 8+ / S8 Ultra
        - Galaxy S8 et S8+
        - Galaxy S9 et S9+
        - Galaxy S10 (gamme)
        - Galaxy S20 (gamme)
        - Galaxy S21 (gamme)
        - Galaxy S22 (gamme)
        - Galaxy S23 (gamme)
        - Galaxy S24 (gamme)
        - Galaxy S25 (gamme)
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

## Vérification sur iPhone et iPad {#how-to-check-on-iphone-and-ipad}

1. Les iPhone 15 et versions ultérieures (sauf iPhone 16e et iPhone 17e) prennent en charge le DisplayPort Alt Mode via leur port USB-C. Consultez la [documentation Apple sur la connexion à un écran](https://support.apple.com/en-ie/105099#displays){target="_blank"} pour votre modèle exact.
2. Les iPhone 14 et antérieurs utilisent Lightning et ne sont pas compatibles.
3. Tous les iPad avec USB-C (iPad Pro, iPad Air de 4e génération et ultérieurs, iPad mini de 6e génération et ultérieurs, iPad de 10e génération et ultérieurs) prennent en charge la sortie vidéo.
4. Les iPad avec l’ancien port Lightning ne sont pas compatibles.

!!! note "Exemples de modèles avec sortie vidéo USB-C"

    Les iPhone ci-dessous ont été vérifiés à partir de la [documentation Apple sur les écrans externes](https://support.apple.com/en-ie/105099#displays){target="_blank"}.

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
        - iPad (10e génération)
    - iPad mini
        - iPad mini (6e génération)
        - iPad mini (A17 Pro)
    - iPad Air
        - iPad Air (5e génération)
        - iPad Air (4e génération)
        - iPad Air 11 pouces (M4)
        - iPad Air 11 pouces (M3)
        - iPad Air 11 pouces (M2)
        - iPad Air 13 pouces (M4)
        - iPad Air 13 pouces (M3)
        - iPad Air 13 pouces (M2)
    - iPad Pro
        - iPad Pro 11 pouces (M5)
        - iPad Pro 11 pouces (M4)
        - iPad Pro 11 pouces (4e génération)
        - iPad Pro 11 pouces (3e génération)
        - iPad Pro 12,9 pouces (5e génération)
        - iPad Pro 12,9 pouces (6e génération)
        - iPad Pro 13 pouces (M5)
        - iPad Pro 13 pouces (M4)

## Consoles portables, tablettes et autres appareils {#handhelds-tablets-and-other-devices}

1. **Steam Deck**, **ROG Ally**, **Lenovo Legion Go** : tous prennent en charge le DP Alt Mode.
2. **La plupart des tablettes Windows** avec USB-C (Surface Pro 8 et ultérieures, etc.) sont compatibles.
3. Pour les autres appareils, consultez la fiche technique officielle et recherchez *« DisplayPort »*, *« Alt Mode »*, *« video output »* ou *« Thunderbolt »*.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
