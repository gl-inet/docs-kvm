# Jak sprawdzić, czy port USB-C urządzenia obsługuje DP Alt Mode {#how-to-check-if-your-devices-usb-c-port-supports-dp-alt-mode}

## Czym jest DP Alt Mode {#what-is-dp-alt-mode}

DP Alt Mode (DisplayPort Alternate Mode) to funkcja dostępna w niektórych portach USB-C, która pozwala przesyłać wysokiej jakości sygnał wideo oprócz danych i zasilania.

Umożliwia przesyłanie obrazu jednym kablem USB-C z telefonu, tabletu lub laptopa bezpośrednio do monitora, telewizora lub projektora, bez specjalnego adaptera ani stacji dokującej. Bez DP Alt Mode port może tylko przesyłać dane i dostarczać zasilanie; nie może wysyłać obrazu do zewnętrznego wyświetlacza.

## Dlaczego to ważne {#why-it-matters}

DP Alt Mode ma znaczenie dla **Comet Q**, ponieważ urządzenie wykorzystuje ten tryb do odbierania obrazu. Sterowane urządzenie musi obsługiwać natywne wyjście wideo przez port USB-C. Adapter DisplayLink może nie zapewnić tej funkcji przy bezpośrednim połączeniu z Comet Q.

Nie wszystkie porty USB-C mają te same możliwości. Niektóre przesyłają tylko dane i zasilanie, inne również obraz. Kształt złącza jest taki sam, ale jego funkcje mogą się różnić. Dwa identycznie wyglądające porty USB-C mogą działać zupełnie inaczej, dlatego warto sprawdzić ich możliwości przed zakupem akcesoriów do wyświetlania obrazu przez USB-C.

## Ogólne sposoby sprawdzania obsługi DP Alt Mode {#general-methods-to-verify-dp-alt-mode}

1. **Sprawdź specyfikację**.

    Znajdź dokładny model na stronie producenta. Szukaj określeń takich jak DisplayPort, DP Alt Mode, wyjście wideo lub Thunderbolt.

2. **Sprawdź oznaczenia portu**.

    Logo DisplayPort w kształcie litery D lub ikona błyskawicy Thunderbolt obok portu USB-C wskazują na możliwość wyprowadzania obrazu.

3. **Sprawdź ustawienia systemowe**.

    Ustawienia systemowe mogą pomóc zidentyfikować podłączony wyświetlacz, ale nie zawsze pozwalają stwierdzić, czy dany port USB-C obsługuje natywny DP Alt Mode. Połącz tę metodę ze sprawdzeniem specyfikacji producenta i testem bezpośredniego połączenia. Poniżej znajdziesz instrukcje dla poszczególnych platform.

    - [Jak sprawdzić w Windows](#how-to-check-on-windows)
    - [Jak sprawdzić na Macu](#how-to-check-on-mac)
    - [Jak sprawdzić w Androidzie](#how-to-check-on-android)
    - [Jak sprawdzić na iPhonie i iPadzie](#how-to-check-on-iphone-and-ipad)
    - [Konsole przenośne, tablety i inne urządzenia](#handhelds-tablets-and-other-devices)

4. **Wykonaj szybki test**.

    Podłącz urządzenie do monitora lub telewizora za pomocą kabla lub adaptera USB-C do HDMI / DisplayPort, który wyraźnie wymaga DP Alt Mode. Jeśli obraz zostanie zduplikowany lub pulpit rozszerzony, natywne wyjście wideo działa na tym porcie. Nie używaj adaptera DisplayLink do tego testu.

---

## Jak sprawdzić w Windows {#how-to-check-on-windows}

1. Naciśnij `Win + X` i otwórz **Device Manager**.
2. Poszukaj wpisów zawierających *„USB4”* lub *„Thunderbolt”*. Pomagają one zidentyfikować sprzęt, ale sam Device Manager nie potwierdza obsługi DP Alt Mode na konkretnym porcie.
3. Sprawdź instrukcję laptopa lub stronę produktu u producenta, dotyczącą dokładnie tego portu. Szukaj *„DisplayPort over USB-C”* lub *„DP Alt Mode”*.
4. Podłącz Comet Q bezpośrednio albo podłącz wyświetlacz przez adapter wyraźnie wymagający DP Alt Mode. Otwórz **Settings** > **System** > **Display** > **Multiple displays**, aby sprawdzić, czy wyświetlacz został wykryty.

**Uwaga**:

1. **DisplayLink nie potwierdza obsługi DP Alt Mode.** DisplayLink przesyła obraz jako dane USB i może działać także przez USB-A. Wpis DisplayLink w Device Manager ani działający wyświetlacz podłączony przez stację dokującą DisplayLink nie potwierdzają natywnego wyjścia wideo USB-C. Zobacz [Synaptics: USB-C z DisplayLink](https://www.synaptics.com/products/displaylink-graphics/usb-c){target="_blank"}.

2. Jeśli laptop ma kilka portów USB-C, tylko niektóre mogą obsługiwać wyjście wideo. Sprawdź każdy port osobno.

## Jak sprawdzić na Macu {#how-to-check-on-mac}

1. Kliknij **Apple menu** > **About This Mac** > **More Info**.
2. Przewiń w dół i kliknij **System Report**.
3. W sekcji **Hardware** wybierz **Thunderbolt / USB4** lub **USB**.
4. Każdy port USB-C wymieniony w sekcji Thunderbolt / USB4 domyślnie obsługuje DisplayPort Alt Mode.

**Wskazówka**: Wszystkie współczesne komputery Mac z portami USB-C / Thunderbolt obsługują DisplayPort Alt Mode bez dodatkowej konfiguracji.

!!! note "Obsługiwane modele"

    - MacBook Neo (A18 Pro)
    - MacBook Air
        - MacBook Air 13-in. (M5)
        - MacBook Air 15-in. (M5)
        - MacBook Air 13-in. (M4)
        - MacBook Air 13-in. (M3)
        - MacBook Air 13-in. (M2)
        - MacBook Air 13-in. (M1, 2020)
        - MacBook Air 15-in. (M4)
        - MacBook Air 15-in. (M3)
        - MacBook Air 15-in. (M2, 2023)
        - MacBook Air (Intel, 2020)
    - MacBook Pro
        - MacBook Pro 14-in. (M5)
        - MacBook Pro 14-in. (M5 Pro)
        - MacBook Pro 14-in. (M5 Max)
        - MacBook Pro 16-in. (M5 Pro)
        - MacBook Pro 16-in. (M5 Max)
        - MacBook Pro 13-in. (M2, 2022)
        - MacBook Pro 13-in. (M1, 2020)
        - MacBook Pro 13-in. (Intel, dwa porty, 2020)
        - MacBook Pro 13-in. (Intel, cztery porty, 2020)
        - MacBook Pro 14-in. (M4 Max)
        - MacBook Pro 14-in. (M4 Pro)
        - MacBook Pro 14-in. (M4)
        - MacBook Pro 14-in. (M3)
        - MacBook Pro 14-in. (M3 Pro lub M3 Max)
        - MacBook Pro 14-in. (M2 Pro lub M2 Max, 2023)
        - MacBook Pro 14-in. (M1 Pro lub M1 Max, 2021)
        - MacBook Pro 16-in. (M4 Max)
        - MacBook Pro 16-in. (M4 Pro)
        - MacBook Pro 16-in. (M3 Pro lub M3 Max)
        - MacBook Pro 16-in. (M2 Pro lub M2 Max, 2023)
        - MacBook Pro 16-in. (M1 Pro lub M1 Max, 2021)
        - MacBook Pro 16-in. (Intel, 2019)
    - iMac
        - iMac (M4, dwa porty)
        - iMac (M4, cztery porty)
        - iMac (M3, dwa porty)
        - iMac (M3, cztery porty)
        - iMac 21.5-in. (Intel, 2019)
        - iMac 21.5-in. (Intel, 2017)
        - iMac 24-in. (M1, dwa porty, 2021)
        - iMac 24-in. (M1, cztery porty, 2021)
        - iMac27-in. (Intel,2020)
        - iMac Pro (Intel, 2017)
    - Mac mini
        - Mac mini (M4)
        - Mac mini (M4 Pro)
        - Mac mini (M2 lub M2 Pro)
        - Mac mini (M1, 2020)
        - Mac mini (Intel, 2018)
    - Mac Studio
        - Mac Studio (M4 Max)
        - Mac Studio (M3 UIitra)
        - Mac Studio (M2 Max lub M2 UItra)
        - Mac Studio (M1 Max lub M1 UItra, 2022)
    - Mac Pro
        - Mac Pro (M2 UItra)
        - Mac Pro (Intel, 2019)

## Jak sprawdzić w Androidzie {#how-to-check-on-android}

1. Otwórz **Settings** telefonu i wyszukaj *„display”*, *„HDMI”* lub *„desktop mode”*.
2. Poszukaj funkcji takich jak **Samsung DeX**, **Motorola Ready For**, **Huawei EasyProjection** lub *„External display”*. Sprawdź w dokumentacji producenta, czy dokładny model obsługuje **przewodowe połączenie z wyświetlaczem przez USB-C**. Sama funkcja bezprzewodowego wyświetlania nie potwierdza obsługi DP Alt Mode.
3. Jeśli telefon obsługuje tę funkcję, po podłączeniu monitora zwykle pojawi się powiadomienie, np. *„External display connected”*.
4. Potwierdź wyjście wideo przez bezpośrednie połączenie z Comet Q lub wyświetlaczem za pomocą adaptera wymagającego DP Alt Mode. Same aplikacje z informacjami o USB nie pozwalają wiarygodnie potwierdzić obsługi natywnego wyjścia wideo.

**Uwaga**: Wiele niedrogich telefonów z Androidem nie obsługuje DP Alt Mode, mimo że ma port USB-C. Zawsze sprawdź to przed zakupem Comet Q.

!!! note "Przykłady urządzeń Samsung z przewodowym wyjściem wideo"

    Poniższe pozycje dotyczące urządzeń Samsung sprawdzono na podstawie [informacji Samsung o zgodności z DeX](https://www.samsung.com/us/support/answer/ANS10001955/){target="_blank"}.

    - Galaxy A90 5G
    - Galaxy Book
    - Galaxy Fold
    - Galaxy Note
        - Galaxy Note 8
        - Galaxy Note 9
        - Galaxy Note 10 — seria
        - Galaxy Note20 — seria
    - Galaxy S
        - Galaxy Tab S7 / 7+
        - Galaxy Tab S8 / 8+ / S8 Ultra
        - Galaxy S8 i S8+
        - Galaxy S9 i S9+
        - Galaxy S10 — seria
        - Galaxy S20 — seria
        - Galaxy S21 — seria
        - Galaxy S22 — seria
        - Galaxy S23 — seria
        - Galaxy S24 — seria
        - Galaxy S25 — seria
    - Galaxy Tab
        - Galaxy Tab S4
        - Galaxy Tab S5e
        - Galaxy Tab S6
    - Galaxy Z
        - Galaxy Z Flip7
        - Galaxy Z Flip8
        - Galaxy Z Fold2
        - Galaxy Z Fold3
        - Galaxy Z Fold4
        - Galaxy Z Fold7

## Jak sprawdzić na iPhonie i iPadzie {#how-to-check-on-iphone-and-ipad}

1. Seria iPhone 15 i nowsze (z wyjątkiem iPhone 16e i iPhone 17e) obsługują DisplayPort Alt Mode przez port USB-C. Sprawdź dokładny model w [dokumentacji Apple dotyczącej podłączania wyświetlaczy](https://support.apple.com/en-ie/105099#displays){target="_blank"}.
2. iPhone 14 i starsze mają złącze Lightning i nie są zgodne.
3. Wszystkie modele iPada z USB-C (iPad Pro, iPad Air 4. generacji i nowsze, iPad mini 6. generacji i nowsze oraz iPad 10. generacji i nowsze) obsługują wyjście wideo.
4. iPady ze starszym portem Lightning nie są zgodne.

!!! note "Przykłady modeli z wyjściem wideo USB-C"

    Poniższe pozycje dotyczące iPhone’ów sprawdzono na podstawie [dokumentacji Apple dotyczącej wyświetlaczy zewnętrznych](https://support.apple.com/en-ie/105099#displays){target="_blank"}.

    - iPhone
        - iPhone 18 Pro
        - iPhone 18 Pro Max
        - iPhone 17 Pro
        - iPhone 17 Pro Max
        - iPhone 17
        - iPhone 16 Pro
        - iPhone 16 Pro Max
        - iPhone 16
        - iPhone 16 Plus
        - iPhone 15 Pro
        - iPhone 15 Pro Max
        - iPhone 15
        - iPhone 15 Plus
    - iPad
        - iPad (A16)
        - iPad (10. generacji)
    - iPad mini
        - iPad mini (6. generacji)
        - iPad mini (A17 Pro)
    - iPad Air
        - iPad Air (5. generacji)
        - iPad Air (4. generacji)
        - iPad Air 11-inch (M4)
        - iPad Air 11-inch (M3)
        - iPad Air 11-inch (M2)
        - iPad Air 13-inch (M4)
        - iPad Air 13‑inch (M3)
        - iPad Air 13-inch (M2)
    - iPad Pro
        - iPad Pro 11‑inch (M5)
        - iPad Pro 11‑inch (M4)
        - iPad Pro 11-inch (4. generacji)
        - iPad Pro 11-inch (3. generacji)
        - iPad Pro 12.9-inch (5. generacji)
        - iPad Pro 12.9-inch (6. generacji)
        - iPad Pro 13‑inch (M5)
        - iPad Pro 13‑inch (M4)

## Konsole przenośne, tablety i inne urządzenia {#handhelds-tablets-and-other-devices}

1. **Steam Deck**, **ROG Ally**, **Lenovo Legion Go** — wszystkie obsługują DP Alt Mode.
2. **Większość tabletów z Windows** i USB-C (Surface Pro 8 i nowsze itd.) — obsługuje ten tryb.
3. W przypadku innych urządzeń sprawdź oficjalną specyfikację i szukaj określeń *„DisplayPort”*, *„Alt Mode”*, *„video output”* lub *„Thunderbolt”*.

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
