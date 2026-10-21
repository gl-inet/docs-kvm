# De apparaatidentiteit van de KVM wijzigen {#how-to-change-kvm-device-identity}

## Wat is de apparaatidentiteit van de KVM? {#what-is-kvm-device-identity}

De apparaatidentiteit van een GL.iNet KVM is de identificatie waarmee het aangesloten apparaat de KVM tijdens de communicatie herkent en onderscheidt.

Doorgaans heeft de KVM een Type-C-poort, zoals hieronder weergegeven, die wordt aangesloten op de USB-poort van het bestuurde apparaat om randapparaten (bijvoorbeeld toetsenbord, muis, USB-stick of microfoon) en een cd-rom-station te simuleren.

![Type-C-poort van de GL-RM1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

Wanneer u aan de besturende kant met de muis klikt, op het toetsenbord typt of de microfoon gebruikt, worden deze signalen op afstand naar het fysieke KVM-apparaat verzonden. De KVM stuurt ze vervolgens via de Type-C-poort door naar het bestuurde apparaat.

De KVM wordt daarom meestal gezien als een samengesteld apparaat dat meerdere randapparaten emuleert die op de USB-poorten van het bestuurde apparaat zijn aangesloten.

![Werkingsprincipe van de apparaatidentiteit](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/principle.png){class="glboxshadow"}

!!! Note "Opmerking"

    Als de invoermethode of het toetsenbord van het besturende apparaat niet overeenkomt met die van het bestuurde apparaat, staan sommige symbolen of letters mogelijk op een andere plek op het toetsenbord. Daardoor kan de uitvoer aan de bestuurde kant afwijken van de invoer aan de besturende kant. Klik [hier](../faq/keyboard_does_not_input_output_as_expected.md) voor meer informatie.

## Waarom de apparaatidentiteit wijzigen? {#why-change-device-identity}

Omdat de GL.iNet KVM voor gebruikersinteractie meerdere apparaten tegelijk emuleert, wordt de KVM bij aansluiting op het bestuurde apparaat herkend als een verzameling apparaten, waaronder een monitor, meerdere USB-apparaten zoals muis en toetsenbord, en een USB-stick.

Standaard is de apparaatidentiteit **GLKVM**. Daardoor wordt het apparaat in de systeeminstellingen van het bestuurde apparaat weergegeven als GLKVM of Glinet Composite Device. Dit is meestal geen probleem, omdat deze instellingen alleen voor de gebruikers zelf zichtbaar zijn.

![Standaardapparaatidentiteit](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}
<small>(Instellingen voor Bluetooth en apparaten)</small>

![Luidsprekerinstellingen](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(Luidsprekerinstellingen)</small>

In de volgende situaties kan het echter nodig zijn de apparaatidentiteit van de KVM te wijzigen.

??? "Situatie 1: waarschuwingen van bewakingssoftware op een kantoorcomputer voorkomen"

    Als het bestuurde apparaat een kantoorcomputer is, kan daarop ingebouwde of geïnstalleerde bewakingssoftware draaien. Deze tools kunnen externe toegang via de KVM als afwijkende activiteit aanmerken, waarschuwingen geven en dit zelfs aan IT-systemen melden.
    
    Door de apparaatidentiteit van de KVM te wijzigen, kunt u zulke onnodige meldingen voorkomen, terwijl de bediening op afstand normaal blijft werken.

??? "Situatie 2: gebruik van de KVM verbergen bij het delen van het scherm in online vergaderingen"

    Tijdens online vergaderingen waarbij u uw scherm deelt, kunnen de systeeminstellingen van het bestuurde apparaat (bijvoorbeeld Bluetooth en apparaten) de standaardidentiteit van de KVM tonen. Zo kunnen deelnemers zien dat u externe toegang via een KVM gebruikt, wat sommige gebruikers liever vermijden.

    Door de apparaatidentiteit te wijzigen, blijft de KVM verborgen in gedeelde schermen.

    ![Scherm delen](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/screen_sharing.png){class="glboxshadow"}
    <small>(scherm delen)</small>

??? "Situatie 3: niet-reagerende muis/toetsenbord op het bestuurde apparaat oplossen"

    Als u de muis en het toetsenbord van het bestuurde apparaat niet via de KVM kunt bedienen, kunt u de apparaatidentiteit van de KVM wijzigen om compatibiliteitsproblemen te voorkomen en een soepele signaaloverdracht tussen de KVM en het bestuurde apparaat mogelijk te maken.

## Beperkingen van het aanpassen van de apparaatidentiteit {#limitations-of-device-identity-customization}

!!! Warning "Software voor gedragsdetectie kan de KVM toch herkennen"

    Hoe u de USB-apparaatidentiteit ook aanpast, de USB-**structuur** van de virtuele apparaten (toetsenbord, muis, microfoon, camera enzovoort) kan voor software voor gedragsdetectie nog steeds verdacht lijken.

    Het onderliggende probleem is dat al deze virtuele randapparaten bij **één samengesteld USB-apparaat** horen. Een samengesteld apparaat met alleen een toetsenbord en muis is vrij gebruikelijk – veel ontvangers voor draadloze toetsenborden en muizen (zoals Logitech Unifying) hebben een vergelijkbare structuur – maar één samengesteld USB-apparaat dat tegelijkertijd **een toetsenbord, een muis en een microfoon** bevat, komt in de praktijk zeer zelden voor.

    Alleen het wijzigen van de apparaatidentiteit is daarom **mogelijk niet voldoende** om detectie door geavanceerde bewakingssoftware of software voor gedragsanalyse te voorkomen.

## De apparaatidentiteit wijzigen {#how-to-change-device-identity}

### Firmware v1.10 en hoger {#firmware-v110-and-above}

1. Meld u aan bij uw KVM en ga rechtsboven naar **Settings**. Zoek onder **USB Devices** de optie **Device Identity** en pas deze aan.

    ![Identiteit aanpassen 1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize1.png){class="glboxshadow"}

2. Klik in het pop-upvenster op **Confirm** om opnieuw op te starten.

    ![Identiteit aanpassen 2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize2.png){class="glboxshadow"}

3. Na het opnieuw opstarten is de apparaatidentiteit in de KVM-console gewijzigd.

    ![Identiteit aanpassen 3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize3.png){class="glboxshadow"}

4. Controleer de apparaatidentiteit. In het volgende voorbeeld wordt Windows 11 Pro als bestuurd apparaat gebruikt om de apparaatidentiteit te controleren.

    Ga op het bestuurde apparaat naar **Settings** -> **Bluetooth & devices**. De invoer- en audioapparaten worden nu herkend zoals u ze hebt ingesteld.

    ![Identiteit aanpassen 4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize4.png){class="glboxshadow"}

### Firmware v1.9 en eerder {#firmware-v19-and-earlier}

1. Meld u aan bij uw KVM en ga naar **Settings** -> **System** -> **Device Identity**. Selecteer een vooraf ingestelde identiteit in de vervolgkeuzelijst.

    ![Identiteit aanpassen 1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    U kunt ook op **Customize** klikken en de gewenste parameters invullen in het pop-upvenster.

    ![Identiteit aanpassen 2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. Klik in het pop-upvenster op **Confirm** om opnieuw op te starten.

    ![Identiteit aanpassen 3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. Na het opnieuw opstarten is de apparaatidentiteit in de KVM-console gewijzigd.

    ![Identiteit aanpassen 4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

4. Controleer de apparaatidentiteit. In het volgende voorbeeld wordt Windows 10 Pro als bestuurd apparaat gebruikt om de apparaatidentiteit te controleren.

    Ga op het bestuurde apparaat naar **Settings** -> **Bluetooth & devices**. De invoer- en audioapparaten worden nu herkend zoals u ze hebt ingesteld.

    ![Identiteit aanpassen 5](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
