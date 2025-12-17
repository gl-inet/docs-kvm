# Comet Pro (GL-RM10) Quick Setup Guide

## Connect the Devices

For clarity, the controlling device is referred to as Device A, and the controlled device as Device B.

![connect devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/connect-devices.png){class="glboxshadow"}

1. Connect the Comet Pro to the power source.

    ![power on](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/01-power-on.jpg){class="glboxshadow"}

2. Use an HD cable to connect the Comet Pro's HD IN port to the HD OUT port of the Device B. Use another HD cable to connect the Comet Pro's HD OUT port to the monitor if the Device B is a desktop computer.

    ![Connect the HD cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/02-hd-cable.png){class="glboxshadow"}

3. Connect the Comet Pro's USB Type-C port to the USB interface of the Device B using a USB cable.

    ![Connect the USB cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/03-usb-cable.png){class="glboxshadow"}

4. Connect the Comet Pro to a network source via an Ethernet cable or Wi-Fi.

    - Ethernet: Connect the Comet Pro's Ethernet port to a network source.

        ![Connect via ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/04-ethernet.png){class="glboxshadow"}

    - Wi-Fi: Swipe left on the touchscreen, connect Comet Pro to an existing Wi-Fi network (2.4G/5G supported).

        ![Connect via wifi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/04-wifi.png){class="glboxshadow"}

5. Device connection is complete. 

    Now you can access Comet Pro's control panel locally or remotely.

## Local Access to Comet Pro

There are two methods to access Comet Pro via LAN.

**Method 1**. via Domain

First, ensure your controlling device is on the same LAN as your Comet Pro.

Launch a browser on the controlling device. Chrome or Edge is recommended for better compatibility.

Enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

**Note**: You will need to set up your admin password when accessing your KVM for the first time.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow gl-90-desktop"}

You will be able to access Comet Pro's control panel locally, thus access the controlled device connected to it.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow gl-90-desktop"}

**Method 2**. via IP address

Find Comet Pro's IP address on the touchscreen, enter this IP address in the browser, and you will be able to access it locally, thus access the controlled device.

For example, if the Comet Pro's IP address is `192.168.8.197`. 

Open a new tab in the browser and enter this IP in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

**Note**: You will need to set up your admin password when accessing your KVM for the first time.

![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow gl-90-desktop"}

You will be able to access the Comet Pro's control panel locally, thus access the controlled device connected to it.

![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow gl-90-desktop"}

## Remote Access to Comet Pro

**Method 1**. via Cloud service

1. Bind your device to KVM Cloud.

    This needs to be done within the local network.

    First, locally access your Comet Pro, and go to the Cloud Service in the upper right corner. Click **Bind To Cloud**.

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    You will be re-directed to a login page. Input your glinet account and click **Log In**.

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow gl-90-desktop"}

    Confirm your device info, and click **Bind**.

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow gl-90-desktop"}

    Wait a second and your Comet Pro will be bound to your account successfully. Click **Done**.

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow gl-90-desktop"}

2. Remote access via Cloud service.

    Open a browser (take Google Chrome as an example), and enter `glkvm.com` in the address bar. You will see a login page. Use your glinet account to log in.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow gl-90-desktop"}

    After login, you will see the devices bound to your account. Click on the device you want to remotely access.

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow gl-90-desktop"}

    It will redirect to a new webpage with the domain `glkvm.top`, `glkvm.site`, or `glkvm.xyz`. These domains are secure and provided by GL.iNet.
    
    Enter the admin password and log in.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow gl-90-desktop"}

    Then you will be able to access your Comet Pro and the controlled device remotely via Cloud, without installing the app.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow gl-90-desktop"}

**Method 2**. via GLKVM App

1. Install the [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} on your controlling device.

2. Sign up and log in.
    
    Sign up for a GL.iNet account. If you already have one, skip this step.

    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/sign_up_account.png){class="glboxshadow"}
    
    Enter the username and password to log in.
    
    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/log_in_account.png){class="glboxshadow"}

4. Bind your device.

    If your Comet Pro and the controlling device are in the same local area network, click **Add Device**. It will start searching automatically.

    ![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow gl-90-desktop"}

    If your Comet Pro has not been detected or it is not in the same local network, click the **+** button in the upper right corner to add it manually.

    ![add manually](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_manually_1.png){class="glboxshadow gl-90-desktop"}

    Customize the device name and input the S/N, which can be found on the bottom label.

    ![add manually](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_manually_2.png){class="glboxshadow"}

    Binding device. Please ensure a stable network connection.

    ![binding](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/binding.png){class="glboxshadow gl-90-desktop"}
    
    Binding successful. Your Comet Pro has been bound to your account. Click **Done**.

    ![binding successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/binding_successful.png){class="glboxshadow gl-90-desktop"}

    You will be directed to the homepage, where your Comet Pro will be displayed Online.

    ![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow gl-90-desktop"}

    Click on it, input the admin password (created during the first access), and you can remotely access the Comet Pro's control panel, thus access the controlled device connected to it.

    ![remote access via app](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/remote_access_via_app.jpg){class="glboxshadow gl-90-desktop"}

**Method 3**. via Tailscale

Comet Pro integrates with Tailscale, allowing you to remotely access it via Tailscale virtual network.

In the control panel, navigate to **Apps Center** -> **Tailscale**, bind your Comet Pro to your Tailscale account. 

Next, bind your controlling device to the same account. Then you will be able to remotely access your Comet Pro by typing its Tailscale virtual IP into a web browser on the controlling device, without installing GLKVM app.

Click [here](../../faq/remote_access_to_controlled_device_via_tailscale.md){target="_blank"} for more instructions.
