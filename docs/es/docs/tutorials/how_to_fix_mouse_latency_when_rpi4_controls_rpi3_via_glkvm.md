# Cómo solucionar el retardo del ratón al controlar un RPi3 desde un RPi4 {#how-to-fix-mouse-latency-when-rpi4-controls-rpi3}

Al utilizar un Raspberry Pi4 para controlar un Raspberry Pi3 mediante un KVM GL.iNet, puede aparecer un retardo del ratón que suele durar unos segundos.

Para resolverlo, añada `usbhid.mousepoll=0` a la línea de parámetros de arranque de `/boot/cmdline.txt` o `/boot/firmware/cmdline.txt` del dispositivo controlado, en este caso el RPI3, y reinícielo.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
