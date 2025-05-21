# What should I do if I cannot control the mouse?

Sometimes you may find that even if all the cables are connected, you still cannot control the mouse on the remote controlled device through KVM.

## Possible Causes

1. **Incorrect wiring**. 

    Taking Comet (GL-RM1) as an example, Comet has two USB Type-C interfaces: 

    - One for power input.
    - The other for connecting to a controlled device's USB port to receive keyboard and mouse signals. 
    
    You may have connected the two in reverse, causing the KVM to fail to start up and the mouse to be uncontrollable.

2. **USB cable mismatch**. 

    You may have used a USB cable that only supplies power but cannot transfer data to connect the controlled device's USB port to the KVM USB port, due to the inability to transmit signals, the mouse cannot be controlled normally.

## Suggestions

1. **Check the wiring**. 

    Taking Comet (GL-RM1) as an example. 
    
    The USB Type-C interface on the side is labeled "5V 2A" for power input, while the USB Type-C interface on the back has logos for mouse and keyboard, indicating that it is used to connect to the controlled device, in order to receive keyboard and mouse signals. 

    Please check if these two Type-C interfaces are connected correctly.

    ![rm1 hardware ports](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/rm1_ports.png){class="glboxshadow"}

2. **Check the USB cable**. 

    Use the included USB cable. Ensure it connects the controlled device’s USB port to the KVM’s USB port and supports data transmission.

    Only cables capable of data transfer allow keyboard and mouse control of the remote device.

    Reconnect the USB cable and restart the controlled device.

3. **Try upgrading the KVM's firmware to the latest version**.

4. **Check if the controlled device is blocked by IT security software**.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.