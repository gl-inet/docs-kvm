# Så åtgärdar du musfördröjning när RPi4 styr RPi3 {#how-to-fix-mouse-latency-when-rpi4-controls-rpi3}

När du använder en Raspberry Pi 4 för att styra en Raspberry Pi 3 via GL.iNet KVM kan musen få en fördröjning som vanligtvis varar i några sekunder.

Åtgärda problemet genom att lägga till `usbhid.mousepoll=0` på startraden i `/boot/cmdline.txt` (eller i `/boot/firmware/cmdline.txt`) på den hanterade servern (dvs. RPi3 i det här fallet) och starta om den.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
