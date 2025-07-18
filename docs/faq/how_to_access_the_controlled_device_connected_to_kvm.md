# How to access the controlled device connected to GL.iNet KVM?

There are three ways to access the controlled device connected to GL.iNet KVM: 

- Local access via web browser
- Remote access via GLKVM app
- Remote access via Tailscale

## Local Access via web browser

Before you begin, please ensure your KVM and the controlling device are in the same LAN network.

There are two ways to locally access the controlled device via web browser.

**Method 1. Using Domain Name**

Launch a browser on the controlling device. Chrome or Edge is recommended for better compatibility.

Enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

You will be able to access your KVM's control panel locally, thus access the controlled device connected to it.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.png){class="glboxshadow"}

**Method 2. Using IP Address**

Find your KVM's IP address in the upper router, enter this IP into the browser, and you will be able to access your KVM locally, thus access the controlled device.

Take a router GL-AXT1800 and a KVM Comet as an example: Comet is connected to the LAN port of GL-AXT1800 router via an Ethernet cable, and the controlled device is connected to Comet correctly via HD cable and USB cable.

Log in to the web admin panel of GL-AXT1800, find the IP address of Comet in the Client list, as shown below.

![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/local_access_via_ip.png){class="glboxshadow"}

Open a new tab in the browser, enter Comet's IP in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

You will be able to access the Comet's control panel locally, thus access the controlled device connected to it.

![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.png){class="glboxshadow"}

## Remote Access via GLKVM App

Install the [GLKVM app](https://www.gl-inet.com/app-rm/){target="_blank"} on your controlling device, and follow [this link](remote_access_to_controlled_device_via_glkvm_app.md){target="_blank"} to remotely access your GL.iNet KVM and the controlled device via GLKVM app.

## Remote Access via Tailscale

GL.iNet KVM integrates Tailscale, allowing you to bind it to the Tailscale virtual network for remote access - no need to install GLKVM app. This is particularly useful when your controlling device runs neither Windows nor macOS. 

Follow [this link](remote_access_to_controlled_device_via_tailscale.md){target="_blank"} to remotely access your GL.iNet KVM and the controlled device via Tailscale.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.