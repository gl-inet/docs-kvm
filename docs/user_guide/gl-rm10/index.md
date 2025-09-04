# Comet Pro (GL-RM10) User Guide

## Product Overview

Comet Pro (GL-RM10) is a remote KVM over Wi-Fi solution, tailored for seamless remote control and device management.

It is powered by a Qual-Core A53 CPU, equipped with 1GB DDR3 memory and 32GB eMMC storage to ensure smoothness. With the touchscreen display, you can view the device's IP address at a glance and perform basic operations such as Wi-Fi connection.

In terms of connectivity, Comet Pro supports Dual Band Wi-Fi 6, enabling stable and high-speed network connections. It also offers video passthrough functionality, allowing for the direct transmission of video signals with no quality loss. With support for 4K@30FPS video output, it provides a high-definition visual experience during remote control. 

Whether for personal or professional use, Comet Pro is an excellent choice for efficient remote device management.

## Appearance

![appearance 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/appearance-1.jpg){class="glboxshadow"}

![appearance 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/appearance-2.png){class="glboxshadow"}

## Quick Setup Guide

### Connect the Devices

For clarity, the controlling device is referred to as Device A, and the controlled device as Device B.

![connect devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/connect-device.png){class="glboxshadow" width="535"}

1. Connect the Comet Pro to the power source.

    ![power on](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/01-power-on.png){class="glboxshadow"}

2. Use an HD cable to connect the Comet Pro's HD IN port to the HD OUT port of the Device B. Use another HD cable to connect the Comet Pro's HD OUT port to the monitor if the Device B is a desktop computer.

    ![Connect the HD cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/02-hd-cable.png){class="glboxshadow" width="500"}

3. Connect the Comet Pro's USB Type-C port to the USB interface of the Device B using a USB cable.

    ![Connect the USB cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/03-usb-cable.png){class="glboxshadow" width="500"}

4. Connect the Comet Pro to a network source via an Ethernet cable or Wi-Fi.

    - Ethernet: Connect the Comet Pro's Ethernet port to a network source.

        ![Connect via ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/04-ethernet.png){class="glboxshadow" width="466"}

    - Wi-Fi: Swipe left on the touchscreen, connect Comet Pro to an existing Wi-Fi network (2.4G/5G supported).

        ![Connect via wifi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/04-wifi.png){class="glboxshadow" width="466"}

5. Device connection is complete. 

    Now you can access Comet Pro's control panel locally or remotely.

### Local Access to Comet Pro

There are two methods to access Comet Pro via LAN.

**Method 1**. via Domain

First, ensure your controlling device is on the same LAN as your Comet Pro.

Launch a browser on the controlling device. Chrome or Edge is recommended for better compatibility.

Enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow gl-90-desktop"}

You will be able to access Comet Pro's control panel locally, thus access the controlled device connected to it.

![local access via domain](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/local-access-domain.png){class="glboxshadow gl-90-desktop"}

**Method 2**. via IP address

Find Comet Pro's IP address on the touchscreen, enter this IP address in the browser, and you will be able to access it locally, thus access the controlled device.

For example, if the Comet Pro's IP address is `192.168.8.190`. 

Open a new tab in the browser and enter this IP in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/local_access_login.png){class="glboxshadow gl-90-desktop"}

You will be able to access the Comet Pro's control panel locally, thus access the controlled device connected to it.

![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/local-access-ip.png){class="glboxshadow gl-90-desktop"}

### Remote Access to Comet Pro

**Method 1**. via Cloud service

1. Bind your device to KVM Cloud.

    This needs to be done within the local network.

    First, locally access your Comet Pro, and go to the Cloud Service in the upper right corner. Click **Access Cloud**.

    ![access cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/access_cloud.jpg){class="glboxshadow"}

    You will be re-directed to a login page. Input your glinet account and click **Log In**.

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow gl-90-desktop"}

    Confirm your device info, and click **Bind**.

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow gl-90-desktop"}

    Wait a second and your Comet Pro will be bound to your account successfully. Click **Done**.

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow gl-90-desktop"}

2. Remote access via Cloud service.

    Open a browser (take Google Chrome as an example), and enter `glkvm.com` in the address bar. You will see a login page. Use your glinet account to log in.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow gl-90-desktop"}

    After login, you will see the devices bound to your account. Click on the device you want to remotely access.

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow gl-90-desktop"}

    It will open a new tab asking for device admin password. Enter the admin password and log in.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow gl-90-desktop"}

    Then you will be able to access your Comet Pro and the controlled device remotely via Cloud, without installing the app.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.jpg){class="glboxshadow gl-90-desktop"}

**Method 2**. via GLKVM App

1. Install the [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} on your controlling device.

2. Sign up and log in.
    
    Sign up for a GL.iNet account. If you already have one, skip this step.

    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/sign_up_account.png){class="glboxshadow"}
    
    Enter the username and password to log in.
    
    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/log_in_account.png){class="glboxshadow"}

4. Bind your device.

    If your Comet Pro and the controlling device are in the same local area network, click **Add Device**. It will start searching automatically.

    ![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow gl-90-desktop"}

    If your Comet Pro has not been detected or it is not in the same local network, click the **+** button in the upper right corner to add it manually.

    ![add manually](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_manually_1.png){class="glboxshadow gl-90-desktop"}

    Customize the device name and input the S/N, which can be found on the bottom label.

    ![add manually](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_manually_2.png){class="glboxshadow"}

    Binding device. Please ensure a stable network connection.

    ![binding](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/binding.png){class="glboxshadow gl-90-desktop"}
    
    Binding successful. Your Comet Pro has been bound to your account. Click **Done**.

    ![binding successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/binding_successful.png){class="glboxshadow gl-90-desktop"}

    You will be directed to the homepage, where your Comet Pro will be displayed Online.

    ![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow gl-90-desktop"}

    Click on it, input the admin password (created during the first access), and you can remotely access the Comet Pro's control panel, thus access the controlled device connected to it.

    ![remote access via app](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/remote_access_via_app.png){class="glboxshadow gl-90-desktop"}

**Method 3**. via Tailscale

Comet Pro integrates with Tailscale, allowing you to remotely access it via Tailscale virtual network.

In the control panel, navigate to Apps Center -> Tailscale, bind your Comet Pro to your Tailscale account. 

Next, bind your controlling device to the same account. Then you will be able to remotely access your Comet Pro by typing its Tailscale virtual IP into a web browser on the controlling device, without installing GLKVM app.

Click [here](../../faq/remote_access_to_controlled_device_via_tailscale.md){target="_blank"} for more instructions.

## Control Panel Introduction

### Settings

In the control panel, navigate to **Settings**, you will get a page as below.

![settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/settings-1.png){class="glboxshadow"}

#### Video

You can modify the video quality, orientation and EDID settings of the control page. 

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings-video.jpg){class="glboxshadow"}
    
- Quality: Adjust the video quality to low/medium/high/ultra-high according to your network and resolution requirements.

- Orientation: Adjust the control page rotation degree.

- EDID: Extended Display Identification Data. It aims to automatically match the display optimal parameters. The default configuration is suitable for most scenarios and usually does not need to be modified. Click [here](https://docs.gl-inet.com/kvm/en/faq/how_to_set_edid_for_glkvm/){target="_blank"} for details.

- Mode: You can switch the mode between WebRTC H.264 and Direct H.264.

#### Remote Device Settings

You can adjust the relevant settings of the controlled device.

![settings-remote device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings-remote-device.png){class="glboxshadow"}

- Speaker: Control audio output from the controlled device (e.g., system sounds, video audio)

- Microphone: Transmit local audio input (e.g., your voice) to the controlled device for remote interaction.

- Keyboard: Turn on or off the keyboard of the controlled device.

- Show Virtual Keyboard: Display and use the virtual keyboard on the control page.

    ![virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/virtual-keyboard.png){class="glboxshadow gl-90-desktop"}

- Mouse: Turn on or off the mouse of the controlled device.

- Show Local Cursor: Display the mouse of the current device on the screen.

- Mouse Jiggle: This feature is available since firmware v1.3.0. 
    
    It is applied to prevent the computer from entering sleep due to prolonged inactivity (e.g., remote meetings, server management).

- Scroll Rate: It refers to the speed at which the mouse wheel scrolls or the number of lines/units scrolled per wheel rotation, affecting how quickly content moves on the remote.

- Scroll Direction: It determines whether scrolling the mouse wheel up/down moves content on the remote screen in the same direction (natural scrolling) or the opposite direction (traditional scrolling). 

    Four direction modes are available: Standard, Vertical Invert, Horizontal Invert, and Both Invert.  

- Mouse Mode: Including Absolute Mode and Relative Mode.

- Relative Sensitivity: It is available when the Mouse Mode is Relative.

#### System

You can change the system display settings of the control panel, or reset the device with one click.

![settings-system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/settings-system.jpg){class="glboxshadow"}

- Device Identity: Change or customize your KVM's identity recognized by the controlled device.

    Note that the EDID and device identification will remain synchronized; changing one of them will make the other one automatically updated to ensure correct recognition.

- Language: Switch the language of control panel. 

- Color Mode: Switch the theme color, including dark and light modes.

- Time Zone: You can change the time zone of the KVM control panel. This is only for the KVM control panel, not the system time of the controlled device.  

- Reset KVM: Factory reset your KVM with just one click.

#### Network

You can check Comet Pro's network details.

![settings-network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/settings-network.png){class="glboxshadow"}

As shown above, Comet Pro connects to the router via an Ethernet cable and Wi-Fi at the same time.

Click **Modify** to change the Ethernet or Wi-Fi settings.

![settings-network-modify](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/ethernet-settings.png){class="glboxshadow"}

### Toolbox

In the control panel, navigate to **Toolbox**.

![toolbox](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/toolbox.png){class="glboxshadow"}

#### Clipboard

The clipboard allows you to easily paste text from the controlling device to the controlled device, without the need to transfer files.

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-clipboard.png){class="glboxshadow"}

#### Shortcut

It shows some common shortcut options.

![toolbox-shortcut](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-shortcut.png){class="glboxshadow"}

Click **Show All** to show all shortcut options.

![toolbox-shortcut-all](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-shortcut-all.png){class="glboxshadow"}  

Click **Modify** to adjust the shortcut options.

![toolbox-shortcut-modify](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-shortcut-modify.png){class="glboxshadow gl-50-desktop"}  

#### Wake On Lan

Wake-on-LAN (WOL) is a technology that allows the controlled device to be remotely powered on or awakened from a low-power state.

Click **Add Device** to choose a device from the same LAN and set up Wake-on-LAN.

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-wol.png){class="glboxshadow"}  

#### Terminal

You can access the Comet Pro's terminal to perform advanced settings.

![toolbox-terminal-1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/toolbox-terminal-1.png){class="glboxshadow"}

Click **Access**, you will be re-directed to the GLKVM terminal, as shown below.

![toolbox-terminal-2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/access-terminal.png){class="glboxshadow"}

### Accessories

GL.iNet offers optional accessories for KVM devices, providing additional convenience for remote management. 

Firstly, connect the accessories to the controlled device. Please refer to the user guide of the corresponding accessories.

- [GL-Fingerbot (GL-FGB-01)](../gl-fgb-01/index.md){target="_blank"}

- [GL-ATX Board](../gl-atx-board/index.md){target="_blank"}

Then log in to the control panel, navigate to **Accessories**. 

![accessories](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/accessories.png){class="glboxshadow"}

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

Comet Pro allows you to transfer files between the host controlling device and the controlled device.

In the control panel, navigate to **Virtual Media**.

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/virtual_media.png){class="glboxshadow"}

Drag or click the box to upload files from host, or upload from URL. 

As an example, two images have been uploaded from the host controlling device to the Comet Pro here.

![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/upload-files.png){class="glboxshadow"}

Click **Mount To Remote**, two options are provided: **File Sharing** and **Image Mounting**.

![mount to remote](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/mount_to_remote.jpg){class="glboxshadow"}
    
#### File Sharing

It Emulates a read-write USB drive. Upload the files from the host to the Comet Pro and transfer to the controlled device.

Click on **File Sharing**, and a window will pop up in the upper-right corner of the control panel to display file sharing steps. Click "Don't remind me" to hide this prompt.  
    
![file sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/file_sharing_1.png){class="glboxshadow"}

Then turn to the Comet Pro's control panel, go to **This PC** of your controlled device, and find a Removable Disk. Some operating systems may display its name as **GLKVM**. 

Now you can view, move or delete the files in this drive.

![file sharing 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/file-sharing-icon.png){class="glboxshadow"}
    
#### Image Mounting

It emulates a read-only CD-Rom, supports BIOS/UEFI boot, for system reinstallation or ISO-based software installation.

Comet Pro can simulate a read-only virtual CD/DVD or disk drive on the target host. You can access this drive during the BIOS or UEFI startup process. 
    
This function can help you reinstall the operating system or mount an ISO to install applications on the target host and other tasks.
    
Click on **Image Mounting**, in the pop-up Mount Settings, select the file and ensure this file can be mounted as an iso format, then click **Mount Image**. 

![image mounting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/image_mounting.png){class="glboxshadow"}

Then you can use this file on the controlled end.

### Apps Center

In the control panel, navigate to **Apps Center**, the integrated applications can be found here.

![image mounting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/apps_center.png){class="glboxshadow"}

#### Tailscale

Comet Pro integrates with Tailscale, allowing you to remotely access it via Tailscale virtual network.

In the control panel, navigate to Apps Center -> Tailscale, bind Comet Pro and your controlling device to your Tailscale account. Then you can remotely access it by typing its Tailscale virtual IP into a web browser on the controlling device, without installing GLKVM app.

Click [here](../../faq/remote_access_to_controlled_device_via_tailscale.md){target="_blank"} for more instructions.

Once enabled, the page will show the bind account.

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/tailscale_enabled.png){class="glboxshadow"}

### Help

Here you can find more information about GL.iNet KVM and help documentation, as well as export logs for troubleshooting.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/help.png){class="glboxshadow"}

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

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/firmware_upgrade.png){class="glboxshadow"}

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

### Fingerbot

The Fingerbot, acting as a physical button emulator, is designed to enable remote control of physical power button on the controlled device. 

Remove the cover above the Fingerbot to find a USB Bluetooth Receiver, and insert it into the USB port of Comet Pro. 

Attach the Fingerbot to the controlled device, ensure that the robotic arm of the Fingerbot can reach the physical power button of the controlled device when pressed downward, so as to achieve control of the power supply of the controlled device.

Then log in to Comet Pro's control panel, go to [Accessories](#accessories) to customize the Fingerbot settings.

Please refer to [GL-Fingerbot (FGB-01) User Guide](../gl-fgb-01/index.md){target="_blank"} for details.

### ATX Board

The ATX Board, acting as a smart power management module, enables remote control of the controlled device's power supply by simulating physical power button operations (power on/off/reboot). 

Unlike the Fingerbot, which controls device through physical button presses, the ATX main board will be directly installed in the controlled device's host box, providing more concealed and stable power management.

Please refer to [GL-ATX Board User Guide](../gl-atx-board/index.md){target="_blank"} for details.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.