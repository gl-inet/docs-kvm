# Comet PoE (GL-RM1PE) User Guide

Comet PoE (GL-RM1PE) is the Power-over-Ethernet version of the [Comet (GL-RM1)](../gl-rm1/index.md), designed for simplified single-cable setups. The PoE model delivers both power and network connectivity via a single Ethernet cable, reducing cable clutter and simplifying installation, especially in hard-to-reach environments.

In addition, this version upgrades the EMMC capacity to 32GB, making it more capable of handling system logs, recordings, or custom firmware.

## Product Overview

### Appearance

![appearance 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/appearance-1.png){class="glboxshadow"}

![appearance 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/appearance-2.jpg){class="glboxshadow"}

### Interface

![interface](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/interface.png){class="glboxshadow"}

### LED

There is 1x LED on the top panel of Comet PoE.

| LED Status               | Indication                        |
| :----------------------- | :-------------------------------- |
| Solid Blue               | Starting up                       |
| Flashing White           | Started up but No Internet        |
| Solid White              | Connected to Internet             |
| Flashing Blue & White    | Firmware Upgrading                |

## Quick Setup Guide

### Connect the Devices

For clarity, the controlling device is referred to as Device A, and the controlled device as Device B.

![distinguishing devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/connect-1.png){class="glboxshadow"}

1. Connect the Comet PoE to the PoE Switch with an Ethernet cable.

    ![connect ethernet cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/connect-2.png){class="glboxshadow"}

2. Use an HD cable to connect the Comet PoE's HD IN port to the HD OUT port of the Device B.

    ![connect hdmi cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/connect-3.png){class="glboxshadow"}

3. Connect the Comet PoE's USB port to the USB interface of the Device B using a USB cable.

    ![Connect usb cbale](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/connect-4.png){class="glboxshadow"}

4. Device connection is complete. 

    You can now access the Comet PoE control panel locally via a browser on the controlling device, or download the GLKVM app on the controlling device to remotely access it.

### Local Access to Comet PoE

There are two methods to access Comet PoE via LAN.

**Method 1**. via Domain Name

Launch a browser on the controlling device. Chrome or Edge is recommended for better compatibility.

Enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

You will be able to access the Comet PoE's control panel locally, thus access the controlled device connected to it.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.png){class="glboxshadow"}

**Method 2**. via IP Address

Find the IP address of Comet PoE in the upper router, enter this IP address in the browser, and you will be able to access the Comet PoE locally, thus access the controlled device.

Take GL-AXT1800 as an example: Comet PoE is connected to the LAN port of GL-AXT1800 router via an Ethernet cable, and the controlled device is connected to Comet PoE correctly via HD cable and USB cable.

Log in to the web admin panel of GL-AXT1800, find the IP address of Comet PoE in the Client list, as shown below.

![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/local_access_via_ip.png){class="glboxshadow"}

Open a new tab in the browser, enter Comet PoE's IP in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

You will be able to access the Comet PoE's control panel locally, thus access the controlled device connected to it.

![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.png){class="glboxshadow"}

### Remote Access to Comet PoE

**Method 1**. via GLKVM App

1. Install the [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} on your controlling device.

2. Sign up and log in.
    
    Sign up for a GL.iNet account. If you already have one, skip this step.

    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/sign_up_account.png){class="glboxshadow"}
    
    Enter the username and password to log in.
    
    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/log_in_account.png){class="glboxshadow"}

4. Bind your device.

    If your Comet PoE and the controlling device are in the same local area network, click **Add Device**. It will start searching automatically.

    ![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow gl-90-desktop"}

    If your Comet PoE has not been detected or it is not in the same local network, click the **+** button in the upper right corner to add it manually.

    ![add manually](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_manually_1.png){class="glboxshadow gl-90-desktop"}

    Customize the device name and input the S/N, which can be found on the bottom label.

    ![add manually](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_manually_2.png){class="glboxshadow"}

    Binding device. Please ensure a stable network connection.

    ![binding](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/binding.png){class="glboxshadow gl-90-desktop"}
    
    Binding successful. Your Comet PoE has been bound to your account. Click **Done**.

    ![binding successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/binding_successful.png){class="glboxshadow gl-90-desktop"}

    You will be directed to the homepage, where your Comet PoE will be displayed Online.

    ![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow gl-90-desktop"}

    Click on it. Now you can access the Comet PoE's control panel remotely, thus access the controlled device connected to it.

    ![remote access via app](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/remote_control_panel.jpg){class="glboxshadow gl-90-desktop"}

**Method 2**. via Tailscale

Comet PoE integrates Tailscale, allowing you to bind it to the Tailscale virtual network for remote access.

In Comet PoE's control panel, navigate to Apps Center -> Tailscale, bind Comet PoE to your Tailscale account.

Next, bind your controlling device to the same account. Then you will be able to remotely access your Comet PoE by typing its Tailscale virtual IP into a web browser on the controlling device, without installing GLKVM app.

Click [here](../../faq/remote_access_to_controlled_device_via_tailscale.md){target="_blank"} for more instructions.

## Control Panel Introduction

### Settings

In the control panel, navigate to **Settings**, you will get a page as below.

![settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings.jpg){class="glboxshadow"}

#### Video

You can modify the video quality, orientation and EDID settings of the control page. 

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings-video.png){class="glboxshadow"}
    
- Quality: Adjust the video quality to low/medium/high according to your network and resolution requirements.

- Orientation: Adjust the control page rotation degree.

- EDID: Extended Display Identification Data. It aims to automatically match the display optimal parameters. The default configuration is suitable for most scenarios and usually does not need to be modified. Click [here](https://docs.gl-inet.com/kvm/en/faq/how_to_set_edid_for_glkvm/){target="_blank"} for details.

#### Remote Device Settings

You can adjust the relevant settings of the controlled device.

![settings-remote device settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings-remote_device_settings.png){class="glboxshadow"}

- Audio: Turn on or off the sound of the controlled device.

- Keyboard: Turn on or off the keyboard of the controlled device.

- Show Virtual Keyboard: Display and use the virtual keyboard on the control page.

    ![virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/virtual_keyboard.jpg){class="glboxshadow gl-90-desktop"}

- Mouse: Turn on or off the mouse of the controlled device.

- Show Local Cursor: Display the mouse of the current device on the screen.

- Mouse Jiggle: It is applied to prevent the computer from entering sleep due to prolonged inactivity (e.g., remote meetings, server management).

- Scroll Rate: It refers to the speed at which the mouse wheel scrolls or the number of lines/units scrolled per wheel rotation, affecting how quickly content moves on the remote.

- Scroll Direction: It determines whether scrolling the mouse wheel up/down moves content on the remote screen in the same direction (natural scrolling) or the opposite direction (traditional scrolling). 

    Four direction modes are available: Standard, Vertical Invert, Horizontal Invert, and Both Invert.  

- Mouse Mode: Including Absolute Mode and Relative Mode.

- Relative Sensitivity: It is available when the Mouse Mode is Relative.

#### System

![settings-system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings-system.png){class="glboxshadow"}

- Language: Switch the language of control panel. 

- Color Mode: Switch the theme color, including dark and light modes.

- Reset KVM

### Toolbox

In the control panel, navigate to **Toolbox**.

![toolbox](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox.jpg){class="glboxshadow"}

#### Clipboard

The clipboard allows you to easily paste text from the controlling device to the controlled device, without the need to transfer files.

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-clipboard.png){class="glboxshadow"}

#### Shortcut

It shows some common shortcut options. 

![toolbox-shortcut](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-shortcut.png){class="glboxshadow"}

Click **Show All** to show all shortcut options.

![toolbox-shortcut-all](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-shortcut-all.png){class="glboxshadow"}  

Click **Modify** to adjust the shortcut options.

![toolbox-shortcut-modify](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-shortcut-modify.png){class="glboxshadow"}  

#### Wake On Lan

Wake-on-LAN (WOL) is a technology that allows the controlled device to be remotely powered on or awakened from a low-power state.

Click **Add Device** to choose a device from the same LAN and set up Wake-on-LAN.

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-wol.png){class="glboxshadow"}  

#### Terminal

You can access the terminal of Comet to perform advanced settings.

![toolbox-terminal-1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-terminal-1.png){class="glboxshadow"}

Click **Access**, you will be re-directed to the GLKVM terminal, as shown below.

![toolbox-terminal-2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-terminal-2.png){class="glboxshadow"}

### Accessories

GL.iNet offers optional accessories for KVM devices to provide additional convenience for remote management. 

Firstly, connect the accessories to the controlled device. Please refer to the user guide of the corresponding accessories.

- [GL-Fingerbot (GL-FGB-01)](../gl-fgb-01/index.md){target="_blank"}

- [GL-ATX Board](../gl-atx-board/index.md){target="_blank"}

Then log in to the control panel, navigate to **Accessories**. 

![accessories](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/accessories.png){class="glboxshadow"}

**Note**: Accessory settings are only displayed after installation.

#### Fingerbot
    
The Fingerbot is adhered to the physical power button of the controlled device, to achieve remote control of the controlled device's power supply.
    
It works as per the following settings.

- Time: The duration for which the Fingerbot presses.

- Strength: Two levels of pressing strength are provided: Light Press mode and Hard Press mode.

    - Light Press Mode: Perfect for short or soft-touch buttons.
        
    - Hard Press Mode: Ideal for deep or firm buttons.

    ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

#### ATX Power

The ATX Board is installed in the computer host box to achieve remote control of the controlled device's power on/off/reboot.

It works as per the following settings.

- Power: Provides short press and long press functions.

- Restart: Restart the device.

### Virtual Media

Comet PoE allows you to transfer files between the host controlling device and the controlled device.

In the control panel, navigate to **Virtual Media**.

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/virtual_media_1.png){class="glboxshadow"}

Drag or click the box to upload files from host, or upload from URL. 

As an example, two images have been uploaded from the controlling device to the Comet PoE here.

![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/virtual_media_2.png){class="glboxshadow"}

Click **Mount To Remote**, two options are provided: **File Sharing** and **Image Mounting**.

![mount to remote](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/mount_to_remote.jpg){class="glboxshadow"}
    
#### File Sharing

It Emulates a read-write USB drive. Upload the files from the host to the Comet PoE and transfer to the controlled device.

Click on **File Sharing**, and a window will pop up in the upper-right corner of the control panel to display file sharing steps. Click "Don't remind me" to hide this prompt.  
    
![file sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/file_sharing_1.png){class="glboxshadow"}

Then turn to the Comet PoE's control panel, go to **This PC** of your controlled device, find a Drive named **GLKVM**. 
    
Now you can view, move or delete the files in this drive.

![file sharing 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/file_sharing_2.png){class="glboxshadow"}
    
#### Image Mounting

It emulates a read-only CD-Rom, supports BIOS/UEFI boot, for system reinstallation or ISO-based software installation.

Comet PoE can simulate a read-only virtual CD/DVD or disk drive on the target host. You can access this drive during the BIOS or UEFI startup process. 
    
This function can help you reinstall the operating system or mount an ISO to install applications on the target host and other tasks.
    
Click on **Image Mounting**, in the pop-up Mount Settings, select the file and ensure this file can be mounted as an iso format, then click **Mount Image**. 

![image mounting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/image_mounting.png){class="glboxshadow"}

Then you can use this file on the controlled end.

### Apps Center

In the control panel, navigate to **Apps Center**, the integrated applications can be found here.

![image mounting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/apps_center.jpg){class="glboxshadow"}

#### Tailscale

Comet PoE integrates with Tailscale, allowing you to bind it to the Tailscale virtual network for remote access.

In the control panel, navigate to Apps Center -> Tailscale, bind Comet PoE to your Tailscale account, then you can remotely access it by typing its Tailscale virtual IP into a web browser on the controlling device, without installing GLKVM app.

![tailscale](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/tailscale.png){class="glboxshadow"}

More instructions about Tailscale, please refer to [Tailscale documentation](https://tailscale.com/kb){class="_blank"}.

### Help

Here you can find more information about GL.iNet KVM and help documentation, as well as export logs for troubleshooting.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/help.jpg){class="glboxshadow"}

### System Settings

In the control panel, navigate to the upper-right corner to access the following system functions and options:

- Collapse Toolbar
- Full-Screen
- Upgrade Firmware
- Cloud Service
- Security (including Change Admin Password and 2FA Auth)
- Reboot
- Logout

#### Upgrade

Local and Online Upgrades are supported.

![upgrade firmware](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/firmware_upgrade.jpg){class="glboxshadow"}

#### Cloud Service

GL.iNet KVM panel can be accessed locally, so as to manage the controlled device under local network. Click [here](#local-access-to-the-controlled-device) for more details.

If you want to access the controlled device remotely, we suggest you download the App to use Cloud service.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/cloud_service.png){class="glboxshadow"}

#### Security

- Change Admin Password.

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/change_password.png){class="glboxshadow gl-60-desktop"}

- 2FA Auth: Enable two-factor authentication to protect your account.

## Accessory Guide

GL.iNet offers optional accessories for KVM devices to provide additional convenience for remote management.

### Fingerbot

The Fingerbot, acting as a physical button emulator, is designed to enable remote control of physical power button on the controlled device. 

Remove the cover above the Fingerbot to find a USB Bluetooth Receiver, and insert it into the USB port of Comet PoE. 

Attach the Fingerbot to the controlled device, ensure that the robotic arm of the Fingerbot can reach the physical power button of the controlled device when pressed downward, so as to achieve control of the power supply of the controlled device.

Then log in to the Comet PoE's control panel, go to [Accessories](#accessories) to customize the Fingerbot settings.

Please refer to [GL-Fingerbot (FGB-01) User Guide](../gl-fgb-01/index.md){target="_blank"} for details.

### ATX Board

The ATX Board, acting as a smart power management module, enables remote control of the controlled device's power supply by simulating physical power button operations (power on/off/reboot). 

Unlike the Fingerbot, which controls device through physical button presses, the ATX main board will be directly installed in the controlled device's host box, providing more concealed and stable power management.

Please refer to [GL-ATX Board User Guide](../gl-atx-board/index.md){target="_blank"} for details.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.