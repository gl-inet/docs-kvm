# Muisvertraging verhelpen wanneer een RPi4 een RPi3 bestuurt {#how-to-fix-mouse-latency-when-rpi4-controls-rpi3}

Wanneer u een Raspberry Pi4 gebruikt om via een GL.iNet KVM een Raspberry Pi3 te bedienen, kan de muis vertraging vertonen, meestal enkele seconden.

U lost dit op door `usbhid.mousepoll=0` toe te voegen aan de opstartregel in `/boot/cmdline.txt` (of in `/boot/firmware/cmdline.txt`) op de beheerde server (in dit geval de RPI3) en deze opnieuw op te starten.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
