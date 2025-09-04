# What devices can GL.iNet KVM control? Do I need to install any software to use KVM?

GL.iNet KVM can be used to control any device that uses HDMI output and USB input, such as laptops, desktops, Raspberry Pi, mini hosts, etc.

No software is required to be installed on the controlled device. 

As to the controlling device, whether a software needs to be installed on it depends on the way you want to access the KVM and controlled device.

## Local Access

If you want to access the controlled device in the same local area network (LAN), simply open a browser on the controlling device, enter `glkvm.local` or the KVM's IP in the address bar, and you can access the KVM locally, thus accessing the controlled device. No software needs to be installed on the controlling device.
    
Click [here](local_access_to_controlled_device_via_browser.md){target="_blank"} for details.
    
## Remote Access

- **Cloud Service**
    
    This method is ideal for those who cannot or do not want to install the GLKVM app.

    Bind your KVM to your Cloud account, then you can remotely access your KVM by typing `glkvm.com` into a web browser on your controlling device, thus accessing the controlled device, without installing the GLKVM app.

    Click [here](remote_access_to_controlled_device_via_cloud.md){target="_blank"} for details.

- **GLKVM App**
    
    If your controlling device runs Windows or macOS, you can install the [GLKVM app](https://www.gl-inet.com/app-rm/){target="_blank"} on it to remotely access your KVM, thus accessing the controlled device.
        
    Click [here](remote_access_to_controlled_device_via_glkvm_app.md){target="_blank"} for details.
    
- **Tailscale**
    
    This method is also suitable for those who cannot or do not want to install the GLKVM app, but it requires more steps.

    Bind your KVM and controlling device to the same Tailscale account, then you can remotely access your KVM by typing the KVM's Tailscale virtual IP into a web browser on your controlling device, thus accessing the controlled device, without installing the GLKVM app.
    
    Click [here](remote_access_to_controlled_device_via_tailscale.md){target="_blank"} for details.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.