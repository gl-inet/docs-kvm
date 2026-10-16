# Nie można nawiązać połączenia zdalnego przez aplikację GLKVM {#connection-failed-when-remote-access-via-glkvm-app}

Podczas dostępu zdalnego przez aplikację GLKVM urządzenie KVM może mieć status Online, ale po jego kliknięciu połączenie zatrzymuje się na komunikacie „Connecting”.

![Urządzenie online](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/device_online.png){class="glboxshadow"}

![Nawiązywanie połączenia](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connecting.png){class="glboxshadow"}

Rozwiązywanie problemów:

1. Zapewnij stabilne połączenie sieciowe.

    Upewnij się, że KVM ma stabilne połączenie z Internetem. Ciągłe białe światło diody LED oznacza prawidłowe połączenie sieciowe.

2. Sprawdź reguły zapory sieciowej.

    Tymczasowo wyłącz lokalną zaporę lub dodaj domeny związane z GL.iNet (np. glkvm.com) do listy dozwolonych. Po wprowadzeniu zmian spróbuj połączyć się ponownie.

    Poniżej przedstawiono przykładową procedurę zmiany reguł zapory w sieci Sky.

    ??? note "Sieć Sky (np. Sky Max Hub)"

        Mechanizmy zabezpieczeń sieci Sky mogą uznać domenę `glkvm.com` za podejrzaną i zablokować dostęp. Ograniczenia można usunąć w aplikacji Sky.<br>

        1. Otwórz aplikację MySky, przejdź do **Broadband** -> **Advanced Security** i sprawdź, czy domeny związane z GL.iNet są zablokowane.

            ![Ustawienia zabezpieczeń MySky](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-1.png){class="glboxshadow"}

        2. Jeśli domena jest zablokowana, kliknij strzałkę w dół, aby wyświetlić szczegóły, a następnie wybierz **Allow Access**, aby usunąć blokadę.

            ![Odblokowanie dostępu w MySky](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-2.png){class="glboxshadow" width="300"}

3. Wyłącz VPN lub serwer proxy na urządzeniu sterującym.

    Upewnij się, że na urządzeniu z aplikacją GLKVM nie są włączone usługi VPN ani proxy, ponieważ mogą zakłócać połączenie.

4. Jeśli to możliwe, uruchom ponownie KVM.

    Jeśli to możliwe, wykonaj sprzętowy restart urządzenia KVM, aby usunąć przejściowe problemy sieciowe lub programowe.

    Jeśli nie jesteś w pobliżu urządzenia KVM, możesz uruchomić je ponownie zdalnie przez aplikację GLKVM:

    1. Na liście urządzeń kliknij **Manage** w prawym górnym rogu kafelka urządzenia.

        ![Ponowne uruchamianie w aplikacji — krok 1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_1.png){class="glboxshadow"}

    2. Kliknij **More** i wybierz **Reboot**.

        ![Ponowne uruchamianie w aplikacji — krok 2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_2.png){class="glboxshadow"}

Dodatkowe uwagi techniczne:

1. Upewnij się, że rozwiązywanie nazw DNS dla tych domen działa prawidłowo.

2. Sprawdź, czy ruch wychodzący na standardowych portach KVM i dostępu zdalnego nie jest blokowany.

3. W sieciach firmowych skonsultuj się z administratorem IT w sprawie możliwych zasad filtrowania ruchu.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
