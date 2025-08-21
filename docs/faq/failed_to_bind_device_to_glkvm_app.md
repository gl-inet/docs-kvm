# What should I do if I failed to bind device to the GLKVM app?

The [GLKVM app](https://www.gl-inet.com/app-rm/){target="_blank"} allows you to remotely access your controlled device from a host device. Simply install the app on your host device and bind your GL.iNet KVM device to it.

However, binding failures may occur during this process.

Click on the error message below to view the corresponding solution.

??? "Binding failed, unable to obtain basic KVM device information."

    1. Check the LED state. Ensure the LED is solid white and your KVM device is connected to Internet.
    2. Restart your KVM device, wait for 2 minutes and try to bind it again.
    3. Follow the steps below to check the network by Ping command.
       
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

    1. Check the LED state. Ensure the LED is solid white and your KVM device is connected to Internet.
    2. Restart your KVM device, wait for 2 minutes and try to bind it again.
    3. Follow the steps below to check the network by Ping command.
       
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

        The Cloud service is enabled by default, but if you disable it manually via web browser, device re-binding to the GLKVM app will fail. Please access your KVM device locally via web browser to re-enable the Cloud service.

??? "Binding failed, KVM is already bind by others."

    The KVM device has been bound to another email. Please check if you have bound it to your another email address.

??? "Other"

    Check if VPN is enabled on your controlling device, on which the GLKVM app is installed. 
    
    Disable any VPN or proxy software, including AstroWarp, Tailscale and ZeroTier, then try to bind your KVM to the GLKVM app again.

If problem persists, please contact us at [support@gl-inet.com](mailto:support@gl-inet.com) and provide Device Model, Firmware version and MAC address.
