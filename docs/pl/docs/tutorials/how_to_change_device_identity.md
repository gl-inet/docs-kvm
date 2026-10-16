# Jak zmienić tożsamość urządzenia KVM

## Czym jest tożsamość urządzenia KVM

Tożsamość urządzenia GL.iNet KVM to identyfikator, dzięki któremu podłączone urządzenie może rozpoznać KVM i odróżnić go od innych urządzeń podczas komunikacji.

KVM jest zwykle wyposażony w port Type-C, pokazany poniżej, który łączy się z portem USB sterowanego urządzenia w celu emulowania urządzeń peryferyjnych (np. klawiatury, myszy, dysku USB i mikrofonu) oraz napędu CD-ROM.

![Port Type-C GL-RM1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

Gdy klikniesz myszą, wpiszesz tekst na klawiaturze lub użyjesz mikrofonu po stronie sterującej, sygnały te są zdalnie przesyłane do fizycznego urządzenia KVM. Następnie KVM przekazuje je do sterowanego urządzenia przez port Type-C.

KVM jest więc zwykle traktowany jako urządzenie złożone, emulujące kilka urządzeń peryferyjnych podłączonych do portów USB sterowanego urządzenia.

![Zasada działania tożsamości urządzenia](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/principle.png){class="glboxshadow"}

!!! Note "Uwaga"

    Jeśli metoda wprowadzania tekstu lub układ klawiatury na urządzeniu sterującym różnią się od tych na urządzeniu sterowanym, niektóre symbole lub litery mogą znajdować się w innych miejscach klawiatury. W efekcie znaki na sterowanym urządzeniu mogą różnić się od wpisanych. Szczegóły znajdziesz [tutaj](../faq/keyboard_does_not_input_output_as_expected.md).

## Dlaczego warto zmienić tożsamość urządzenia

Ponieważ GL.iNet KVM emuluje kilka urządzeń służących do interakcji z użytkownikiem, sterowane urządzenie rozpoznaje go jako zestaw wielu urządzeń: monitor, urządzenia USB, takie jak mysz i klawiatura, oraz dysk USB.

Domyślna tożsamość to **GLKVM**, dlatego w ustawieniach systemowych sterowanego urządzenia KVM jest wyświetlany jako GLKVM lub Glinet Composite Device. Zwykle nie stanowi to problemu, ponieważ ustawienia te są widoczne tylko dla samych użytkowników.

![Domyślna tożsamość urządzenia](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}
<small>(Ustawienia Bluetooth i urządzeń)</small>

![Ustawienia głośnika](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(Ustawienia głośnika)</small>

Zmiana tożsamości urządzenia KVM może być jednak potrzebna w poniższych sytuacjach.

??? "Sytuacja 1: Unikanie alertów oprogramowania monitorującego na komputerze służbowym"

    Jeśli sterowane urządzenie jest komputerem służbowym, może zawierać wbudowane lub zainstalowane oprogramowanie monitorujące. Narzędzia te mogą uznać zdalny dostęp przez KVM za nietypową aktywność, wywołać alerty, a nawet zgłosić ją do systemów IT.

    Zmiana tożsamości KVM może pomóc uniknąć takich zbędnych powiadomień przy zachowaniu normalnego działania zdalnego sterowania.

??? "Sytuacja 2: Ukrywanie użycia KVM podczas udostępniania ekranu na spotkaniu online"

    Podczas spotkań online wymagających udostępniania ekranu ustawienia systemowe sterowanego urządzenia (np. Bluetooth i urządzenia) mogą wyświetlać domyślną tożsamość KVM. Może to ujawnić uczestnikom korzystanie ze zdalnego dostępu przez KVM, czego niektórzy użytkownicy wolą uniknąć.

    Zmiana tożsamości urządzenia pozwala ukryć jego domyślną nazwę na udostępnianym ekranie.

    ![Udostępnianie ekranu](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/screen_sharing.png){class="glboxshadow"}
    <small>(Udostępnianie ekranu)</small>

??? "Sytuacja 3: Rozwiązywanie problemów z brakiem reakcji myszy lub klawiatury na sterowanym urządzeniu"

    Jeśli nie możesz sterować myszą i klawiaturą przez KVM, spróbuj zmienić jego tożsamość, aby uniknąć problemów ze zgodnością i umożliwić poprawne przesyłanie sygnałów między KVM a sterowanym urządzeniem.

## Ograniczenia dostosowywania tożsamości urządzenia

!!! Warning "Oprogramowanie analizujące zachowanie nadal może rozpoznać KVM"

    Niezależnie od zmian tożsamości urządzenia USB, **struktura** wirtualizowanych urządzeń (klawiatury, myszy, mikrofonu, kamery itd.) nadal może wydawać się podejrzana oprogramowaniu analizującemu zachowanie.

    Podstawowy problem polega na tym, że wszystkie te wirtualizowane urządzenia peryferyjne należą do **jednego złożonego urządzenia USB**. Urządzenie złożone obejmujące samą klawiaturę i mysz jest dość powszechne — podobną strukturę ma wiele bezprzewodowych odbiorników klawiatur i myszy, np. Logitech Unifying. Jednak pojedyncze złożone urządzenie USB obejmujące jednocześnie **klawiaturę, mysz i mikrofon** jest w praktyce niezwykle rzadkie.

    Dlatego sama zmiana tożsamości urządzenia **może nie wystarczyć**, aby uniknąć wykrycia przez zaawansowane oprogramowanie monitorujące lub analizujące zachowanie.

## Jak zmienić tożsamość urządzenia

### Firmware v1.10 i nowszy

1. Zaloguj się do KVM i przejdź do **Settings** w prawym górnym rogu. W sekcji **USB Devices** znajdź **Device Identity** i dostosuj tę opcję.

    ![Dostosowywanie tożsamości — krok 1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize1.png){class="glboxshadow"}

2. W wyskakującym oknie kliknij **Confirm**, aby uruchomić urządzenie ponownie.

    ![Potwierdzenie ponownego uruchomienia](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize2.png){class="glboxshadow"}

3. Po ponownym uruchomieniu nowa tożsamość będzie widoczna w konsoli KVM.

    ![Zmieniona tożsamość](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize3.png){class="glboxshadow"}

4. Sprawdź tożsamość urządzenia. Poniższy przykład przedstawia weryfikację na sterowanym urządzeniu z Windows 11 Pro.

    Na sterowanym urządzeniu przejdź do **Settings** -> **Bluetooth & devices**. Urządzenia wejściowe i dźwiękowe powinny być rozpoznawane zgodnie z wprowadzonymi ustawieniami.

    ![Weryfikacja tożsamości](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize4.png){class="glboxshadow"}

### Firmware v1.9 i starszy

1. Zaloguj się do KVM i przejdź do **Settings** -> **System** -> **Device Identity**. Wybierz gotową tożsamość z listy rozwijanej.

    ![Wybór tożsamości](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    Możesz też kliknąć **Customize** i wpisać wybrane parametry w wyskakującym oknie.

    ![Własna tożsamość](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. W wyskakującym oknie kliknij **Confirm**, aby uruchomić urządzenie ponownie.

    ![Ponowne uruchamianie](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. Po ponownym uruchomieniu nowa tożsamość będzie widoczna w konsoli KVM.

    ![Zmieniona tożsamość w konsoli](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

4. Sprawdź tożsamość urządzenia. Poniższy przykład przedstawia weryfikację na sterowanym urządzeniu z Windows 10 Pro.

    Na sterowanym urządzeniu przejdź do **Settings** -> **Bluetooth & devices**. Urządzenia wejściowe i dźwiękowe powinny być rozpoznawane zgodnie z wprowadzonymi ustawieniami.

    ![Weryfikacja tożsamości](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
