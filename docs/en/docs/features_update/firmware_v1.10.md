# Firmware v1.10

This release introduces native WebRTC, real-time data monitoring, centralized USB devices management, and a new Settings Center. It also improves startup performance, security, and microphone stability for a smoother and more reliable remote KVM experience.

Get the latest firmware from the [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"}

## WebRTC (Native) Mode
This firmware introduces **WebRTC (Native) Mode**. It uses the Google WebRTC Library to improve streaming performance and provide a smoother real-time remote control experience.

![webrtc mode](https://static.gl-inet.com/docs/kvm/features_update/1.10/webrtc_native_mode.png){class="glboxshadow" width=400}

## Connection Stats

**Connection Stats** displays real-time connection information and trend charts, including network latency, jitter, packet loss rate, bitrate, frame rate, and playback delay.

- Click the list icon to view real-time connection data and device status.

    ![Connection Stats 1](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_1.png){class="glboxshadow"}

- Click the chart icon to view trend charts for network latency, jitter, and packet loss rate.

    ![Connection Stats 2](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_2.png){class="glboxshadow"}

## Settings Center

This release adds a new **Settings Center** that centralizes USB device, preference, network, security, cloud, and system settings. Existing options, such as hostname configuration, cloud management, and firmware upgrades, are now easier to access in one place.

### USB Devices

The **USB Devices** provides centralized management for USB emulation devices. From this page, you can enable or disable virtual peripherals to improve compatibility with the controlled host.

![usb devices](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_usb_devices.png){class="glboxshadow"}

- **USB Emulated Devices**: Enable or disable USB emulated devices, including the mouse, keyboard, microphone, camera, and virtual media. Some devices cannot be enabled at the same time. Availability is updated automatically.

- **Device Identity**: Customize or modify the KVM's identity recognized by the controlled device. Note that EDID and device identification remain synchronized. Changing either one will automatically update the other to ensure correct device recognition.

### Preferences

The **Preferences** let you manage layout preferences, system settings, and device screen settings.

![preferences](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences**: Configure the toolbar in fullscreen mode and the status bar in windowed mode.

- **System Settings**: Set the browser tab title, UI language, color mode, and timezone.

- **Device Screen**: Preview and configure the built-in device screen, including lock screen mode, time format, date format, and wallpaper. 

    **Note**: This feature is available only on models with a built-in display.

### Network

You can view and manage device network settings, including the hostname, Ethernet connection, and wireless network information.

![network](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_network.png){class="glboxshadow"}

- **Hostname**: Change the device hostname directly from the console. This feature was introduced in firmware v1.7.0.

- **Ethernet Settings**: View and configure the Ethernet connection. You can use DHCP to obtain network settings automatically, or select **Static** to manually enter the IP address, netmask, gateway, and other required parameters.

- **Wireless**: IP address, gateway, and MAC address are displayed once the device joins a Wi‑Fi network. 

    **Note**: The Wireless feature is available only on supported models.

### Security

The **Security** lets you change the administrator password, enable two-factor authentication, and customize the TLS certificate.

![security](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_security.png){class="glboxshadow"}

- **Access Password**: Manage the admin password or enable two-factor authentication (2FA) to secure device access.

- **TLS Certificate**: Use the default certificate or upload a custom certificate and private key for browser access.

### Cloud

Devices can be bound to cloud services via URL or code for remote access and management. You can also download the mobile app, manage the connection, or unbind the device as needed.

![cloud](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_cloud.png){class="glboxshadow"}

### System

In **System**, you can access system management, firmware upgrade, and support options.

![system](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_system.png){class="glboxshadow"} 

- **System**: Reboot the device or reset it to its factory settings.

- **Upgrade**: Enable Beta Center to receive beta firmware updates, or use **Local Upgrade** to install firmware from a local file.

- **Help & Support**: Export device logs for troubleshooting and access user guides, FAQs, and other support documents.

## Other Enhancements

- **Startup Performance**: Improved device startup speed.

- **Password Policy**: Strengthened password policy (minimum 10 characters with at least two character types) to enhance security.

- **Caps Lock Indicator**: Added a Caps Lock status indicator for the controlled device.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.