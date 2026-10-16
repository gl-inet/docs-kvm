# Come risolvere il ritardo del mouse quando RPi4 controlla RPi3 {#how-to-fix-mouse-latency-when-rpi4-controls-rpi3}

Quando usi un Raspberry Pi4 per controllare un Raspberry Pi3 tramite KVM GL.iNet, il mouse può presentare un ritardo di alcuni secondi.

Per risolvere il problema, aggiungi `usbhid.mousepoll=0` alla riga dei parametri di avvio nel file `/boot/cmdline.txt` oppure `/boot/firmware/cmdline.txt` del server gestito, cioè RPI3 in questo caso, quindi riavvialo.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
