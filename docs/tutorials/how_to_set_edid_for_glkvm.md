# How to set EDID for GL.iNet KVM?

## What is EDID

EDID, i.e. Extended Display Identification Data, is a standard data format formulated by the Video Electronics Standards Association (VESA). It is stored in the non-volatile memory of the display and contains key information of the display such as the manufacturer, maximum resolution, refresh rate, etc. Devices like computers can automatically adjust the parameters of the output signal by reading the EDID to ensure that the display shows images in the best state.

Generally speaking, when devices such as computers, laptops, and game consoles are connected to a display, they will automatically read the EDID to set appropriate display parameters, avoiding problems such as blurry images and flickering, and providing users with a clear and stable visual experience.

The EDID settings in GL.iNet KVM aims to automatically match the optimal parameters of the display. When a GL.iNet KVM is connected to the controlled device, it can automatically adjust the display output to present the best picture by reading the EDID of the display. 

## How to set EDID for GL.iNet KVM

On the GL.iNet KVM console, navigate to **Settings** -> **Video** -> **EDID**. There are some preset EDID settings. 

![edid preset](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/edid_preset.jpg){class="glboxshadow"}

**The default EDID of GL.iNet KVM is already suitable for most scenarios and usually does not need to be modified**.

In case of special situations, such as to configure UEFI/BIOS or customize the resolution/refresh rate, you can select a preset value, e.g., 1920×1280/AUO/60HZ, or switch to Customize and enter the custom EDID code.

If you can't find a suitable code, you may refer to [this link](https://github.com/linuxhw/EDID){target="blank"} or steps below to customize EDID configuration.

1. Find a suitable EDID in [this link](https://github.com/linuxhw/EDID){target="blank"} and copy it.

    ![edid code](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/edid_code.jpg){class="glboxshadow"}

2. Log in to the GL.iNet KVM console and navigate to **Settings** -> **EDID**. Switch to **Customize** mode, paste the parameters to the input box, and click **Set Custom** to apply the settings.

    ![edid customize](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/edid_customize.png){class="glboxshadow"}

!!! Note

    1. The resolution shall not exceed 2560×1440@60Hz. For example, a resolution of 2560×1600@60Hz is not supported.
    2. The maximum supported refresh rate is 60Hz. For resolutions higher than 1920x1080, a frame rate of 60FPS or lower is recommended.
    3. Avoid including interlaced resolutions, otherwise it will cause the image to display abnormally.
    4. The input EDID code block shall not exceed two.
    5. Basic audio support is required. Otherwise the sound card may not be selectable in the controlled device, resulting in no sound. 

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
