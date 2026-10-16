# Co zrobić, jeśli nie słychać dźwięku z urządzenia docelowego {#what-should-i-do-if-theres-no-audio-from-the-controlled-device}

Jeśli po połączeniu KVM z urządzeniem docelowym nie słychać z niego dźwięku (np. podczas odtwarzania filmów), skorzystaj z poniższych wskazówek:

1. Upewnij się, że w konsoli KVM włączono Speaker.

    W konsoli KVM przejdź do **Settings** -> **Remote Device Settings** -> **Speaker** i upewnij się, że głośnik jest włączony. Sprawdź też, czy ikona w prawym dolnym rogu jest podświetlona, co oznacza jej aktywność.

    ![Głośnik](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/speaker.png){class="glboxshadow"}

2. Upewnij się, że wszystkie przewody między KVM a urządzeniem docelowym są dobrze podłączone. Luźne połączenia mogą wpływać na wyjście dźwięku.

3. Sprawdź, czy podłączony jest konwerter HDMI. Niektóre konwertery nie obsługują dźwięku.

    Zalecamy użycie dołączonego przewodu HDMI, ponieważ niektóre przewody zgodne ze starszymi standardami HDMI mogą nie obsługiwać transmisji dźwięku.

4. Sprawdź, czy urządzenie sterujące i urządzenie docelowe nie są wyciszone.

5. Sprawdź ustawienia wyjścia dźwięku urządzenia docelowego i upewnij się, że wybrano **GLKVM**.

    ??? "macOS"

        Na urządzeniu docelowym przejdź do **Settings** -> **Sound** -> **Output & Input** -> **Output** i zmień urządzenie wyjściowe na **GLKVM**.

        ![Ustawienia wyjścia dźwięku w macOS](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/mac_output_settings.png){class="glboxshadow"}

    ??? "Windows"

        Na urządzeniu docelowym przejdź do **Settings** -> **Sound** -> **Output** i zmień urządzenie wyjściowe na **GLKVM**.

        ![Ustawienia wyjścia dźwięku w Windows — krok 1](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_1.png){class="glboxshadow"}

        ![Ustawienia wyjścia dźwięku w Windows — krok 2](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_2.png){class="glboxshadow"}

        Możesz też kliknąć ikonę dźwięku w prawym dolnym rogu ekranu urządzenia docelowego i wybrać **GLKVM** jako urządzenie odtwarzające.

        ![Ustawienia wyjścia dźwięku w Windows — krok 3](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_3.png){class="glboxshadow"}

6. Sprawdź sterownik karty graficznej urządzenia docelowego. Jeśli sterownik nie jest zainstalowany, urządzenie nie będzie mogło wysyłać dźwięku, więc nie będzie on słyszalny na urządzeniu sterującym.

7. Sprawdź zaawansowane ustawienia dźwięku urządzenia sterującego i upewnij się, że wyjście dźwięku przeglądarki nie jest wyciszone.

    Poniżej przedstawiono przykładowe zaawansowane ustawienia dźwięku w Windows 10 Pro.

    Przejdź do **Settings** -> **Sound** -> **Advanced sound options**.

    ![Zaawansowane opcje dźwięku](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/advanced_sound_options.png){class="glboxshadow"}

    Dostosuj głośność poszczególnych aplikacji i dźwięków systemowych.

    ![Głośność aplikacji](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/app_volume.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
