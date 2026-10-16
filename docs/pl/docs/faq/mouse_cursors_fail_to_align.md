# Co zrobić, jeśli kursory myszy się nie pokrywają {#what-should-i-do-if-mouse-cursors-fail-to-align}

Jeśli kursor myszy urządzenia sterującego nie pokrywa się z kursorem urządzenia docelowego, wykonaj poniższe czynności.

![Rozbieżne kursory myszy](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/mouse_cursor.png){class="glboxshadow"}

1. **Sprawdź, czy problem występuje podczas ruchu myszy, czy także w spoczynku.**

    <u>Przypadek 1</u>. Jeśli kursory pokrywają się w spoczynku, ale tracą synchronizację podczas ruchu, sprawdź sieć po obu stronach i zapewnij stabilne połączenie.

    Możesz też ukryć kursor lokalny, tak aby na ekranie sterowania widoczny był tylko kursor zdalny. Pozwoli to uniknąć problemu rozbieżnych kursorów.

    W konsoli KVM przejdź do **Settings** -> **Remote Device Settings** -> **Show Local Cursor** i wyłącz tę opcję.

    ![Ukrywanie kursora lokalnego](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/hide_local_cursor.jpg){class="glboxshadow"}

    <u>Przypadek 2</u>. Jeśli kursory nie pokrywają się nawet w spoczynku, ponownie wybierz typ urządzenia w konsoli KVM (tylko dla Comet Q / GL-RMQ1).

    ![Typ urządzenia](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/device_type.png){class="glboxshadow"}

    Jeśli problem nadal występuje, przejdź do następnego kroku.

2. **Jeśli urządzeniem docelowym jest laptop, przyczyną jest prawdopodobnie nieprawidłowa rozdzielczość ekranu.**

    Sprawdź proporcje ekranu laptopa, a następnie zmień rozdzielczość na laptopie docelowym lub ustawienie EDID urządzenia KVM.

    ??? note "Zmiana rozdzielczości na laptopie docelowym"

        **W systemie macOS**:

        1. Przejdź do **Settings** -> **Displays** -> **Optimize for**.

            ![Ustawienia ekranów w macOS](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos1.png){class="glboxshadow" width="582"}

        2. Wybierz **GLKVM**.

            ![Wybór GLKVM](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos2.png){class="glboxshadow" width="582"}

        3. Wybierz odpowiednią rozdzielczość i sprawdź, czy kursory myszy się pokrywają.

            ![Rozdzielczość](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos3.png){class="glboxshadow"}

        **W systemie Windows**:

        1. Przejdź do **Settings** -> **System** -> **Displays**.

            ![Ustawienia ekranu w Windows](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows1.png){class="glboxshadow"}

        2. Przewiń w dół do **Display resolution** i kliknij pole po prawej stronie.

            ![Rozdzielczość ekranu](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows2.png){class="glboxshadow"}

        3. Wybierz odpowiednią rozdzielczość ekranu, a następnie kliknij **Keep changes** w wyświetlonym oknie, aby ją zastosować.

            ![Rozdzielczość ekranu](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows3.png){class="glboxshadow"}

            ![Rozdzielczość ekranu](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows4.png){class="glboxshadow"}

    ??? note "Zmiana ustawienia EDID urządzenia KVM"

        EDID (Extended Display Identification Data) umożliwia automatyczne dobranie optymalnych parametrów wyświetlania. Domyślne EDID jest odpowiednie w większości sytuacji i zwykle nie wymaga zmiany. Szczegóły znajdziesz [tutaj](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}.

        Jeśli po zmianie EDID obraz się nie aktualizuje, spróbuj ponownie uruchomić urządzenie docelowe.

3. **Jeśli urządzenie docelowe nie jest laptopem (np. komputer stacjonarny z monitorem zewnętrznym)**, sprawdź proporcje jego głównego ekranu, a następnie odpowiednio zmień EDID KVM. Szczegóły znajdziesz [tutaj](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
