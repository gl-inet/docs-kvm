# KVM ueber USB OTG entbricken

In dieser Anleitung wird erklaert, wie Sie ein GL.iNet KVM-Geraet ueber USB OTG entbricken. Diese Methode eignet sich, wenn das KVM-Geraet gebrickt ist und nicht ueber ein normales Firmware-Update oder den U-Boot-Safe-Mode wiederhergestellt werden kann.

## Unterstuetzte Geraete

- RMQ1

## Voraussetzungen

Bereiten Sie bitte die folgenden Werkzeuge vor, um das Geraet zu entbricken.

- Ein Computer mit Windows, macOS oder Ubuntu

**Hinweis**

- Verbinden Sie den RMQ1 nicht ueber seinen USB-C-Port mit einem Netzteil.

- Sichern Sie vor dem Flashen der Firmware die Partition `factory`, um geraetespezifische Daten wie MAC-Adresse und Zertifikat zu erhalten. Wenn die Weboberflaeche weiterhin erreichbar ist, navigieren Sie bitte zu **Toolbox** -> **Terminal** -> **Access** und fuehren Sie den folgenden Befehl aus:

      ```
      dd if=/dev/mtd6 of=/userdata/media/factory.bin
      ```

      Die Sicherungsdatei erscheint unter **Virtual Media** und kann auf Ihren lokalen Computer heruntergeladen werden.

- Trennen Sie das USB-C-Kabel zwischen RMQ1 und Computer waehrend der Wiederherstellung nicht. Andernfalls kann das Geraet beschaedigt werden.

- Wenn das Geraet nach dem Flashen automatisch neu starten soll, navigieren Sie vor Beginn zu **Settings** -> **Options** -> **Reboot to Normal Mode After Download** und aktivieren Sie diese Option. Wenn diese Option nicht aktiviert ist, muessen Sie das Geraet nach Abschluss des Flashens manuell neu starten, d. h. das Stromkabel trennen und wieder anschliessen.

## Schritte zum Entbricken

### Windows

1. Laden Sie die U-Boot-Firmware fuer Ihr RMQ1-Geraet [hier](https://dl.gl-inet.com/kvm/rmq1/stable) auf Ihren Computer herunter (waehlen Sie **DOWNLOAD FOR USB OTG**).

      ![rmq1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

2. Installieren Sie die USB-Treiber:

      * Laden Sie das Treiberpaket [hier](https://fw.gl-inet.com/tools/ax/Driver_V1.20.46.1.7z) auf Ihren Computer herunter und entpacken Sie es in ein beliebiges Verzeichnis.

      * Doppelklicken Sie auf die Datei `DriverSetup.exe`, um das Installationsprogramm auszufuehren.

         ![driver-1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-1.png){class="glboxshadow"}

         ![driver-2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-2.png){class="glboxshadow"}

         ![driver-3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-3.png){class="glboxshadow"}

3. Installieren Sie das AXDL-Tool.

      * Laden Sie AXDL [hier](https://www.teambition.com/task/6a55bcdb655bb6b2abdd5def) auf Ihren Computer herunter und entpacken Sie es in ein leicht erreichbares Verzeichnis.

      * Doppelklicken Sie auf die Datei `AXDL.exe`, um das Flashing-Tool auszufuehren.

         ![axdl-1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-1.png){class="glboxshadow"}

4. Oeffnen Sie das AXDL-Fenster, klicken Sie auf `load.axp` und waehlen Sie die in Schritt 1 heruntergeladene Firmware aus, um sie zu laden.

      ![axdl-2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-2.png){class="glboxshadow"}

      Klicken Sie auf `Start downloading`.

      ![axdl-3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-3.png){class="glboxshadow"}

5. Schalten Sie Ihr KVM-Geraet aus. Halten Sie die RESET-Taste an der Unterseite des RMQ1 gedrueckt und verbinden Sie das Geraet mit dem mitgelieferten USB-C-Kabel mit Ihrem Computer.

6. Wenn in der Statusspalte `Downloading...` angezeigt wird, lassen Sie die RESET-Taste los.

      ![axdl-4](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-4.png){class="glboxshadow"}

7. Warten Sie, bis das AXDL-Tool `Passed` anzeigt. Damit wird bestaetigt, dass der Flashvorgang abgeschlossen ist.

      ![axdl-5](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-5.png){class="glboxshadow"}

### macOS / Linux

Das offizielle AXDL-Tool ist nur fuer Windows verfuegbar. Unter macOS und Linux koennen Sie axdl-rs verwenden, einen quelloffenen, inoffiziellen Axera Image Downloader in Rust.

1. Installieren Sie die Rust-Toolchain ueber [rustup](https://rustup.rs/)

2. Laden Sie die U-Boot-Firmware fuer Ihr RMQ1-Geraet [hier](https://dl.gl-inet.com/kvm/rmq1/stable) auf Ihren Computer herunter (waehlen Sie **DOWNLOAD FOR USB OTG**).

      ![rmq1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

3. Installieren Sie die plattformspezifischen Abhaengigkeiten:

      - **Linux (Debian-basiert)**

         ```
         sudo apt install -y libudev-dev libusb-1.0-0-dev
         ```
         Konfigurieren Sie udev-Regeln, damit normale Benutzer auf das Geraet zugreifen koennen:

         ```
         # Repository klonen
         git clone https://github.com/gl-inet/axdl-rs.git

         # In das Verzeichnis wechseln
         cd axdl-rs

         # udev-Regeldatei in das Systemverzeichnis kopieren
         sudo cp 99-axdl.rules /etc/udev/rules.d/

         # udev-Regeln neu laden, damit die Aenderungen wirksam werden
         sudo udevadm control --reload
         ```

         Wenn der Benutzer nicht Mitglied der Gruppe `plugdev` ist, fuegen Sie ihn bitte der Gruppe hinzu und melden Sie sich danach erneut an, damit die Aenderung wirksam wird.

         ```
         sudo usermod -a -G plugdev $USER
         ```

      - **macOS**

         Installieren Sie `libusb` ueber `brew`, um die USB-Kommunikation mit KVM-Geraeten zu ermoeglichen:

         ```
         brew install libusb
         ```

         Erstellen Sie das Tool `axdl-cli`

         ```
         cargo build --bin axdl-cli --package axdl-cli
         ```

4. Geben Sie den folgenden Befehl ein, um die Firmware zu flashen. Ersetzen Sie ` /path/to/firmware.axp ` bitte durch den tatsaechlichen Pfad zu Ihrer heruntergeladenen Firmwaredatei.

      ```
      cargo run --bin axdl-cli --package axdl-cli -- --file /path/to/firmware.axp --wait-for-device
      ```

      Das Tool zeigt `Waiting for device to be ready` an und wechselt in einen Wartezustand.

5. Schalten Sie Ihr KVM-Geraet aus. Halten Sie die RESET-Taste an der Unterseite des RMQ1 gedrueckt und verbinden Sie das Geraet mit dem mitgelieferten USB-C-Kabel mit Ihrem Computer.

6. Warten Sie, bis der Flashvorgang abgeschlossen ist.

      **Hinweis:** Nach Abschluss des Flashens startet das Geraet moeglicherweise nicht automatisch neu. Fuehren Sie beim RMQ1 manuell einen **Power Cycle** durch (aus- und wieder einschalten), um die neue Firmware zu aktivieren.

      **Erwartete Ausgabe**

      Nach einem erfolgreichen Flashvorgang zeigt das Terminal die folgende Ausgabe an.

      Hinweis: Compiler-Warnungen koennen gefahrlos ignoriert werden.

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
