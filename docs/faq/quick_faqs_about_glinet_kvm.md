# Quick FAQs about GL.iNet KVM

This is a brief Q&A collection for GL.iNet KVM, designed to provide quick answers to some common basic questions.

## Basic Information

**Q1. What devices can GL.iNet KVM control?**

A1. GL.iNet KVM can be used to control any device that uses HDMI output and USB input, such as laptops, desktops, Raspberry Pi, mini hosts, etc.

---

**Q2. Do I need to install any software to use GL.iNet KVM?**

A2. No software is required to be installed on the controlled device, and it can be Windows, macOS, ChromeOS, Linux, etc.

As to the controlling device, whether a software needs to be installed on it depends on the way you want to access the KVM.

??? "Local Access"

    If you want to access KVM over the same local area network (LAN), no software needs to be installed on the controlling device.

    Simply open a browser on the controlling device, enter either the KVM's IP address or `glkvm.local` in the address bar to access KVM locally.
    
    Click [here](local_access_via_browser.md){target="_blank"} for details.
    
??? "Remote Access"

    - **GLKVM App**
    
        If your controlling device runs Windows, macOS, Android, or iOS, you can install the [GLKVM app](https://www.gl-inet.com/app-rm/){target="_blank"} on it and access your KVM remotely, thus accessing the controlled device.
        
        Click [here](remote_access_via_glkvm_app.md){target="_blank"} for details.
        
    - **Cloud Service**
    
        This method is ideal for those who cannot or do not want to install the GLKVM app.

        Bind your KVM to the Cloud service, then you can access your KVM remotely by typing `glkvm.com` into a web browser on your controlling device, thus accessing the controlled device, without installing the GLKVM app.

        Click [here](remote_access_via_cloud.md){target="_blank"} for details.
    
    - **Tailscale**
    
        This method is suitable for those who cannot or do not want to use the GLKVM app or Cloud service, though it involves more steps.

        Bind your KVM and controlling device to the same Tailscale account, then you can access your KVM remotely by typing the KVM's Tailscale virtual IP into a web browser on your controlling device, thus accessing the controlled device.
    
        Click [here](remote_access_via_tailscale.md){target="_blank"} for details.

    - **ZeroTier**
    
        This method is suitable for those who cannot or do not want to use the GLKVM app or Cloud service, though it involves more steps.

        Join your KVM and controlling device into the same ZeroTier network, then you can access your KVM remotely by typing the KVM's ZeroTier IP into a web browser on your controlling device, thus accessing the controlled device.
    
        Click [here](remote_access_via_zerotier.md){target="_blank"} for details.

    - **NetBird**

        This method is suitable for those who cannot or do not want to use the GLKVM app or Cloud service, though it involves more steps.

        [NetBird](https://netbird.io/){target="_blank"} is an open-source zero trust networking platform that lets you build secure private networks for home and business use. As a WireGuard®-based overlay network, NetBird enables secure access to your devices anytime and anywhere.
        
        GL.iNet KVM integrates NetBird, allowing you to bind it to the NetBird virtual network for remote access. 

        Click [here](remote_access_via_netbird.md){target="_blank"} for details.

---

**Q3. How do I access GL.iNet KVM?**

A3. You can access GL.iNet KVM either locally or remotely via six different methods:

- [Local access via web browser](local_access_via_browser.md){target="_blank"}
- [Remote access via Cloud service](remote_access_via_cloud.md){target="_blank"}
- [Remote access via GLKVM app](remote_access_via_glkvm_app.md){target="_blank"}
- [Remote access via Tailscale](remote_access_via_tailscale.md){target="_blank"}
- [Remote access via ZeroTier](remote_access_via_zerotier.md){target="_blank"}
- [Remote access via NetBird](remote_access_via_netbird.md){target="_blank"}

---

**Q4. Do I need to open ports (exposed to WAN) for GL.iNet KVM to achieve remote access?**

A4. No. No open ports or even a public IP is needed.

---

**Q5. Does GLKVM app support ChromeOS/Linux?**

A5. No. Currently the GLKVM app does not support installation on Chrome or Linux OS. 

If your controlling device runs Chrome/Linux OS, the GLKVM app cannot be installed, thus remote access to controlled device via GLKVM app is not supported.

However, you can use <u> Cloud Service</u>, <u>Tailscale</u>, <u>ZeroTier</u>, or <u>NetBird</u> to achieve remote access. See Q3 above for details.

Alternatively, you can access the KVM locally via a web browser. See Q3 above for details.

---

**Q7. Can Comet (GL-RM1) connect to wireless network?**

A7. No. Comet (GL-RM1) does not support wireless network connection.

It needs to be connected to a network device (e.g., a router) via an Ethernet cable for Internet access.

If you prefer a KVM that supports Wi-Fi, you may consider [Comet Pro (GL-RM10)](https://www.gl-inet.com/products/gl-rm10/){target="_blank"} or [Comet 5G (GL-RM10RC)](https://www.gl-inet.com/products/gl-rm10rc/){target="_blank"}.

---

## Power Control

**Q1. Can GL.iNet KVM control a computer's power on and off?**

A1. Yes. You can control the target device's power on and off remotely via the methods below:

- Wake-on-LAN (Built-in software service)

- [ATX board](../user_guide/gl-atx-board/index.md){target="_blank"} (Accessories, additional purchase required)

- [FingerBot](../user_guide/gl-fgb-01/index.md){target="_blank"} (Accessories, additional purchase required)

---

**Q2. How to use ATX Board for remote power control?**

A2. Please refer to [ATX Board User Guide](../user_guide/gl-atx-board/index.md){target="_blank"}.

---

## Features

> Below are FAQs for a few features. See the corresponding [user guide](../user_guide/index.md) for complete details.

**Q1. Do I have to use KVM Cloud Service?**

A1. No. The Cloud Service is optional. 

If you don't rely on the cloud for remote access, you can use third-party overlay networking tools, such as Tailscale, ZeroTier and NetBird.

---

**Q2. Can I use GL.iNet KVM to control multiple devices?**

A2. No. GL.iNet KVM can only control one device. 

To control multiple devices, you can either purchase multiple GL.iNet KVM devices and bind them to the same GL.iNet account, or purchase a third-party KVM switch with Hotkey Switching and use it in conjunction with GL.iNet KVM. Note: Compatibility issues may arise.

---

**Q3. What is Wake-on-Lan?**

A3. Wake-on-LAN (WOL) is a technology that allows a computer or device to be remotely powered on or awakened from a low-power state over a network. It works by sending a "magic packet" containing the target device's MAC address, which triggers the device to start up. Common uses include remote administration, energy-saving standby configurations, and centralized system management.

---

**Q4. Does GL.iNet KVM support Mouse Jiggle?**

A4. Yes. You can enable Mouse Jiggle on the KVM console.

The Mouse Jiggler feature simulates subtle, periodic mouse movements to prevent the computer (i.e., the controlled device) from going to sleep due to prolonged inactivity, such as during remote meetings and server management.

---

**Q5. Does GL.iNet KVM support two-way audio?**

A5. Yes. You can enable Speaker and Microphone on the KVM console to achieve two-way audio transmission.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.