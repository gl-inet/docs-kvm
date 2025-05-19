# How to fix mouse cursor overlay issue on macOS?

When using GL-RM1, you may get the issue that the mouse cursor of the controlling device can't be superimposed on the controlled macOS device.

![mouse cursor cannot be superimposed](https://static.gl-inet.com/docs/kvm/faq/mouse_cursor_overlay_issue/mouse_cursor_cannot_be_superimposed.png){class="glboxshadow gl-60-desktop"}

It's related to the display resolution. The macOS resolution is different from that of GLKVM.

Please go to the Settings -> Displays -> Optimize for.

![settings](https://static.gl-inet.com/docs/kvm/faq/mouse_cursor_overlay_issue/mac_settings.png){class="glboxshadow gl-60-desktop"}

Change it to **GLKVM**.

![select glkvm](https://static.gl-inet.com/docs/kvm/faq/mouse_cursor_overlay_issue/select_glkvm.png){class="glboxshadow gl-60-desktop"}

Choose the Resolution you prefer, and you’ll find the mouse cursor is superimposed. Then you can enjoy using it.

![resolution](https://static.gl-inet.com/docs/kvm/faq/mouse_cursor_overlay_issue/resolution.png){class="glboxshadow gl-60-desktop"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.