# Restaurer un KVM via USB OTG {#how-to-unbrick-kvm-via-usb-otg}

Ce tutoriel explique comment restaurer un KVM GL.iNet bloqué via USB OTG. Cette méthode convient lorsque l’appareil ne peut pas être restauré par une mise à jour normale du micrologiciel ou par le mode de secours U-Boot.

## Appareils pris en charge {#supported-devices}

- RMQ1

## Prérequis {#prerequisites}

Préparez les éléments suivants pour restaurer l’appareil.

- Un ordinateur sous Windows, macOS ou Ubuntu

**Remarque**

- Ne branchez pas le RMQ1 à un adaptateur secteur via son port USB-C.

- Avant de flasher le micrologiciel, sauvegardez la partition `factory` pour conserver les données propres à l’appareil (adresse MAC, certificat, etc.). Si l’interface Web reste accessible, accédez à **Toolbox** → **Terminal** → **Access**, puis exécutez la commande suivante :

      ```
      dd if=/dev/mtd6 of=/userdata/media/factory.bin
      ```

      Le fichier de sauvegarde apparaît dans **Virtual Media** et peut être téléchargé sur votre ordinateur local.

- Ne débranchez pas le câble USB-C entre le RMQ1 et l’ordinateur pendant la restauration, sous peine d’endommager l’appareil.

- Pour que l’appareil redémarre automatiquement après le flashage, activez **Settings** → **Options** → **Reboot to Normal Mode After Download** avant de commencer. Sinon, vous devrez le redémarrer manuellement après le flashage, en débranchant puis en rebranchant le câble d’alimentation.

## Étapes de restauration {#unbrick-steps}

### Windows {#windows}

1. Téléchargez le micrologiciel U-Boot de votre RMQ1 sur votre ordinateur depuis [cette page](https://dl.gl-inet.com/kvm/rmq1/stable) (sélectionnez **DOWNLOAD FOR USB OTG**).

      ![RMQ1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

2. Installez les pilotes USB :

      * Téléchargez le paquet de pilotes sur votre ordinateur depuis [ce lien](https://fw.gl-inet.com/tools/ax/Driver_V1.20.46.1.7z) et extrayez-le dans le répertoire de votre choix.

      * Double-cliquez sur `DriverSetup.exe` pour lancer le programme d’installation.

         ![Installation du pilote 1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-1.png){class="glboxshadow"}

         ![Installation du pilote 2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-2.png){class="glboxshadow"}

         ![Installation du pilote 3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-3.png){class="glboxshadow"}

3. Installez l’outil AXDL.

      * Téléchargez AXDL sur votre ordinateur depuis [ce lien](https://fw.gl-inet.com/tools/ax/AXDL_V1.24.22.1.7z) et extrayez-le dans un répertoire facile d’accès.

      * Double-cliquez sur `AXDL.exe` pour lancer l’outil de flashage.

         ![Outil AXDL 1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-1.png){class="glboxshadow"}

4. Ouvrez le panneau AXDL, cliquez sur `load.axp`, puis sélectionnez le micrologiciel téléchargé à l’étape 1 pour le charger.

      ![Outil AXDL 2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-2.png){class="glboxshadow"}

      Cliquez sur `Start downloading`.

      ![Outil AXDL 3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-3.png){class="glboxshadow"}

5. Éteignez votre KVM. Maintenez le bouton RESET sous le RMQ1 enfoncé et connectez l’appareil à votre ordinateur avec le câble USB-C fourni.

6. Lorsque `Downloading...` apparaît dans la colonne d’état, relâchez le bouton RESET.

      ![Outil AXDL 4](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-4.png){class="glboxshadow"}

7. Attendez que l’outil AXDL affiche `Passed`, ce qui confirme la fin du flashage.

      ![Outil AXDL 5](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-5.png){class="glboxshadow"}

### macOS / Linux {#macos-linux}

L’outil officiel AXDL est réservé à Windows. Sous macOS et Linux, vous pouvez utiliser axdl-rs, un outil non officiel et open source de téléchargement d’images Axera écrit en Rust.

1. Installez la chaîne d’outils Rust avec [rustup](https://rustup.rs/).

2. Téléchargez le micrologiciel U-Boot de votre RMQ1 sur votre ordinateur depuis [cette page](https://dl.gl-inet.com/kvm/rmq1/stable) (sélectionnez **DOWNLOAD FOR USB OTG**).

      ![RMQ1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

3. Clonez le dépôt source et ouvrez son répertoire. Cette étape est nécessaire sous macOS comme sous Linux. Vérifiez que Git est installé, puis exécutez :

      ```bash
      git clone https://github.com/gl-inet/axdl-rs.git
      cd axdl-rs
      ```

      Exécutez toutes les commandes suivantes dans ce répertoire.

4. Installez les dépendances propres à votre plateforme :

      - **Linux (distributions basées sur Debian)**

         ```
         sudo apt install -y libudev-dev libusb-1.0-0-dev
         ```
         Configurez les règles udev pour permettre aux utilisateurs ordinaires d’accéder à l’appareil :

         ```
         # Copy the udev rule file to the system directory
         sudo cp 99-axdl.rules /etc/udev/rules.d/

         # Reload udev rules to apply changes
         sudo udevadm control --reload
         ```

         Si l’utilisateur n’appartient pas au groupe `plugdev`, ajoutez-le à ce groupe, puis déconnectez-vous et reconnectez-vous pour appliquer la modification.

         ```
         sudo usermod -a -G plugdev $USER
         ```

      - **macOS**

         Installez `libusb` avec `brew` pour permettre la communication USB avec les KVM :

         ```
         brew install libusb
         ```

5. Compilez l’outil `axdl-cli` sur la plateforme utilisée :

      ```bash
      cargo build --bin axdl-cli --package axdl-cli
      ```

6. Saisissez la commande suivante pour flasher le micrologiciel. Remplacez `/path/to/firmware.axp` par le chemin réel du fichier téléchargé.

      ```
      cargo run --bin axdl-cli --package axdl-cli -- --file /path/to/firmware.axp --wait-for-device
      ```

      L’outil affiche `Waiting for device to be ready` et attend la connexion de l’appareil.

7. Éteignez votre KVM. Maintenez le bouton RESET sous le RMQ1 enfoncé et connectez l’appareil à votre ordinateur avec le câble USB-C fourni.

8. Attendez la fin du flashage.

      **Remarque :** L’appareil peut ne pas redémarrer automatiquement après le flashage. **Coupez puis rétablissez son alimentation** pour activer le nouveau micrologiciel.

      **Sortie attendue**

      Après un flashage réussi, le terminal affiche la sortie ci-dessous.

      Remarque : les avertissements du compilateur peuvent être ignorés.

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

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
