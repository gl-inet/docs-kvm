# GL-ATX Board User Guide

The ATX board is an optional accessory for GL.iNet KVM device. As a smart power management module, it enables remote control of the controlled device's power supply by simulating physical power button operations (power on/off/reboot). 

The ATX board will be installed in the controlled device's chassis, providing more concealed and stable power management.

![rm1-and-atx-borad](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/rm1-and-atx-borad.jpg){class="glboxshadow"}

## Components

There are some components in the ATX Package:

- ATX main board
- USB-A to Type-C cable
- 9 PIN Wire Set
- Screw package
- ATX Bracket Set

![components](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/components.png){class="glboxshadow gl-60-desktop"}

## ATX Board PIN-OUT

![pinout](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/pinout.jpg){class="glboxshadow gl-80-desktop"}

Explanation of Interfaces:

1. Type-C Interface: Connect to the KVM device.
2. Firmware Upgrade button: for the single-chip microcomputer on the ATX main board.
3. Reset button.
4. Connect to the control line of the computer panel.
5. Connect to the F_PANEL interface of the computer.

!!! note

    Interfaces 4 and 5 can be connected interchangeably. That is, interface 5 can be connected to the control line of the computer panel, and interface 4 can be connected to the F_PANEL. The LED status on the board is consistent with the Power LED status on the computer panel.

Interfaces 4/5 diagram:

![interface](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/interface.png){class="glboxshadow gl-60-desktop"}

## ATX Board Installation

Watch this video to install ATX board, or follow the steps below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3VEjZgzgI44" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Screw ATX Board and Bracket

Fix the ATX board and the ATX Bracket Set with the screws provided.

![screwing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/screwing.png){class="glboxshadow gl-60-desktop"}

### 2. Install ATX Board into the Chassis

Connect interfaces 4 and 5 respectively to the controlled computer's control line and F_PANEL interface. 

The 9 PIN Wire Set provided in the ATX Package allows you to connect one of the ATX board interface 4/5 to the controlled computer's control line or F_PANEL interface. 
    
You need to use the wire set included in your computer chassis to connect another ATX board interface 4/5 to the controlled computer's control line or F_PANEL interface.

!!! Note

    The interface polarity may vary depending on different  PC chassis. Please double check it before installation.

**Here are two examples of connecting one of the ATX board interfaces 4/5 to the controlled computer's F_PANEL interface.**

**Example 1. For 10-1 pin PANEL**

If the row of pins on the motherboard of your controlled computer for connecting to the control panel is 10-1 pin PANEL, as shown below.

![10-1pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/10-1pin_panel_1.png){class="glboxshadow"}

Please refer to the diagram below for connection, make sure that the silkscreen printing (i.e., the words HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) are visible facing outward and not obscured facing inward.

![10-1pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/10-1pin_panel_2.jpg){class="glboxshadow"}
<small>Front View</small>

![10-1pin panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/10-1pin_panel_3.jpg){class="glboxshadow"}
<small>Rear View</small>

Then use the wire set included in your computer chassis to connect another ATX board interface to the computer control line.

**Example 2. For 20-5 pin PANEL**

If the row of pins on the motherboard of your controlled computer for connecting to the control panel is 20-5 pin PANEL, as shown below.

![20-5pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/20-5pin_panel_1.jpg){class="glboxshadow"}

Please refer to the diagram below for connection, make sure that the silkscreen printing (i.e., the words HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) are visible facing outward and not obscured facing inward.

![20-5pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/20-5pin_panel_2.jpg){class="glboxshadow"}
<small>Front View</small>

![20-5pin panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/20-5pin_panel_3.png){class="glboxshadow"}
<small>Rear View</small>

Then use the wire set included in your computer chassis to connect another ATX board interface to the computer control line.

The final connected ATX board is shown below.

![axt board install 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/atx_board_install1.png){class="glboxshadow gl-60-desktop"}

![axt board install 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/atx_board_install2.jpg){class="glboxshadow"}
<small>Detailed front view of ATX board</small>

![axt board install 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/atx_board_install3.jpg){class="glboxshadow"}
<small>Detailed rear view of ATX board</small>

Then place the ATX board bracket on the side frame of the computer chassis (if required).

![axt board install 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/atx_board_install4.png){class="glboxshadow"}

### 3. Connect ATX Board and KVM

Connect the Type-C interface of ATX board to the USB-A interface of the KVM device (such as Comet GL-RM1), using the included USB-A to Type-C cable.

![axt board install 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/atx_board_install5.png){class="glboxshadow"}

![axt board install 6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/axt_package/atx_board_install6.jpg){class="glboxshadow"}

This completes the installation of the ATX board. 

Please log in to the Comet, navigate to [Accessories](../gl-rm1/index.md/#accessories) to set the ATX power.

!!! Note

    If you can't turn on/off the controlled computer via GL-RM1 control page, please check the polarity of the wiring, try flipping the connector polarity to avoid wrong wiring.