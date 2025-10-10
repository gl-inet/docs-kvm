# Mouse cursors fail to overlap on KVM control interface

If you notice that the mouse cursor of the controlling device cannot overlap with that of the controlled device, please follow the steps below for troubleshooting.

![mouse cursors do not overlap](https://static.gl-inet.com/docs/kvm/faq/mouse_cursor_overlay_issue/mouse_cursor_cannot_be_superimposed.png){class="glboxshadow gl-90-desktop"}

**Step 1**. Confirm whether the issue occurs when the mouse is moving or stationary. 

If the cursor can overlap when stationary but lags when moving the mouse on the controlling device, causing it to fail to overlap with the cursor on the controlled device, please check the network environment on both sides and ensure network stability.

If the cursor can not be overlapped in stationary, turn to the next step.

**Step 2**. If the controlled device is a laptop, it may be a display resolution issue. Please confirm the screen aspect ratio of your laptop, then either switch the display resolution of the controlled laptop or switch the EDID in the GLKVM app.

The following is an example of switching display resolution on a macOS laptop.

Go to the Settings -> Displays -> Optimize for.

![settings](https://static.gl-inet.com/docs/kvm/faq/mouse_cursor_overlay_issue/mac_settings.png){class="glboxshadow gl-80-desktop"}

Change it to **GLKVM**.

![select glkvm](https://static.gl-inet.com/docs/kvm/faq/mouse_cursor_overlay_issue/select_glkvm.png){class="glboxshadow gl-80-desktop"}

Choose the corresponding resolution, and check if the mouse cursor is superimposed.

![resolution](https://static.gl-inet.com/docs/kvm/faq/mouse_cursor_overlay_issue/resolution.png){class="glboxshadow gl-80-desktop"}

**Step 3**. If the controlled device is not a laptop, please confirm the ratio of the controlled device's main screen, then switch the EDID for your KVM device based on this screen ratio.

Click [here](how_to_set_edid_for_glkvm.md) to learn how to set EDID for GL.iNet KVM.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.