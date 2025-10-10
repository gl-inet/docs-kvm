# How to remotely access the controlled device via GLKVM app?

Before you begin, please ensure the controlled device has been connected to the GL.iNet KVM correctly, and the KVM is connected to Internet stably.

Follow the steps below to remotely access the controlled device via GLKVM app.

## 1. Install GLKVM app

Install the [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} on your controlling device. It supports Windows and macOS.

## 2. Sign up and log in

Sign up for a GL.iNet account. If you already have one, skip this step.

![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/sign_up_account.png){class="glboxshadow"}

Log in to your account.
    
![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/log_in_account.png){class="glboxshadow"}

## 3. Bind your device

If your KVM and the controlling device are in the same local area network, click **Add Device**. It will start searching automatically.

![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow gl-90-desktop"}

If your KVM has not been detected or it is not in the same local network, click the **+** button in the upper right corner to add it manually.

![add manually](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_manually_1.png){class="glboxshadow gl-90-desktop"}

Customize the device name and input the S/N, which can be found on the bottom label of the KVM device.

![add manually](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_manually_2.png){class="glboxshadow"}

Binding device. Please ensure a stable network connection.

![binding](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/binding.png){class="glboxshadow gl-90-desktop"}
    
Binding successful. Your KVM device has been bound to your account. Click **Done**.

![binding successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/binding_successful.png){class="glboxshadow gl-90-desktop"}

You will be directed to the homepage, where your KVM device will be displayed Online.

![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow gl-90-desktop"}

## 4. Remote access

Click your KVM device.

![remote control](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/remote_control.png){class="glboxshadow gl-90-desktop"}

It will open a new window and display a connection progress bar.

![connecting to remote device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting_to_remote_device.png){class="glboxshadow gl-90-desktop"}

Once connected, enter the admin password to log in to your device.

![enter admin password to log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/log_in_device.png){class="glboxshadow gl-90-desktop"}

You will be logged in to the control panel of your KVM device. Now you can access the controlled device through KVM.

![remote control panel](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/remote_access_via_app.jpg){class="glboxshadow gl-90-desktop"}

??? "Troubleshooting: Connection failed when remote access via GLKVM app"

    When accessing remotely through the GLKVM app, sometimes you may encounter a problem where the KVM device displays Online in the GLKVM app, but when clicked, it shows "Connection Failed".

    ![device online](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/device_online.jpg){class="glboxshadow gl-90-desktop"}

    ![connecting](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connecting.jpg){class="glboxshadow gl-90-desktop"}

    ![connection failed](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connection_failed.jpg){class="glboxshadow gl-90-desktop"}

    Here are some troubleshooting tips:

    1. Make sure the KVM is connected to the Internet. A solid-white LED indicates normal network connectivity.

    2. Check if the controlling device (where the GLKVM app is installed) has VPN or proxy enabled. Disable the VPN and proxy, then re-open the GLKVM app and reconnect to your device.

    3. Check whether the local firewall of the controlling device blocks the GLKVM app's access to the Internet, or intercepts GL.iNet-related domains' traffic (such as goodcloud.xyz, gl-inet.net, astrowarp.net, etc.). Disable the local firewall or add GL.iNet-related domains into the firewall allowlist, then try again.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
