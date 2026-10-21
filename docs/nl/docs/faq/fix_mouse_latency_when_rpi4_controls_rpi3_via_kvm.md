# Muisvertraging verhelpen wanneer een RPi4 een RPi3 bestuurt via een KVM {#how-to-fix-mouse-latency-when-rpi4-controls-rpi3-via-kvm}

Wanneer u een RPi3 via een KVM vanaf een RPi4 op afstand bedient, kan de muis vertraging vertonen, meestal enkele seconden.

U lost dit op door `usbhid.mousepoll=0` toe te voegen aan de regel met opstartparameters in `/boot/cmdline.txt` of `/boot/firmware/cmdline.txt` op de bestuurde RPi3 en het apparaat daarna opnieuw op te starten.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
