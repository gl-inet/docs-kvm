# Często zadawane pytania o Comet Q {#frequently-asked-questions-about-comet-q}

## Ogólne {#general}

1. **P: Co zrobić, jeśli ekran sterowania KVM wyświetla "Unable to Display" po połączeniu Comet Q z sterowanym urządzeniem?**

    O: Sterowane urządzenie nie obsługuje **USB-C DisplayPort Alt Mode**, co uniemożliwia przesyłanie obrazu.

    Sprawdź [tutaj](../../tutorials/how_to_check_usb-c_port_dp_alt_mode.md), czy Twoje urządzenie obsługuje DisplayPort Alt Mode.

2. **P: Dlaczego na urządzeniu sterującym nie pojawia się klawiatura do wpisania hasła, gdy ekran sterowanego urządzenia jest zablokowany?**

    O: Ze względu na ograniczenia bezpieczeństwa iOS/Android system blokuje stronę wpisywania hasła podczas klonowania ekranu lub zdalnego sterowania. Możesz wpisać hasło odblokowania bezpośrednio po stronie urządzenia sterującego, aby odblokować urządzenie.

3. **P: Dlaczego dźwięk nie jest przesyłany do urządzenia sterującego, gdy na sterowanym urządzeniu trwa połączenie głosowe?**

    O: Problem ten występuje zwykle na iPhone'ach i niektórych urządzeniach z Androidem. Gdy na sterowanym urządzeniu aplikacja komunikacyjna (np. WhatsApp lub Microsoft Teams) obsługuje połączenie głosowe, ograniczenia systemu iOS/Android pozwalają odtwarzać dźwięk tylko przez lokalne głośniki sterowanego urządzenia. Dźwięk nie może wtedy być przesyłany przez KVM do urządzenia sterującego.

    **Wskazówka**: Dźwięk multimediów (filmów, muzyki, gier itp.) może być normalnie przesyłany przez KVM do urządzenia sterującego, gdy aplikacje komunikacji głosowej są nieaktywne.

## iOS {#ios}

1. **P: Dlaczego po podłączeniu do Comet Q nie mogę regulować głośności systemowej na urządzeniach z iOS?**

    O: Ze względu na ograniczenia iOS po podłączeniu iPhone'a/iPada do urządzenia klonującego ekran, takiego jak KVM GL.iNet, które jest ustawione jako wyjście audio, systemowa regulacja głośności staje się niedostępna.

2. **P: Dlaczego urządzenie z iOS nie wyświetla lokalnie obrazu podczas strumieniowego odtwarzania filmów w aplikacjach wideo?**

    O: Gdy urządzenie z iOS jest połączone z urządzeniem klonującym ekran, takim jak KVM GL.iNet, niektóre aplikacje wideo (np. YouTube lub Netflix) domyślnie przesyłają obraz przez **AirPlay**, przez co urządzenie z iOS nie wyświetla go lokalnie. Nie można wyłączyć tego zachowania na poziomie systemu.

    Aby sterowane urządzenie odtwarzało filmy lokalnie podczas klonowania ekranu, odtwarzaj je w przeglądarce internetowej.

3. **P: Co zrobić, jeśli po podłączeniu do Comet Q na urządzeniu z iOS znika klawiatura ekranowa?**

    O: Prawdopodobnie iOS rozpoznaje Comet Q jako zewnętrzną klawiaturę fizyczną i automatycznie ukrywa systemową klawiaturę ekranową. W takim przypadku używaj klawiatury urządzenia sterującego lub klawiatury ekranowej wbudowanej w konsolę KVM.

    Jeśli nadal potrzebujesz klawiatury ekranowej iOS, przejdź do **Settings** > **Accessibility** > **Touch** > **AssistiveTouch**, a następnie włącz **Show Onscreen Keyboard**.

    ![Ustawienia AssistiveTouch](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/assistive_touch.png){class="glboxshadow" width="360"}

4. **P: Podczas klonowania ekranu iPhone'a/iPada w orientacji pionowej lub poziomej kursor po stronie sterującej nadal jest przesunięty, nawet po zmianie orientacji ekranu w konsoli KVM. Co zrobić?**

    O: Dokładne śledzenie kursora na iPhonie lub iPadzie wymaga zgodności orientacji żyroskopu urządzenia z orientacją wyświetlanego obrazu. Podczas zdalnego sterowania system może nieprawidłowo wykrywać bieżący stan żyroskopu, powodując przesunięcie kursora.

    Aby rozwiązać problem, włącz **Portrait Orientation Lock**/**Rotation Lock** na iPhonie/iPadzie, co zapewni dokładne śledzenie kursora.

    ![Blokada orientacji pionowej](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/portrait_lock.png){class="glboxshadow" width="360"}
    <small>(Portrait Orientation Lock on iPhone)</small>

5. **P: Dlaczego klawiatura nie działa prawidłowo na urządzeniach z iOS, niektóre klawisze nie reagują lub wskaźnik myszy się przesuwa?**

    O: Zwykle przyczyną jest włączona funkcja **Mouse Keys** na urządzeniu z iOS. Umożliwia ona przesuwanie wskaźnika myszy za pomocą klawiatury lub klawiatury numerycznej.

    Aby rozwiązać problem, przejdź do **Settings** > **Accessibility** > **Touch** > **AssistiveTouch** > **Mouse Keys** i wyłącz Mouse Keys.

## Android {#android}

1. **P: Dlaczego nie mogę sterować urządzeniem w bezwzględnym trybie myszy?**

    O: Ze względu na ograniczenia systemu Android urządzeniami z Androidem można sterować tylko we względnym trybie myszy.

    Podczas sterowania przez aplikację mobilną glkvm całkowicie zakryj palcem wskaźnik myszy, aby wykonywać operacje.

2. **P: Co zrobić, jeśli obraz po stronie sterującej nie jest zsynchronizowany z ekranem sterowanego telefonu z Androidem?**

    O: Niektóre telefony z Androidem rozpoznają Comet Q jako dodatkowy ekran zamiast ekranu klonowanego. Aby to zmienić, ustaw na telefonie tryb **Screen Mirroring**.

    Przykład dla serii Samsung S:

    Przejdź do **Settings** > **Device Connections** > **Samsung DeX** > **Connected Display**, a następnie wybierz tryb **Screen Mirroring**.

---

Masz dodatkowe pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
