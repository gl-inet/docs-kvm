# Come risolvere il ritardo del mouse quando RPi4 controlla RPi3 tramite KVM {#how-to-fix-mouse-latency-when-rpi4-controls-rpi3-via-kvm}

Quando controlli RPi3 da remoto con RPi4 tramite KVM, il mouse può presentare un ritardo di diversi secondi.

Per risolvere il problema, aggiungi `usbhid.mousepoll=0` alla riga dei parametri di avvio nel file `/boot/cmdline.txt` o `/boot/firmware/cmdline.txt` sul dispositivo RPi3 controllato, quindi riavvialo.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
