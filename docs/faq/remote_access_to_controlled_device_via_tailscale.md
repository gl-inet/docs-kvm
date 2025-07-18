# How to remotely access the controlled device via Tailscale?

GL.iNet KVM integrates Tailscale, allowing you to bind it to the Tailscale virtual network for remote access - no need to install GLKVM app. This is particularly useful when your controlling device runs neither Windows nor macOS. 

Follow these steps to remotely access your GL.iNet KVM and the controlled device via Tailscale.

## 1. Enable Tailscale in local access

**Before you begin, please connect your KVM and the controlling device to the same network.**

Then access your KVM's control panel locally using domain name or IP address. A domain name will be used here for illustration.

Firstly, launch a browser on the controlling device. Chrome or Edge is recommended for better compatibility.
    
Secondly, enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain.png){class="glboxshadow"}

You will be able to access your KVM's control panel locally.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/local_access_domain.png){class="glboxshadow"}

Thirdly, in the control panel, navigate to **Apps Center** -> **Tailscale**, enable Tailscale.

![apps center](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/apps_center.jpg){class="glboxshadow"}

## 2. Bind KVM to your tailnet

Upon enabling tailscale, the page will display an option to bind device. Click on **Bind Device**.

![enable tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enable_tailscale.png){class="glboxshadow"}

You will be directed to the Tailscale login page. Enter your email to log in.

![log in tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

After logging in, the page prompts that you are about to connect the device glkvm to your Tailnet. Click on **Connect**.

![connect kvm to tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_kvm_to_tailscale.png){class="glboxshadow"}

Device binding successful. Your KVM device has been successfully bound to your tailnet. 

![bind kvm successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_kvm_successful.png){class="glboxshadow"}

You will be re-directed to your Tailscale console, where a device labeled **glkvm** is displayed under **Machines**.

![tailscale console 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_1.png){class="glboxshadow"}

## 3. Bind controlling device to your tailnet

Install Tailscale on your controlling device from [here](https://tailscale.com/download){target="_blank"}, and log in with the same Tailscale account. Your controlling device will be bound to your tailnet.

The following is an example of binding a Windows laptop as a controlling device to tailnet.

Run Tailscale on the controlling device. Log in with the same email.

![log in tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

After logging in, the page prompts that you are about to connect the controlling device (e.g. a laptop) to your Tailnet. Click on **Connect**.

![connect pc to tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_pc_to_tailscale.png){class="glboxshadow"}

Device binding successful. The controlling device has been successfully bound to your tailnet. 

![bind pc successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_pc_successful.png){class="glboxshadow"}

You will be re-directed to your Tailscale console, where the controlling device is also displayed under **Machines**.

![tailscale console 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_2.png){class="glboxshadow"}

## 4. Remote access via Tailscale

In the Tailscale console, click on the **Address** of glkvm, which is **100.104.185.26** in the following image.

![get vittual ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/get_vitual_ip.png){class="glboxshadow"}

Four values will be displayed above:

- glkvm (device name)
- glkvm.tail1fd0.ts.net (Tailscale-assigned domain)
- fd7a:115c:a1e0:301:b92f” (virtual IPv6)
- 100.104.185.26 (virtual IPv4). 

They are allocated by Tailscale for device identification and virtual network communication. You can remotely access your KVM device using the Tailscale-assigned domain, vitual IPv4 and virtual IPv6.

Take the virtual IPv4 as an example.

Copy the virtual IPv4 of your KVM device. Open a new tab and enter the copied IP address.

![access vitual ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enter_vitual_ip.png){class="glboxshadow"}

It may prompt a privacy error. [Why do I get this privacy error?](privacy_error_from_your_browser.md){target="_blank"}

![privacy error](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/privacy_error.png){class="glboxshadow"}

Click on **Advanced**, and **Proceed to 100.104.185.26**.

![proceed](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/proceed.png){class="glboxshadow"}

You will be directed to the GLKVM login page. Enter the admin password to log in. 

![access login page](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/access_login_page.png){class="glboxshadow"}

You will be able to access your GL.iNet KVM and the controlled device via Tailscale virtual IP.

![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/remote_access_via_tailscale.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.