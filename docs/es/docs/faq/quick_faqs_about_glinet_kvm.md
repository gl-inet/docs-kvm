# Preguntas rápidas sobre los KVM GL.iNet {#quick-faqs-about-glinet-kvm}

Esta recopilación ofrece respuestas rápidas a algunas preguntas básicas frecuentes sobre los KVM GL.iNet.

## Información básica {#basic-information}

**P1. ¿Qué dispositivos puede controlar un KVM GL.iNet?**

R1. Un KVM GL.iNet puede controlar cualquier dispositivo con salida HDMI y entrada USB, como portátiles, equipos de escritorio, Raspberry Pi o miniequipos.

Además, Comet Q (GL-RMQ1) puede controlar cualquier dispositivo cuyo puerto USB-C admita DisplayPort Alt Mode para la salida de vídeo, sin necesidad de un puerto HDMI. Esto incluye determinados iPhone, iPad, teléfonos Android, MacBook, Mac mini y la mayoría de los portátiles Windows modernos, entre otros. Consulte los detalles [aquí](../user_guide/gl-rmq1/product_overview.md#compatibility).

---

**P2. ¿Necesito instalar algún software para utilizar un KVM GL.iNet?**

R2. No es necesario instalar software en el dispositivo controlado, que puede utilizar Windows, macOS, ChromeOS, Linux u otros sistemas.

La necesidad de instalar software en el dispositivo de control depende del método de acceso al KVM.

??? "Control cercano (solo para Comet 5G)"

    **Nota**: este método solo está disponible en Comet 5G (GL-RM10RC).

    Comet 5G ofrece Wi-Fi Nearby Control para una gestión local rápida sin conexiones por cable. Cambie el modo de red Wi-Fi de Comet 5G a AP para que genere un SSID Wi-Fi único. Conéctese a ese SSID para acceder de forma segura a su consola. Consulte los detalles [aquí](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control).

    Al activar el modo AP, Comet 5G se desconecta de la red Wi-Fi a la que estaba conectado y solo permite el acceso cercano, sin conexión a Internet.

??? "Control local (solo para Comet X)"

    **Nota**: este método solo está disponible en Comet X (GL-RM4PE).

    Comet X dispone de un puerto HDMI OUT y dos puertos USB adicionales, útiles para solucionar problemas, configurar el equipo e instalar sistemas operativos de forma local. Conecte un monitor, un ratón y un teclado para controlar directamente el hardware sin configuración adicional. Consulte los detalles [aquí](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control).

??? "Acceso por LAN"

    Para acceder al KVM desde la misma red local (LAN), no necesita instalar software en el dispositivo de control.

    Abra un navegador en el dispositivo de control e introduzca la IP del KVM o `glkvm.local` en la barra de direcciones para acceder de forma local.

    Consulte los detalles [aquí](local_access_via_browser.md){target="_blank"}.

??? "Acceso remoto"

    - **Aplicación GLKVM**

        Si el dispositivo de control utiliza Windows, macOS, Android o iOS, puede instalar la [aplicación GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} y acceder de forma remota al KVM y, a través de él, al dispositivo controlado.

        Consulte los detalles [aquí](remote_access_via_glkvm_app.md){target="_blank"}.

    - **Servicio de nube**

        Este método es adecuado si no puede o no desea instalar la aplicación GLKVM.

        Vincule el KVM al servicio de nube. Después introduzca `glkvm.com` en un navegador del dispositivo de control para acceder de forma remota al KVM y al dispositivo controlado, sin instalar la aplicación GLKVM.

        Consulte los detalles [aquí](remote_access_via_cloud.md){target="_blank"}.

    - **Tailscale**

        Este método es adecuado si no puede o no desea utilizar la aplicación GLKVM o el servicio de nube, aunque requiere más pasos.

        Vincule el KVM y el dispositivo de control a la misma cuenta de Tailscale. Después introduzca la IP virtual de Tailscale del KVM en un navegador del dispositivo de control para acceder de forma remota al KVM y al dispositivo controlado.

        Consulte los detalles [aquí](remote_access_via_tailscale.md){target="_blank"}.

    - **ZeroTier**

        Este método es adecuado si no puede o no desea utilizar la aplicación GLKVM o el servicio de nube, aunque requiere más pasos.

        Añada el KVM y el dispositivo de control a la misma red ZeroTier. Después introduzca la IP de ZeroTier del KVM en un navegador del dispositivo de control para acceder de forma remota al KVM y al dispositivo controlado.

        Consulte los detalles [aquí](remote_access_via_zerotier.md){target="_blank"}.

    - **NetBird**

        Este método es adecuado si no puede o no desea utilizar la aplicación GLKVM o el servicio de nube, aunque requiere más pasos.

        [NetBird](https://netbird.io/){target="_blank"} es una plataforma de redes de confianza cero y código abierto que permite crear redes privadas seguras para uso doméstico y empresarial. Su red superpuesta basada en WireGuard® permite acceder a los dispositivos de forma segura desde cualquier lugar y en cualquier momento.

        Los KVM GL.iNet integran NetBird para vincularse a su red virtual y permitir el acceso remoto.

        Consulte los detalles [aquí](remote_access_via_netbird.md){target="_blank"}.

---

**P3. ¿Cómo accedo a un KVM GL.iNet?**

R3. Puede acceder de forma local o remota mediante los siguientes métodos:

- [Acceso por LAN mediante un navegador](local_access_via_browser.md){target="_blank"}
- [Acceso remoto mediante el servicio de nube](remote_access_via_cloud.md){target="_blank"}
- [Acceso remoto mediante la aplicación GLKVM](remote_access_via_glkvm_app.md){target="_blank"}
- [Acceso remoto mediante Tailscale](remote_access_via_tailscale.md){target="_blank"}
- [Acceso remoto mediante ZeroTier](remote_access_via_zerotier.md){target="_blank"}
- [Acceso remoto mediante NetBird](remote_access_via_netbird.md){target="_blank"}

Además, algunos modelos admiten Nearby Control o Local Control para acceder a ellos en el lugar donde se encuentran sin conectarlos a otro router.

- [Control cercano (solo para Comet 5G)](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control){target="_blank"}
- [Control local (solo para Comet X)](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control){target="_blank"}

---

**P4. ¿Necesito abrir puertos hacia la WAN para acceder de forma remota a un KVM GL.iNet?**

R4. No. No es necesario abrir puertos ni disponer de una IP pública.

---

**P5. ¿La aplicación GLKVM es compatible con ChromeOS o Linux?**

R5. No. Actualmente, la aplicación GLKVM no se puede instalar en ChromeOS ni Linux.

Si el dispositivo de control utiliza ChromeOS o Linux, no podrá instalar la aplicación GLKVM ni acceder al dispositivo controlado de forma remota mediante ella.

Sin embargo, puede utilizar el <u>servicio de nube</u>, <u>Tailscale</u>, <u>ZeroTier</u> o <u>NetBird</u> para acceder de forma remota. Consulte la P3 anterior.

También puede acceder al KVM de forma local mediante un navegador. Consulte la P3 anterior.

---

**P6. ¿Puede Comet (GL-RM1) conectarse a una red inalámbrica?**

R6. No. Comet (GL-RM1) no admite conexiones de red inalámbricas.

Debe conectarse a un dispositivo de red, como un router, mediante un cable Ethernet para acceder a Internet.

Si prefiere un KVM compatible con Wi-Fi, puede considerar estos modelos:

* [Comet Pro (GL-RM10)](https://www.gl-inet.com/products/gl-rm10/){target="_blank"}
* [Comet 5G (GL-RM10RC)](https://www.gl-inet.com/products/gl-rm10rc/){target="_blank"}
* [Comet Q (GL-RMQ1)](https://www.gl-inet.com/products/gl-rmq1/){target="_blank"}

---

## Control de alimentación {#power-control}

**P1. ¿Puede un KVM GL.iNet encender y apagar el dispositivo controlado de forma remota?**

R1. Puede encender y apagar el dispositivo controlado de forma remota mediante estos métodos:

- Wake-on-LAN, servicio de software integrado.

- [Placa ATX](../user_guide/gl-atx-board/index.md){target="_blank"}, vendida por separado; no funciona con Comet Q.

- [FingerBot](../user_guide/gl-fgb-01/index.md){target="_blank"}, vendido por separado; no funciona con Comet Q.

---

**P2. ¿Cómo se utiliza la placa ATX para controlar la alimentación de forma remota?**

R2. Consulte la [guía de usuario de la placa ATX](../user_guide/gl-atx-board/index.md){target="_blank"}.

---

## Funciones {#features}

!!! Tip "Consejo"

    A continuación se responden preguntas sobre algunas funciones habituales. Consulte la [guía de usuario](../user_guide/index.md) correspondiente para conocer todas las funciones.

**P1. ¿Es obligatorio utilizar el servicio KVM Cloud?**

R1. No. El servicio de nube es opcional.

Si no desea depender de la nube para acceder de forma remota, puede utilizar herramientas de redes superpuestas de terceros, como Tailscale, ZeroTier o NetBird.

---

**P2. ¿Puedo utilizar un solo KVM GL.iNet para controlar varios dispositivos?**

R2. Los siguientes KVM GL.iNet solo pueden controlar un dispositivo:

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)
* Comet Q (GL-RMQ1)

Comet X (GL-RM4PE) puede conectarse a un máximo de cuatro dispositivos al mismo tiempo, aunque solo permite controlar uno a la vez. Puede alternar rápidamente entre ellos con el botón físico del panel frontal si está junto al equipo, o mediante la consola remota si está en otro lugar.

Comet X (GL-RM4PE) tiene cuatro canales independientes en el panel trasero. Cada canal incluye un puerto HDMI para vídeo, un puerto Type-C para las señales del teclado y el ratón, y un puerto USB 2.0 para periféricos USB, como Fingerbot o una placa ATX.

---

**P3. ¿Qué es Wake-on-LAN?**

R3. Wake-on-LAN (WOL) permite encender un equipo o dispositivo de forma remota, o reactivarlo desde un estado de bajo consumo, a través de una red. Funciona enviando un «paquete mágico» con la dirección MAC del dispositivo para activar su arranque. Se utiliza para la administración remota, las configuraciones de espera con ahorro energético y la gestión centralizada de sistemas.

---

**P4. ¿Los KVM GL.iNet admiten Mouse Jiggle?**

R4. Sí. Puede activar Mouse Jiggle en la consola KVM.

La función Mouse Jiggler simula pequeños movimientos periódicos del ratón para evitar que el equipo controlado entre en suspensión por inactividad prolongada, por ejemplo durante reuniones remotas o tareas de administración de servidores.

---

**P5. ¿Los KVM GL.iNet admiten audio bidireccional?**

R5. Sí. Active Speaker y Microphone en la consola KVM para transmitir audio en ambos sentidos.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
