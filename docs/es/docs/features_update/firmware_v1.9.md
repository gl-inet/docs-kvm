# Firmware v1.9

Esta versión incorpora nuevas funciones, mejoras de interacción, mayor protección de la privacidad y conexiones de red más fiables para ofrecer una experiencia de KVM remoto más completa, estable y segura.

Obtenga el firmware más reciente en el [centro de descargas de firmware](https://dl.gl-inet.com/kvm){target="_blank"}

## Modo de latencia {#latency-mode}

Este firmware incorpora **Latency Mode**, que permite equilibrar la respuesta a las entradas y la fluidez del vídeo. Puede seleccionar Lowest Latency o Smooth Display para optimizar el rendimiento del control remoto.

![Modo de latencia](https://static.gl-inet.com/docs/kvm/features_update/1.9/latency_mode.png){class="glboxshadow" width="360"}

- Lowest Latency: minimiza la latencia de entrada para que el teclado y el ratón respondan con mayor rapidez.
- Smooth Display: optimiza la imagen para eliminar los saltos y la pérdida de fotogramas, y conseguir una reproducción estable.

## Facilidad de uso del ratón {#mouse-usability}

Se ha añadido la opción **Primary Button** para mejorar la facilidad de uso del ratón. Puede establecer el botón izquierdo o el derecho como botón principal según sus preferencias.

![Botón principal](https://static.gl-inet.com/docs/kvm/features_update/1.9/primary_button.png){class="glboxshadow" width="360"}

## Pantalla del dispositivo {#screen-display}

Puede personalizar los ajustes de **Screen Display** del KVM desde la pantalla táctil, incluidos el bloqueo de pantalla, el fondo de pantalla, el formato de hora (24 horas / 12 horas) y el formato de fecha. Esta función está disponible exclusivamente en los modelos equipados con pantalla táctil.

También puede configurar rápidamente herramientas de redes superpuestas, como Tailscale y NetBird, directamente desde la pantalla táctil con unos pocos toques. Esta función no estaba disponible en versiones anteriores del firmware.

![Pantalla del dispositivo](https://static.gl-inet.com/docs/kvm/features_update/1.9/screen_display.png){class="glboxshadow" width="360"}

## Idioma {#language}

Las versiones anteriores del firmware solo admitían chino e inglés. Esta versión añade compatibilidad nativa con el **japonés** para facilitar el uso a los usuarios de ese idioma.

![Idioma](https://static.gl-inet.com/docs/kvm/features_update/1.9/language.png){class="glboxshadow" width="360"}

## Extensiones {#extensions}

Esta versión integra [NetBird](https://netbird.io/){target="_blank"}, una plataforma de red de código abierto basada en el modelo de confianza cero que permite crear redes privadas seguras para hogares y empresas. Esta solución de red superpuesta se basa en WireGuard® y permite acceder de forma segura al KVM desde cualquier lugar a través de las redes virtuales de NetBird. Consulte las [instrucciones de configuración](../faq/remote_access_via_netbird.md){target="_blank"}.

![NetBird](https://static.gl-inet.com/docs/kvm/features_update/1.9/netbird.png){class="glboxshadow"}

## Otras mejoras {#other-enhancements}

- Programa de firmware beta: puede participar en el programa beta para probar funciones antes de su lanzamiento.

- Reconocimiento de texto: esta herramienta utiliza el reconocimiento óptico de caracteres (OCR) para capturar texto de cualquier área seleccionada de la pantalla remota. Admite chino, inglés y el modo bilingüe chino-inglés. Consulte [más detalles](../tutorials/how_to_capture_text_from_remote_screen.md).

- Zona horaria por ciudad: establezca su zona horaria seleccionando una ciudad.

- Seguridad de las sesiones: los tokens de inicio de sesión ahora caducan 12 horas después de finalizar la sesión; anteriormente eran permanentes.

- Seguridad de los registros del sistema: se ha implementado el enmascaramiento de datos sensibles en todos los registros del sistema.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [contacte con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
