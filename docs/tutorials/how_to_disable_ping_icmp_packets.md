# How to disable outgoing PING/ICMP packets from KVM?

The KVM device periodically sends PING (ICMP) packets for network connectivity detection. This document explains how to disable this behavior and the associated side effects.

## For Ethernet-Only Devices

For devices with only an Ethernet connection, such as Comet (GL-RM1) and Comet PoE (GL-RM1PE), the system sends PING packets to the default gateway to check internet connectivity. The result is indicated by the LED status.

To temporarily disable this behavior, run the following command:

```bash
/etc/init.d/S23led stop
```

> **Note:** Disabling this service will also make the **Reset button** unavailable.

## For Devices with Both Ethernet and Wi-Fi

For devices equipped with both Ethernet and Wi-Fi, the system sends PING packets to public DNS servers to verify internet access for each network interface. This mechanism is used for dynamic multi-WAN failover, ensuring that the device can switch to Wi-Fi if the Ethernet connection loses internet access.

To temporarily disable this behavior, run the following command:

```bash
/etc/init.d/S98multi-wan stop
```

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
