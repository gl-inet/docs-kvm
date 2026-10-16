# Co zrobić, jeśli nie mogę sterować myszą i klawiaturą {#what-should-i-do-if-i-cannot-control-the-mouse-and-keyboard}

Jeśli mimo prawidłowego podłączenia wszystkich przewodów nie możesz sterować myszą i klawiaturą urządzenia docelowego przez KVM, wykonaj poniższe czynności.

1. Sprawdź połączenia.

    Jako przykład posłuży Comet (GL-RM1). Ma on dwa porty USB Type-C:

    - Port z boku jest oznaczony „5V 2A” i służy do zasilania (podłączenia zasilacza).
    - Drugi port, z tyłu, jest oznaczony symbolami myszy i klawiatury. Łączy się go z portem USB urządzenia docelowego, aby przesyłać sygnały klawiatury i myszy.

    Jeśli zamienisz te połączenia, urządzenie KVM nie uruchomi się, a mysz i klawiatura nie będą reagować.

    Sprawdź, czy oba porty Type-C są prawidłowo podłączone.

    ![Porty GL-RM1](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/gl-rm1-ports.png){class="glboxshadow gl-80-desktop"}

2. Sprawdź przewód USB.

    Użyj dołączonego przewodu USB. Upewnij się, że łączy port USB urządzenia docelowego z portem USB KVM i obsługuje transmisję danych.

    Tylko przewody obsługujące transmisję danych umożliwiają sterowanie myszą i klawiaturą urządzenia zdalnego.

    Podłącz ponownie przewód USB i uruchom ponownie urządzenie docelowe.

3. Zmień tryb myszy na Relative.

    Zaloguj się do KVM, przejdź do Settings -> Mouse Mode, wybierz Relative i sprawdź, czy problem ustąpił.

    ![Tryb myszy](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/mouse_mode.jpg){class="glboxshadow"}

4. Wyłącz Virtual Media.

    Zaloguj się do KVM, przejdź do Virtual Media, kliknij ikonę trzech kropek i wyłącz tę funkcję.

    ![Wyłączanie nośników wirtualnych](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/disable_virtual_media.png){class="glboxshadow" width="422"}

    Gdy funkcja nośników wirtualnych jest włączona, KVM może symulować pamięć USB podłączoną do urządzenia docelowego. Niektóre urządzenia wyłączają jednak wszystkie wejścia USB po wykryciu nieznanej pamięci USB, przez co mysz i klawiatura przestają reagować.

5. Zmień tożsamość urządzenia.

    Zaloguj się do KVM, przejdź do Settings -> System -> Device Identity i zmień tożsamość, pod jaką urządzenie docelowe rozpoznaje KVM.

    ![Zmiana tożsamości urządzenia](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/change_device_identity.png){class="glboxshadow"}

6. Zaktualizuj oprogramowanie sprzętowe KVM do najnowszej wersji. [Centrum pobierania oprogramowania KVM](https://dl.gl-inet.com/kvm){target="_blank"}

7. Sprawdź w Menedżerze urządzeń komputera docelowego, czy któryś ze sterowników nie działa nieprawidłowo.

8. Sprawdź, czy oprogramowanie zabezpieczające nie blokuje urządzenia docelowego.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
