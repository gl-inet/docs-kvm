# Co zrobić, jeśli na ekranie zdalnym nie widać interfejsu BIOS {#what-should-i-do-if-the-remote-screen-does-not-show-the-bios-interface}

Jeśli podczas dostępu do urządzenia docelowego przez KVM na ekranie zdalnym nie widać interfejsu BIOS (np. pojawia się No HDMI Signal), przyczyną jest zwykle wysyłanie obrazu BIOS tylko na monitor główny. Poniżej znajdziesz wskazówki.

## Laptop {#laptop}

Jeśli urządzeniem docelowym jest laptop, jego wbudowany ekran pełni rolę ekranu głównego, więc zewnętrzny KVM nie może wyświetlić interfejsu BIOS.

## Komputer stacjonarny {#desktop}

W przypadku komputerów stacjonarnych podłącz monitor główny do portu DisplayPort, jeśli jest dostępny. Większość kart graficznych i płyt głównych podczas uruchamiania nadaje pierwszeństwo wyjściu DP przed HDMI.

Aby interfejs BIOS był widoczny przez KVM, skorzystaj z poniższych metod.

- Wypróbuj różne porty monitora. Podłącz GL.iNet KVM do portu ustawionego na komputerze jako główne wyjście obrazu.

- Użyj rozdzielacza HDMI 1 na 2 (brak w zestawie), aby powielić sygnał ekranu głównego do urządzenia KVM.

> **Uwaga**: Ten problem może również wystąpić po uruchomieniu urządzenia docelowego w **Windows PE**, ponieważ sygnał BIOS jest przesyłany tylko do monitora głównego i nie jest widoczny na zdalnym ekranie KVM.

> Zalecamy sprawdzenie działania z dodatkowym monitorem. Jeśli ekran dodatkowy nadal nie odbiera sygnału, KVM nie będzie mógł przechwycić obrazu BIOS. Aby rozwiązać ten problem, możesz ręcznie zintegrować lub zainstalować sterowniki ekranu w systemie WinPE.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
