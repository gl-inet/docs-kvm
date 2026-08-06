# How to unbrick KVM via USB OTG

This tutorial explains how to unbrick a GL.iNet KVM device using USB OTG. This method is suitable for situations where the KVM device is bricked and cannot be restored via a standard firmware update or U-Boot safe mode.

## Supported devices

- RMQ1

## Prerequisites

Please prepare the following tools to unbrick the device.

- A Windows running Windows, macOS or Ubuntu

**Note**

- Do not connect the RMQ1 to a power adapter via its USB-C port.
  
- Before flashing the firmware, back up the `factory` partition to preserve device-specific data (such as the MAC address and certificate). If the Web UI remains accessible, please navigate to **Toolbox** → **Terminal** → **Access**, and run the following command:

```
dd if=/dev/mtd6 of=/userdata/media/factory.bin
```

<<<<<<< HEAD
The backup file will appear in **Virtual Media** and can be downloaded to your local computer.

- Do not disconnect the USB-C cable between the RMQ1 and the computer during the recovery process; otherwise, the device may be damaged.
=======
## Windows

### Install

1. **Install the USB driver**
   
   Extract and install the driver from `Driver_V1.20.46.1.7z`.
   
   ![driver-1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-1.png){class="glboxshadow"}
   
   ![driver-2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-2.png){class="glboxshadow"}

   ![driver-3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-3.png){class="glboxshadow"}

2. **Launch the flashing tool**
   
   Extract the flashing utility from `AXDL_V1.24.22.1.7z` and run `AXDL.exe`. 
   
   ![axdl-1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-1.png){class="glboxshadow"}
   
   > **Optional:** To have the device automatically reboot after flashing, go to **Settings** → **Options** → enable **Reboot to normal after download** before starting. If this option is not enabled, you will need to power cycle the device manually after flashing completes (disconnect and reconnect the power cable).

### Flashing

1. **Load the firmware**
   
   Click **Load .axp** to select and load the `.axp` firmware file, then click **Start downloading**.     
   
   ![axdl-2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-2.png){class="glboxshadow"}
   
   ![axdl-3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-3.png){class="glboxshadow"}

2. **Connect the device in flashing mode**
   
   - **Do not** connect the RMQ1 to a power adapter via its USB-C port.
   - Press and **hold the RESET button** on the bottom of the RMQ1.
   - While holding RESET, connect the RMQ1's USB-C cable to your PC.
   - The flashing tool will automatically detect the device and begin flashing. Once the tool shows the flashing progress, you can **release the RESET button**.
   
   ![axdl-4](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-4.png){class="glboxshadow"}

## macOS / Linux

The official AXDL tool is Windows-only, but you can use the open-source [axdl-rs](https://github.com/ciniml/axdl-rs) (an unofficial Axera image downloader written in Rust) as an alternative.

### Install

- Rust toolchain — install via [rustup](https://rustup.rs/)

- `.axp` firmware file — download the latest firmware from the [official firmware page](https://dl.gl-inet.com/kvm/rmq1/beta); look for the file labeled **DOWNLOAD FOR USB OTG**

- Platform-specific dependencies:
>>>>>>> a235fd9d15fe9858c1a9ef499f1500cf30128712
  
- If you want the device to reboot automatically after the flashing, navigate to **Settings** → **Options** → **Reboot to Normal Mode After Download** and enable it before you begin. If this option is not enabled, you must manually reboot the device after the flashing is complete (i.e., by unplugging and reconnecting the power cable).

## Unbirck Steps

### Windows
1. Download the U-Boot firmware for your RMQ1 device to your computer from [here](https://dl.gl-inet.com/kvm/rmq1/stable) (select **DOWNLOAD FOR USB OTG**). 

![rmq1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}
  
2. Install the USB drivers:
  
- Download the driver package to your computer from [here](https://fw.gl-inet.com/tools/ax/Driver_V1.20.46.1.7z) and extract it to any directory.
  
- Double click the `DriverSetup.exe` file to run the installer.

![driver-1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-1.png){class="glboxshadow"}

![driver-2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-2.png){class="glboxshadow"}

![driver-3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/driver-3.png){class="glboxshadow"}

3. Install the AXDL Tool.
  
- Download AXDL to your computer from [here](https://www.teambition.com/task/6a55bcdb655bb6b2abdd5def) and extract it to an easily accessible directory.
  
- Double click the `AXDL.exe` file to run the flashing tool.

![axdl-1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-1.png){class="glboxshadow"}

4. Open the AXDL panel, click "load.axp", and select the firmware downloaded in Step 1 to upload it.

![axdl-2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-2.png){class="glboxshadow"}

Click "Start downloading".

![axdl-3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-3.png){class="glboxshadow"}

5. Power off your KVM device. Press and hold the RESET button on the bottom of the RMQ1, connect the device to your computer using the included USB-C cable.
  
6. Upon seeing "Downloading..." in the status column, release the RESET button.
  
![axdl-4](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-4.png){class="glboxshadow"}

7. Wait until the AXDL tool displays **Passed** to confirm that the flashing process is complete.

![axdl-5](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/axdl-5.png){class="glboxshadow"}

### macOS / Linux

The official AXDL tool is Windows-only. For macOS and Linux, you can use axdl-rs—an open-source, unofficial Axera image downloader written in Rust.

1. Install the Rust toolchain via [rustup](https://rustup.rs/)
  
2. Download the U-Boot firmware for your RMQ1 device to your computer from [here](https://dl.gl-inet.com/kvm/rmq1/stable) (select **DOWNLOAD FOR USB OTG**).

![rmq1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}
  
3. Install platform-specific dependencies:
  
- **Linux (Debian-based)**

   ```
   sudo apt install -y libudev-dev libusb-1.0-0-dev
   ```
   Configure udev rules to allow regular users to access the device:

   ```
   # Clone the repository
   git clone https://github.com/gl-inet/axdl-rs.git

   # Change directory
   cd axdl-rs

   # Copy the udev rule file to the system directory
   sudo cp 99-axdl.rules /etc/udev/rules.d/

   # Reload udev rules to apply changes
   sudo udevadm control --reload
   ```

   If the user is not in the `plugdev` group, please add them to the group, then re-log in for the changes to take effect.

   ```
   sudo usermod -a -G plugdev $USER
   ```

- **macOS**

   Install `libusb` via `brew` to enable USB communication with KVM devices:

   Build the `axdl-cli` tool

   ```
   cargo build --bin axdl-cli --package axdl-cli
   ```

4. Enter the following command to flash the firmware. Please replace the **/path/to/firmware.axp** with the actual path to your downloaded firmware file.

```
cargo run --bin axdl-cli --package axdl-cli -- --file /path/to/firmware.axp --wait-for-device
```

The tool will display “Waiting for device to be ready” and enter a waiting state.

5. Power off your KVM device. Press and hold the RESET button on the bottom of the RMQ1, connect the device to your computer using the included USB-C cable.
  
6. Wait until the flashing process is complete.

**Note:** Once flashing is complete, the device may not reboot automatically. Manually **power cycle** (power off and on) the RMQ1 to activate the new firmware.

**Expected Output**

After a successful flash, the terminal will display the output below. 

Note: Ccompiler warnings can be safely ignored.

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
