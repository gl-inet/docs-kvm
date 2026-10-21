# Korte veelgestelde vragen over GL.iNet KVM {#quick-faqs-about-glinet-kvm}

Dit is een korte verzameling vragen en antwoorden over GL.iNet KVM, bedoeld om snel antwoord te geven op enkele veelvoorkomende basisvragen.

## Basisinformatie {#basic-information}

**V1. Welke apparaten kan een GL.iNet KVM bedienen?**

A1. Een GL.iNet KVM kan elk apparaat met HDMI-uitvoer en USB-invoer bedienen, zoals laptops, desktops, Raspberry Pi, minicomputers enzovoort.

Daarnaast kan de Comet Q (GL-RMQ1) elk apparaat bedienen waarvan de USB‑C-poort DisplayPort Alt Mode voor video-uitvoer ondersteunt; een HDMI-poort is niet nodig. Dit omvat onder meer bepaalde iPhones, iPads, Android-telefoons, MacBooks, Mac minis en de meeste moderne Windows-laptops. Klik [hier](../user_guide/gl-rmq1/product_overview.md#compatibility) voor meer informatie.

---

**V2. Moet ik software installeren om een GL.iNet KVM te gebruiken?**

A2. Op het bestuurde apparaat hoeft geen software te worden geïnstalleerd. Het bestuurde apparaat kan Windows, macOS, ChromeOS, Linux enzovoort gebruiken.

Of er software op het besturende apparaat moet worden geïnstalleerd, hangt af van de manier waarop u de KVM wilt openen.

??? "Bediening in de buurt (alleen voor Comet 5G)"

    **Opmerking**: Deze methode is alleen beschikbaar op de Comet 5G (GL-RM10RC).

    De Comet 5G biedt bediening in de buurt via wifi, voor snel lokaal beheer zonder bekabelde verbindingen. Zet de wifinetwerkmodus van de Comet 5G op AP-modus; het apparaat genereert dan een unieke wifi-SSID. Maak verbinding met deze SSID om de console van de Comet 5G veilig te openen. Klik [hier](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control) voor meer informatie.

    Wanneer u de AP-modus activeert, wordt de verbinding van de Comet 5G met het bovenliggende wifinetwerk verbroken en is alleen toegang in de buurt mogelijk (zonder internetverbinding).

??? "Lokale bediening (alleen voor Comet X)"

    **Opmerking**: Deze methode is alleen beschikbaar op de Comet X (GL-RM4PE).

    De Comet X heeft een HDMI OUT-poort en twee extra USB-poorten, ideaal voor lokale probleemoplossing, configuratie en installatie van een besturingssysteem. Sluit eenvoudig uw monitor, muis en toetsenbord aan voor plug-and-play lokale bediening van de hardware. Klik [hier](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control) voor meer informatie.

??? "Toegang via het LAN"

    Als u de KVM via hetzelfde lokale netwerk (LAN) wilt openen, hoeft u geen software op het besturende apparaat te installeren.

    Open een browser op het besturende apparaat en voer het IP-adres van de KVM of `glkvm.local` in de adresbalk in om de KVM lokaal te openen.
    
    Klik [hier](local_access_via_browser.md){target="_blank"} voor meer informatie.
    
??? "Externe toegang"

    - **GLKVM-app**
    
        Als uw besturende apparaat Windows, macOS, Android of iOS gebruikt, kunt u de [GLKVM-app](https://www.gl-inet.com/app-rm/){target="_blank"} erop installeren en uw KVM – en daarmee het bestuurde apparaat – op afstand openen.
        
        Klik [hier](remote_access_via_glkvm_app.md){target="_blank"} voor meer informatie.
        
    - **Cloudservice**
    
        Deze methode is ideaal als u de GLKVM-app niet kunt of wilt installeren.

        Koppel uw KVM aan de cloudservice. Daarna kunt u uw KVM – en daarmee het bestuurde apparaat – op afstand openen door `glkvm.com` in te voeren in een webbrowser op uw besturende apparaat, zonder de GLKVM-app te installeren.

        Klik [hier](remote_access_via_cloud.md){target="_blank"} voor meer informatie.
    
    - **Tailscale**
    
        Deze methode is geschikt als u de GLKVM-app of de cloudservice niet kunt of wilt gebruiken, al zijn er meer stappen nodig.

        Koppel uw KVM en uw besturende apparaat aan hetzelfde Tailscale-account. Daarna kunt u uw KVM – en daarmee het bestuurde apparaat – op afstand openen door het virtuele Tailscale-IP-adres van de KVM in te voeren in een webbrowser op uw besturende apparaat.
    
        Klik [hier](remote_access_via_tailscale.md){target="_blank"} voor meer informatie.

    - **ZeroTier**
    
        Deze methode is geschikt als u de GLKVM-app of de cloudservice niet kunt of wilt gebruiken, al zijn er meer stappen nodig.

        Voeg uw KVM en uw besturende apparaat toe aan hetzelfde ZeroTier-netwerk. Daarna kunt u uw KVM – en daarmee het bestuurde apparaat – op afstand openen door het ZeroTier-IP-adres van de KVM in te voeren in een webbrowser op uw besturende apparaat.
    
        Klik [hier](remote_access_via_zerotier.md){target="_blank"} voor meer informatie.

    - **NetBird**

        Deze methode is geschikt als u de GLKVM-app of de cloudservice niet kunt of wilt gebruiken, al zijn er meer stappen nodig.

        [NetBird](https://netbird.io/){target="_blank"} is een opensource zero-trust-netwerkplatform waarmee u veilige privénetwerken kunt opzetten voor thuis- en zakelijk gebruik. Als overlaynetwerk op basis van WireGuard® biedt NetBird altijd en overal veilige toegang tot uw apparaten.
        
        De GL.iNet KVM is geïntegreerd met NetBird, zodat u de KVM aan het virtuele NetBird-netwerk kunt koppelen voor externe toegang.

        Klik [hier](remote_access_via_netbird.md){target="_blank"} voor meer informatie.

---

**V3. Hoe open ik een GL.iNet KVM?**

A3. Over het algemeen kunt u een GL.iNet KVM op verschillende manieren lokaal of op afstand openen:

- [Toegang via het LAN met een webbrowser](local_access_via_browser.md){target="_blank"}
- [Externe toegang via de cloudservice](remote_access_via_cloud.md){target="_blank"}
- [Externe toegang via de GLKVM-app](remote_access_via_glkvm_app.md){target="_blank"}
- [Externe toegang via Tailscale](remote_access_via_tailscale.md){target="_blank"}
- [Externe toegang via ZeroTier](remote_access_via_zerotier.md){target="_blank"}
- [Externe toegang via NetBird](remote_access_via_netbird.md){target="_blank"}

Bovendien ondersteunen sommige GL.iNet KVM-modellen bediening in de buurt of lokale bediening, zodat u ze ter plaatse kunt openen zonder verbinding met een andere router.

- [Bediening in de buurt (alleen voor Comet 5G)](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control){target="_blank"}
- [Lokale bediening (alleen voor Comet X)](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control){target="_blank"}

---

**V4. Moet ik poorten openen (blootgesteld aan het WAN) om externe toegang tot een GL.iNet KVM mogelijk te maken?**

A4. Nee. Er zijn geen open poorten en zelfs geen openbaar IP-adres nodig.

---

**V5. Ondersteunt de GLKVM-app ChromeOS/Linux?**

A5. Nee. De GLKVM-app kan momenteel niet worden geïnstalleerd op ChromeOS of Linux.

Als uw besturende apparaat ChromeOS/Linux gebruikt, kan de GLKVM-app niet worden geïnstalleerd en wordt externe toegang tot het bestuurde apparaat via de GLKVM-app dus niet ondersteund.

U kunt echter <u>de cloudservice</u>, <u>Tailscale</u>, <u>ZeroTier</u> of <u>NetBird</u> gebruiken voor externe toegang. Zie V3 hierboven voor meer informatie.

U kunt de KVM ook lokaal openen via een webbrowser. Zie V3 hierboven voor meer informatie.

---

**V6. Kan de Comet (GL-RM1) verbinding maken met een draadloos netwerk?**

A6. Nee. De Comet (GL-RM1) ondersteunt geen draadloze netwerkverbinding.

Het apparaat moet voor internettoegang met een ethernetkabel worden aangesloten op een netwerkapparaat (bijvoorbeeld een router).

Als u liever een KVM met wifi-ondersteuning hebt, kunt u de volgende modellen overwegen:

* [Comet Pro (GL-RM10)](https://www.gl-inet.com/products/gl-rm10/){target="_blank"}
* [Comet 5G (GL-RM10RC)](https://www.gl-inet.com/products/gl-rm10rc/){target="_blank"}
* [Comet Q (GL-RMQ1)](https://www.gl-inet.com/products/gl-rmq1/){target="_blank"}

---

## Bediening van de voeding {#power-control}

**V1. Kan een GL.iNet KVM het doelapparaat op afstand in- en uitschakelen?**

A1. Met een GL.iNet KVM kunt u het doelapparaat op de volgende manieren op afstand in- en uitschakelen:

- Wake-on-LAN (ingebouwde softwareservice)

- [ATX Board](../user_guide/gl-atx-board/index.md){target="_blank"} (apart verkrijgbaar; werkt niet met de Comet Q)

- [Fingerbot](../user_guide/gl-fgb-01/index.md){target="_blank"} (apart verkrijgbaar; werkt niet met de Comet Q)

---

**V2. Hoe gebruik ik het ATX Board voor het op afstand bedienen van de voeding?**

A2. Raadpleeg de [gebruikershandleiding van het ATX Board](../user_guide/gl-atx-board/index.md){target="_blank"}.

---

## Functies {#features}

!!! Tip "Tip"

    Hieronder vindt u veelgestelde vragen over enkele veelgebruikte functies. Raadpleeg de bijbehorende [gebruikershandleiding](../user_guide/index.md) voor alle details over de functies.

**V1. Moet ik de KVM-cloudservice gebruiken?**

A1. Nee. De cloudservice is optioneel.

Als u voor externe toegang niet afhankelijk wilt zijn van de cloud, kunt u overlaynetwerktools van derden gebruiken, zoals Tailscale, ZeroTier en NetBird.

---

**V2. Kan ik met één GL.iNet KVM meerdere apparaten bedienen?**

A2. De volgende GL.iNet KVM's kunnen slechts één doelapparaat bedienen:

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)
* Comet Q (GL-RMQ1)

De Comet X (GL-RM4PE) kan daarentegen tegelijkertijd op maximaal vier doelapparaten worden aangesloten, maar u kunt slechts één apparaat tegelijk bedienen. Ter plaatse kunt u met de fysieke knop op het voorpaneel snel tussen de vier aangesloten apparaten wisselen; op afstand doet u dit via de externe console.

De Comet X (GL-RM4PE) heeft vier onafhankelijke kanalen op het achterpaneel. Elk kanaal heeft een HDMI-poort voor de overdracht van videosignalen, een Type-C-poort voor de overdracht van toetsenbord- en muissignalen en een USB 2.0-poort voor USB-randapparaten (bijvoorbeeld een Fingerbot of ATX Board).

---

**V3. Wat is Wake-on-LAN?**

A3. Wake-on-LAN (WOL) is een technologie waarmee een computer of apparaat via een netwerk op afstand kan worden ingeschakeld of uit een energiebesparende stand kan worden gewekt. Hiervoor wordt een "magic packet" met het MAC-adres van het doelapparaat verzonden, waardoor het apparaat opstart. Veelvoorkomende toepassingen zijn beheer op afstand, energiebesparende stand-byconfiguraties en centraal systeembeheer.

---

**V4. Ondersteunt de GL.iNet KVM Mouse Jiggle?**

A4. Ja. U kunt Mouse Jiggle inschakelen in de KVM-console.

De functie Mouse Jiggle simuleert subtiele, periodieke muisbewegingen om te voorkomen dat de computer (dus het bestuurde apparaat) bij langdurige inactiviteit in de slaapstand gaat, bijvoorbeeld tijdens online vergaderingen of serverbeheer.

---

**V5. Ondersteunt de GL.iNet KVM tweerichtingsaudio?**

A5. Ja. U kunt Speaker en Microphone inschakelen in de KVM-console voor audio-overdracht in twee richtingen.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
