# How to disable outgoing PING/ICMP packets from KVM

The KVM device periodically sends PING (ICMP) packets for network connectivity detection. This document explains how to disable this behavior and the associated side effects.

## Ethernet-Only Devices (RM1/RM1PE)

For devices with only an Ethernet connection, PING packets are sent to the default gateway to determine whether the device is connected to the internet. The result is reflected in the LED indicator.

To temporarily disable this behavior, run the following command:

```bash
/etc/init.d/S23led stop
```

> **Note:** Disabling this service will also cause the **Reset button** to become unavailable.

## Devices with Both Ethernet and WiFi

For devices equipped with both Ethernet and WiFi, PING packets are sent to public DNS servers to check whether each network interface has internet access. This is used for dynamic multi-WAN failover, ensuring that the device can switch to WiFi if the Ethernet connection loses internet connectivity.

To temporarily disable this behavior, run the following command:

```bash
/etc/init.d/S98multi-wan stop
```

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
