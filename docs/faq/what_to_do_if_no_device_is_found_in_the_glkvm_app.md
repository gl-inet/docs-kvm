# What to do if no device is found in the GLKVM app?

You may encounter an issue that no device is found in the GLKVM app when adding device for the first time.

![no device found](https://static.gl-inet.com/docs/kvm/faq/what_to_do_if_no_device_found_in_the_glkvm_app/no_device_found.png){class="glboxshadow gl-80-desktop"}

Here are some troubleshooting tips:

1. Make sure the KVM is connected to the Internet. A solid-white LED indicates normal network connectivity.

    For LED explanation of Comet (GL-RM1), please click [here](../user_guide/gl-rm1/index.md/#led){target="_blank"}.

2. Make sure the KVM and the controlling device are connected to the same network when adding device.

3. Check whether the controlled device has VPN enabled. Disable the VPN and try finding device again.

4. Check whether the local firewall of the controlled device blocks the GLKVM app's access to the Internet, or intercepts GL.iNet-related domains' traffic (such as goodcloud.xyz, gl-inet.net, astrowarp.net, etc.). 

    Disable the local firewall or add GL.iNet-related domains into the firewall allowlist, then try again.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.