# What should I do if the remote screen goes blank or shows no HDMI signal

When accessing the controlled device through KVM, if the remote screen goes blank or shows no HDMI signal, follow the steps below to troubleshoot.

![white screen](https://static.gl-inet.com/docs/kvm/faq/blank_screen/white_screen.png){class="glboxshadow"}
<small>(White screen)</small>

![black screen](https://static.gl-inet.com/docs/kvm/faq/blank_screen/black_screen.png){class="glboxshadow"}
<small>(Black screen)</small>

First, check whether this is related to video transmission. Log in to your KVM, go to **Settings** -> **Video** -> **Transfer** and set the transfer mode to **Direct**. 

![change transfer](https://static.gl-inet.com/docs/kvm/faq/blank_screen/change_transfer.png){class="glboxshadow" width="360"}

If the problem persists, check the possible causes listed below one by one.

## Check Hardware Connection

1. **Faulty HDMI Cable**

    Aging HDMI cables, oxidized connectors, or internal breaks can interrupt signal transmission. Replace it with a high-quality HDMI cable.

    You can also check the HDMI signal status on the KVM console. Find the monitor icon in the bottom right corner and check if it shows "No HDMI signal".

    ![no HDMI signal](https://static.gl-inet.com/docs/kvm/faq/blank_screen/no_hdmi_signal.png){class="glboxshadow"}

2. **Incorrect Connection**

    If your controlled device is a desktop PC, ensure the KVM's **HDMI IN** port is connected to the HDMI OUT port of the desktop's graphics card or motherboard. Make sure the plug is fully inserted and secure. For devices with multiple HDMI outputs (e.g., dedicated GPU + motherboard output), try switching to a different port.

    If your controlled device is a laptop, ensure the KVM's **HDMI IN** port is connected to the laptop's HDMI OUT port.

    Tip: Some KVM models (such as Comet Pro and Comet 5G) have two HDMI ports. Make sure the HDMI cable from the controlled device is plugged into the KVM's HDMI IN port. If connected to HDMI OUT, no HDMI signal will be detected on the KVM console.

3. **Improper Use of Adapters**

    If an HDMI adapter is required, use a **VGA-to-HDMI** adapter to connect the controlled device to the GL.iNet KVM's HDMI IN port. 
    
    Using an HDMI-to-VGA adapter for this connection will fail to transmit video signals properly, resulting in a blank screen.

    ![adapter comparison](https://static.gl-inet.com/docs/kvm/faq/blank_screen/adapter_comparison.png){class="glboxshadow"}

## Check Browser Settings

If you access the controlled device via a browser and encounter a blank screen issue, try the following methods:

1. **Test with multiple browsers.** Try Chrome, Firefox, Edge, etc. to determine if the issue is browser-specific.

2. **Disable WebRTC Leak Protection/Control Extensions.** If you have installed any extensions/plug-ins to your web browser that may affect WebRTC connections, please disable them and test again. You may also go to the browser's Settings -> Privacy & Security to ensure the web browser allows WebRTC connections.  

    ![webrtc](https://static.gl-inet.com/docs/kvm/faq/blank_screen/webrtc.png){class="glboxshadow"}

## Check Controlled Device Status and Settings

1. **Device Not Powered On or in Sleep Mode**

    Ensure the controlled device is fully powered on and not in sleep/hibernation mode due to power management settings (wake it via local buttons as needed).

2. **Abnormal Graphics Card Drivers on the Controlled Device**

    Uninstalled or corrupted graphics card drivers can cause no video output. Update or reinstall the graphics card drivers on the controlled device (when logged in locally).

3. **Incorrect Connection of Dedicated and Integrated Graphics**

    If the controlled device has both a dedicated and integrated graphics card, ensure the HDMI cable is connected to the correct graphics port (e.g., connect the HDMI cable to the dedicated graphics port if it is installed).

4. **Abnormal Display Settings on the Controlled Device (Low Probability)**

    When the GL.iNet KVM connects to the controlled device, it automatically adjusts display output by reading the monitor's EDID for optimal performance. In most cases, the default EDID configuration is suitable for most scenarios and no need to modify.

    If the controlled device is compatible with standard monitors, blank screens or display issues are unlikely when accessing it via GLKVM. However, a few specific compatibility issues (e.g., Linux system + ASUS monitor) may cause blank screens when using GLKVM.

    Please check if your controlled device is compatible with standard monitors, and if it has compatibility issues with a specific monitor.

5. **Resolution Negotiation Issue**
   
    When GLKVM is connected to certain operating systems (e.g., Proxmox VE Hypervisor), it may fail to negotiate the available display resolution correctly, resulting in display issues. This can be resolved by manually adjusting the resolution on the controlled device.

    Here is a guide on how to modify the system resolution for your reference.

    Proxmox VE Hypervisor:
    1. Open the PVE terminal and enter the command below to edit file /etc/default/grub.

       ```nano /etc/default/grub```

    2. Add the following line.

       ```GRUB_CMDLINE_LINUX_DEFAULT="quiet gfxpayload=text nomodeset"```

    3. Uncomment the line `GRUB_GFXMODE` by removing the `#` and set the desired resolution, such as `1024x768`. 

       ```GRUB_GFXMODE=1024x768```

    4. Press `Ctrl + O` and hit Enter to save the configuration.

    5. Press `Ctrl + X` to exit the nano editor.

    6. Enter the command below to apply the configuration.

       ```update-grub```
       

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.