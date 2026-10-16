# Comet PoE (GL-RM1PE) — przewodnik po konsoli {#comet-poe-gl-rm1pe-console-guide}

## Sesja {#session}

W konsoli przejdź do **Session**. Strona ustawień obejmuje cztery sekcje:

- [Wideo](#video)
- [Dźwięk i kamera](#audio-camera)
- [Klawiatura](#keyboard)
- [Mysz](#mouse)

### Wideo {#video}

W sekcji Session możesz dostosować ustawienia wideo, takie jak tryb wyświetlania, jakość i przesyłanie obrazu, orientacja ekranu oraz EDID.

![Ustawienia wideo](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/session_video.png){class="glboxshadow"}

- **Transfer**: wybierz sposób przesyłania obrazu: WebRTC, WebRTC (FEC), WebRTC (Native) lub Direct. Pamiętaj, że tryb Direct nie przesyła dźwięku.

    !!! note "Czym różnią się WebRTC, WebRTC (FEC), WebRTC (Native) i Direct?"

        - **WebRTC**: zapewnia równowagę między płynnym obrazem a stabilnym dźwiękiem podczas zdalnego sterowania w czasie rzeczywistym.

        - **WebRTC (FEC)**: dodaje korekcję błędów, aby poprawić stabilność połączenia przy słabej lub niestabilnej sieci. Po wybraniu tej opcji utracone pakiety danych są automatycznie odtwarzane przez przesyłanie niewielkiej ilości danych nadmiarowych, co ogranicza migotanie obrazu i opóźnienia.

        - **WebRTC (Native)**: wykorzystuje bibliotekę Google WebRTC, aby zwiększyć wydajność przesyłania strumieniowego i płynność zdalnego sterowania w czasie rzeczywistym. Ten tryb przesyłania wprowadzono w oprogramowaniu układowym v1.10.0.

        - **Direct**: zapewnia najniższe opóźnienia i bezstratną jakość obrazu, ale nie obsługuje przesyłania dźwięku.

- **Mode**: w razie potrzeby przełączaj między trybami Smart i Normal. Tryb Smart pomaga zmniejszyć wykorzystanie pasma, zwłaszcza przy słabym połączeniu sieciowym.

- **Latency Mode**: możesz wybrać Lowest Latency lub Smooth Display. Tę funkcję wprowadzono w oprogramowaniu układowym v1.9.0.

    !!! note "Czym różnią się Lowest Latency i Smooth Display?"

        - **Lowest Latency**: minimalizuje opóźnienie sygnałów wejściowych, zapewniając szybszą reakcję klawiatury i myszy.

        - **Smooth Display**: optymalizuje wyświetlanie, aby eliminować zacięcia i utratę klatek oraz zapewniać płynne odtwarzanie.

- **Quality**: dostosuj jakość obrazu do warunków sieciowych i wymaganej rozdzielczości, wybierając Auto/Low/Medium/High/Ultra-high/Lossless.

- **FEC Packets**: przy niestabilnym połączeniu automatycznie odtwarza utracone pakiety przez wysyłanie niewielkiej ilości danych nadmiarowych, ograniczając migotanie obrazu i opóźnienia. Możesz ustawić współczynnik FEC na 5%/10%/15%/20%.

- **Orientation**: ustaw kąt obrotu obrazu konsoli na 0°/90°/180°/270°.

- **EDID**: skrót od Extended Display Identification Data; umożliwia automatyczne dopasowanie optymalnych parametrów wyświetlania.

    Ustawienie domyślne sprawdza się w większości sytuacji i zwykle nie wymaga zmiany. Szczegóły znajdziesz [tutaj](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. Jeśli po zmianie EDID obraz się nie odświeża, uruchom ponownie sterowane urządzenie.

- **View**: określa sposób skalowania obrazu przy zmianie rozmiaru okna przeglądarki. Dostępne opcje: Adaptive, Best Picture Quality, Original Pixel. Tę funkcję wprowadzono w oprogramowaniu układowym v1.8.0.

### Dźwięk i kamera {#audio-camera}

Możesz dostosować ustawienia dźwięku i kamery sterowanego urządzenia.

![Dźwięk i kamera](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/session_audio_camera.png){class="glboxshadow"}

- **Speaker**: steruje dźwiękiem wychodzącym z sterowanego urządzenia (np. dźwiękami systemowymi lub dźwiękiem filmów).

- **Microphone**: przesyła lokalny dźwięk (np. Twój głos) z urządzenia sterującego do urządzenia zdalnego. Obsługuje wyciszanie jednym kliknięciem i skrót aktywujący mikrofon podczas przytrzymywania (Press To Speak).

    **Uwaga**: Przed użyciem skrótu należy go ręcznie skonfigurować w [ustawieniach](#usb-devices).

- **Camera**: po włączeniu kamery na urządzeniu sterującym lokalny obraz wideo jest przekazywany do zdalnego komputera, na którym emulowana jest wirtualna kamera USB. Aplikacje działające na zdalnym komputerze (np. narzędzia konferencyjne i FaceTime) mogą korzystać z tego obrazu tak samo jak z kamery fizycznie do niego podłączonej.

    **Uwaga**: Tę funkcję wprowadzono w oprogramowaniu układowym v1.10.0 i jest ona obsługiwana wyłącznie w trybie WebRTC (FEC). Obecnie można z niej korzystać tylko w przeglądarce internetowej; aplikacja mobilna i klient na komputer nie są jeszcze obsługiwane.

### Klawiatura {#keyboard}

Sekcja Keyboard umożliwia skonfigurowanie obsługi klawiatury na sterowanym urządzeniu.

![Ustawienia klawiatury](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/session_keyboard.png){class="glboxshadow"}

- **Bad Link Mode**: natychmiast zwalnia klawisze. Każde naciśnięcie jest przesyłane jako pojedyncze szybkie naciśnięcie i zwolnienie, co zapobiega zablokowaniu klawiszy lub niezamierzonemu powtarzaniu znaków podczas zdalnego sterowania.

- **Show Virtual Keyboard**: wyświetla klawiaturę ekranową w konsoli i umożliwia jej używanie.

    ![Wyświetlanie klawiatury ekranowej](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/session_virtual_keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: zamienia klawisze Cmd i Ctrl, aby zapewnić zgodność klawiatury między różnymi systemami operacyjnymi.

### Mysz {#mouse}

Możesz dostosować ustawienia myszy, aby wygodniej korzystać z sterowanego urządzenia.

![Ustawienia myszy](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/session_mouse.png){class="glboxshadow"}

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

- **Primary Button**: wybierz lewy lub prawy przycisk jako przycisk główny. Tę funkcję wprowadzono w oprogramowaniu układowym v1.9.0.

## Narzędzia {#toolbox}

W konsoli przejdź do **Toolbox**. Strona narzędzi obejmuje pięć sekcji:

- [Schowek](#clipboard)
- [OCR](#ocr)
- [Skróty](#shortcut)
- [Wake on LAN](#wake-on-lan)
- [Terminal](#terminal)

### Schowek {#clipboard}

Schowek pozwala łatwo wklejać tekst z urządzenia sterującego do sterowanego bez przesyłania plików.

![Schowek w narzędziach](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_clipboard.png){class="glboxshadow"}

### OCR {#ocr}

OCR to funkcja rozpoznawania tekstu, która umożliwia zaznaczenie obszaru zdalnego ekranu i łatwe wyodrębnienie z niego tekstu. Tę funkcję wprowadzono w oprogramowaniu układowym v1.9.0.

Aby z niej skorzystać, kliknij strzałkę w dół i wybierz język rozpoznawania: chiński, angielski lub tryb dwujęzyczny (Zh/En).

![Język rozpoznawania tekstu](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_ocr_language.png){class="glboxshadow"}

Następnie kliknij **Capture**. Zdalny ekran zostanie przyciemniony. Zaznacz prostokątem tekst, który chcesz wyodrębnić, a system automatycznie go rozpozna. Rozpoznany tekst możesz skopiować.

![Kopiowanie tekstu](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_ocr_copy_text.png){class="glboxshadow"}

Dzięki tej funkcji możesz łatwo przechwycić tekst ze zdalnego ekranu (sterowanego urządzenia) i skopiować go na lokalne urządzenie sterujące.

### Skróty {#shortcut}

Skróty pozwalają szybciej wykonywać działania bez użycia klawiatury ekranowej, usprawniając codzienną pracę. Tutaj znajdziesz często używane skróty.

![Skróty w narzędziach — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_shortcut_1.png){class="glboxshadow"}

Kliknij **Modify**, aby dostosować dostępne skróty.

![Skróty w narzędziach — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_shortcut_2.png){class="glboxshadow"}

### Wake-on-LAN {#wake-on-lan}

Wake-on-LAN (WOL) to technologia umożliwiająca zdalne włączenie sterowanego urządzenia lub wybudzenie go ze stanu niskiego poboru energii.

Kliknij **Add Device** i wybierz urządzenie z tej samej sieci LAN.

![Wake-on-LAN w narzędziach](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_wol.png){class="glboxshadow"}

![Dodawanie urządzenia Wake-on-LAN](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/wol-add-device.png){class="glboxshadow" width=500}

Jeśli urządzenia, które chcesz dodać, nie ma na liście, kliknij **Add Manually** i wpisz jego nazwę oraz adres MAC.

![Ręczne dodawanie urządzenia Wake-on-LAN](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/wol-add-manually.png){class="glboxshadow" width=500}

### Terminal {#terminal}

Możesz otworzyć terminal urządzenia Comet PoE, aby wprowadzić zaawansowane ustawienia. Kliknij **Access**.

![Terminal w narzędziach — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_terminal_1.png){class="glboxshadow"}

Nastąpi przekierowanie do terminala GLKVM.

![Terminal w narzędziach — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_terminal_2.png){class="glboxshadow"}

## Akcesoria {#accessories}

GL.iNet oferuje opcjonalne akcesoria KVM do zdalnego włączania i wyłączania zasilania urządzenia.

Najpierw zapoznaj się z odpowiednim podręcznikiem użytkownika, aby podłączyć akcesorium do sterowanego urządzenia.

- [Fingerbot (FGB-01) — podręcznik użytkownika](../gl-fgb-01/index.md){target="_blank"}

- [Płytka ATX (GL-ATXPC) — podręcznik użytkownika](../gl-atx-board/index.md){target="_blank"}

Następnie zaloguj się do konsoli KVM i przejdź do **Accessories**. Ustawienia akcesorium są dostępne dopiero po jego zainstalowaniu.

### Fingerbot {#fingerbot}

Fingerbot przykleja się przy fizycznym przycisku zasilania sterowanego urządzenia, aby zdalnie sterować jego zasilaniem.

Działa zgodnie z ustawieniami w konsoli.

![Ustawienia akcesorium Fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/fingerbot.png){class="glboxshadow"}

- **Time**: czas naciskania przycisku przez Fingerbot. Możesz ustawić 0.5s/3s/8s.

- **Strength**: dostępne są dwa poziomy siły nacisku: Lightly Press i Firmly Press.

    - **Lightly Press**: do płytkich przycisków lub przycisków o małym oporze.

    - **Firmly Press**: do głębokich przycisków lub przycisków o dużym oporze.

    ![Tryb naciskania](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### Zasilanie ATX {#atx-power}

Płytkę ATX instaluje się w obudowie komputera, aby zdalnie go włączać, wyłączać i ponownie uruchamiać.

Działa zgodnie z ustawieniami w konsoli.

![Ustawienia zasilania ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/atxboard.png){class="glboxshadow"}

- **Power (Short Press)**: służy do zwykłego włączenia zasilania lub wybudzenia systemu.

- **Power (Long Press)**: wymusza wyłączenie urządzenia.

- **Restart**: uruchamia urządzenie ponownie.

## Nośniki wirtualne {#virtual-media}

W konsoli przejdź do **Virtual Media**. Tutaj możesz wykonywać następujące działania:

- [Udostępnianie plików](#file-sharing)
- [Montowanie obrazów](#image-mounting)
- [Zmiana nośnika danych](#replace-storage-drive)
- [Formatowanie dysku](#format-disk)

![Nośniki wirtualne](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/virtual-media.png){class="glboxshadow"}

### Udostępnianie plików {#file-sharing}

Comet PoE może emulować dysk USB z możliwością odczytu i zapisu, umożliwiając udostępnianie plików między urządzeniem sterującym a sterowanym oraz zarządzanie nimi.

**Aby udostępnić pliki z urządzenia sterującego sterowanemu urządzeniu, wykonaj poniższe kroki.**

1. Przeciągnij pliki z urządzenia sterującego do pola przesyłania lub kliknij to pole, aby je wybrać. Możesz też przesłać pliki z adresu URL.

    Po przesłaniu pliki będą widoczne w następujący sposób.

    ![Przesyłanie plików](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/file-sharing1.png){class="glboxshadow"}

2. Kliknij **Mount To Remote** -> **File Sharing**.

    ![Udostępnianie plików](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/file-sharing2.png){class="glboxshadow"}

3. W konsoli pojawi się okno z instrukcjami udostępniania plików, jak pokazano poniżej.

    ![Wskazówki udostępniania plików](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/file-sharing3.png){class="glboxshadow"}

4. Poczekaj chwilę, aż na ekranie automatycznie pojawi się dysk **"GLKVM"**. Pliki przesłane wcześniej z urządzenia sterującego do Comet PoE będą udostępnione sterowanemu urządzeniu. Możesz je teraz przeglądać, przenosić i usuwać z tego dysku na sterowanym urządzeniu.

    ![Dysk GLKVM](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/file-sharing4.png){class="glboxshadow"}

    **Wskazówka**: Jeśli dysk nie pojawi się automatycznie, otwórz **This PC** na sterowanym urządzeniu.

    ![Widok This PC](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/thispc.png){class="glboxshadow"}

    Następnie znajdź dysk **GLKVM**. Możesz przeglądać, przenosić i usuwać znajdujące się na nim pliki.

5. Aby zakończyć udostępnianie, kliknij **Virtual Media** na pasku narzędzi, a następnie **Stop Sharing**.

    ![Zatrzymywanie udostępniania — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/stop-sharing1.png){class="glboxshadow"}

**Aby udostępnić pliki z sterowanego urządzenia urządzeniu sterującemu, wykonaj poniższe kroki.**

1. Na sterowanym urządzeniu przenieś lub skopiuj pliki, które chcesz udostępnić, na dysk **GLKVM**.

    Na przykład plik PDF o nazwie "slate7pro_datasheet" został skopiowany z pulpitu sterowanego urządzenia na dysk **GLKVM**.

    ![Przenoszenie pliku na dysk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/file-sharing5.png){class="glboxshadow"}

2. Wróć do konsoli Comet PoE, kliknij **Virtual Media** na pasku narzędzi, a następnie **Stop Sharing**.

    ![Zatrzymywanie udostępniania — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/stop-sharing2.png){class="glboxshadow"}

3. Plik pojawi się w sekcji **Virtual Media**, jak pokazano poniżej. Teraz możesz pobrać go z Comet PoE na urządzenie sterujące.

    ![Udostępniony plik](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/file-sharing6.png){class="glboxshadow"}

### Montowanie obrazów {#image-mounting}

Comet PoE może emulować w sterowanym urządzeniu wirtualny napęd CD/DVD lub dysk tylko do odczytu. Dostęp do tego napędu jest możliwy podczas uruchamiania BIOS-u lub UEFI.

Ta funkcja umożliwia ponowną instalację systemu operacyjnego, zamontowanie obrazu ISO w celu instalacji aplikacji na sterowanym urządzeniu oraz wykonywanie innych zadań.

1. Przeciągnij plik do pola przesyłania lub kliknij to pole, aby go wybrać. **Upewnij się, że plik można zamontować jako obraz ISO**.

    Po przesłaniu pliki będą widoczne w następujący sposób.

    ![Montowanie obrazu — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/image-mounting1.png){class="glboxshadow"}

2. Kliknij **Mount To Remote** -> **Image Mounting**.

    ![Montowanie obrazu — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/image-mounting2.png){class="glboxshadow"}

3. W wyświetlonym oknie wybierz plik i kliknij **Mount Image**.

    ![Montowanie obrazu — krok 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/image-mounting3.png){class="glboxshadow"}

4. W konsoli pojawi się okno z instrukcjami montowania, jak pokazano poniżej.

    ![Montowanie obrazu — krok 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/image-mounting4.png){class="glboxshadow"}

5. Teraz możesz korzystać z tego pliku przez napęd CD na sterowanym urządzeniu.

    ![Montowanie obrazu — krok 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/image-mounting5.png){class="glboxshadow"}

### Zmiana nośnika danych {#replace-storage-drive}

Możesz podłączyć nośnik USB do portu USB urządzenia KVM, aby zastąpić pamięć wewnętrzną.

![Zmiana nośnika danych](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/replace-storage.png){class="glboxshadow"}

### Formatowanie dysku {#format-disk}

Jednym kliknięciem możesz sformatować dysk lub wyłączyć nośniki wirtualne.

![Formatowanie dysku](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/format-disable.png){class="glboxshadow"}

- **Format**: usuwa wszystkie dane z dysku i ponownie tworzy strukturę jego systemu plików.

- **Disable**: wyłączenie nośników wirtualnych spowoduje natychmiastowe ponowne uruchomienie urządzenia KVM.

## Centrum aplikacji {#apps-center}

W konsoli przejdź do **Apps Center**. Tutaj znajdziesz zintegrowane aplikacje.

![Centrum aplikacji](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} to usługa sieci mesh VPN oparta na WireGuard, która tworzy szyfrowane, prywatne połączenia między urządzeniami bez przekierowywania portów ani skomplikowanej konfiguracji zapory.

Comet PoE integruje się z Tailscale, umożliwiając zdalny dostęp przez wirtualną sieć Tailscale.

Powiąż Comet PoE i urządzenie sterujące z tym samym kontem Tailscale. Następnie wpisz **wirtualny adres IP Tailscale** urządzenia Comet PoE w przeglądarce na urządzeniu sterującym, aby uzyskać do niego zdalny dostęp bez instalowania aplikacji GLKVM. Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_tailscale.md){target="_blank"}.

Po powiązaniu konsola wyświetla powiązane konto Tailscale i udostępnia zaawansowane funkcje, w tym Exit Node i Subnet Routes.

![Włączona usługa Tailscale](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/app-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} tworzy szyfrowane wirtualne sieci nakładkowe, które łączą urządzenia w różnych lokalizacjach na całym świecie tak, jakby znajdowały się w tej samej sieci lokalnej.

Comet PoE integruje się z ZeroTier, umożliwiając zdalny dostęp przez wirtualną sieć ZeroTier.

Dołącz Comet PoE i urządzenie sterujące do tej samej sieci ZeroTier. Następnie wpisz **adres IP ZeroTier** urządzenia Comet PoE w przeglądarce na urządzeniu sterującym, aby uzyskać do niego zdalny dostęp bez instalowania aplikacji GLKVM. Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_zerotier.md){target="_blank"}.

Po powiązaniu konsola wyświetla identyfikator sieci ZeroTier i wirtualny adres IP.

![Włączona usługa ZeroTier](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/app-zerotier-enabled.png){class="glboxshadow"}

### NetBird {#netbird}

[NetBird](https://netbird.io/){target="_blank"} to platforma sieciowa typu zero trust o otwartym kodzie źródłowym, która umożliwia tworzenie bezpiecznych sieci prywatnych do użytku domowego i firmowego. Jako sieć nakładkowa oparta na WireGuard® zapewnia bezpieczny dostęp do urządzeń w dowolnym miejscu i czasie.

Comet PoE integruje się z NetBird, umożliwiając zdalny dostęp przez wirtualną sieć NetBird. Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_netbird.md){target="_blank"}.

Po powiązaniu konsola wyświetla wirtualny adres IP NetBird.

![Włączona usługa NetBird](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/app-netbird-enabled.png){class="glboxshadow"}

## Pomoc {#help}

W konsoli przejdź do **Help**. Tutaj znajdziesz więcej informacji o urządzeniach KVM GL.iNet i dokumentację pomocy, a także wyeksportujesz dzienniki do rozwiązywania problemów.

![Pomoc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/help.png){class="glboxshadow"}

## Pasek narzędzi {#toolbar}

W prawym górnym rogu konsoli znajdziesz następujące narzędzia:

- [Zwijanie paska narzędzi](#collapse)
- [Pełny ekran](#fullscreen)
- [Aktualizacja](#upgrade)
- [Statystyki połączenia](#connection-stats)
- [Usługa chmurowa](#cloud-service)
- [Wylogowanie](#logout)

### Zwijanie {#collapse}

Kliknij ikonę strzałki w górę w prawym górnym rogu, aby zwinąć pasek narzędzi.

![Zwijanie paska narzędzi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_collapse_1.png){class="glboxshadow"}

Gdy pasek narzędzi jest zwinięty, kliknij strzałkę w dół u góry, aby go rozwinąć.

![Zwijanie paska narzędzi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_collapse_2.png){class="glboxshadow"}

### Pełny ekran {#fullscreen}

Kliknij ikonę pełnego ekranu (kwadrat) w prawym górnym rogu, aby włączyć tryb pełnoekranowy.

![Tryb pełnoekranowy](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_fullscreen_1.png){class="glboxshadow"}

Aby wyjść z trybu pełnoekranowego, naciśnij i przytrzymaj klawisz **Esc** lub kliknij ikonę wyjścia z pełnego ekranu (siatka) w prawym górnym rogu.

![Tryb pełnoekranowy](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_fullscreen_2.png){class="glboxshadow"}

### Aktualizacja {#upgrade}

Kliknij numer wersji oprogramowania układowego w prawym górnym rogu, aby sprawdzić dostępność aktualizacji.

![Aktualizacja oprogramowania układowego — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_upgrade_1.png){class="glboxshadow"}

W wyświetlonym oknie możesz kliknąć **Local Upgrade**, aby przesłać plik oprogramowania układowego.

![Aktualizacja oprogramowania układowego — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_upgrade_2.png){class="glboxshadow" width=400}

![Aktualizacja oprogramowania układowego — krok 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_upgrade_3.png){class="glboxshadow" width=400}

Przed aktualizacją lokalną pobierz najnowsze oprogramowanie układowe z [centrum pobierania oprogramowania](https://dl.gl-inet.com/kvm){target="_blank"}.

### Statystyki połączenia {#connection-stats}

Sekcja Connection Stats zawiera panel danych, który monitoruje opóźnienia, ich zmienność i inne wskaźniki w czasie rzeczywistym.

Kliknij ikonę listy, aby wyświetlić stan urządzenia i bieżące dane.

![Panel danych — widok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_data_dashboard_1.png){class="glboxshadow"}

Kliknij ikonę wykresu, aby wyświetlić statystyki, w tym opóźnienia sieciowe, ich zmienność, utratę pakietów, bieżącą liczbę klatek na sekundę i opóźnienie odtwarzania.

![Panel danych — widok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_data_dashboard_2.png){class="glboxshadow"}

### Usługa chmurowa {#cloud-service}

Chmura KVM GL.iNet umożliwia zdalny dostęp do sterowanego urządzenia. Szczegóły znajdziesz [tutaj](../../faq/remote_access_via_cloud.md){target="_blank"}.

Po powiązaniu Comet PoE z chmurą konsola wyświetla stan chmury w następujący sposób.

![Usługa chmurowa](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_cloud_service.png){class="glboxshadow"}

### Wylogowanie {#logout}

Aby się wylogować, kliknij ikonę Logout.
![Wylogowanie z konsoli](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/logout.png){class="glboxshadow"}

## Ustawienia {#settings}
W konsoli kliknij ikonę Settings na pasku nawigacji, aby otworzyć poniższą stronę ustawień. Tę funkcję wprowadzono w oprogramowaniu układowym v1.10.0.

- [Urządzenia USB](#usb-devices)
- [Preferencje](#preferences)
- [Sieć](#network)
- [Zabezpieczenia](#security)
- [Chmura](#cloud)
- [System](#system)

![Ustawienia](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/settings.png){class="glboxshadow"}

### Urządzenia USB {#usb-devices}

Sekcja USB Device umożliwia centralne zarządzanie wszystkimi emulowanymi urządzeniami USB. Na tej stronie możesz włączać i wyłączać wirtualne urządzenia peryferyjne, aby poprawić zgodność z sterowanym komputerem.

![Emulowane urządzenia USB](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/settings_usb_devices.png){class="glboxshadow"}

- **Microphone**

    Gdy mikrofon jest wyciszony, kliknij Settings, aby dostosować skróty do swoich potrzeb. Naciśnij i przytrzymaj przypisany skrót, aby zacząć mówić. Zwolnienie klawisza ponownie wyciszy mikrofon.

    ![Ustawienia mikrofonu — krok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/mic_settings_1.png){class="glboxshadow" width=600}

    ![Ustawienia mikrofonu — krok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/mic_settings_2.png){class="glboxshadow" width=434}

  - **Device Identity**

    Dostosuj lub zmień identyfikację KVM widoczną dla sterowanego urządzenia. EDID i identyfikacja urządzenia pozostają zsynchronizowane: zmiana jednego ustawienia automatycznie aktualizuje drugie, zapewniając prawidłowe rozpoznawanie urządzenia.

    ![Identyfikacja urządzenia](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/settings_device_identity.png){class="glboxshadow" width=350}

### Preferencje {#preferences}

Sekcja Preferences umożliwia zarządzanie ustawieniami Layout Preferences, System Settings i Device Screen.

![Preferencje](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences**: w razie potrzeby włącz wyświetlanie paska narzędzi na pełnym ekranie i paska stanu w trybie okienkowym.

- **System Settings**: wybierz tytuł karty przeglądarki (Tab Title), język (Language: chiński, angielski lub japoński), motyw kolorystyczny (Color Mode: Light lub Dark) i strefę czasową (Timezone) odpowiednią dla Twojego regionu.

- **Device Screen**: możesz zarządzać ekranem urządzenia i wyświetlać jego podgląd. Dostępne ustawienia obejmują tryb Lock Screen (World Clock, Clock Only lub Wallpaper Only), Time Format, Date Format i Wallpaper.

### Sieć {#network}

Możesz sprawdzać i zmieniać ustawienia sieciowe Comet PoE, takie jak nazwa hosta i adres IP.

![Ustawienia sieci](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_network.png){class="glboxshadow"}

- **Hostname**: możesz zmienić nazwę hosta urządzenia bezpośrednio w konsoli. Tę funkcję wprowadzono w oprogramowaniu układowym v1.7.0.

    ![Zmiana nazwy hosta](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_network_hostname.png){class="glboxshadow" width=600}

- **Ethernet Settings**: gdy Comet PoE łączy się z nadrzędnym urządzeniem sieciowym za pomocą kabla Ethernet, tutaj wyświetlane są szczegóły tego połączenia.

    Jeśli używany jest protokół DHCP, strona wygląda następująco.

    ![Ustawienia DHCP połączenia Ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_network_dhcp.png){class="glboxshadow" width=600}

    Aby ustawić statyczny adres IP, zmień protokół na **Static** i wpisz wymagane parametry sieciowe (np. adres IP, maskę podsieci i bramę).

    ![Statyczny adres IP połączenia Ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_network_static.png){class="glboxshadow" width=600}

### Zabezpieczenia {#security}

Sekcja Security umożliwia zmianę hasła administratora, włączenie uwierzytelniania dwuskładnikowego i dostosowanie certyfikatu TLS.

![Zabezpieczenia](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_security.png){class="glboxshadow"}

- Zmiana hasła administratora

    ![Zmiana hasła administratora](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/change-password.png){class="glboxshadow" width="434"}

- 2FA: włącz uwierzytelnianie dwuskładnikowe, aby chronić konto.

    ![Uwierzytelnianie dwuskładnikowe 2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/2fa.png){class="glboxshadow"}

- Certyfikat TLS

    Do dostępu przez przeglądarkę system używa fabrycznie zainstalowanego certyfikatu domyślnego. Aby używać własnego certyfikatu TLS, kliknij **Custom** w sekcji TLS Certificate, a następnie prześlij **plik certyfikatu i plik klucza prywatnego**.

    ![Własny certyfikat TLS](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_security_custom.png){class="glboxshadow"}

### Chmura {#cloud}

Sekcja Cloud umożliwia zdalny dostęp do urządzenia i zarządzanie nim za pomocą usług chmurowych.

Możesz powiązać urządzenie z chmurą za pomocą adresu URL. W **More Settings** znajdziesz inne opcje, takie jak Bind With Code i App Download. W razie potrzeby możesz też użyć opcji Disable.

![Ustawienia chmury — widok 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_cloud_1.png){class="glboxshadow"}

Po pomyślnym powiązaniu możesz wyświetlić informacje o powiązanym koncie chmurowym. Kliknij **Access Cloud**, aby zarządzać urządzeniami, lub **More Settings**, aby w razie potrzeby wyłączyć usługę albo usunąć powiązanie.

![Ustawienia chmury — widok 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_cloud_2.png){class="glboxshadow"}

Te same operacje możesz wykonywać również przez Cloud Service na górnym pasku narzędzi.

### System {#system}

W ustawieniach System możesz skonfigurować następujące elementy:

![System](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_system.png){class="glboxshadow"}

- **System**: kliknij **Reboot**, aby ponownie uruchomić urządzenie, lub **Reset**, aby usunąć bieżącą konfigurację urządzenia i skonfigurować je od nowa.

- **Upgrade**: możesz włączyć Beta Center, aby otrzymywać aktualizacje testowych wersji oprogramowania układowego, lub użyć Local Upgrade, aby ręcznie zainstalować je z pliku lokalnego.

    ![Aktualizacja lokalna](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setthing_system_local_update.png){class="glboxshadow" width=400}

- **Help & Support**: opcja Export Log Files pozwala zapisać dzienniki działania urządzenia na potrzeby rozwiązywania problemów i pomocy posprzedażowej. Help Document udostępnia podręczniki użytkownika, odpowiedzi na często zadawane pytania i dokumentację rozwiązywania problemów.
