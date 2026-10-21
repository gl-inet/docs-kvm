# Vad gör jag om det inte går att koppla enheten till GLKVM-appen? {#what-should-i-do-if-i-failed-to-bind-device-to-the-glkvm-app}

Med [GLKVM-appen](https://www.gl-inet.com/app-rm/){target="_blank"} får du fjärråtkomst till den styrda enheten från den styrande enheten. Installera bara appen på den styrande enheten och koppla din GL.iNet KVM-enhet till den, så kan du komma åt den styrda enheten på distans när som helst och var som helst.

Kopplingen av enheten kan dock misslyckas av olika anledningar.

Klicka på felmeddelandet nedan för att se motsvarande lösningar.

??? "Binding failed, unable to obtain basic KVM device information."

    ![Kopplingen misslyckades, fel i enhetsinformationen](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_device_info_error.png){class="glboxshadow"}

    1. Kontrollera lysdiodens status. Se till att lysdioden lyser med fast vitt sken och att KVM-enheten är ansluten till internet.
    2. Starta om KVM-enheten, vänta i 2 minuter och försök koppla den igen.
    3. Om du lägger till enheten med serienummer (S/N Code) ska du kontrollera att du anger rätt serienummer.
    4. Följ stegen nedan för att kontrollera nätverket med kommandot **Ping**.

        1. Anslut den styrande enheten till samma nätverk som KVM-enheten.

        2. Starta en webbläsare (Chrome eller Edge rekommenderas) på den styrande enheten och ange `glkvm.local` i adressfältet. Ange administratörslösenordet för att logga in.

            ![Lokal åtkomst via domän](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. När du har loggat in går du till **Toolbox** -> **Terminal** och klickar på **Access** för att logga in i terminalen.

            ![Öppna terminalen](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Pinga `google.com` för att kontrollera nätverksstatusen.

            ![Ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Om nätverket fungerar som det ska får du resultatet nedan.

            ![Ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Om nätverket är instabilt eller inte tillgängligt kontaktar du din internetleverantör eller routerns support.

??? "Device network error, binding failed."

    ![Kopplingen misslyckades, nätverksfel](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_network_error.png){class="glboxshadow"}

    1. Kontrollera lysdiodens status. Se till att lysdioden lyser med fast vitt sken och att KVM-enheten är ansluten till internet.
    2. Starta om KVM-enheten, vänta i 2 minuter och försök koppla den igen.
    3. Kontrollera att molntjänsten är aktiverad.

        Molntjänsten är aktiverad som standard, men om du tidigare har inaktiverat den manuellt misslyckas en ny koppling av enheten till GLKVM-appen. Öppna KVM-enheten lokalt via domännamn eller IP-adress för att aktivera molntjänsten igen.

    4. Följ stegen nedan för att kontrollera nätverket med kommandot **Ping**.

        1. Anslut den styrande enheten till samma nätverk som KVM-enheten.

        2. Starta en webbläsare (Chrome eller Edge rekommenderas) på den styrande enheten och ange `glkvm.local` i adressfältet. Ange administratörslösenordet för att logga in.

            ![Lokal åtkomst via domän](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. När du har loggat in går du till **Toolbox** -> **Terminal** och klickar på **Access** för att logga in i terminalen.

            ![Öppna terminalen](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Pinga `google.com` för att kontrollera nätverksstatusen.

            ![Ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Om nätverket fungerar som det ska får du resultatet nedan.

            ![Ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Om nätverket är instabilt eller inte tillgängligt kontaktar du din internetleverantör eller routerns support.

??? "Binding failed, KVM is already bound by others."

    ![Kopplingen misslyckades, redan kopplad av någon annan](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_bound_by_others.png){class="glboxshadow"}

    Det betyder att KVM-enheten redan är kopplad till ett annat konto.

    1. Kontrollera om du har kopplat den till en annan av dina e-postadresser. Prova med andra konton om du har några.

    2. Om du lägger till enheten med serienummer (S/N Code) ska du kontrollera att du anger rätt serienummer.

??? "Incorrect Dynamic Binding Code. You have 4 attempts remaining."

    ![Felaktig kopplingskod](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_binding_code.png){class="glboxshadow"}

    Det betyder att du har angett en ogiltig eller utgången kopplingskod.

    1. Logga in på KVM-enhetens administrationskonsol lokalt, gå till **Cloud Service** i det övre högra hörnet och klicka på **Bind with Code** för att få en dynamisk kopplingskod.

    2. För modellen GL-RM10 (Comet Pro) kan du även hämta koden på pekskärmen. Svep till skärmen **Cloud Service** och tryck på **Generate Binding Code**, så visas en dynamisk kopplingskod på pekskärmen. Ange kopplingskoden i GLKVM-appen för att slutföra kopplingen.

        ![Generera kopplingskod](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_code_screen.png){class="glboxshadow"}

    3. Om kopplingskoden har gått ut klickar du på **Regenerate** för att få en ny.

??? "Incorrect Device ID. You have 4 attempts remaining."

    ![Felaktigt enhets-ID](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_device_id.png){class="glboxshadow"}

    Det betyder att du har angett fel enhets-ID (Device ID).

    1. Kontrollera rätt enhets-ID på etiketten på undersidan.

    2. Om du inte kan läsa etiketten på undersidan kan du försöka koppla enheten via lokal åtkomst.

        Logga in på KVM-enhetens administrationskonsol lokalt, gå till **Cloud Service** i det övre högra hörnet och klicka på **Bind To KVM Cloud**. Du omdirigeras då till kopplingssidan med en unik token. Logga in med ditt molnkonto och bekräfta enhetsinformationen för att slutföra kopplingen.

??? "Övrigt"

    Kontrollera om VPN är aktiverat på den styrande enheten där GLKVM-appen är installerad.

    Inaktivera all VPN- och proxyprogramvara, inklusive AstroWarp, Tailscale och ZeroTier, och försök sedan koppla din KVM till GLKVM-appen igen.

Om problemet kvarstår kontaktar du oss på [support@gl-inet.com](mailto:support@gl-inet.com) och anger enhetsmodell, firmwareversion och MAC-adress.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
