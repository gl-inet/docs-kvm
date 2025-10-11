# What should I do if the KVM control interface only displays the remote desktop wallpaper?

When accessing the controlled device through KVM, if you can only see the remote desktop wallpaper and no operations respond, it's likely that your controlled device has multiple displays and it's set to **Extend Displays**.

![extend display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/extend_displays.jpg){class="glboxshadow"}

To fix this issue, please set the display settings of the controlled device to **Duplicate display**.

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