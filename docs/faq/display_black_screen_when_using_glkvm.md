# Display black screen when accessing the controlled device using GLKVM

If it displays black screen when accessing the controlled device via GLKVM, please check the following possible causes one by one:

## Check Hardware Connection

1. **Faulty HDMI Cable**

    Aging HDMI cables, oxidized connectors, or internal breaks can interrupt signal transmission. Replace with a high-quality HDMI cable.

2. **Incorrect Connection**

    Take GL-RM1 as an example: The HDMI IN port of GL-RM1 must be connected to the HDMI OUT port of the controlled device's graphics card/motherboard. Ensure the plug is fully inserted and secure.

    If the controlled device has multiple HDMI ports (e.g., graphics card + motherboard), test by switching to different ports.

3. **Improper Use of Adapters**

    If an HDMI adapter is required, use a **VGA-to-HDMI** adapter to connect the controlled device to the GL.iNet KVM's HDMI IN port. 
    
    Using an HDMI-to-VGA adapter for this connection will fail to transmit video signals properly, resulting in a black screen or no display.

    ![adapter comparison](https://static.gl-inet.com/docs/kvm/faq/blank_screen/adapter_comparison.png){class="glboxshadow"}

## Check Controlled Device Status and Settings

1. **Device Not Powered On or in Sleep Mode**

    Ensure the controlled device is fully powered on and not in sleep/hibernation mode due to power management settings (wake it via local buttons if needed).

2. **Abnormal Graphics Card Drivers on the Controlled Device**

    Uninstalled or corrupted graphics card drivers can cause no video output. Update or reinstall the graphics card drivers on the controlled device (when logged in locally).

3. **Incorrect Connection of Dedicated and Integrated Graphics**

    If the controlled device has both a dedicated and integrated graphics card, ensure the HDMI cable is connected to the correct graphics port (e.g., connect the HDMI cable to the dedicated graphics port if it is installed).

4. **Abnormal Display Settings on the Controlled Device (Low Probability)**

    When the GL.iNet KVM connects to the controlled device, it automatically adjusts display output by reading the monitor's EDID for optimal performance. In most cases, the default EDID configuration is suitable for most scenarios and no need to modify.

    If the controlled device is compatible with a standard monitor, black screens or display issues are unlikely when accessing via GLKVM. However, compatibility issues (e.g., Linux system + ASUS monitor) may cause black screens or no display when using GLKVM.

    If you customize the KVM's EDID, ensure the following conditions are met:

    - The resolution shall not exceed 2560×1440@60Hz. For example, a resolution of 2560×1600@60Hz is not supported.

    - The maximum supported refresh rate is 60Hz. For resolutions higher than 1920×1080, a frame rate of 60FPS or lower is recommended.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.