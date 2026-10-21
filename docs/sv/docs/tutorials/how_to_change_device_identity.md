# Så ändrar du KVM-enhetens enhetsidentitet {#how-to-change-kvm-device-identity}

## Vad är KVM-enhetens enhetsidentitet? {#what-is-kvm-device-identity}

Enhetsidentiteten för GL.iNet KVM är den identifierare som gör att KVM-enheten kan identifieras och särskiljas av den anslutna enheten under kommunikationen.

KVM-enheten har vanligtvis en Type-C-port, enligt bilden nedan, som ansluts till den styrda enhetens USB-port för att emulera kringutrustning (t.ex. tangentbord, mus, USB-minne, mikrofon) och cd-rom.

![Type-C-port på GL-RM1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

När du klickar med musen, skriver på tangentbordet eller använder mikrofonen på den styrande sidan överförs signalerna på distans till den fysiska KVM-enheten. KVM-enheten vidarebefordrar dem sedan till den styrda enheten via sin Type-C-port.

KVM-enheten uppfattas därför vanligtvis som en sammansatt enhet som emulerar flera enheter för kringutrustning som är anslutna till den styrda enhetens USB-portar.

![Princip för enhetsidentitet](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/principle.png){class="glboxshadow"}

!!! Note "Obs!"

    Om inmatningsmetoden/tangentbordet på den styrande enheten inte överensstämmer med den styrda enhetens kan vissa symboler/bokstäver ha olika positioner på tangentbordet. Det kan göra att det som den styrda sidan matar ut inte stämmer överens med det som matas in på den styrande sidan. Klicka [här](../faq/keyboard_does_not_input_output_as_expected.md) för mer information.

## Varför ändra enhetsidentiteten? {#why-change-device-identity}

Eftersom GL.iNet KVM fungerar som en kombinerad emulator av flera enheter för användarinteraktion identifieras den, när den ansluts till den styrda enheten, som en uppsättning av flera enheter, bland annat en skärm, flera USB-enheter som mus och tangentbord samt ett USB-minne.

Som standard är enhetsidentiteten **GLKVM**, och därför visas den som GLKVM eller Glinet Composite Device i systeminställningarna på den styrda enheten. Det brukar inte vara något problem, eftersom inställningarna bara syns för användaren själv.

![Standardidentitet för enheten](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}
<small>(Inställningar för Bluetooth och enheter)</small>

![Högtalarinställningar](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(Högtalarinställningar)</small>

I följande scenarier kan användare dock behöva ändra KVM-enhetens enhetsidentitet.

??? "Scenario 1: Undvika varningar från övervakningsprogram på en kontorsdator"

    Om den styrda enheten är en kontorsdator kan den ha inbyggda eller installerade övervakningsprogram. Sådana verktyg kan markera fjärråtkomst via KVM som onormal aktivitet, utlösa varningar och till och med rapportera till IT-system.

    Genom att ändra KVM-enhetens enhetsidentitet kan du undvika sådana onödiga meddelanden, samtidigt som fjärrstyrningen fungerar som vanligt.

??? "Scenario 2: Dölja användningen av KVM vid skärmdelning i onlinemöten"

    Under onlinemöten med skärmdelning kan den styrda enhetens systeminställningar (t.ex. Bluetooth och enheter) visa KVM-enhetens standardidentitet. Det kan avslöja för mötesdeltagarna att du använder KVM för fjärråtkomst, vilket vissa användare inte vill.

    Genom att ändra enhetsidentiteten förblir KVM-enheten dold på delade skärmar.

    ![Skärmdelning](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/screen_sharing.png){class="glboxshadow"}
    <small>(skärmdelning)</small>

??? "Scenario 3: Åtgärda mus/tangentbord som inte svarar på den styrda enheten"

    Om du inte kan styra musen och tangentbordet på den styrda enheten via KVM-enheten kan du prova att ändra KVM-enhetens enhetsidentitet för att undvika kompatibilitetsproblem, så att signalerna överförs smidigt mellan KVM-enheten och den styrda enheten.

## Begränsningar vid anpassning av enhetsidentiteten {#limitations-of-device-identity-customization}

!!! Warning "Program för beteendeanalys kan fortfarande identifiera KVM-enheten"

    Oavsett hur du anpassar USB-enhetens identitet kan USB-**strukturen** för de virtualiserade enheterna (tangentbord, mus, mikrofon, kamera osv.) fortfarande verka misstänkt för program som analyserar beteenden.

    Grundproblemet är att all denna virtualiserade kringutrustning hör till **en enda sammansatt USB-enhet**. En sammansatt enhet med bara tangentbord och mus är relativt vanlig – många trådlösa mottagare för tangentbord/mus (som Logitech Unifying) har en liknande struktur – men en enda sammansatt USB-enhet som samtidigt innehåller **tangentbord, mus och mikrofon** är i praktiken mycket ovanlig.

    Att bara ändra enhetsidentiteten **räcker därför kanske inte** för att undgå avancerad övervakning eller program för beteendeanalys.

## Så ändrar du enhetsidentiteten {#how-to-change-device-identity}

### Firmware v1.10 och senare {#firmware-v110-and-above}

1. Logga in på din KVM och gå till **Settings** uppe till höger. Leta upp **Device Identity** under **USB Devices** och anpassa den.

    ![Anpassa identiteten 1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize1.png){class="glboxshadow"}

2. Klicka på **Confirm** i popup-fönstret för att starta om.

    ![Anpassa identiteten 2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize2.png){class="glboxshadow"}

3. Efter omstarten har enhetsidentiteten ändrats i KVM-konsolen.

    ![Anpassa identiteten 3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize3.png){class="glboxshadow"}

4. Verifiera enhetsidentiteten. I följande exempel används Windows 11 Pro som styrd enhet för att verifiera enhetsidentiteten.

    Gå till **Settings** -> **Bluetooth & devices** på den styrda enheten. Indata- och ljudenheterna har identifierats med de namn som du har angett.

    ![Anpassa identiteten 4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize4.png){class="glboxshadow"}

### Firmware v1.9 och tidigare {#firmware-v19-and-earlier}

1. Logga in på din KVM och gå till **Settings** -> **System** -> **Device Identity**. Välj en förinställd identitet i listrutan.

    ![Anpassa identiteten 1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    Du kan också klicka på **Customize** och fylla i önskade parametrar i popup-fönstret.

    ![Anpassa identiteten 2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. Klicka på **Confirm** i popup-fönstret för att starta om.

    ![Anpassa identiteten 3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. Efter omstarten har enhetsidentiteten ändrats i KVM-konsolen.

    ![Anpassa identiteten 4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

4. Verifiera enhetsidentiteten. I följande exempel används Windows 10 Pro som styrd enhet för att verifiera enhetsidentiteten.

    Gå till **Settings** -> **Bluetooth & devices** på den styrda enheten. Indata- och ljudenheterna har identifierats med de namn som du har angett.

    ![Anpassa identiteten 5](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
