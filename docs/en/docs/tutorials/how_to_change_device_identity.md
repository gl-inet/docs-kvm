# How to change KVM device identity

## What is KVM device identity

GL.iNet KVM's device identity refers to the identifier that enables the KVM to be recognized and distinguished by the connected device during communication. 

Typically, the KVM is equipped with a Type-C port, as shown below, which connects to the controlled device's USB port to simulate peripheral devices (e.g., keyboard, mouse, USB drive, microphone) and CD-ROM. 

![gl-rm1 type-c](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

When you click the mouse, type on the keyboard, or use the microphone on the controlling end, these signals are remotely transmitted to the physical KVM device. The KVM then forwards them to the controlled device through its Type-C port.

Therefore, the KVM is usually regarded as a composite device, emulating several peripheral devices connected to the controlled device's USB ports.

![device identity principle](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/principle.png){class="glboxshadow"}

!!! Note

    If the input method/keyboard of the controlling device is not consistent with that of the controlled device, some symbols/letters may have different positions on the keyboard, which can cause the output of the controlled end to be inconsistent with the input of the controlling end. Click [here](../faq/keyboard_does_not_input_output_as_expected.md) for details.

## Why change device identity

Since GL.iNet KVM works as a combined emulator of several devices for user interaction, when connected to the controlled device, it is recognized as a set of multiple devices, including a monitor, several USB devices such as mouse and keyboard, and USB drive. 

By default, the device identity is **GLKVM**, thus it will be displayed as GLKVM or Glinet Composite Device in the system settings of the controlled device. This usually does not cause inconvenience, as these settings are only visible to users themselves.

![device identity default](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}
<small>(Bluetooth & devices settings)</small>

![speaker settings](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(Speaker settings)</small>

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

## Limitations of Device Identity Customization

!!! Warning "Behavioral Detection Software May Still Identify KVM"

    Regardless of how you customize the USB device identity, the USB **structure** of the virtualized devices (keyboard, mouse, microphone, camera, etc.) may still appear suspicious to behavioral detection software.

    The fundamental issue is that all these virtualized peripherals belong to a **single composite USB device**. While a composite device containing only a keyboard and mouse is relatively common — many wireless keyboard/mouse receivers (such as Logitech Unifying) present a similar structure — a single composite USB device that simultaneously includes **keyboard, mouse, and microphone** is extremely rare in practice. 

    Therefore, changing the device identity alone **may not be sufficient** to evade detection by advanced monitoring or behavioral analysis software.

## How to change device identity

### Firmware v1.10 and above

1. Log in to your KVM and navigate to **Settings** in the upper-right. In the **USB Devices**, find the **Device Identity** and customize it.

    ![identity customize1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize1.png){class="glboxshadow"}

2. In the pop-up window, click **Confirm** to restart.

    ![identity customize2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize2.png){class="glboxshadow"}

3. After restarting, the Device Identity is changed on the KVM console.

    ![identity customize3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize3.png){class="glboxshadow"}

4. Verify device identity.

    Access your controlled device through KVM, and navigate to **Settings** -> **Bluetooth & devices** (taking Windows 11 Pro as an example). The input device has been recognized as the custom devices you set, instead of the default GLKVM.

    ![identity customize4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize4.png){class="glboxshadow"}

### Firmware v1.9 and earlier

1. Log in to your KVM, and navigate to **Settings** -> **System** -> **Device Identity**. Select a preset identity from the drop-down list.

    ![identity customize1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    Or click on **Customize** and fill in the parameters you want in the pop-up window.

    ![identity customize2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. In the pop-up window, click **Confirm** to restart.

    ![identity customize3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. After restarting, the Device Identity is changed on the KVM console.

    ![identity customize4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

4. Verify device identity.

    Access your controlled device through KVM, and navigate to **Settings** -> **Bluetooth & devices** (taking Windows 10 Pro as an example). The input devices (keyboard and mouse), audio device (microphone), and display (monitor) will be recognized as the custom devices you set, instead of the default GLKVM.

    ![identity customize5](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.