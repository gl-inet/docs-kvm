# Jak przywrócić działanie KVM za pomocą RKDevTool

Ten poradnik pokazuje, jak przywrócić działanie GL.iNet KVM za pomocą RKDevTool. Dotyczy sytuacji, gdy KVM jest niesprawny i nie można go odzyskać przez zwykłą aktualizację firmware ani tryb awaryjny U-Boot.

## Przygotowanie

Przygotuj następujące narzędzia do odzyskiwania urządzenia.

- Komputer z systemem Windows
- Kabel USB do transmisji danych
- Zasilacz do urządzenia KVM

!!! Note "Uwaga"

    Podczas odzyskiwania NIE odłączaj kabla USB ani nie wyłączaj zasilania KVM, ponieważ może to uszkodzić urządzenie.

    Przed rozpoczęciem zalecamy utworzenie kopii zapasowej ważnych danych.

## Kroki odzyskiwania

Aby uniknąć niepowodzenia, wykonaj kroki w podanej kolejności.

1. Wyłącz urządzenie KVM.

2. Pobierz na komputer najnowszy firmware swojego urządzenia KVM [stąd](https://dl.gl-inet.com/kvm){target="_blank"}.

3. Pobierz pakiet sterowników [stąd](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/DriverAssitant_v5.11.zip) i rozpakuj go do dowolnego katalogu na komputerze.

4. Kliknij dwukrotnie plik .exe i zainstaluj sterownik.

    ![Instalacja sterownika — krok 1](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_1.png){class="glboxshadow"}

    ![Instalacja sterownika — krok 2](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_2.png){class="glboxshadow"}

5. Pobierz **RKDevTool** [stąd](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/RKDevTool_Release_v3.37.zip) i rozpakuj go do łatwo dostępnego katalogu na komputerze.

6. Kliknij dwukrotnie plik .exe, aby uruchomić narzędzie do wgrywania firmware.

    ![Uruchamianie RKDevTool — krok 1](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_1.png){class="glboxshadow"}

    ![Uruchamianie RKDevTool — krok 2](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_2.png){class="glboxshadow"}

7. Połącz port Type-C OTG urządzenia KVM z portem USB komputera za pomocą kabla USB do transmisji danych.

    Poniżej pokazano port Type-C OTG na przykładzie Comet (GL-RM1).

    ![Podłączanie kabla USB](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/otg-port-rm1.png){class="glboxshadow gl-60-desktop"}

8. Przytrzymaj przycisk RESET przez **10 sekund**, jednocześnie podłączając kabel zasilania do KVM. Następnie zwolnij przycisk. KVM przejdzie do trybu Loader.

    ![Przycisk resetowania](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/reset_button_rm1.jpg){class="glboxshadow" width="433"}

9. W panelu RKDevTool przejdź do **Upgrade Firmware** -> **Firmware** i wybierz firmware pobrany w kroku 2, aby go załadować.

    ![Wybór firmware](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/select_firmware.png){class="glboxshadow"}

    Następnie wybierz **Upgrade** obok Firmware. Pojawi się komunikat „Found Loader Device” i rozpocznie się wgrywanie firmware.

    ![Panel RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/rkdevtool_panel.jpg){class="glboxshadow"}

    Po zakończeniu aktualizacji KVM uruchomi się automatycznie ponownie.

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
