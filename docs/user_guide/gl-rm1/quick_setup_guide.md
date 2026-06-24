# Comet (GL-RM1) V1/V2 Quick Setup

Watch this video or follow the steps below to set up your Comet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/JDgflRaIHw0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Connect Devices

For clarity, Device A refers to the controlling device, and Device B the controlled device.

![connect devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/01_device_distinction.jpg){class="glboxshadow"}

1. Connect the Comet to the power source.

    ![power on](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/02_power-on.jpg){class="glboxshadow"}

2. Connect the Comet's HD IN port to the Device B's HD OUT port using an HDMI cable.

    ![Connect the HD cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/03_hdmi.jpg){class="glboxshadow"}

3. Connect the Comet's USB-Device port to the Device B's USB port using a USB cable.

    ![Connect the USB port](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/04_usb-cable.jpg){class="glboxshadow"}

    !!! Warning
    
        Comet's USB‑C data port is intended solely for keyboard and mouse signal transmission. Do not connect it to any Thunderbolt host via a USB‑C to USB‑C cable. Thunderbolt ports support bidirectional power delivery, and reverse current injection may permanently damage the KVM hardware.

4. Plug the Comet's Ethernet port to a network source.

    ![Connect to network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/05_ethernet.jpg){class="glboxshadow"}

5. Device connection is complete. Now you can access the Comet's console locally or remotely.

## Local Access

There are two ways to access Comet on the local network: via domain name or IP address.

Before accessing, ensure your controlling device is on the same LAN as Comet.

### Domain

1. Launch a browser on the controlling device. Chrome or Edge is recommended for better compatibility.

2. Enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Note**: You will need to set up your admin password when accessing for the first time.

3. You can then access the Comet's console locally and gain access to the controlled device.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### IP address

1. Find Comet's IP address in the upper router.

    For example, Comet is connected to the LAN port of a GL.iNet router GL-AXT1800 via an Ethernet cable.
    
    Log in to the GL-AXT1800 web admin panel, find Comet's IP address in the Client list, as shown below.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

2. Open a new tab in the browser and enter Comet's IP in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Note**: You will need to set up your admin password when accessing for the first time.

3. You can then access the Comet's console locally and gain access to the controlled device.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Remote Access

There are multiple ways to access Comet remotely: via Cloud service, GLKVM App, Tailscale, ZeroTier, and NetBird.

### Cloud service

1. Bind your device to KVM Cloud. This needs to be done on the local network. 

    There are two ways to bind your KVM to the Cloud: Regular Binding or Dynamic Code Binding. Here we take Regular Binding as an example. If you prefer Dynamic Code Binding, click [here](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} for details.
    
    First, locally access your Comet and navigate to **Cloud Service** in the upper right corner. Click **Bind To Cloud**.

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    You will be redirected to a login page. Log in with your glinet cloud account. 

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Second, confirm your device info, and click **Bind**.

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Wait a second and your device will be bound to your account successfully. Click **Done**.

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}
    
2. Remote access via Cloud service.

    Open a browser (take Google Chrome as an example), and enter `glkvm.com` in the address bar. You will see a login page. Use your glinet account to log in.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    After login, you will see the devices bound to your account. Click on the device you want to remotely access.

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    It will redirect to a new webpage with the domain `glkvm.xyz`, `glkvm.site`, or `glkvm.top`. These domains are secure and provided by GL.iNet.
    
    Enter the admin password and log in.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    You will then be able to remotely access the KVM and the controlled device via Cloud, without installing the app.

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

### GLKVM App

1. Install the [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} on your controlling device.

2. Log in with your GL.iNet account. 

    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    If you don't have one, sign up first and log in.
    
    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

3. Bind your device.

    After login, the page will display as follows. Click **Add Device**.

    ![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

    You can bind your device in three ways: Auto Discover, S/N Code, and Dynamic Binding Code.

    ??? "Auto Discover"
    
        This needs to be done on the local network. Ensure your controlling device is on the same LAN as Comet.
    
        Click **Auto Discover**. It will start searching automatically.
    
        ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}
        
        Locate your KVM and enter its Device ID to bind it to your account.
    
        ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}
    
    ??? "S/N Code"
    
        This applies to the scenario where your KVM is not detected, or is not on the same LAN, but you have its serial number (S/N).
        
        Click **S/N Code**. In the pop-up window, customize the device name and enter the S/N, which is printed on the label bottom of your KVM device.
    
        ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}
    
    ??? "Dynamic Binding Code"
    
        This needs to be done on the local network. Ensure your controlling device is on the same LAN as Comet.
    
        1. Log in to your KVM locally using domain or IP address. Click [here](../../faq/local_access_via_browser.md) for details. 
    
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

Comet integrates with Tailscale, allowing you to remotely access it through Tailscale virtual network.

On Comet's console, navigate to **Apps Center** -> **Tailscale**, enable it and bind your Comet to your Tailscale account. 

Next, bind your controlling device to the same account. Then you will be able to remotely access your Comet by entering its **Tailscale virtual IP** in a web browser on the controlling device, without installing GLKVM app.

See [here](../../faq/remote_access_via_tailscale.md){target="_blank"} for details.

### ZeroTier

Comet integrates with ZeroTier, allowing you to remotely access it through ZeroTier virtual network.

On Comet's console, navigate to **Apps Center** -> **ZeroTier** and enable it.

Next, join both Comet and your controlling device to the same ZeroTier network (using a 16-character alphanumeric Network ID), then you can remotely access your Comet by entering its **ZeroTier IP** in a web browser on the controlling device, without installing GLKVM app.

See [here](../../faq/remote_access_via_zerotier.md){target="_blank"} for details.

### NetBird

Comet integrates with NetBird, allowing you to remotely access it through NetBird virtual network. 

On Comet's console, navigate to **Apps Center** -> **NetBird**, enable it and bind your Comet to your NetBird account. 

Next, bind your controlling device to the same account. Then you will be able to remotely access your Comet by entering its **NetBird virtual IP** in a web browser on the controlling device, without installing GLKVM app.

See [here](../../faq/remote_access_via_netbird.md){target="_blank"} for details.
