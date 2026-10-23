# What should I do if I see "Press Failed" when using Fingerbot

If the KVM console displays "Press Failed" when you use Fingerbot, there may be a pairing issue between Fingerbot and your KVM device. 

Follow the steps below to remove the existing pairing and pair Fingerbot again.

1. Log in to your KVM and go to **Toolbox** -> **Terminal** -> **Access Terminal** to open the Terminal. 

2. Run the following commands in sequence:

    ```
    bluetoothctl
    ```
    ```
    scan on
    ```

    ![open bluetoothctl](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/bluetoothctl.png){class="glboxshadow"}

    Wait a moment, then run `scan off` to stop scanning.

3. Run `devices` to view all detected Bluetooth devices. Find your Fingerbot (listed as FGB) and record its MAC address.

    ![devices](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/devices.png){class="glboxshadow"}

4. Enter `exit` to leave the bluetoothctl session. Then run the command below to remove the old pairing record. Replace this MAC address with your Fingerbot's actual MAC address.

    ```
    bluetoothctl remove E1:2D:B2:75:D5:BC
    ```

5. Re-pair the Fingerbot with the following command. Replace this MAC address with your Fingerbot's actual MAC address.

    ```
    fingerbot pair E1:2D:B2:75:D5:BC
    ```

    ![repair fingerbot](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/repair.png){class="glboxshadow"}

    You will see **Done** in the terminal if the operation succeeds. Then try using Fingerbot again. 

6. If the problem persists, please contact us at [support@gl-inet.com](mailto:support@gl-inet.com) and provide the information below for further troubleshooting.

    - The output of the following commands:

        ```
        fingerbot action
        ```
        ```
        ls -l /
        ```

    - The latest KVM logs, exported from **Help** > **Export Log Files**.

        ![export logs](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/export_logs.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
