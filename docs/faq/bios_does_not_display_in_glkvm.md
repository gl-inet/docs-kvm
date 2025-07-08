# What should I do if the BIOS interface does not display in GLKVM?

You may encounter an issue where the GLKVM app fails to display the BIOS interface of the controlled device (e.g., a completely black screen). This is because the BIOS interface typically outputs only to the primary monitor.

Here are some suggestions.

## Laptop

If the controlled device is a laptop, the laptop's screen is the primary monitor of the controlled end. Therefore, external KVM devices (e.g., Comet GL-RM1) will not display the BIOS interface.

## Desktop

If the controlled device is a desktop computer, set the monitor connected to the DP port as the primary display, as DP-port monitors generally take priority over HDMI-port monitors.

To enable the GLKVM to display the BIOS interface, you may try the following methods:
    
- Test and adjust the connection port of the GL.iNet KVM device.
    
- Purchase a 1-to-2 HDMI splitter and use it to mirror the primary monitor to the KVM device.

**Note**: When the controlled device runs on a Windows PE system, this issue (i.e. the BIOS outputs only to the primary monitor and thus not appear in the GLKVM app) may also occur. 

It is recommended to use another monitor to test. If the display still fails to output to the second monitor, the KVM device will not be able to capture the BIOS interface. In this case, you can integrate or install the display driver into the WinPE system yourself.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.