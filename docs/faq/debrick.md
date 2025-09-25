# Using U-Boot to unbrick your KVM

If you bricked your KVM due to some DIY projects or flashing a wrong firmware, your KVM may not be able to power up properly. In this case, you can re-install the firmware by using U-Boot failsafe.

## Preparation

Please prepare a computer with an Ethernet port. 

If your computer does not have Ethernet port, prepare an additional USB Ethernet Adapter. 

## Unbrick steps

To avoid unbrick failure, please follow the steps below strictly.

1. Please download firmware [here](https://dl.gl-inet.com/kvm){target="_blank"} to your computer.

2. Remove the power of KVM. Connect your computer to the Ethernet port of the KVM.

3. Press and hold the Reset button firmly, and power on the KVM **at the same time**.

    Then you will see the LED flashing in a regular pattern several times. Release the button **after** the flash sequence changes.

    - **Comet (GL-RM1)**: When holding the Reset button, the blue LED will flash 5 times. Release the Reset button after the 5 flashes, and the blue LED will remain solid.

    - **Comet PoE (GL-RM1PE)**: When holding the Reset button, the blue LED will flash 5 times. Release the Reset button after the 5 flashes, and the blue LED will remain solid.

    - **Comet Pro (GL-RM10)**: Hold the Reset button for about 5 seconds, during which power on the KVM at the same time, then release the button. It will enter the U-Boot mode.

4. Manually set the IP address of your computer to **192.168.1.2**. Please check the step-by-step guide for different operating systems below.

    ??? "Windows 7 / Windows 10"

        1. Go to **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Right click **Local Area Connection** -> **Properties**.

        3. Click **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Set the **IP adress** to `192.168.1.2` manually.

        5. Set the **Subnet mask** to `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. Click the **OK** button.

    ??? "Windows 11"

        1. Open Settings.

        2. Click on **Network & Internet**.

        3. Click the **Ethernet** tab.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        4. Under the "IP assignment" section, click the **Edit** button.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Select the **Manual** option.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        6. Turn on the **IPv4 toggle** switch.

        7. Set the static **IP address** as **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        8. Specify the **Subnet mask** as **255.255.255.0**.

        9. Click the **Save** button.

    ??? "macOS"
    
        1. Click the **Apple** icon in the top left corner of the screen, and select **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        2. Click **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        4. Click **Ethernet** on the left and then click the drop-down box next to **Configure IPv4** and select **Manually**. If you are using a USB Ethernet Adapter, Ethernet may not be found and it may show up as the name of the USB Ethernet Adapter.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        4. Enter the **IPv4 Address** to `192.168.1.2`, **Subnet Mask** to `255.255.255.0`, **Router** to `192.168.1.1`, then click the Apply button in the lower right corner.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

5. Use browser to visit **http://192.168.1.1**. This is the U-Boot Web UI.

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    **Note:** The U-Boot Web UI above may not be exactly the same as what you see, because the U-Boot version is different for different production dates. For security reasons, we currently do not provide separate U-Boot upgrades. If an update is necessary, we will integrate it into the new firmware.

6. Click **Choose file** button to find the firmware file. Then click **Update firmware** button.

7. Wait for about 3 minutes. **Do NOT power off your KVM when updating.** 

    The KVM is ready when its LED is **flashing white**.

8. Revert the computer IP setting you did in step 4.

9. Unplug the Ethernet cable between your computer and the KVM, then connect your KVM to a network source (e.g. a router or a network switch) via this Ethernet cable. For Comet Pro (GL-RM10), you can also connect it to the Wi-Fi.

    Wait for about 1 minute to allow the KVM to obtain Internet access. Then connect your computer to the network source, and you will be able to access the KVM via `glkvm.local` again.

    **Note:** Configuration settings are typically retained. However, they will be reverted to default if a configuration error caused the system failure that required recovery.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
