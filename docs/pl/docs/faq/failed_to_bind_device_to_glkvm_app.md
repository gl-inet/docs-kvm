# Co zrobić, jeśli nie udało się powiązać urządzenia z aplikacją GLKVM {#what-should-i-do-if-i-failed-to-bind-device-to-the-glkvm-app}

[Aplikacja GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} umożliwia zdalny dostęp do urządzenia docelowego z urządzenia sterującego. Wystarczy zainstalować aplikację na urządzeniu sterującym i powiązać z nią urządzenie GL.iNet KVM, aby uzyskać dostęp do urządzenia docelowego z dowolnego miejsca i o dowolnej porze.

Powiązanie urządzenia może jednak nie powieść się z różnych przyczyn.

Kliknij poniższy komunikat o błędzie, aby wyświetlić odpowiednie rozwiązania.

??? "Binding failed, unable to obtain basic KVM device information."

    ![Błąd pobierania informacji o urządzeniu podczas powiązania](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_device_info_error.png){class="glboxshadow"}

    1. Sprawdź stan diody LED. Upewnij się, że świeci ciągłym białym światłem, a urządzenie KVM ma połączenie z Internetem.
    2. Uruchom ponownie urządzenie KVM, poczekaj 2 minuty i spróbuj powiązać je ponownie.
    3. Jeśli dodajesz urządzenie za pomocą numeru S/N, upewnij się, że został on wpisany poprawnie.
    4. Wykonaj poniższe czynności, aby sprawdzić połączenie sieciowe poleceniem **Ping**.

        1. Podłącz urządzenie sterujące do tej samej sieci co KVM.

        2. Otwórz przeglądarkę na urządzeniu sterującym (zalecamy Chrome lub Edge) i wpisz `glkvm.local` w pasku adresu. Wpisz hasło administratora, aby się zalogować.

            ![Dostęp lokalny za pomocą nazwy domeny](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. Po zalogowaniu przejdź do **Toolbox** -> **Terminal** i kliknij **Access**, aby zalogować się do terminala.

            ![Dostęp do terminala](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Wykonaj polecenie ping dla `google.com`, aby sprawdzić stan sieci.

            ![Test ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Jeśli sieć działa prawidłowo, otrzymasz wynik podobny do poniższego.

            ![Test ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Jeśli połączenie sieciowe jest niestabilne lub niedostępne, skontaktuj się z dostawcą Internetu lub pomocą techniczną producenta routera.

??? "Device network error, binding failed."

    ![Błąd sieci podczas powiązania](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_network_error.png){class="glboxshadow"}

    1. Sprawdź stan diody LED. Upewnij się, że świeci ciągłym białym światłem, a urządzenie KVM ma połączenie z Internetem.
    2. Uruchom ponownie urządzenie KVM, poczekaj 2 minuty i spróbuj powiązać je ponownie.
    3. Upewnij się, że usługa chmurowa jest włączona.

        Usługa chmurowa jest domyślnie włączona, ale jeśli wcześniej wyłączono ją ręcznie, ponowne powiązanie urządzenia z aplikacją GLKVM nie powiedzie się. Uzyskaj lokalny dostęp do urządzenia KVM za pomocą nazwy domeny lub adresu IP, aby ponownie włączyć usługę chmurową.

    4. Wykonaj poniższe czynności, aby sprawdzić połączenie sieciowe poleceniem **Ping**.

        1. Podłącz urządzenie sterujące do tej samej sieci co KVM.

        2. Otwórz przeglądarkę na urządzeniu sterującym (zalecamy Chrome lub Edge) i wpisz `glkvm.local` w pasku adresu. Wpisz hasło administratora, aby się zalogować.

            ![Dostęp lokalny za pomocą nazwy domeny](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. Po zalogowaniu przejdź do **Toolbox** -> **Terminal** i kliknij **Access**, aby zalogować się do terminala.

            ![Dostęp do terminala](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Wykonaj polecenie ping dla `google.com`, aby sprawdzić stan sieci.

            ![Test ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            Jeśli sieć działa prawidłowo, otrzymasz wynik podobny do poniższego.

            ![Test ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            Jeśli połączenie sieciowe jest niestabilne lub niedostępne, skontaktuj się z dostawcą Internetu lub pomocą techniczną producenta routera.

??? "Binding failed, KVM is already bound by others."

    ![Urządzenie jest już powiązane z innym kontem](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_bound_by_others.png){class="glboxshadow"}

    Oznacza to, że urządzenie KVM zostało już powiązane z innym kontem.

    1. Sprawdź, czy urządzenie nie jest powiązane z Twoim innym adresem e-mail. Jeśli masz inne konta, sprawdź je.

    2. Jeśli dodajesz urządzenie za pomocą numeru S/N, upewnij się, że został on wpisany poprawnie.

??? "Incorrect Dynamic Binding Code. You have 4 attempts remaining."

    ![Nieprawidłowy kod powiązania](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_binding_code.png){class="glboxshadow"}

    Oznacza to, że wpisany kod powiązania jest nieprawidłowy lub wygasł.

    1. Zaloguj się lokalnie do konsoli administracyjnej KVM, przejdź do **Cloud Service** w prawym górnym rogu i kliknij **Bind with Code**, aby uzyskać dynamiczny kod powiązania.

    2. W modelu GL-RM10 (Comet Pro) kod można też uzyskać na ekranie dotykowym. Przesuń do ekranu **Cloud Service** i kliknij **Generate Binding Code**, aby wyświetlić dynamiczny kod powiązania. Wpisz ten kod w aplikacji GLKVM, aby ukończyć powiązanie.

        ![Generowanie kodu powiązania](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_code_screen.png){class="glboxshadow"}

    3. Jeśli kod powiązania wygaśnie, kliknij **Regenerate**, aby uzyskać nowy.

??? "Incorrect Device ID. You have 4 attempts remaining."

    ![Nieprawidłowy identyfikator urządzenia](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_device_id.png){class="glboxshadow"}

    Oznacza to, że wpisano nieprawidłowy identyfikator Device ID.

    1. Sprawdź prawidłowy Device ID na etykiecie spodniej.

    2. Jeśli nie możesz sprawdzić etykiety spodniej, spróbuj powiązać urządzenie przez dostęp lokalny.

        Zaloguj się lokalnie do konsoli administracyjnej KVM, przejdź do **Cloud Service** w prawym górnym rogu i kliknij **Bind To KVM Cloud**. Nastąpi przekierowanie do strony powiązania z unikatowym tokenem. Zaloguj się na konto w chmurze i potwierdź informacje o urządzeniu, aby ukończyć powiązanie.

??? "Inne"

    Sprawdź, czy na urządzeniu sterującym z zainstalowaną aplikacją GLKVM jest włączona usługa VPN.

    Wyłącz wszystkie programy VPN i proxy, w tym AstroWarp, Tailscale oraz ZeroTier, a następnie ponownie spróbuj powiązać KVM z aplikacją GLKVM.

Jeśli problem nadal występuje, skontaktuj się z nami pod adresem [support@gl-inet.com](mailto:support@gl-inet.com) i podaj model urządzenia, wersję oprogramowania sprzętowego oraz adres MAC.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
