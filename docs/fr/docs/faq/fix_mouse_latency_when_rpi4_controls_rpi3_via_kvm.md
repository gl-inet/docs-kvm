# Corriger la latence de la souris lorsque le RPi4 contrôle le RPi3 via KVM {#how-to-fix-mouse-latency-when-rpi4-controls-rpi3-via-kvm}

Un décalage de la souris de plusieurs secondes peut apparaître lorsque vous contrôlez un RPi3 à distance depuis un RPi4 via KVM.

Pour le résoudre, ajoutez `usbhid.mousepoll=0` à la ligne de paramètres de démarrage dans `/boot/cmdline.txt` ou `/boot/firmware/cmdline.txt` sur le RPi3 contrôlé, puis redémarrez-le.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
