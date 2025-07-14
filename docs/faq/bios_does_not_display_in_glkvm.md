# What should I do if the BIOS interface does not display in GLKVM?

You may encounter an issue where the GL.iNet KVM device fails to display the BIOS interface of the controlled device (e.g., No HDMI Signal). This is because the BIOS interface typically outputs only to the primary monitor.

Here are some suggestions.

## Laptop

If the controlled device is a laptop, the laptop's screen is the primary monitor of the controlled end. Therefore, external KVM devices (e.g., Comet GL-RM1) will not display the BIOS interface.

## Desktop

For desktop computers, we recommend connecting the primary monitor to the DisplayPort (DP) if any. This is because graphics cards or motherboards often prioritize DP output over HDMI during startup.

To enable the GLKVM to display the BIOS interface, you may try the following methods:
    
- Try different connection ports for your monitors. Connect the GL.iNet KVM to the port that your computer recognizes as the primary output.
    
- Purchase a 1-to-2 HDMI splitter and use it to mirror the primary monitor to the KVM device.

**Note**: When the controlled device runs on a Windows PE system, this issue (i.e. the BIOS outputs only to the primary monitor and thus not appear in the GL.iNet KVM device) may also occur. 

It is recommended to use another monitor to test. If the display still fails to output to the second monitor, the KVM device will not be able to capture the BIOS interface. In this case, you can integrate or install the display driver into the WinPE system yourself.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.