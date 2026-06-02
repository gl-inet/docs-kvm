# How to access KVM remotely via Tailscale

GL.iNet KVM integrates Tailscale, allowing you to bind it to the Tailscale virtual network for remote access — no need to install the GLKVM app or use the cloud service. This is particularly useful when your controlling device does not run Windows, macOS, Android, or iOS (and thus cannot install the GLKVM app), or when you do not want to use the GLKVM app or cloud service.

Follow these steps to remotely access your GL.iNet KVM via Tailscale.

## Bind KVM to Tailscale

**Before you begin, connect your KVM and the controlling device to the same local network.**

1. Open a browser on the controlling device. Chrome or Edge is recommended for better compatibility.
    
2. Log in to your KVM console locally using its domain or IP address. Here we use the default domain as an example.

    Enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter your admin password.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

3. After logging in, go to **Apps Center** -> **Tailscale**. Enable Tailscale and click **Bind Device**.

    ![enable tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enable_tailscale.png){class="glboxshadow"}

4. You will be directed to the Tailscale login page. Enter your email to log in.

    ![log in tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

5. After logging in, the page prompts that you are about to connect the device glkvm to your Tailnet. Click **Connect**.

    ![connect kvm to tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_kvm_to_tailscale.png){class="glboxshadow"}

    Your KVM device will then be bound to your tailnet successfully. 

    ![bind kvm successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_kvm_successful.png){class="glboxshadow"}
    
6. You will be redirected to your Tailscale console, where a device labeled **glkvm** is displayed under **Machines**.

    ![tailscale console 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_1.png){class="glboxshadow"}

## Bind the controlling device

The example below demonstrates how to bind a Windows laptop (as the controlling device) to the Tailscale network.

1. Install Tailscale on your laptop from [here](https://tailscale.com/download){target="_blank"}.

2. Run Tailscale on the laptop and log in with the same email.

    ![log in tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

3. After logging in, the page prompts that you are about to connect the laptop (e.g. the controlling device) to your Tailnet. Click **Connect**.

    ![connect pc to tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_pc_to_tailscale.png){class="glboxshadow"}

    Your laptop will then be bound to your tailnet successfully. 

    ![bind pc successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_pc_successful.png){class="glboxshadow"}

4. You will be redirected to your Tailscale console, where the controlling device is also displayed under **Machines**.

    ![tailscale console 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_2.png){class="glboxshadow"}

## Remote access via Tailscale

In the Tailscale console, click the glkvm's **Address** (`100.104.185.26` in this example).

![get vittual ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/get_vitual_ip.png){class="glboxshadow"}

You will see four values:

- glkvm (device name)
- glkvm.tail1fd0.ts.net (Tailscale-assigned domain)
- fd7a:115c:a1e0:301:b92f (virtual IPv6)
- 100.104.185.26 (virtual IPv4). 

They are allocated by Tailscale for device identification and virtual network communication. You can remotely access your KVM device using the Tailscale-assigned domain, vitual IPv4 and virtual IPv6.

Take the virtual IPv4 as an example.

1. Copy the virtual IPv4 address of your KVM device. 

2. Open a new tab and paste the IP address into the address bar.

    ![access vitual ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enter_vitual_ip.png){class="glboxshadow"}

    A privacy error may appear. [Why do I get this privacy error?](privacy_error_from_your_browser.md){target="_blank"}

    ![privacy error](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/privacy_error.png){class="glboxshadow"}

    Click **Advanced**, then **Proceed to 100.104.185.26**. You will be redirected to the GLKVM login page.

    ![proceed](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/proceed.png){class="glboxshadow"}

3. Enter your admin password to log in. You can now access your GL.iNet KVM and the controlled device via the Tailscale virtual IP.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/remote_access_via_tailscale.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.