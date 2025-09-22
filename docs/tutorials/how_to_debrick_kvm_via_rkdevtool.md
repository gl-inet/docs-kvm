# How to debrick KVM via RKDevTool

This tutorial will introduce how to debrick GL.iNet KVM using the RKDevTool. It applies to scenarios where the KVM is bricked and cannot be recovered via regular firmware updates or U-Boot failsafe mode.

## Preparation

Please prepare the following tools for debricking.

- A Windows computer
- A USB data cable
- A power adapter (for the KVM device)

!!! Note 

    Do NOT disconnect the USB cable or power off KVM during the debricking process, as this may damage the device.
    
    It is recommended to back up important data before starting the debricking process.

## Debrick steps

To avoid debrick failure, please follow the steps in order. 

1. Power off your KVM device.

2. Download the driver package from [here](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/DriverAssitant_v5.11.zip) to your computer, and extract it to any directory.

3. Double click the .exe file to complete the driver installation program.

    ![install driver](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_1.png){class="glboxshadow"}

    ![install driver](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_2.png){class="glboxshadow"}

4. Download the **RKDevTool** from [here](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/RKDevTool_Release_v2.84.zip) to your computer, and extract it to an easily accessible directory.

5. Double click the .exe file to run the flashing tool on your computer.

    ![run rkdevtool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_1.png){class="glboxshadow"}

    ![run rkdevtool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_2.png){class="glboxshadow"}

6. Connect the KVM's Type-C OTG port to the computer's USB port via a USB data cable.

    Take Comet (GL-RM1) as an example. The Type-C OTG port is shown below.

    ![connect usb cable](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/otg-port-rm1.png){class="glboxshadow gl-60-desktop"}

7. Hold the RESET button for **10 seconds** while plugging the power cable into KVM. Then release the button. Your KVM device will enter the Loader mode.

    ![reset button](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/reset_button_rm1.jpg){class="glboxshadow" width="433"}

8. After successfully entering the Loader mode, the RKDevTool will display "Found Loader Device". 

    ![rkdevtool panel](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/rkdevtool_panel.jpg){class="glboxshadow"}

    The KVM device will automatically restart once the upgrade is complete.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.