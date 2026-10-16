# Come ripristinare il KVM tramite USB OTG

Questo tutorial spiega come ripristinare un dispositivo KVM GL.iNet tramite USB OTG. Questo metodo è adatto ai casi in cui il KVM è bloccato e non può essere ripristinato con un normale aggiornamento del firmware o con la modalità di ripristino U-Boot.

## Dispositivi supportati

- RMQ1

## Prerequisiti

Prepara i seguenti strumenti per ripristinare il dispositivo.

- Un computer con Windows, macOS o Ubuntu

**Nota**

- Non collegare RMQ1 a un alimentatore tramite la sua porta USB-C.

- Prima di scrivere il firmware, esegui il backup della partizione `factory` per conservare i dati specifici del dispositivo (come indirizzo MAC e certificato). Se l'interfaccia web è ancora accessibile, vai su **Toolbox** → **Terminal** → **Access** ed esegui il seguente comando:

      ```
      dd if=/dev/mtd6 of=/userdata/media/factory.bin
      ```

      Il file di backup comparirà in **Virtual Media** e potrà essere scaricato sul computer locale.

- Non scollegare il cavo USB-C tra RMQ1 e il computer durante il ripristino; in caso contrario, il dispositivo potrebbe danneggiarsi.

- Se desideri che il dispositivo si riavvii automaticamente dopo la scrittura del firmware, vai su **Settings** → **Options** → **Reboot to Normal Mode After Download** e attiva l'opzione prima di iniziare. Se l'opzione non è attiva, dovrai riavviare manualmente il dispositivo al termine della scrittura, scollegando e ricollegando il cavo di alimentazione.

## Procedura di ripristino

### Windows

1. Scarica sul computer il firmware U-Boot per RMQ1 da [questa pagina](https://dl.gl-inet.com/kvm/rmq1/stable) (seleziona **DOWNLOAD FOR USB OTG**).

      ![rmq1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

2. Installa i driver USB:

      * Scarica sul computer il pacchetto dei driver da [questo link](https://fw.gl-inet.com/tools/ax/Driver_V1.20.46.1.7z) ed estrailo in una cartella a scelta.

      * Fai doppio clic sul file `DriverSetup.exe` per avviare il programma di installazione.

         ![driver-1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-1.png){class="glboxshadow"}

         ![driver-2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-2.png){class="glboxshadow"}

         ![driver-3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-3.png){class="glboxshadow"}

3. Installa lo strumento AXDL.

      * Scarica AXDL sul computer da [questo link](https://fw.gl-inet.com/tools/ax/AXDL_V1.24.22.1.7z) ed estrailo in una cartella facilmente accessibile.

      * Fai doppio clic sul file `AXDL.exe` per avviare lo strumento di scrittura del firmware.

         ![axdl-1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-1.png){class="glboxshadow"}

4. Apri il pannello di AXDL, fai clic su `load.axp` e seleziona il firmware scaricato al passaggio 1 per caricarlo.

      ![axdl-2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-2.png){class="glboxshadow"}

      Fai clic su `Start downloading`.

      ![axdl-3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-3.png){class="glboxshadow"}

5. Spegni il dispositivo KVM. Tieni premuto il pulsante RESET sul fondo di RMQ1 e collega il dispositivo al computer con il cavo USB-C incluso.

6. Quando compare `Downloading...` nella colonna di stato, rilascia il pulsante RESET.

      ![axdl-4](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-4.png){class="glboxshadow"}

7. Attendi che lo strumento AXDL mostri `Passed` per confermare il completamento della scrittura del firmware.

      ![axdl-5](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-5.png){class="glboxshadow"}

### macOS / Linux

Lo strumento AXDL ufficiale è disponibile solo per Windows. Su macOS e Linux puoi utilizzare axdl-rs, uno strumento non ufficiale e open source per il caricamento delle immagini Axera, scritto in Rust.

1. Installa la toolchain Rust tramite [rustup](https://rustup.rs/)

2. Scarica sul computer il firmware U-Boot per RMQ1 da [questa pagina](https://dl.gl-inet.com/kvm/rmq1/stable) (seleziona **DOWNLOAD FOR USB OTG**).

      ![rmq1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

3. Clona il repository del codice sorgente e accedi alla relativa cartella. Questo passaggio è necessario sia su macOS sia su Linux. Assicurati che Git sia installato, quindi esegui:

      ```bash
      git clone https://github.com/gl-inet/axdl-rs.git
      cd axdl-rs
      ```

      Esegui i comandi rimanenti da questa cartella.

4. Installa le dipendenze specifiche della piattaforma:

      - **Linux (basato su Debian)**

         ```
         sudo apt install -y libudev-dev libusb-1.0-0-dev
         ```
         Configura le regole udev per consentire agli utenti normali di accedere al dispositivo:

         ```
         # Copy the udev rule file to the system directory
         sudo cp 99-axdl.rules /etc/udev/rules.d/

         # Reload udev rules to apply changes
         sudo udevadm control --reload
         ```

         Se l'utente non appartiene al gruppo `plugdev`, aggiungilo al gruppo ed esegui nuovamente l'accesso affinché le modifiche abbiano effetto.

         ```
         sudo usermod -a -G plugdev $USER
         ```

      - **macOS**

         Installa `libusb` tramite `brew` per abilitare la comunicazione USB con i dispositivi KVM:

         ```
         brew install libusb
         ```

5. Compila lo strumento `axdl-cli` sulla piattaforma utilizzata:

      ```bash
      cargo build --bin axdl-cli --package axdl-cli
      ```

6. Inserisci il comando seguente per scrivere il firmware. Sostituisci ` /path/to/firmware.axp ` con il percorso effettivo del file del firmware scaricato.

      ```
      cargo run --bin axdl-cli --package axdl-cli -- --file /path/to/firmware.axp --wait-for-device
      ```

      Lo strumento mostrerà `Waiting for device to be ready` ed entrerà in attesa.

7. Spegni il dispositivo KVM. Tieni premuto il pulsante RESET sul fondo di RMQ1 e collega il dispositivo al computer con il cavo USB-C incluso.

8. Attendi il completamento della scrittura del firmware.

      **Nota:** al termine della scrittura, il dispositivo potrebbe non riavviarsi automaticamente. **Spegni e riaccendi** manualmente RMQ1 per attivare il nuovo firmware.

      **Output previsto**

      Dopo una scrittura riuscita, il terminale mostrerà l'output riportato di seguito.

      Nota: gli avvisi del compilatore possono essere ignorati.

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

Hai ancora domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
