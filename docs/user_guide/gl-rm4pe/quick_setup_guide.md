# Comet X (GL-RM4PE) Quick Setup

## Connect Devices

For clarity, Device A refers to the controlling device, and Device B the controlled device.

![connect1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect1.png){class="glboxshadow"}

1. Connect the Comet X to a PoE switch using an Ethernet cable, or power it with a 5V/3A power adapter.

    ![connect2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect2.png){class="glboxshadow"}

    ***Note**: If using a power adapter for power supply, connect the Comet X to a network device (such as router) via an Ethernet cable for Internet access.*

2. Connect the Comet X's **HDMI IN** port to Device B using an HDMI cable. This enables video signal transmission.

    ![connect3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect3.png){class="glboxshadow"}

3. Connect the Comet X's **USB-C** port to Device B using a USB cable. This USB-C port must pair with the corresponding HDMI IN port for proper keyboard and mouse signal transmission.

    ![connect4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect4.png){class="glboxshadow"}

    !!! Warning
    
        Comet X's USB‑C data port is intended solely for keyboard and mouse signal transmission. Do not connect it to any Thunderbolt host via a USB‑C to USB‑C cable. Thunderbolt ports support bidirectional power delivery, and reverse current injection may permanently damage the KVM hardware.

4. (Optional) Connect the Comet X's **HDMI OUT** port to an external monitor to duplicate the display (video loopout). See [Local Control](#local-control) for details.

5. Connection complete. Now you can access the Comet X's console locally or remotely.

## Rack Mounting

Mount Comet X onto server rack rails as needed.

1. Use the included screws to attach the mounting brackets to Comet X.

    ![install1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install1.png){class="glboxshadow"}

2. Secure Comet X to the rack rails with rack screws. **Rack screws are not included**.

    ![install2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install2.png){class="glboxshadow"}

## Local Control

Control the device directly via physical cables, no network, IP address or domain name required.

Comet X features an HDMI OUT port and two extra USB ports, ideal for local troubleshooting, configuration and OS installation. Simply connect your monitor, mouse and keyboard for plug-and-play local hardware control.

1. Connect the **HDMI OUT** port on Comet X's rear panel to an external monitor to duplicate the display (video loopout).

    ![local control1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control1.png){class="glboxshadow"}

2. Connect a keyboard and mouse to Comet X's USB ports on the front panel.

    ![local control2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control2.png){class="glboxshadow"}

3. You can now control the connected device(s) with your local keyboard and mouse, while video signals are looped out to the local monitor.

## LAN Access

There are two ways to access Comet X on the local network: via domain name or IP address.

Before accessing, ensure your controlling device is on the same LAN as Comet X.

### Domain

1. Launch a browser on the controlling device. Chrome or Edge is recommended for better compatibility.

2. Enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain1.png){class="glboxshadow"}

    ***Note**: You will need to set up your admin password when accessing for the first time.*

3. You can then access the Comet X's console locally and gain access to the controlled device.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain2.png){class="glboxshadow"}

### IP address

1. Find Comet X's IP address on the touchscreen. In this example, the Comet X's IP address is `192.168.8.197`. 

2. Launch a browser and enter this IP in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip1.png){class="glboxshadow"}

    ***Note**: You will need to set up your admin password when accessing for the first time.*

3. You can then access the Comet X's console locally and gain access to the controlled device.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip2.png){class="glboxshadow"}

## Remote Access

There are multiple ways to access Comet X remotely: via Cloud service, GLKVM App, Tailscale, and ZeroTier.

### Cloud service

1. Bind your device to KVM Cloud. This needs to be done on the local network. 

    There are two ways to bind your KVM to the Cloud: Regular Binding or Dynamic Code Binding. Here we take Regular Binding as an example. If you prefer Dynamic Code Binding, click [here](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} for details.

    First, locally access your Comet X and navigate to **Cloud Service** in the upper right corner. Click **Bind To KVMCloud**.

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_to_cloud.png){class="glboxshadow"}

    You will be redirected to a login page. Log in with your glinet cloud account. 

    ![cloud bind device1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind1.png){class="glboxshadow"}

    Second, confirm your device info, and click **Bind**.

    ![cloud bind device2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind2.png){class="glboxshadow"}

    Wait a second. Your Comet X will be bound to your account. Click **Done**.

    ![cloud bind device success](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind_success.png){class="glboxshadow"}

2. Remote access via Cloud service.

    After clicking Done, you will be redirected to a site with domain `glkvm.com`, where you can see your device.

    ![cloud devices list](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_devices.png){class="glboxshadow"}

    ***Tip**: If you are not redirected, enter `glkvm.com` manually in the address bar and log in to your glinet account. After login, you will see your device bound to your account.*
    
    Click on the device you want to remotely access. 
    
    ![cloud access](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access.png){class="glboxshadow"}
    
    It will open a new webpage. Enter your admin password to log in.

    ![cloud access1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access1.png){class="glboxshadow"}
    
    You will then be able to access your Comet X and the controlled device remotely via Cloud.

    ![cloud access2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access2.png){class="glboxshadow"}

### GLKVM App

1. Install the [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} on your controlling device.

2. Log in with your GL.iNet account. 

    ![log in](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_login.jpg){class="glboxshadow"}

    If you don't have one, sign up first and log in.
    
    ![sign up](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_signup.png){class="glboxshadow"}

3. Bind your device.

    After login, the page will display as follows. Click **Add Device**.

    ![add device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_add_device.png){class="glboxshadow"}

    You can bind your device in three ways: Auto Discover, S/N Code, and Dynamic Binding Code.

    ??? "Auto Discover"
    
        This needs to be done on the local network. Ensure your controlling device is on the same LAN as Comet X, and have your KVM device ID ready.
    
        Click **Auto Discover**. It will start searching.
    
        ![auto discover 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover1.png){class="glboxshadow"}
        
        Find your KVM and enter its **Device ID** to bind it to your account.
    
        ![auto discover 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover2.png){class="glboxshadow"}

        ![auto discover 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover3.png){class="glboxshadow"}
    
    ??? "S/N Code"
    
        This applies to the scenario where your KVM is not detected, or is not on the same LAN, but you have its serial number (S/N).
        
        Click **S/N Code**. In the pop-up window, set a device name and enter the S/N, which is printed at the bottom of the KVM device.
    
        ![sn code](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/add_sncode.png){class="glboxshadow"}
    
    ??? "Dynamic Binding Code"
    
        This needs to be done on the local network. Ensure your controlling device is on the same LAN as Comet X.
    
        1. Log in to your KVM locally using domain or IP address. Click [here](#lan-access) for details. 
    
        2. Navigate to **Cloud Service** in the upper-right corner and click **Bind With Code**. 
    
            ![bind with code 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code1.png){class="glboxshadow"}
    
        3. It will generate an 8-digit dynamic code randomly for device binding, valid for 60 seconds. Click the code to copy it.
    
            ![bind with code 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code2.png){class="glboxshadow"}
    
        4. Back to the GLKVM app, enter the dynamic binding code and click **Bind**.
    
            ![dynamic code](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code3.png){class="glboxshadow"}

4. Remote access via GLKVM App.

    Once your KVM device is bound to your account, it will show "Online" in the app.

    ![app device online](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_devices.png){class="glboxshadow"}

    Click your KVM device. It will open a new window and start connecting.

    ![app connecting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_connecting.png){class="glboxshadow"}

    Once connected, enter your admin password to log in to your device.

    ![app access1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access1.png){class="glboxshadow"}

    You will then access your KVM device, through which you can access the controlled device.

    ![app access2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access2.png){class="glboxshadow"}

### Tailscale

Comet X integrates with Tailscale, allowing you to remotely access it through Tailscale virtual network.

On the console, navigate to **Apps Center** -> **Tailscale**, enable it and bind your Comet X to your Tailscale account. 

Next, bind your controlling device to the same account. You will then be able to remotely access your Comet X by entering its **Tailscale virtual IP** in a web browser on the controlling device, without installing GLKVM app.

See [here](../../faq/remote_access_via_tailscale.md){target="_blank"} for details.

### ZeroTier

Comet X integrates with ZeroTier, allowing you to remotely access it through ZeroTier virtual network.

On the console, navigate to **Apps Center** -> **ZeroTier** and enable it.

Next, join both Comet X and your controlling device to the same ZeroTier network (using a 16-character alphanumeric Network ID), then you can remotely access your Comet X by entering its **ZeroTier IP** in a web browser on the controlling device, without installing GLKVM app.

See [here](../../faq/remote_access_via_zerotier.md){target="_blank"} for details.
