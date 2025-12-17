# Comet PoE (GL-RM1PE) Quick Setup Guide

## Connect the Devices

For clarity, the controlling device is referred to as Device A, and the controlled device as Device B.

![distinguish devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/connect-1.png){class="glboxshadow"}

1. Connect the Comet PoE to the PoE Switch with an Ethernet cable.

    ![connect ethernet cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/connect-2.png){class="glboxshadow gl-80-desktop"}

2. Use an HD cable to connect the Comet PoE's HD IN port to the HD OUT port of the Device B.

    ![connect hdmi cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/connect-3.png){class="glboxshadow gl-80-desktop"}

3. Connect the Comet PoE's USB port to the USB interface of the Device B using a USB cable.

    ![Connect usb cbale](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/connect-4.png){class="glboxshadow gl-80-desktop"}

4. Device connection is complete. 

    You can now access the Comet PoE control panel locally via a browser on the controlling device, or download the GLKVM app on the controlling device to remotely access it.

## Local Access to Comet PoE

There are two methods to access Comet PoE via LAN.

**Method 1**. via Domain

First, ensure your controlling device is on the same LAN as your Comet PoE.

Launch a browser on the controlling device. Chrome or Edge is recommended for better compatibility.

Enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

**Note**: You will need to set up your admin password when accessing your KVM for the first time.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow gl-90-desktop"}

You will be able to access the Comet PoE's control panel locally, thus access the controlled device connected to it.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow gl-90-desktop"}

**Method 2**. via IP address

Find the IP address of Comet PoE in the upper router, enter this IP address in the browser, and you will be able to access the Comet PoE locally, thus access the controlled device.

Take GL-AXT1800 as an example: Comet PoE is connected to the LAN port of GL-AXT1800 router via an Ethernet cable, and the controlled device is connected to Comet PoE correctly via HD cable and USB cable.

Log in to the web admin panel of GL-AXT1800, find the IP address of Comet PoE in the Client list, as shown below.

![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/local_access_via_ip.png){class="glboxshadow"}

Open a new tab in the browser, enter Comet PoE's IP in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

**Note**: You will need to set up your admin password when accessing your KVM for the first time.

![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow gl-90-desktop"}

You will be able to access the Comet PoE's control panel locally, thus access the controlled device connected to it.

![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow gl-90-desktop"}

## Remote Access to Comet PoE

**Method 1**. via Cloud service

1. Bind your device to KVM Cloud.

    This needs to be done within the local network.

    First, locally access your Comet PoE, and go to the Cloud Service in the upper right corner. Click **Bind To Cloud**.

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    You will be re-directed to a login page. Input your glinet account and click **Log In**.

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow gl-90-desktop"}

    Confirm your device info, and click **Bind**.

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow gl-90-desktop"}

    Wait a second and your device will be bound to your account successfully. Click **Done**.

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow gl-90-desktop"}

2. Remote access via Cloud service.

    Open a browser (take Google Chrome as an example), and enter `glkvm.com` in the address bar. You will see a login page. Use your glinet account to log in.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow gl-90-desktop"}

    After login, you will see the devices bound to your account. Click on the device you want to remotely access.

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow gl-90-desktop"}

    It will redirect to a new webpage with the domain `glkvm.xyz`, `glkvm.site`, or `glkvm.top`. These domains are secure and provided by GL.iNet.
    
    Enter the admin password and log in.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow gl-90-desktop"}

    Then you will be able to access the Comet PoE and the controlled device remotely via Cloud, without installing the app.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow gl-90-desktop"}

**Method 2**. via GLKVM App

1. Install the [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} on your controlling device.

2. Sign up and log in.
    
    Sign up for a GL.iNet account. If you already have one, skip this step.

    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/sign_up_account.png){class="glboxshadow"}
    
    Enter the username and password to log in.
    
    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/log_in_account.png){class="glboxshadow"}

4. Bind your device.

    If your Comet PoE and the controlling device are in the same local area network, click **Add Device**. It will start searching automatically.

    ![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow gl-90-desktop"}

    If your Comet PoE has not been detected or it is not in the same local network, click the **+** button in the upper right corner to add it manually.

    ![add manually](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_manually_1.png){class="glboxshadow gl-90-desktop"}

    Customize the device name and input the S/N, which can be found on the bottom label.

    ![add manually](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_manually_2.png){class="glboxshadow"}

    Binding device. Please ensure a stable network connection.

    ![binding](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/binding.png){class="glboxshadow gl-90-desktop"}
    
    Binding successful. Your Comet PoE has been bound to your account. Click **Done**.

    ![binding successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/binding_successful.png){class="glboxshadow gl-90-desktop"}

    You will be directed to the homepage, where your Comet PoE will be displayed Online.

    ![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow gl-90-desktop"}

    Click on it, input the admin password (created during the first access), and you can remotely access the Comet PoE's control panel, thus access the controlled device connected to it.

    ![remote access via app](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/remote_access_via_app.jpg){class="glboxshadow gl-90-desktop"}

**Method 3**. via Tailscale

Comet PoE integrates with Tailscale, allowing you to remotely access it via Tailscale virtual network.

In Comet PoE's control panel, navigate to **Apps Center** -> **Tailscale**, bind Comet PoE to your Tailscale account.

Next, bind your controlling device to the same account. Then you will be able to remotely access your Comet PoE by typing its Tailscale virtual IP into a web browser on the controlling device, without installing GLKVM app.

Click [here](../../faq/remote_access_to_controlled_device_via_tailscale.md){target="_blank"} for more instructions.