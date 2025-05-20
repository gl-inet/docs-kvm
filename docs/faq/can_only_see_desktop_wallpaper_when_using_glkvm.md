# What to do if I can only see desktop wallpaper when using GLKVM?

If you can only see desktop wallpaper when accessing the controlled device via GLKVM, it's likely that your controlled deivce has multiple displays and it's set to **Extend Displays**.

![extend display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/extend_displays.jpg){class="_blank"}

Take Windows 1O as an example. 

On the controlled device, go to **Settings** -> **System** -> **Display**.

![win10 system settings](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/win10_system_settings.png){class="_blank"}

On the Display page, scroll down to locate **Multiple displays**.

Switch from Extend Displays to **Duplicate display**.

![duplicate display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/duplicate_displays.jpg){class="_blank"}

Click **Keep changes**.

![keep changes](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/keep_changes.png){class="_blank"}

Then check if you can access the controlled device normally.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.