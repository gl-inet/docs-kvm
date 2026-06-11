# Comet Q (GL-RMQ1) Console Guide

## Settings

On the console, navigate to **Settings**. The settings page includes four sections: 

- [Video](#video)
- [Audio&Keyboard&Mouse](#audiokeyboardmouse)
- [System](#system)
- [Network](#network)

### Quick Search

You can quickly find the settings you want by entering keywords at the top of the Settings page.

![quick search](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/quick-search.png){class="glboxshadow"}

### Video

You can customize video settings on the console, such as EDID, video quality, video transmission and screen orientation.

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-video.png){class="glboxshadow"}

- **Type**: Select your controlled device type. 

    The system automatically applies the recommended mouse mode and EDID settings to deliver the best display aspect ratio and control accuracy. Switch this option if the device is not recognized correctly or you need to use a custom type.

- **EDID**: Short for Extended Display Identification Data, it automatically matches the optimal display parameters.

    The default setting applies to most scenarios and generally does not need to be modified. See [here](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} for details. If the screen does not refresh after EDID adjustment, restart the controlled device.

- **Mode**: Switch between Smart and Normal mode as needed. Smart mode helps reduce bandwidth consumption, especially in weak networks.

- **Quality**: Adjust the video quality to Low/Medium/High/Ultra-high/Lossless according to your network environment and resolution requirements.

- **Transfer**: Switch the video transmission method between WebRTC, WebRTC (FEC), and Direct. Note that the Direct transfer has no sound.

    !!! note "What's the difference between WebRTC, WebRTC (FEC) and Direct?"

        - **WebRTC**: Balances smooth video and stable audio for real-time remote control.
        
        - **WebRTC (FEC)**: Adds forward error correction to improve connection stability under poor or unstable network conditions. When selected, it automatically repairs lost data packets by transmitting a small amount of redundant data, reducing screen flickering and lag.
        
        - **Direct**: Provides the lowest latency and lossless video quality, but does not support audio transmission.

- **Orientation**: Adjust the console's rotation angle to 0°/90°/180°/270°.

- **View**: This setting determines screen scaling when resizing the browser window. Available options: Adaptive, Best Picture Quality, Original Pixel.

### Audio&Keyboard&Mouse

You can adjust relevant settings of the audio, keyboard, and mouse.

![audio keyboard mouse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/audio-keyboard-mouse.png){class="glboxshadow"}

- **Speaker**: Control audio output from the controlled device (e.g., system sounds, video audio)

- **Microphone**: Transmit local audio (e.g., your voice) from the controlling device to the remote end. It supports one-click mute, and a long-press shortcut to activate the microphone (i.e., Press To Speak).

    ![mic settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/mic-settings.png){class="glboxshadow"}

    ![press to speak](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/press-to-speak.png){class="glboxshadow"}

- **Keyboard**: Turn on or off the keyboard of the controlled device.

- **Bad Link Mode**: i.e. Release keys immediately. Each key press is sent as a single quick press-and-release action, preventing stuck keys or unintended repeated input during remote control.

- **Show Virtual Keyboard**: Show and use the virtual keyboard on the console.

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-keyboard.png){class="glboxshadow"}

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

![settings-system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-system.png){class="glboxshadow"}

- **Device Identity**: Customize or modify the KVM's identity recognized by the controlled device. Note that EDID and device identification remain synchronized. Changing either one will automatically update the other to ensure correct device recognition.

    ![device identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/device-identity.png){class="glboxshadow"}

- **Language**: Set the console's language to Chinese or English.

- **Color Mode**: Customize the theme color to Light or Dark mode.

- **Time Zone**: Customize the time zone of the KVM console. 

- **Reset KVM**: Factory reset your KVM with just one click.

### Network

You can check and modify Comet Q's network details, such as Hostname and IP address.

![settings-network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-network.png){class="glboxshadow"}

- **Hostname**: You can modify the device hostname directly on the console.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/hostname.png){class="glboxshadow"}

- **Wi-Fi**: Comet Q's Wi-Fi IP address will be displayed here when it connects to a Wi-Fi network. Click the Wi-Fi SSID or the right arrow to view the Wi-Fi details, including the SSID, assigned IP address, gateway, and the MAC address your Comet Q uses to connect to.

    ![wifi config](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/wifi-config.png){class="glboxshadow"}

    If you want to connect it to a different Wi‑Fi network, click **Switch Wi-Fi** and select a Wi-Fi from the available network list.

## Toolbox

On the console, navigate to **Toolbox**. The toolbox page includes three sections: 

- [Clipboard](#clipboard)
- [Shortcut](#shortcut)
- [Terminal](#terminal)

### Clipboard

The clipboard allows you to easily paste text from the controlling device to the controlled device, without the need to transfer files.

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-clipboard.png){class="glboxshadow"}

### Shortcut

The shortcut let you perform actions faster without using the virtual keyboard, helping you work more efficiently and save time on daily tasks. You can find some common shortcuts here.

![toolbox-shortcut1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut1.png){class="glboxshadow"}

Click **Modify** to adjust the shortcuts options as needed.

![toolbox-shortcut2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut2.png){class="glboxshadow"}  

### Terminal

You can access Comet Q's terminal to perform advanced settings. Click **Access**.

![toolbox-terminal1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal1.png){class="glboxshadow"}

You will be redirected to the GLKVM terminal.

![toolbox-terminal2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal2.png){class="glboxshadow"}

## Virtual Media

On the console, navigate to **Virtual Media**. Comet Q can emulate a read-write USB drive, allowing you to share and manage files between the controlling device and the controlled device.

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-media.png){class="glboxshadow"}

### File Sharing

**To share files from the controlling device to the controlled one, follow the steps below.**

1. Drag or click the box to upload files from your controlling device or upload from URL. 

    Once uploaded, the files will be displayed as follows.

    ![file-sharing1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing1.png){class="glboxshadow"}

2. Click **Mount To Remote** -> **File Sharing**. 

    ![file-sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing2.png){class="glboxshadow"}

3. A window will pop up on the console, indicating the file sharing steps, as shown below.
    
    ![file-sharing3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing3.png){class="glboxshadow"}

4. Wait a second, and a drive named **"GLKVM"** may pop up on the screen automatically. You will then see the files you previously uploaded from the controlling device to Comet Q have been shared to the controlled device. Now you can view, move or delete the files in this drive on the controlled device.

    ![file-sharing4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing4.png){class="glboxshadow"}

    **Tips**: If the drive does not pop up automatically, go to **This PC** of your controlled device. 

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/thispc.png){class="glboxshadow"}
    
    Then find a drive named **GLKVM**. Now you can view, move or delete the files in this drive.

5. If you want to stop the sharing, click **Virtual Media** in the toolbar and click **Stop Sharing**.

    ![stop sharing1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing1.png){class="glboxshadow"}

**To share files from the controlled device to the controlling one, follow the steps below.**

1. On the controlled device, move or copy the files you want to share into the drive **GLKVM**. 

    For example, a PDF file named "gl-rm10_datasheet" has been moved from the controlled device's Desktop to the drive **GLKVM**. 

    ![file-sharing5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing5.png){class="glboxshadow"}
    
2. Turn to the Comet Q's console, click **Virtual Media** in the toolbar and click **Stop Sharing**.

    ![stop sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing2.png){class="glboxshadow"}
    
3. This file will then be displayed under the **Virtual Media**, as shown below. Now you can download this file from Comet Q to your controlling device.

    ![file sharing6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing6.png){class="glboxshadow"}

### Format Disk

You can format the disk or disable the virtual media with one click.

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/format-disable.png){class="glboxshadow"}

- **Format**: Erase all data on the disk and reinitialize its file system structure.

- **Disable**: Disable the virtual media will immediately reboot the KVM device. 

## Apps Center

On the console, navigate to **Apps Center**. The integrated applications can be found here.

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-center.png){class="glboxshadow"}

### Tailscale

[Tailscale](https://tailscale.com/){target="_blank"} is a WireGuard-based mesh VPN service that builds encrypted peer-to-peer private networks across devices without port forwarding or complex firewall setup.

Comet Q integrates with Tailscale, allowing you to access it remotely through the Tailscale virtual network.

Simply bind Comet Q and your controlling device to the same Tailscale account, then you can remotely access your Comet Q by entering its **Tailscale virtual IP** into a web browser on the controlling device, without installing the GLKVM app. See [here](../../faq/remote_access_via_tailscale.md){target="_blank"} for details.

After binding, the console displays the linked Tailscale account and unlocks advanced features including Exit Node and Subnet Routes.

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier

[ZeroTier](https://www.zerotier.com/){target="_blank"} creates encrypted overlay virtual networks to connect scattered devices globally as if they are inside the same local area network.

Comet Q integrates with ZeroTier, allowing you to access it remotely through the ZeroTier virtual network.

Simply join Comet Q and your controlling device to the same ZeroTier network, then you can remotely access your Comet Q by entering its **ZeroTier IP** in a web browser on the controlling device, without installing the GLKVM app. See [here](../../faq/remote_access_via_zerotier.md){target="_blank"} for details.

After binding, the console displays the ZeroTier Network ID and Virtual IP.

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-zerotier-enabled.png){class="glboxshadow"}

## Help

On the console, navigate to **Help**. Here you can find more information about GL.iNet KVM and help documentation, as well as export logs for troubleshooting.

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/help.png){class="glboxshadow"}

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

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse1.png){class="glboxshadow"}

When the toolbar is collapsed, click the downward arrow icon at the top to expand it.

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse2.png){class="glboxshadow"}

### Fullscreen

Click the fullscreen icon (square-shaped) in the upper right corner to switch to fullscreen mode.

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen1.png){class="glboxshadow"}

To exit fullscreen, press and hold the **Esc** key, or click the exit fullscreen icon (grid-shaped) in the upper right corner. 

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen2.png){class="glboxshadow"}

### Upgrade

Click the firmware version in the upper right corner to check for updates.

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade1.png){class="glboxshadow"}

In the pop-up window, you can perform an online upgrade if newer firmware is available. Alternatively, download the latest firmware from the [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"} and perform a local upgrade as needed.

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade2.png){class="glboxshadow"}

### Cloud Service

GL.iNet KVM Cloud allows you to access the controlled device remotely. See [here](../../faq/remote_access_via_cloud.md){target="_blank"} for details.

Once your Comet Q is bound to the Cloud, the console will display the cloud status as follows.

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/cloud.png){class="glboxshadow"}

### Security

The security allows you to change admin password, enable two-factor authentication, and customize TLS certificate. 

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/security.png){class="glboxshadow"}

- Change Admin Password

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/admin-password.png){class="glboxshadow" width="434"}

- 2FA: Enable two-factor authentication to protect your account.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/2fa.png){class="glboxshadow"}

- TLS Certificate

    The system will use the pre-installed default certificate for browser access. If you want to customize the TLS certificate for web browser access, click **TLS Certificate** in the upper right corner of the console, select **Custom Certificate**, then upload your **certificate file & private key file**.

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/tls-certificate.png){class="glboxshadow"}
