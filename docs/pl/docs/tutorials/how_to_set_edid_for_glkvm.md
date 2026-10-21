# Jak ustawić EDID w GL.iNet KVM {#how-to-set-edid-for-glinet-kvm}

## Czym jest EDID {#what-is-edid}

EDID (Extended Display Identification Data) to standardowy format danych opracowany przez Video Electronics Standards Association (VESA). Jest zapisany w pamięci nieulotnej wyświetlacza i zawiera najważniejsze informacje, takie jak producent, maksymalna rozdzielczość czy częstotliwość odświeżania. Urządzenia, np. komputery, mogą odczytywać EDID, aby automatycznie dostosować parametry sygnału wyjściowego i zapewnić optymalny obraz.

Po podłączeniu do wyświetlacza komputery, laptopy i konsole do gier zwykle automatycznie odczytują EDID, aby ustawić odpowiednie parametry obrazu. Pomaga to uniknąć nieostrego obrazu i migotania oraz uzyskać wyraźny, stabilny obraz.

Ustawienia EDID w GL.iNet KVM służą do automatycznego dopasowania optymalnych parametrów wyświetlania. Po podłączeniu GL.iNet KVM do sterowanego urządzenia odczyt EDID wyświetlacza umożliwia automatyczne dostosowanie wyjścia obrazu w celu uzyskania najlepszej jakości.

## Gotowe ustawienia EDID {#preset-edid}

W konsoli GL.iNet KVM przejdź do **Settings** -> **Video** -> **EDID**. Dostępne są tam gotowe ustawienia EDID.

![Gotowe ustawienia EDID](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_preset.jpg){class="glboxshadow"}

**Domyślne EDID w GL.iNet KVM jest odpowiednie w większości zastosowań i zwykle nie wymaga zmiany**.

W szczególnych sytuacjach, np. przy konfiguracji UEFI/BIOS lub dostosowywaniu rozdzielczości i częstotliwości odświeżania, możesz wybrać gotowe ustawienie, np. 1920×1280/AUO/60HZ.

## Własne EDID {#custom-edid}

Jeśli nie możesz znaleźć odpowiedniego kodu EDID, skorzystaj z [tego repozytorium](https://github.com/linuxhw/EDID){target="blank"} lub poniższych kroków, aby dostosować konfigurację EDID.

!!! Tip "Wskazówka"

    Znalezienie EDID dokładnie odpowiadającego wybranej rozdzielczości i częstotliwości odświeżania może być trudne. Narzędzia do edycji EDID, takie jak **RTDtool** lub **EEditZ**, pozwalają zmienić istniejące EDID zgodnie z potrzebami.

1. Znajdź odpowiednie EDID [tutaj](https://github.com/linuxhw/EDID){target="blank"} i skopiuj je.

2. Zaloguj się do konsoli GL.iNet KVM i przejdź do **Settings** -> **EDID**. Przełącz na tryb **Customize**, wklej parametry do pola i kliknij **Set Custom**, aby zastosować ustawienia.

    ![Własne EDID](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_customize.png){class="glboxshadow"}

!!! Note "Uwaga"

    1. Rozdzielczość nie może przekraczać 2560×1440@60Hz. Na przykład rozdzielczość 2560×1600@60Hz nie jest obsługiwana.
    2. Maksymalna obsługiwana częstotliwość odświeżania wynosi 60Hz. Dla rozdzielczości powyżej 1920x1080 zalecana jest liczba klatek 60FPS lub niższa.
    3. Unikaj rozdzielczości z przeplotem, ponieważ mogą powodować nieprawidłowe wyświetlanie obrazu.
    4. Wprowadzone EDID nie może zawierać więcej niż dwóch bloków danych.
    5. Wymagana jest podstawowa obsługa dźwięku. W przeciwnym razie na sterowanym urządzeniu może nie być możliwości wyboru karty dźwiękowej, co spowoduje brak dźwięku.

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
