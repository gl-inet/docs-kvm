# Comet Pro (GL-RM10) — szybka konfiguracja {#comet-pro-gl-rm10-quick-setup}

Obejrzyj ten film lub wykonaj poniższe kroki, aby skonfigurować Comet Pro.

<iframe width="560" height="315" src="https://www.youtube.com/embed/onxj5EEf9Ys" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Podłączanie urządzeń {#connect-devices}

Dla jasności urządzenie A oznacza urządzenie sterujące, a urządzenie B — urządzenie sterowane.

![Podłączanie urządzeń](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/connect-devices.png){class="glboxshadow"}

1. Podłącz Comet Pro do źródła zasilania.

    ![Podłączanie zasilania](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/01-power-on.png){class="glboxshadow"}

2. Połącz port HD IN urządzenia Comet Pro z portem HD OUT urządzenia B za pomocą kabla HDMI. W razie potrzeby użyj drugiego kabla HD, aby połączyć port HD OUT urządzenia Comet Pro z monitorem zewnętrznym.

    ![Podłączanie kabla HD](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/02-hd-cable.png){class="glboxshadow"}

3. Połącz port USB Type-C urządzenia Comet Pro z portem USB urządzenia B za pomocą kabla USB.

    ![Podłączanie kabla USB](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/03-usb-cable.png){class="glboxshadow"}

4. Podłącz Comet Pro do sieci za pomocą kabla Ethernet lub Wi-Fi.

    - Ethernet: podłącz port Ethernet urządzenia Comet Pro do sieci.

        ![Łączenie przez Ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/04-ethernet.png){class="glboxshadow"}

    - Wi-Fi: przesuń palcem w lewo na ekranie dotykowym i połącz Comet Pro z istniejącą siecią Wi-Fi (obsługiwane pasma: 2.4G/5G).

        ![Łączenie przez Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/quick_setup/04-wifi.png){class="glboxshadow"}

5. Podłączanie urządzeń zostało zakończone. Teraz możesz otworzyć konsolę Comet Pro lokalnie lub zdalnie.

## Dostęp lokalny {#local-access}

Dostęp do Comet Pro w sieci lokalnej można uzyskać na dwa sposoby: przez nazwę domenową lub adres IP.

Przed połączeniem upewnij się, że urządzenie sterujące znajduje się w tej samej sieci LAN co Comet Pro.

### Nazwa domenowa {#domain}

1. Uruchom przeglądarkę na urządzeniu sterującym. Dla lepszej zgodności zalecamy Chrome lub Edge.

2. Wpisz `glkvm.local` w pasku adresu. Nastąpi przekierowanie do strony logowania GLKVM. Wpisz hasło administratora.

    ![Dostęp lokalny przez nazwę domenową](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Uwaga**: Przy pierwszym połączeniu należy ustawić hasło administratora.

3. Teraz możesz lokalnie otworzyć konsolę Comet Pro i uzyskać dostęp do sterowanego urządzenia.

    ![Dostęp lokalny przez nazwę domenową](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### Adres IP {#ip-address}

1. Sprawdź adres IP urządzenia Comet Pro na ekranie dotykowym. W tym przykładzie adres IP urządzenia Comet Pro to `192.168.8.197`.

2. Uruchom przeglądarkę i wpisz ten adres IP w pasku adresu. Nastąpi przekierowanie do strony logowania GLKVM. Wpisz hasło administratora.

    ![Dostęp lokalny przez adres IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Uwaga**: Przy pierwszym połączeniu należy ustawić hasło administratora.

3. Teraz możesz lokalnie otworzyć konsolę Comet Pro i uzyskać dostęp do sterowanego urządzenia.

    ![Dostęp lokalny przez adres IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Dostęp zdalny {#remote-access}

Dostęp zdalny do Comet Pro można uzyskać na kilka sposobów: przez usługę chmurową, aplikację GLKVM, Tailscale, ZeroTier i NetBird.

### Usługa chmurowa {#cloud-service}

1. Powiąż urządzenie z chmurą KVM. Tę czynność należy wykonać w sieci lokalnej.

    Urządzenie KVM można powiązać z chmurą na dwa sposoby: Regular Binding lub Dynamic Code Binding. Tutaj przedstawiamy Regular Binding. Jeśli wolisz Dynamic Code Binding, szczegóły znajdziesz [tutaj](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}.

    Najpierw połącz się lokalnie z Comet Pro i przejdź do **Cloud Service** w prawym górnym rogu. Kliknij **Bind To Cloud**.

    ![Powiązanie z chmurą](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    Nastąpi przekierowanie do strony logowania. Zaloguj się za pomocą konta chmurowego glinet.

    ![Logowanie w celu powiązania urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Następnie potwierdź informacje o urządzeniu i kliknij **Bind**.

    ![Potwierdzanie powiązania urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Poczekaj chwilę, aż Comet Pro zostanie powiązany z kontem. Kliknij **Done**.

    ![Pomyślne powiązanie urządzenia](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Uzyskaj dostęp zdalny przez usługę chmurową.

    Otwórz przeglądarkę (np. Google Chrome) i wpisz `glkvm.com` w pasku adresu. Zobaczysz stronę logowania. Zaloguj się na konto glinet.

    ![Logowanie do dostępu zdalnego](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    Po zalogowaniu zobaczysz urządzenia powiązane z kontem. Kliknij urządzenie, do którego chcesz uzyskać dostęp zdalny.

    ![Wybór urządzenia do dostępu zdalnego](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    Na nowo otwartej stronie wpisz hasło administratora, aby się zalogować.

    ![Logowanie administratora do dostępu zdalnego](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Teraz możesz uzyskać zdalny dostęp do Comet Pro i sterowanego urządzenia przez chmurę, bez instalowania aplikacji.

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

        Tę czynność należy wykonać w sieci lokalnej. Upewnij się, że urządzenie sterujące znajduje się w tej samej sieci LAN co Comet Pro.

        Kliknij **Auto Discover**. Wyszukiwanie rozpocznie się automatycznie.

        ![Automatyczne wykrywanie — krok 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

        Znajdź urządzenie KVM i wpisz jego Device ID, aby powiązać je z kontem.

        ![Automatyczne wykrywanie — krok 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

    ??? "S/N Code"

        Ta metoda przydaje się, gdy KVM nie został wykryty lub nie znajduje się w tej samej sieci LAN, ale znasz jego numer seryjny (S/N).

        Kliknij **S/N Code**. W wyświetlonym oknie nadaj urządzeniu nazwę i wpisz numer S/N znajdujący się na etykiecie na spodzie urządzenia KVM.

        ![Kod numeru seryjnego](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Tę czynność należy wykonać w sieci lokalnej. Upewnij się, że urządzenie sterujące znajduje się w tej samej sieci LAN co Comet Pro.

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

Comet Pro integruje się z Tailscale, umożliwiając zdalny dostęp przez wirtualną sieć Tailscale.

W konsoli przejdź do **Apps Center** -> **Tailscale**, włącz usługę i powiąż Comet Pro z kontem Tailscale.

Następnie powiąż urządzenie sterujące z tym samym kontem. Wpisz **wirtualny adres IP Tailscale** urządzenia Comet Pro w przeglądarce na urządzeniu sterującym, aby uzyskać zdalny dostęp bez instalowania aplikacji GLKVM.

Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier {#zerotier}

Comet Pro integruje się z ZeroTier, umożliwiając zdalny dostęp przez wirtualną sieć ZeroTier.

W konsoli przejdź do **Apps Center** -> **ZeroTier** i włącz usługę.

Następnie dołącz Comet Pro i urządzenie sterujące do tej samej sieci ZeroTier, używając 16-znakowego alfanumerycznego Network ID. Wpisz **adres IP ZeroTier** urządzenia Comet Pro w przeglądarce na urządzeniu sterującym, aby uzyskać zdalny dostęp bez instalowania aplikacji GLKVM.

Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_zerotier.md){target="_blank"}.

### NetBird {#netbird}

Comet Pro integruje się z NetBird, umożliwiając zdalny dostęp przez wirtualną sieć NetBird.

W konsoli przejdź do **Apps Center** -> **NetBird**, włącz usługę i powiąż Comet Pro z kontem NetBird.

Następnie powiąż urządzenie sterujące z tym samym kontem. Wpisz **wirtualny adres IP NetBird** urządzenia Comet Pro w przeglądarce na urządzeniu sterującym, aby uzyskać zdalny dostęp bez instalowania aplikacji GLKVM.

Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_netbird.md){target="_blank"}.
