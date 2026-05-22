# What should I do if the remote screen does not show the BIOS interface?

When accessing the controlled device through KVM, if the remote screen does not show the BIOS interface (e.g., No HDMI Signal), the reason is that the BIOS interface typically outputs only to the primary monitor. Here are some suggestions.

## Laptop

If the controlled device is a laptop, its built-in screen serves as the primary display, so the external KVM cannot render the BIOS interface.

## Desktop

For desktop devices, connect the primary monitor to the DisplayPort port if available. This is because most graphics cards and motherboards prioritize DP output over HDMI during startup.

Follow the methods below to make the BIOS interface visible via KVM.
    
- Switch between different monitor ports. Connect GL.iNet KVM to the port set as the primary display output on your computer.
    
- Use a 1-to-2 HDMI splitter (not included) to duplicate the primary display signal to the KVM device.

> **Note**: This problem may also occur when the controlled device boots into **Windows PE**, as BIOS signals only transmit to the primary monitor and cannot be shown on the remote KVM screen.

> It is advised to test with an extra monitor. If the secondary display still cannot receive signals, the KVM will fail to capture the BIOS screen. You may manually integrate or install display drivers into the WinPE system to resolve this.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.