# Wat moet ik doen als het toetsenbord niet de verwachte invoer of uitvoer geeft? {#what-shoud-i-do-if-keyboard-does-not-input-or-output-as-expected}

Als het besturende en het bestuurde apparaat **verschillende invoermethoden of toetsenbordindelingen** gebruiken, worden symbolen en tekens zoals "!", "@" en "#" die u lokaal invoert, mogelijk niet correct aan de externe kant weergegeven.

## Waarom gebeurt dit? {#why-does-it-happen}

De KVM wordt door het bestuurde apparaat als toetsenbord gezien. De toetsen die u op het toetsenbord van het besturende apparaat indrukt, worden op basis van de bijbehorende toetsposities naar de KVM verzonden en vervolgens aan het bestuurde apparaat toegewezen.

Als de invoermethode of het toetsenbord van het besturende apparaat niet overeenkomt met die van het bestuurde apparaat, staan sommige symbolen of letters op een andere plek op het toetsenbord. Daardoor komt de uitvoer aan de bestuurde kant niet overeen met de invoer aan de besturende kant.

![Vergelijking van US- en JIS-toetsenborden](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/apple-keyboards-US-JIS.jpg){class="glboxshadow"}

## Oplossingen {#solutions}

U kunt op het bestuurde apparaat de invoermethode of het toetsenbord voor de betreffende taal installeren, zodat de toetstoewijzing overeenkomt.

??? "Windows"

    1. Ga naar **Settings** -> **Time & Language** -> **Language** -> **Preferred Language**. Klik op **Add a language**.

        ![Een taal toevoegen](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/add_language.png){class="glboxshadow"}

    2. Kies een taal om te installeren.

        ![Een taal kiezen](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/choose_language.png){class="glboxshadow"}

??? "macOS"

    1. Kies op uw Mac **Apple menu** > **System Settings** en klik in de zijbalk op **Keyboard**. (Mogelijk moet u omlaag scrollen.)
    
    2. Ga naar **Text Input** en klik op **Edit**.
    
    3. Klik op de knop **Add** en zoek naar een taal. Selecteer een of meer invoerbronnen voor elke taal die u wilt gebruiken en klik op **Add**.
    
    4. Als u in een andere taal wilt typen, selecteert u de gewenste taal in het invoermenu in de menubalk.
    
        U kunt in het invoermenu op **Show Keyboard Viewer** klikken om de toetsenbordindeling te zien van de taal die op dat moment is geselecteerd.
        
        Nadat u een invoerbron hebt toegevoegd, wordt het invoermenu automatisch in de menubalk weergegeven. De taal van de invoerbron wordt automatisch toegevoegd aan uw lijst met voorkeurstalen in de instellingen voor Taal en regio en aan uw lijst met dicteertalen (indien beschikbaar) in de toetsenbordinstellingen.

    Bron: [Write in another language on Mac – Apple Support](https://support.apple.com/guide/mac-help/write-in-another-language-on-mac-mchlp1406/mac){target="_blank"}

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
