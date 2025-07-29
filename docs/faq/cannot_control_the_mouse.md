# What should I do if I cannot control the mouse and keyboard?

Sometimes you may find that even if all the cables are connected, you still cannot control the mouse & keyboard on the controlled device through KVM.

Here are some suggestions.

1. Check the wiring. 

    Taking Comet (GL-RM1) as an example. It has two USB Type-C ports:  

    - The one on the side is labeled "5V 2A" for power input (connecting to a power adapter).  
    - The other on the back has logos for mouse and keyboard, connecting to the controlled device's USB port to receive keyboard and mouse signals. 

    Reversing these two connections will prevent the KVM device from starting up and make the mouse & keyboard unresponsive.
    
    Please check if these two Type-C interfaces are connected correctly.

    ![gl-rm1 ports](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/gl-rm1-ports.png){class="glboxshadow gl-80-desktop"}

2. Check the USB cable. 

    Use the included USB cable. Ensure it connects the controlled device's USB port to the KVM's USB port and supports data transmission.

    Only cables capable of data transfer allow keyboard and mouse control of the remote device.

    Reconnect the USB cable and restart the controlled device.

3. Try switching the mouse mode to Relative mode. 

    Log in to your KVM device, navigate to Settings -> Mouse Mode, switch it to Relative, and check if the problem can be resolved.

    ![mouse mode](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/mouse_mode.png){class="glboxshadow"}

4. Upgrade the KVM's firmware to the latest version. [KVM Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"}

5. Check the Device Manager on the controlled computer for any malfunctioning drivers.

6. Check if the controlled device is blocked by IT security software.


---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.