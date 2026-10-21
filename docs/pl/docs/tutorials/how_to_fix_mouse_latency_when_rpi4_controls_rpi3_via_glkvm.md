# Jak usunąć opóźnienia myszy podczas sterowania RPi3 za pomocą RPi4 {#how-to-fix-mouse-latency-when-rpi4-controls-rpi3}

Podczas sterowania Raspberry Pi3 za pomocą Raspberry Pi4 przez GL.iNet KVM mogą występować opóźnienia myszy, zwykle trwające kilka sekund.

Aby rozwiązać ten problem, dopisz `usbhid.mousepoll=0` do wiersza parametrów rozruchowych w `/boot/cmdline.txt` (lub `/boot/firmware/cmdline.txt`) na zarządzanym serwerze (w tym przypadku RPI3), a następnie uruchom go ponownie.

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
