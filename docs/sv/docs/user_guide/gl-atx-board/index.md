# Användarhandbok för ATX-kort (GL-ATXPC) {#atx-board-gl-atxpc-user-guide}

ATX-kortet är ett valfritt tillbehör till GL.iNet KVM-enheter. Som en smart strömhanteringsmodul gör det det möjligt att fjärrstyra strömförsörjningen till den styrda enheten genom att simulera tryck på den fysiska strömknappen (starta/stänga av/starta om).

ATX-kortet monteras i den styrda enhetens chassi, vilket ger en mer dold och stabil strömhantering.

**Obs!** Comet Q (GL-RMQ1) fungerar inte med ATX-kortet.

![Comet och ATX-kort](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/rm1-and-atx-borad.jpg){class="glboxshadow"}

## Förpackningens innehåll {#package-contents}

![Innehåll i förpackningen](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/inside-the-box.png){class="glboxshadow gl-80-desktop"}

- 1 x ATX-huvudkort
- 1 x 9-stifts kabelsats
- 1 x Skruvförpackning
- 1 x USB-A till Type-C-kabel
- 1 x ATX-fästesats

## Stiftkonfiguration {#pin-out}

![Stiftkonfiguration](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/pinout.jpg){class="glboxshadow gl-80-desktop"}

Beskrivning av gränssnitten:

1. Type-C-gränssnitt: ansluts till KVM-enheten.
2. Knapp för firmwareuppgradering: för mikrokontrollern på ATX-huvudkortet.
3. Återställningsknapp.
4. Ansluts till datorpanelens styrkabel.
5. Ansluts till datorns F_PANEL-gränssnitt.

!!! note "Obs!"

    1. Gränssnitt 4 och 5 kan användas omväxlande. Det innebär att gränssnitt 5 kan anslutas till datorpanelens styrkabel och gränssnitt 4 till F_PANEL.

    2. ATX-kortet har två lysdioder, och båda beter sig på samma sätt som strömlysdioden (blå anger ATX-systemet, grön anger datorns ström). ATX-kortet har ingen lysdiod för hårddisk (HDD). Lysdiodernas status på kortet överensstämmer med strömlysdiodens status på datorns frontpanel.

Diagram över gränssnitt 4/5:

![Gränssnitt](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface.png){class="glboxshadow gl-60-desktop"}

## Installation {#installation}

Se den här videon för att installera ATX-kortet, eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3VEjZgzgI44" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Skruva fast ATX-kortet och fästet {#1-screw-atx-board-and-bracket}

Fäst ATX-kortet och ATX-fästesatsen med de medföljande skruvarna.

![Fastskruvning](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/screwing.jpg){class="glboxshadow gl-90-desktop"}

### 2. Montera ATX-kortet i datorchassit {#2-install-atx-board-into-pc-case}

Anslut gränssnitt 4 och 5 till den styrda datorns styrkabel respektive F_PANEL-gränssnitt.

![Anslutning av gränssnitt](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface_connect.jpg){class="glboxshadow gl-90-desktop"}

Med den 9-stifts kabelsats som ingår i ATX-förpackningen kan du ansluta ett av ATX-kortets gränssnitt 4/5 till den styrda datorns styrkabel eller F_PANEL-gränssnitt.

För att ansluta ATX-kortets andra gränssnitt 4/5 till den styrda datorns styrkabel eller F_PANEL-gränssnitt behöver du använda kabelsatsen som följer med datorchassit.

**Obs!** Gränssnittens polaritet kan variera mellan olika datorchassin. Kontrollera polariteten noga före installationen.

Nedan visas några exempel på hur gränssnitt 4/5 ansluts till den styrda datorns F_PANEL-gränssnitt.

??? "För 10-1-stifts PANEL"

    Om stiftraden på den styrda datorns moderkort som används för anslutning till kontrollpanelen är en 10-1-stifts PANEL, enligt bilden nedan.

    ![10-1-stifts panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_1.png){class="glboxshadow"}

    Anslut enligt diagrammet nedan och se till att silkscreentrycket (dvs. texterna HDDLED±, RESET SW, POWER SW, POWERLED+ osv.) är synligt utåt och inte döljs inåt.

    ![10-1-stifts panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_2.jpg){class="glboxshadow"}
    <small>Framifrån</small>

    ![10-1-stifts panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_3.jpg){class="glboxshadow"}
    <small>Bakifrån</small>

    Använd sedan kabelsatsen som följer med datorchassit för att ansluta ATX-kortets andra gränssnitt till datorns styrkabel.

??? "För 20-5-stifts PANEL"

    Om stiftraden på den styrda datorns moderkort som används för anslutning till kontrollpanelen är en 20-5-stifts PANEL, enligt bilden nedan.

    ![20-5-stifts panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_1.jpg){class="glboxshadow"}

    Anslut enligt diagrammet nedan och se till att silkscreentrycket (dvs. texterna HDDLED±, RESET SW, POWER SW, POWERLED+ osv.) är synligt utåt och inte döljs inåt.

    ![20-5-stifts panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_2.jpg){class="glboxshadow"}
    <small>Framifrån</small>

    ![20-5-stifts panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_3.png){class="glboxshadow"}
    <small>Bakifrån</small>

    Använd sedan kabelsatsen som följer med datorchassit för att ansluta ATX-kortets andra gränssnitt till datorns styrkabel.

??? "För 20-8-stifts PANEL"

    Om stiftraden på den styrda datorns moderkort som används för anslutning till kontrollpanelen är en 20-8-stifts PANEL, enligt bilden nedan.

    ![20-8-stifts panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_1.jpg){class="glboxshadow"}

    Anslut enligt diagrammet nedan och se till att silkscreentrycket (dvs. texterna HDDLED±, RESET SW, POWER SW, POWERLED+ osv.) är synligt utåt och inte döljs inåt.

    ![20-8-stifts panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_2.png){class="glboxshadow"}

    Använd sedan kabelsatsen som följer med datorchassit för att ansluta ATX-kortets andra gränssnitt till datorns styrkabel.

Det färdigkopplade ATX-kortet visas nedan.

![ATX-kortet anslutet](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected1.png){class="glboxshadow gl-90-desktop"}

![ATX-kortet anslutet](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected2.png){class="glboxshadow gl-90-desktop"}

Montera sedan ATX-kortets fäste i datorchassit.

![Montering av ATX-kortet](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install1.png){class="glboxshadow gl-90-desktop"}

![Montering av ATX-kortet](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install2.png){class="glboxshadow gl-90-desktop"}

### 3. Anslut ATX-kortet till KVM-enheten {#3-connect-atx-board-and-kvm}

Anslut ATX-kortets Type-C-port till KVM-enhetens USB-A-port (till exempel Comet GL-RM1) med den medföljande USB-kabeln.

![Montering av ATX-kortet](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install3.png){class="glboxshadow gl-90-desktop"}

![Montering av ATX-kortet](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install4.png){class="glboxshadow gl-90-desktop"}

Därmed är installationen av ATX-kortet klar.

![Montering av ATX-kortet](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install5.png){class="glboxshadow gl-90-desktop"}

Nu kan du logga in på din KVM och gå till **Accessories** för att styra strömmen via ATX-kortet.

![ATX-strömstyrning](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/atx_power.png){class="glboxshadow gl-90-desktop"}

## Vanliga frågor {#faq}

**F1. Kan jag använda GL-ATXPC-kortet med KVM-enheter som inte kommer från GL.iNet?**

S1. Nej. GL-ATXPC-kortet är ett tillbehör till GL.iNet KVM-enheter och ska användas tillsammans med en GL.iNet KVM.

---

**F2. Vad ska jag göra om jag inte kan styra fjärrenhetens ström (på/av) via KVM-enheten efter att ATX-kortet har installerats?**

S2. Prova följande åtgärder.

- Kontrollera att den styrda enheten kan startas och stängas av normalt när du trycker på den fysiska strömknappen på datorchassits frontpanel.

- Kontrollera kablarnas polaritet. Prova att vända på polariteten för POWER SW-kontakten på den styrda enhetens moderkort för att utesluta felaktig koppling.

    ![Kontaktens polaritet](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/power-sw-connector.png){class="glboxshadow gl-90-desktop"}

- När du ansluter till F_PANEL-gränssnittet på den styrda enhetens moderkort ska du se till att silkscreentrycket (t.ex. HDDLED±, RESET SW, POWER SW, POWERLED+ osv.) är synligt utåt och inte döljs inåt.

- Uppgradera KVM-enhetens firmware.

---

**F3. Kan jag använda en enda GL.iNet KVM för att styra flera ATX-kort?**

S3. Följande GL.iNet KVM-enheter kan bara styra ett ATX-kort.

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)

Comet X (GL-RM4PE) stöder däremot upp till fyra ATX-kort samtidigt. Comet X har fyra oberoende kanaler på baksidan. Varje kanal har en HDMI-port för överföring av videosignal, en Type-C-port för överföring av tangentbords- och mussignaler och en USB 2.0-port för USB-kringutrustning (t.ex. Fingerbot eller ATX-kort).

**Obs!** Comet Q (GL-RMQ1) fungerar inte med ATX-kortet.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
