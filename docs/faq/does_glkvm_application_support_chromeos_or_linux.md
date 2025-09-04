# Does GLKVM app support ChromeOS/Linux?

The GLKVM app is designed for the controlling device (i.e. the Host). Currently the GLKVM app does not support installation on Chrome or Linux OS, so if your controlling device is running Chrome/Linux OS, the GLKVM app cannot be installed, thus remote access to controlled device via GLKVM app is not supported. 

However, you can use **Cloud Service** or **Tailscale** to achieve remote access.

- Cloud Service

    This method is ideal for those who cannot or do not want to install the GLKVM app.

    Bind your KVM to your Cloud account, then you can remotely access your KVM by typing `glkvm.com` into a web browser on your controlling device, thus accessing the controlled device, without installing the GLKVM app.

    Click [here](remote_access_to_controlled_device_via_cloud.md){target="_blank"} for details.

- Tailscale
    
    This method is also suitable for those who cannot or do not want to install the GLKVM app, but it requires more steps.

    Bind your KVM and controlling device to the same Tailscale account, then you can remotely access your KVM by typing the KVM's Tailscale virtual IP into a web browser on your controlling device, thus accessing the controlled device, without installing the GLKVM app.
    
    Click [here](remote_access_to_controlled_device_via_tailscale.md){target="_blank"} for details.

Alternatively, you can locally access the controlled device through a web browser in the same local network. 

As to the controlled device, no need to install any software on it. That is to say, it can be Windows, macOS, ChromeOS, Linux, etc.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.