# Co zrobić, jeśli tryb myszy Relative nie działa z rejestratorem Reolink NVR {#what-should-i-do-if-relative-mouse-mode-doesnt-work-on-reolink-nvr}

Podczas sterowania rejestratorem Reolink NVR (zwłaszcza modelem bez obsługi dwóch myszy) lub niektórymi starszymi komputerami (np. bez portów USB) przez GL.iNet KVM tryb myszy Relative może nie działać. Typowe problemy obejmują całkowity brak reakcji lub działający ruch myszy przy braku reakcji na kliknięcia.

Problem wynika głównie z niezgodności między emulacją myszy KVM a ograniczonymi możliwościami urządzeń takich jak Reolink NVR:

- **Przed wersją oprogramowania v1.4.0**: KVM emulował tylko jedną mysz. Przełączenie między trybami Relative i Absolute wymagało ponownego uruchomienia KVM, ale rozwiązanie to działało poprawnie z większością starszych lub specjalistycznych urządzeń.

- **Po wersji oprogramowania v1.4.0**: Aby umożliwić płynne przełączanie trybów bez restartu, zmieniono domyślne działanie na jednoczesną emulację dwóch myszy (jednej dla trybu Relative, drugiej dla Absolute). Reolink NVR i niektóre starsze komputery nie obsługują jednak dwóch myszy, co powoduje dwa częste problemy:

    - Tryb myszy Relative w ogóle nie działa;
    - Ruch myszy działa, ale kliknięcia nie wywołują reakcji.

Aby rozwiązać problem, możesz wymusić tryb myszy Relative w terminalu. Wykonaj poniższe czynności:

1. Otwórz konsolę KVM i przejdź do **Toolbox** -> **Terminal**. Kliknij **Access**, aby otworzyć terminal KVM.

2. Otwórz plik konfiguracji następującym poleceniem:

    `vi /etc/kvmd/override.yaml`

3. Wprowadź poniższą konfigurację, aby wymusić tryb myszy Relative:

    ```
    kvmd:
        hid:
            mouse:
                absolute: false
    ```

4. Zapisz plik i zamknij edytor.

5. Uruchom ponownie urządzenie KVM, aby zastosować zmiany.

!!! note

    1. Jeśli powyższa metoda nie działa, spróbuj przywrócić oprogramowanie KVM do wersji starszej niż v1.4 (jeśli jest dostępna), która obsługuje emulację jednej myszy i jest zgodna ze starszymi urządzeniami.

    2. Samodzielna aplikacja GLKVM dla Mac OS nie obsługuje trybu myszy Relative z powodu ograniczeń silnika przeglądarki (brak obsługi API requestPointerLock). Zamiast niej użyj konsoli WWW.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
