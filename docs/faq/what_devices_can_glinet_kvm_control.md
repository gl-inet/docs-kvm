# What devices can GL.iNet KVM control? Do I need to install any software to use KVM?

GL.iNet KVM can be used to control any device that uses HDMI output and USB input, such as laptops, desktops, Raspberry Pi, mini hosts, etc.

No software is required to be installed on the controlled device. 

As to the controlling device, whether software needs to be installed on it depends on the way you want to access the controlled device.

- Local Access

    If you want to access the controlled device in the local area network (LAN), you can directly launch a browser on the controlling PC, enter `glkvm.local` in the address bar to access the glkvm local management page.
    
- Remote Access

    If your controlling device is Windows or macOS, you can install the [GLKVM application](https://www.gl-inet.com/app-rm/){target="_blank"} on it to access GL.iNet KVM and the controlled device. 

    Alternatively, if you cannot or don't want to install GLKVM application, you may use Tailscale to achieve remote access, which is integrated in Comet (GL-RM1). In this way, you can directly access Comet by typing its Tailscale virtual IP into a browser, without installing GLKVM app.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.