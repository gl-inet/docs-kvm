# Control Panel Guide

## Settings

In the control panel, navigate to **Settings**, you will get a page as below.

![settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/settings.png){class="glboxshadow"}

### Video

You can modify the video quality, orientation and EDID settings of the control page. 

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings-video.jpg){class="glboxshadow"}
    
- Quality: Adjust the video quality to low/medium/high/ultra-high according to your network and resolution requirements.

- Orientation: Adjust the control page rotation degree.

- EDID: Extended Display Identification Data. It aims to automatically match the display optimal parameters. The default configuration is suitable for most scenarios and usually does not need to be modified. Click [here](https://docs.gl-inet.com/kvm/en/faq/how_to_set_edid_for_glkvm/){target="_blank"} for details.

- Mode: You can switch the mode between WebRTC H.264 and Direct H.264.

### Remote Device Settings

You can adjust the relevant settings of the controlled device.

![settings-remote device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings-remote-device.png){class="glboxshadow"}

- Speaker: Control audio output from the controlled device (e.g., system sounds, video audio)

- Microphone: Transmit local audio input (e.g., your voice) to the controlled device for remote interaction.

- Keyboard: Turn on or off the keyboard of the controlled device.

- Show Virtual Keyboard: Display and use the virtual keyboard on the control page.

    ![virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/show_virtual_keyboard.png){class="glboxshadow"}

- Mouse: Turn on or off the mouse of the controlled device.

- Show Local Cursor: Display the mouse of the current device on the screen.

- Mouse Jiggle: This feature is available since firmware v1.3.0. 
    
    It is applied to prevent the computer from entering sleep due to prolonged inactivity (e.g., remote meetings, server management).

- Scroll Rate: It refers to the speed at which the mouse wheel scrolls or the number of lines/units scrolled per wheel rotation, affecting how quickly content moves on the remote.

- Scroll Direction: It determines whether scrolling the mouse wheel up/down moves content on the remote screen in the same direction (natural scrolling) or the opposite direction (traditional scrolling). 

    Four direction modes are available: Standard, Vertical Invert, Horizontal Invert, and Both Invert.  

- Mouse Mode: Including Absolute Mode and Relative Mode.

- Relative Sensitivity: It is available when the Mouse Mode is Relative.

### System

You can change the system display settings of the control panel, or reset the device with one click.

![settings-system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings-system.jpg){class="glboxshadow"}

- Device Identity: Change or customize your KVM's identity recognized by the controlled device.

    Note that the EDID and device identification will remain synchronized; changing one of them will make the other one automatically updated to ensure correct recognition.

- Language: Switch the language of control panel. 

- Color Mode: Switch the theme color, including dark and light modes.

- Time Zone: You can change the time zone of the KVM control panel. This is only for the KVM control panel, not the system time of the controlled device.  

- Reset KVM: Factory reset your KVM with just one click.

### Network

You can check Comet Pro's network details.

![settings-network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/settings-network.png){class="glboxshadow"}

As shown above, Comet Pro connects to the router via an Ethernet cable and Wi-Fi at the same time.

Click **Modify** to change the Ethernet or Wi-Fi settings.

![settings-network-modify](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/ethernet-settings.png){class="glboxshadow"}

## Toolbox

In the control panel, navigate to **Toolbox**.

![toolbox](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/toolbox.png){class="glboxshadow"}

### Clipboard

The clipboard allows you to easily paste text from the controlling device to the controlled device, without the need to transfer files.

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-clipboard.png){class="glboxshadow"}

### Shortcut

It shows some common shortcut options.

![toolbox-shortcut](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-shortcut.png){class="glboxshadow"}

Click **Show All** to show all shortcut options.

![toolbox-shortcut-all](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-shortcut-all.png){class="glboxshadow"}  

Click **Modify** to adjust the shortcut options.

![toolbox-shortcut-modify](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-shortcut-modify.png){class="glboxshadow gl-50-desktop"}  

### Wake On Lan

Wake-on-LAN (WOL) is a technology that allows the controlled device to be remotely powered on or awakened from a low-power state.

Click **Add Device** to choose a device from the same LAN and set up Wake-on-LAN.

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-wol.png){class="glboxshadow"}  

### Terminal

You can access the Comet Pro's terminal to perform advanced settings.

![toolbox-terminal-1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-terminal-1.png){class="glboxshadow"}

Click **Access**, you will be re-directed to the GLKVM terminal, as shown below.

![toolbox-terminal-2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/access-terminal.png){class="glboxshadow"}

## Accessories

GL.iNet offers optional accessories for KVM devices, providing additional convenience for remote management. 

Firstly, connect the accessories to the controlled device. Please refer to the user guide of the corresponding accessories.

- [GL-Fingerbot (GL-FGB-01)](../gl-fgb-01/index.md){target="_blank"}

- [GL-ATX Board](../gl-atx-board/index.md){target="_blank"}

Then log in to the control panel, navigate to **Accessories**. 

![accessories](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/accessories.png){class="glboxshadow"}

**Note**: Accessory settings are only displayed after installation.

### Fingerbot
    
The Fingerbot is adhered to the physical power button of the controlled device, to achieve remote control of the controlled device's power supply.
    
It works as per the following settings.

- Time: The duration for which the Fingerbot presses.

- Strength: Two levels of pressing strength are provided: Light Press mode and Hard Press mode.

    - Light Press Mode: Perfect for short or soft-touch buttons.
        
    - Hard Press Mode: Ideal for deep or firm buttons.

    ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### ATX Power

The ATX Board is installed in the computer host box to achieve remote control of the controlled device's power on/off/reboot.

It works as per the following settings.

- Power: Provides short press and long press functions.

- Restart: Restart the device.

## Virtual Media

Comet Pro allows you to transfer files between the host controlling device and the controlled device.

In the control panel, navigate to **Virtual Media**.

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/virtual_media.jpg){class="glboxshadow"}

Drag or click the box to upload files from your controlling device, or upload from URL. 

As an example, two images have been uploaded from the controlling device to the Comet Pro here.

![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/upload-files.png){class="glboxshadow"}

Click **Mount To Remote**, and you will see two options: **File Sharing** and **Image Mounting**.

![mount to remote](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/mount_to_remote.jpg){class="glboxshadow"}
    
### File Sharing

It emulates a read-write USB drive, allowing you to share and manage files between the controlling device and the controlled device.

Upload files from your controlling device to Comet Pro, and click on **File Sharing**. A window will pop up in the control panel to indicate file sharing steps. Click "Don't remind me" to hide it.
    
![file sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/file_sharing_1.png){class="glboxshadow"}

Turn to the Comet Pro's control panel and access your controlled device. Go to **This PC** and find a Drive named **GLKVM**. Now you can view, move or delete the files in this drive.

![file sharing 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/file-sharing-icon.png){class="glboxshadow"}

If you want to share files from the controlled device to the controlling device, simply place the files into this drive. Those files will be displayed under the Virtual Media in the Comet Pro's control panel after you stop the file sharing.

For example, a PDF file named "gl-rm1_datasheet" has been placed into this drive. In Comet Pro's control panel, go to Virtual Media and click **Stop Sharing**.

![file sharing 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/file_sharing_3.png){class="glboxshadow"}

Then this file will be displayed under the Virtual Media, as shown below. Now you can download this file from Comet Pro to your controlling device.

![file sharing 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/file_sharing_4.png){class="glboxshadow"}
    
### Image Mounting

It emulates a read-only CD-Rom, supports BIOS/UEFI boot, for system reinstallation or ISO-based software installation.

Comet Pro can simulate a read-only virtual CD/DVD or disk drive on the target host. You can access this drive during the BIOS or UEFI startup process. 
    
This function can help you reinstall the operating system or mount an ISO to install applications on the target host and other tasks.
    
Click on **Image Mounting**, in the pop-up Mount Settings, select the file and ensure this file can be mounted as an iso format, then click **Mount Image**. 

![image mounting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/image_mounting.png){class="glboxshadow"}

Then you can use this file on the controlled end.

## Apps Center

In the control panel, navigate to **Apps Center**, the integrated applications can be found here.

![image mounting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/apps_center.png){class="glboxshadow"}

### Tailscale

Comet Pro integrates with Tailscale, allowing you to remotely access it via Tailscale virtual network.

In the control panel, navigate to Apps Center -> Tailscale, bind Comet Pro and your controlling device to your Tailscale account. Then you can remotely access it by typing its Tailscale virtual IP into a web browser on the controlling device, without installing GLKVM app.

Click [here](../../faq/remote_access_to_controlled_device_via_tailscale.md){target="_blank"} for more instructions.

Once enabled, the page will show the bind account.

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/tailscale_enabled.png){class="glboxshadow"}

## Help

Here you can find more information about GL.iNet KVM and help documentation, as well as export logs for troubleshooting.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/help.png){class="glboxshadow"}

## System Settings

In the control panel, navigate to the upper-right corner to access the following system functions and options:

- Collapse Toolbar
- Full-Screen
- Upgrade Firmware
- Cloud Service
- Security (including Change Admin Password and 2FA Auth)
- Reboot
- Logout

### Upgrade

Local and Online Upgrades are supported.

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/upgrade_firmware.png){class="glboxshadow"}

### Cloud Service

GL.iNet KVM panel can be accessed locally, so as to manage the controlled device under local network. Click [here](#local-access-to-the-controlled-device) for more details.

If you want to access the controlled device remotely, we suggest you download the App to use Cloud service.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/cloud_service.jpg){class="glboxshadow"}

### Security

- Change Admin Password.

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/change_password.png){class="glboxshadow gl-60-desktop"}

- 2FA Auth: Enable two-factor authentication to protect your account.
