# Frequently Asked Questions about GL.iNet KVM

This document compiles commonly asked questions and answers about GL.iNet KVM (Remote Keyboard Video Mouse), designed to help you resolve issues quickly and use the device efficiently. 

If your question is not listed here, please contact our technical support team for further assistance.

## Basic Information

**Q1. What devices can GL.iNet KVM control?**

A1. GL.iNet KVM can be used to control any device that uses HDMI output and USB input, such as laptops, desktops, Raspberry Pi, mini hosts, etc.

---

**Q2. Do I need to install any software to use GL.iNet KVM?**

A2. No software is required to be installed on the controlled device, and it can be Windows, macOS, ChromeOS, Linux, etc.

As to the controlling device, whether a software needs to be installed on it depends on the way you want to access the controlled device.

??? "Local Access"

    If you want to access the controlled device in the same local area network (LAN), simply open a browser on the controlling device, enter `glkvm.local` or the KVM's IP in the address bar, and you can access the KVM locally, thus accessing the controlled device. No software needs to be installed on the controlling device.
    
    Click [here](local_access_to_controlled_device_via_browser.md){target="_blank"} for details.
    
??? "Remote Access"

    - **Cloud Service**
    
        This method is ideal for those who cannot or do not want to install the GLKVM app.

        Bind your KVM to your Cloud account, then you can remotely access your KVM by typing `glkvm.com` into a web browser on your controlling device, thus accessing the controlled device, without installing the GLKVM app.

        Click [here](remote_access_to_controlled_device_via_cloud.md){target="_blank"} for details.

    - **GLKVM App**
    
        If your controlling device runs Windows or macOS, you can install the [GLKVM app](https://www.gl-inet.com/app-rm/){target="_blank"} on it to remotely access your KVM, thus accessing the controlled device.
        
        Click [here](remote_access_to_controlled_device_via_glkvm_app.md){target="_blank"} for details.
    
    - **Tailscale**
    
        This method is also suitable for those who cannot or do not want to install the GLKVM app, but it requires more steps.

        Bind your KVM and controlling device to the same Tailscale account, then you can remotely access your KVM by typing the KVM's Tailscale virtual IP into a web browser on your controlling device, thus accessing the controlled device, without installing the GLKVM app.
    
        Click [here](remote_access_to_controlled_device_via_tailscale.md){target="_blank"} for details.

---

**Q3. How do I access the GL.iNet KVM and the controlled device?**

A3. There are four ways to access the GL.iNet KVM and the controlled device: 

- [Local access via web browser](local_access_to_controlled_device_via_browser.md){target="_blank"}
- [Remote access via Cloud service](remote_access_to_controlled_device_via_cloud.md){target="_blank"}
- [Remote access via GLKVM app](remote_access_to_controlled_device_via_glkvm_app.md){target="_blank"}
- [Remote access via Tailscale](remote_access_to_controlled_device_via_tailscale.md){target="_blank"}

---

**Q4. Do I need to open ports (exposed to WAN) for GL.iNet KVM to achieve remote access?**

A4. No. No open ports or even a public IP is needed.

---

**Q5. Does GLKVM app support ChromeOS/Linux?**

A5. No. Currently the GLKVM app does not support installation on Chrome or Linux OS. 

If your controlling device runs Chrome/Linux OS, the GLKVM app cannot be installed, thus remote access to controlled device via GLKVM app is not supported.

However, you can use <u> Cloud Service</u> or <u>Tailscale</u> to achieve remote access. Check the Q3 above for details.

Alternatively, you can locally access the controlled device via a web browser. Check the Q3 above for details.

As to the controlled device, no need to install any software on it. It can be Windows, macOS, ChromeOS, Linux, etc.

---

**Q7. Can Comet (GL-RM1) connect to wireless network?**

A7. Comet (GL-RM1) does not support wireless network connection.

It needs to be connected to a network device (e.g., a router) via an Ethernet cable for Internet access.

If you prefer to purchase a KVM that supports Wi-Fi, you may consider Comet Pro (GL-RM10), a remote KVM over Wi-Fi solution.

---

## Power Control

**Q1. Can GL.iNet KVM control the power on/off of a computer?**

A1. Sure. You can achieve remote power control for the controlled device in the following ways:

- Wake-on-LAN (Built-in software service)

- [ATX board](../user_guide/gl-atx-board/index.md){target="_blank"} (Accessories, additional purchase required)

- [FingerBot](../user_guide/gl-fgb-01/index.md){target="_blank"} (Accessories, additional purchase required)

---

**Q2. How to use ATX Board for remote power control?**

A2. Please refer to [GL-ATX Board User Guide](https://docs.gl-inet.com/kvm/en/user_guide/gl-atx-board/){target="_blank"}.

---

## Features

**Q1. Do I have to use KVM cloud service?**

A1. No. You can choose to use or not use cloud service.

---

**Q2. Can I use Comet to control multiple devices?**

A2. No. Comet and Comet PoE can only control one device. 

To control multiple devices, you can either purchase multiple Comets and bind them to the same GL.iNet account, or purchase a third-party KVM switch with Hotkey Switching and use it in conjunction with Comet/Comet PoE. Note: Compatibility issues may arise.

---

**Q3. What is Wake-on-Lan?**

A3. Wake-on-LAN (WOL) is a technology that allows a computer or device to be remotely powered on or awakened from a low-power state over a network. It works by sending a "magic packet" containing the target device's MAC address, which triggers the device to start up. Common uses include remote administration, energy-saving standby configurations, and centralized system management.

---

**Q4. Does Comet support Mouse Jiggle?**

A4. Yes. You can enable Mouse Jiggle on the KVM control panel.

It aims to prevent the computer from entering sleep due to prolonged inactivity (e.g., remote meetings, server management), assist in game idle status (when users leave the keyboard temporarily) to avoid being detected as offline by the system, and simulate user operations in software automated testing to ensure stable program operation.

---

**Q5. Does Comet support two-way audio?**

A5. Yes. You can enable Speaker and Microphone on the KVM control panel to achieve two-way audio transmission.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.