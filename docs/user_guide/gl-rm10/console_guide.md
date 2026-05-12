# Comet Pro (GL-RM10) Console Guide

## Settings

On the console, navigate to **Settings**. The settings page includes four sections: 

- [Video](#video)
- [Remote Device Settings](#remote-device-settings)
- [System](#system)
- [Network](#network)

![settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/settings-general.png){class="glboxshadow"}

### Video

You can customize video settings on the console, such as display mode, video quality, video transmission, screen orientation, and EDID.

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/settings-video.png){class="glboxshadow"}

- **Mode**: Switch between Normal and Smart mode. Smart mode balances latency and video quality for a better experience, especially in weak networks.
    
- **Quality**: Adjust the video quality to low/medium/high/ultra-high/Lossless according to your network environment and resolution requirements.

- **Transfer**: Switch the video transmission method between WebRTC, WebRTC (FEC), and Direct. Note that the Direct transfer has no sound.

    !!! note "What's the difference between WebRTC, WebRTC (FEC) and Direct?"

        - **WebRTC**: Balances smooth video and stable audio for real-time remote control.
        
        - **WebRTC (FEC)**: Adds forward error correction to improve connection stability under poor or unstable network conditions. When selected, it automatically repairs lost data packets by transmitting a small amount of redundant data, reducing screen flickering and lag.
        
        - **Direct**: Provides the lowest latency and lossless video quality, but does not support audio transmission.

- **Orientation**: Adjust the console's rotation angle to 0°/90°/180°/270°.

- **EDID**: Extended Display Identification Data (EDID) automatically matches the optimal display parameters. The default EDID is suitable for most scenarios and generally does not need to be modified. Click [here](../../faq/how_to_set_edid_for_glkvm.md){target="_blank"} for details. If the EDID has been changed but the screen does not update, try restarting the controlled device.

- **View**: This feature controls whether the screen follows the browser window when resizing. Three options are available: Adaptive, Best Picture Quality, and Original Pixel.

### Remote Device Settings

You can adjust the relevant settings of the controlled device.

![settings-remote device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/settings-remote-device.png){class="glboxshadow"}

- **Speaker**: Control audio output from the controlled device (e.g., system sounds, video audio)

- **Microphone**: Transmit local audio input (e.g., your voice) to the controlled device for remote interaction. It supports one-click mute, and a long-press shortcut to activate the microphone.

- **Keyboard**: Turn on or off the keyboard of the controlled device.

- **Bad Link Mode**: i.e. Release keys immediately. Each key press is sent as a single quick press-and-release action, preventing stuck keys or unintended repeated input during remote control.

- **Show Virtual Keyboard**: Show and use the virtual keyboard on the console.

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/settings-virtual-keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: This feature swaps the Cmd and Ctrl keys to ensure keyboard compatibility across different operating systems.

- **Mouse**: Turn on or off the mouse of the controlled device.

- **Show Local Cursor**: Display the mouse of the current device on the screen.

- **Mouse Jiggle**: The Mouse Jiggler feature simulates subtle, periodic mouse movements to prevent the computer (i.e., the controlled device) from going to sleep due to prolonged inactivity, such as during remote meetings and server management.

- **Scroll Rate**: It refers to the speed at which the mouse wheel scrolls or the number of lines/units scrolled per wheel rotation, affecting how quickly content moves on the remote.

- **Scroll Direction**: It determines whether scrolling the mouse wheel up/down moves content on the remote screen in the same direction (natural scrolling) or the opposite direction (traditional scrolling). 

    Four direction modes are available: Standard, Vertical Invert, Horizontal Invert, and Both Invert.  

- **Mouse Mode**: Allows switching between Absolute Mode and Relative Mode to ensure smooth and accurate cursor control in different remote control scenarios.

    !!! note "What's the difference between Absolute Mode and Relative Mode?"

        - **Relative Mode**: The mouse position is calculated based on movement rather than fixed screen coordinates. You must click inside the remote window to control the mouse. The cursor is locked within the remote screen and cannot move out smoothly. This mode provides better compatibility with BIOS, old systems, and embedded devices.

        - **Absolute Mode**: The mouse position corresponds to exact screen coordinates. The remote cursor follows the local one smoothly and accurately, allowing seamless movement between your local screen and the remote screen. It is ideal for daily desktop control and precise operations, though a slight delay may occur due to network transmission.

        In short, use Absolute for smooth daily control; use Relative for BIOS access, some older devices that do not support absolute positioning, or to avoid accidental cursor movement.

- **Relative Sensitivity**: It is available when the Mouse Mode is Relative.

### System

You can customize the system display settings of the console, or reset the device with one click.

![settings-system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/settings-system.png){class="glboxshadow"}

- **Device Identity**: Customize or modify the KVM's identity recognized by the controlled device. Note that EDID and device identification remain synchronized. Changing either one will automatically update the other to ensure correct device recognition.

- **Language**: Set the console's language to Chinese or English.

- **Color Mode**: Customize the theme color to Light or Dark mode.

- **Time Zone**: Customize the time zone of the KVM console. 

- **Reset KVM**: Factory reset your KVM with just one click.

### Network

You can check Comet Pro's network details, e.g., Hostname and IP address.

![settings-network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/settings-network.png){class="glboxshadow"}

- **Hostname**: You can modify the device hostname directly on the console. This feature has been available since firmware v1.7.0.

- **Ethernet**: When Comet Pro connects to an upstream network device via an Ethernet cable, its Ethernet IP address will be displayed here. You can click the IP address or the right arrow to view the ethernet details.

    When the protocol is DHCP, the page displays as follows.

    ![ethernet dhcp](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/ethernet-dhcp.png){class="glboxshadow"}

    If you want to set a static IP address, switch the protocol to **Static** and enter the required network parameters (e.g., IP address, netmask, gateway) accordingly.

    ![ethernet static](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/ethernet-static.png){class="glboxshadow"}

- **Wireless**: When Comet Pro connects to a Wi-Fi network, its Wi-Fi IP address will be displayed here. You can click the IP address or the right arrow to view the Wi-Fi details, including the SSID, assigned IP address, gateway, and the MAC address your Comet Pro uses to connect to.

    ![wifi config](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/wifi-config.png){class="glboxshadow"}

    To connect Comet Pro to a different Wi‑Fi network, click **Switch Wi-Fi** and select a network from the list of available Wi‑Fi networks.

    ![join wifi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/join-wifi-network.png){class="glboxshadow"}

## Toolbox

On the console, navigate to **Toolbox**. The toolbox page includes four sections: 

- [Clipboard](#clipboard)
- [Shortcut](#shortcut)
- [Wake On Lan](#wake-on-lan)
- [Terminal](#terminal)

![toolbox](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox-general.png){class="glboxshadow"}

### Clipboard

The clipboard allows you to easily paste text from the controlling device to the controlled device without file transfer, making it highly convenient for copying and pasting long text.

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox-clipboard.png){class="glboxshadow"}

### Shortcut

The shortcut let you perform actions faster without using the virtual keyboard, helping you work more efficiently and save time on daily tasks. You can find some common shortcuts here.

![toolbox-shortcut1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox-shortcut1.png){class="glboxshadow"}

Click **Modify** to adjust the shortcuts options as needed.

![toolbox-shortcut2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox-shortcut2.png){class="glboxshadow"}  

### Wake On Lan

Wake-on-LAN (WOL) is a technology that allows the controlled device to be remotely powered on or awakened from a low-power state.

Click **Add Device** to choose a device from the same LAN and set up Wake-on-LAN.

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox-wol.png){class="glboxshadow"}  

### Terminal

You can access Comet Pro's terminal to perform advanced settings.

![toolbox-terminal1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox-terminal-1.png){class="glboxshadow"}

Click **Access**, and you will be re-directed to the GLKVM terminal, as shown below.

![toolbox-terminal2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox-terminal-2.png){class="glboxshadow"}

## Accessories

GL.iNet offers optional accessories for KVM devices to provide additional convenience for remote control. 

First, refer to the corresponding user guide for connecting the accessory to the controlled device.

- [Fingerbot (FGB-01) User Guide](../gl-fgb-01/index.md){target="_blank"}

- [ATX Board (GL-ATXPC) User Guide](../gl-atx-board/index.md){target="_blank"}

Second, log in to the KVM console and navigate to **Accessories**. You will be able to control the device's power on/off through the accessories. 

**Note**: Accessory settings are only available after the accessory is installed.

### Fingerbot
    
The Fingerbot is adhered to the physical power button of the controlled device, to achieve remote control of the controlled device's power supply.
    
It works according to the settings configured on the console.

![accessories fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/accessories-fgb.png){class="glboxshadow"}

- **Time**: The press duration of the Fingerbot. You can set it to 0.5s/3s/8s.

- **Strength**: There are two levels of pressing strength: Lightly Press and Firmly Press.

    - **Lightly Press**: Perfect for short or soft-touch buttons.
    
    - **Firmly Press**: Ideal for deep or firm buttons.

    ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### ATX Power

The ATX Board is installed in the computer case to achieve remote control of the device's power on/off/reboot.

It works according to the settings configured on the console.

![accessories atxpower](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/accessories-atx.png){class="glboxshadow"}

- **Power (Short Press)**: Used for regular power-on or system wake-up.

- **Power (Long Press)**: Performs a forced shutdown operation.

- **Restart**: Restart the device.

## Virtual Media

Comet Pro allows you to transfer files or mount images between the controlling device and the controlled device.

On the console, navigate to **Virtual Media**. Here you can perform the following operations:

- [Share Files](#file-sharing)
- [Mount Images](#image-mounting)
- [Replace Storage Drive](#replace-storage-drive)
- [Format Disk](#format-disk)

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/virtual-media.png){class="glboxshadow"}
    
### File Sharing

It emulates a read-write USB drive, allowing you to share and manage files between the controlling device and the controlled device.

**To share files from the controlling device to the controlled one, follow the steps below.**

1. Drag or click the box to upload files from your controlling device or upload from URL. 

    Once uploaded, the files will be displayed as follows.

    ![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-uploaded.png){class="glboxshadow"}

2. Click **Mount To Remote** -> **File Sharing**. 

    ![file sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount1.png){class="glboxshadow"}

    A window will pop up on the console, indicating the file sharing steps, as shown below.
    
    ![file sharing prompt](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount2-prompt.png){class="glboxshadow"}

3. Wait a second, and a drive named **"GLKVM"** will pop up on the screen automatically. You will then see the files you previously uploaded from the controlling device to Comet Pro have been shared to the controlled device. Now you can view, move or delete the files in this drive on the controlled end.

    ![file sharing glkvm drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount3.png){class="glboxshadow"}

    **Tips**: If the drive does not pop up automatically, go to **This PC** of your controlled device. 

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-thispc.png){class="glboxshadow"}
    
    Then find a drive named **GLKVM**. Now you can view, move or delete the files in this drive.

4. If you want to stop the sharing, click **Virtual Media** in the toolbar and click **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/stop-sharing1.png){class="glboxshadow"}

**To share files from the controlled device to the controlling one, follow the steps below.**

1. On the controlled device, move or copy the files you want to share into the drive **GLKVM**. 

    For example, an image named "slate7-pro_gl-be10000" has been moved from the controlled device's Desktop to the drive **GLKVM**. 

    ![copy file to drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-copy.png){class="glboxshadow"}
    
2. Turn to the Comet Pro's console, click **Virtual Media** in the toolbar and click **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/stop-sharing2.png){class="glboxshadow"}
    
3. This file will then be displayed under the **Virtual Media**, as shown below. Now you can download this file from Comet Pro to your controlling device.

    ![file shared](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-shared.png){class="glboxshadow"}

### Image Mounting

Comet Pro can simulate a read-only virtual CD/DVD or a disk drive on the controlled device. You can access this drive during the BIOS or UEFI startup process. 
    
This function can help you reinstall the operating system or mount an ISO to install applications on the device being controlled, or perform other tasks.
    
1. Drag or click the box to upload files. **Ensure this file can be mounted as an iso format**.

    Once uploaded, the files will be displayed as follows.

    ![image mount1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount1.png){class="glboxshadow"}
    
2. Click **Mount To Remote** -> **Image Mounting**. 

    ![image mount2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount2.png){class="glboxshadow"}

3. In the pop-up window, select the file and click **Mount Image**.

    ![image mount3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount3.png){class="glboxshadow"}

    Then you can use this file from the CD drive on the controlled device.

    ![image mount4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount4.png){class="glboxshadow"}

### Replace Storage Drive

You can insert a USB storage device into the KVM USB port to replace the internal storage.

![replace storage drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/replace-storage.png){class="glboxshadow"}

### Format Disk

You can format the disk or disable the virtual media with one click.

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/format-storage.png){class="glboxshadow"}

- **Format**: Erase all data on the disk and reinitialize its file system structure.

- **Disable**: Disable the virtual media will immediately reboot the KVM device. 

## Apps Center

On the console, navigate to **Apps Center**. The integrated applications can be found here.

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/apps_center.png){class="glboxshadow"}

### Tailscale

Comet Pro integrates with Tailscale, allowing you to access it remotely through the Tailscale virtual network.

Simply bind both Comet Pro and your controlling device to the same Tailscale account, and you will be able to remotely access the Comet Pro by entering its **Tailscale virtual IP** into a web browser on the controlling device, without installing the GLKVM app.

Click [here](../../faq/remote_access_via_tailscale.md){target="_blank"} for detailed instructions.

After binding, the Comet Pro's console will show the bound Tailscale account.

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/control_panel/tailscale.png){class="glboxshadow"}

### ZeroTier

Comet Pro integrates with ZeroTier, allowing you to access it remotely through the ZeroTier virtual network.

Simply join both Comet Pro and your controlling device to the same ZeroTier network (using a 16-character alphanumeric Network ID), and you can remotely access Comet Pro by entering its **ZeroTier IP** in a web browser on the controlling device, with no need to install the GLKVM app.

Click [here](../../faq/remote_access_via_zerotier.md){target="_blank"} for detailed instructions.

After binding, the Comet Pro's console will show the ZeroTier Network ID and Virtual IP.

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/zerotier_enabled.png){class="glboxshadow"}

## Help

On the console, navigate to **Help**. Here you can find more information about GL.iNet KVM and help documentation, as well as export logs for troubleshooting.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/help.png){class="glboxshadow"}

## Toolbar

On the console, navigate to the top right corner to access the following tools:

- [Collapse Toolbar](#collapse)
- [Fullscreen](#fullscreen)
- [Upgrade](#upgrade)
- [Cloud Service](#cloud-service)
- [Security](#security)
- Reboot
- Logout

### Collapse

Click the upward arrow icon in the top right corner to collapse the toolbar.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/collapse1.png){class="glboxshadow"}

When the toolbar is collapsed, click the downward arrow icon at the top to expand it.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/collapse2.png){class="glboxshadow"}

### Fullscreen

Click the fullscreen icon (square-shaped) in the upper right corner to switch to fullscreen mode.

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/fullscreen1.png){class="glboxshadow"}

To exit fullscreen, press and hold the **Esc** key, or click the exit fullscreen icon (grid-shaped) in the upper right corner. 

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/fullscreen2.png){class="glboxshadow"}

### Upgrade

Click the firmware version in the upper right corner to check for updates.

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade1.png){class="glboxshadow"}

You can upgrade your Comet Pro online if newer firmware is available. Alternatively, download the latest firmware from the [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} and perform a local upgrade.

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade2.png){class="glboxshadow"}

### Cloud Service

GL.iNet KVM Cloud Service allows you to access the controlled device remotely. Click [here](../gl-rm10/quick_setup_guide.md#remote-access-to-comet-pro) for details.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/cloud-service1.png){class="glboxshadow"}

If your Comet Pro has been bound to the GL.iNet Cloud, the console will display the cloud status as follows.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/cloud-service2.png){class="glboxshadow"}

### Security

The security allows you to perform some security settings, e.g., change admin password, enable two-factor authentication, or customize TLS certificate. 

- Change Admin Password

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/change-password.png){class="glboxshadow" width="434"}

- 2FA: Enable two-factor authentication to protect your account.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/2fa.png){class="glboxshadow"}

- TLS Certificate

    The system will use the pre-installed default certificate for browser access. If you want to customize the TLS certificate for web browser access, click **TLS Certificate** in the upper right corner of the console, select **Custom Certificate**, then upload your **certificate file & private key file**.

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/tls-cert-custom.png){class="glboxshadow"}
