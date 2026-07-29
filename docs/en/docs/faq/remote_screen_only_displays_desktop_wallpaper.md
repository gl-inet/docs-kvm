# What should I do if the remote screen only displays the desktop wallpaper

When accessing the controlled device through KVM, if you can only see the desktop wallpaper and no operations respond, it's likely that your controlled device uses multiple monitors configured in **Extend Displays** mode.

![extend display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/extend_displays.jpg){class="glboxshadow"}

To resolve the problem, switch the controlled device's display mode to **Duplicate display**.

Take Windows 10 as an example. 

On the controlled device, go to **Settings** -> **System** -> **Display**.

![win10 system settings](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/win10_system_settings.png){class="glboxshadow"}

On the Display page, scroll down to locate **Multiple displays**.

Switch from Extend Displays to **Duplicate display**.

![duplicate display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/duplicate_displays.jpg){class="glboxshadow"}

Click **Keep changes**.

![keep changes](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/keep_changes.png){class="glboxshadow"}

Then check if you can access the controlled device normally.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.