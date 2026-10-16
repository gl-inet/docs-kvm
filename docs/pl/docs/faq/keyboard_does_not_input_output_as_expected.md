# Co zrobić, jeśli klawiatura nie wprowadza lub nie wyświetla oczekiwanych znaków {#what-shoud-i-do-if-keyboard-does-not-input-or-output-as-expected}

Jeśli urządzenie sterujące i docelowe korzystają z **różnych metod wprowadzania lub układów klawiatury**, znaki i symbole, takie jak „!”, „@” czy „#”, wpisywane lokalnie mogą być nieprawidłowo wyświetlane po stronie zdalnej.

## Dlaczego tak się dzieje {#why-does-it-happen}

Urządzenie docelowe traktuje KVM jak klawiaturę. Naciśnięcia klawiszy na urządzeniu sterującym są przesyłane do KVM zgodnie z ich pozycjami, a następnie odwzorowywane na urządzeniu docelowym.

Jeśli jednak metoda wprowadzania lub układ klawiatury urządzenia sterującego różni się od ustawień urządzenia docelowego, niektóre symbole lub litery zajmują inne pozycje. W rezultacie urządzenie docelowe wyświetla inne znaki niż wpisane na urządzeniu sterującym.

![Porównanie układów klawiatury US i JIS](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/apple-keyboards-US-JIS.jpg){class="glboxshadow"}

## Rozwiązania {#solutions}

Aby uzyskać spójne odwzorowanie klawiszy, zainstaluj na urządzeniu docelowym metodę wprowadzania lub układ klawiatury dla odpowiedniego języka.

??? "Windows"

    1. Przejdź do **Settings** -> **Time & Language** -> **Language** -> **Preferred Language**. Kliknij **Add a language**.

        ![Dodawanie języka](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/add_language.png){class="glboxshadow"}

    2. Wybierz język do zainstalowania.

        ![Wybór języka](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/choose_language.png){class="glboxshadow"}

??? "MacOS"

    1. Na Macu wybierz **Apple menu** > **System Settings**, a następnie kliknij **Keyboard** na pasku bocznym. Może być konieczne przewinięcie w dół.

    2. Przejdź do **Text Input** i kliknij **Edit**.

    3. Kliknij przycisk **Add** i wyszukaj język. Wybierz co najmniej jedno źródło wprowadzania dla każdego używanego języka, a następnie kliknij **Add**.

    4. Aby rozpocząć pisanie w innym języku, wybierz go w menu wprowadzania na pasku menu.

        Możesz kliknąć **Show Keyboard Viewer** w menu wprowadzania, aby wyświetlić układ klawiatury aktualnie wybranego języka.

        Po dodaniu źródła wprowadzania menu wprowadzania pojawi się automatycznie na pasku menu. Język źródła zostanie automatycznie dodany do listy preferowanych języków w ustawieniach Language & Region oraz do listy języków Dictation (jeśli są dostępne) w ustawieniach Keyboard.

    Materiały: [Pisanie w innym języku na Macu – Wsparcie Apple](https://support.apple.com/guide/mac-help/write-in-another-language-on-mac-mchlp1406/mac){target="_blank"}

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
