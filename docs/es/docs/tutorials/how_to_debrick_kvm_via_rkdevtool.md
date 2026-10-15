# Cómo recuperar un KVM que ha quedado inutilizable mediante RKDevTool {#how-to-unbrick-kvm-via-rkdevtool}

Este tutorial explica cómo recuperar un KVM GL.iNet que ha quedado inutilizable mediante RKDevTool cuando no se puede recuperar con una actualización normal de firmware ni con el modo de recuperación de U-Boot.

## Preparación {#preparation}

Prepare lo siguiente:

- Un equipo Windows.
- Un cable USB de datos.
- Un adaptador de corriente para el KVM.

!!! Note "Nota"

    NO desconecte el cable USB ni apague el KVM durante la recuperación, ya que podría dañar el dispositivo.

    Se recomienda hacer una copia de seguridad de los datos importantes antes de comenzar.

## Pasos de recuperación {#unbrick-steps}

Siga los pasos en orden para evitar que falle la recuperación.

1. Apague el KVM.

2. Descargue el firmware más reciente de su KVM en el equipo desde [aquí](https://dl.gl-inet.com/kvm){target="_blank"}.

3. Descargue el paquete de controladores desde [aquí](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/DriverAssitant_v5.11.zip) y extráigalo en cualquier carpeta del equipo.

4. Haga doble clic en el archivo .exe para completar la instalación del controlador.

    ![Instalar el controlador](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_1.png){class="glboxshadow"}

    ![Instalación del controlador](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_2.png){class="glboxshadow"}

5. Descargue **RKDevTool** desde [aquí](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/RKDevTool_Release_v3.37.zip) y extráigalo en una carpeta de fácil acceso.

6. Haga doble clic en el archivo .exe para ejecutar la herramienta de instalación de firmware.

    ![Ejecutar RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_1.png){class="glboxshadow"}

    ![Ventana de RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_2.png){class="glboxshadow"}

7. Conecte el puerto Type-C OTG del KVM al puerto USB del equipo mediante un cable USB de datos.

    En Comet (GL-RM1), el puerto Type-C OTG es el que se muestra a continuación.

    ![Conectar el cable USB](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/otg-port-rm1.png){class="glboxshadow gl-60-desktop"}

8. Mantenga pulsado RESET durante **10 segundos** mientras conecta el cable de alimentación al KVM. Después suelte el botón. El KVM entrará en modo Loader.

    ![Botón Reset](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/reset_button_rm1.jpg){class="glboxshadow" width="433"}

9. En RKDevTool, vaya a **Upgrade Firmware** -> **Firmware** y seleccione el firmware descargado en el paso 2.

    ![Seleccionar el firmware](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/select_firmware.png){class="glboxshadow"}

    Después vaya a **Upgrade**, junto a Firmware. Aparecerá "Found Loader Device" y comenzará la instalación del firmware.

    ![Panel de RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/rkdevtool_panel.jpg){class="glboxshadow"}

    El KVM se reiniciará automáticamente al finalizar la actualización.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
