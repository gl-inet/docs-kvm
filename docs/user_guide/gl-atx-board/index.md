# ATX Board (GL-ATXPC) User Guide

The ATX board is an optional accessory for GL.iNet KVM device. As a smart power management module, it enables remote control of the controlled device's power supply by simulating physical power button operations (power on/off/reboot). 

The ATX board will be installed in the controlled device's chassis, providing more concealed and stable power management.

![rm1-and-atx-borad](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/rm1-and-atx-borad.jpg){class="glboxshadow"}

## Package Contents

![inside the box](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/inside-the-box.png){class="glboxshadow gl-80-desktop"}

- 1 x ATX main board
- 1 x 9-PIN Wire Set
- 1 x Screw package
- 1 x USB-A to Type-C cable
- 1 x ATX Bracket Set

## PIN-OUT

![pinout](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/pinout.jpg){class="glboxshadow gl-80-desktop"}

Explanation of Interfaces:

1. Type-C Interface: Connect to the KVM device.
2. Firmware Upgrade button: for the single-chip microcomputer on the ATX main board.
3. Reset button.
4. Connect to the control line of the computer panel.
5. Connect to the F_PANEL interface of the computer.

!!! note

    1. Interfaces 4 and 5 can be connected interchangeably. That is to say, interface 5 can be connected to the control line of the computer panel, and interface 4 can be connected to the F_PANEL. 
    
    2. There are two LEDs on the ATX board, and both LEDs' behavior is the same as the Power LED (blue indicates the ATX system; green indicates PC power). There is no HDD LED on the ATX board. The LED status on the board is consistent with the Power LED status on the computer panel. 

Interfaces 4/5 diagram:

![interface](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface.png){class="glboxshadow gl-60-desktop"}

## Installation

Watch this video to install ATX board, or follow the steps below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3VEjZgzgI44" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Screw ATX Board and Bracket

Fix the ATX board and the ATX Bracket Set with the screws provided.

![screwing](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/screwing.jpg){class="glboxshadow gl-90-desktop"}

### 2. Install ATX Board into PC Case

Connect interfaces 4 and 5 respectively to the controlled PC's control line and F_PANEL interface. 

![interface connect](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface_connect.jpg){class="glboxshadow gl-90-desktop"}

The 9-PIN Wire Set provided in the ATX Package allows you to connect one of the ATX board interface 4/5 to the controlled computer's control line or F_PANEL interface. 
    
You need to use the wire set included in your computer case to connect another ATX board interface 4/5 to the controlled computer's control line or F_PANEL interface.

**Note**: The interface polarity may vary depending on different PC case. Please double check it before installation.

Below are some examples of connecting interface 4/5 to the F_PANEL interface of the controlled computer for your reference.

??? "For 10-1 pin PANEL"

    If the row of pins on your controlled computer's motherboard used to connect to the control panel is a 10-1 pin PANEL, as shown below.

    ![10-1pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_1.png){class="glboxshadow"}

    Please refer to the diagram below for connection, make sure that the silkscreen printing (i.e., the words HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) is visible facing outward and not obscured facing inward.

    ![10-1pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_2.jpg){class="glboxshadow"}
    <small>Front View</small>

    ![10-1pin panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_3.jpg){class="glboxshadow"}
    <small>Rear View</small>

    Then use the wire set included in your computer case to connect another ATX board interface to the computer control line.

??? "For 20-5 pin PANEL"

    If the row of pins on your controlled computer's motherboard used to connect to the control panel is a 20-5 pin PANEL, as shown below.

    ![20-5pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_1.jpg){class="glboxshadow"}

    Please refer to the diagram below for connection, make sure that the silkscreen printing (i.e., the words HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) is visible facing outward and not obscured facing inward.

    ![20-5pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_2.jpg){class="glboxshadow"}
    <small>Front View</small>

    ![20-5pin panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_3.png){class="glboxshadow"}
    <small>Rear View</small>

    Then use the wire set included in your computer case to connect another ATX board interface to the computer control line.

??? "For 20-8 pin PANEL"

    If the row of pins on your controlled computer's motherboard used to connect to the control panel is a 20-8 pin PANEL, as shown below.

    ![20-8pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_1.jpg){class="glboxshadow"}

    Please refer to the diagram below for connection, make sure that the silkscreen printing (i.e., the words HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) is visible facing outward and not obscured facing inward.

    ![20-8pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_2.png){class="glboxshadow"}

    Then use the wire set included in your computer case to connect another ATX board interface to the computer control line.

The final connected ATX board is shown below.

![atx board connected](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected1.png){class="glboxshadow gl-90-desktop"}

![atx board connected](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected2.png){class="glboxshadow gl-90-desktop"}

Then install the ATX board bracket into the computer case.

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install1.png){class="glboxshadow gl-90-desktop"}

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install2.png){class="glboxshadow gl-90-desktop"}

### 3. Connect ATX Board and KVM

Connect the Type-C port of ATX board to the USB-A port of the KVM device (such as Comet GL-RM1) using the included USB cable.

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install3.png){class="glboxshadow gl-90-desktop"}

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install4.png){class="glboxshadow gl-90-desktop"}

This completes the installation of the ATX board. 

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install5.png){class="glboxshadow gl-90-desktop"}

Now you can log in to your KVM, navigate to **Accessories** to control the ATX power.

![atx power](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/atx_power.png){class="glboxshadow gl-90-desktop"}

## FAQ

**Q1. Can I use the GL-ATXPC board with non-GL.iNet KVM devices?**

A1. No. GL-ATXPC board is an accessory for GL.iNet KVM devices. It should be used in conjunction with GL.iNet KVM.

---

**Q2. After installing the ATX board, what should I do if I cannot control the remote device's power (on/off) via the KVM?**

A2. Please try the following methods.

- Ensure the controlled device can be powered on/off normally when the physical power button on the PC case front panel is pressed.

- Check the wiring polarity. Try flipping the POWER SW connector polarity on the controlled device's motherboard to avoid incorrect wiring.

    ![connector polarity](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/power-sw-connector.png){class="glboxshadow gl-90-desktop"}

- When connecting to the F_PANEL interface on the controlled device's motherboard, ensure the silkscreen printing (e.g., HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) is visible facing outward, not obscured facing inward.

- Upgrade the KVM's firmware.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.