# Comet Pro (GL-RM10) Console Guide

## Session

On the console, navigate to **Session**. The settings page includes four sections: 

- [Video](#video)
- [Audio & Camera](#audio--camera)
- [Keyboard](#keyboard)
- [Mouse](#mouse)

### Video

You can customize video settings on the Session, such as display mode, video quality, video transmission, screen orientation, and EDID.

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session-video.png){class="glboxshadow"}

- **Transfer**: Switch the video transmission method between WebRTC, WebRTC (FEC), WebRTC (Native) and Direct. Note that the Direct transfer has no sound.

    !!! note "What's the difference between WebRTC, WebRTC (FEC), WebRTC (Native) and Direct?"

        - **WebRTC**: Balances smooth video and stable audio for real-time remote control.
        
        - **WebRTC (FEC)**: Adds forward error correction to improve connection stability under poor or unstable network conditions. When selected, it automatically repairs lost data packets by transmitting a small amount of redundant data, reducing screen flickering and lag.
  
        - **WebRTC (Native)**: Powered by the Google WebRTC Library to provide improved streaming performance and a smoother real-time remote control experience. This transfer mode was introduced in firmware v1.10.0.
        
        - **Direct**: Provides the lowest latency and lossless video quality, but does not support audio transmission.

- **Mode**: Switch between Smart and Normal mode as needed. Smart mode helps reduce bandwidth consumption, especially in weak networks.

- **Latency Mode**: You can choose between Lowest Latency and Smooth Display for the device. This feature was introduced in firmware v1.9.0.

    !!! note "What's the difference between Lowest Latency and Smooth Display?"

        - **Lowest Latency**: Minimizes input latency to deliver snappier keyboard and mouse response.

        - **Smooth Display**: Optimizes visual performance to eliminate stuttering and frame loss for steady playback.

- **Quality**: Adjust the video quality to Auto/Low/Medium/High/Ultra-high/Lossless according to your network environment and resolution requirements.

- **FEC Packets**：When the network is unstable, it automatically repairs lost data packets by sending a small amount of redundant data, reducing screen flickering and lag. You can adjust the FEC ratio to 5%/10%/15%/20%.

- **Orientation**: Adjust the console's rotation angle to 0°/90°/180°/270°.

- **EDID**: Short for Extended Display Identification Data, it automatically matches the optimal display parameters.

    The default setting applies to most scenarios and generally does not need to be modified. See [here](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} for details. If the screen does not refresh after EDID adjustment, restart the controlled device.

- **View**: This setting determines screen scaling when resizing the browser window. Available options: Adaptive, Best Picture Quality, Original Pixel. This feature was introduced in firmware v1.8.0.
  
- **Screen Privacy**: When the privacy screen is enabled, the HDMI-OUT external display will no longer show content, ensuring the privacy of remote operations.

### Audio & Camera

You can adjust the Audio and Camera settings for the controlled device.

![Audio_Camera](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_audio_camera.png){class="glboxshadow"}

- **Speaker**: Control audio output from the controlled device (e.g., system sounds, video audio).

- **Microphone**: Transmit local audio (e.g., your voice) from the controlling device to the remote end. It supports one-click mute, and a long-press shortcut to activate the microphone (i.e., Press To Speak).

    **Note**: The shortcut must be manually configured in [Settings](#usb-devices) prior to use.

- **Camera**: When the camera is enabled on the controlling device, local video frames are transmitted via passthrough to the remote host, where a virtual USB camera is emulated. Applications running on the remote host (e.g., conferencing tools and FaceTime) can consume this video feed, providing the same user experience as a physical camera directly attached to the remote host.
    
    **Note**: This feature was introduced in firmware v1.10.0 and is supported exclusively in WebRTC (FEC) mode. At present, it is accessible only via a web browser; support for the app and desktop client is not yet available.

### Keyboard

The Keyboard allows you to configure settings for keyboard use on the controlled device.

![keyboard image ](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_keyboard.png){class="glboxshadow"}

- **Bad Link Mode**: i.e. Release keys immediately. Each key press is sent as a single quick press-and-release action, preventing stuck keys or unintended repeated input during remote control.

- **Show Virtual Keyboard**: Show and use the virtual keyboard on the console.

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_show_virtual_keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: This feature swaps the Cmd and Ctrl keys to ensure keyboard compatibility across different operating systems.

### Mouse

You can adjust the mouse settings for a better experience on the controlled device.

![mouse image](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_mouse.png){class="glboxshadow"}

- **Show Local Cursor**: Display the mouse of the current device on the screen.

- **Mouse Jiggle**: The Mouse Jiggle feature simulates subtle, periodic mouse movements to prevent the controlled device from going to sleep due to prolonged inactivity, such as during remote meetings and server management.

- **Scroll Rate**: It refers to the speed at which the mouse wheel scrolls or the number of lines/units scrolled per wheel rotation, affecting how quickly content moves on the remote.

- **Scroll Direction**: It determines whether scrolling the mouse wheel up/down moves content on the remote screen in the same direction (natural scrolling) or the opposite direction (traditional scrolling). 

    Four direction modes are available: Standard, Vertical Invert, Horizontal Invert, and Both Invert.  

- **Mouse Mode**: Allows switching between Absolute Mode and Relative Mode to ensure smooth and accurate cursor control in different remote control scenarios.

    !!! note "What's the difference between Absolute Mode and Relative Mode?"

        - **Relative Mode**: The mouse position is calculated based on movement rather than fixed screen coordinates. You must click inside the remote window to control the mouse. The cursor is locked within the remote screen and cannot move out smoothly. This mode provides better compatibility with BIOS, old systems, and embedded devices.

        - **Absolute Mode**: The mouse position corresponds to exact screen coordinates. The remote cursor follows the local one smoothly and accurately, allowing seamless movement between your local screen and the remote screen. It is ideal for daily desktop control and precise operations, though a slight delay may occur due to network transmission.

        In short, use Absolute for smooth daily control; use Relative for BIOS access, some older devices that do not support absolute positioning, or to avoid accidental cursor movement.

- **Relative Sensitivity**: It is available when the Mouse Mode is Relative.

- **Primary Button**: Select the left or right button as the primary click. This feature was introduced in firmware v1.9.0.

## Toolbox

On the console, navigate to **Toolbox**. The toolbox page includes five sections: 

- [Clipboard](#clipboard)
- [OCR](#ocr)
- [Shortcut](#shortcut)
- [Wake on Lan](#wake-on-lan)
- [Terminal](#terminal)

### Clipboard

The clipboard allows you to easily paste text from the controlling device to the controlled device, without the need to transfer files.

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_clipboard.png){class="glboxshadow"}

### OCR

The OCR is Text Recognition feature, which allows you to select an area on the remote screen and extract text from it easily. This feature was introduced in firmware v1.9.0.

To use it, click the downward arrow to select your preferred recognition language, such as Chinese, English, or bilingual (Zh/En).

![recognition language](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_ocr.png){class="glboxshadow"}

Next, click **Capture** and the remote screen will dim. Draw a box around the text you want to extract, and the system will identify it automatically. You can then copy the recognized text as needed. 

![copy text](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/ocr_copy_text.png){class="glboxshadow"}

With this feature, you can easily capture text from the remote screen (i.e., the controlled device) and copy it to the local controlling device.

### Shortcut

The shortcut let you perform actions faster without using the virtual keyboard, helping you work more efficiently and save time on daily tasks. You can find some common shortcuts here.

![toolbox-shortcut1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_shorcut.png){class="glboxshadow"}

Click **Modify** to adjust the shortcuts options as needed.

![toolbox-shortcut2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_shorcut_modify.png){class="glboxshadow"}  

### Wake-on-Lan

Wake-on-LAN (WOL) is a technology that allows the controlled device to be remotely powered on or awakened from a low-power state.

Click **Add Device** and choose a device from the same LAN.

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_wake_on_lan.png){class="glboxshadow"}

![wol-add-device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/wol-add-device.png){class="glboxshadow"}

If the device you want to add is not in the list, click **Add Manually** and enter the device name and MAC address.

![wol-add-manually](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/wol-add-manually.png){class="glboxshadow"}

### Terminal

You can access Comet Pro's terminal to perform advanced settings. Click **Access**.

![toolbox-terminal1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_terminal.png){class="glboxshadow"}

You will be redirected to the GLKVM terminal.

![toolbox-terminal2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox-terminal-2.png){class="glboxshadow"}

## Accessories

GL.iNet offers optional KVM accessories to remotely control the device's power on/off. 

First, see the corresponding user guide to connect the accessory to your controlled device.

- [Fingerbot (FGB-01) User Guide](../gl-fgb-01/index.md){target="_blank"}

- [ATX Board (GL-ATXPC) User Guide](../gl-atx-board/index.md){target="_blank"}

Second, log in to the KVM console and navigate to **Accessories**. The accessory settings are only available after the accessory is installed.

### Fingerbot
    
The Fingerbot is adhered to the physical power button of the controlled device, to achieve remote control of the controlled device's power supply.
    
It works according to the settings on the console.

![accessories fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/accessories-fgb.png){class="glboxshadow"}

- **Time**: The press duration of the Fingerbot. You can set it to 0.5s/3s/8s.

- **Strength**: There are two levels of pressing strength: Lightly Press and Firmly Press.

    - **Lightly Press**: Perfect for short or soft-touch buttons.
    
    - **Firmly Press**: Ideal for deep or firm buttons.

    ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### ATX Power

The ATX Board is installed in the computer case to remotely control the device's power on/off/reboot.

It works according to the settings on the console.

![accessories atxpower](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/accessories-atx.png){class="glboxshadow"}

- **Power (Short Press)**: Used for regular power-on or system wake-up.

- **Power (Long Press)**: Performs a forced shutdown operation.

- **Restart**: Restart the device.

## Virtual Media

On the console, navigate to **Virtual Media**. Here you can perform the following operations:

- [File Sharing](#file-sharing)
- [Image Mounting](#image-mounting)
- [Replace Storage Drive](#replace-storage-drive)
- [Format Disk](#format-disk)

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/virtual-media.png){class="glboxshadow"}
    
### File Sharing

Comet Pro emulates a read-write USB drive, allowing you to share and manage files between the controlling device and the controlled device.

**To share files from the controlling device to the controlled one, follow the steps below.**

1. Drag or click the box to upload files from your controlling device or upload from URL. 

    Once uploaded, the files will be displayed as follows.

    ![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-uploaded.png){class="glboxshadow"}

2. Click **Mount To Remote** -> **File Sharing**. 

    ![file sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount1.png){class="glboxshadow"}

3. A window will pop up on the console, indicating the file sharing steps, as shown below.
    
    ![file sharing prompt](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount2-prompt.png){class="glboxshadow"}

4. Wait a second, and a drive named **"GLKVM"** will pop up on the screen automatically. You will then see the files you previously uploaded from the controlling device to Comet Pro have been shared to the controlled device. Now you can view, move or delete the files in this drive on the controlled device.

    ![file sharing glkvm drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount3.png){class="glboxshadow"}

    **Tips**: If the drive does not pop up automatically, go to **This PC** of your controlled device. 

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-thispc.png){class="glboxshadow"}
    
    Then find a drive named **GLKVM**. Now you can view, move or delete the files in this drive.

5. If you want to stop the sharing, click **Virtual Media** in the toolbar and click **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/stop-sharing1.png){class="glboxshadow"}

**To share files from the controlled device to the controlling one, follow the steps below.**

1. On the controlled device, move or copy the files you want to share into the drive **GLKVM**. 

    For example, an image named "slate7-pro_gl-be10000" has been moved from the controlled device's Desktop to the drive **GLKVM**. 

    ![move file to drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-copy.png){class="glboxshadow"}
    
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

4. Now you can use this file from the CD drive on the controlled device.

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

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/apps-center.png){class="glboxshadow"}

### Tailscale

[Tailscale](https://tailscale.com/){target="_blank"} is a WireGuard-based mesh VPN service that builds encrypted peer-to-peer private networks across devices without port forwarding or complex firewall setup.

Comet Pro integrates with Tailscale, allowing you to access it remotely through the Tailscale virtual network.

Simply bind Comet Pro and your controlling device to the same Tailscale account, then you can remotely access your Comet Pro by entering its **Tailscale virtual IP** into a web browser on the controlling device, without installing the GLKVM app. See [here](../../faq/remote_access_via_tailscale.md){target="_blank"} for details.

After binding, the console displays the linked Tailscale account and unlocks advanced features including Exit Node and Subnet Routes.

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/tailscale-enabled.png){class="glboxshadow"}

### ZeroTier

[ZeroTier](https://www.zerotier.com/){target="_blank"} creates encrypted overlay virtual networks to connect scattered devices globally as if they are inside the same local area network.

Comet Pro integrates with ZeroTier, allowing you to access it remotely through the ZeroTier virtual network.

Simply join Comet Pro and your controlling device to the same ZeroTier network, then you can remotely access your Comet Pro by entering its **ZeroTier IP** in a web browser on the controlling device, without installing the GLKVM app. See [here](../../faq/remote_access_via_zerotier.md){target="_blank"} for details.

After binding, the console displays the ZeroTier Network ID and Virtual IP.

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/zerotier-enabled.png){class="glboxshadow"}

### NetBird

[NetBird](https://netbird.io/){target="_blank"} is an open-source zero trust networking platform that lets you build secure private networks for home and business use. As a WireGuard®-based overlay network, NetBird enables secure access to your devices anytime and anywhere.

Comet Pro integrates with NetBird, allowing you to remotely access it through NetBird virtual network. See [here](../../faq/remote_access_via_netbird.md){target="_blank"} for details.

After binding, the console displays the NetBird Virtual IP.

![netbird enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/netbird-enabled.png){class="glboxshadow"}

## Help

On the console, navigate to **Help**. Here you can find more information about GL.iNet KVM and help documentation, as well as export logs for troubleshooting.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/help.png){class="glboxshadow"}

## Toolbar

On the console, navigate to the top right corner to access the following tools:

- [Collapse Toolbar](#collapse)
- [Fullscreen](#fullscreen)
- [Upgrade](#upgrade)
- [Connection Stats](#connection-stats)
- [Cloud Service](#cloud-service)
- [Logout](#logout)

### Collapse

Click the upward arrow icon in the top right corner to collapse the toolbar.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/collapse_1.png){class="glboxshadow"}

When the toolbar is collapsed, click the downward arrow icon at the top to expand it.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/collapse_2.png){class="glboxshadow"}

### Fullscreen

Click the fullscreen icon (square-shaped) in the upper right corner to switch to fullscreen mode.

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/fullscreen_1.png){class="glboxshadow"}

To exit fullscreen, press and hold the **Esc** key, or click the exit fullscreen icon (grid-shaped) in the upper right corner. 

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/fullscreen_2.png){class="glboxshadow"}

### Upgrade

Click the firmware version in the upper right corner to check for updates.

![firmware upgrade 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade_1.png){class="glboxshadow"}

In the pop-up window, you can click **Local Upgrade** to upload a firmware file.

![firmware upgrade 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade_2.png){class="glboxshadow"}

![firmware upgrade 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade_3.png){class="glboxshadow" width=350}

Download the latest firmware from the [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} before performing a local upgrade.

### Connection Stats

The Connection Stats contains a Data Dashboard, which monitors latency, jitter, and other real-time metrics.

Click the List icon to display the device status and real-time data.

![data dashboard 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/data_dashboard_1.png){class="glboxshadow"}

Click the chart icon to view statistical data, including network latency, network jitter, packet loss rate, real-time frame rate, and playback delay.

![data dashboard 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/data_dashboard_2.png){class="glboxshadow"}

### Cloud Service

GL.iNet KVM Cloud allows you to access the controlled device remotely. See [here](../../faq/remote_access_via_cloud.md){target="_blank"} for details.

Once your Comet Pro is bound to the Cloud, the console will display the cloud status as follows.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/cloud.png){class="glboxshadow"}

### Logout

To log out, click the Logout icon.
![layout](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/logout.png){class="glboxshadow"}

## Settings
On the console, click the Settings icon in the navigation bar to open the following Settings page. This feature was introduced in firmware v1.10.0. 

- [USB Devices](#usb-devices)
- [Preferences](#preferences)
- [Network](#network)
- [Security](#security)
- [Cloud](#cloud)
- [System](#system)

![Settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting.png){class="glboxshadow"}

### USB Devices

The USB Device provides centralized management for all USB emulation devices. From this page, you can toggle virtual peripherals on or off for better compatibility with the controlled host.

![USB Emulated Devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_usb_devices.png){class="glboxshadow"}

- **Microphone**
        
    When the microphone is muted, you can click Settings to customize shortcuts based on your usage habits. Press and hold the assigned shortcut key to start speaking; releasing it will mute the microphone again.

    ![mic settings 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mic_setting_1.png){class="glboxshadow" width=600}

    ![mic settings 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mic_setting_2.png){class="glboxshadow" width=434}

  - **Device Identity**

    Customize or modify the KVM's identity recognized by the controlled device. Note that EDID and device identification remain synchronized. Changing either one will automatically update the other to ensure correct device recognition.

    ![Device Identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/device_identification.png){class="glboxshadow" width=350}

### Preferences

The Preferences provides management of Layout Preferences, System Settings, and Device Screen settings.

![Preferences](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_preference.png){class="glboxshadow"}

- **Layout Preferences**:You can manage show toolbar in fullscreen and show status bar in window mode as needed.
  
- **System Settings**: To customize System Settings, select the browser Tab Title, Language (Chinese, English, or Japanese), Color Mode (Light or Dark), and Timezone based on your region.

- **Device Screen**: You can manage and preview the device screen. Available settings include the Lock Screen mode (World Clock, Clock Only, or Wallpaper Only), Time Format, Date Format, and Wallpaper.

### Network

You can check and modify Comet Pro's network details, such as Hostname and IP address.

![network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network.png){class="glboxshadow"}

- **Hostname**: You can modify the device hostname directly on the console. This feature was introduced in firmware v1.7.0.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_hostname.png){class="glboxshadow" width=600}

- **Ethernet Settings**: When Comet Pro connects to an upstream network device via an Ethernet cable, its Ethernet details will be displayed here. 

    If the protocol is DHCP, the page displays as follows.

    ![ethernet dhcp](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_dhcp.png){class="glboxshadow" width=600}

    If you want to set a static IP address, switch the protocol to **Static** and enter the required network parameters (e.g., IP address, netmask, gateway) accordingly.

    ![ethernet static](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_static.png){class="glboxshadow" width=600}

- **Wireless**: When Comet Pro connects to a Wi-Fi network, its IP address, gateway, and MAC address will be displayed here.

    ![wifi config](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_wifi.png){class="glboxshadow" width=600}

    If you want to connect it to a different Wi‑Fi network, click **Switch Wi-Fi** and select a Wi-Fi from the available network list.

    ![join wifi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_switch_network.png){class="glboxshadow" width=500}

### Security

The security allows you to change admin password, enable two-factor authentication, and customize TLS certificate. 

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_security.png){class="glboxshadow"}

- Change Admin Password

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/change-password.png){class="glboxshadow" width="434"}

- 2FA: Enable two-factor authentication to protect your account.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/2fa.png){class="glboxshadow"}

- TLS Certificate

    The system will use the pre-installed default certificate for browser access. If you want to customize the TLS certificate for web browser access, click **Custom** under TLS Certificate, then upload your **certificate file & private key file**.

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_security_custom.png){class="glboxshadow"} 

### Cloud

The Cloud allows you to remotely access and manage your device through cloud services.

You can bind your device to the Cloud via URL. In **More Settings**, you'll find other options like Bind With Code and App Download. Disable is also available if needed.

![Cloud 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_cloud_1.png){class="glboxshadow"} 

Once bound successfully, you can view the bound cloud account information. Click **Access Cloud** to manage Devices or click **More Settings** to disable or unbind as needed. 

![Cloud 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_cloud_2.png){class="glboxshadow"} 

Alternatively, you can also perform the above management operations via Cloud Service on the top toolbar.

### System

In the System settings, you can configure the following:

![system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_system.png){class="glboxshadow"} 

- **System**: Click **Reboot** to restart the device, or click **Reset** to clear the current device configuration and set up the device again.

- **Upgrade**: You can enable Beta Center to receive beta firmware updates, or use Local Upgrade to manually install from a local file.
  
    ![local Upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setthing_system_local_update.png){class="glboxshadow" width=400} 

- **Help & Support**: Export Log Files allows you to save device runtime logs for troubleshooting and after-sales support. Help Document provides access to user guides, FAQs, and troubleshooting documentation.