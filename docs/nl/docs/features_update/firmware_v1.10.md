# Firmware v1.10 {#firmware-v110}

Deze release introduceert native WebRTC, realtime gegevensbewaking, centraal beheer van USB-apparaten en een nieuw instellingencentrum. Daarnaast zijn de opstartprestaties, de beveiliging en de stabiliteit van de microfoon verbeterd, voor een soepelere en betrouwbaardere externe KVM-ervaring.

Download de nieuwste firmware via het [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"}

## Modus WebRTC (Native) {#webrtc-native-mode}
Deze firmware introduceert de **WebRTC (Native) Mode**. Deze modus gebruikt de Google WebRTC Library om de streamingprestaties te verbeteren en een soepelere realtime bediening op afstand te bieden.

![WebRTC-modus](https://static.gl-inet.com/docs/kvm/features_update/1.10/webrtc_native_mode.png){class="glboxshadow" width=400}

## Verbindingsstatistieken {#connection-stats}

**Connection Stats** toont realtime verbindingsinformatie en trendgrafieken, waaronder netwerklatentie, jitter, pakketverlies, bitsnelheid, framesnelheid en afspeelvertraging.

Klik op het lijstpictogram om realtime verbindingsgegevens en de apparaatstatus te bekijken.

![Verbindingsstatistieken 1](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_1.png){class="glboxshadow"}

Klik op het grafiekpictogram om trendgrafieken voor netwerklatentie, jitter en pakketverlies te bekijken.

![Verbindingsstatistieken 2](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_2.png){class="glboxshadow"}

## Instellingencentrum {#settings-center}

Deze release voegt een nieuw **Settings Center** toe waarin de instellingen voor USB-apparaten, voorkeuren, netwerk, beveiliging, cloud en systeem zijn samengebracht. Bestaande opties, zoals het configureren van de hostnaam, cloudbeheer en firmware-upgrades, zijn nu eenvoudiger op één plek te vinden.

### USB-apparaten {#usb-devices}

**USB Devices** biedt centraal beheer van geëmuleerde USB-apparaten. Op deze pagina kunt u virtuele randapparaten in- of uitschakelen om de compatibiliteit met de bestuurde host te verbeteren.

![USB-apparaten](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_usb_devices.png){class="glboxshadow"}

- **USB Emulated Devices**: geëmuleerde USB-apparaten in- of uitschakelen, waaronder de muis, het toetsenbord, de microfoon, de camera en virtuele media. Sommige apparaten kunnen niet tegelijk worden ingeschakeld. De beschikbaarheid wordt automatisch bijgewerkt.

- **Device Identity**: hiermee past u de identiteit van de KVM aan zoals die door het bestuurde apparaat wordt herkend. Let op: EDID en apparaatidentiteit blijven gesynchroniseerd. Als u een van beide wijzigt, wordt de andere automatisch bijgewerkt, zodat het apparaat correct wordt herkend.

### Voorkeuren {#preferences}

Met **Preferences** beheert u de lay-outvoorkeuren, de systeeminstellingen en de instellingen van het apparaatscherm.

![Voorkeuren](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences**: hiermee configureert u de werkbalk in de modus voor volledig scherm en de statusbalk in de venstermodus.

- **System Settings**: hiermee stelt u de titel van het browsertabblad, de interfacetaal, de kleurmodus en de tijdzone in.

- **Device Screen**: hiermee bekijkt en configureert u het ingebouwde apparaatscherm, waaronder de vergrendelschermmodus, de tijdnotatie, de datumnotatie en de achtergrond.

    **Opmerking**: Deze functie is alleen beschikbaar op modellen met een ingebouwd scherm.

### Netwerk {#network}

U kunt de netwerkinstellingen van het apparaat bekijken en beheren, waaronder de hostnaam, de ethernetverbinding en de gegevens van het draadloze netwerk.

![Netwerk](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_network.png){class="glboxshadow"}

- **Hostname**: wijzig de hostnaam van het apparaat rechtstreeks in de console. Deze functie is geïntroduceerd in firmware v1.7.0.

- **Ethernet Settings**: bekijk en configureer de ethernetverbinding. U kunt DHCP gebruiken om de netwerkinstellingen automatisch te verkrijgen, of **Static** selecteren om het IP-adres, het netmasker, de gateway en andere vereiste parameters handmatig in te voeren.

- **Wireless**: het IP-adres, de gateway en het MAC-adres worden weergegeven zodra het apparaat verbinding heeft gemaakt met een wifinetwerk.

    **Opmerking**: De functie Wireless is alleen beschikbaar op ondersteunde modellen.

### Beveiliging {#security}

Met **Security** kunt u het beheerderswachtwoord wijzigen, tweestapsverificatie inschakelen en een eigen TLS-certificaat instellen.

![Beveiliging](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_security.png){class="glboxshadow"}

- **Access Password**: beheer het beheerderswachtwoord of schakel tweestapsverificatie (2FA) in om de toegang tot het apparaat te beveiligen.

- **TLS Certificate**: gebruik het standaardcertificaat of upload een eigen certificaat en privésleutel voor toegang via de browser.

### Cloud {#cloud}

Apparaten kunnen via een URL of code aan clouddiensten worden gekoppeld voor externe toegang en extern beheer. U kunt ook de mobiele app downloaden, de verbinding beheren of het apparaat naar behoefte ontkoppelen.

![Cloud](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_cloud.png){class="glboxshadow"}

### Systeem {#system}

Onder **System** vindt u opties voor systeembeheer, firmware-upgrades en ondersteuning.

![Systeem](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_system.png){class="glboxshadow"} 

- **System**: start het apparaat opnieuw op of zet het terug naar de fabrieksinstellingen.

- **Upgrade**: schakel Beta Center in om bètafirmware-updates te ontvangen, of gebruik **Local Upgrade** om firmware vanuit een lokaal bestand te installeren.

- **Help & Support**: exporteer apparaatlogboeken voor probleemoplossing en open gebruikershandleidingen, veelgestelde vragen en andere ondersteuningsdocumentatie.

## Overige verbeteringen {#other-enhancements}

- **Opstartprestaties**: het apparaat start sneller op.

- **Wachtwoordbeleid**: strenger wachtwoordbeleid (minimaal 10 tekens met ten minste twee soorten tekens) voor betere beveiliging.

- **Caps Lock-indicator**: er is een statusindicator voor Caps Lock van het bestuurde apparaat toegevoegd.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
