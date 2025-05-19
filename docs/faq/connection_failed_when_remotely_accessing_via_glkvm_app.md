# Connection failed when remotely accessing via GLKVM app

When accessing remotely through the GLKVM app, sometimes you may encounter a problem where the KVM device displays Online in the GLKVM app, but when clicked, it shows "Connection Failed".

![device online](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/device_online.jpg){class="glboxshadow"}

![connecting](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connecting.jpg){class="glboxshadow"}

![connection failed](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connection_failed.jpg){class="glboxshadow"}

Here are some troubleshooting tips:

1. Make sure the KVM is connected to the Internet. A solid-white LED indicates normal network connectivity.

    For LED explanation of Comet (GL-RM1), please click [here](../user_guide/gl-rm1/index.md/#led){target="_blank"}.

2. Check if the controlling device (where the GLKVM app is installed) has VPN or proxy enabled. Disable the VPN and proxy, then try finding device again.

3. Check whether the local firewall of the controlling device blocks the GLKVM app's access to the Internet, or intercepts GL.iNet-related domains' traffic (such as goodcloud.xyz, gl-inet.net, astrowarp.net, etc.). 

    Disable the local firewall or add GL.iNet-related domains into the firewall allowlist, then try again.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
