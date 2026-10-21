# Wat moet ik doen als ik de muis en het toetsenbord niet kan bedienen? {#what-should-i-do-if-i-cannot-control-the-mouse-and-keyboard}

Als u de muis en het toetsenbord van het bestuurde apparaat niet via de KVM kunt bedienen, terwijl alle kabels correct zijn aangesloten, kunt u de volgende suggesties proberen.

1. Controleer de bedrading.

    Neem de Comet (GL-RM1) als voorbeeld. Deze heeft twee USB Type-C-poorten:

    - De poort aan de zijkant heeft het label "5V 2A" en is bedoeld voor de stroomvoorziening (aansluiting op een voedingsadapter).
    - De poort aan de achterkant heeft symbolen voor muis en toetsenbord en wordt aangesloten op de USB-poort van het bestuurde apparaat om toetsenbord- en muissignalen over te dragen.

    Als u deze twee aansluitingen verwisselt, start het KVM-apparaat niet op en reageren muis en toetsenbord niet.
    
    Controleer of deze twee Type-C-aansluitingen correct zijn aangesloten.

    ![Poorten van de GL-RM1](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/gl-rm1-ports.png){class="glboxshadow gl-80-desktop"}

2. Controleer de USB-kabel.

    Gebruik de meegeleverde USB-kabel. Zorg ervoor dat deze de USB-poort van het bestuurde apparaat verbindt met de USB-poort van de KVM en dat de kabel gegevensoverdracht ondersteunt.

    Alleen kabels die gegevens kunnen overdragen, maken bediening van het externe apparaat met toetsenbord en muis mogelijk.

    Sluit de USB-kabel opnieuw aan en start het bestuurde apparaat opnieuw op.

3. Zet de muismodus op de relatieve muismodus.

    Meld u aan bij uw KVM, ga naar Settings -> Mouse Mode, zet de modus op Relative en controleer of het probleem daarmee is opgelost.

    ![Muismodus](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/mouse_mode.jpg){class="glboxshadow"}

4. Schakel de virtuele media uit.

    Meld u aan bij uw KVM, ga naar Virtual Media, klik op het pictogram met de drie puntjes en schakel de virtuele media uit.

    ![Virtuele media uitschakelen](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/disable_virtual_media.png){class="glboxshadow" width="422"}

    Wanneer virtuele media zijn ingeschakeld, simuleert de KVM namelijk een USB-opslagstation dat op het bestuurde apparaat is aangesloten. Sommige apparaten schakelen echter alle USB-invoer uit wanneer ze een onbekend USB-opslagstation detecteren, waardoor muis en toetsenbord niet meer reageren.

5. Wijzig de apparaatidentiteit.

    Meld u aan bij uw KVM, ga naar Settings -> System -> Device Identity en wijzig de identiteit waarmee uw KVM door het bestuurde apparaat wordt herkend.

    ![Apparaatidentiteit wijzigen](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/change_device_identity.png){class="glboxshadow"}

6. Voer een upgrade uit van de firmware van de KVM naar de nieuwste versie. [KVM Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"}

7. Controleer in Apparaatbeheer op de bestuurde computer of er stuurprogramma's niet goed werken.

8. Controleer of het bestuurde apparaat wordt geblokkeerd door IT-beveiligingssoftware.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
