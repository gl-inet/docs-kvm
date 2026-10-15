# Qué hacer si el modo de ratón relativo no funciona en un NVR Reolink {#what-should-i-do-if-relative-mouse-mode-doesnt-work-on-reolink-nvr}

Al controlar un NVR Reolink mediante un KVM GL.iNet, especialmente si el modelo no admite dos ratones, o determinados equipos antiguos, como los que no tienen puertos USB, el modo de ratón relativo puede no funcionar. Puede fallar por completo o permitir mover el cursor sin que respondan los clics.

Esto se debe principalmente a la incompatibilidad entre la emulación de ratón del KVM y las capacidades limitadas de dispositivos como los NVR Reolink:

- **Antes del firmware v1.4.0**: el KVM emulaba un solo ratón. Era necesario reiniciar el KVM para cambiar entre los modos relativo y absoluto, pero funcionaba correctamente con la mayoría de los dispositivos antiguos o especializados.

- **Después del firmware v1.4.0**: para cambiar de modo sin reiniciar, se modificó el comportamiento predeterminado para emular dos ratones a la vez, uno relativo y otro absoluto. Los NVR Reolink y algunos equipos antiguos no admiten dos ratones, lo que puede provocar estos problemas:

    - El modo de ratón relativo no funciona en absoluto.
    - El cursor se mueve, pero los clics no responden.

Puede resolverlo forzando el modo de ratón relativo desde el terminal. Siga estos pasos:

1. Acceda a la consola KVM y vaya a **Toolbox** -> **Terminal**. Haga clic en **Access** para abrir el terminal del KVM.

2. Abra el archivo de configuración con este comando:

    `vi /etc/kvmd/override.yaml`

3. Utilice la siguiente configuración para forzar el modo de ratón relativo:

    ```
    kvmd:
        hid:
            mouse:
                absolute: false
    ```

4. Guarde el archivo y salga del editor.

5. Reinicie el KVM para aplicar los cambios.

!!! note "Nota"

    1. Si este método no funciona, pruebe a volver a una versión del firmware anterior a v1.4, si está disponible, que emule un solo ratón y sea compatible con dispositivos antiguos.

    2. La aplicación independiente GLKVM para Mac OS no admite el modo de ratón relativo debido a limitaciones del motor del navegador, que no dispone de la API requestPointerLock. Utilice la consola web.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
