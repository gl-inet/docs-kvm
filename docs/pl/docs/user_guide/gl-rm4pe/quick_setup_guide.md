# Comet X (GL-RM4PE) — szybka konfiguracja {#comet-x-gl-rm4pe-quick-setup}

## Podłączanie urządzeń {#connect-devices}

Dla jasności urządzenie A oznacza urządzenie sterujące, a urządzenie B — urządzenie sterowane.

![Podłączanie — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect1.png){class="glboxshadow"}

1. Połącz Comet X z przełącznikiem PoE za pomocą kabla Ethernet lub zasil urządzenie zasilaczem 5V/3A.

    ![Podłączanie — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect2.png){class="glboxshadow"}

    ***Uwaga**: Jeśli używasz zasilacza, połącz Comet X kablem Ethernet z urządzeniem sieciowym (np. routerem), aby zapewnić dostęp do Internetu.*

2. Połącz port **HDMI IN** urządzenia Comet X z urządzeniem B za pomocą kabla HDMI, aby umożliwić przesyłanie obrazu.

    ![Podłączanie — krok 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect3.png){class="glboxshadow"}

3. Połącz port **USB-C** urządzenia Comet X z urządzeniem B za pomocą kabla USB. Ten port USB-C musi odpowiadać używanemu portowi HDMI IN, aby sygnały klawiatury i myszy były prawidłowo przesyłane.

    ![Podłączanie — krok 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect4.png){class="glboxshadow"}

4. (Opcjonalnie) Połącz port **HDMI OUT** urządzenia Comet X z monitorem zewnętrznym, aby powielić obraz (przelotowe wyjście wideo). Szczegóły znajdziesz w sekcji [Sterowanie lokalne](#local-control).

5. Połączenia są gotowe. Teraz możesz otworzyć konsolę Comet X lokalnie lub zdalnie.

## Montaż w szafie rack {#rack-mounting}

W razie potrzeby zamontuj Comet X na szynach szafy serwerowej.

1. Przykręć uchwyty montażowe do Comet X dołączonymi śrubami.

    ![Instalacja — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install1.png){class="glboxshadow"}

2. Przymocuj Comet X do szyn za pomocą śrub do szaf rack. **Śruby do szaf rack nie są dołączone do zestawu**.

    ![Instalacja — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install2.png){class="glboxshadow"}

## Sterowanie lokalne {#local-control}

Steruj urządzeniem bezpośrednio przez fizyczne przewody — bez sieci, adresu IP ani nazwy domenowej.

Comet X ma port HDMI OUT i dwa dodatkowe porty USB, które ułatwiają lokalną diagnostykę, konfigurację i instalację systemu operacyjnego. Podłącz monitor, mysz i klawiaturę, aby bezpośrednio sterować sprzętem bez dodatkowej konfiguracji.

1. Połącz port **HDMI OUT** na tylnym panelu Comet X z monitorem zewnętrznym, aby powielić obraz (przelotowe wyjście wideo).

    ![Sterowanie lokalne — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control1.png){class="glboxshadow"}

2. Podłącz klawiaturę i mysz do portów USB na przednim panelu Comet X.

    ![Sterowanie lokalne — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control2.png){class="glboxshadow"}

3. Teraz możesz sterować podłączonymi urządzeniami za pomocą lokalnej klawiatury i myszy, a obraz będzie przekazywany na lokalny monitor.

## Dostęp przez sieć LAN {#lan-access}

Dostęp do Comet X w sieci lokalnej można uzyskać na dwa sposoby: przez nazwę domenową lub adres IP.

Przed połączeniem upewnij się, że urządzenie sterujące znajduje się w tej samej sieci LAN co Comet X.

### Nazwa domenowa {#domain}

1. Uruchom przeglądarkę na urządzeniu sterującym. Dla lepszej zgodności zalecamy Chrome lub Edge.

2. Wpisz `glkvm.local` w pasku adresu. Nastąpi przekierowanie do strony logowania GLKVM. Wpisz hasło administratora.

    ![Dostęp lokalny przez nazwę domenową](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain1.png){class="glboxshadow"}

    ***Uwaga**: Przy pierwszym połączeniu należy ustawić hasło administratora.*

3. Teraz możesz lokalnie otworzyć konsolę Comet X i uzyskać dostęp do sterowanego urządzenia.

    ![Dostęp lokalny przez nazwę domenową](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain2.png){class="glboxshadow"}

### Adres IP {#ip-address}

1. Sprawdź adres IP urządzenia Comet X na ekranie dotykowym. W tym przykładzie adres IP urządzenia Comet X to `192.168.8.197`.

2. Uruchom przeglądarkę i wpisz ten adres IP w pasku adresu. Nastąpi przekierowanie do strony logowania GLKVM. Wpisz hasło administratora.

    ![Dostęp lokalny przez adres IP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip1.png){class="glboxshadow"}

    ***Uwaga**: Przy pierwszym połączeniu należy ustawić hasło administratora.*

3. Teraz możesz lokalnie otworzyć konsolę Comet X i uzyskać dostęp do sterowanego urządzenia.

    ![Dostęp lokalny przez adres IP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip2.png){class="glboxshadow"}

## Dostęp zdalny {#remote-access}

Dostęp zdalny do Comet X można uzyskać na kilka sposobów: przez usługę chmurową, aplikację GLKVM, Tailscale i ZeroTier.

### Usługa chmurowa {#cloud-service}

1. Powiąż urządzenie z chmurą KVM. Tę czynność należy wykonać w sieci lokalnej.

    Urządzenie KVM można powiązać z chmurą na dwa sposoby: Regular Binding lub Dynamic Code Binding. Tutaj przedstawiamy Regular Binding. Jeśli wolisz Dynamic Code Binding, szczegóły znajdziesz [tutaj](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"}.

    Najpierw połącz się lokalnie z Comet X i przejdź do **Cloud Service** w prawym górnym rogu. Kliknij **Bind To KVMCloud**.

    ![Powiązanie z chmurą](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_to_cloud.png){class="glboxshadow"}

    Nastąpi przekierowanie do strony logowania. Zaloguj się za pomocą konta chmurowego glinet.

    ![Powiązanie urządzenia z chmurą — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind1.png){class="glboxshadow"}

    Następnie potwierdź informacje o urządzeniu i kliknij **Bind**.

    ![Powiązanie urządzenia z chmurą — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind2.png){class="glboxshadow"}

    Poczekaj chwilę, aż Comet X zostanie powiązany z kontem. Kliknij **Done**.

    ![Pomyślne powiązanie urządzenia z chmurą](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind_success.png){class="glboxshadow"}

2. Uzyskaj dostęp zdalny przez usługę chmurową.

    Po kliknięciu Done nastąpi przekierowanie do witryny `glkvm.com`, w której zobaczysz swoje urządzenie.

    ![Lista urządzeń w chmurze](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_devices.png){class="glboxshadow"}

    ***Wskazówka**: Jeśli przekierowanie nie nastąpi, wpisz ręcznie `glkvm.com` w pasku adresu i zaloguj się na konto glinet. Po zalogowaniu zobaczysz urządzenie powiązane z kontem.*

    Kliknij urządzenie, do którego chcesz uzyskać dostęp zdalny.

    ![Dostęp przez chmurę](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access.png){class="glboxshadow"}

    Otworzy się nowa strona. Wpisz hasło administratora, aby się zalogować.

    ![Dostęp przez chmurę — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access1.png){class="glboxshadow"}

    Teraz możesz uzyskać zdalny dostęp do Comet X i sterowanego urządzenia przez chmurę.

    ![Dostęp przez chmurę — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access2.png){class="glboxshadow"}

### Aplikacja GLKVM {#glkvm-app}

1. Zainstaluj [aplikację GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} na urządzeniu sterującym.

2. Zaloguj się na konto GL.iNet.

    ![Logowanie](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_login.jpg){class="glboxshadow"}

    Jeśli nie masz konta, najpierw je utwórz, a następnie się zaloguj.

    ![Rejestracja](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_signup.png){class="glboxshadow"}

3. Powiąż urządzenie.

    Po zalogowaniu strona będzie wyglądać następująco. Kliknij **Add Device**.

    ![Dodawanie urządzenia](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_add_device.png){class="glboxshadow"}

    Urządzenie możesz powiązać na trzy sposoby: Auto Discover, S/N Code i Dynamic Binding Code.

    ??? "Auto Discover"

        Tę czynność należy wykonać w sieci lokalnej. Upewnij się, że urządzenie sterujące znajduje się w tej samej sieci LAN co Comet X, i przygotuj identyfikator Device ID urządzenia KVM.

        Kliknij **Auto Discover**. Rozpocznie się wyszukiwanie.

        ![Automatyczne wykrywanie — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover1.png){class="glboxshadow"}

        Znajdź urządzenie KVM i wpisz jego **Device ID**, aby powiązać je z kontem.

        ![Automatyczne wykrywanie — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover2.png){class="glboxshadow"}

        ![Automatyczne wykrywanie — krok 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover3.png){class="glboxshadow"}

    ??? "S/N Code"

        Ta metoda przydaje się, gdy KVM nie został wykryty lub nie znajduje się w tej samej sieci LAN, ale znasz jego numer seryjny (S/N).

        Kliknij **S/N Code**. W wyświetlonym oknie nadaj urządzeniu nazwę i wpisz numer S/N znajdujący się na spodzie urządzenia KVM.

        ![Kod numeru seryjnego](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/add_sncode.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        Tę czynność należy wykonać w sieci lokalnej. Upewnij się, że urządzenie sterujące znajduje się w tej samej sieci LAN co Comet X.

        1. Zaloguj się lokalnie do KVM za pomocą nazwy domenowej lub adresu IP. Szczegóły znajdziesz [tutaj](#lan-access).

        2. Przejdź do **Cloud Service** w prawym górnym rogu i kliknij **Bind With Code**.

            ![Powiązanie za pomocą kodu — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code1.png){class="glboxshadow"}

        3. Zostanie wygenerowany losowy 8-cyfrowy kod powiązania urządzenia, ważny przez 60 sekund. Kliknij kod, aby go skopiować.

            ![Powiązanie za pomocą kodu — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code2.png){class="glboxshadow"}

        4. Wróć do aplikacji GLKVM, wpisz dynamiczny kod powiązania i kliknij **Bind**.

            ![Kod dynamiczny](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code3.png){class="glboxshadow"}

4. Uzyskaj dostęp zdalny przez aplikację GLKVM.

    Po powiązaniu urządzenia KVM z kontem aplikacja wyświetli stan "Online".

    ![Urządzenie dostępne w aplikacji](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_devices.png){class="glboxshadow"}

    Kliknij urządzenie KVM. Otworzy się nowe okno i rozpocznie się łączenie.

    ![Nawiązywanie połączenia w aplikacji](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_connecting.png){class="glboxshadow"}

    Po nawiązaniu połączenia wpisz hasło administratora, aby zalogować się do urządzenia.

    ![Dostęp przez aplikację — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access1.png){class="glboxshadow"}

    Uzyskasz dostęp do KVM, a za jego pośrednictwem do sterowanego urządzenia.

    ![Dostęp przez aplikację — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access2.png){class="glboxshadow"}

### Tailscale {#tailscale}

Comet X integruje się z Tailscale, umożliwiając zdalny dostęp przez wirtualną sieć Tailscale.

W konsoli przejdź do **Apps Center** -> **Tailscale**, włącz usługę i powiąż Comet X z kontem Tailscale.

Następnie powiąż urządzenie sterujące z tym samym kontem. Wpisz **wirtualny adres IP Tailscale** urządzenia Comet X w przeglądarce na urządzeniu sterującym, aby uzyskać zdalny dostęp bez instalowania aplikacji GLKVM.

Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_tailscale.md){target="_blank"}.

### ZeroTier {#zerotier}

Comet X integruje się z ZeroTier, umożliwiając zdalny dostęp przez wirtualną sieć ZeroTier.

W konsoli przejdź do **Apps Center** -> **ZeroTier** i włącz usługę.

Następnie dołącz Comet X i urządzenie sterujące do tej samej sieci ZeroTier, używając 16-znakowego alfanumerycznego Network ID. Wpisz **adres IP ZeroTier** urządzenia Comet X w przeglądarce na urządzeniu sterującym, aby uzyskać zdalny dostęp bez instalowania aplikacji GLKVM.

Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_zerotier.md){target="_blank"}.
