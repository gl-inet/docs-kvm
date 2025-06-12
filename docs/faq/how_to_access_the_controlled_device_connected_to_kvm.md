# How to access the controlled device connected to GL.iNet KVM?

Take GL-RM1 (Comet) as an example. There are three ways to access the controlled device: 

- Local access via Web browser
- Remote access via GLKVM application
- Remote access via Tailscale

## Local Access via Web browser

<iframe width="560" height="315" src="https://www.youtube.com/embed/PlJ5JLt7aUo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To locally access the controlled device via web browser, please ensure the controlling device (i.e. the host) and the controlled device are in the same LAN network.

Then enter `glkvm.local` in the web browser (Chrome or Edge is recommended for better compatibility), and you will be directed to the GLKVM local management page.

Alternatively, find the LAN IP address of your GL.iNet KVM device from the upper router, then enter its IP address in the browser, it will also take you to the local management page as well.

## Remote Access via GLKVM App

Install the [GLKVM application](https://www.gl-inet.com/app-rm/){target="_blank"} on the controlling device, then you can remotely access GL.iNet KVM and the controlled device.

## Remote Access via Tailscale

If you cannot or don't want to install GLKVM application, you may use Tailscale to achieve remote access, which is integrated in Comet (GL-RM1). 

In this way, you can directly access Comet by typing its Tailscale virtual IP into a browser, without installing GLKVM app.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.