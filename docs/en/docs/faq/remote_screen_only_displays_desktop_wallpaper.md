# What should I do if the remote screen only displays the desktop wallpaper

=== "Windows"
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

=== "macos"
     When your MacBook is connected to a KVM, the remote view only shows desktop wallpaper and no application windows, which may result from **Extended display** mode. Please follow these steps to switch to **mirror display** to resolve the issue:
     
    1. Click the Apple menu in the top-left corner of your screen and select **System Settings**.  

    2. Scroll down the sidebar and choose **Displays**.  

        ![mac system settings](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-system-settings.png){class="glboxshadow"}
 
    3. In the layout view, click on the **External display** ; you’ll see MacBook screen and any connected monitors.

    4. Click the **Use as** dropdown menu and select **Mirror mode**, usually Mirror for Built-in Display.  

        ![mac mirror display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-mirror-display.png){class="glboxshadow"}

    After setup, your Mac’s local screen will be duplicated to KVM, so you can view the full desktop and all application windows remotely.
    
    !!! Note
        This solution only applies to display issues caused by Extended display mode. If the problem persists after enabling mirroring, please ensure your MacBook has completed local user login and is not stuck at the system login screen.
      
---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.