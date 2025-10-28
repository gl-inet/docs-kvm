# How to change device identity?

## What is device identity

Device identity refers to the KVM's identity recognized by the controlled device. It can be found in the KVM's control panel -> **Settings** -> **System**. By default, the device identity is **GLKVM**.

![device identity control panel](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/device_identity.png){class="glboxshadow"}

Typically, the KVM is equipped with a Type-C port, as shown below, which connects to the controlled device's USB port to simulate keyboard and mouse signal. 

![gl-rm1 type-c](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

When the user clicks the mouse or types on the keyboard on the KVM control panel (i.e. remote control end), the keyboard and mouse signals will be remotely transmitted to the physical KVM device, and then the KVM will map the input to the controlled device through its Type-C port based on the corresponding key positions. 

!!! Note

    If the input method/keyboard of the controlling device is not consistent with that of the controlled device, some symbols/letters may have different positions on the keyboard, which can cause the output of the controlled end to be inconsistent with the input of the controlling end. Click [here](../faq/keyboard_does_not_input_output_as_expected.md) for details.

Therefore, the KVM is usually regarded as a peripheral device connected to the controlled device's USB port, such as a keyboard. 

Since the device identity of GL.iNet KVM is GLKVM by default, it is displayed as GLKVM or similar identifier in the system settings of the controlled device (such as Bluetooth & devices).

![device identity default](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}

## Why change device identity

By default, GL.iNet KVM is recognized by the controlled devices as peripheral devices, such as a keyboard, microphone, or monitor. This usually does not cause inconvenience, as these settings are visible only by users themselves.

![mic settings](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/mic.png){class="glboxshadow"}
<small>(microphone settings)</small>

![speaker settings](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(speaker settings)</small>

However, when you need to remotely access a controlled device through KVM and participate in video conference on the controlled device, if you do the screen sharing, the audio, mouse, or monitor settings displayed on the controlled device may expose that you are using KVM for remote access. 

![screen sharing](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/screen_sharing.png){class="glboxshadow"}
<small>(screen sharing)</small>

Therefore, customizing the device identity of KVM can help prevent this from happening.

## How to change device identity

1. Log in to your KVM, and navigate to **Settings** -> **System** -> **Device Identity**. Select a preset identity from the drop-down list.

    ![customize1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    Or click on **Customize** and fill in the parameters you want in the pop-up window.

    ![customize2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. Once selected, there will be a pop-up window asking to restart. Click **Confirm** to restart.

    ![customize3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. After restarting, on the KVM control panel, the Device Identity has been changed to the modified one.

    ![customize4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

    Access your controlled device via KVM, and navigate to **Settings** -> **Bluetooth & devices** (taking Windows 10 Pro as an example). The input (keyboard), audio, and monitor are recognized as the devices you customized, which are no longer GLKVM. 

    ![customize5](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.