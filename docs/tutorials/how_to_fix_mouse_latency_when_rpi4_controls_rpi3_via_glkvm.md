# How to fix mouse latency when RPi4 controls RPi3 via GLKVM

When using a Raspberry Pi4 to control a Raspberry Pi3 via GL.iNet KVM, mouse latency issues may occur, typically lasting for a few seconds.

To fix it, append `usbhid.mousepoll=0` to the boot line in `/boot/cmdline.txt` (or in `/boot/firmware/cmdline.txt`) on the managed server (i.e. RPI3 in this case) and reboot it.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.