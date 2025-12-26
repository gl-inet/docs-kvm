# How to remotely access the controlled device via GLKVM app?

Before you begin, please ensure the controlled device has been connected to the GL.iNet KVM correctly, and the KVM is connected to Internet stably.

Follow the steps below to remotely access the controlled device via GLKVM app.

## 1. Install GLKVM app

Install the [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} on your controlling device. It supports Windows and macOS.

## 2. Log in account

Open the GLKVM app and log in with your GL.iNet account. 

![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

If you don't have a GL.iNet account, sign up for one and then log in.
    
![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

## 3. Bind devices

After login, the page will display as follows. Click **Add Device**.

There are three ways to bind your device: Auto Discover, S/N Code, and Dynamic Binding Code.

![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

### Auto Discover

This needs to be done within the local network. Please ensure that your KVM and the controlling device are on the same LAN.

1. Click **Auto Discover**. It will start searching automatically.

    ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

2. Locate your KVM and enter its Device ID to bind it to your account.

    ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

### S/N Code

This applies to the scenario where your KVM is not detected, or is not on the same LAN, but you have its serial number (S/N).

1. Click **S/N Code**. 

2. In the pop-up window, customize the device name and enter the S/N, which is printed on the label bottom of your KVM device.

    ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

### Dynamic Binding Code

Please upgrade your KVM firmware to version 1.7 before using this feature.

This needs to be done within the local network. Please ensure that your KVM and the controlling device are on the same LAN.

1. Log in to your KVM locally using domain or IP address. Click [here](../faq/local_access_to_controlled_device_via_browser.md) for details. 

2. Navigate to **Cloud Service** in the upper-right corner, and click **Bind With Code**. 

    ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. It will generate an 8-digit dynamic code randomly for device binding, valid for 60 seconds. Click the code to copy it.

    ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Back to the GLKVM app, enter the dynamic binding code and click **Bind**.

    ![dynamic code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

## 4. Remote access

Once your KVM device is bound to your account, it will show "Online" in the app.

![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

Click your KVM device. It will open a new window and start connecting.

![connecting](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

Once connected, enter the admin password to log in to your device.

![connected log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

You will then access your KVM device, through which you can access the controlled device.

![connected access](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
