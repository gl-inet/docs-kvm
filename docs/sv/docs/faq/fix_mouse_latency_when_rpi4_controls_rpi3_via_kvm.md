# Så åtgärdar du musfördröjning när RPi4 styr RPi3 via KVM {#how-to-fix-mouse-latency-when-rpi4-controls-rpi3-via-kvm}

När du styr en RPi3 på distans från en RPi4 via KVM kan musen få en fördröjning som vanligtvis varar i flera sekunder.

Lös problemet genom att lägga till `usbhid.mousepoll=0` på raden med startparametrar i `/boot/cmdline.txt` eller `/boot/firmware/cmdline.txt` på den styrda RPi3-enheten och sedan starta om enheten.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
