# Recuperar un KVM que ha quedado inutilizable mediante U-Boot {#using-u-boot-to-unbrick-your-kvm}

Si el KVM ha quedado inutilizable por modificaciones propias o por instalar un firmware incorrecto, es posible que no arranque correctamente. En ese caso, puede reinstalar el firmware mediante el modo de recuperación de U-Boot.

## Preparación {#preparation}

Prepare un equipo de escritorio o portátil con un puerto Ethernet. Si su equipo no tiene este puerto, necesitará un adaptador USB a Ethernet adicional.

## Pasos de recuperación {#unbrick-steps}

Siga estrictamente estos pasos para evitar que falle la recuperación.

1. Descargue el firmware en su equipo desde [aquí](https://dl.gl-inet.com/kvm){target="_blank"}.

2. Desconecte la alimentación del KVM. Conecte su equipo al puerto Ethernet del KVM.

3. Mantenga pulsado firmemente el botón Reset y, **al mismo tiempo, encienda el KVM**.

    Espere a que el LED parpadee varias veces siguiendo una secuencia regular. Suelte el botón Reset **después** de que cambie el patrón de parpadeo.

    !!! note "Patrones de parpadeo del LED según el modelo"

        - **Comet (GL-RM1)**: mientras mantiene pulsado Reset, el LED azul parpadeará 5 veces. Suelte Reset después de los 5 parpadeos; el LED azul permanecerá fijo.

        - **Comet PoE (GL-RM1PE)**: mientras mantiene pulsado Reset, el LED azul parpadeará 5 veces. Suelte Reset después de los 5 parpadeos; el LED azul permanecerá fijo.

        - **Comet Pro (GL-RM10)**: mantenga pulsado Reset unos 5 segundos mientras enciende el KVM y después suelte el botón. El dispositivo entrará en el modo U-Boot.

        - **Comet 5G (GL-RM10RC)**: mantenga pulsado Reset unos 5 segundos mientras enciende el KVM y después suelte el botón. El dispositivo entrará en el modo U-Boot.

4. Establezca manualmente la dirección IP del equipo en **192.168.1.2**. Consulte los pasos correspondientes a su sistema operativo.

    ??? "Windows 7 / Windows 10"

        1. Vaya a **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Haga clic con el botón derecho en **Local Area Connection** -> **Properties**.

        3. Haga clic en **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Establezca manualmente **IP address** en `192.168.1.2`.

        5. Establezca **Subnet mask** en `255.255.255.0`.

            ![Propiedades de IPv4](https://static.gl-inet.com/docs/kvm/faq/debrick/win7_set_ip.jpg){class="glboxshadow"}

        6. Haga clic en **OK**.

    ??? "Windows 11"

        1. Abra Settings.

        2. Haga clic en **Network & Internet**.

        3. Haga clic en la pestaña **Ethernet**.

            ![Ethernet en Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet.png){class="glboxshadow"}

        4. En "IP assignment", haga clic en **Edit**.

            ![Editar IP de Ethernet en Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit1.png){class="glboxshadow"}

        5. Seleccione **Manual**.

            ![Configuración manual de IP en Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit2.png){class="glboxshadow"}

        6. Active el interruptor **IPv4**.

        7. Establezca la **IP address** estática en **192.168.1.2**.

            ![Dirección IP estática en Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit3.png){class="glboxshadow"}

        8. Establezca **Subnet mask** en **255.255.255.0**.

        9. Haga clic en **Save**.

    ??? "macOS"

        1. Haga clic en el icono de **Apple**, en la esquina superior izquierda, y seleccione **System Preferences**.

            ![Preferencias del sistema de macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences.png){class="glboxshadow"}

        2. Haga clic en **Network**.

            ![Configuración de red en macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences_network.png){class="glboxshadow"}

        4. Haga clic en **Ethernet** a la izquierda y, en el desplegable junto a **Configure IPv4**, seleccione **Manually**. Si utiliza un adaptador USB a Ethernet, puede aparecer el nombre del adaptador en lugar de Ethernet.

            ![Configuración manual de IP en macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_1.png){class="glboxshadow"}

        4. Introduzca `192.168.1.2` en **IPv4 Address**, `255.255.255.0` en **Subnet Mask** y `192.168.1.1` en **Router**; después haga clic en Apply, en la esquina inferior derecha.

            ![Dirección IP manual en macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_2.png){class="glboxshadow"}

5. Abra **http://192.168.1.1** en un navegador. Se mostrará la interfaz web de U-Boot.

    ![Interfaz web de U-Boot](https://static.gl-inet.com/docs/kvm/faq/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    **Nota:** la interfaz de U-Boot puede diferir de la imagen, ya que la versión varía según la fecha de fabricación. Por motivos de seguridad, actualmente no ofrecemos actualizaciones independientes de U-Boot. Si se necesita una actualización, se integrará en un nuevo firmware.

6. Haga clic en **Choose file** y seleccione el archivo de firmware. Después haga clic en **Update firmware**.

7. Espere unos 3 minutos. **NO desconecte la alimentación del KVM durante la actualización.**

    El KVM estará listo cuando el LED **parpadee en blanco**.

8. Restablezca la configuración IP del equipo que modificó en el paso 4.

9. Desconecte el cable Ethernet entre el equipo y el KVM. Después conecte el KVM a una red, por ejemplo a un router o un conmutador de red, mediante ese cable Ethernet o por Wi-Fi.

    Espere aproximadamente 1 minuto para que el KVM obtenga acceso a Internet. Después podrá volver a acceder a él.

    **Nota:** normalmente se conserva la configuración. Sin embargo, se restablecerá a los valores predeterminados si un error de configuración provocó el fallo del sistema que hizo necesaria la recuperación.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
