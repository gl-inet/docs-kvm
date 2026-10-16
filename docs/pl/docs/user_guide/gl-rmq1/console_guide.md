# Comet Q (GL-RMQ1) — przewodnik po konsoli {#comet-q-gl-rmq1-console-guide}

## Ustawienia {#settings}

W konsoli przejdź do **Settings**. Strona ustawień obejmuje cztery sekcje:

- [Wideo](#video)
- [Dźwięk, klawiatura i mysz](#audiokeyboardmouse)
- [System](#system)
- [Sieć](#network)

### Szybkie wyszukiwanie {#quick-search}

Aby szybko znaleźć odpowiednie ustawienia, wpisz słowa kluczowe u góry strony Settings.

![Szybkie wyszukiwanie](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/quick-search.png){class="glboxshadow"}

### Wideo {#video}

W konsoli możesz dostosować ustawienia wideo, takie jak EDID, jakość i przesyłanie obrazu oraz orientacja ekranu.

![Ustawienia wideo](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-video.png){class="glboxshadow"}

- **Type**: wybierz typ sterowanego urządzenia.

    System automatycznie stosuje zalecany tryb myszy i ustawienia EDID, aby zapewnić optymalne proporcje obrazu i dokładność sterowania. Zmień tę opcję, jeśli urządzenie nie zostało prawidłowo rozpoznane lub chcesz użyć niestandardowego typu.

- **EDID**: skrót od Extended Display Identification Data; umożliwia automatyczne dopasowanie optymalnych parametrów wyświetlania.

    Ustawienie domyślne sprawdza się w większości sytuacji i zwykle nie wymaga zmiany. Szczegóły znajdziesz [tutaj](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. Jeśli po zmianie EDID obraz się nie odświeża, uruchom ponownie sterowane urządzenie.

- **Mode**: w razie potrzeby przełączaj między trybami Smart i Normal. Tryb Smart pomaga zmniejszyć wykorzystanie pasma, zwłaszcza przy słabym połączeniu sieciowym.

- **Quality**: dostosuj jakość obrazu do warunków sieciowych i wymaganej rozdzielczości, wybierając Low/Medium/High/Ultra-high/Lossless.

- **Transfer**: wybierz sposób przesyłania obrazu: WebRTC, WebRTC (FEC) lub Direct. Pamiętaj, że tryb Direct nie przesyła dźwięku.

    !!! note "Czym różnią się WebRTC, WebRTC (FEC) i Direct?"

        - **WebRTC**: zapewnia równowagę między płynnym obrazem a stabilnym dźwiękiem podczas zdalnego sterowania w czasie rzeczywistym.

        - **WebRTC (FEC)**: dodaje korekcję błędów, aby poprawić stabilność połączenia przy słabej lub niestabilnej sieci. Po wybraniu tej opcji utracone pakiety danych są automatycznie odtwarzane przez przesyłanie niewielkiej ilości danych nadmiarowych, co ogranicza migotanie obrazu i opóźnienia.

        - **Direct**: zapewnia najniższe opóźnienia i bezstratną jakość obrazu, ale nie obsługuje przesyłania dźwięku.

- **Orientation**: ustaw kąt obrotu obrazu konsoli na 0°/90°/180°/270°.

- **View**: określa sposób skalowania obrazu przy zmianie rozmiaru okna przeglądarki. Dostępne opcje: Adaptive, Best Picture Quality, Original Pixel.

### Dźwięk, klawiatura i mysz {#audiokeyboardmouse}

Możesz dostosować ustawienia dźwięku, klawiatury i myszy.

![Dźwięk, klawiatura i mysz](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/audio-keyboard-mouse.png){class="glboxshadow"}

- **Speaker**: steruje dźwiękiem wychodzącym z sterowanego urządzenia (np. dźwiękami systemowymi lub dźwiękiem filmów).

- **Microphone**: przesyła lokalny dźwięk (np. Twój głos) z urządzenia sterującego do urządzenia zdalnego. Obsługuje wyciszanie jednym kliknięciem i skrót aktywujący mikrofon podczas przytrzymywania (Press To Speak).

    ![Ustawienia mikrofonu](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/mic-settings.png){class="glboxshadow"}

    ![Mówienie podczas przytrzymywania klawisza](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/press-to-speak.png){class="glboxshadow"}

- **Keyboard**: włącz lub wyłącz klawiaturę sterowanego urządzenia.

- **Bad Link Mode**: natychmiast zwalnia klawisze. Każde naciśnięcie jest przesyłane jako pojedyncze szybkie naciśnięcie i zwolnienie, co zapobiega zablokowaniu klawiszy lub niezamierzonemu powtarzaniu znaków podczas zdalnego sterowania.

- **Show Virtual Keyboard**: wyświetla klawiaturę ekranową w konsoli i umożliwia jej używanie.

    ![Wyświetlanie klawiatury ekranowej](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: zamienia klawisze Cmd i Ctrl, aby zapewnić zgodność klawiatury między różnymi systemami operacyjnymi.

- **Mouse**: włącz lub wyłącz mysz sterowanego urządzenia.

- **Show Local Cursor**: wyświetla na ekranie kursor myszy bieżącego urządzenia.

- **Mouse Jiggle**: symuluje niewielkie, okresowe ruchy myszy, aby zapobiec uśpieniu sterowanego urządzenia wskutek długiej bezczynności, np. podczas zdalnych spotkań lub zarządzania serwerami.

- **Scroll Rate**: określa szybkość przewijania kółkiem myszy lub liczbę wierszy/jednostek przewijanych przy obrocie kółka, wpływając na szybkość przesuwania treści na zdalnym ekranie.

- **Scroll Direction**: określa, czy obrót kółka myszy w górę lub w dół przesuwa treść na zdalnym ekranie w tym samym kierunku (przewijanie naturalne), czy w przeciwnym (przewijanie tradycyjne).

    Dostępne są cztery tryby kierunku: Standard, Vertical Invert, Horizontal Invert i Both Invert.

- **Mouse Mode**: umożliwia przełączanie między trybami Absolute Mode i Relative Mode, aby zapewnić płynne i dokładne sterowanie kursorem w różnych zastosowaniach zdalnych.

    !!! note "Czym różnią się Absolute Mode i Relative Mode?"

        - **Relative Mode**: pozycja myszy jest obliczana na podstawie ruchu zamiast stałych współrzędnych ekranu. Aby sterować myszą, kliknij wewnątrz okna zdalnego. Kursor jest zablokowany w obszarze zdalnego ekranu i nie można go płynnie wyprowadzić poza ten obszar. Ten tryb zapewnia lepszą zgodność z BIOS-em, starszymi systemami i urządzeniami wbudowanymi.

        - **Absolute Mode**: pozycja myszy odpowiada dokładnym współrzędnym ekranu. Zdalny kursor płynnie i precyzyjnie podąża za lokalnym, umożliwiając swobodne przechodzenie między ekranem lokalnym a zdalnym. Tryb sprawdza się podczas codziennej pracy z pulpitem i precyzyjnych operacji, choć transmisja sieciowa może powodować niewielkie opóźnienie.

        Do płynnej codziennej pracy używaj trybu Absolute. Tryb Relative sprawdza się w BIOS-ie, na starszych urządzeniach bez obsługi pozycjonowania bezwzględnego lub gdy chcesz uniknąć przypadkowego ruchu kursora.

- **Relative Sensitivity**: opcja dostępna, gdy ustawienie Mouse Mode ma wartość Relative.

### System {#system}

Możesz dostosować ustawienia wyświetlania konsoli lub zresetować urządzenie jednym kliknięciem.

![Ustawienia systemu](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-system.png){class="glboxshadow"}

- **Device Identity**: dostosuj lub zmień identyfikację KVM widoczną dla sterowanego urządzenia. EDID i identyfikacja urządzenia pozostają zsynchronizowane: zmiana jednego ustawienia automatycznie aktualizuje drugie, zapewniając prawidłowe rozpoznawanie urządzenia.

    ![Identyfikacja urządzenia](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/device-identity.png){class="glboxshadow"}

- **Language**: ustaw język konsoli na chiński lub angielski.

- **Color Mode**: wybierz jasny motyw Light lub ciemny Dark.

- **Time Zone**: dostosuj strefę czasową konsoli KVM.

- **Reset KVM**: przywróć ustawienia fabryczne KVM jednym kliknięciem.

### Sieć {#network}

Możesz sprawdzać i zmieniać ustawienia sieciowe Comet Q, takie jak nazwa hosta i adres IP.

![Ustawienia sieci](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-network.png){class="glboxshadow"}

- **Hostname**: możesz zmienić nazwę hosta urządzenia bezpośrednio w konsoli.

    ![Zmiana nazwy hosta](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/hostname.png){class="glboxshadow"}

- **Wi-Fi**: po połączeniu Comet Q z siecią Wi-Fi w tym miejscu pojawi się jego adres IP w tej sieci. Kliknij identyfikator SSID Wi-Fi lub strzałkę w prawo, aby wyświetlić szczegóły sieci, w tym SSID, przypisany adres IP, bramę i adres MAC używany przez Comet Q do połączenia.

    ![Konfiguracja Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/wifi-config.png){class="glboxshadow"}

    Aby połączyć urządzenie z inną siecią Wi-Fi, kliknij **Switch Wi-Fi** i wybierz sieć z listy dostępnych sieci.

## Narzędzia {#toolbox}

W konsoli przejdź do **Toolbox**. Strona narzędzi obejmuje trzy sekcje:

- [Schowek](#clipboard)
- [Skróty](#shortcut)
- [Terminal](#terminal)

### Schowek {#clipboard}

Schowek pozwala łatwo wklejać tekst z urządzenia sterującego do sterowanego bez przesyłania plików.

![Schowek w narzędziach](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-clipboard.png){class="glboxshadow"}

### Skróty {#shortcut}

Skróty pozwalają szybciej wykonywać działania bez użycia klawiatury ekranowej, usprawniając codzienną pracę. Tutaj znajdziesz często używane skróty.

![Skróty w narzędziach — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut1.png){class="glboxshadow"}

Kliknij **Modify**, aby dostosować dostępne skróty.

![Skróty w narzędziach — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut2.png){class="glboxshadow"}

### Terminal {#terminal}

Możesz otworzyć terminal urządzenia Comet Q, aby wprowadzić zaawansowane ustawienia. Kliknij **Access**.

![Terminal w narzędziach — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal1.png){class="glboxshadow"}

Nastąpi przekierowanie do terminala GLKVM.

![Terminal w narzędziach — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal2.png){class="glboxshadow"}

## Nośniki wirtualne {#virtual-media}

W konsoli przejdź do **Virtual Media**. Comet Q może emulować dysk USB z możliwością odczytu i zapisu, umożliwiając udostępnianie plików między urządzeniem sterującym a sterowanym oraz zarządzanie nimi.

![Nośniki wirtualne](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-media.png){class="glboxshadow"}

### Udostępnianie plików {#file-sharing}

**Aby udostępnić pliki z urządzenia sterującego sterowanemu urządzeniu, wykonaj poniższe kroki.**

1. Przeciągnij pliki z urządzenia sterującego do pola przesyłania lub kliknij to pole, aby je wybrać. Możesz też przesłać pliki z adresu URL.

    Po przesłaniu pliki będą widoczne w następujący sposób.

    ![Udostępnianie plików — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing1.png){class="glboxshadow"}

2. Kliknij **Mount To Remote** -> **File Sharing**.

    ![Udostępnianie plików — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing2.png){class="glboxshadow"}

3. W konsoli pojawi się okno z instrukcjami udostępniania plików, jak pokazano poniżej.

    ![Udostępnianie plików — krok 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing3.png){class="glboxshadow"}

4. Poczekaj chwilę, aż na ekranie pojawi się automatycznie dysk **"GLKVM"**. Pliki przesłane wcześniej z urządzenia sterującego do Comet Q będą udostępnione sterowanemu urządzeniu. Możesz je teraz przeglądać, przenosić i usuwać z tego dysku na sterowanym urządzeniu.

    ![Udostępnianie plików — krok 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing4.png){class="glboxshadow"}

    **Wskazówka**: Jeśli dysk nie pojawi się automatycznie, otwórz **This PC** na sterowanym urządzeniu.

    ![Widok This PC](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/thispc.png){class="glboxshadow"}

    Następnie znajdź dysk **GLKVM**. Możesz przeglądać, przenosić i usuwać znajdujące się na nim pliki.

5. Aby zakończyć udostępnianie, kliknij **Virtual Media** na pasku narzędzi, a następnie **Stop Sharing**.

    ![Zatrzymywanie udostępniania — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing1.png){class="glboxshadow"}

**Aby udostępnić pliki z sterowanego urządzenia urządzeniu sterującemu, wykonaj poniższe kroki.**

1. Na sterowanym urządzeniu przenieś lub skopiuj pliki, które chcesz udostępnić, na dysk **GLKVM**.

    Na przykład plik PDF o nazwie "gl-rm10_datasheet" został przeniesiony z pulpitu sterowanego urządzenia na dysk **GLKVM**.

    ![Udostępnianie plików — krok 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing5.png){class="glboxshadow"}

2. Wróć do konsoli Comet Q, kliknij **Virtual Media** na pasku narzędzi, a następnie **Stop Sharing**.

    ![Zatrzymywanie udostępniania — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing2.png){class="glboxshadow"}

3. Plik pojawi się w sekcji **Virtual Media**, jak pokazano poniżej. Teraz możesz pobrać go z Comet Q na urządzenie sterujące.

    ![Udostępnianie plików — krok 6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing6.png){class="glboxshadow"}

### Formatowanie dysku {#format-disk}

Jednym kliknięciem możesz sformatować dysk lub wyłączyć nośniki wirtualne.

![Formatowanie dysku](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/format-disable.png){class="glboxshadow"}

- **Format**: usuwa wszystkie dane z dysku i ponownie tworzy strukturę jego systemu plików.

- **Disable**: wyłączenie nośników wirtualnych spowoduje natychmiastowe ponowne uruchomienie urządzenia KVM.

## Centrum aplikacji {#apps-center}

W konsoli przejdź do **Apps Center**. Tutaj znajdziesz zintegrowane aplikacje.

![Centrum aplikacji](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} to usługa sieci mesh VPN oparta na WireGuard, która tworzy szyfrowane, prywatne połączenia między urządzeniami bez przekierowywania portów ani skomplikowanej konfiguracji zapory.

Comet Q integruje się z Tailscale, umożliwiając zdalny dostęp przez wirtualną sieć Tailscale.

Powiąż Comet Q i urządzenie sterujące z tym samym kontem Tailscale. Następnie wpisz **wirtualny adres IP Tailscale** urządzenia Comet Q w przeglądarce na urządzeniu sterującym, aby uzyskać do niego zdalny dostęp bez instalowania aplikacji GLKVM. Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_tailscale.md){target="_blank"}.

Po powiązaniu konsola wyświetla powiązane konto Tailscale i udostępnia zaawansowane funkcje, w tym Exit Node i Subnet Routes.

![Włączona usługa Tailscale](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} tworzy szyfrowane wirtualne sieci nakładkowe, które łączą urządzenia w różnych lokalizacjach na całym świecie tak, jakby znajdowały się w tej samej sieci lokalnej.

Comet Q integruje się z ZeroTier, umożliwiając zdalny dostęp przez wirtualną sieć ZeroTier.

Dołącz Comet Q i urządzenie sterujące do tej samej sieci ZeroTier. Następnie wpisz **adres IP ZeroTier** urządzenia Comet Q w przeglądarce na urządzeniu sterującym, aby uzyskać do niego zdalny dostęp bez instalowania aplikacji GLKVM. Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_zerotier.md){target="_blank"}.

Po powiązaniu konsola wyświetla identyfikator sieci ZeroTier i wirtualny adres IP.

![Włączona usługa ZeroTier](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-zerotier-enabled.png){class="glboxshadow"}

## Pomoc {#help}

W konsoli przejdź do **Help**. Tutaj znajdziesz więcej informacji o urządzeniach KVM GL.iNet i dokumentację pomocy, a także wyeksportujesz dzienniki do rozwiązywania problemów.

![Pomoc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/help.png){class="glboxshadow"}

## Pasek narzędzi {#toolbar}

W prawym górnym rogu konsoli znajdziesz następujące narzędzia:

- [Zwijanie paska narzędzi](#collapse)
- [Pełny ekran](#fullscreen)
- [Aktualizacja](#upgrade)
- [Usługa chmurowa](#cloud-service)
- [Zabezpieczenia](#security)
- Ponowne uruchomienie
- Wylogowanie

### Zwijanie {#collapse}

Kliknij ikonę strzałki w górę w prawym górnym rogu, aby zwinąć pasek narzędzi.

![Zwijanie paska narzędzi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse1.png){class="glboxshadow"}

Gdy pasek narzędzi jest zwinięty, kliknij strzałkę w dół u góry, aby go rozwinąć.

![Zwijanie paska narzędzi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse2.png){class="glboxshadow"}

### Pełny ekran {#fullscreen}

Kliknij ikonę pełnego ekranu (kwadrat) w prawym górnym rogu, aby włączyć tryb pełnoekranowy.

![Tryb pełnoekranowy](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen1.png){class="glboxshadow"}

Aby wyjść z trybu pełnoekranowego, naciśnij i przytrzymaj klawisz **Esc** lub kliknij ikonę wyjścia z pełnego ekranu (siatka) w prawym górnym rogu.

![Tryb pełnoekranowy](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen2.png){class="glboxshadow"}

### Aktualizacja {#upgrade}

Kliknij numer wersji oprogramowania układowego w prawym górnym rogu, aby sprawdzić dostępność aktualizacji.

![Aktualizacja oprogramowania układowego](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade1.png){class="glboxshadow"}

W wyświetlonym oknie możesz wykonać aktualizację online, jeśli dostępne jest nowsze oprogramowanie układowe. Możesz też pobrać najnowsze oprogramowanie z [centrum pobierania oprogramowania](https://dl.gl-inet.com/kvm){target="_blank"} i w razie potrzeby wykonać aktualizację lokalną.

![Aktualizacja oprogramowania układowego](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade2.png){class="glboxshadow"}

### Usługa chmurowa {#cloud-service}

Chmura KVM GL.iNet umożliwia zdalny dostęp do sterowanego urządzenia. Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_cloud.md){target="_blank"}.

Po powiązaniu Comet Q z chmurą konsola wyświetla stan chmury w następujący sposób.

![Usługa chmurowa](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/cloud.png){class="glboxshadow"}

### Zabezpieczenia {#security}

Sekcja Security umożliwia zmianę hasła administratora, włączenie uwierzytelniania dwuskładnikowego i dostosowanie certyfikatu TLS.

![Zabezpieczenia](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/security.png){class="glboxshadow"}

- Zmiana hasła administratora

    ![Zmiana hasła administratora](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/admin-password.png){class="glboxshadow" width="434"}

- 2FA: włącz uwierzytelnianie dwuskładnikowe, aby chronić konto.

    ![Uwierzytelnianie dwuskładnikowe 2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/2fa.png){class="glboxshadow"}

- Certyfikat TLS

    Do dostępu przez przeglądarkę system używa fabrycznie zainstalowanego certyfikatu domyślnego. Aby używać własnego certyfikatu TLS, kliknij **TLS Certificate** w prawym górnym rogu konsoli, wybierz **Custom Certificate**, a następnie prześlij **plik certyfikatu i plik klucza prywatnego**.

    ![Własny certyfikat TLS](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/tls-certificate.png){class="glboxshadow"}
