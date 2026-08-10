# KVM ueber USB OTG entbricken

## Unterstuetzte Geraete

- RMQ1

## Voraussetzungen

- Ein Windows-PC / macOS / Ubuntu

- RMQ1-Geraet

- `.axp`-Firmwaredatei - laden Sie die neueste Firmware von der [offiziellen Firmware-Seite](https://dl.gl-inet.com/kvm/rmq1/beta) herunter; suchen Sie nach der Datei mit der Kennzeichnung **DOWNLOAD FOR USB OTG**

  ![rmq1-usbotg](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

> **Wichtig:** Sichern Sie vor dem Flashen die Partition `factory`, um geraetespezifische Daten wie MAC-Adresse und Zertifikatsdaten zu erhalten. Wenn das Geraet noch ueber die Weboberflaeche erreichbar ist, gehen Sie zu **Toolbox** -> **Terminal** -> **Access** und fuehren Sie dann aus:
>
> ```bash
> dd if=/dev/mtd6 of=/userdata/media/factory.bin
> ```
>
> Die Sicherungsdatei erscheint unter **Virtual Media** und kann auf Ihren lokalen Computer heruntergeladen werden.

## Windows

### Installation

1. **USB-Treiber installieren**

    Entpacken und installieren Sie den Treiber aus `Driver_V1.20.46.1.7z`.

    ![driver-1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-1.png){class="glboxshadow"}

    ![driver-2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-2.png){class="glboxshadow"}

    ![driver-3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-3.png){class="glboxshadow"}

2. **Flashing-Tool starten**

    Entpacken Sie das Flashing-Tool aus `AXDL_V1.24.22.1.7z` und starten Sie `AXDL.exe`.

    ![axdl-1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-1.png){class="glboxshadow"}

    > **Optional:** Wenn das Geraet nach dem Flashen automatisch neu starten soll, gehen Sie vor dem Start zu **Settings** -> **Options** und aktivieren Sie **Reboot to normal after download**. Wenn diese Option nicht aktiviert ist, muessen Sie das Geraet nach Abschluss des Flashens manuell aus- und wieder einschalten (Stromkabel trennen und erneut anschliessen).

### Flashen

1. **Firmware laden**

    Klicken Sie auf **Load .axp**, um die `.axp`-Firmwaredatei auszuwaehlen und zu laden, und klicken Sie dann auf **Start downloading**.

    ![axdl-2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-2.png){class="glboxshadow"}

    ![axdl-3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-3.png){class="glboxshadow"}

2. **Geraet im Flashing-Modus verbinden**

    - Verbinden Sie den RMQ1 **nicht** ueber seinen USB-C-Port mit einem Netzteil.
    - Halten Sie die **RESET-Taste** an der Unterseite des RMQ1 gedrueckt.
    - Verbinden Sie den RMQ1 waehrenddessen per USB-C-Kabel mit Ihrem PC.
    - Das Flashing-Tool erkennt das Geraet automatisch und startet den Flashvorgang. Sobald das Tool den Fortschritt des Flashens anzeigt, koennen Sie die **RESET-Taste loslassen**.

    ![axdl-4](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-4.png){class="glboxshadow"}

## macOS / Linux

Das offizielle AXDL-Tool ist nur fuer Windows verfuegbar. Alternativ koennen Sie das Open-Source-Tool [axdl-rs](https://github.com/ciniml/axdl-rs) verwenden, einen inoffiziellen Axera Image Downloader in Rust.

### Installation

- Rust-Toolchain - Installation ueber [rustup](https://rustup.rs/)

- `.axp`-Firmwaredatei - laden Sie die neueste Firmware von der [offiziellen Firmware-Seite](https://dl.gl-inet.com/kvm/rmq1/beta) herunter; suchen Sie nach der Datei mit der Kennzeichnung **DOWNLOAD FOR USB OTG**

- Plattformspezifische Abhaengigkeiten:

  **Linux (Debian-basiert):**

  ```bash
  sudo apt install -y libudev-dev libusb-1.0-0-dev
  ```

  Konfigurieren Sie udev-Regeln, um Zugriff auf das Geraet ohne Root-Rechte zu erlauben:

  ```bash
  git clone https://github.com/gl-inet/axdl-rs.git
  cd axdl-rs
  sudo cp 99-axdl.rules /etc/udev/rules.d/
  sudo udevadm control --reload
  ```

  Wenn Ihr Benutzer nicht Mitglied der Gruppe `plugdev` ist, fuegen Sie ihn hinzu und melden Sie sich erneut an:

  ```bash
  sudo usermod -a -G plugdev $USER
  ```

  **macOS:**

  ```
  brew install libusb
  ```

  **Build:**

  ```bash
  cargo build --bin axdl-cli --package axdl-cli
  ```

### Flashen

1. Fuehren Sie den Flashing-Befehl aus. Verwenden Sie dabei den Pfad zu Ihrer heruntergeladenen `.axp`-Datei:

   ```bash
   cargo run --bin axdl-cli --package axdl-cli -- --file /path/to/firmware.axp --wait-for-device
   ```

   Das Tool zeigt `Waiting for the device to be ready` an und wartet.

2. **Geraet im Flashing-Modus verbinden**

   - Verbinden Sie den RMQ1 **nicht** mit einem Netzteil.
   - Halten Sie die **RESET-Taste** an der Unterseite des RMQ1 gedrueckt.
   - Verbinden Sie den RMQ1 waehrenddessen per USB-C-Kabel mit Ihrem PC.
   - Sobald das Tool den Fortschritt des Flashens anzeigt, koennen Sie die **RESET-Taste loslassen**.

3. Nach Abschluss des Flashens startet das Geraet moeglicherweise nicht automatisch neu. Schalten Sie den RMQ1 manuell aus und wieder ein (Stromkabel trennen und erneut anschliessen), damit er mit der neuen Firmware startet.

**Erwartete Ausgabe**

Ein erfolgreicher Flashvorgang sieht wie folgt aus (Compiler-Warnungen koennen ignoriert werden):

<details>
<summary>Beispielprotokoll</summary>

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

</details>
