# Display blank screen when accessing the controlled device using GLKVM

When accessing the controlled device via GLKVM, if you encounter blank (white or black) screen issue as shown below, please check the following possible causes one by one.

![blank screen](https://static.gl-inet.com/docs/kvm/faq/blank_screen/blank_screen.jpg){class="glboxshadow"}

Please navigate to Settings -> Video -> Transfer and change the Transfer to **Derict H.264**. 

![change mode](https://static.gl-inet.cn/KVM/rm10/1change_mode.png){class="glboxshadow"}

If the problem persists, please check the following settings.

## Check Hardware Connection

1. **Faulty HDMI Cable**

    Aging HDMI cables, oxidized connectors, or internal breaks can interrupt signal transmission. Replace with a high-quality HDMI cable.

    You can also check the HDMI signal status in the GLKVM app. Navigate to the monitor icon in the bottom right corner and check if it says "No HDMI signal".

    ![no HDMI signal](https://static.gl-inet.com/docs/kvm/faq/blank_screen/no_hdmi_signal.png){class="glboxshadow"}

2. **Incorrect Connection**

    Take GL-RM1 as an example: The HDMI IN port of GL-RM1 must be connected to the HDMI OUT port of the controlled device's graphics card/motherboard. Ensure the plug is fully inserted and secure.

    If the controlled device has multiple HDMI ports (e.g., graphics card + motherboard), test by switching to different ports.

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

    Ensure the controlled device is fully powered on and not in sleep/hibernation mode due to power management settings (wake it via local buttons if needed).

2. **Abnormal Graphics Card Drivers on the Controlled Device**

    Uninstalled or corrupted graphics card drivers can cause no video output. Update or reinstall the graphics card drivers on the controlled device (when logged in locally).

3. **Incorrect Connection of Dedicated and Integrated Graphics**

    If the controlled device has both a dedicated and integrated graphics card, ensure the HDMI cable is connected to the correct graphics port (e.g., connect the HDMI cable to the dedicated graphics port if it is installed).

4. **Abnormal Display Settings on the Controlled Device (Low Probability)**

    When the GL.iNet KVM connects to the controlled device, it automatically adjusts display output by reading the monitor's EDID for optimal performance. In most cases, the default EDID configuration is suitable for most scenarios and no need to modify.

    If the controlled device is compatible with standard monitors, blank screens or display issues are unlikely when accessing it via GLKVM. However, a few specific compatibility issues (e.g., Linux system + ASUS monitor) may cause blank screens when using GLKVM.

    Please check if your controlled device is compatible with standard monitors, and if it has compatibility issues with a specific monitor.
    
---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.