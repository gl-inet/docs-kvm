# ¿Qué debo hacer si aparece "Press Failed" al usar Fingerbot? {#what-should-i-do-if-i-see-press-failed-when-using-fingerbot}

Si la consola KVM muestra "Press Failed" al usar Fingerbot, puede haber un problema de emparejamiento entre Fingerbot y su dispositivo KVM.

Siga los pasos siguientes para eliminar el emparejamiento existente y volver a emparejar Fingerbot.

1. Inicie sesión en su KVM y vaya a **Toolbox** -> **Terminal** -> **Access Terminal** para abrir el terminal.

2. Ejecute los siguientes comandos en orden:

    ```
    bluetoothctl
    ```
    ```
    scan on
    ```

    ![open bluetoothctl](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/bluetoothctl.png){class="glboxshadow"}

    Espere un momento y ejecute `scan off` para detener la búsqueda.

3. Ejecute `devices` para ver todos los dispositivos Bluetooth detectados. Busque su Fingerbot (que aparece como FGB) y anote su dirección MAC.

    ![devices](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/devices.png){class="glboxshadow"}

4. Introduzca `exit` para salir de la sesión de bluetoothctl. A continuación, ejecute el siguiente comando para eliminar el registro de emparejamiento anterior. Sustituya esta dirección MAC por la dirección MAC real de su Fingerbot.

    ```
    bluetoothctl remove E1:2D:B2:75:D5:BC
    ```

5. Vuelva a emparejar Fingerbot con el siguiente comando. Sustituya esta dirección MAC por la dirección MAC real de su Fingerbot.

    ```
    fingerbot pair E1:2D:B2:75:D5:BC
    ```

    ![repair fingerbot](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/repair.png){class="glboxshadow"}

    Si la operación se realiza correctamente, verá **Done** en el terminal. Después, intente usar Fingerbot de nuevo.

6. Si el problema persiste, póngase en contacto con nosotros en [support@gl-inet.com](mailto:support@gl-inet.com) y proporcione la siguiente información para continuar con el diagnóstico.

    - La salida de los siguientes comandos:

        ```
        fingerbot action
        ```
        ```
        ls -l /
        ```

    - Los registros más recientes del KVM, exportados desde **Help** > **Export Log Files**.

        ![export logs](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/export_logs.png){class="glboxshadow"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
