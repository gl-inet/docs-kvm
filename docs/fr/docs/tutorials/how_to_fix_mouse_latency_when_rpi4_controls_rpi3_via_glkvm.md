# Corriger la latence de la souris lorsque le RPi4 contrôle le RPi3 {#how-to-fix-mouse-latency-when-rpi4-controls-rpi3}

Lorsque vous utilisez un Raspberry Pi4 pour contrôler un Raspberry Pi3 via un KVM GL.iNet, un décalage de la souris de quelques secondes peut se produire.

Pour le corriger, ajoutez `usbhid.mousepoll=0` à la ligne de démarrage dans `/boot/cmdline.txt` (ou `/boot/firmware/cmdline.txt`) sur le serveur contrôlé (ici le RPI3), puis redémarrez-le.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
