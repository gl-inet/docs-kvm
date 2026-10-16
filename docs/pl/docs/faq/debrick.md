# Przywracanie działania KVM za pomocą U-Boot {#using-u-boot-to-unbrick-your-kvm}

Jeśli KVM przestał działać wskutek własnych modyfikacji lub wgrania nieprawidłowego oprogramowania sprzętowego, może nie uruchamiać się prawidłowo. W takim przypadku możesz ponownie zainstalować oprogramowanie sprzętowe w trybie awaryjnym U-Boot.

## Przygotowanie {#preparation}

Przygotuj komputer stacjonarny lub laptop z portem Ethernet. Jeśli komputer nie ma portu Ethernet, potrzebny będzie dodatkowy adapter USB–Ethernet.

## Procedura przywracania działania {#unbrick-steps}

Aby przywracanie się powiodło, ściśle przestrzegaj poniższych kroków.

1. Pobierz na komputer oprogramowanie sprzętowe dostępne [tutaj](https://dl.gl-inet.com/kvm){target="_blank"}.

2. Odłącz zasilanie KVM. Połącz komputer z portem Ethernet urządzenia KVM.

3. Naciśnij i przytrzymaj przycisk Reset, **jednocześnie włączając zasilanie KVM**.

    Poczekaj, aż dioda LED kilka razy zamiga w regularnej sekwencji. Zwolnij przycisk Reset **dopiero po** zmianie sposobu migania.

    !!! note "Sposób migania diody LED zależnie od modelu"

        - **Comet (GL-RM1)**: Gdy przytrzymujesz przycisk Reset, niebieska dioda LED mignie 5 razy. Po 5 mignięciach zwolnij przycisk Reset; niebieska dioda zacznie świecić światłem ciągłym.

        - **Comet PoE (GL-RM1PE)**: Gdy przytrzymujesz przycisk Reset, niebieska dioda LED mignie 5 razy. Po 5 mignięciach zwolnij przycisk Reset; niebieska dioda zacznie świecić światłem ciągłym.

        - **Comet Pro (GL-RM10)**: Przytrzymaj przycisk Reset przez około 5 sekund, jednocześnie włączając zasilanie KVM, a następnie zwolnij przycisk. Urządzenie przejdzie do trybu U-Boot.

        - **Comet 5G (GL-RM10RC)**: Przytrzymaj przycisk Reset przez około 5 sekund, jednocześnie włączając zasilanie KVM, a następnie zwolnij przycisk. Urządzenie przejdzie do trybu U-Boot.

4. Ręcznie ustaw adres IP komputera na **192.168.1.2**. Poniżej znajdują się instrukcje dla poszczególnych systemów operacyjnych.

    ??? "Windows 7 / Windows 10"

        1. Przejdź do **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Kliknij prawym przyciskiem myszy **Local Area Connection** -> **Properties**.

        3. Kliknij **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Ręcznie ustaw **IP address** na `192.168.1.2`.

        5. Ustaw **Subnet mask** na `255.255.255.0`.

            ![Właściwości IPv4](https://static.gl-inet.com/docs/kvm/faq/debrick/win7_set_ip.jpg){class="glboxshadow"}

        6. Kliknij przycisk **OK**.

    ??? "Windows 11"

        1. Otwórz Settings.

        2. Kliknij **Network & Internet**.

        3. Kliknij kartę **Ethernet**.

            ![Ustawienia Ethernet w Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet.png){class="glboxshadow"}

        4. W sekcji „IP assignment” kliknij przycisk **Edit**.

            ![Edycja ustawień IP Ethernet w Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit1.png){class="glboxshadow"}

        5. Wybierz opcję **Manual**.

            ![Edycja ustawień IP Ethernet w Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit2.png){class="glboxshadow"}

        6. Włącz przełącznik **IPv4**.

        7. Ustaw statyczny **IP address** na **192.168.1.2**.

            ![Edycja ustawień IP Ethernet w Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit3.png){class="glboxshadow"}

        8. Ustaw **Subnet mask** na **255.255.255.0**.

        9. Kliknij przycisk **Save**.

    ??? "macOS"

        1. Kliknij ikonę **Apple** w lewym górnym rogu ekranu i wybierz **System Preferences**.

            ![Preferencje systemowe macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences.png){class="glboxshadow"}

        2. Kliknij **Network**.

            ![Ustawienia sieci w macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences_network.png){class="glboxshadow"}

        3. Kliknij **Ethernet** po lewej stronie, następnie rozwiń listę obok **Configure IPv4** i wybierz **Manually**. Jeśli korzystasz z adaptera USB–Ethernet, pozycja Ethernet może być wyświetlana pod nazwą adaptera.

            ![Ręczne ustawianie adresu IP w macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_1.png){class="glboxshadow"}

        4. Ustaw **IPv4 Address** na `192.168.1.2`, **Subnet Mask** na `255.255.255.0`, a **Router** na `192.168.1.1`, następnie kliknij przycisk Apply w prawym dolnym rogu.

            ![Ręczne ustawianie adresu IP w macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_2.png){class="glboxshadow"}

5. Otwórz w przeglądarce **http://192.168.1.1**. Jest to interfejs WWW U-Boot.

    ![Interfejs WWW U-Boot](https://static.gl-inet.com/docs/kvm/faq/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    **Uwaga:** Powyższy interfejs WWW U-Boot może różnić się od wyświetlanego na Twoim urządzeniu, ponieważ wersja U-Boot zależy od daty produkcji. Ze względów bezpieczeństwa nie udostępniamy obecnie osobnych aktualizacji U-Boot. Jeśli aktualizacja okaże się konieczna, zostanie dołączona do nowego oprogramowania sprzętowego.

6. Kliknij **Choose file** i wybierz plik oprogramowania sprzętowego. Następnie kliknij przycisk **Update firmware**.

7. Poczekaj około 3 minut. **NIE wyłączaj zasilania KVM podczas aktualizacji.**

    KVM jest gotowy, gdy dioda LED **miga na biało**.

8. Przywróć poprzednie ustawienia IP komputera zmienione w kroku 4.

9. Odłącz przewód Ethernet łączący komputer z KVM, a następnie podłącz KVM do sieci (np. routera lub przełącznika sieciowego) za pomocą tego przewodu Ethernet albo przez Wi-Fi.

    Poczekaj około 1 minuty, aż KVM uzyska dostęp do Internetu. Po tym czasie dostęp do KVM powinien być ponownie możliwy.

    **Uwaga:** Ustawienia konfiguracji są zwykle zachowywane. Zostaną jednak przywrócone do wartości domyślnych, jeśli przyczyną awarii systemu wymagającej przywracania był błąd konfiguracji.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
