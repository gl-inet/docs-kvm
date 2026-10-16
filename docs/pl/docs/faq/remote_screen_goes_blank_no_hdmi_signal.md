# Co zrobić, jeśli ekran zdalny jest pusty lub brak sygnału HDMI {#what-should-i-do-if-the-remote-screen-goes-blank-or-shows-no-hdmi-signal}

Jeśli podczas dostępu do urządzenia docelowego przez KVM ekran zdalny jest pusty lub pojawia się informacja o braku sygnału HDMI, wykonaj poniższe czynności diagnostyczne.

![Biały ekran](https://static.gl-inet.com/docs/kvm/faq/blank_screen/white_screen.png){class="glboxshadow"}
<small>(Biały ekran)</small>

![Czarny ekran](https://static.gl-inet.com/docs/kvm/faq/blank_screen/black_screen.png){class="glboxshadow"}
<small>(Czarny ekran)</small>

Najpierw sprawdź, czy problem dotyczy transmisji obrazu. Zaloguj się do KVM, przejdź do **Settings** -> **Video** -> **Transfer** i ustaw tryb transmisji na **Direct**.

![Zmiana trybu transmisji](https://static.gl-inet.com/docs/kvm/faq/blank_screen/change_transfer.png){class="glboxshadow" width="360"}

Jeśli problem nadal występuje, sprawdź kolejno poniższe możliwe przyczyny.

## Sprawdź połączenia sprzętowe {#check-hardware-connection}

1. **Uszkodzony przewód HDMI**

    Zużyte przewody HDMI, utlenione złącza lub wewnętrzne uszkodzenia mogą przerywać transmisję sygnału. Wymień przewód na wysokiej jakości przewód HDMI.

    Możesz też sprawdzić stan sygnału HDMI w konsoli KVM. Znajdź ikonę monitora w prawym dolnym rogu i sprawdź, czy wyświetla komunikat „No HDMI signal”.

    ![Brak sygnału HDMI](https://static.gl-inet.com/docs/kvm/faq/blank_screen/no_hdmi_signal.png){class="glboxshadow"}

2. **Nieprawidłowe podłączenie**

    Jeśli urządzeniem docelowym jest komputer stacjonarny, upewnij się, że port **HDMI IN** KVM jest podłączony do portu HDMI OUT karty graficznej lub płyty głównej komputera. Wtyczka musi być całkowicie i stabilnie włożona. Jeśli urządzenie ma wiele wyjść HDMI (np. kartę dedykowaną i wyjście na płycie głównej), wypróbuj inny port.

    Jeśli urządzeniem docelowym jest laptop, upewnij się, że port **HDMI IN** KVM jest podłączony do portu HDMI OUT laptopa.

    Wskazówka: Niektóre modele KVM (takie jak Comet Pro i Comet 5G) mają dwa porty HDMI. Upewnij się, że przewód HDMI z urządzenia docelowego jest podłączony do portu HDMI IN KVM. Po podłączeniu do HDMI OUT konsola KVM nie wykryje sygnału HDMI.

3. **Nieprawidłowe użycie adapterów**

    Jeśli wymagany jest adapter HDMI, użyj adaptera **VGA-to-HDMI**, aby podłączyć urządzenie docelowe do portu HDMI IN GL.iNet KVM.

    Adapter HDMI-to-VGA użyty do tego połączenia nie przekaże prawidłowo sygnału obrazu, przez co ekran pozostanie pusty.

    ![Porównanie adapterów](https://static.gl-inet.com/docs/kvm/faq/blank_screen/adapter_comparison.png){class="glboxshadow"}

## Sprawdź ustawienia przeglądarki {#check-browser-settings}

Jeśli uzyskujesz dostęp do urządzenia docelowego przez przeglądarkę i ekran jest pusty, wypróbuj poniższe metody:

1. **Sprawdź kilka przeglądarek.** Wypróbuj Chrome, Firefox, Edge itp., aby ustalić, czy problem dotyczy konkretnej przeglądarki.

2. **Wyłącz rozszerzenia chroniące przed wyciekami WebRTC lub sterujące WebRTC.** Jeśli w przeglądarce zainstalowano rozszerzenia lub wtyczki mogące wpływać na połączenia WebRTC, wyłącz je i sprawdź ponownie. Możesz też przejść do Settings -> Privacy & Security w przeglądarce i upewnić się, że zezwala ona na połączenia WebRTC.

    ![Ustawienia WebRTC](https://static.gl-inet.com/docs/kvm/faq/blank_screen/webrtc.png){class="glboxshadow"}

## Sprawdź stan i ustawienia urządzenia docelowego {#check-controlled-device-status-and-settings}

1. **Urządzenie jest wyłączone lub uśpione**

    Upewnij się, że urządzenie docelowe jest w pełni uruchomione i nie znajduje się w trybie uśpienia lub hibernacji wskutek ustawień zarządzania energią (w razie potrzeby wybudź je lokalnymi przyciskami).

2. **Nieprawidłowe sterowniki karty graficznej urządzenia docelowego**

    Brak lub uszkodzenie sterowników karty graficznej może powodować brak obrazu. Zaktualizuj lub ponownie zainstaluj sterowniki karty graficznej na urządzeniu docelowym po zalogowaniu lokalnym.

3. **Nieprawidłowe podłączenie do grafiki dedykowanej lub zintegrowanej**

    Jeśli urządzenie docelowe ma grafikę dedykowaną i zintegrowaną, upewnij się, że przewód HDMI jest podłączony do właściwego portu (np. do portu karty dedykowanej, jeśli jest zainstalowana).

4. **Nieprawidłowe ustawienia ekranu urządzenia docelowego (mało prawdopodobne)**

    Po połączeniu z urządzeniem docelowym GL.iNet KVM automatycznie dostosowuje wyjście obrazu, odczytując EDID monitora w celu uzyskania optymalnego działania. Domyślna konfiguracja EDID jest odpowiednia w większości sytuacji i zwykle nie wymaga zmiany.

    Jeśli urządzenie docelowe jest zgodne ze standardowymi monitorami, problemy z pustym ekranem lub wyświetlaniem podczas dostępu przez GLKVM są mało prawdopodobne. Niektóre szczególne problemy ze zgodnością (np. Linux i monitor ASUS) mogą jednak powodować pusty ekran w GLKVM.

    Sprawdź, czy urządzenie docelowe jest zgodne ze standardowymi monitorami i czy nie występują problemy ze zgodnością z konkretnym monitorem.

5. **Problem z rozdzielczością**

    Po podłączeniu GLKVM do niektórych systemów operacyjnych (np. Proxmox VE Hypervisor) dostępna rozdzielczość może zostać nieprawidłowo wynegocjowana, co powoduje problemy z obrazem. Można to rozwiązać, ręcznie zmieniając rozdzielczość na urządzeniu docelowym.

    Poniżej znajduje się przykładowa procedura zmiany rozdzielczości w Proxmox VE Hypervisor.

    1. Otwórz terminal PVE i wpisz poniższe polecenie, aby edytować plik `/etc/default/grub`.

        ```
        nano /etc/default/grub
        ```

    2. Dodaj poniższy wiersz.

        ```
        GRUB_CMDLINE_LINUX_DEFAULT="quiet gfxpayload=text nomodeset"
        ```

    3. Usuń znak `#`, aby odkomentować wiersz `GRUB_GFXMODE`, i ustaw żądaną rozdzielczość, np. `1024x768`.

        ```
        GRUB_GFXMODE=1024x768
        ```

    4. Naciśnij `Ctrl + O`, a następnie Enter, aby zapisać konfigurację.

    5. Naciśnij `Ctrl + X`, aby zamknąć edytor nano.

    6. Wpisz poniższe polecenie, aby zastosować konfigurację.

        ```
        update-grub
        ```

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
