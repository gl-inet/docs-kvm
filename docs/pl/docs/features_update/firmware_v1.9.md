# Firmware v1.9 {#firmware-v19}

Ta wersja wprowadza nowe funkcje, usprawnia interakcję, zwiększa ochronę prywatności i poprawia niezawodność połączeń sieciowych, zapewniając pełniejsze, stabilniejsze i bezpieczniejsze zdalne sterowanie przez KVM.

Pobierz najnowszy firmware z [centrum pobierania firmware](https://dl.gl-inet.com/kvm){target="_blank"}.

## Tryb opóźnienia {#latency-mode}

Ten firmware wprowadza **Latency Mode**, który pozwala wybrać równowagę między szybkością reakcji na polecenia a płynnością obrazu. Możesz ustawić Lowest Latency lub Smooth Display, aby zoptymalizować zdalne sterowanie.

![Tryb opóźnienia](https://static.gl-inet.com/docs/kvm/features_update/1.9/latency_mode.png){class="glboxshadow" width="360"}

- Lowest Latency: Minimalizuje opóźnienie wejścia, zapewniając szybszą reakcję na klawiaturę i mysz.
- Smooth Display: Optymalizuje obraz, aby wyeliminować zacinanie i utratę klatek oraz zapewnić płynne odtwarzanie.

## Wygodniejsza obsługa myszy {#mouse-usability}

Dodano opcję **Primary Button**, która ułatwia obsługę myszy. Możesz ustawić lewy lub prawy przycisk jako główny, zgodnie z własnymi przyzwyczajeniami.

![Główny przycisk myszy](https://static.gl-inet.com/docs/kvm/features_update/1.9/primary_button.png){class="glboxshadow" width="360"}

## Ekran urządzenia {#screen-display}

Na ekranie dotykowym można dostosować ustawienia **Screen Display** urządzenia KVM, w tym blokadę ekranu, tapetę, format czasu (24-godzinny / 12-godzinny) i format daty. Ta funkcja jest dostępna wyłącznie w modelach z ekranem dotykowym.

Ponadto można szybko skonfigurować narzędzia sieci nakładkowych, takie jak Tailscale i NetBird, bezpośrednio na ekranie dotykowym za pomocą kilku dotknięć. W poprzednich wersjach firmware nie było takiej możliwości.

![Ekran urządzenia](https://static.gl-inet.com/docs/kvm/features_update/1.9/screen_display.png){class="glboxshadow" width="360"}

## Język {#language}

Poprzednie wersje firmware obsługiwały tylko chiński i angielski. Ta wersja dodaje natywną obsługę **języka japońskiego**, aby ułatwić korzystanie japońskim użytkownikom.

![Język](https://static.gl-inet.com/docs/kvm/features_update/1.9/language.png){class="glboxshadow" width="360"}

## Rozszerzenia {#extensions}

Ta wersja integruje [NetBird](https://netbird.io/){target="_blank"}, platformę sieciową open source opartą na modelu zero trust, służącą do budowania bezpiecznych prywatnych sieci domowych i firmowych. Rozwiązanie to wykorzystuje WireGuard® i umożliwia bezpieczny zdalny dostęp do KVM z dowolnego miejsca przez wirtualne sieci NetBird. Instrukcję konfiguracji znajdziesz [tutaj](../faq/remote_access_via_netbird.md){target="_blank"}.

![NetBird](https://static.gl-inet.com/docs/kvm/features_update/1.9/netbird.png){class="glboxshadow"}

## Pozostałe ulepszenia {#other-enhancements}

- Program firmware beta: Użytkownicy mogą dołączyć do programu beta, aby testować funkcje przed ich oficjalnym wydaniem.

- Rozpoznawanie tekstu: Narzędzie wykorzystujące optyczne rozpoznawanie znaków (OCR) pozwala przechwytywać tekst z dowolnego zaznaczonego obszaru zdalnego ekranu. Obsługuje język chiński, angielski i tryb dwujęzyczny chińsko-angielski. Szczegóły znajdziesz [tutaj](../tutorials/how_to_capture_text_from_remote_screen.md).

- Strefa czasowa według miasta: Ustaw strefę czasową, wybierając odpowiednie miasto.

- Bezpieczeństwo sesji logowania: Tokeny logowania wygasają teraz po 12 godzinach od zakończenia sesji (wcześniej były bezterminowe).

- Bezpieczeństwo logów systemowych: Wprowadzono maskowanie danych wrażliwych we wszystkich logach systemowych.

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
