# Een gebrickte KVM herstellen via USB OTG {#how-to-unbrick-kvm-via-usb-otg}

In deze handleiding leest u hoe u een gebrickt GL.iNet KVM-apparaat herstelt via USB OTG. Deze methode is geschikt voor situaties waarin het KVM-apparaat gebrickt is en niet kan worden hersteld via een gewone firmware-update of de U-Boot-veilige modus.

## Ondersteunde apparaten {#supported-devices}

- RMQ1

## Vereisten {#prerequisites}

Zorg voor de volgende hulpmiddelen om het apparaat te herstellen.

- Een computer met Windows, macOS of Ubuntu

**Opmerking**

- Sluit de RMQ1 niet via de USB-C-poort aan op een voedingsadapter.
  
- Maak vóór het flashen van de firmware een back-up van de partitie `factory` om apparaatspecifieke gegevens (zoals het MAC-adres en het certificaat) te behouden. Als de webinterface nog toegankelijk is, gaat u naar **Toolbox** → **Terminal** → **Access** en voert u de volgende opdracht uit:

      ```
      dd if=/dev/mtd6 of=/userdata/media/factory.bin
      ```
      
      Het back-upbestand verschijnt in **Virtual Media** en kan naar uw lokale computer worden gedownload.

- Koppel de USB-C-kabel tussen de RMQ1 en de computer niet los tijdens het herstel, anders kan het apparaat beschadigd raken.
  
- Als u wilt dat het apparaat na het flashen automatisch opnieuw opstart, gaat u vóór het begin naar **Settings** → **Options** → **Reboot to Normal Mode After Download** en schakelt u deze optie in. Als deze optie niet is ingeschakeld, moet u het apparaat na het flashen handmatig opnieuw opstarten (door de voedingskabel los te koppelen en weer aan te sluiten).

## Stappen voor herstel {#unbrick-steps}

### Windows {#windows}

1. Download de U-Boot-firmware voor uw RMQ1 [hier](https://dl.gl-inet.com/kvm/rmq1/stable) naar uw computer (selecteer **DOWNLOAD FOR USB OTG**).

      ![RMQ1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

2. Installeer de USB-stuurprogramma's:

      * Download het stuurprogrammapakket [hier](https://fw.gl-inet.com/tools/ax/Driver_V1.20.46.1.7z) naar uw computer en pak het uit in een willekeurige map.
      
      * Dubbelklik op het bestand `DriverSetup.exe` om het installatieprogramma uit te voeren.

         ![Stuurprogramma 1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-1.png){class="glboxshadow"}

         ![Stuurprogramma 2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-2.png){class="glboxshadow"}

         ![Stuurprogramma 3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-3.png){class="glboxshadow"}

3. Installeer de AXDL-tool.
  
      * Download AXDL [hier](https://fw.gl-inet.com/tools/ax/AXDL_V1.24.22.1.7z) naar uw computer en pak het uit in een gemakkelijk bereikbare map.
         
      * Dubbelklik op het bestand `AXDL.exe` om de flashtool te starten.

         ![AXDL 1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-1.png){class="glboxshadow"}

4. Open het AXDL-venster, klik op `load.axp` en selecteer de firmware die u in stap 1 hebt gedownload om deze te uploaden.
   
      ![AXDL 2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-2.png){class="glboxshadow"}

      Klik op `Start downloading`.

      ![AXDL 3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-3.png){class="glboxshadow"}

5. Schakel uw KVM-apparaat uit. Houd de RESET-knop aan de onderkant van de RMQ1 ingedrukt en sluit het apparaat met de meegeleverde USB-C-kabel aan op uw computer.

6. Laat de RESET-knop los zodra in de statuskolom `Downloading...` verschijnt.

      ![AXDL 4](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-4.png){class="glboxshadow"}

7. Wacht tot de AXDL-tool `Passed` toont als bevestiging dat het flashen is voltooid.

      ![AXDL 5](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-5.png){class="glboxshadow"}

### macOS / Linux {#macos-linux}

De officiële AXDL-tool is alleen beschikbaar voor Windows. Voor macOS en Linux kunt u axdl-rs gebruiken, een niet-officiële opensource-downloader voor Axera-images, geschreven in Rust.

1. Installeer de Rust-toolchain via [rustup](https://rustup.rs/)

2. Download de U-Boot-firmware voor uw RMQ1 [hier](https://dl.gl-inet.com/kvm/rmq1/stable) naar uw computer (selecteer **DOWNLOAD FOR USB OTG**).

      ![RMQ1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

3. Kloon de bronrepository en ga naar de map ervan. Deze stap is zowel op macOS als op Linux vereist. Zorg ervoor dat Git is geïnstalleerd en voer het volgende uit:

      ```bash
      git clone https://github.com/gl-inet/axdl-rs.git
      cd axdl-rs
      ```

      Voer de overige opdrachten in deze map uit.

4. Installeer de platformspecifieke afhankelijkheden:
  
      - **Linux (op Debian gebaseerd)**

         ```
         sudo apt install -y libudev-dev libusb-1.0-0-dev
         ```
         Configureer udev-regels zodat gewone gebruikers toegang hebben tot het apparaat:

         ```
         # Kopieer het udev-regelbestand naar de systeemmap
         sudo cp 99-axdl.rules /etc/udev/rules.d/

         # Laad de udev-regels opnieuw om de wijzigingen toe te passen
         sudo udevadm control --reload
         ```

         Als de gebruiker niet in de groep `plugdev` zit, voegt u deze aan de groep toe en meldt u zich daarna opnieuw aan zodat de wijzigingen van kracht worden.

         ```
         sudo usermod -a -G plugdev $USER
         ```

      - **macOS**

         Installeer `libusb` via `brew` om USB-communicatie met KVM-apparaten mogelijk te maken:

         ```
         brew install libusb
         ```

5. Bouw de tool `axdl-cli` op een van beide platforms:

      ```bash
      cargo build --bin axdl-cli --package axdl-cli
      ```

6. Voer de volgende opdracht in om de firmware te flashen. Vervang ` /path/to/firmware.axp ` door het werkelijke pad naar het gedownloade firmwarebestand.

      ```
      cargo run --bin axdl-cli --package axdl-cli -- --file /path/to/firmware.axp --wait-for-device
      ```

      De tool toont `Waiting for device to be ready` en gaat wachten.

7. Schakel uw KVM-apparaat uit. Houd de RESET-knop aan de onderkant van de RMQ1 ingedrukt en sluit het apparaat met de meegeleverde USB-C-kabel aan op uw computer.
  
8. Wacht tot het flashen is voltooid.

      **Opmerking:** Na het flashen start het apparaat mogelijk niet automatisch opnieuw op. Schakel de RMQ1 handmatig uit en weer in (**power cycle**) om de nieuwe firmware te activeren.

      **Verwachte uitvoer**

      Na een geslaagde flash toont de terminal de onderstaande uitvoer.

      Opmerking: compilerwaarschuwingen kunnen veilig worden genegeerd

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

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
