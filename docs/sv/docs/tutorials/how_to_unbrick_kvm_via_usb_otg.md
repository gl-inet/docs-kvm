# Så återställer du en obrukbar KVM via USB OTG {#how-to-unbrick-kvm-via-usb-otg}

Den här guiden beskriver hur du återställer en obrukbar GL.iNet KVM-enhet via USB OTG. Metoden passar när KVM-enheten har blivit obrukbar och inte kan återställas via en vanlig firmwareuppdatering eller U-Boot-felsäkerhetsläget.

## Enheter som stöds {#supported-devices}

- RMQ1

## Förutsättningar {#prerequisites}

Förbered följande verktyg för att återställa enheten.

- En dator med Windows, macOS eller Ubuntu

**Obs!**

- Anslut inte RMQ1 till en nätadapter via dess USB-C-port.

- Innan du flashar firmwaren ska du säkerhetskopiera partitionen `factory` för att bevara enhetsspecifika data (som MAC-adress och certifikat). Om webbgränssnittet fortfarande är tillgängligt går du till **Toolbox** → **Terminal** → **Access** och kör följande kommando:

      ```
      dd if=/dev/mtd6 of=/userdata/media/factory.bin
      ```

      Säkerhetskopian visas under **Virtual Media** och kan laddas ned till din lokala dator.

- Koppla inte bort USB-C-kabeln mellan RMQ1 och datorn under återställningen, eftersom enheten då kan skadas.

- Om du vill att enheten ska starta om automatiskt efter flashningen går du till **Settings** → **Options** → **Reboot to Normal Mode After Download** och aktiverar alternativet innan du börjar. Om alternativet inte är aktiverat måste du starta om enheten manuellt när flashningen är klar (dvs. genom att koppla bort och återansluta strömkabeln).

## Steg för återställning {#unbrick-steps}

### Windows {#windows}

1. Ladda ned U-Boot-firmwaren för din RMQ1-enhet till datorn [här](https://dl.gl-inet.com/kvm/rmq1/stable) (välj **DOWNLOAD FOR USB OTG**).

      ![RMQ1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

2. Installera USB-drivrutinerna:

      * Ladda ned drivrutinspaketet till datorn [här](https://fw.gl-inet.com/tools/ax/Driver_V1.20.46.1.7z) och packa upp det i valfri katalog.

      * Dubbelklicka på filen `DriverSetup.exe` för att köra installationsprogrammet.

         ![Drivrutin 1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-1.png){class="glboxshadow"}

         ![Drivrutin 2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-2.png){class="glboxshadow"}

         ![Drivrutin 3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-3.png){class="glboxshadow"}

3. Installera verktyget AXDL.

      * Ladda ned AXDL till datorn [här](https://fw.gl-inet.com/tools/ax/AXDL_V1.24.22.1.7z) och packa upp det i en lättåtkomlig katalog.

      * Dubbelklicka på filen `AXDL.exe` för att köra flashverktyget.

         ![AXDL 1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-1.png){class="glboxshadow"}

4. Öppna AXDL-panelen, klicka på `load.axp` och välj den firmware som du laddade ned i steg 1 för att ladda upp den.

      ![AXDL 2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-2.png){class="glboxshadow"}

      Klicka på `Start downloading`.

      ![AXDL 3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-3.png){class="glboxshadow"}

5. Stäng av KVM-enheten. Håll in återställningsknappen (RESET) på undersidan av RMQ1 och anslut enheten till datorn med den medföljande USB-C-kabeln.

6. När `Downloading...` visas i statuskolumnen släpper du återställningsknappen.

      ![AXDL 4](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-4.png){class="glboxshadow"}

7. Vänta tills AXDL-verktyget visar `Passed`, vilket bekräftar att flashningen är klar.

      ![AXDL 5](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-5.png){class="glboxshadow"}

### macOS/Linux {#macos-linux}

Det officiella verktyget AXDL finns bara för Windows. För macOS och Linux kan du använda axdl-rs – ett inofficiellt verktyg med öppen källkod för nedladdning av Axera-avbildningar, skrivet i Rust.

1. Installera Rust-verktygskedjan via [rustup](https://rustup.rs/)

2. Ladda ned U-Boot-firmwaren för din RMQ1-enhet till datorn [här](https://dl.gl-inet.com/kvm/rmq1/stable) (välj **DOWNLOAD FOR USB OTG**).

      ![RMQ1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

3. Klona källkodsarkivet och gå till dess katalog. Steget krävs på både macOS och Linux. Kontrollera att Git är installerat och kör sedan:

      ```bash
      git clone https://github.com/gl-inet/axdl-rs.git
      cd axdl-rs
      ```

      Kör resten av kommandona i den här katalogen.

4. Installera plattformsspecifika beroenden:

      - **Linux (Debian-baserat)**

         ```
         sudo apt install -y libudev-dev libusb-1.0-0-dev
         ```
         Konfigurera udev-regler så att vanliga användare får åtkomst till enheten:

         ```
         # Kopiera udev-regelfilen till systemkatalogen
         sudo cp 99-axdl.rules /etc/udev/rules.d/

         # Läs in udev-reglerna på nytt för att tillämpa ändringarna
         sudo udevadm control --reload
         ```

         Om användaren inte finns i gruppen `plugdev` lägger du till användaren i gruppen och loggar sedan in på nytt för att ändringarna ska börja gälla.

         ```
         sudo usermod -a -G plugdev $USER
         ```

      - **macOS**

         Installera `libusb` via `brew` för att möjliggöra USB-kommunikation med KVM-enheter:

         ```
         brew install libusb
         ```

5. Bygg verktyget `axdl-cli` på valfri plattform:

      ```bash
      cargo build --bin axdl-cli --package axdl-cli
      ```

6. Ange följande kommando för att flasha firmwaren. Ersätt ` /path/to/firmware.axp ` med den faktiska sökvägen till den nedladdade firmwarefilen.

      ```
      cargo run --bin axdl-cli --package axdl-cli -- --file /path/to/firmware.axp --wait-for-device
      ```

      Verktyget visar `Waiting for device to be ready` och väntar.

7. Stäng av KVM-enheten. Håll in återställningsknappen (RESET) på undersidan av RMQ1 och anslut enheten till datorn med den medföljande USB-C-kabeln.

8. Vänta tills flashningen är klar.

      **Obs!** När flashningen är klar kanske enheten inte startar om automatiskt. Gör en manuell **strömcykling** (stäng av och slå på) av RMQ1 för att aktivera den nya firmwaren.

      **Förväntade utdata**

      Efter en lyckad flashning visar terminalen utdata enligt nedan.

      Obs! Kompilatorvarningar kan ignoreras.

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

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
