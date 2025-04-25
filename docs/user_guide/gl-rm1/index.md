# Comet (GL-RM1) User Guide

Comet (GL-RM1) is an open-source remote KVM device with a wide range of applications. You can use it to remote control your home computer when away from home, access to local resources, etc. It supports remote control of offline devices, allowing you to handle computer boot failures and adjust BIOS settings. It also has a remote file transfer function, enabling easy data transfer for both online and offline computers. With audio support, it provides a more immersive remote interaction experience. In a word, it is an essential tool for remote work and device management.

## Product Overview

### Appearance

![appearance 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/appearance_1.jpg){class="glboxshadow"}

![appearance 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/appearance_2.jpg){class="glboxshadow"}

### LED

There is 1x LED on the top panel of Comet. Here's the LED explanation.

| LED Status               | Indication                        |
| :----------------------- | :-------------------------------- |
| Solid Blue               | Starting up                       |
| Flashing White           | Started up but No Internet        |
| Solid White              | Connected to Internet             |
| Flashing Blue & White    | Firmware Upgrading                |

### Button

There is 1x Button at the side panel of Comet. Here's the button explanation.

| Function                   | Operation                                | LED Indication                        |
| :------------------------- | :--------------------------------------- | :------------------------------------ |
| Enter U-Boot Flashing Mode | With device powered on, press and hold <br>the button for more than 3s then release | Pressing the button: Flashing Blue <br>Entered U-Boot mode: Solid Blue      |
| Reset                      | With device powered on, press and hold <br>the button for 8-20s then release        | Pressing for 1-8s: Slowly Flashing <br>Pressing for 8-20s: Quickly Flashing |

## Quick Setup Guide

### Connect the Devices

![connect devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/01_controlling-device-and-device-being-controlled.jpg){class="glboxshadow"}

1. Connect the Comet to the power source to power it on.
    ![Connect the GL-RM1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/02_power-on.jpg){class="glboxshadow"}

2. Use an HDMI cable to connect the Comet's HDMI-IN port to the HDMI-OUT port of the Device B.
    ![HDMI cable to connect the GL-RM1's HDMI-IN port](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/03_hdmi.jpg){class="glboxshadow"}

3. Connect the Comet's USB-Device port to the USB interface of the Device B using a USB cable.
    ![Connect the GL-RM1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/04_usb-cable.jpg){class="glboxshadow"}

4. Plug the Comet's Ethernet port to a network source.
    ![Connect the GL-RM1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/05_ethernet.jpg){class="glboxshadow"}

### Local Access to Comet

**Method 1**. via Domain Name

Open a browser, enter `glkvm.local`, you will enter the local management page.

**Method 2**. via IP Address

Find the IP address of Comet in the upper router, enter this IP address in the browser, you will be able to access the Comet locally, thus access the controlled device connected to Comet.

Take GL-AXT1800 as an example. Here we connect the Comet to the LAN port of GL-AXT1800 router through an Ethernet cable, so GL-AXT1800 is the upper router. Log in to the web admin panel of GL-AXT1800, find the IP address of Comet in the Client list, as shown below.

![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/local_access_via_ip.png){class="glboxshadow"}

Now we can use this IP to access Comet locally, thus access the controlled device.

![local access](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/local_access.png){class="glboxshadow"}

### Remote Access to Comet

**Method 1**. via GLKVM Application

1. Install the [GLKVM App](https://link.gl-inet.com/label-rm1-app/){target="_blank"} on your controlling device.

2. Register an Account.
    
    Register a GL.iNet account. If you already have one, skip this step.

    ![sign up](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/sign_up_account.png){class="glboxshadow gl-80-desktop"}

3. Log in to your Account.

    Enter the username and password to log in.
    
    ![log in](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/log_in.png){class="glboxshadow gl-80-desktop"}

4. Bind your device.

    There are two methods to bind Comet to your account.

    === "Bind via Local Area Network"
    
        Please ensure that the current Controlling Device is in the same local area network as the Comet.

        Click "Add Device", select your Comet.

        ![add device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/add_device.png){class="glboxshadow gl-80-desktop"}

        ![select device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/select_device.jpg){class="glboxshadow gl-80-desktop"}

    === "Bind via Adding Manually"

        Click the "+" button in the upper right corner.

        ![click + button](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/add_button.jpg){class="glboxshadow gl-80-desktop"}

        Customize device name and input the S/N, which is printed on the label on the back of the device.

        ![add manually](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/add_manually.png){class="glboxshadow gl-80-desktop"}

    You can now start using Comet to remote access the controlled device.

**Method 2**. via Tailscale

You can bind Comet to your Tailscale account, add it into your Tailscale virtual network. 

In this way, you can directly access Comet by typing its Tailscale virtual IP into a web browser on the controlling device, without installing GLKVM app.

More instructions about Tailscale, please refer to [Tailscale documentation](https://tailscale.com/kb){class="_blank"}.

## Function Introduction

### Settings

Move to the top navigation bar, click **Settings**, you will get a page as below.

![settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings.png){class="glboxshadow"}

- Video

    You can modify the video quality, orientation and EDID of GL-RM1 control page. 
    
    - Quality: Adjust the video quality to low/medium/high according to your network and resolution requirements.
    - Orientation: Adjust the rotation degree of GL-RM1 control page.
    - EDID: Extended Display Identification Data. It aims to automatically match the display optimal parameters. The default configuration is suitable for most scenarios and usually does not need to be modified. Refer to [this link](https://docs.gl-inet.com/kvm/en/faq/how_to_set_edid_for_glkvm/){target="_blank"} for more details.

- Remote Device Settings

    You can adjust the relevant settings of the controlled device.

    - Audio: Turn on or off the sound of the controlled device.
    - Mouse: Turn on or off the mouse of the controlled device.
    - Keyboard: Turn on or off the keyboard of the controlled device.
    - Show Virtual Keyboard: Whether to display and use the virtual keyboard on the control page.
    - Show Local Cursor: Whether to display the mouse of the current device on the screen.

- System

    - Language: Switch the language of control page. 
    - Color Mode: Switch the theme color, including dark and light modes.
    - Reset KVM

### Toolbox

In the top navigation bar, click  **Toolbox**.

![toolbox](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox.png){class="glboxshadow"}

- Clipboard

    The clipboard allows you to paste the text content of the control end into the controlled device.

- Shortcut

    Here are some common shortcut key options. Click "ALL" to show all options.

    ![all shortcuts](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/shortcut_all.png){class="glboxshadow"}  

- Wake On Lan

    Wake on LAN (WOL) is a technology that allows the controoled device to be remotely powered on or awakened from a low-power state.

    Click Add Device to set it up.

- Terminal

    Access Terminal: You can access the terminal of GL-RM1 through this function.

    ![access terminal](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/access_terminal.png){class="glboxshadow"} 

### Accessories

GL.iNet provides optional accessories, which you can connect to the GL-RM1 for use.

In the top navigation bar, click  **Accessories**.

![accessories](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/accessories.png){class="glboxshadow"}

- Fingerbot

    The FingerBot is an optional accessory. Acting as a physical button emulator, it is designed to enable remote control of physical power button on the controlled device.
    
    - Time: The duration for which the Fingerbot presses.
    - Strength: Two levels of pressing strength are provided.

    Click [here](#fingerbot) to find more details about FingerBot.

- ATX Power

    The ATX Board is another optional accessory. It is installed in the computer host box, enabling remote control of the controlled device's power supply (power on/off/reboot).

    - Power: Provides short press and long press functions.
    - Restart: Restart the device.

    Click [here](https://docs.gl-inet.com/kvm/en/user_guide/gl-atx-board/){target="_blank"} to find more details about ATX board.

### Virtual Media

GL-RM1 allows you to transfer files from the host to GL-RM1, and then from GL-RM1 to the controlled device.

In the top navigation bar, click  **Virtual Media**.

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/virtual_media.png){class="glboxshadow"}

You can drag or click the box to upload files from host or from URL. As an example, two images were uploaded from the host to the GL-RM1 here.

![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/upload_files_example.png){class="glboxshadow"}

You can perform operations such as deletion and download.

Click **Mount To Remote**, two options are provided: **File Sharing** and **Image Mounting**.
    
- File Sharing: Emulates a read-write USB drive. Upload the files to the KVM (GL-RM1) and transfer from the host to the remoted device.

    Click "File Sharing", a window will pop up in the upper right corner of the control page.
    
    ![file sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/file_sharing.png){class="glboxshadow"}

    Check the GL-RM1 control page, go to "This PC" of your controlled device, you will see a Drive named "GLKVM(F:)". Now you can view, move or delete the files in this drive.

    ![file sharing 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/file_sharing_2.jpg){class="glboxshadow"}
    
- Image Mounting: Emulates a read-only CD-Rom, supports BIOS/UEFI boot, for system reinstallation or ISO-based software installation.

    GL-RM1 can simulate a read-only virtual CD/DVD or disk drive on the target host. You can access this drive during the BIOS or UEFI startup process. This function can help you reinstall the operating system or mount an ISO to install applications on the target host and other tasks.
    
    Click "Image Mounting", in the Mount Settings, select the image you need and click "Mount Image". The image will be mounting. 

    ![image mounting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/image_mounting.png){class="glboxshadow"}

    Then you can use this file on the controlled end.

### Apps Center

In the top navigation bar, click  **Apps Center**.

![image mounting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/apps_center.png){class="glboxshadow"}

#### Tailscale

This feature is available since firmware v1.1.0

Bind Comet to your own Tailscale account, then you can remotly access it by its Tailscale virtual IP.

More instructions about Tailscale, please refer to [Tailscale documentation](https://tailscale.com/kb){class="_blank"}.

### Help

Here you can find more information about GL.iNet KVM, or export log for troubleshooting.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/help.png){class="glboxshadow"}

### System

In the upper right corner, you can adjust the screen size, such as collapsing the toolbar or enabling full-screen display. You can also upgrade firmware, enable Cloud service, change admin password, and restart/logout of your GL-RM1.

- Upgrade

    Local and Online Upgrades are supported.

    ![upgrade firmware](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/upgrade_firmware.png){class="glboxshadow"}

- Cloud Service

    GL.iNet KVM panel can be accessed locally, so as to manage the controlled device under local network. Click [here](#local-access-to-the-controlled-device) for more details.

    If you want to access the controlled device remotely, please download the App to use Cloud service.

    ![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/cloud_service.png){class="glboxshadow"}

- Security

    - Change Admin Password.

        ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/change_password.png){class="glboxshadow gl-60-desktop"}

    - 2FA Code: Enable two-factor authentication to protect your account.

## Accessories

GL.iNet provides standard accessories that you can connect to the GL-RM1.

### FingerBot

The FingerBot, acting as a physical button emulator, is designed to enable remote control of physical power button on the controlled device. 

Remove the cover above the FingerBot to find a USB wireless receiver, and insert it into the USB port of GL-RM1. Then attach the FingerBot to the physical power button of the controlled device, it will be able to remote control the ON/OFF of the controlled device by physically pressing the power button.

Then you can log in to GL-RM1, go to [Accessories](#accessories) to set the FingerBot.

**Note**: This product is not available yet.

### ATX Board

The ATX Board is an optional accessory. Like a smart power management module, it enables remote control of the controlled device's power supply by simulating physical power button operations (power on/off/reboot). 

Unlike the FingerBot, which controls device through physical button presses, the ATX main board will be directly installed in the controlled device's host box, providing more concealed and stable power management.

Please refer to [GL-ATX Board User Guide](https://docs.gl-inet.com/kvm/en/user_guide/gl-atx-board/){target="_blank"} for details.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.