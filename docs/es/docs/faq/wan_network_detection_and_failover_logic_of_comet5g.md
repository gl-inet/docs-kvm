# Detección de redes WAN y conmutación por error de Comet 5G {#what-is-the-wan-network-detection-and-failover-logic-of-comet-5g}

1. El sistema utiliza detección mediante ping: envía sondas a todas las interfaces cada **3 segundos** y evalúa las condiciones de conmutación por error cada **9 segundos**.

2. Si todas las pruebas ping de la interfaz de mayor prioridad fallan durante un periodo de **9 segundos**, pero la interfaz de menor prioridad sigue siendo accesible, se realiza la conmutación al finalizar ese periodo. No se conmuta si ninguna interfaz es accesible.

3. Las interfaces marcadas como desconectadas siguen recibiendo sondas ping en segundo plano.

4. Recuperación: si la interfaz de mayor prioridad vuelve a responder al ping durante un periodo de **9 segundos**, el sistema vuelve a utilizarla al finalizar ese periodo.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
