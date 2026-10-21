# Firmware v1.9 {#firmware-v19}

Deze release biedt nieuwe functionele uitbreidingen, betere interactiviteit, sterkere privacybescherming en betrouwbaardere netwerkverbindingen – allemaal bedoeld voor een completere, stabielere en veiligere externe KVM-ervaring.

Download de nieuwste firmware via het [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"}

## Latentiemodus {#latency-mode}

Deze firmware introduceert **Latency Mode**, waarmee u een balans vindt tussen invoerreactiviteit en vloeiend beeld. U kunt Latency Mode instellen op Lowest Latency of Smooth Display om de prestaties bij bediening op afstand te optimaliseren.

![Latentiemodus](https://static.gl-inet.com/docs/kvm/features_update/1.9/latency_mode.png){class="glboxshadow" width="360"}
    
- Lowest Latency: minimaliseert de invoerlatentie voor een snellere reactie van toetsenbord en muis.
- Smooth Display: optimaliseert de beelduitvoer om haperingen en framedrops te voorkomen en zorgt voor een stabiele weergave.

## Gebruiksgemak van de muis {#mouse-usability}

Er is een nieuwe optie **Primary Button** toegevoegd om het gebruiksgemak van de muis te verbeteren. U kunt de linker- of rechterknop als primaire knop instellen, afhankelijk van uw persoonlijke voorkeur.

![Primaire knop](https://static.gl-inet.com/docs/kvm/features_update/1.9/primary_button.png){class="glboxshadow" width="360"}

## Schermweergave {#screen-display}

Via het touchscreen kunt u de instellingen voor **Screen Display** van de KVM aanpassen, waaronder schermvergrendeling, achtergrond, tijdnotatie (24-uurs/12-uurs) en datumnotatie. Deze functie is alleen beschikbaar op modellen met een touchscreen.

Daarnaast kunt u overlaytools zoals Tailscale en NetBird met een paar tikken rechtstreeks via het touchscreen configureren – een functie die in eerdere firmwareversies niet beschikbaar was.

![Schermweergave](https://static.gl-inet.com/docs/kvm/features_update/1.9/screen_display.png){class="glboxshadow" width="360"}

## Taal {#language}

Eerdere firmwareversies ondersteunden alleen Chinees en Engels; deze versie voegt ondersteuning voor **Japans** toe, zodat de interface toegankelijker is voor Japanse gebruikers.

![Taal](https://static.gl-inet.com/docs/kvm/features_update/1.9/language.png){class="glboxshadow" width="360"}

## Uitbreidingen {#extensions}

Deze release integreert [NetBird](https://netbird.io/){target="_blank"}, een opensource zero-trust-netwerkplatform voor het opzetten van veilige privénetwerken voor thuis en op het werk. Deze overlayoplossing is gebaseerd op WireGuard® en biedt via virtuele NetBird-netwerken overal veilige externe toegang tot uw KVM. Zie [hier](../faq/remote_access_via_netbird.md){target="_blank"} voor installatie-instructies.

![NetBird](https://static.gl-inet.com/docs/kvm/features_update/1.9/netbird.png){class="glboxshadow"}

## Overige verbeteringen {#other-enhancements}

- Bètafirmwareprogramma: gebruikers kunnen deelnemen aan het bètaprogramma om functies te testen voordat ze officieel worden uitgebracht.

- Tekstherkenning: met behulp van optische tekenherkenning (OCR) kunt u tekst overnemen uit elk geselecteerd gebied op het externe scherm. Ondersteunde talen zijn Chinees, Engels en een tweetalige modus Chinees-Engels. Zie [hier](../tutorials/how_to_capture_text_from_remote_screen.md) voor meer informatie.

- Tijdzone op basis van stad: stel uw tijdzone in door een stad te selecteren.

- Beveiliging van aanmeldsessies: aanmeldtokens verlopen nu 12 uur na het beëindigen van de sessie (voorheen waren tokens permanent geldig).

- Beveiliging van systeemlogboeken: gevoelige gegevens worden in alle systeemlogboeken gemaskeerd.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
