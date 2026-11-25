# ¿Cómo restablecer los ajustes de fábrica de su KVM de GL.iNet? {#how-do-i-factory-reset-my-glinet-kvm}

## Método 1. Usar el botón físico de restablecimiento {#method-1-use-the-physical-reset-button}

Asegúrese de que el KVM esté encendido y haya terminado de arrancar.

Mantenga pulsado el botón físico RESET durante **8 a 10 segundos** y suéltelo. Si el KVM tiene un orificio de restablecimiento, use un alfiler para mantener pulsado el botón del interior durante 8 segundos y luego suéltelo. En el Comet X (GL-RM4PE), use el botón de conmutación del panel frontal.

Espere a que el KVM se reinicie automáticamente. No desconecte la alimentación durante el restablecimiento.

No mantenga pulsado el botón de restablecimiento al encender el KVM. No use el botón de restablecimiento del ordenador conectado ni el de la placa ATX.

## Método 2. Usar la interfaz web local {#method-2-use-the-local-web-interface}

Conecte el ordenador y el KVM a la misma red local. Abra la dirección IP local del KVM en un navegador e inicie sesión. Consulte [Cómo acceder al KVM de forma local mediante un navegador](local_access_via_browser.md).

Si el KVM tiene la versión v1.10 del firmware o una posterior, abra **Settings** en la esquina superior derecha y vaya a **System** -> **Reset Device**. Haga clic en **Reset**, confirme y espere a que el KVM se reinicie automáticamente. No desconecte la alimentación durante el restablecimiento.

![reset 1](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset1.png){class="glboxshadow"}

Si el KVM tiene la versión v1.9 del firmware o una anterior, abra **Settings** en la esquina superior izquierda y vaya a **System** -> **Reset KVM**. Haga clic en **Reset**, confirme y espere a que el KVM se reinicie automáticamente. No desconecte la alimentación durante el restablecimiento.

![reset 2](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset2.png){class="glboxshadow"}

## Después del restablecimiento {#after-the-reset}

El restablecimiento de fábrica borra los ajustes personalizados del KVM. La dirección IP local del KVM puede cambiar tras el reinicio. Vuelva a abrir la interfaz web local, siga las indicaciones de la configuración inicial para establecer una contraseña de administrador y configure de nuevo manualmente los ajustes que necesite.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
