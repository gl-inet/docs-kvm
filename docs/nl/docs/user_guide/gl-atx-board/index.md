# ATX Board (GL-ATXPC) – gebruikershandleiding {#atx-board-gl-atxpc-user-guide}

Het ATX Board is een optioneel accessoire voor GL.iNet KVM-apparaten. Als slimme module voor energiebeheer maakt het mogelijk de voeding van het bestuurde apparaat op afstand te bedienen door het indrukken van de fysieke aan/uit-knop te simuleren (inschakelen/uitschakelen/opnieuw opstarten).

Het ATX Board wordt in de behuizing van het bestuurde apparaat geïnstalleerd, wat zorgt voor een onopvallender en stabieler energiebeheer.

**Opmerking**: Comet Q (GL-RMQ1) werkt niet met het ATX Board.

![Comet en ATX Board](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/rm1-and-atx-borad.jpg){class="glboxshadow"}

## Inhoud van de verpakking {#package-contents}

![Inhoud van de doos](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/inside-the-box.png){class="glboxshadow gl-80-desktop"}

- 1 x ATX-hoofdprintplaat
- 1 x 9-pins kabelset
- 1 x zakje met schroeven
- 1 x USB-A-naar-Type-C-kabel
- 1 x ATX-bevestigingsbeugelset

## Pinout {#pin-out}

![Pinout](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/pinout.jpg){class="glboxshadow gl-80-desktop"}

Uitleg van de aansluitingen:

1. Type-C-aansluiting: aansluiten op het KVM-apparaat.
2. Knop voor firmware-upgrade: voor de single-chip microcomputer op de ATX-hoofdprintplaat.
3. Resetknop.
4. Aansluiten op de bedieningskabel van het computerpaneel.
5. Aansluiten op de F_PANEL-aansluiting van de computer.

!!! note "Opmerking"

    1. Aansluitingen 4 en 5 zijn onderling verwisselbaar. Dat wil zeggen dat u aansluiting 5 ook op de bedieningskabel van het computerpaneel kunt aansluiten en aansluiting 4 op de F_PANEL-aansluiting.
    
    2. Het ATX Board heeft twee leds die zich allebei gedragen als de voedingsled (blauw geeft het ATX-systeem aan; groen geeft aan dat de pc van stroom wordt voorzien). Het ATX Board heeft geen HDD-led. De ledstatus op het board komt overeen met de status van de voedingsled op het computerpaneel.

Schema van aansluitingen 4/5:

![Aansluitingen](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface.png){class="glboxshadow gl-60-desktop"}

## Installatie {#installation}

Bekijk deze video om het ATX Board te installeren of volg de onderstaande stappen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3VEjZgzgI44" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. ATX Board en beugel vastschroeven {#1-screw-atx-board-and-bracket}

Bevestig het ATX Board en de ATX-bevestigingsbeugelset met de meegeleverde schroeven.

![Vastschroeven](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/screwing.jpg){class="glboxshadow gl-90-desktop"}

### 2. ATX Board in de pc-behuizing installeren {#2-install-atx-board-into-pc-case}

Sluit aansluitingen 4 en 5 aan op respectievelijk de bedieningskabel en de F_PANEL-aansluiting van de bestuurde pc.

![Aansluitingen verbinden](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface_connect.jpg){class="glboxshadow gl-90-desktop"}

Met de 9-pins kabelset uit de ATX-verpakking kunt u een van de aansluitingen 4/5 van het ATX Board verbinden met de bedieningskabel of de F_PANEL-aansluiting van de bestuurde computer.
    
Gebruik de kabelset die bij uw computerbehuizing is geleverd om de andere aansluiting 4/5 van het ATX Board te verbinden met de bedieningskabel of de F_PANEL-aansluiting van de bestuurde computer.

**Opmerking**: De polariteit van de aansluitingen kan per pc-behuizing verschillen. Controleer deze zorgvuldig vóór de installatie.

Hieronder ziet u ter referentie enkele voorbeelden van het aansluiten van aansluiting 4/5 op de F_PANEL-aansluiting van de bestuurde computer.

??? "Voor een PANEL met 10-1 pinnen"

    Als de rij pinnen op het moederbord van uw bestuurde computer voor de aansluiting op het bedieningspaneel een PANEL met 10-1 pinnen is, zoals hieronder weergegeven:

    ![PANEL met 10-1 pinnen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_1.png){class="glboxshadow"}

    Sluit de kabels aan volgens het onderstaande schema. Zorg ervoor dat de zeefdrukopdruk (dat wil zeggen de teksten HDDLED±, RESET SW, POWER SW, POWERLED+ enzovoort) naar buiten gericht en zichtbaar is, en niet naar binnen gericht en verborgen.

    ![PANEL met 10-1 pinnen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_2.jpg){class="glboxshadow"}
    <small>Vooraanzicht</small>

    ![PANEL met 10-1 pinnen 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_3.jpg){class="glboxshadow"}
    <small>Achteraanzicht</small>

    Gebruik vervolgens de kabelset die bij uw computerbehuizing is geleverd om de andere aansluiting van het ATX Board te verbinden met de bedieningskabel van de computer.

??? "Voor een PANEL met 20-5 pinnen"

    Als de rij pinnen op het moederbord van uw bestuurde computer voor de aansluiting op het bedieningspaneel een PANEL met 20-5 pinnen is, zoals hieronder weergegeven:

    ![PANEL met 20-5 pinnen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_1.jpg){class="glboxshadow"}

    Sluit de kabels aan volgens het onderstaande schema. Zorg ervoor dat de zeefdrukopdruk (dat wil zeggen de teksten HDDLED±, RESET SW, POWER SW, POWERLED+ enzovoort) naar buiten gericht en zichtbaar is, en niet naar binnen gericht en verborgen.

    ![PANEL met 20-5 pinnen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_2.jpg){class="glboxshadow"}
    <small>Vooraanzicht</small>

    ![PANEL met 20-5 pinnen 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_3.png){class="glboxshadow"}
    <small>Achteraanzicht</small>

    Gebruik vervolgens de kabelset die bij uw computerbehuizing is geleverd om de andere aansluiting van het ATX Board te verbinden met de bedieningskabel van de computer.

??? "Voor een PANEL met 20-8 pinnen"

    Als de rij pinnen op het moederbord van uw bestuurde computer voor de aansluiting op het bedieningspaneel een PANEL met 20-8 pinnen is, zoals hieronder weergegeven:

    ![PANEL met 20-8 pinnen 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_1.jpg){class="glboxshadow"}

    Sluit de kabels aan volgens het onderstaande schema. Zorg ervoor dat de zeefdrukopdruk (dat wil zeggen de teksten HDDLED±, RESET SW, POWER SW, POWERLED+ enzovoort) naar buiten gericht en zichtbaar is, en niet naar binnen gericht en verborgen.

    ![PANEL met 20-8 pinnen 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_2.png){class="glboxshadow"}

    Gebruik vervolgens de kabelset die bij uw computerbehuizing is geleverd om de andere aansluiting van het ATX Board te verbinden met de bedieningskabel van de computer.

Het volledig aangesloten ATX Board ziet er als volgt uit.

![ATX Board aangesloten](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected1.png){class="glboxshadow gl-90-desktop"}

![ATX Board aangesloten](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected2.png){class="glboxshadow gl-90-desktop"}

Installeer vervolgens de beugel van het ATX Board in de computerbehuizing.

![ATX Board installeren](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install1.png){class="glboxshadow gl-90-desktop"}

![ATX Board installeren](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install2.png){class="glboxshadow gl-90-desktop"}

### 3. ATX Board en KVM verbinden {#3-connect-atx-board-and-kvm}

Verbind de Type-C-poort van het ATX Board met de meegeleverde USB-kabel met de USB-A-poort van het KVM-apparaat (zoals de Comet GL-RM1).

![ATX Board installeren](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install3.png){class="glboxshadow gl-90-desktop"}

![ATX Board installeren](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install4.png){class="glboxshadow gl-90-desktop"}

Hiermee is de installatie van het ATX Board voltooid.

![ATX Board installeren](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install5.png){class="glboxshadow gl-90-desktop"}

U kunt zich nu aanmelden bij uw KVM en naar **Accessories** gaan om de ATX-voeding te bedienen.

![ATX-voeding](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/atx_power.png){class="glboxshadow gl-90-desktop"}

## Veelgestelde vragen {#faq}

**V1. Kan ik het GL-ATXPC-board gebruiken met KVM-apparaten die niet van GL.iNet zijn?**

A1. Nee. Het GL-ATXPC-board is een accessoire voor KVM-apparaten van GL.iNet en moet samen met een GL.iNet KVM worden gebruikt.

---

**V2. Wat kan ik doen als ik na de installatie van het ATX Board de voeding van het externe apparaat niet via de KVM kan in- of uitschakelen?**

A2. Probeer de volgende methoden.

- Controleer of het bestuurde apparaat normaal in- en uitgeschakeld kan worden met de fysieke aan/uit-knop op het voorpaneel van de pc-behuizing.

- Controleer de polariteit van de bedrading. Draai de polariteit van de POWER SW-connector op het moederbord van het bestuurde apparaat om, om onjuiste bedrading uit te sluiten.

    ![Polariteit van de connector](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/power-sw-connector.png){class="glboxshadow gl-90-desktop"}

- Zorg er bij het aansluiten op de F_PANEL-aansluiting op het moederbord van het bestuurde apparaat voor dat de zeefdrukopdruk (bijvoorbeeld HDDLED±, RESET SW, POWER SW, POWERLED+ enzovoort) naar buiten gericht en zichtbaar is, en niet naar binnen gericht en verborgen.

- Voer een upgrade uit van de firmware van de KVM.

---

**V3. Kan ik met één GL.iNet KVM meerdere ATX Boards bedienen?**

A3. De volgende GL.iNet KVM's kunnen slechts één ATX Board bedienen.

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)

Comet X (GL-RM4PE) ondersteunt daarentegen maximaal vier ATX Boards tegelijk. Comet X heeft vier onafhankelijke kanalen op het achterpaneel. Elk kanaal heeft een HDMI-poort voor de overdracht van videosignalen, een Type-C-poort voor de overdracht van toetsenbord- en muissignalen en een USB 2.0-poort voor USB-randapparaten (bijvoorbeeld een Fingerbot of ATX Board).

**Opmerking**: Comet Q (GL-RMQ1) werkt niet met het ATX Board.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
