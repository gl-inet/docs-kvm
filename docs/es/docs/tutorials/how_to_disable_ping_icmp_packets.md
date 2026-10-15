# Cómo desactivar los paquetes PING/ICMP salientes del KVM {#how-to-disable-outgoing-pingicmp-packets-from-kvm}

El KVM envía periódicamente paquetes PING (ICMP) para comprobar la conectividad de red. Este documento explica cómo desactivar este comportamiento y sus efectos secundarios.

## Dispositivos que solo tienen Ethernet {#for-ethernet-only-devices}

En dispositivos con conexión únicamente Ethernet, como Comet (GL-RM1) y Comet PoE (GL-RM1PE), el sistema envía paquetes PING a la puerta de enlace predeterminada para comprobar la conexión a Internet. El resultado se indica mediante el LED.

Para desactivar temporalmente este comportamiento, ejecute:

```bash
/etc/init.d/S23led stop
```

> **Nota:** al desactivar este servicio, el **botón Reset** también dejará de estar disponible.

## Dispositivos con Ethernet y Wi-Fi {#for-devices-with-both-ethernet-and-wi-fi}

En dispositivos con Ethernet y Wi-Fi, el sistema envía paquetes PING a servidores DNS públicos para comprobar el acceso a Internet de cada interfaz. Este mecanismo permite la conmutación dinámica por error entre varias conexiones WAN, para que el dispositivo cambie a Wi-Fi si Ethernet pierde acceso a Internet.

Para desactivar temporalmente este comportamiento, ejecute:

```bash
/etc/init.d/S98multi-wan stop
```

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
