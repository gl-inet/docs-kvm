# Frequently Asked Questions about GL.iNet KVM

This document compiles commonly asked questions and answers about GL.iNet KVM (Remote Keyboard Video Mouse), designed to help you resolve issues quickly and use the device efficiently. 

If your question is not listed here, please contact our technical support team for further assistance.

## Basic Information

**Q1. What devices can GL.iNet KVM control?**

A1. GL.iNet KVM can be used to control any device that uses HDMI output and USB input, such as laptops, desktops, Raspberry Pi, mini hosts, etc.

---

**Q2. Do I need to install any software to use KVM?**

A2. No software is required to be installed on the controlled device. 

As to the controlling device, whether software needs to be installed on it depends on the way you want to access the controlled device.

- Local Access

    If you want to access the controlled device in the local area network (LAN), you can directly launch a browser on the controlling PC, enter `glkvm.local` in the address bar to access the glkvm local management page. No need to install any sofeware on the controlling device.
    
- Remote Access

    If your controlling device is Windows or macOS, you can install the [GLKVM application](https://www.gl-inet.com/app-rm/){target="_blank"} on it to remotely access GL.iNet KVM and the controlled device. 

    Alternatively, if you cannot or don't want to install GLKVM application, you may use **Tailscale** to achieve remote access, which is integrated in Comet (GL-RM1). In this way, simply type Comet's Tailscale virtual IP into a browser, you can directly access Comet and the controlled device without installing GLKVM app.

---

**Q3. How do I access the GL.iNet KVM and the controlled device connected to it?**

A3. Take GL-RM1 (Comet) as an example. There are three ways to access the GL-RM1 and the controlled device: 

- Local access via Web browser
- Remote access via GLKVM application
- Remote access via Tailscale

Click [here](how_to_access_the_controlled_device_connected_to_kvm.md) for more details.

---

**Q4. Do I need to open ports (exposed to WAN) for GL.iNet KVM to achieve remote access?**

A4. No. No open ports or even a public IP is needed.

---

**Q5. Does GLKVM application support ChromeOS/Linux?**

A5. No. Currently the GLKVM app does not support installation on Chrome or Linux OS. 

If your controlling device is running Chrome/Linux OS, the GLKVM app cannot be installed, thus remote access to controlled device via GLKVM app is not supported.

However, you may use **Tailscale** to achieve remote access, which is integrated in Comet (GL-RM1). In this way, you can directly access Comet by typing its Tailscale virtual IP into a browser, without installing GLKVM app.

Alternatively, you can locally access the controlled device through a web browser in the local LAN network.

As to the remotely-controlled device, no need to install any software on it. That is to say, it can be Windows, macOS, ChromeOS, Linux, etc.

---

**Q7. Can GL-RM1 (Comet) connect to wireless network?**

A7. GL-RM1 (Comet) does not support connecting to wireless network.

You need to connect it to a network device (such as a router) via an Ethernet cable to get Internet access.

---

## Power On/Off Control

**Q1. Can GL.iNet KVM control the power on/off of a computer?**

A1. Sure. You can control the power of the controlled devices in the following ways:

- Wake on LAN (Built-in software service)

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

**Q2. What do I need for centralized device management?**

A2. You could get multiple Comet and bind them to one account on GLKVM, or get a KVM switch with hotkeys yourself.

---

**Q3. What is Wake On Lan?**

A3. Wake on LAN (WOL) is a technology that allows a computer or device to be remotely powered on or awakened from a low-power state over a network. It works by sending a "magic packet" containing the target device's MAC address, which triggers the device to start up. Common uses include remote administration, energy-saving standby configurations, and centralized system management.

---

**Q4. Does Comet support Mouse Jitter?**

A4. Yes. Comet supports mouse jitter function from firmware v1.3.

The mouse jitter function is applied to prevent the computer from entering sleep due to prolonged inactivity (e.g., remote meetings, server management), assist in game idle status (when users leave the keyboard temporarily) to avoid being detected as offline by the system, and simulate user operations in software automated testing to ensure stable program operation.

---

**Q5. Does Comet support remote microphone (i.e., transmitting audio from the controlling device to the controlled device)?**

A5. This feature will be available from firmware v1.4.0.

---

## Troubleshooting

**Q1. Why can't I control the mouse and keyboard?**

A1. Please refer to [this link](cannot_control_the_mouse.md).

---

**Q2. Why does the mouse cursor fail to overlap with that on the controlled device?**

A2. It usually happens when the controlled device is a laptop.

You can modify the resolution of the controlled device to the appropriate parameters (recommended), or modify the EDID of the KVM to adjust it.

Click [here](mouse_cursors_fail_to_overlap_when_using_glkvm.md) for more instructions.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.