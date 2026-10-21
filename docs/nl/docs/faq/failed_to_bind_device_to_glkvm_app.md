# Wat moet ik doen als het koppelen van een apparaat aan de GLKVM-app mislukt? {#what-should-i-do-if-i-failed-to-bind-device-to-the-glkvm-app}

Met de [GLKVM-app](https://www.gl-inet.com/app-rm/){target="_blank"} kunt u vanaf het besturende apparaat op afstand toegang krijgen tot uw bestuurde apparaat. Installeer de app op uw besturende apparaat en koppel uw GL.iNet KVM-apparaat eraan; daarna kunt u het bestuurde apparaat altijd en overal op afstand openen.

Het koppelen van het apparaat kan echter om verschillende redenen mislukken.

Klik hieronder op de foutmelding voor de bijbehorende oplossingen.

??? "Binding failed, unable to obtain basic KVM device information."

    ![Koppelen mislukt: fout bij apparaatgegevens](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_device_info_error.png){class="glboxshadow"}

    1. Controleer de status van de led. Zorg ervoor dat de led continu wit brandt en dat uw KVM-apparaat met internet is verbonden.
    2. Start uw KVM-apparaat opnieuw op, wacht 2 minuten en probeer het apparaat opnieuw te koppelen.
    3. Als u het apparaat toevoegt met de S/N-code, controleer dan of u het juiste serienummer invoert.
    4. Volg de onderstaande stappen om het netwerk te controleren met de opdracht **Ping**.
       
        1. Verbind uw besturende apparaat met hetzelfde netwerk als uw KVM.

        2. Open een browser (Chrome of Edge wordt aanbevolen) op het besturende apparaat en voer `glkvm.local` in de adresbalk in. Voer het beheerderswachtwoord in om u aan te melden.

            ![Lokale toegang via domeinnaam](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. Ga na het aanmelden naar **Toolbox** -> **Terminal** en klik op **Access** om u bij de terminal aan te melden.

            ![Terminal openen](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Ping `google.com` om de netwerkstatus te controleren.
        
            ![Ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Als het netwerk goed werkt, krijgt u het resultaat dat hieronder wordt weergegeven.

            ![Ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}
            
            Als het netwerk onstabiel of niet beschikbaar is, neemt u contact op met uw internetprovider of de ondersteuning van uw router.

??? "Device network error, binding failed."

    ![Koppelen mislukt: netwerkfout](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_network_error.png){class="glboxshadow"}

    1. Controleer de status van de led. Zorg ervoor dat de led continu wit brandt en dat uw KVM-apparaat met internet is verbonden.
    2. Start uw KVM-apparaat opnieuw op, wacht 2 minuten en probeer het apparaat opnieuw te koppelen.
    3. Controleer of de cloudservice is ingeschakeld.

        De cloudservice is standaard ingeschakeld. Als u deze eerder handmatig hebt uitgeschakeld, mislukt het opnieuw koppelen van het apparaat aan de GLKVM-app. Open uw KVM-apparaat lokaal via de domeinnaam of het IP-adres om de cloudservice weer in te schakelen.

    4. Volg de onderstaande stappen om het netwerk te controleren met de opdracht **Ping**.
       
        1. Verbind uw besturende apparaat met hetzelfde netwerk als uw KVM.

        2. Open een browser (Chrome of Edge wordt aanbevolen) op het besturende apparaat en voer `glkvm.local` in de adresbalk in. Voer het beheerderswachtwoord in om u aan te melden.

            ![Lokale toegang via domeinnaam](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. Ga na het aanmelden naar **Toolbox** -> **Terminal** en klik op **Access** om u bij de terminal aan te melden.

            ![Terminal openen](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Ping `google.com` om de netwerkstatus te controleren.
        
            ![Ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Als het netwerk goed werkt, krijgt u het resultaat dat hieronder wordt weergegeven.

            ![Ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Als het netwerk onstabiel of niet beschikbaar is, neemt u contact op met uw internetprovider of de ondersteuning van uw router.

??? "Binding failed, KVM is already bound by others."

    ![Koppelen mislukt: al door anderen gekoppeld](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_bound_by_others.png){class="glboxshadow"}

    Dit betekent dat het KVM-apparaat al aan een ander account is gekoppeld.
    
    1. Controleer of u het apparaat aan een ander e-mailadres van u hebt gekoppeld. Probeer eventuele andere accounts.
    
    2. Als u het apparaat toevoegt met de S/N-code, controleer dan of u het juiste serienummer invoert.

??? "Incorrect Dynamic Binding Code. You have 4 attempts remaining."

    ![Onjuiste koppelingscode](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_binding_code.png){class="glboxshadow"}

    Dit betekent dat u een ongeldige of verlopen koppelingscode hebt ingevoerd.
    
    1. Meld u lokaal aan bij de beheerconsole van uw KVM, ga rechtsboven naar **Cloud Service** en klik op **Bind with Code** om een dynamische koppelingscode te krijgen.
    
    2. Bij het model GL-RM10 (Comet Pro) kunt u de code ook via het touchscreen opvragen. Veeg naar het scherm **Cloud Service** en tik op **Generate Binding Code**; er verschijnt dan een dynamische koppelingscode op het touchscreen. Voer deze koppelingscode in de GLKVM-app in om de koppeling te voltooien.

        ![Koppelingscode genereren](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_code_screen.png){class="glboxshadow"}
    
    3. Als de koppelingscode is verlopen, klikt u op **Regenerate** om een nieuwe code te krijgen.

??? "Incorrect Device ID. You have 4 attempts remaining."

    ![Onjuiste apparaat-ID](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_device_id.png){class="glboxshadow"}

    Dit betekent dat u een onjuiste apparaat-ID hebt ingevoerd.
    
    1. Controleer het label aan de onderkant voor de juiste apparaat-ID.
    
    2. Als u het label aan de onderkant niet kunt controleren, probeer het apparaat dan te koppelen via lokale toegang.
    
        Meld u lokaal aan bij de beheerconsole van uw KVM, ga rechtsboven naar **Cloud Service** en klik op **Bind To KVM Cloud**. U wordt dan met een uniek token doorgestuurd naar de koppelingspagina. Meld u aan met uw cloudaccount en bevestig de apparaatgegevens om de koppeling te voltooien.

??? "Overig"

    Controleer of er een VPN is ingeschakeld op het besturende apparaat waarop de GLKVM-app is geïnstalleerd.
    
    Schakel alle VPN- of proxysoftware uit, waaronder AstroWarp, Tailscale en ZeroTier, en probeer uw KVM daarna opnieuw aan de GLKVM-app te koppelen.

Als het probleem zich blijft voordoen, neemt u contact met ons op via [support@gl-inet.com](mailto:support@gl-inet.com) en vermeldt u het apparaatmodel, de firmwareversie en het MAC-adres.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
