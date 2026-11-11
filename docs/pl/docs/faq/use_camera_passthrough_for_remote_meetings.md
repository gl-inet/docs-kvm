# Jak przesyłać obraz z lokalnej kamery podczas spotkań zdalnych? {#how-can-i-use-camera-passthrough-for-remote-meetings}

**Uwaga**: Tę funkcję wprowadzono w oprogramowaniu układowym v1.10.0 i jest ona obsługiwana wyłącznie w trybie WebRTC (FEC). Obecnie można z niej korzystać w przeglądarkach internetowych i kliencie na komputer, ale aplikacja mobilna nie jest jeszcze obsługiwana.

---

Pracując z domu, możesz za pomocą KVM uzyskać dostęp do komputera w biurze i dołączyć na nim do wideokonferencji w Zoom, Microsoft Teams lub podobnej aplikacji. Kamera może jednak pokazywać tylko biuro, a nie Ciebie.

Funkcja **Camera** urządzenia GL.iNet KVM umożliwia przesyłanie obrazu z kamery komputera domowego do komputera w biurze jako wirtualnej kamery USB. Wybierz tę kamerę w aplikacji do spotkań, aby inni uczestnicy mogli Cię widzieć podczas udostępniania plików lub aplikacji z komputera w biurze.

## Szybka konfiguracja {#quick-setup}

Wykonaj poniższe kroki, aby użyć funkcji Camera na przykładzie wideokonferencji w Zoom.

1. Przed dołączeniem do spotkania zaloguj się do KVM na komputerze sterującym i przejdź do **Session** -> **Audio & Camera**. Włącz Camera, a następnie kliknij ikonę kamery, aby rozpocząć.

    ![enable camera 1](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera.png){class="glboxshadow"}

    Jeśli podczas włączania Camera pojawi się komunikat o limicie zasobów USB, przejdź do **Settings** -> **USB Devices** i wyłącz nieużywane emulowane urządzenia USB, aby zwolnić zasoby. Następnie włącz Camera i spróbuj ponownie.

    ![enable camera 3](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-3.png){class="glboxshadow"}

    Przeglądarka może poprosić o dostęp do kamery. Wybierz kamerę, której chcesz używać, sprawdź podgląd obrazu i zezwól na dostęp.

    ![enable camera 2](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-2.png){class="glboxshadow"}

2. Otwórz Zoom i dołącz do spotkania na komputerze sterowanym. Kliknij strzałkę obok przycisku wideo i wybierz **UVC camera**.

    ![uvc-camera](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/uvc-camera.png){class="glboxshadow"}

    Następnie włącz wideo, aby inni uczestnicy mogli zobaczyć obraz z kamery urządzenia sterującego.

    **Uwaga**: Zapewnij stabilne połączenie sieciowe, aby obraz podczas spotkania był płynny i wyraźny.

## Rozwiązywanie problemów {#troubleshooting}

??? note "Co zrobić, jeśli obraz z kamery nie dociera do komputera sterowanego?"

    Sprawdź, czy komputer sterowany rozpoznaje wirtualną kamerę KVM.

    Na komputerze sterowanym przejdź do **Settings** -> **Bluetooth & devices** -> **Cameras** i poszukaj UVC Camera w sekcji Connected cameras.

    ![check camera settings](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/check-camera-settings.png){class="glboxshadow"}

    Jeśli kamera się nie pojawia, połączenie danych USB między KVM a komputerem sterowanym może być rozłączone lub poluzowane.

??? note "Co zrobić, jeśli podczas włączania Camera w konsoli KVM pojawia się komunikat 'Camera Access Denied'?"

    ![camera access denied](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/camera-access-denied.png){class="glboxshadow"}

    Sprawdź następujące elementy na komputerze sterującym:

    - **Dostępność kamery**: Upewnij się, że kamera jest podłączona i działa. Przetestuj ją w systemowej aplikacji aparatu, a następnie zamknij aplikację przed ponowną próbą.

    - **Uprawnienia systemowe**: W Windows 11 przejdź do Settings -> Privacy & security -> Camera i włącz następujące opcje: Camera access, Let apps access your camera oraz Let desktop apps access your camera.

    - **Uprawnienia przeglądarki**: Zezwól witrynie KVM na dostęp do kamery. Jeśli dostęp był wcześniej zablokowany, zaktualizuj uprawnienia kamery dla witryny i odśwież stronę.

    - **Użycie kamery**: Zamknij inne aplikacje lub karty przeglądarki, które mogą korzystać z kamery, takie jak Zoom lub Microsoft Teams.

    Po wykonaniu tych kontroli ponownie włącz Camera w konsoli KVM.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
