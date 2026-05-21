# How to access serial console via USB TTL?

Follow the steps below to use the USB TTL adapter for serial debugging:

1. Plug the USB TTL adapter into the USB port of your KVM device.
2. Run the following command to open the serial port connection:

```bash
minicom -D /dev/ttyUSB0 -b 115200
```

This command establishes serial connection to `/dev/ttyUSB0` at a baud rate of `115200`.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.