# Jak używać dźwięku dwukierunkowego podczas spotkań zdalnych? {#how-can-i-use-two-way-audio-for-remote-meetings}

Pracując z domu, możesz za pomocą KVM uzyskać dostęp do komputera w biurze i dołączyć do spotkań głosowych w Zoom, Microsoft Teams lub podobnej aplikacji. Funkcja dźwięku dwukierunkowego w urządzeniu KVM firmy GL.iNet pozwala mówić do mikrofonu lokalnego komputera i słuchać innych uczestników przez jego głośniki lub słuchawki.

## Szybka konfiguracja {#quick-setup}

Poniższe kroki pokazują na przykładzie spotkania w Zoom, jak używać mikrofonu i głośnika lokalnego urządzenia podczas spotkań zdalnych.

1. Przed dołączeniem do spotkania zaloguj się do KVM na komputerze sterującym i przejdź do **Session** -> **Audio & Camera**. Włącz **Speaker** i **Microphone**. Sprawdź, czy obie ikony w prawym dolnym rogu są aktywne.

    ![Włączanie głośnika i mikrofonu](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/enable-speaker-and-microphone.png){class="glboxshadow"}

    Na przykład po włączeniu **Microphone** przeglądarka może poprosić o dostęp do mikrofonu. Wybierz mikrofon, którego chcesz użyć, i zezwól na dostęp.

    ![Prośba o dostęp do mikrofonu](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/microphone-permission-popup.png){class="glboxshadow"}

2. Otwórz Zoom i dołącz do spotkania na komputerze sterowanym. Kliknij strzałkę obok przycisku dźwięku i wybierz następujące urządzenia, jak pokazano w przykładzie:

    - **Microphone**: Microphone (6-Comet Microphone)

    - **Speaker**: EPSON PJ (HD Audio Driver for Display Audio)

    ![Wybór mikrofonu i głośnika](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/select-microphone-and-speaker.png){class="glboxshadow"}

    Następnie wyłącz wyciszenie mikrofonu, aby rozmawiać z innymi uczestnikami. Usłyszysz ich przez głośniki lub słuchawki komputera sterującego.

    Jeśli chcesz również udostępnić uczestnikom obraz z lokalnej kamery, zapoznaj się z [instrukcją przesyłania obrazu z kamery](../faq/use_camera_passthrough_for_remote_meetings.md).

## Rozwiązywanie problemów {#troubleshooting}

??? note "Co zrobić, jeśli inni uczestnicy mnie nie słyszą?"

    Na komputerze sterowanym przejdź do **Settings** -> **System** -> **Sound** i poszukaj w sekcji **Input** wirtualnego mikrofonu KVM, widocznego w tym przykładzie jako **Comet Microphone**. Sprawdź, czy ten mikrofon jest również wybrany w aplikacji do spotkań.

    ![Sprawdzanie wejścia](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-input.png){class="glboxshadow"}

    - Jeśli wirtualny mikrofon KVM się nie pojawia, sprawdź połączenie danych USB między KVM a komputerem sterowanym. Tym połączeniem dźwięk z mikrofonu trafia do komputera sterowanego.

    - Jeśli wirtualny mikrofon KVM jest widoczny i wybrany, ale nie dociera do niego dźwięk, sprawdź, czy mikrofon nie jest wyciszony na komputerze sterującym ani w aplikacji do spotkań na komputerze sterowanym. Sprawdź uprawnienia do mikrofonu w systemie i przeglądarce na komputerze sterującym. Zamknij inne aplikacje lub karty przeglądarki, które mogą korzystać z mikrofonu.

??? note "Co zrobić, jeśli nie słyszę innych uczestników?"

    Na komputerze sterowanym przejdź do **Settings** -> **System** -> **Sound** i poszukaj w sekcji **Output** wyjścia audio HDMI podłączonego do KVM, widocznego w tym przykładzie jako **EPSON PJ**. Sprawdź, czy w aplikacji do spotkań to samo urządzenie jest wybrane jako głośnik.

    ![Sprawdzanie wyjścia](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-output.png){class="glboxshadow"}

    - Jeśli wyjście audio HDMI się nie pojawia, sprawdź połączenie HDMI między komputerem sterowanym a KVM. To połączenie przesyła dźwięk z komputera sterowanego. Jeśli używasz adaptera HDMI, sprawdź, czy obsługuje dźwięk.

    - Jeśli wyjście audio HDMI jest widoczne i wybrane, ale nadal nie słyszysz innych uczestników, sprawdź, czy dźwięk nie jest wyciszony na komputerze sterującym, w karcie przeglądarki ani w głośnikach lub słuchawkach.

    Więcej informacji znajdziesz w artykule [Brak dźwięku z urządzenia sterowanego](../faq/no_audio_from_the_controlled_device.md).

??? note "Co zrobić, jeśli dźwięk znika po odświeżeniu strony lub ponownym połączeniu?"

    Ponownie sprawdź **Speaker** i **Microphone** w konsoli KVM. Zasady bezpieczeństwa przeglądarki mogą wyłączyć odtwarzanie przez głośnik lub wyciszyć mikrofon po odświeżeniu strony lub ponownym połączeniu.

    Więcej informacji znajdziesz w artykule [Dlaczego ustawienia głośnika i mikrofonu nie są zachowywane](../faq/speaker_microphone_settings_cannot_be_retained.md).

??? note "Co zrobić, jeśli pojawia się komunikat „Microphone Access Denied”?"

    Na komputerze sterującym sprawdź następujące ustawienia:

    - **Uprawnienia systemowe**: W Windows 11 przejdź do **Settings** -> **Privacy & security** -> **Microphone**. Włącz **Microphone access**, **Let apps access your microphone** i **Let desktop apps access your microphone**.

    - **Uprawnienia przeglądarki**: Zezwól witrynie KVM na dostęp do mikrofonu. Jeśli wcześniej zablokowano dostęp, zaktualizuj uprawnienia witryny do mikrofonu i odśwież stronę.

    - **Użycie mikrofonu**: Zamknij inne aplikacje lub karty przeglądarki, które mogą korzystać z mikrofonu.

    Po wykonaniu tych czynności ponownie włącz **Microphone** w konsoli KVM.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
