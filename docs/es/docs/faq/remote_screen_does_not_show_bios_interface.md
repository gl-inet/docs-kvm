# Qué hacer si la pantalla remota no muestra la interfaz de la BIOS {#what-should-i-do-if-the-remote-screen-does-not-show-the-bios-interface}

Si la pantalla remota no muestra la interfaz de la BIOS al acceder al dispositivo controlado mediante KVM, por ejemplo si aparece No HDMI Signal, puede deberse a que la BIOS normalmente solo envía la imagen al monitor principal. Pruebe lo siguiente.

## Portátil {#laptop}

Si el dispositivo controlado es un portátil, su pantalla integrada actúa como pantalla principal, por lo que el KVM externo no puede mostrar la BIOS.

## Equipo de escritorio {#desktop}

En los equipos de escritorio, conecte el monitor principal al puerto DisplayPort, si está disponible. La mayoría de las tarjetas gráficas y placas base dan prioridad a la salida DP sobre HDMI durante el arranque.

Utilice estos métodos para que la BIOS sea visible mediante el KVM.

- Pruebe los distintos puertos de monitor. Conecte el KVM GL.iNet al puerto configurado como salida de pantalla principal del equipo.

- Utilice un divisor HDMI de 1 a 2, no incluido, para duplicar la señal de la pantalla principal hacia el KVM.

> **Nota**: este problema también puede producirse cuando el dispositivo controlado arranca en **Windows PE**, ya que las señales de la BIOS solo se transmiten al monitor principal y no se muestran en la pantalla remota del KVM.

> Se recomienda probar con un monitor adicional. Si la pantalla secundaria tampoco recibe señal, el KVM no podrá capturar la BIOS. Puede integrar o instalar manualmente los controladores de pantalla en WinPE para resolverlo.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
