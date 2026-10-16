# Cómo recuperar un KVM que ha quedado inutilizable mediante USB OTG {#how-to-unbrick-kvm-via-usb-otg}

Este tutorial explica cómo recuperar un KVM GL.iNet que ha quedado inutilizable mediante USB OTG cuando no se puede restaurar con una actualización normal de firmware ni con el modo de recuperación de U-Boot.

## Dispositivos compatibles {#supported-devices}

- RMQ1

## Requisitos previos {#prerequisites}

Prepare lo siguiente para recuperar el dispositivo.

- Un equipo con Windows, macOS o Ubuntu.

**Nota**

- No conecte el RMQ1 a un adaptador de corriente mediante su puerto USB-C.

- Antes de instalar el firmware, haga una copia de seguridad de la partición `factory` para conservar los datos específicos del dispositivo, como la dirección MAC y el certificado. Si todavía puede acceder a la interfaz web, vaya a **Toolbox** → **Terminal** → **Access** y ejecute:

      ```
      dd if=/dev/mtd6 of=/userdata/media/factory.bin
      ```

      El archivo de copia de seguridad aparecerá en **Virtual Media** y podrá descargarlo en su equipo local.

- No desconecte el cable USB-C entre el RMQ1 y el equipo durante la recuperación, ya que podría dañar el dispositivo.

- Si desea que el dispositivo se reinicie automáticamente después de instalar el firmware, vaya a **Settings** → **Options** → **Reboot to Normal Mode After Download** y active la opción antes de comenzar. Si no la activa, deberá reiniciar el dispositivo manualmente al terminar, desconectando y volviendo a conectar la alimentación.

## Pasos de recuperación {#unbrick-steps}

### Windows {#windows}

1. Descargue el firmware U-Boot para su RMQ1 desde [aquí](https://dl.gl-inet.com/kvm/rmq1/stable) y seleccione **DOWNLOAD FOR USB OTG**.

      ![RMQ1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

2. Instale los controladores USB:

      * Descargue el paquete de controladores desde [aquí](https://fw.gl-inet.com/tools/ax/Driver_V1.20.46.1.7z) y extráigalo en cualquier carpeta del equipo.

      * Haga doble clic en `DriverSetup.exe` para ejecutar el instalador.

         ![Instalador del controlador](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-1.png){class="glboxshadow"}

         ![Instalación del controlador](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-2.png){class="glboxshadow"}

         ![Controlador instalado](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-3.png){class="glboxshadow"}

3. Instale AXDL Tool.

      * Descargue AXDL desde [aquí](https://fw.gl-inet.com/tools/ax/AXDL_V1.24.22.1.7z) y extráigalo en una carpeta de fácil acceso.

      * Haga doble clic en `AXDL.exe` para ejecutar la herramienta de instalación de firmware.

         ![Herramienta AXDL](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-1.png){class="glboxshadow"}

4. En el panel de AXDL, haga clic en `load.axp` y seleccione el firmware descargado en el paso 1.

      ![Cargar el firmware en AXDL](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-2.png){class="glboxshadow"}

      Haga clic en `Start downloading`.

      ![Iniciar la instalación](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-3.png){class="glboxshadow"}

5. Apague el KVM. Mantenga pulsado RESET, en la parte inferior del RMQ1, y conecte el dispositivo al equipo con el cable USB-C incluido.

6. Cuando aparezca `Downloading...` en la columna de estado, suelte RESET.

      ![Instalación en curso](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-4.png){class="glboxshadow"}

7. Espere a que AXDL muestre `Passed`, que confirma que la instalación ha finalizado.

      ![Instalación finalizada](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-5.png){class="glboxshadow"}

### macOS / Linux {#macos-linux}

La herramienta oficial AXDL solo está disponible para Windows. En macOS y Linux puede utilizar axdl-rs, una herramienta no oficial de código abierto escrita en Rust para descargar imágenes a dispositivos Axera.

1. Instale las herramientas de Rust mediante [rustup](https://rustup.rs/).

2. Descargue el firmware U-Boot para su RMQ1 desde [aquí](https://dl.gl-inet.com/kvm/rmq1/stable) y seleccione **DOWNLOAD FOR USB OTG**.

      ![RMQ1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

3. Clone el repositorio de código fuente y acceda a su directorio. Este paso es necesario tanto en macOS como en Linux. Compruebe que Git está instalado y ejecute:

      ```bash
      git clone https://github.com/gl-inet/axdl-rs.git
      cd axdl-rs
      ```

      Ejecute los comandos restantes en este directorio.

4. Instale las dependencias de su plataforma:

      - **Linux basado en Debian**

         ```
         sudo apt install -y libudev-dev libusb-1.0-0-dev
         ```
         Configure las reglas udev para que los usuarios normales puedan acceder al dispositivo:

         ```
         # Copy the udev rule file to the system directory
         sudo cp 99-axdl.rules /etc/udev/rules.d/

         # Reload udev rules to apply changes
         sudo udevadm control --reload
         ```

         Si el usuario no pertenece al grupo `plugdev`, añádalo al grupo y vuelva a iniciar sesión para aplicar el cambio.

         ```
         sudo usermod -a -G plugdev $USER
         ```

      - **macOS**

         Instale `libusb` mediante `brew` para permitir la comunicación USB con los KVM:

         ```
         brew install libusb
         ```

5. Compile la herramienta `axdl-cli` en cualquiera de las dos plataformas:

      ```bash
      cargo build --bin axdl-cli --package axdl-cli
      ```

6. Ejecute este comando para instalar el firmware. Sustituya ` /path/to/firmware.axp ` por la ruta real del archivo descargado.

      ```
      cargo run --bin axdl-cli --package axdl-cli -- --file /path/to/firmware.axp --wait-for-device
      ```

      La herramienta mostrará `Waiting for device to be ready` y quedará a la espera.

7. Apague el KVM. Mantenga pulsado RESET, en la parte inferior del RMQ1, y conecte el dispositivo al equipo con el cable USB-C incluido.

8. Espere a que finalice la instalación.

      **Nota:** el dispositivo puede no reiniciarse automáticamente. **Desconecte y vuelva a conectar la alimentación** del RMQ1 para activar el nuevo firmware.

      **Salida esperada**

      Si la instalación finaliza correctamente, el terminal mostrará la siguiente salida.

      Nota: las advertencias del compilador pueden ignorarse.

      ```
      $ cargo run --bin axdl-cli --package axdl-cli -- --file glkvm-RMQ1-nand-1.8.1-0518-1779101289.axp --wait-for-device
      warning: `axdl` (lib) generated 6 warnings
         Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.07s
         Running `target/debug/axdl-cli --file glkvm-RMQ1-nand-1.8.1-0518-1779101289.axp --wait-for-device`
      Waiting for the device to be ready
      Loading the AXP image configuration
      Start download
      Handshaking with the device
      Downloading the flash downloaders
      [00:00:03] [############################################################################]
      Downloading the partition table
      Skipping partition: FACTORY (excluded by default)
      Downloading image DDRINIT
      Downloading image UBOOT
      Downloading image LOGO
      Downloading image DTB
      Downloading image KERNEL
      Downloading image RECOVERY
      Downloading image MEDIA
      Downloading image ROOTFS
      [00:00:26] [############################################################################]
      Downloading image SPL
      Done
      ```

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
