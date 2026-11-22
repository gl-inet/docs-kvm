# Jak przywrócić ustawienia fabryczne urządzenia GL.iNet KVM? {#how-do-i-factory-reset-my-glinet-kvm}

## Metoda 1 – Użycie fizycznego przycisku resetowania {#method-1-use-the-physical-reset-button}

Upewnij się, że urządzenie KVM jest włączone i zakończyło uruchamianie.

Naciśnij i przytrzymaj fizyczny przycisk RESET przez **8–10 sekund**, a następnie go zwolnij. Jeśli urządzenie KVM ma otwór do resetowania, wciśnij szpilką przycisk wewnątrz otworu, przytrzymaj go przez 8 sekund, a następnie zwolnij. W modelu Comet X (GL-RM4PE) użyj przycisku przełączania na przednim panelu.

Poczekaj, aż urządzenie KVM automatycznie uruchomi się ponownie. Nie odłączaj zasilania podczas resetowania.

Nie przytrzymuj przycisku resetowania podczas włączania urządzenia KVM. Nie używaj przycisku resetowania na podłączonym komputerze ani na płytce ATX.

## Metoda 2 – Użycie lokalnego interfejsu WWW {#method-2-use-the-local-web-interface}

Podłącz komputer i urządzenie KVM do tej samej sieci lokalnej. Otwórz lokalny adres IP urządzenia KVM w przeglądarce i zaloguj się. Zobacz [Jak uzyskać lokalny dostęp do KVM przez przeglądarkę](local_access_via_browser.md).

Jeśli urządzenie KVM ma firmware v1.10 lub nowszy, otwórz **Settings** w prawym górnym rogu i przejdź do **System** -> **Reset Device**. Kliknij **Reset**, potwierdź i poczekaj, aż urządzenie KVM automatycznie uruchomi się ponownie. Nie odłączaj zasilania podczas resetowania.

![reset 1](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset1.png){class="glboxshadow"}

Jeśli urządzenie KVM ma firmware v1.9 lub starszy, otwórz **Settings** w lewym górnym rogu i przejdź do **System** -> **Reset KVM**. Kliknij **Reset**, potwierdź i poczekaj, aż urządzenie KVM automatycznie uruchomi się ponownie. Nie odłączaj zasilania podczas resetowania.

![reset 2](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset2.png){class="glboxshadow"}

## Po zresetowaniu {#after-the-reset}

Przywrócenie ustawień fabrycznych usuwa niestandardowe ustawienia urządzenia KVM. Po ponownym uruchomieniu lokalny adres IP urządzenia KVM może się zmienić. Otwórz ponownie lokalny interfejs WWW, postępuj zgodnie z instrukcjami konfiguracji początkowej, aby ustawić hasło administratora, a następnie ręcznie skonfiguruj ponownie potrzebne ustawienia.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
