# How to access the KVM remotely via NetBird?

> Note: Please upgrade your KVM firmware to v1.9.0 before using this feature.

[NetBird](https://netbird.io/){target="_blank"} is an open-source zero trust networking platform that lets you build secure private networks for home and business use. As a WireGuard®-based overlay network, NetBird enables secure access to your devices anytime and anywhere.

GL.iNet KVM integrates NetBird, allowing you to bind it to the NetBird virtual network for remote access — no need to install the GLKVM app or use the cloud service. 

Follow these steps to remotely access your GL.iNet KVM via NetBird.

## Bind KVM to NetBird

**Before you begin, connect your KVM and the controlling device to the same local network.**

1. Log in to your KVM console locally using its domain or IP address, then go to **Apps Center** -> **NetBird**. Enable NetBird and click **Bind Device**. 

    ![bind device](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/1-bind-device.png){class="glboxshadow"}

2. You will be redirected to the device confirmation page. Click **Confirm**.

    ![confirm device](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/2-confirm.png){class="glboxshadow"}

3. Sign in to your NetBird account. If you don't have an account, sign up first.

    ![netbird sign in](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/3-signin.png){class="glboxshadow"}

4. After signing in, the KVM device will be automatically bound to your account.

    ![kvm connected](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/4-connected.png){class="glboxshadow"}

    On the NetBird dashboard, you can also see your KVM listed on the **Peers** page.

    ![netbird dashboard](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/5-dashboard.png){class="glboxshadow"}

## Bind the controlling device

The example below demonstrates how to bind a Windows laptop (as the controlling device) to the NetBird network.

1. Install NetBird on your laptop from [here](https://app.netbird.io/install){target="_blank"}. 

    ![install netbird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/6-install.png){class="glboxshadow"}

2. Run NetBird on the laptop and add it to the same NetBird network. 

    NetBird does not display a separate window/UI on the desktop; it only resides as an icon in the system tray (bottom-right corner). All operations are performed via the right-click menu.

    Right click the NetBird icon, and click **Connect**. 

    ![pc connect](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/7-pc-connect.png){class="glboxshadow gl-50-desktop"}

3. In the pop-up window, click **Accept** to authorize.

    ![authorize](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/8-authorize.png){class="glboxshadow"}

    Your laptop will be automatically bound to your account and added to the same NetBird network.

    ![pc connected](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/9-login-success.png){class="glboxshadow"}

4. On the NetBird dashboard, there are two devices on the **Peers** page: your KVM and the controlling laptop.

    ![netbird dashboard](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/10-dashboard.png){class="glboxshadow"}

## Remote access via NetBird

The example below demonstrates how to remotely access the KVM console via the NetBird virtual IP address.

1. On your laptop, sign in to the NetBird dashboard and navigate to **Peers**. 

    Find your KVM device and click its **NetBird IP** (`100.100.141.229` in this example) to copy the virtual IP.

    ![kvm netbird ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/11-kvm-netbird-ip.png){class="glboxshadow"}

    Hover your cursor over the IP address to view more details, such as Public IP, domain and region.

2. Open a new browser tab, paste the copied NetBird IP into the address bar and hit Enter. You will be redirected to the GLKVM login page. 

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-login.png){class="glboxshadow"}

    Enter your admin password to log in. You can now access your GL.iNet KVM and the controlled device via the NetBird IP.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-access.png){class="glboxshadow"}

    **Tip**: A privacy error may appear when accessing this NetBird IP for the first time. Simply click **Advanced** -> **Proceed** to continue. See [Privacy error from your browser](privacy_error_from_your_browser.md){target="_blank"} for details.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.