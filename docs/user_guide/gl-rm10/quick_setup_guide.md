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

There are two methods to access Comet Pro in the local network: via domain name or IP address.

### Domain

First, ensure your controlling device is on the same LAN as your Comet Pro.

Launch a browser on the controlling device. Chrome or Edge is recommended for better compatibility.

Enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

**Note**: You will need to set up your admin password when accessing your KVM for the first time.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

You will be able to access Comet Pro's control panel locally, thus access the controlled device connected to it.

![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### IP address

Find Comet Pro's IP address on the touchscreen, enter this IP address in the browser, and you will be able to access it locally, thus access the controlled device.

For example, if the Comet Pro's IP address is `192.168.8.197`. 

Open a new tab in the browser and enter this IP in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

**Note**: You will need to set up your admin password when accessing your KVM for the first time.

![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

You will be able to access the Comet Pro's control panel locally, thus access the controlled device connected to it.

![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Remote Access to Comet Pro

There are three ways to access Comet Pro remotely: via Cloud service, GLKVM App, or Tailscale.

### Cloud service

1. Bind your device to KVM Cloud.

    **Note**: Device binding needs to be done within the local network. 

    There are two ways to bind your KVM to the Cloud: Regular Binding or Dynamic Code Binding. Here we take Regular Binding as an example. If you prefer Dynamic Code Binding, click [here](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} for detailed instructions.

    First, locally access your Comet Pro, and navigate to **Cloud Service** in the upper right corner. Click **Bind To Cloud**.

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    You will be re-directed to a login page. Log in with your glinet cloud account. 

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Second, confirm your device info, and click **Bind**.

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Wait a second and your Comet Pro will be bound to your account successfully. Click **Done**.

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Remote access via Cloud service.

    Open a browser (take Google Chrome as an example), and enter `glkvm.com` in the address bar. You will see a login page. Use your glinet account to log in.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    After login, you will see the devices bound to your account. Click on the device you want to remotely access.

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    It will redirect to a new webpage with the domain `glkvm.xyz`, `glkvm.site`, or `glkvm.top`. These domains are secure and provided by GL.iNet.
    
    Enter the admin password and log in.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    Then you will be able to access your Comet Pro and the controlled device remotely via Cloud, without installing the app.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

### GLKVM App

1. Install the [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} on your controlling device.

2. Log in with your GL.iNet account. 

    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    If you don't have a GL.iNet account, sign up for one and then log in.
    
    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

3. Bind your device.

    After login, the page will display as follows. Click **Add Device**.

    There are three ways to bind your device: Auto Discover, S/N Code, and Dynamic Binding Code.

    ![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

    - Auto Discover
    
        This needs to be done within the local network. Please ensure that your KVM and the controlling device are on the same LAN.
    
        Click **Auto Discover**. It will start searching automatically.
    
        ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}
        
        Locate your KVM and enter its Device ID to bind it to your account.
    
        ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}
    
    - S/N Code
    
        This applies to the scenario where your KVM is not detected, or is not on the same LAN, but you have its serial number (S/N).
        
        Click **S/N Code**. In the pop-up window, customize the device name and enter the S/N, which is printed on the label bottom of your KVM device.
    
        ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}
    
    - Dynamic Binding Code
    
        Please upgrade your KVM firmware to version 1.7 before using this feature.
    
        This needs to be done within the local network. Please ensure that your KVM and the controlling device are on the same LAN.
    
        1. Log in to your KVM locally using domain or IP address. Click [here](../../faq/local_access_to_controlled_device_via_browser.md) for details. 
    
        2. Navigate to **Cloud Service** in the upper-right corner, and click **Bind With Code**. 
    
            ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}
    
        3. It will generate an 8-digit dynamic code randomly for device binding, valid for 60 seconds. Click the code to copy it.
    
            ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}
    
        4. Back to the GLKVM app, enter the dynamic binding code and click **Bind**.
    
            ![dynamic code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

4. Remote access via GLKVM App.

    Once your KVM device is bound to your account, it will show "Online" in the app.

    ![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

    Click your KVM device. It will open a new window and start connecting.

    ![connecting](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

    Once connected, enter the admin password to log in to your device.

    ![connected log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

    You will then access your KVM device, through which you can access the controlled device.

    ![connected access](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

### Tailscale

Comet Pro integrates with Tailscale, allowing you to remotely access it via Tailscale virtual network.

In the control panel, navigate to **Apps Center** -> **Tailscale**, bind your Comet Pro to your Tailscale account. 

Next, bind your controlling device to the same account. Then you will be able to remotely access your Comet Pro by typing its Tailscale virtual IP into a web browser on the controlling device, without installing GLKVM app.

Click [here](../../faq/remote_access_to_controlled_device_via_tailscale.md){target="_blank"} for detailed instructions.
