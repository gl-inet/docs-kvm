# Vanliga frågor om Comet Q {#frequently-asked-questions-about-comet-q}

## Allmänt {#general}

1. **F: Vad ska jag göra om KVM-styrskärmen visar "Unable to Display" när Comet Q ansluts till den styrda enheten?**

    S: Det beror på att den styrda enheten inte stöder **USB-C DisplayPort Alt Mode**, vilket förhindrar utmatning av videoströmmen.

    Se [här](../../tutorials/how_to_check_usb-c_port_dp_alt_mode.md) hur du kontrollerar om din enhet stöder DisplayPort Alt Mode.

2. **F: Varför kan den styrande enheten inte visa tangentbordet för lösenordsinmatning när den styrda enhetens skärm är låst?**

    S: På grund av säkerhetsbegränsningar i iOS/Android blockerar systemet sidan för lösenordsinmatning vid skärmspegling eller fjärrstyrning. Du kan ange upplåsningslösenordet direkt från den styrande sidan för att låsa upp enheten.

3. **F: Varför överförs inte ljudet till den styrande enheten när den styrda enheten används för ett röstsamtal?**

    S: Problemet uppstår ofta på iPhone och vissa Android-enheter. När programvara för röstkommunikation (t.ex. WhatsApp, Microsoft Teams) används för röstsamtal på den styrda enheten kan ljudet, på grund av systembegränsningar i iOS/Android, bara spelas upp via den styrda enhetens lokala högtalare och kan inte överföras till den styrande sidan via KVM-enheten.

    **Tips!** Medieljud (videor, musik, spel osv.) kan överföras normalt till den styrande sidan via KVM-enheten när appar för röstkommunikation inte är aktiva.

## iOS {#ios}

1. **F: Varför kan jag inte justera systemvolymen på iOS-enheter efter att de har anslutits till Comet Q?**

    S: På grund av begränsningar i iOS blir systemets inbyggda volymkontroll otillgänglig när en iPhone/iPad ansluts till en skärmspeglingsenhet, till exempel en GL.iNet KVM, som har angetts som ljudutgång.

2. **F: Varför visar iOS-enheten ingen lokal videobild när jag strömmar video i videoappar?**

    S: När en iOS-enhet ansluts till en skärmspeglingsenhet, till exempel en GL.iNet KVM, matar vissa videoappar (t.ex. YouTube, Netflix) som standard ut videon via **AirPlay**, och därför visar iOS-enheten ingen lokal videobild. Detta beteende kan inte inaktiveras på systemnivå.

    Om du vill att den styrda enheten ska spela upp videor lokalt medan den speglas spelar du i stället upp videorna i en webbläsare.

3. **F: Vad ska jag göra om skärmtangentbordet försvinner från iOS-enheten efter att den har anslutits till Comet Q?**

    S: Troligen identifierar iOS Comet Q som ett externt fysiskt tangentbord och döljer automatiskt det inbyggda skärmtangentbordet. Använd i så fall tangentbordet på den styrande enheten eller det virtuella tangentbordet i KVM-konsolen.

    Om du ändå behöver använda skärmtangentbordet i iOS går du till **Settings** > **Accessibility** > **Touch** > **AssistiveTouch** och aktiverar **Show Onscreen Keyboard**.

    ![AssistiveTouch](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/assistive_touch.png){class="glboxshadow" width="360"}

4. **F: När jag speglar en iPhone/iPad i stående/liggande läge hamnar musen på den styrande sidan fortfarande ur position, även efter att jag har justerat skärmorienteringen i KVM-konsolen. Vad ska jag göra?**

    S: För exakt markörspårning på iPhone eller iPad måste enhetens gyroskoporientering och den visade skärmorienteringen stämma exakt överens. Vid fjärrstyrning kan systemet misslyckas med att identifiera gyroskopets aktuella läge korrekt, vilket leder till att musen hamnar fel.

    Åtgärda detta genom att aktivera **Portrait Orientation Lock**/**Rotation Lock** på din iPhone/iPad, så att markörspårningen blir exakt.

    ![Låst stående läge](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/portrait_lock.png){class="glboxshadow" width="360"}
    <small>(Låst stående läge på iPhone)</small>

5. **F: Varför fungerar tangentbordet inte korrekt på iOS-enheter, där vissa tangenter inte fungerar eller muspekaren driver iväg?**

    S: Problemet orsakas vanligtvis av att funktionen **Mouse Keys** är aktiverad på iOS-enheten. Med Mouse Keys kan användaren flytta muspekaren med ett tangentbord eller en numerisk knappsats.

    Lös problemet genom att gå till **Settings** > **Accessibility** > **Touch** > **AssistiveTouch** > **Mouse Keys** och inaktivera Mouse Keys.

## Android {#android}

1. **F: Varför kan jag inte styra enheten i absolut musläge?**

    S: På grund av begränsningar i Android-operativsystemet kan Android-enheter bara styras i relativt musläge.

    När du styr via GLKVM-mobilappen täcker du muspekaren helt med fingret för att utföra åtgärder.

2. **F: Vad ska jag göra om skärmen som visas på den styrande sidan inte är synkroniserad med skärmen på den styrda Android-telefonen?**

    S: Vissa Android-telefoner identifierar Comet Q som en utökad skärm i stället för en speglad skärm. Åtgärda detta genom att ändra skärminställningen på telefonen till läget **Screen Mirroring**.

    Med Samsung S-serien som exempel:

    Gå till **Settings** > **Device Connections** > **Samsung DeX** > **Connected Display** och välj läget **Screen Mirroring**.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
