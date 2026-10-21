# Veelgestelde vragen over Comet Q {#frequently-asked-questions-about-comet-q}

## Algemeen {#general}

1. **V: Wat moet ik doen als het KVM-bedieningsscherm "Unable to Display" toont wanneer de Comet Q op het bestuurde apparaat is aangesloten?**

    A: Dit komt doordat uw bestuurde apparaat geen **USB-C DisplayPort Alt Mode** ondersteunt, waardoor er geen videostream kan worden uitgevoerd.
    
    Zie [hier](../../tutorials/how_to_check_usb-c_port_dp_alt_mode.md) om te controleren of uw apparaat DisplayPort Alt Mode ondersteunt.

2. **V: Waarom kan het besturende apparaat het toetsenbord voor het invoeren van het wachtwoord niet weergeven wanneer het scherm van het bestuurde apparaat is vergrendeld?**
    
    A: Vanwege beveiligingsbeperkingen van iOS/Android blokkeert het systeem de pagina voor wachtwoordinvoer tijdens schermspiegeling of bediening op afstand. U kunt het ontgrendelwachtwoord rechtstreeks vanaf het besturende apparaat invoeren om uw apparaat te ontgrendelen.

3. **V: Waarom wordt het geluid niet naar het besturende apparaat verzonden wanneer er op het bestuurde apparaat een spraakoproep wordt gevoerd?**
    
    A: Dit probleem doet zich vaak voor op iPhones en sommige Android-apparaten. Wanneer op het bestuurde apparaat software voor spraakcommunicatie (bijvoorbeeld WhatsApp of Microsoft Teams) wordt gebruikt voor spraakoproepen, kan het geluid door systeembeperkingen van iOS/Android alleen via de lokale luidsprekers van het bestuurde apparaat worden afgespeeld en niet via de KVM naar het besturende apparaat worden verzonden.

    **Tip**: Media-audio (video's, muziek, games enzovoort) kan normaal via de KVM naar het besturende apparaat worden verzonden wanneer er geen apps voor spraakcommunicatie actief zijn.

## iOS {#ios}

1. **V: Waarom kan ik het systeemvolume op iOS-apparaten niet aanpassen nadat ik verbinding heb gemaakt met de Comet Q?**
    
    A: Door beperkingen van iOS is de systeemeigen volumeregeling niet meer beschikbaar zodra een iPhone/iPad is verbonden met een apparaat voor schermspiegeling, zoals een GL.iNet KVM, dat als audio-uitvoer is ingesteld.

2. **V: Waarom toont het iOS-apparaat geen lokaal videobeeld bij het streamen van video's via video-apps?**

    A: Wanneer een iOS-apparaat is verbonden met een apparaat voor schermspiegeling, zoals een GL.iNet KVM, voeren sommige video-apps (bijvoorbeeld YouTube of Netflix) video standaard uit via **AirPlay**. Daardoor toont het iOS-apparaat geen lokaal videobeeld. Dit gedrag kan niet op systeemniveau worden uitgeschakeld.
    
    Als u wilt dat het bestuurde apparaat video's tijdens het spiegelen lokaal afspeelt, speelt u de video's in plaats daarvan af via een webbrowser.

3. **V: Wat moet ik doen als het schermtoetsenbord van het iOS-apparaat verdwijnt nadat het met de Comet Q is verbonden?**
    
    A: Waarschijnlijk herkent iOS de Comet Q als een extern fysiek toetsenbord en verbergt het systeem automatisch het eigen schermtoetsenbord. Gebruik in dat geval het toetsenbord van het besturende apparaat of het virtuele toetsenbord in de KVM-console.
    
    Als u het schermtoetsenbord van iOS toch wilt gebruiken, gaat u naar **Settings** > **Accessibility** > **Touch** > **AssistiveTouch** en schakelt u **Show Onscreen Keyboard** in.

    ![AssistiveTouch](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/assistive_touch.png){class="glboxshadow" width="360"}

4. **V: Bij het spiegelen van een iPhone/iPad in staande/liggende stand blijft de muis op het besturende apparaat verschoven, zelfs nadat ik de schermstand in de KVM-console heb aangepast. Wat moet ik doen?**
    
    A: Voor nauwkeurige aanwijzerbesturing op een iPhone of iPad moet de oriëntatie van de gyroscoop van het apparaat exact overeenkomen met de weergegeven schermstand. Tijdens bediening op afstand kan het systeem de huidige toestand van de gyroscoop soms niet correct detecteren, waardoor de muis verschuift.
    
    Schakel ter oplossing **Portrait Orientation Lock**/**Rotation Lock** in op uw iPhone/iPad, zodat de aanwijzer nauwkeurig wordt gevolgd.

    ![Vergrendeling staande stand](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/portrait_lock.png){class="glboxshadow" width="360"}  
    <small>(Portrait Orientation Lock op een iPhone)</small>

5. **V: Waarom werkt het toetsenbord niet goed op iOS-apparaten, waarbij sommige toetsen niet werken of de muisaanwijzer verschuift?**

    A: Dit probleem wordt meestal veroorzaakt doordat de functie **Mouse Keys** op het iOS-apparaat is ingeschakeld. Met Mouse Keys kunnen gebruikers de muisaanwijzer bewegen met een toetsenbord of numeriek toetsenblok.

    Ga ter oplossing naar **Settings** > **Accessibility** > **Touch** > **AssistiveTouch** > **Mouse Keys** en schakel Mouse Keys uit.

## Android {#android}

1. **V: Waarom kan ik het apparaat niet bedienen in de absolute muismodus?**
    
    A: Door beperkingen van het Android-besturingssysteem kunnen Android-apparaten alleen in de relatieve muismodus worden bediend.
    
    Wanneer u via de mobiele GLKVM-app bedient, bedekt u de muisaanwijzer volledig met uw vinger om handelingen uit te voeren.

2. **V: Wat moet ik doen als het scherm op het besturende apparaat niet synchroon loopt met het scherm van de bestuurde Android-telefoon?**
    
    A: Sommige Android-telefoons herkennen de Comet Q als een uitgebreid beeldscherm in plaats van een gespiegeld scherm. Wijzig ter oplossing de weergave-instelling op uw telefoon naar de modus **Screen Mirroring**.

    Neem de Samsung S-serie als voorbeeld:
    
    Ga naar **Settings** > **Device Connections** > **Samsung DeX** > **Connected Display** en selecteer de modus **Screen Mirroring**.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
