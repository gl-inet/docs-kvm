# Comet Q (GL-RMQ1) Quick Setup

## Connect Devices

For clarity, Device A refers to the controlling device, and Device B the controlled device.

![connect 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect1.png){class="glboxshadow"}

1. Connect the Comet Q's Type-C cable to the Type-C port on Device B.

    ![connect 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect2.png){class="glboxshadow"}

2. If Device B is a touchscreen mobile device such as a smartphone or tablet, enable accessibility controls first. This allows Comet Q to operate the touchscreen.

    - iOS: **Settings** > **Accessibility** > **Touch** > Enable **AssistiveTouch**.

    - Android: Search for **Mouse** or **Accessibility** in Settings. Menu paths vary by device brand and model.

    ![connect 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect3.png){class="glboxshadow" width="600"}

3. Follow the on-screen instructions to complete the initial setup. See [here](../gl-rmq1/product_overview.md#touchscreen) for details.

    ![connect 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/quick_setup/connect4.png){class="glboxshadow"}

## Local Access

There are two ways to access Comet Q on the local network: via domain name or IP address.

Before accessing, ensure your controlling device is on the same LAN as Comet Q.

### Domain

1. Launch a browser on the controlling device. Chrome or Edge is recommended for better compatibility.

2. Enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Note**: You will need to set up your admin password when accessing for the first time.

3. You can then access the Comet Q's console locally and gain access to the controlled device.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### IP address

1. Connect Comet Q to a Wi-Fi network and find its IP address on the touchscreen. In this example, the Comet Q's IP address is `192.168.8.197`.

2. Launch a browser and enter this IP in the address bar. You will be directed to the GLKVM login page. Enter the admin password.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Note**: You will need to set up your admin password when accessing for the first time.

3. You can then access the Comet Q's console locally and gain access to the controlled device.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## Remote Access

There are multiple ways to access Comet Q remotely: via Cloud service, GLKVM App, Tailscale, and ZeroTier.

### Cloud service

1. Bind your device to KVM Cloud. This needs to be done on the local network. 

    There are two ways to bind your KVM to the Cloud: Regular Binding or Dynamic Code Binding. Here we take Regular Binding as an example. If you prefer Dynamic Code Binding, click [here](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} for details.

    First, locally access your Comet Q and navigate to **Cloud Service** in the upper right corner. Click **Bind To Cloud**.

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    You will be redirected to a login page. Log in with your glinet cloud account. 

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    Second, confirm your device info, and click **Bind**.

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    Wait a second and your Comet Q will be bound to your account successfully. Click **Done**.

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. Remote access via Cloud service.

    Open a browser (take Google Chrome as an example), and enter `glkvm.com` in the address bar. You will see a login page. Use your glinet account to log in.

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    After login, you will see the devices bound to your account. Click on the device you want to remotely access.

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    It will redirect to a new webpage with the domain `glkvm.xyz`, `glkvm.site`, or `glkvm.top`. These domains are secure and provided by GL.iNet.
    
    Enter the admin password and log in.

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    You will then be able to remotely access your Comet Q and the controlled device via Cloud, without installing the app.

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
    
        This needs to be done on the local network. Ensure your controlling device is on the same LAN as Comet Q.
    
        Click **Auto Discover**. It will start searching automatically.
    
        ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}
        
        Locate your KVM and enter its Device ID to bind it to your account.
    
        ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}
    
    ??? "S/N Code"
    
        This applies to the scenario where your KVM is not detected, or is not on the same LAN, but you have its serial number (S/N).
        
        Click **S/N Code**. In the pop-up window, customize the device name and enter the S/N, which is printed on the label bottom of your KVM device.
    
        ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}
    
    ??? "Dynamic Binding Code"
    
        This needs to be done on the local network. Ensure your controlling device is on the same LAN as Comet Q.
    
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

Comet Q integrates with Tailscale, allowing you to remotely access it through Tailscale virtual network.

On the console, navigate to **Apps Center** -> **Tailscale**, enable it and bind your Comet Q to your Tailscale account. 

Next, bind your controlling device to the same account. You will then be able to remotely access your Comet Q by entering its **Tailscale virtual IP** in a web browser on the controlling device, without installing GLKVM app.

See [here](../../faq/remote_access_via_tailscale.md){target="_blank"} for details.

### ZeroTier

Comet Q integrates with ZeroTier, allowing you to remotely access it through ZeroTier virtual network.

On the console, navigate to **Apps Center** -> **ZeroTier** and enable it.

Next, join both Comet Q and your controlling device to the same ZeroTier network (using a 16-character alphanumeric Network ID), then you can remotely access your Comet Q by entering its **ZeroTier IP** in a web browser on the controlling device, without installing GLKVM app.

See [here](../../faq/remote_access_via_zerotier.md){target="_blank"} for details.
