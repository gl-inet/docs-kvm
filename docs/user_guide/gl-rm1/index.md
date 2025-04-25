# Comet (GL-RM1) User Guide

GL-RM1 is an open-source remote KVM device with a wide range of applications. You can use it to remote control your home computer when away from home, access to local resources, etc. It supports remote control of offline devices, allowing you to handle computer boot failures and adjust BIOS settings. It also has a remote file transfer function, enabling easy data transfer for both online and offline computers. With audio support, it provides a more immersive remote interaction experience. In a word, it is an essential tool for remote work and device management.

## Quick Setup Guide

This section will guide you how to set up GL-RM1 quickly. Connect the device, remote and local access to the controlled device.

### Connect the Devices

![connect devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/01_controlling-device-and-device-being-controlled.jpg){class="glboxshadow"}

1. Connect the GL-RM1 to the power source to power it on.
    ![Connect the GL-RM1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/02_power-on.jpg){class="glboxshadow"}

2. Use an HDMI cable to connect the GL-RM1's HDMI-IN port to the HDMI-OUT port of the Device B.
    ![HDMI cable to connect the GL-RM1's HDMI-IN port](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/03_hdmi.jpg){class="glboxshadow"}

3. Connect the GL-RM1's USB-Device port to the USB interface of the Device B using a USB cable.
    ![Connect the GL-RM1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/04_usb-cable.jpg){class="glboxshadow"}

4. Plug the GL-RM1's Ethernet port to a network source.
    ![Connect the GL-RM1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/05_ethernet.jpg){class="glboxshadow"}

### LED Explanation

| LED Status               | Indication                        |
| :----------------------- | :-------------------------------- |
| Solid Blue               | Starting up                       |
| Flashing White           | Started up but No Internet        |
| Solid White              | Connected to Internet             |
| Flashing Blue & White    | Firmware Upgrading                |

### Button Explanation

| Function                   | Operation                                | LED Indication                        |
| :------------------------- | :--------------------------------------- | :------------------------------------ |
| Enter U-Boot Flashing Mode | With device powered on, press and hold <br>the button for more than 3s then release | Pressing the button: Flashing Blue <br>Entered U-Boot mode: Solid Blue      |
| Reset                      | With device powered on, press and hold <br>the button for 8-20s then release        | Pressing for 1-8s: Slowly Flashing <br>Pressing for 8-20s: Quickly Flashing |

### Remote Access to the Controlled Device

Follow the steps below.

1. Install the [App](https://link.gl-inet.com/label-rm1-app/){target="_blank"} on your remote controlling device.

2. Register an Account.
    
    Register a glinet account. If you already have one, skip this step.

    ![sign up](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/sign_up_account.png){class="glboxshadow gl-80-desktop"}

3. Log in to your Account.

    Enter the username and password to log in.
    
    ![log in](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/log_in.png){class="glboxshadow gl-80-desktop"}

4. Bind your GL-RM1.

    There are two methods to bind GL-RM1 to your account.

    === "Bind via Local Area Network"
    
        Please ensure that the current Controlling Device is in the same local area network as the GL-RM1.

        Click "Add Device" and select your GL-RM1.

        ![add device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/add_device.png){class="glboxshadow gl-80-desktop"}

        ![select device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/select_device.jpg){class="glboxshadow gl-80-desktop"}

    === "Bind via Adding Manually"

        Click the "+" button in the upper right corner.

        ![click + button](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/add_button.jpg){class="glboxshadow gl-80-desktop"}

        Customize device name and input the S/N, which is printed on the label on the back of the device.

        ![add manually](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/add_manually.png){class="glboxshadow gl-80-desktop"}

You can now start using GL-RM1 to remote access the controlled device.

### Local Access to the Controlled Device

**Method 1**. Open a browser, enter `glkvm.local`, you will enter the local management page.

**Method 2**. Find the IP address of GL-RM1 in its upper router, enter this IP address in the browser, you will be able to access the controlled device through GL-RM1 locally.

Take GL-AXT1800 as an example. Here we connect the GL-RM1 to the LAN port of GL-AXT1800 router through an Ethernet cable, so GL-AXT1800 is the upper router. Log in to the web admin panel of GL-AXT1800, the IP address of GL-RM1 can be found in the Client list, as shown below.

![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/local_access_via_ip.png){class="glboxshadow"}

Now you can use this IP to access your controlled device locally via GL-RM1.

![local access](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/local_access.png){class="glboxshadow"}

## Function Introduction

### Settings

Move to the top navigation bar, click **Settings**, you will get a page as below.

![settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings.png){class="glboxshadow"}

- Video

    You can modify the video quality, orientation and EDID of GL-RM1 control page. 
    
    - Quality: Adjust the video quality to low/medium/high according to your network and resolution requirements.
    - Orientation: Adjust the rotation degree of GL-RM1 control page.
    - EDID: Extended Display Identification Data. It aims to automatically match the display optimal parameters. The default configuration is suitable for most scenarios and usually does not need to be modified. Refer to [this link](https://docs.gl-inet.com/kvm/en/faq/how_to_set_edid_for_glkvm/){target="blank"} for more details.

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

    Click [here](https://docs.gl-inet.com/kvm/en/user_guide/gl-rm1/#fingerbot) to find more details about FingerBot.

- ATX Power

    The ATX Board is another optional accessory. It is installed in the computer host box, enabling remote control of the controlled device's power supply (power on/off/reboot).

    - Power: Provides short press and long press functions.
    - Restart: Restart the device.

    Click [here](https://docs.gl-inet.com/kvm/en/user_guide/gl-rm1/#atx-package) to find more details about ATX package.

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

- Tailscale: You can bind this device to your own Tailscale account to manage it under Tailscale network.

    More instructions about Tailscale, please refer to [Tailscale documentation](https://tailscale.com/kb){class="blank"}.

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

Then you can log in to GL-RM1, go to [Accessories](https://docs.gl-inet.com/kvm/en/user_guide/gl-rm1/#accessories) to set the FingerBot.

**Note**: This product is not available yet.

### ATX Package

The ATX package is an optional accessory, the most important part of which is the AXT main board. Like a smart power management module, it enables remote control of the controlled device's power supply by simulating physical power button operations (power on/off/reboot). 

Unlike the FingerBot, which controls device through physical button presses, the ATX main board will be directly installed in the controlled device's host box, providing more concealed and stable power management.

#### Components

There are some components in the ATX Package box:

- ATX main board
- USB-A to Type-C cable
- 9 PIN Wire Set
- Screw package
- ATX Bracket Set

![components](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/components.png){class="glboxshadow gl-60-desktop"}

#### PIN-OUT of the ATX Board

![pinout](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/pinout.jpg){class="glboxshadow gl-80-desktop"}

Explanation of Interfaces:

1. Type-C Interface: Connect to the GL-RM1 device.
2. Firmware Upgrade button: for the single-chip microcomputer on the ATX main board.
3. Reset button.
4. Connect to the control line of the computer panel.
5. Connect to the F_PANEL interface of the computer.

!!! note

    Interfaces 4 and 5 can be connected interchangeably. That is, interface 5 can be connected to the control line of the computer panel, and interface 4 can be connected to the F_PANEL. The LED status on the board is consistent with the Power LED status on the computer panel.

Interfaces 4/5 diagram:

![interface](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/interface.png){class="glboxshadow gl-60-desktop"}

#### ATX Main Board Installation

Firstly, fix the ATX main board and the ATX Bracket Set with the screws provided.

![screwing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/screwing.png){class="glboxshadow gl-60-desktop"}

Secondly, connect interfaces ④ and ⑤ respectively to the controlled computer's control line and F_PANEL interface. 

The 9 PIN Wire Set provided in the ATX Package allows you to connect one of the ATX board interface 4/5 to the controlled computer's control line or F_PANEL interface. 
    
You need to use the wire set included in your computer host box to connect another ATX board interface 4/5 to the controlled computer's control line or F_PANEL interface.

Here are two examples of connecting one of the axt board interfaces 4/5 to the controlled computer's F_PANEL interface.

**Example 1. For 20-5 pin PANEL**

If the row of pins on the motherboard of your controlled computer for connecting to the control panel is 20-5 pin PANEL, as shown below.

![20-5pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/20-5pin_panel_1.jpg){class="glboxshadow"}

Please refer to the diagram below for connection, make sure that the silkscreen printing (i.e., the words HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) are visible facing outward and not obscured facing inward.

![20-5pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/20-5pin_panel_2.jpg){class="glboxshadow"}
<small>Example of the front view</small>

![20-5pin panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/20-5pin_panel_3.png){class="glboxshadow"}
<small>Example of the rear view</small>

Then use the wire set included in your computer host box to connect another ATX board interface to the computer control line.

**Example 2. For 10-1 pin PANEL**

If the row of pins on the motherboard of your controlled computer for connecting to the control panel is 10-1 pin PANEL, as shown below.

![10-1pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/10-1pin_panel_1.png){class="glboxshadow"}

Please refer to the diagram below for connection, make sure that the silkscreen printing (i.e., the words HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) are visible facing outward and not obscured facing inward.

![10-1pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/10-1pin_panel_2.jpg){class="glboxshadow"}
<small>Example of the front view</small>

![10-1pin panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/10-1pin_panel_3.jpg){class="glboxshadow"}
<small>Example of the rear view</small>

Then use the wire set included in your computer host box to connect another ATX board interface to the computer control line.

The final connected AXT board is shown below.

![axt board install 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/axt_board_install1.png){class="glboxshadow gl-60-desktop"}

Detailed front view of AXT board

![axt board install 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/axt_board_install2.jpg){class="glboxshadow"}

Detailed rear view of AXT board

![axt board install 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/axt_board_install3.jpg){class="glboxshadow"}

Thirdly, place the ATX board bracket on the side frame of the computer host box.

![axt board install 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/axt_board_install4.png){class="glboxshadow"}

Finally, connect the Type-C interface of ATX board to the USB-A interface of the GL-RM1, using the included USB-A to Type-C cable.

![axt board install 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/axt_board_install5.png){class="glboxshadow"}

![axt board install 6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/axt_board_install6.png){class="glboxshadow"}

This completes the installation of the AXT board. You can log in to the GL-RM1, navigate to [Accessories](https://docs.gl-inet.com/kvm/en/user_guide/gl-rm1/#accessories) to set the ATX power.

!!! Note

    If you can't turn on/off the controlled computer via GL-RM1 control page, please check the polarity of the wiring, try flipping the connector polarity to avoid wrong wiring.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.