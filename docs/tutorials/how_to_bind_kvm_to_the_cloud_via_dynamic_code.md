# How to bind KVM to the cloud via dynamic code?

This tutorial will introduce how to easily bind GL.iNet KVM to the cloud through dynamic code.

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

    **Note**: The dynamic code is valid within 60 seconds. If the dynamic code expires, go back to the KVM admin panel, and click **Regenerate Code** to get a new one.

    ![regenerate code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

7. The device will be successfully bound to your cloud account. Click **Done**.

    ![bind with code 7](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_7.png){class="glboxshadow"}

    You will see the KVM in the device list. Now you can access it remotely via Cloud Service.

    ![bind with code 8](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_8.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.