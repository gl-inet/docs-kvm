# Connection failed when remote access via GLKVM app

When accessing remotely through the GLKVM app, sometimes you may encounter a problem where the KVM device displays Online in the GLKVM app, but when clicked, it shows "Connection Failed".

![device online](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/device_online.jpg){class="glboxshadow"}

![connecting](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connecting.jpg){class="glboxshadow"}

![connection failed](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connection_failed.jpg){class="glboxshadow"}

Troubleshooting Guide:

1. Ensure stable network connectivity.

    Make sure the KVM is connected to the Internet. A solid-white LED indicates normal network connectivity.

2. Check Network Firewall Rules.

    Disable the local firewall temporarily, or add GL.iNet-related domains (e.g., glkvm.com, glkvm.xyz, glkvm.top) to the firewall allowlist. Retry the connection after applying changes.

3. Disable VPN/Proxy on the Controlling Device.

    Ensure the device running the GLKVM app does not have VPN or proxy services enabled, as these may interfere with connectivity.

4. Restart the KVM if Possible.

    Perform a hardware restart on the KVM device if possible to clear transient network or software issues.

Additional Technical Notes:

1. Ensure DNS resolution for the domains is functional.

2. Confirm that outbound traffic to standard KVM/remote-access ports is not blocked.

3. For enterprise networks, consult IT administrators regarding potential traffic filtering policies.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
