# How to unbrick KVM via USB OTG

## Supported devices

- RMQ1

## Prerequisites

- A Windows PC / mac OS / Ubuntu

- RMQ1 device

- `.axp` firmware file — download the latest firmware from the [official firmware page](https://dl.gl-inet.com/kvm/rmq1/beta); look for the file labeled **DOWNLOAD FOR USB OTG**
  
  ![rmq1-usbotg](https://static.gl-inet.com/docs/kvm/tutorials/how_to_unbrick_kvm_via_usb_otg/rmq1-usbotg.png){class="glboxshadow"}

> **Important:** Before flashing, back up the `factory` partition to preserve device-specific data (e.g., MAC address, cert data). If the device is still accessible via the web interface, go to **Toolbox** → **Terminal** → **Access**, then run:
> 
> ```bash
> dd if=/dev/mtd6 of=/userdata/media/factory.bin
> ```
> 
> The backup file will appear in **Virtual Media** and can be downloaded to your local machine.

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
  
  **Linux (Debian-based):**
  
  ```bash
  sudo apt install -y libudev-dev libusb-1.0-0-dev
  ```
  
  Configure udev rules to allow non-root access to the device:
  
  ```bash
  git clone https://github.com/gl-inet/axdl-rs.git
  cd axdl-rs
  sudo cp 99-axdl.rules /etc/udev/rules.d/
  sudo udevadm control --reload
  ```
  
  If your user is not in the `plugdev` group, add it and re-login:
  
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

### Flashing

1. Run the flashing command (use the path to your downloaded `.axp` file):
   
   ```bash
   cargo run --bin axdl-cli --package axdl-cli -- --file /path/to/firmware.axp --wait-for-device
   ```
   
   The tool will display `Waiting for the device to be ready` and wait.

2. **Connect the device in flashing mode**
   
   - **Do not** connect the RMQ1 to a power adapter.
   - Press and **hold the RESET button** on the bottom of the RMQ1.
   - While holding RESET, connect the RMQ1's USB-C cable to your PC.
   - Once the tool shows the flashing progress, you can **release the RESET button**.

3. After flashing completes, the device may not auto-reboot. **Power cycle** the RMQ1 manually (disconnect and reconnect the power cable) to boot into the new firmware.

**Expected output**

A successful flash looks like this (compiler warnings can be safely ignored):

<details>
<summary>Example log</summary>

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
