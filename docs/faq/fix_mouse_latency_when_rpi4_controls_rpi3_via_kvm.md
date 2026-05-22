# How to fix mouse latency when RPi4 controls RPi3 via KVM?

Mouse lag may appear when operating RPi3 remotely from RPi4 over KVM, usually lasting several seconds.

To resolve the issue, add `usbhid.mousepoll=0` to the boot parameter line in `/boot/cmdline.txt` or `/boot/firmware/cmdline.txt` on the controlled RPi3, then restart the device.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.