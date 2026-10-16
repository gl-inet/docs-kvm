# Comet (GL-RM1) V1/V2 — szybka konfiguracja {#comet-gl-rm1-v1v2-quick-setup}

Obejrzyj ten film lub wykonaj poniższe kroki, aby skonfigurować Comet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/JDgflRaIHw0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Podłączanie urządzeń {#connect-devices}

Dla jasności urządzenie A oznacza urządzenie sterujące, a urządzenie B — urządzenie sterowane.

![Podłączanie urządzeń](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/01_device_distinction.jpg){class="glboxshadow"}

1. Podłącz Comet do źródła zasilania.

    ![Podłączanie zasilania](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/02_power-on.jpg){class="glboxshadow"}

2. Połącz port HD IN urządzenia Comet z portem HD OUT urządzenia B za pomocą kabla HDMI.

    ![Podłączanie kabla HD](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/03_hdmi.jpg){class="glboxshadow"}

3. Połącz port USB-Device urządzenia Comet z portem USB urządzenia B za pomocą kabla USB.

    ![Podłączanie portu USB](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/04_usb-cable.jpg){class="glboxshadow"}

4. Podłącz port Ethernet urządzenia Comet do sieci.

    ![Podłączanie do sieci](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/05_ethernet.jpg){class="glboxshadow"}

5. Podłączanie urządzeń zostało zakończone. Teraz możesz otworzyć konsolę Comet lokalnie lub zdalnie.

## Dostęp lokalny {#local-access}

Dostęp do Comet w sieci lokalnej można uzyskać na dwa sposoby: przez nazwę domenową lub adres IP.

Przed połączeniem upewnij się, że urządzenie sterujące znajduje się w tej samej sieci LAN co Comet.

### Nazwa domenowa {#domain}

1. Uruchom przeglądarkę na urządzeniu sterującym. Dla lepszej zgodności zalecamy Chrome lub Edge.

2. Wpisz `glkvm.local` w pasku adresu. Nastąpi przekierowanie do strony logowania GLKVM. Wpisz hasło administratora.

    ![Dostęp lokalny przez nazwę domenową](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Uwaga**: Przy pierwszym połączeniu należy ustawić hasło administratora.

3. Teraz możesz lokalnie otworzyć konsolę Comet i uzyskać dostęp do sterowanego urządzenia.

    ![Dostęp lokalny przez nazwę domenową](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### Adres IP {#ip-address}

1. Znajdź adres IP urządzenia Comet w ustawieniach nadrzędnego routera.

    W tym przykładzie Comet jest połączony kablem Ethernet z portem LAN routera GL.iNet GL-AXT1800.

    Zaloguj się do internetowego panelu administracyjnego GL-AXT1800 i znajdź adres IP urządzenia Comet na liście Client, jak pokazano poniżej.

    ![Dostęp lokalny przez adres IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

2. Otwórz nową kartę w przeglądarce i wpisz adres IP urządzenia Comet w pasku adresu. Nastąpi przekierowanie do strony logowania GLKVM. Wpisz hasło administratora.

    ![Dostęp lokalny przez adres IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Uwaga**: Przy pierwszym połączeniu należy ustawić hasło administratora.

3. Teraz możesz lokalnie otworzyć konsolę Comet i uzyskać dostęp do sterowanego urządzenia.

    ![Dostęp lokalny przez adres IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Dostęp zdalny {#remote-access}

Dostęp zdalny do Comet można uzyskać na kilka sposobów: przez usługę chmurową, aplikację GLKVM, Tailscale, ZeroTier i NetBird.

### Usługa chmurowa {#cloud-service}

1. Powiąż urządzenie z chmurą KVM. Tę czynność należy wykonać w sieci lokalnej.

    Urządzenie KVM można powiązać z chmurą na dwa sposoby: Regular Binding lub Dynamic Code Binding. Tutaj przedstawiamy Regular Binding. Jeśli wolisz Dynamic Code Binding, szczegóły znajdziesz [tutaj](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}.

    Najpierw połącz się lokalnie z Comet i przejdź do **Cloud Service** w prawym górnym rogu. Kliknij **Bind To Cloud**.

    ![Powiązanie z chmurą](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    Nastąpi przekierowanie do strony logowania. Zaloguj się za pomocą konta chmurowego glinet.

    ![Logowanie w celu powiązania urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Następnie potwierdź informacje o urządzeniu i kliknij **Bind**.

    ![Potwierdzanie powiązania urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Poczekaj chwilę, aż urządzenie zostanie powiązane z kontem. Kliknij **Done**.

    ![Pomyślne powiązanie urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Uzyskaj dostęp zdalny przez usługę chmurową.

    Otwórz przeglądarkę (np. Google Chrome) i wpisz `glkvm.com` w pasku adresu. Zobaczysz stronę logowania. Zaloguj się na konto glinet.

    ![Logowanie do dostępu zdalnego](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Po zalogowaniu zobaczysz urządzenia powiązane z kontem. Kliknij urządzenie, do którego chcesz uzyskać dostęp zdalny.

    ![Wybór urządzenia do dostępu zdalnego](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    Na nowo otwartej stronie wpisz hasło administratora, aby się zalogować.

    ![Logowanie administratora do dostępu zdalnego](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Teraz możesz uzyskać dostęp zdalny do KVM i sterowanego urządzenia przez chmurę, bez instalowania aplikacji.

    ![Nawiązano dostęp zdalny](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

### Aplikacja GLKVM {#glkvm-app}

1. Zainstaluj [aplikację GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} na urządzeniu sterującym.

2. Zaloguj się na konto GL.iNet.

    ![Logowanie](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    Jeśli nie masz konta, najpierw je utwórz, a następnie się zaloguj.

    ![Rejestracja](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

3. Powiąż urządzenie.

    Po zalogowaniu strona będzie wyglądać następująco. Kliknij **Add Device**.

    ![Dodawanie urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

    Urządzenie możesz powiązać na trzy sposoby: Auto Discover, S/N Code i Dynamic Binding Code.

    ??? "Auto Discover"

        Tę czynność należy wykonać w sieci lokalnej. Upewnij się, że urządzenie sterujące znajduje się w tej samej sieci LAN co Comet.

        Kliknij **Auto Discover**. Wyszukiwanie rozpocznie się automatycznie.

        ![Automatyczne wykrywanie — krok 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

        Znajdź urządzenie KVM i wpisz jego Device ID, aby powiązać je z kontem.

        ![Automatyczne wykrywanie — krok 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

    ??? "S/N Code"

        Ta metoda przydaje się, gdy KVM nie został wykryty lub nie znajduje się w tej samej sieci LAN, ale znasz jego numer seryjny (S/N).

        Kliknij **S/N Code**. W wyświetlonym oknie nadaj urządzeniu nazwę i wpisz numer S/N znajdujący się na etykiecie na spodzie urządzenia KVM.

        ![Kod numeru seryjnego](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Tę czynność należy wykonać w sieci lokalnej. Upewnij się, że urządzenie sterujące znajduje się w tej samej sieci LAN co Comet.

        1. Zaloguj się lokalnie do KVM za pomocą nazwy domenowej lub adresu IP. Szczegóły znajdziesz [tutaj](../../faq/local_access_via_browser.md).

        2. Przejdź do **Cloud Service** w prawym górnym rogu i kliknij **Bind With Code**.

            ![Powiązanie za pomocą kodu — krok 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

        3. Zostanie wygenerowany losowy 8-cyfrowy kod powiązania urządzenia, ważny przez 60 sekund. Kliknij kod, aby go skopiować.

            ![Powiązanie za pomocą kodu — krok 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

        4. Wróć do aplikacji GLKVM, wpisz dynamiczny kod powiązania i kliknij **Bind**.

            ![Kod dynamiczny](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

4. Uzyskaj dostęp zdalny przez aplikację GLKVM.

    Po powiązaniu urządzenia KVM z kontem aplikacja wyświetli stan "Online".

    ![Urządzenie dostępne w sieci](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

    Kliknij urządzenie KVM. Otworzy się nowe okno i rozpocznie się łączenie.

    ![Nawiązywanie połączenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

    Po nawiązaniu połączenia wpisz hasło administratora, aby zalogować się do urządzenia.

    ![Logowanie po nawiązaniu połączenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

    Uzyskasz dostęp do KVM, a za jego pośrednictwem do sterowanego urządzenia.

    ![Dostęp po nawiązaniu połączenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

### Tailscale {#tailscale}

Comet integruje się z Tailscale, umożliwiając zdalny dostęp przez wirtualną sieć Tailscale.

W konsoli Comet przejdź do **Apps Center** -> **Tailscale**, włącz usługę i powiąż Comet z kontem Tailscale.

Następnie powiąż urządzenie sterujące z tym samym kontem. Wpisz **wirtualny adres IP Tailscale** urządzenia Comet w przeglądarce na urządzeniu sterującym, aby uzyskać zdalny dostęp bez instalowania aplikacji GLKVM.

Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier {#zerotier}

Comet integruje się z ZeroTier, umożliwiając zdalny dostęp przez wirtualną sieć ZeroTier.

W konsoli Comet przejdź do **Apps Center** -> **ZeroTier** i włącz usługę.

Następnie dołącz Comet i urządzenie sterujące do tej samej sieci ZeroTier, używając 16-znakowego alfanumerycznego Network ID. Wpisz **adres IP ZeroTier** urządzenia Comet w przeglądarce na urządzeniu sterującym, aby uzyskać zdalny dostęp bez instalowania aplikacji GLKVM.

Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_zerotier.md){target="_blank"}.

### NetBird {#netbird}

Comet integruje się z NetBird, umożliwiając zdalny dostęp przez wirtualną sieć NetBird.

W konsoli Comet przejdź do **Apps Center** -> **NetBird**, włącz usługę i powiąż Comet z kontem NetBird.

Następnie powiąż urządzenie sterujące z tym samym kontem. Wpisz **wirtualny adres IP NetBird** urządzenia Comet w przeglądarce na urządzeniu sterującym, aby uzyskać zdalny dostęp bez instalowania aplikacji GLKVM.

Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_netbird.md){target="_blank"}.
