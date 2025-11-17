# Comet 5G (GL-RM10RC) Quick Setup Guide

## Connect the Devices

For clarity, the controlling device is referred to as Device A, and the controlled device as Device B.

![connect devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/connect_device.png){class="glboxshadow"}

1. Insert a SlM card into your Comet 5G, and power it on.

    ![insert sim power on](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/01-insert-sim-power-on.jpg){class="glboxshadow"}

2. Use an HDMI cable to connect the Comet 5G's HDMI IN port to the HDMI port of Device B. Use another HDMI cable to connect the Comet 5G's HDMI OUT port to the monitor if Device B is a desktop computer.

    ![Connect the HDMI cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/02-hdmi-cable.jpg){class="glboxshadow"}

3. Connect the Comet 5G's Type-C port to the Type-C interface of Device B using a USB-C cable.

    ![Connect the USB cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/03-usb-cable.jpg){class="glboxshadow"}

4. Connect the Comet 5G to a network source.

    - 5G: With SIM card inserted, the 5G connection will be automatically established upon system startup. The connection priority is Ethernet > Wi-Fi > 5G.

    - Wi-Fi: Swipe left on the touchscreen, and connect Comet 5G to an existing Wi-Fi network (2.4G and 5G supported).

        ![Connect via wifi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/04-network-wifi.png){class="glboxshadow"}

    - Ethernet: Connect the Comet 5G's Ethernet port to a network source.

        ![Connect via ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/04-network-ethernet.png){class="glboxshadow"}

5. Device connection is complete. 

    Now you can access Comet 5G's control panel locally or remotely.

## Local Access to Comet 5G

There are two methods to access Comet 5G locally.

**Method 1**. via Domain

First, ensure your controlling device is on the same LAN as your Comet 5G.

Launch a browser on the controlling device. Chrome or Edge is recommended for better compatibility.

Enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow gl-90-desktop"}

You will be able to access Comet 5G's control panel locally, thus access the controlled device connected to it.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow gl-90-desktop"}

**Method 2**. via IP address

Find Comet 5G's IP address on the touchscreen, enter this IP address in the browser, and you will be able to access it locally, thus access the controlled device.

For example, if the Comet 5G's IP address is `192.168.8.197`. 

Open a new tab in the browser and enter this IP in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow gl-90-desktop"}

You will be able to access the Comet 5G's control panel locally, thus access the controlled device connected to it.

![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow gl-90-desktop"}

## Remote Access to Comet 5G

**Method 1**. via Cloud service

1. Bind your device to KVM Cloud.

    This needs to be done within the local network.

    First, locally access your Comet 5G, and go to the Cloud Service in the upper right corner. Click **Access Cloud**.

    ![access cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/access_cloud.jpg){class="glboxshadow"}

    You will be re-directed to a login page. Input your glinet account and click **Log In**.

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow gl-90-desktop"}

    Confirm your device info, and click **Bind**.

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow gl-90-desktop"}

    Wait a second and your Comet 5G will be bound to your account successfully. Click **Done**.

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow gl-90-desktop"}

2. Remote access via Cloud service.

    Open a browser (take Google Chrome as an example), and enter `glkvm.com` in the address bar. You will see a login page. Use your glinet account to log in.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow gl-90-desktop"}

    After login, you will see the devices bound to your account. Click on the device you want to remotely access.

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow gl-90-desktop"}

    It will open a new tab asking for device admin password. Enter the admin password and log in.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow gl-90-desktop"}

    Then you will be able to access your Comet 5G and the controlled device remotely via Cloud, without installing the app.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow gl-90-desktop"}

**Method 2**. via GLKVM App

1. Install the [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} on your controlling device.

2. Sign up and log in.
    
    Sign up for a GL.iNet account. If you already have one, skip this step.

    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/sign_up_account.png){class="glboxshadow"}
    
    Enter the username and password to log in.
    
    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/log_in_account.png){class="glboxshadow"}

4. Bind your device.

    If your Comet 5G and the controlling device are in the same local area network, click **Add Device**. It will start searching automatically.

    ![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow gl-90-desktop"}

    If your Comet 5G has not been detected or it is not in the same local network, click the **+** button in the upper right corner to add it manually.

    ![add manually](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_manually_1.png){class="glboxshadow gl-90-desktop"}

    Customize the device name and input the S/N, which can be found on the bottom label.

    ![add manually](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_manually_2.png){class="glboxshadow"}

    Binding device. Please ensure a stable network connection.

    ![binding](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/binding.png){class="glboxshadow gl-90-desktop"}
    
    Binding successful. Your Comet 5G has been bound to your account. Click **Done**.

    ![binding successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/binding_successful.png){class="glboxshadow gl-90-desktop"}

    You will be directed to the homepage, where your Comet 5G will be displayed Online.

    ![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow gl-90-desktop"}

    Click on it, input the admin password (created during the first access), and you can remotely access the Comet 5G's control panel, thus access the controlled device connected to it.

    ![remote access via app](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/remote_access_via_app.jpg){class="glboxshadow gl-90-desktop"}

**Method 3**. via Tailscale

Comet 5G integrates with Tailscale, allowing you to remotely access it via Tailscale virtual network.

In the control panel, navigate to Apps Center -> Tailscale, bind your Comet 5G to your Tailscale account. 

Next, bind your controlling device to the same account. Then you will be able to remotely access your Comet 5G by typing its Tailscale virtual IP into a web browser on the controlling device, without installing GLKVM app.

Click [here](../../faq/remote_access_to_controlled_device_via_tailscale.md){target="_blank"} for more instructions.
