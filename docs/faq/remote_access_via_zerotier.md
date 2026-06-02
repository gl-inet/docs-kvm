# How to access the KVM remotely via ZeroTier?

> Note: Please upgrade your KVM firmware to v1.8.0 before using this feature.

GL.iNet KVM integrates ZeroTier, allowing you to bind it to the ZeroTier network for remote access — no need to install the GLKVM app or use the cloud service. 

Follow these steps to remotely access your GL.iNet KVM via ZeroTier.

## Enable ZeroTier

**Before you begin, connect your KVM and the controlling device to the same local network.**

1. Open a browser on the controlling device. Chrome or Edge is recommended for better compatibility.
    
2. Log in to your KVM console locally using its domain or IP address. Here we use the local IP address as an example.

    Enter the KVM's **LAN IP address** (found on the touchscreen or in your router) in the address bar. You will be directed to the GLKVM login page. Enter your admin password.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/1_local_access.png){class="glboxshadow"}

3. After logging in, go to **Apps Center** -> **ZeroTier**. Enable ZeroTier, and you will see a yellow prompt as shown below. 

    Click the hyperlink or [here](https://my.zerotier.com/){target="_blank"} to sign in to ZeroTier Central and create your ZeroTier network.

    ![enable zerotier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/2_enable_zerotier.png){class="glboxshadow"}
    
## Bind KVM to ZeroTier

1. When signing in to [ZeroTier](https://my.zerotier.com/){target="_blank"} for the first time, you may be required to select ZeroTier Central.

    ![select central](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/3_select_central.png){class="glboxshadow"}

    Select the appropriate version to proceed. We take **New Central** as an example here.
    
    Sign in with your email and password. If you don't have an account, sign up first.

    ![zerotier signin](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/4_zerotier_signin.png){class="glboxshadow"}

2. After signing in, create an organization.

    ![create organization](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/5_create_org.png){class="glboxshadow"}

3. Select a plan. Here we choose **Personal** plan as an example, which includes 10 devices, 1 network admin, and 1 network. If you need to create more networks, add more devices, or add custom routes and DNS, choose Essential or Scale plan.

    ![select plan](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/6_select_plan.png){class="glboxshadow"}

4. Now your ZeroTier network has been created. Copy the **Network ID**, which is a 16-character alphanumeric string. You will need it later when adding devices to your ZeroTier network. Keep this tab open.

    ![network id](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/7_copy_network_id.png){class="glboxshadow"}

5. Go back to your KVM console, go to **Apps Center** -> **ZeroTier**. Locate the **Network ID** and click **Set**.

    ![network id](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id1.png){class="glboxshadow"}

    In the pop-up window, paste the **Network ID** and click **Confirm**.

    ![network id](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id2.png){class="glboxshadow"}

    You will see a yellow prompt on the console, indicating that this device needs to be authorized. 

    ![authorize1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize1.png){class="glboxshadow"}

6. Go back to ZeroTier Central. You will see a device (your KVM) waiting for approval. Click **Authorize**.

    ![authorize2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize2.png){class="glboxshadow"}

    Once authorized, the status will change to Authorized in green, as shown below.

    ![authorized1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized1.png){class="glboxshadow"}

    On the KVM console, you can also view the **Network ID** and **Virtual IP**, as shown below.

    ![authorized2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized2.png){class="glboxshadow"}

## Bind the controlling device

The example below demonstrates how to bind a Windows laptop (as the controlling device) to the ZeroTier network.

1. Install ZeroTier on your laptop from [here](https://www.zerotier.com/download/){target="_blank"}. 

2. Run ZeroTier on the laptop and add it to the same ZeroTier network. 

    Note that ZeroTier does not display a separate window/UI on the desktop; it only resides as an icon in the system tray (bottom-right corner). All operations are performed via the right-click menu.

    Right click the ZeroTier icon, and click **Join New Network**. In the pop-up window, enter the same **Network ID** to add this PC to the same ZeroTier network.

    ![join network](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/11_pc_join_network.jpg){class="glboxshadow"}

    Then go to ZeroTier Central, fine the Pending device and authorize it.

    ![authorize](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/12_authorize.png){class="glboxshadow"}

2. Once authorized, the status will change to Authorized in green, as shown below.

    ![authorized](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/13_authorized.png){class="glboxshadow"}

3. Now your KVM and the laptop are both added into the same ZeroTier network. You can tell by their Network ID, as shown below.

    ![same zt network](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/14_same_zt_network.png){class="glboxshadow"}

## Remote access via ZeroTier

The example below demonstrates how to remotely access the KVM console via the ZeroTier IP address.

1. On your laptop, sign in to ZeroTier Central with your account, find your KVM device, and click its **ZT IP** to copy it.

    ![zerotier ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/15_zerotier_ip.png){class="glboxshadow"}

2. Open a new browser tab, paste the copied ZeroTier IP into the address bar and hit Enter. You will be redirected to the GLKVM login page. 

    Enter your admin password to log in. You can now access your GL.iNet KVM and the controlled device via the ZeroTier IP.

    ![remote access](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/16_remote_access.png){class="glboxshadow"}

    **Tip**: A privacy error may appear when accessing this ZeroTier IP for the first time. Simply click **Advanced** -> **Proceed** to continue. See [Privacy error from your browser](privacy_error_from_your_browser.md){target="_blank"} for details.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.