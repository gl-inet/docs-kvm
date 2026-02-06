# How to change KVM device identity?

## What is KVM device identity

GL.iNet KVM's device identity refers to the identifier that enables the KVM to be recognized and distinguished by the connected device during communication. 

Since GL.iNet KVM works as a combined emulator of several devices for user interaction, when connected to the controlled device, it is recognized as a set of multiple devices, including a monitor, several USB devices such as mouse and keyboard, and USB drive. 

By default, the device identity is **GLKVM**, which can be found on the KVM console (**Settings** -> **System**). 

![device identity](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/device_identity.png){class="glboxshadow"}

Typically, the KVM is equipped with a Type-C port, as shown below, which connects to the controlled device's USB port to simulate peripheral devices (e.g., keyboard, mouse, USB drive, microphone) and CD-ROM. 

![gl-rm1 type-c](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

When the user clicks the mouse, types on the keyboard, or uses the microphone on the controlling end, these signals are remotely transmitted to the physical KVM device. The KVM then forwards them to the controlled device through its Type-C port. Therefore, the KVM is usually regarded as a composite device, emulating several peripheral devices connected to the controlled device's USB ports.

!!! Note

    If the input method/keyboard of the controlling device is not consistent with that of the controlled device, some symbols/letters may have different positions on the keyboard, which can cause the output of the controlled end to be inconsistent with the input of the controlling end. Click [here](../faq/keyboard_does_not_input_output_as_expected.md) for details.

Since the device identity of GL.iNet KVM is GLKVM by default, it is displayed as GLKVM or Glinet Composite Device in the system settings of the controlled device (such as Bluetooth & devices).

![device identity default](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}

## Why change device identity

By default, GL.iNet KVM is recognized by the controlled device as a composite device, emulating peripherals such as a keyboard, mouse, microphone, and monitor. This usually does not cause inconvenience, as these settings are only visible to users themselves.

![mic settings](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/mic.png){class="glboxshadow"}
<small>(microphone settings)</small>

![speaker settings](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(speaker settings)</small>

However, users may need to change KVM's device identity in the following scenarios.

??? "Scenario 1: Avoiding alerts from monitoring software on office computer"

    When the controlled device is an office computer, it may have built-in or installed monitoring software. These tools may mark KVM remote access as abnormal activity, trigger alerts, and even report to IT systems. 
    
    Changing the KVM's device identity can help prevent such unnecessary notifications, while maintaining normal remote control functionality.

??? "Scenario 2: Hiding KVM remote usage during online meeting screen sharing"

    During online meetings that require screen sharing, the controlled device's system settings (e.g., Bluetooth & devices) may display the KVM's default identity. This may expose your KVM remote access usage to meeting participants, which could be undesirable for some users. 

    Changing the device identity ensures the KVM remains hidden in shared screens.

    ![screen sharing](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/screen_sharing.png){class="glboxshadow"}
    <small>(screen sharing)</small>

??? "Scenario 3: Resolving unresponsive mouse/keyboard control on the controlled device"

    If you fail to control the mouse and keyboard on the controlled device through KVM, try modifying the KVM's device identity to avoid compatibility issues, enabling smooth signal transmission between the KVM and the controlled device.

## How to change device identity

1. Log in to your KVM, and navigate to **Settings** -> **System** -> **Device Identity**. Select a preset identity from the drop-down list.

    ![customize1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    Or click on **Customize** and fill in the parameters you want in the pop-up window.

    ![customize2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. Once selected, there will be a pop-up window asking to restart. Click **Confirm** to restart.

    ![customize3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. After restarting, on the KVM console, the Device Identity has been changed to the modified one.

    ![customize4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

    Access your controlled device via KVM, and navigate to **Settings** -> **Bluetooth & devices** (taking Windows 10 Pro as an example). The input devices (keyboard and mouse), audio device (microphone), and display (monitor) will be recognized as the custom devices you set, instead of the default GLKVM.

    ![customize5](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.