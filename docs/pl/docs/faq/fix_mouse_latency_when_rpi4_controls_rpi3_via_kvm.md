# Jak usunąć opóźnienie myszy podczas sterowania RPi3 z RPi4 przez KVM {#how-to-fix-mouse-latency-when-rpi4-controls-rpi3-via-kvm}

Podczas zdalnego sterowania RPi3 z RPi4 przez KVM może występować opóźnienie myszy, zwykle wynoszące kilka sekund.

Aby rozwiązać problem, dodaj `usbhid.mousepoll=0` do wiersza parametrów rozruchowych w pliku `/boot/cmdline.txt` lub `/boot/firmware/cmdline.txt` na sterowanym RPi3, a następnie uruchom urządzenie ponownie.

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
