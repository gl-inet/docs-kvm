# Comet (GL-RM1) User Guide

Comet (GL-RM1) is a remote KVM device with a wide range of applications. You can use it to remote control your home computer when away from home, access to local resources, etc. It supports remote control of offline devices, allowing you to handle computer boot failures and adjust BIOS settings. It also has a remote file transfer function, enabling easy data transfer for both online and offline computers. With audio support, it provides a more immersive remote interaction experience. In a word, it is an essential tool for remote work and device management.

## Product Overview

### Appearance

![appearance 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/appearance_1.jpg){class="glboxshadow"}

![appearance 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/appearance_2.jpg){class="glboxshadow"}

### LED

There is 1x LED on the top panel of Comet.

| LED Status               | Indication                        |
| :----------------------- | :-------------------------------- |
| Solid Blue               | Starting up                       |
| Flashing White           | Started up but No Internet        |
| Solid White              | Connected to Internet             |
| Flashing Blue & White    | Firmware Upgrading                |

### Button

There is 1x Button at the side panel of Comet.

| Function                   | Operation                                | LED Indication                        |
| :------------------------- | :--------------------------------------- | :------------------------------------ |
| Enter U-Boot Flashing Mode | With device powered on, press and hold <br>the button for more than 3s then release | Pressing the button: Flashing Blue <br>Entered U-Boot mode: Solid Blue      |
| Reset                      | With device powered on, press and hold <br>the button for 8-20s then release        | Pressing for 1-8s: Slowly Flashing <br>Pressing for 8-20s: Quickly Flashing |

## Quick Setup Guide

### Connect the Devices

For clarity, the controlling device is referred to as Device A, and the controlled device as Device B.

![connect devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/01_controlling-device-and-device-being-controlled.jpg){class="glboxshadow"}

1. Connect the Comet to the power source.
    ![Connect the GL-RM1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/02_power-on.jpg){class="glboxshadow"}

2. Use an HDMI cable to connect the Comet's HDMI-IN port to the HDMI-OUT port of the Device B.
    ![HDMI cable to connect the GL-RM1's HDMI-IN port](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/03_hdmi.jpg){class="glboxshadow"}

3. Connect the Comet's USB-Device port to the USB interface of the Device B using a USB cable.
    ![Connect the GL-RM1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/04_usb-cable.jpg){class="glboxshadow"}

4. Plug the Comet's Ethernet port to a network source.
    ![Connect the GL-RM1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/05_ethernet.jpg){class="glboxshadow"}

5. Device connection is complete. 

    You can now access the Comet's control panel locally via a browser on the controlling device, or download the GLKVM app on the controlling device to remotely access it.

### Local Access to Comet

Watch this video to access Comet via LAN, or follow the steps below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/PlJ5JLt7aUo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Method 1**. via Domain Name

Launch a browser on your controlling device, enter `glkvm.local`, you will enter the local management page.

**Method 2**. via IP Address

Find the IP address of Comet in the upper router, enter this IP address in the browser, you will be able to access the Comet locally, thus access the controlled device connected to it.

Take GL-AXT1800 as an example. Here the Comet is connected to the LAN port of GL-AXT1800 router through an Ethernet cable, so GL-AXT1800 is the upper router. Log in to the web admin panel of GL-AXT1800, find the IP address of Comet in the Client list, as shown below.

![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/local_access_via_ip.png){class="glboxshadow"}

Then we can use this IP to access Comet locally, thus access the controlled device.

![local access](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/local_access.png){class="glboxshadow"}

### Remote Access to Comet

**Method 1**. via GLKVM Application

1. Install the [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} on your controlling device.

2. Register an Account.
    
    Register a GL.iNet account. If you already have one, skip this step.

    ![sign up](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/sign_up_account.jpg){class="glboxshadow gl-80-desktop"}

3. Log in to your Account.

    Enter the username and password to log in.
    
    ![log in](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/log_in.png){class="glboxshadow gl-80-desktop"}

4. Bind your device.

    There are two methods to bind Comet to your account.

    === "Bind via Local Area Network"
    
        Please ensure that the current Controlling Device is in the same local area network as the Comet.

        Click "Add Device", select your Comet.

        ![add device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/add_device.jpg){class="glboxshadow gl-80-desktop"}

        ![select device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/select_device.png){class="glboxshadow gl-80-desktop"}

    === "Bind via Adding Manually"

        Click the "+" button in the upper right corner.

        ![click + button](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/add_button.png){class="glboxshadow gl-80-desktop"}

        Customize device name and input the S/N, which is printed on the label on the back of the device.

        ![add manually](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/add_manually.png){class="glboxshadow gl-80-desktop"}

    You can now start using Comet to remote access the controlled device.

**Method 2**. via Tailscale

Comet integrates with Tailscale since firmware v1.1.0, allowing you to bind it to the Tailscale virtual network for remote access.

In Comet's control panel, navigate to Apps Center -> Tailscale, bind Comet to your Tailscale account, then you can remotely access it by typing its Tailscale virtual IP into a web browser on the controlling device, without installing GLKVM app.

More instructions about Tailscale, please refer to [Tailscale documentation](https://tailscale.com/kb){class="_blank"}.

## Control Panel Introduction

### Settings

In the control panel, navigate to **Settings**, you will get a page as below.

![settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings.jpg){class="glboxshadow"}

#### Video

You can modify the video quality, orientation and EDID settings of the control page. 
    
- Quality: Adjust the video quality to low/medium/high according to your network and resolution requirements.

- Orientation: Adjust the control page rotation degree.

- EDID: Extended Display Identification Data. It aims to automatically match the display optimal parameters. The default configuration is suitable for most scenarios and usually does not need to be modified. Click [here](https://docs.gl-inet.com/kvm/en/faq/how_to_set_edid_for_glkvm/){target="_blank"} for details.

#### Remote Device Settings

You can adjust the relevant settings of the controlled device.

- Audio: Turn on or off the sound of the controlled device.

- Keyboard: Turn on or off the keyboard of the controlled device.

- Show Virtual Keyboard: Whether to display and use the virtual keyboard on the control page.

- Mouse: Turn on or off the mouse of the controlled device.

- Show Local Cursor: Whether to display the mouse of the current device on the screen.

- Mouse Jiggle: This feature is available since firmware v1.3. 
    
    It is applied to prevent the computer from entering sleep due to prolonged inactivity (e.g., remote meetings, server management).

- Scroll Rate: It refers to the speed at which the mouse wheel scrolls or the number of lines/units scrolled per wheel rotation, affecting how quickly content moves on the remote.

- Scroll Direction: It determines whether scrolling the mouse wheel up/down moves content on the remote screen in the same direction (natural scrolling) or the opposite direction (traditional scrolling). 

    Four direction modes are available: Standard, Vertical Invert, Horizontal Invert, and Both Invert.  

- Mouse Mode: Including Absolute Mode and Relative Mode.

- Relative Sensitivity: It is available when the Mouse Mode is Relative.

#### System

- Language: Switch the language of control panel. 

- Color Mode: Switch the theme color, including dark and light modes.

- Reset KVM

### Toolbox

In the control panel, navigate to **Toolbox**.

![toolbox](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox.jpg){class="glboxshadow"}

#### Clipboard

The clipboard allows you to easily paste text from the controlling device to the controlled device, without the need to transfer files.

#### Shortcut

It shows some common shortcut key options. Click "ALL" to show all options.

![all shortcuts](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/shortcut_all.png){class="glboxshadow"}  

#### Wake On Lan

Wake on LAN (WOL) is a technology that allows the controlled device to be remotely powered on or awakened from a low-power state.

Click Add Device to set it up.

#### Terminal

Access Terminal: You can access the terminal of Comet through this function.

![access terminal](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/access_terminal.png){class="glboxshadow"} 

### Accessories

GL.iNet offers optional accessories for KVM devices to provide additional convenience for remote management. 

Firstly, connect the accessories to the controlled device. For Fingerbot, please click [here](#fingerbot). For ATX board, please click [here](https://docs.gl-inet.com/kvm/en/user_guide/gl-atx-board/){target="_blank"}.

Then log in to the control panel, navigate to **Accessories**. 

![accessories](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/accessories.jpg){class="glboxshadow"}

**Note**: Accessory settings are only displayed after installation.

#### Fingerbot
    
The Fingerbot is adhered to the physical power button of the controlled device, to achieve remote control of the controlled device's power supply.
    
It works as per the following settings.

- Time: The duration for which the Fingerbot presses.

- Strength: Two levels of pressing strength are provided.

#### ATX Power

The ATX Board is installed in the computer host box to achieve remote control of the controlled device's power on/off/reboot.

It works as per the following settings.

- Power: Provides short press and long press functions.

- Restart: Restart the device.

### Virtual Media

Comet allows you to transfer files between the host controlling device and the controlled device.

In the control panel, navigate to **Virtual Media**.

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/virtual_media.jpg){class="glboxshadow"}

Drag or click the box to upload files from host, or upload from URL. 

As an example, two images have been uploaded from the host controlling device to the Comet here.

![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/upload_files_example.png){class="glboxshadow"}

Click **Mount To Remote**, two options are provided: **File Sharing** and **Image Mounting**.

![mount to remote](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/mount_to_remote.jpg){class="glboxshadow"}
    
#### File Sharing

It Emulates a read-write USB drive. Upload the files from the host to the Comet and transfer to the controlled device.

Click on **File Sharing**, and a window will pop up in the upper-right corner of the control panel to display file sharing steps. Click "Don't remind me" to hide this prompt.  
    
![file sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/file_sharing_1.png){class="glboxshadow"}

Then turn to the Comet's control panel, go to **This PC** of your controlled device, find a Drive named **GLKVM(G:)**. 

Now you can view, move or delete the files in this drive.

![file sharing 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/file_sharing_2.png){class="glboxshadow"}
    
#### Image Mounting

It emulates a read-only CD-Rom, supports BIOS/UEFI boot, for system reinstallation or ISO-based software installation.

Comet can simulate a read-only virtual CD/DVD or disk drive on the target host. You can access this drive during the BIOS or UEFI startup process. 
    
This function can help you reinstall the operating system or mount an ISO to install applications on the target host and other tasks.
    
Click on **Image Mounting**, in the pop-up Mount Settings, select the file and ensure this file can be mounted as an iso format, then click **Mount Image**. 

![image mounting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/image_mounting.png){class="glboxshadow"}

Then you can use this file on the controlled end.

### Apps Center

In the control panel, navigate to **Apps Center**, the integrated applications can be found here.

![image mounting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/apps_center.jpg){class="glboxshadow"}

#### Tailscale

Comet integrates with Tailscale, allowing you to bind it to the Tailscale virtual network for remote access.

In the control panel, navigate to Apps Center -> Tailscale, bind Comet to your Tailscale account, then you can remotely access it by typing its Tailscale virtual IP into a web browser on the controlling device, without installing GLKVM app.

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

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/firmware_upgrade.jpg){class="glboxshadow"}

#### Cloud Service

GL.iNet KVM panel can be accessed locally, so as to manage the controlled device under local network. Click [here](#local-access-to-the-controlled-device) for more details.

If you want to access the controlled device remotely, we suggest you download the App to use Cloud service.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/cloud_service.jpg){class="glboxshadow"}

#### Security

- Change Admin Password.

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/change_password.png){class="glboxshadow gl-60-desktop"}

- 2FA Auth: Enable two-factor authentication to protect your account.

## Accessory Guide

GL.iNet offers optional accessories for KVM devices to provide additional convenience for remote management.

### FingerBot

The FingerBot, acting as a physical button emulator, is designed to enable remote control of physical power button on the controlled device. 

Remove the cover above the FingerBot to find a USB wireless receiver, and insert it into the USB port of Comet. 

Attach the Fingerbot to the controlled device, ensure that the robotic arm of the Fingerbot can reach the physical power button of the controlled device when pressed downward, so as to achieve control of the power supply of the controlled device.

Then log in to Comet's control panel, go to [Accessories](#accessories) to set the FingerBot.

**Note**: This product is not available yet.

### ATX Board

The ATX Board, acting as a smart power management module, enables remote control of the controlled device's power supply by simulating physical power button operations (power on/off/reboot). 

Unlike the FingerBot, which controls device through physical button presses, the ATX main board will be directly installed in the controlled device's host box, providing more concealed and stable power management.

Please refer to [GL-ATX Board User Guide](https://docs.gl-inet.com/kvm/en/user_guide/gl-atx-board/){target="_blank"} for details.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.