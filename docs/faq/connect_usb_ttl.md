---
hide:
  - navigation
  - toc
---

# How to connect USB TTL

To connect a USB TTL device:

1. Insert the USB TTL adapter into one of the USB ports on the KVM device.
2. Use the following command to connect to the USB serial port:

```bash
minicom -D /dev/ttyUSB0 -b 115200
```

This command connects to the USB serial device at `/dev/ttyUSB0` with a baud rate of `115200`.
