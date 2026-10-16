# Jak uzyskać zdalny dostęp do KVM przez aplikację GLKVM {#how-to-access-kvm-remotely-via-glkvm-app}

Przed rozpoczęciem upewnij się, że urządzenie docelowe jest prawidłowo podłączone do GL.iNet KVM, a KVM ma stabilne połączenie sieciowe.

Wykonaj poniższe czynności, aby uzyskać zdalny dostęp do KVM i urządzenia docelowego przez aplikację GLKVM.

## Instalacja i logowanie {#install-and-log-in}

1. Zainstaluj [aplikację GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} na urządzeniu sterującym.

2. Otwórz aplikację GLKVM i zaloguj się na konto GL.iNet.

    ![Logowanie](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Jeśli nie masz konta GL.iNet, utwórz je, a następnie się zaloguj.

    ![Tworzenie konta](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

## Powiązanie KVM {#bind-your-kvm}

Po zalogowaniu strona będzie wyglądać jak poniżej. Kliknij **Add Device**.

KVM można powiązać na trzy sposoby: Auto Discover, S/N Code i Dynamic Binding Code.

![Dodawanie urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

### Auto Discover {#auto-discover}

Tę czynność należy wykonać w sieci lokalnej. Upewnij się, że KVM i urządzenie sterujące znajdują się w tej samej sieci LAN.

1. Kliknij **Auto Discover**. Rozpocznie się automatyczne wyszukiwanie dostępnych urządzeń KVM.

    ![Automatyczne wykrywanie — krok 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

2. Znajdź swój KVM i wpisz jego **Device ID**, aby powiązać go z kontem.

    ![Automatyczne wykrywanie — krok 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

### S/N Code {#sn-code}

Ta metoda jest przydatna, gdy KVM nie został wykryty lub nie znajduje się w tej samej sieci LAN, ale znasz jego numer seryjny (S/N).

1. Kliknij **S/N Code**.

2. W wyświetlonym oknie nadaj urządzeniu nazwę i wpisz jego numer S/N z etykiety na spodzie KVM.

    ![Numer seryjny S/N](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

### Dynamic Binding Code {#dynamic-binding-code}

Przed użyciem tej funkcji zaktualizuj oprogramowanie sprzętowe KVM do wersji v1.7.

Tę czynność należy wykonać w sieci lokalnej. Upewnij się, że KVM i urządzenie sterujące znajdują się w tej samej sieci LAN.

1. Zaloguj się lokalnie do KVM za pomocą nazwy domeny lub adresu IP. Szczegóły znajdziesz [tutaj](../faq/local_access_via_browser.md).

2. Po zalogowaniu przejdź do **Cloud Service** w prawym górnym rogu i kliknij **Bind With Code**.

    ![Powiązanie kodem — krok 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. Zostanie wygenerowany losowy 8-cyfrowy kod do powiązania urządzenia, ważny przez 60 sekund. Kliknij kod, aby go skopiować.

    ![Powiązanie kodem — krok 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Wróć do aplikacji GLKVM, wpisz dynamiczny kod powiązania i kliknij **Bind**.

    ![Kod dynamiczny](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

## Dostęp zdalny {#remote-access}

Po powiązaniu urządzenia KVM z kontem pojawi się przy nim w aplikacji status „Online”.

![Urządzenie online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

Kliknij urządzenie KVM. Otworzy się nowe okno i rozpocznie się nawiązywanie połączenia.

![Nawiązywanie połączenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

Po nawiązaniu połączenia wpisz hasło administratora, aby się zalogować.

![Logowanie po nawiązaniu połączenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

Możesz teraz uzyskać dostęp do urządzenia KVM, a za jego pośrednictwem do urządzenia docelowego.

![Dostęp do podłączonego urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
