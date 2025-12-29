# Comet PoE (GL-RM1PE) Control Panel Guide

## Settings

In the control panel, navigate to **Settings**. The settings page includes four sections: 

- [Video](#video)
- [Remote Device Settings](#remote-device-settings)
- [System](#system)
- [Network](#network)

![settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/settings-general.png){class="glboxshadow"}

### Video

You can customize the video settings of the control page, e.g., display mode, video quality, video transmission, screen orientation, EDID, etc. 

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/settings-video.png){class="glboxshadow"}

- **Mode**: Switch between Normal and Smart mode. Smart mode balances latency and video quality for a better experience, especially in weak networks.
    
- **Quality**: Adjust the video quality to low/medium/high/ultra-high according to your network and resolution requirements.

- **Transfer**: Switch the video transmission method between WebRTC H.264 and Direct H.264. Note that the Direct H.264 has no sound.

- **Orientation**: Adjust the rotation angle of the control page to 0°/90°/180°/270°.

- **EDID**: Extended Display Identification Data (EDID) automatically matches the display's optimal parameters.

    The default configuration is suitable for most scenarios and usually does not need to be modified. Click [here](../../faq/how_to_set_edid_for_glkvm.md){target="_blank"} for details.

### Remote Device Settings

You can adjust the relevant settings of the controlled device.

![settings-remote device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/settings-remote-device.png){class="glboxshadow"}

- **Speaker**: Control audio output from the controlled device (e.g., system sounds, video audio)

- **Microphone**: Transmit local audio input (e.g., your voice) to the controlled device for remote interaction. It supports one-click mute, and a long-press shortcut to activate the microphone.

- **Keyboard**: Turn on or off the keyboard of the controlled device.

- **Show Virtual Keyboard**: Display and use the virtual keyboard on the control page.

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/settings-virtual-keyboard.png){class="glboxshadow"}

- **Mouse**: Turn on or off the mouse of the controlled device.

- **Show Local Cursor**: Display the mouse of the current device on the screen.

- **Mouse Jiggle**: It is applied to prevent the computer from entering sleep due to prolonged inactivity (e.g., remote meetings, server management).

- **Scroll Rate**: It refers to the speed at which the mouse wheel scrolls or the number of lines/units scrolled per wheel rotation, affecting how quickly content moves on the remote.

- **Scroll Direction**: It determines whether scrolling the mouse wheel up/down moves content on the remote screen in the same direction (natural scrolling) or the opposite direction (traditional scrolling). 

    Four direction modes are available: Standard, Vertical Invert, Horizontal Invert, and Both Invert.  

- **Mouse Mode**: Including Absolute Mode and Relative Mode.

- **Relative Sensitivity**: It is available when the Mouse Mode is Relative.

### System

You can customize the system display settings of the control panel, or reset the device with one click.

![settings-system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/settings-system.png){class="glboxshadow"}

- **Device Identity**: Customize or modify the KVM's identity recognized by the controlled device. Note that the EDID and device identification will remain synchronized; changing one of them will make the other one automatically updated to ensure correct recognition.

- **Language**: Set the control panel's language to Chinese or English.

- **Color Mode**: Customize the theme color to dark and light mode.

- **Time Zone**: Customize the time zone of the KVM control panel. This is only for the KVM control panel, not the system time of the controlled device.  

- **Reset KVM**: Factory reset your KVM with just one click.

### Network

You can check Comet PoE's network details, e.g., Hostname and IP address.

![settings-network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/settings-network.png){class="glboxshadow"}

As shown above, Comet PoE connects to an upstream network device via an Ethernet cable, with the IP address `192.168.10.209`.

You can click **Modify** to customize the hostname, or adjust the ethernet settings (e.g., assign a static IP for your KVM) if needed.

![settings-modify-hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/settings-modify-hostname.png){class="glboxshadow"}

![settings-modify-ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/settings-modify-ethernet.png){class="glboxshadow"}

## Toolbox

In the control panel, navigate to **Toolbox**. The toolbox page includes four sections: 

- [Clipboard](#clipboard)
- [Shortcut](#shortcut)
- [Wake On Lan](#wake-on-lan)
- [Terminal](#terminal)

![toolbox](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/toolbox-general.png){class="glboxshadow"}

### Clipboard

The clipboard allows you to easily paste text from the controlling device to the controlled device, without the need to transfer files.

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/toolbox-clipboard.png){class="glboxshadow"}

### Shortcut

You can find some common shortcut options here.

![toolbox-shortcut-1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/toolbox-shortcut.png){class="glboxshadow"}

Click **Modify** to adjust the shortcuts options if needed.

![toolbox-shortcut-modify](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/toolbox-shortcut-modify.png){class="glboxshadow"}  

### Wake On Lan

Wake-on-LAN (WOL) is a technology that allows the controlled device to be remotely powered on or awakened from a low-power state.

Click **Add Device** to choose a device from the same LAN and set up Wake-on-LAN.

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/toolbox-wol.png){class="glboxshadow"}  

### Terminal

You can access Comet PoE's terminal to perform advanced settings.

![toolbox-terminal-1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/toolbox-terminal1.png){class="glboxshadow"}

Click **Access**, and you will be re-directed to the GLKVM terminal, as shown below.

![toolbox-terminal-2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/toolbox-terminal2.png){class="glboxshadow"}

## Accessories

GL.iNet offers optional accessories for KVM devices to provide additional convenience for remote control. 

First, refer to the corresponding user guide for connecting the accessory to the controlled device.

- [Fingerbot (FGB-01) User Guide](../gl-fgb-01/index.md){target="_blank"}

- [ATX Board (GL-ATXPC) User Guide](../gl-atx-board/index.md){target="_blank"}

Second, log in to the control panel and navigate to **Accessories**. You will be able to control the device's power on/off through the accessories. 

**Note**: Accessory settings are only available after the accessory is installed.

### Fingerbot
    
The Fingerbot is adhered to the physical power button of the controlled device, to achieve remote control of the controlled device's power supply.
    
It works according to the settings configured on the control panel.

![accessories fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/accessories-fgb.png){class="glboxshadow"}

- **Time**: The press duration of the Fingerbot. You can set it to 0.5s/3s/8s.

- **Strength**: There are two levels of pressing strength: Lightly Press and Firmly Press.

    - **Lightly Press**: Perfect for short or soft-touch buttons.
    
    - **Firmly Press**: Ideal for deep or firm buttons.

    ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### ATX Power

The ATX Board is installed in the computer case to achieve remote control of the device's power on/off/reboot.

It works according to the settings configured on the control panel.

![accessories atxpower](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/accessories-atx.png){class="glboxshadow"}

- **Power (Short Press)**: Used for regular power-on or system wake-up.

- **Power (Long Press)**: Performs a forced shutdown operation.

- **Restart**: Restart the device.

## Virtual Media

Comet PoE allows you to transfer files or mount images between the controlling device and the controlled device.

In the control panel, navigate to **Virtual Media**. Here you can perform the following operations:

- [Share Files](#file-sharing)
- [Mount Images](#image-mounting)
- [Replace Storage Drive](#replace-storage-drive)
- [Format Disk](#format-disk)

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-general.png){class="glboxshadow"}
    
### File Sharing

It emulates a read-write USB drive, allowing you to share and manage files between the controlling device and the controlled device.

**To share files from the controlling device to the controlled one, follow the steps below.**

1. Drag or click the box to upload files from your controlling device or upload from URL. 

    Once uploaded, the files will be displayed as follows.

    ![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-upload-files.png){class="glboxshadow"}

2. Click **Mount To Remote** -> **File Sharing**. 

    ![file sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-file-sharing.png){class="glboxshadow"}

    A window will pop up in the control panel to indicate file sharing steps, as shown below.
    
    ![file sharing tips](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-sharing-tips.png){class="glboxshadow"}

3. In the Comet PoE's control screen, go to **This PC** of your controlled device. 

    ![go to this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-thispc.png){class="glboxshadow"}

4. Find a disk named **GLKVM**, and you will see the files you uploaded previously from the controlling device to Comet PoE have been shared to the controlled device.

    Now you can view, move or delete the files in this disk.

    ![glkvm disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-glkvm-disk.png){class="glboxshadow"}

5. If you want to stop sharing, click **Virtual Media** in the toolbar and click **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-stop-sharing1.png){class="glboxshadow"}

**To share files from the controlled device to the controlling one, follow the steps below.**

1. Save or copy the files you want to share into the disk **GLKVM**. 

    For example, a PDF file named "gl-rm10_datasheet" has been copied from the controlled device's Desktop into the disk **GLKVM**. 

    ![copy file to disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-copy-file.png){class="glboxshadow"}
    
2. Turn to the Comet PoE's control panel, click **Virtual Media** in the toolbar and click **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-stop-sharing2.png){class="glboxshadow"}
    
3. Then this file will be displayed under the Virtual Media, as shown below. Now you can download this file from Comet PoE to your controlling device.

    ![file shared](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-file-shared.png){class="glboxshadow"}

### Image Mounting

Comet PoE can simulate a read-only virtual CD/DVD or disk drive on the device being controlled. You can access this drive during the BIOS or UEFI startup process. 
    
This function can help you reinstall the operating system or mount an ISO to install applications on the device being controlled, or perform other tasks.
    
1. Drag or click the box to upload files. **Ensure this file can be mounted as an iso format**.

    Once uploaded, the files will be displayed as follows.

    ![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-upload-iso.png){class="glboxshadow"}
    
2. Click **Mount To Remote** -> **Image Mounting**. 

    ![image mounting 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-image-mount1.png){class="glboxshadow"}

3. In the pop-up window, select the file and click **Mount Image**.

    ![image mounting 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-image-mount2.png){class="glboxshadow"}

    Then you can use this file on the controlled end.

### Replace Storage Drive

You can insert a USB storage device into the KVM USB port to replace the internal storage.

![replace storage drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-replace-storage.png){class="glboxshadow"}

### Format Disk

You can format the disk or disable the virtual media with one click.

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/vm-format-disable.png){class="glboxshadow"}

- **Format**: Erase all data on the disk and reinitialize its file system structure.

- **Disable**: Disable the virtual media will immediately reboot the KVM device. 

## Apps Center

In the control panel, navigate to **Apps Center**. The integrated applications can be found here.

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/apps-center.png){class="glboxshadow"}

### Tailscale

Comet PoE integrates with Tailscale, allowing you to remotely access it via Tailscale virtual network.

Simply bind the Comet PoE and your controlling device to the same Tailscale account, and you will be able to remotely access the Comet PoE by entering its **Tailscale virtual IP** into a web browser on the controlling device, without installing the GLKVM app.

Click [here](../../faq/remote_access_to_controlled_device_via_tailscale.md){target="_blank"} for more instructions.

After binding, the control page will show the bound Tailscale account.

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/tailscale-enabled.png){class="glboxshadow"}

## Help

In the control panel, navigate to **Help**. Here you can find more information about GL.iNet KVM and help documentation, as well as export logs for troubleshooting.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/help.png){class="glboxshadow"}

## Toolbar

In the control panel, navigate to the top right corner to access the following tools:

- [Collapse Toolbar](#collapse)
- [Fullscreen](#fullscreen)
- [Upgrade](#upgrade)
- [Cloud Service](#cloud-service)
- [Security](#security)
- Reboot
- Logout

### Collapse

Click the upward arrow icon in the top right corner to collapse the toolbar.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/collapse1.png){class="glboxshadow"}

When the toolbar is collapsed, click the downward arrow icon at the top to expand it.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/collapse2.png){class="glboxshadow"}

### Fullscreen

Click the fullscreen icon (square-shaped) in the top right corner to switch to fullscreen mode.

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/fullscreen1.png){class="glboxshadow"}

When in fullscreen mode, press and hold the Esc key, or click the exit fullscreen icon (grid-shaped) in the top right corner to exit fullscreen. 

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/fullscreen2.png){class="glboxshadow"}

### Upgrade

If there's newer firmware available, you can upgrade it online. Alternatively, you can download the firmware from [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} and perform local upgrade.

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/upgrade1.png){class="glboxshadow"}

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/upgrade2.png){class="glboxshadow"}

### Cloud Service

GL.iNet KVM can be accessed locally, so as to manage the controlled device under local network.

If you want to access the controlled device remotely, we suggest you use Cloud service. Click [here](../gl-rm1pe/quick_setup_guide.md#remote-access-to-comet) for details.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/cloud.png){class="glboxshadow"}

### Security

Change admin password or enable two-factor authentication as needed. 

- Change Admin Password.

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/change-password.png){class="glboxshadow" width="434"}

- 2FA: Enable two-factor authentication to protect your account.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/control_panel/2fa.png){class="glboxshadow"}
