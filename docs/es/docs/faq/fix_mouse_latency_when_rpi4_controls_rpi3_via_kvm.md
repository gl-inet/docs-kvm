# Cómo solucionar el retardo del ratón al controlar un RPi3 desde un RPi4 mediante KVM {#how-to-fix-mouse-latency-when-rpi4-controls-rpi3-via-kvm}

Al manejar un RPi3 de forma remota desde un RPi4 mediante KVM, puede aparecer un retardo del ratón que suele durar varios segundos.

Para resolverlo, añada `usbhid.mousepoll=0` a la línea de parámetros de arranque en `/boot/cmdline.txt` o `/boot/firmware/cmdline.txt` del RPi3 controlado y reinicie el dispositivo.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
