# Jak przywrócić działanie KVM przez USB OTG {#how-to-unbrick-kvm-via-usb-otg}

Ten poradnik wyjaśnia, jak przywrócić działanie urządzenia GL.iNet KVM przez USB OTG. Metoda jest odpowiednia, gdy KVM jest niesprawny i nie można go odzyskać przez standardową aktualizację firmware ani tryb awaryjny U-Boot.

## Obsługiwane urządzenia {#supported-devices}

- RMQ1

## Wymagania wstępne {#prerequisites}

Przygotuj następujące narzędzia do odzyskiwania urządzenia.

- Komputer z Windows, macOS lub Ubuntu

**Uwaga**

- Nie podłączaj RMQ1 do zasilacza przez port USB-C.

- Przed wgraniem firmware utwórz kopię zapasową partycji `factory`, aby zachować dane właściwe dla urządzenia, np. adres MAC i certyfikat. Jeśli interfejs WWW nadal jest dostępny, przejdź do **Toolbox** → **Terminal** → **Access** i uruchom poniższe polecenie:

    ```
    dd if=/dev/mtd6 of=/userdata/media/factory.bin
    ```

    Plik kopii pojawi się w **Virtual Media** i będzie można pobrać go na komputer lokalny.

- Podczas odzyskiwania nie odłączaj kabla USB-C między RMQ1 a komputerem, ponieważ może to uszkodzić urządzenie.

- Aby urządzenie uruchomiło się automatycznie ponownie po wgraniu firmware, przed rozpoczęciem przejdź do **Settings** → **Options** → **Reboot to Normal Mode After Download** i włącz tę opcję. Jeśli opcja jest wyłączona, po zakończeniu wgrywania musisz uruchomić urządzenie ponownie ręcznie, odłączając i ponownie podłączając kabel zasilania.

## Kroki odzyskiwania {#unbrick-steps}

### Windows {#windows}

1. Pobierz na komputer firmware U-Boot dla RMQ1 [stąd](https://dl.gl-inet.com/kvm/rmq1/stable) (wybierz **DOWNLOAD FOR USB OTG**).

    ![Firmware RMQ1 dla USB OTG](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

2. Zainstaluj sterowniki USB:

    * Pobierz pakiet sterowników [stąd](https://fw.gl-inet.com/tools/ax/Driver_V1.20.46.1.7z) i rozpakuj go do dowolnego katalogu na komputerze.

    * Kliknij dwukrotnie plik `DriverSetup.exe`, aby uruchomić instalator.

        ![Instalacja sterownika — krok 1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-1.png){class="glboxshadow"}

        ![Instalacja sterownika — krok 2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-2.png){class="glboxshadow"}

        ![Instalacja sterownika — krok 3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-3.png){class="glboxshadow"}

3. Zainstaluj narzędzie AXDL.

    * Pobierz AXDL [stąd](https://fw.gl-inet.com/tools/ax/AXDL_V1.24.22.1.7z) i rozpakuj go do łatwo dostępnego katalogu na komputerze.

    * Kliknij dwukrotnie plik `AXDL.exe`, aby uruchomić narzędzie do wgrywania firmware.

        ![Uruchamianie AXDL](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-1.png){class="glboxshadow"}

4. W panelu AXDL kliknij `load.axp` i wybierz firmware pobrany w kroku 1, aby go załadować.

    ![Wybór firmware](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-2.png){class="glboxshadow"}

    Kliknij `Start downloading`.

    ![Rozpoczęcie wgrywania](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-3.png){class="glboxshadow"}

5. Wyłącz KVM. Naciśnij i przytrzymaj przycisk RESET na spodzie RMQ1, a następnie podłącz urządzenie do komputera dołączonym kablem USB-C.

6. Gdy w kolumnie stanu pojawi się `Downloading...`, zwolnij przycisk RESET.

    ![Wgrywanie firmware](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-4.png){class="glboxshadow"}

7. Poczekaj, aż narzędzie AXDL wyświetli `Passed`, co potwierdza zakończenie wgrywania firmware.

    ![Wgrywanie zakończone](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-5.png){class="glboxshadow"}

### macOS / Linux {#macos-linux}

Oficjalne narzędzie AXDL działa wyłącznie w Windows. W macOS i Linux możesz użyć axdl-rs — nieoficjalnego narzędzia open source do wgrywania obrazów Axera, napisanego w Rust.

1. Zainstaluj zestaw narzędzi Rust za pomocą [rustup](https://rustup.rs/).

2. Pobierz na komputer firmware U-Boot dla RMQ1 [stąd](https://dl.gl-inet.com/kvm/rmq1/stable) (wybierz **DOWNLOAD FOR USB OTG**).

    ![Firmware RMQ1 dla USB OTG](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

3. Sklonuj repozytorium źródłowe i przejdź do jego katalogu. Ten krok jest wymagany zarówno w macOS, jak i Linux. Upewnij się, że Git jest zainstalowany, a następnie uruchom:

    ```bash
    git clone https://github.com/gl-inet/axdl-rs.git
    cd axdl-rs
    ```

    Pozostałe polecenia wykonuj w tym katalogu.

4. Zainstaluj zależności odpowiednie dla platformy:

    - **Linux (dystrybucje oparte na Debianie)**

        ```
        sudo apt install -y libudev-dev libusb-1.0-0-dev
        ```

        Skonfiguruj reguły udev, aby zwykli użytkownicy mogli uzyskiwać dostęp do urządzenia:

        ```
        # Skopiuj plik reguł udev do katalogu systemowego
        sudo cp 99-axdl.rules /etc/udev/rules.d/

        # Wczytaj ponownie reguły udev, aby zastosować zmiany
        sudo udevadm control --reload
        ```

        Jeśli użytkownik nie należy do grupy `plugdev`, dodaj go do niej, a następnie wyloguj się i zaloguj ponownie, aby zastosować zmiany.

        ```
        sudo usermod -a -G plugdev $USER
        ```

    - **macOS**

        Zainstaluj `libusb` za pomocą `brew`, aby umożliwić komunikację USB z urządzeniami KVM:

        ```
        brew install libusb
        ```

5. Zbuduj narzędzie `axdl-cli` na wybranej platformie:

    ```bash
    cargo build --bin axdl-cli --package axdl-cli
    ```

6. Wpisz poniższe polecenie, aby wgrać firmware. Zastąp `/path/to/firmware.axp` rzeczywistą ścieżką pobranego pliku firmware.

    ```
    cargo run --bin axdl-cli --package axdl-cli -- --file /path/to/firmware.axp --wait-for-device
    ```

    Narzędzie wyświetli `Waiting for device to be ready` i przejdzie w stan oczekiwania.

7. Wyłącz KVM. Naciśnij i przytrzymaj przycisk RESET na spodzie RMQ1, a następnie podłącz urządzenie do komputera dołączonym kablem USB-C.

8. Poczekaj na zakończenie wgrywania firmware.

    **Uwaga:** Po wgraniu firmware urządzenie może nie uruchomić się automatycznie ponownie. Ręcznie **wyłącz i włącz zasilanie** RMQ1, aby aktywować nowy firmware.

    **Oczekiwany wynik**

    Po pomyślnym wgraniu firmware terminal wyświetli poniższy wynik.

    Uwaga: ostrzeżenia kompilatora można bezpiecznie zignorować.

    ```
    $ cargo run --bin axdl-cli --package axdl-cli -- --file glkvm-RMQ1-nand-1.8.1-0518-1779101289.axp --wait-for-device
    warning: `axdl` (lib) generated 6 warnings
       Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.07s
       Running `target/debug/axdl-cli --file glkvm-RMQ1-nand-1.8.1-0518-1779101289.axp --wait-for-device`
    Waiting for the device to be ready
    Loading the AXP image configuration
    Start download
    Handshaking with the device
    Downloading the flash downloaders
    [00:00:03] [############################################################################]
    Downloading the partition table
    Skipping partition: FACTORY (excluded by default)
    Downloading image DDRINIT
    Downloading image UBOOT
    Downloading image LOGO
    Downloading image DTB
    Downloading image KERNEL
    Downloading image RECOVERY
    Downloading image MEDIA
    Downloading image ROOTFS
    [00:00:26] [############################################################################]
    Downloading image SPL
    Done
    ```

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
