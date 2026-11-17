# What should I do if the local and remote cursors don't match {#what-should-i-do-if-the-local-and-remote-cursors-dont-match}

If your local cursor (on the controlling device) does not match the remote cursor (on the controlled device), follow the troubleshooting steps below.

![cursor misalignment](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/mouse_cursor.png){class="glboxshadow"}

1. If the two cursors match when the mouse is idle but go out of sync during movement, check the network on both ends and ensure stable connectivity.

    In addition, you can hide the local cursor so that only the remote cursor shows on the control screen, preventing cursor misalignment issues.

    On the KVM console, navigate to **Settings** -> **Remote Device Settings** -> **Show Local Cursor** and disable it.

    ![hide local cursor](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/hide_local_cursor.jpg){class="glboxshadow"}

2. If the two cursors don't match even when the mouse is idle, and your KVM is Comet Q (GL-RMQ1), reselect your device type on the KVM console. If the problem persists, proceed to the next step.
    
    ![device type](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/device_type.png){class="glboxshadow"}

3. If the controlled device is a laptop, this is likely caused by incorrect display resolution.

    Confirm the laptop's screen aspect ratio, then you can either adjust the resolution on the controlled laptop or modify the EDID setting for your KVM device.
    
    ??? note "Adjust resolution on the controlled laptop"
    
        **For macOS**:

        1. Go to **Settings** -> **Displays** -> **Optimize for**.

            ![mac displays](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos1.png){class="glboxshadow" width="582"}

        2. Change it to **GLKVM**.

            ![select glkvm](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos2.png){class="glboxshadow" width="582"}

        3. Choose the corresponding resolution, then check if the mouse cursor can be overlapped.

            ![resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos3.png){class="glboxshadow"}

        **For Windows**:

        1. Go to **Settings** -> **System** -> **Displays**.

            ![windows display](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows1.png){class="glboxshadow"}

        2. Scroll down to find **Display resolution** and click the box on the right.

            ![display resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows2.png){class="glboxshadow"}

        3. Select the appropriate display resolution, then click **Keep changes** in the pop-up window to apply it.

            ![display resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows3.png){class="glboxshadow"}

            ![display resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows4.png){class="glboxshadow"}

    ??? note "Modify EDID setting for your KVM device"

        EDID, short for Extended Display Identification Data, automatically matches the optimal display parameters. The default EDID is suitable for most scenarios and generally does not need to be modified. See [How to set EDID for GL.iNet KVM](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. 
        
        If the EDID has been changed but the screen does not update, try restarting the controlled device.

4. If the controlled device is not a laptop (e.g. a desktop PC with an external monitor), confirm its primary display aspect ratio, then switch the EDID for your KVM accordingly. See [How to set EDID for GL.iNet KVM](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}. 

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.