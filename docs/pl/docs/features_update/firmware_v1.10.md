# Firmware v1.10

Ta wersja wprowadza natywny WebRTC, monitorowanie danych w czasie rzeczywistym, scentralizowane zarządzanie urządzeniami USB i nowe centrum ustawień. Poprawia również szybkość uruchamiania, bezpieczeństwo i stabilność mikrofonu, zapewniając płynniejsze i bardziej niezawodne zdalne sterowanie przez KVM.

Pobierz najnowszy firmware z [centrum pobierania firmware](https://dl.gl-inet.com/kvm){target="_blank"}.

## Tryb WebRTC (Native)

Ten firmware wprowadza **WebRTC (Native) Mode**. Wykorzystuje bibliotekę Google WebRTC, aby poprawić wydajność strumieniowania i zapewnić płynniejsze zdalne sterowanie w czasie rzeczywistym.

![Tryb WebRTC](https://static.gl-inet.com/docs/kvm/features_update/1.10/webrtc_native_mode.png){class="glboxshadow" width=400}

## Statystyki połączenia

**Connection Stats** wyświetla bieżące informacje o połączeniu i wykresy zmian, w tym opóźnienie sieci, zmienność opóźnienia (jitter), współczynnik utraty pakietów, przepływność, liczbę klatek na sekundę i opóźnienie odtwarzania.

Kliknij ikonę listy, aby wyświetlić bieżące dane połączenia i stan urządzenia.

![Bieżące statystyki połączenia](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_1.png){class="glboxshadow"}

Kliknij ikonę wykresu, aby wyświetlić wykresy zmian opóźnienia sieci, jittera i współczynnika utraty pakietów.

![Wykresy statystyk połączenia](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_2.png){class="glboxshadow"}

## Centrum ustawień

Ta wersja dodaje nowe **Settings Center**, które gromadzi ustawienia urządzeń USB, preferencji, sieci, bezpieczeństwa, chmury i systemu. Istniejące opcje, takie jak konfiguracja nazwy hosta, zarządzanie chmurą i aktualizacje firmware, są teraz łatwiej dostępne w jednym miejscu.

### Urządzenia USB

**USB Devices** umożliwia scentralizowane zarządzanie emulowanymi urządzeniami USB. Na tej stronie można włączać i wyłączać wirtualne urządzenia peryferyjne, aby poprawić zgodność ze sterowanym hostem.

![Urządzenia USB](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_usb_devices.png){class="glboxshadow"}

- **USB Emulated Devices**: Włączaj i wyłączaj emulowane urządzenia USB, w tym mysz, klawiaturę, mikrofon, kamerę i nośniki wirtualne. Niektórych urządzeń nie można włączyć jednocześnie. Dostępność opcji jest aktualizowana automatycznie.

- **Device Identity**: Dostosuj lub zmień tożsamość KVM rozpoznawaną przez sterowane urządzenie. EDID i identyfikacja urządzenia pozostają zsynchronizowane. Zmiana jednej opcji automatycznie aktualizuje drugą, aby zapewnić poprawne rozpoznawanie urządzenia.

### Preferencje

**Preferences** pozwala zarządzać preferencjami układu, ustawieniami systemowymi i ustawieniami ekranu urządzenia.

![Preferencje](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences**: Skonfiguruj pasek narzędzi w trybie pełnoekranowym i pasek stanu w trybie okienkowym.

- **System Settings**: Ustaw tytuł karty przeglądarki, język interfejsu, tryb kolorów i strefę czasową.

- **Device Screen**: Wyświetl podgląd i skonfiguruj wbudowany ekran urządzenia, w tym tryb ekranu blokady, format czasu, format daty i tapetę.

    **Uwaga**: Ta funkcja jest dostępna tylko w modelach z wbudowanym wyświetlaczem.

### Sieć

Możesz przeglądać ustawienia sieciowe urządzenia i zarządzać nimi, w tym nazwą hosta, połączeniem Ethernet i informacjami o sieci bezprzewodowej.

![Sieć](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_network.png){class="glboxshadow"}

- **Hostname**: Zmień nazwę hosta urządzenia bezpośrednio w konsoli. Ta funkcja jest dostępna od wersji firmware v1.7.0.

- **Ethernet Settings**: Przeglądaj i konfiguruj połączenie Ethernet. Użyj DHCP, aby uzyskać ustawienia automatycznie, lub wybierz **Static**, aby ręcznie wpisać adres IP, maskę sieci, bramę i inne wymagane parametry.

- **Wireless**: Po dołączeniu urządzenia do sieci Wi-Fi wyświetlane są adres IP, brama i adres MAC.

    **Uwaga**: Funkcja Wireless jest dostępna tylko w obsługiwanych modelach.

### Bezpieczeństwo

**Security** pozwala zmienić hasło administratora, włączyć uwierzytelnianie dwuskładnikowe i dostosować certyfikat TLS.

![Bezpieczeństwo](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_security.png){class="glboxshadow"}

- **Access Password**: Zarządzaj hasłem administratora lub włącz uwierzytelnianie dwuskładnikowe (2FA), aby zabezpieczyć dostęp do urządzenia.

- **TLS Certificate**: Użyj domyślnego certyfikatu lub prześlij własny certyfikat i klucz prywatny do dostępu przez przeglądarkę.

### Chmura

Urządzenia można powiązać z usługami chmurowymi za pomocą adresu URL lub kodu, aby uzyskać zdalny dostęp i zarządzać nimi. Możesz też pobrać aplikację mobilną, zarządzać połączeniem lub odłączyć urządzenie od konta w razie potrzeby.

![Chmura](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_cloud.png){class="glboxshadow"}

### System

W **System** znajdziesz opcje zarządzania systemem, aktualizacji firmware i pomocy technicznej.

![System](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_system.png){class="glboxshadow"}

- **System**: Uruchom urządzenie ponownie lub przywróć ustawienia fabryczne.

- **Upgrade**: Włącz Beta Center, aby otrzymywać aktualizacje firmware w wersji beta, lub użyj **Local Upgrade**, aby zainstalować firmware z pliku lokalnego.

- **Help & Support**: Wyeksportuj logi urządzenia na potrzeby rozwiązywania problemów i uzyskaj dostęp do instrukcji obsługi, najczęstszych pytań i innych dokumentów pomocy.

## Pozostałe ulepszenia

- **Szybkość uruchamiania**: Skrócono czas uruchamiania urządzenia.

- **Zasady haseł**: Zaostrzono wymagania dotyczące hasła (minimum 10 znaków z co najmniej dwóch kategorii znaków), aby zwiększyć bezpieczeństwo.

- **Wskaźnik Caps Lock**: Dodano wskaźnik stanu Caps Lock na sterowanym urządzeniu.

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
