# What should I do if mouse cursors fail to align?

If the mouse cursor on the controlling device fails to align with the one on the controlled device, follow the troubleshooting steps below.

![cursor misalignment](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/mouse_cursor.png){class="glboxshadow"}

1. **Confirm whether the issue occurs when the mouse is moving or idle.** 

    <u>Case 1</u>. If cursors align correctly when the mouse is idle but go out of sync during movement, please check the network on both ends and ensure stable connectivity.

    In addition, you can hide the local cursor so that only the remote cursor shows on the control screen, preventing cursor misalignment issues.

    On the KVM console, navigate to **Settings** -> **Remote Device Settings** -> **Show Local Cursor** and disable it.

    ![hide local cursor](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/hide_local_cursor.png){class="glboxshadow"}

    <u>Case 2</u>. If cursors fail to align even when the mouse is idle, proceed to the next step.

2. **If the controlled device is a laptop, this is likely caused by incorrect display resolution.** 

    Confirm the laptop's screen aspect ratio, then you can either adjust the resolution on the controlled laptop or modify the EDID setting for your KVM device.
    
    ??? note "Adjust resolution on the controlled laptop"
    
        Take macOS laptop as an example.

        1. Go to **Settings** -> **Displays** -> **Optimize for**.

            ![mac displays](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/mac_displays.png){class="glboxshadow" width="582"}

        2. Change it to **GLKVM**.

            ![select glkvm](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/select_glkvm.png){class="glboxshadow" width="582"}

        3. Choose the corresponding resolution, then check if the mouse cursor can be overlapped.

            ![resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/resolution.png){class="glboxshadow"}

    ??? note "Modify EDID setting for your KVM device"

        EDID, short for Extended Display Identification Data, automatically matches the optimal display parameters. The default EDID is suitable for most scenarios and generally does not need to be modified. See [here](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} for details. 
        
        If the EDID has been changed but the screen does not update, try restarting the controlled device.

3. **If the controlled device is not a laptop (e.g. desktop PC connected to an external monitor)**, confirm its primary display aspect ratio, then switch the EDID for your KVM accordingly. See [here](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} for details. 

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.