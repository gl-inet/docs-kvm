# Diferencias entre el ratón absoluto y el ratón relativo {#what-is-the-difference-between-absolute-mouse-and-relative-mouse}

En la consola del KVM GL.iNet, **Mouse Mode** ofrece dos opciones: **Absolute** y **Relative**. Estos modos difieren en el comportamiento del ratón, los casos de uso y la experiencia de manejo. A continuación se explican para ayudarle a elegir el que mejor se adapte a sus necesidades.

![Modo de ratón](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/mouse_mode.jpg){class="glboxshadow"}

## Ratón absoluto {#absolute-mouse}

El modo absoluto permite controlar el ratón de forma fluida y sincronizada entre el equipo local y el dispositivo controlado. Al activarlo, ambos cursores utilizan el mismo sistema de coordenadas. Puede mover el cursor local entre la consola KVM y la pantalla remota sin interrupciones; el cursor remoto seguirá sus movimientos en tiempo real.

Durante el uso puede producirse un pequeño retardo debido a la transmisión por la red y a la codificación de vídeo. El cursor remoto se moverá ligeramente después que el local, pero esto no afecta a la fluidez general del manejo.

![Ratón absoluto](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/absolute.gif)

## Ratón relativo {#relative-mouse}

El modo relativo no sincroniza las coordenadas de los cursores local y remoto; estos funcionan en capas independientes. Antes de controlar el dispositivo, debe hacer clic dentro de la ventana remota para capturar el cursor.

En este modo, el cursor remoto queda limitado a la ventana remota y no puede pasar directamente al escritorio local. Los bordes de la ventana lo mantienen dentro del entorno controlado. Para liberarlo y volver a controlar el equipo local, pulse `Esc`.

![Ratón relativo](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative.gif)

En el modo Relative puede ajustar **Relative Sensitivity**, con valores de 0.1 a 2.0.

![Sensibilidad relativa](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative_sensitivity.jpg){class="glboxshadow"}

## Diferencias principales {#key-differences}

| Característica | Ratón absoluto | Ratón relativo |
| -------------------- | ------------------------------ | ----------------------------- |
| Coordinación de los cursores | Los cursores local y remoto están sincronizados y comparten el sistema de coordenadas | Los cursores funcionan en capas independientes, sin sincronización de coordenadas |
| Manejo | No es necesario hacer clic para capturar el cursor; movimiento fluido entre pantallas | Debe hacer clic en la pantalla remota para capturar el cursor; no permite pasar entre pantallas de forma fluida |
| Retardo | Pequeño retardo por la red y la codificación de vídeo | Retardo casi inexistente; solo se envían incrementos de movimiento |
| Casos de uso | Control fluido con varias pantallas, cambios frecuentes y posicionamiento preciso, como trabajo remoto o diseño gráfico | Dispositivos antiguos, BIOS o UEFI que no admiten ratón absoluto; evitar clics accidentales; redes inestables con necesidad de menor latencia |

## Resumen {#summary}

El ratón absoluto prioriza una experiencia de control fluida e integrada, mientras que el ratón relativo prioriza la compatibilidad y la estabilidad.

Para la mayoría de las tareas diarias de control remoto con el KVM GL.iNet, se recomienda utilizar el modo absoluto como opción predeterminada. El modo relativo resulta útil si hay problemas de compatibilidad o necesidades específicas.

- Utilice el **ratón absoluto** para un control remoto cotidiano fluido.
- Utilice el **ratón relativo** para acceder a la BIOS, manejar dispositivos antiguos que no admiten posicionamiento absoluto o evitar clics accidentales.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
