# What should I do if I failed to bind device to the GLKVM app?

The [GLKVM app](https://www.gl-inet.com/app-rm/){target="_blank"} enables remote access to your controlled device from the controller device. Simply install the app on your controller device and bind your GL.iNet KVM device to it, and you can access the controlled device remotely anytime, anywhere.

However, device binding might fail due to various reasons.

Click the error message below for corresponding solutions.

??? "Binding failed, unable to obtain basic KVM device information."

    ![binding failed device info error](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_device_info_error.png){class="glboxshadow"}

    1. Check the LED state. Ensure the LED is solid white and your KVM device is connected to Internet.
    2. Restart your KVM device, wait for 2 minutes and try to bind it again.
    3. If you add device by S/N code, make sure you enter the correct S/N.
    4. Follow the steps below to check the network by **Ping** command.
       
        1. Connect your controlling device to the same network as your KVM.

        2. Launch a browser (Chrome or Edge is recommended) on the controlling device, and enter `glkvm.local` in the address bar. Enter the admin password to log in.

            ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. After login, navigate to **Toolbox** -> **Terminal**, click on **Access** to log in to the terminal.

            ![access terminal](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Ping `google.com` to check the network status.
        
            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            If the network is working fine, you will get the result as shown below.

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}
            
            If the network is unstable or unavailable, please contact your ISP or router support.

??? "Device network error, binding failed."

    ![binding failed network error](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_network_error.png){class="glboxshadow"}

    1. Check the LED state. Ensure the LED is solid white and your KVM device is connected to Internet.
    2. Restart your KVM device, wait for 2 minutes and try to bind it again.
    3. Follow the steps below to check the network by **Ping** command.
       
        1. Connect your controlling device to the same network as your KVM.

        2. Launch a browser (Chrome or Edge is recommended) on the controlling device, and enter `glkvm.local` in the address bar. Enter the admin password to log in.

            ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. After login, navigate to **Toolbox** -> **Terminal**, click on **Access** to log in to the terminal.

            ![access terminal](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. Ping `google.com` to check the network status.
        
            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            If the network is working fine, you will get the result as shown below.

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            If the network is unstable or unavailable, please contact your ISP or router support.

    4. Ensure the Cloud service is enabled. 

        The Cloud service is enabled by default, but if you has disabled it manually before, device re-binding to the GLKVM app will fail. Please access your KVM device locally via domain or IP address to re-enable the Cloud service.

??? "Binding failed, KVM is already bound by others."

    ![binding failed bound by others](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_bound_by_others.png){class="glboxshadow"}

    This means the KVM device has been bound to another account.
    
    1. Check if you have bound it to your another email address. Try other accounts if any.
    
    2. If you add device by S/N code, make sure you enter the correct S/N.

??? "Incorrect Dynamic Binding Code. You have 4 attempts remaining."

    ![incorrect binding code](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_binding_code.png){class="glboxshadow"}

    This means you entered an invalid or expired binding code. 
    
    1. Log in to your KVM admin console locally, navigate to **Cloud Service** in the upper right corner and click **Bind with Code** to get a dynamic binding code. 
    
    2. If it expires, click **Regenerate** to get a new one.

??? "Incorrect Device ID. You have 4 attempts remaining."

    ![incorrect device id](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_device_id.png){class="glboxshadow"}

    This means you entered the wrong Device ID. 
    
    1. Check the bottom label for the correct Device ID.
    
    2. If you cannot check the bottom label, try binding your device via local access. 
    
        Log in to your KVM admin console locally, navigate to **Cloud Service** in the upper right corner and click **Bind To KVM Cloud**. Then you will be redirected to the binding page with a unique token. Log in with your Cloud account, and confirm the device information to complete the binding.

??? "Other"

    Check if VPN is enabled on your controlling device, on which the GLKVM app is installed. 
    
    Disable any VPN or proxy software, including AstroWarp, Tailscale and ZeroTier, then try to bind your KVM to the GLKVM app again.

If problem persists, please contact us at [support@gl-inet.com](mailto:support@gl-inet.com) and provide Device Model, Firmware version and MAC address.
