# How to remotely access the controlled device via Cloud service?

Before you begin, please ensure the following:

- The controlled device is connected to the KVM correctly.
    
- The KVM is connected to a stable network.

- You can access the KVM locally, as binding device to the Cloud needs to be done within the local network.

Follow the steps below to remotely access your KVM and the controlled device via Cloud service.

## 1. Bind your device to KVM Cloud

There are two ways to bind your KVM to the Cloud: Regular Binding or Dynamic Code Binding.

- **Regular Binding**: Click "Bind To KVMCloud" on the KVM console, then you will be redirected to the binding page with the token. Log in to your cloud account, and confirm the device information to complete the binding.

- **Dynamic Code Binding**: Click "Bind With Code" on the KVM console, then it will generate an 8-digit dynamic code randomly for device binding. Log in to your cloud account, and enter the code to complete the binding.

### Regular Binding

Log in to your KVM locally via IP address or domain, and navigate to **Cloud Service** in the upper right corner. Click **Bind To Cloud**.

![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

You will be re-directed to a login page. Input your glinet account and click **Log In**.

![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

Confirm your device info, and click **Bind**.

![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

Wait a second and your device will be bound to your account successfully. Click **Done**.

![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

### Dynamic Code Binding

Note: Please upgrade your KVM firmware to version 1.7 before using this feature.

1. Log in to your GL.iNet KVM locally using domain or IP address. Click [here](../faq/local_access_to_controlled_device_via_browser.md) for details. 

2. After login, navigate to **Cloud Service** in the upper-right corner, and click **Bind With Code**.

    ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. It will generate an 8-digit dynamic code randomly for device binding, valid for 60 seconds. Click the code to copy it.

    ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. Visit [https://glkvm.com/](https://glkvm.com/){target="_blank"} and log in with your glinet cloud account. 

    ![bind with code 3](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. After logging in, the page displays as follows.

    ![bind with code 4](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    Click **Add Device** and select **Bind with Code**.

    ![bind with code 5](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. In the pop-up window, enter the 8-digit dynamic code, and click **Bind**.

    ![bind with code 6](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Note**: The dynamic code is valid within 60 seconds. If the dynamic code expires, go back to the KVM console and click **Regenerate Code** to get a new one.

    ![regenerate code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

    The device will then be successfully bound to your cloud account.

## 2. Remote access via Cloud service

Open a browser (take Google Chrome as an example), and enter `glkvm.com` in the address bar. You will see a login page. Use your glinet account to log in.

![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

After login, you will see the devices bound to your account. Click on the device you want to remotely access.

![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

It will redirect to a new webpage with the domain `glkvm.xyz`, `glkvm.site`, or `glkvm.top`. These domains are secure and provided by GL.iNet.
    
Enter the admin password and log in.

![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

Then you will be able to access the KVM and the controlled device remotely via Cloud, without installing the app.

![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.