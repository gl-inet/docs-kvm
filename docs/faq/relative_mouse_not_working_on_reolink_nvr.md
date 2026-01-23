# What should I do if relative mouse mode doesn't work on Reolink NVR?

When using GL.iNet KVM (e.g., Comet Pro GL-RM10) to control Reolink NVR (especially models do not support dual mice) or certain vintage computers (such as those without USB interfaces), the relative mouse mode may not work. Common issues include complete failure of the mode, or trackable mouse movement but unresponsive clicks.

This problem mainly comes from a compatibility issue between the KVM's mouse simulation and the limited capabilities of devices like Reolink NVR:

- **Before firmware v1.4.0**: The KVM was designed to simulate only one mouse. Switching between relative and absolute modes requires you to restart the KVM, but this worked fine with most vintage or specialized devices.

- **After firmware v1.4.0**: To enable seamless mode switching without restart, the default logic was updated to simulate two mice simultaneously (one for relative mode, the other for absolute mode). However, Reolink NVR and some vintage computers lack support for dual mice, causing two common issues:

    - Relative mouse mode doesn’t work at all;
    - Mouse still tracks, but clicking does not respond.

To resolve the issue, you can force relative mouse mode in the terminal. Follow these steps:

1. Access the KVM Console, and navigate to **Toolbox** -> **Terminal**. Click **Access** to enter the KVM terminal.

2. Open the configuration file with the following command:

    `vi /etc/kvmd/override.yaml`

3. Execute the following command to force relative mouse mode:

    ```
    kvmd:
        hid:
            mouse:
                absolute: false
    ```

4. Save the file and exit the editor.

5. Restart the KVM device to apply the changes.

!!! note

    1. If the above configurations don't work, roll back your KVM firmware to v1.3.2, which uses single-mouse simulation compatible with vintage devices.

    2. The standalone GLKVM app for Mac OS does not support relative mouse mode due to browser kernel limitations (lack of requestPointerLock API support). Use the web interface instead.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.