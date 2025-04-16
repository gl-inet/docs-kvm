# How to Set EDID for GL.iNet KVM

## What is EDID

EDID, i.e. Extended Display Identification Data, is a standard data format formulated by the Video Electronics Standards Association (VESA). It is stored in the non-volatile memory of the display and contains key information of the display such as the manufacturer, maximum resolution, refresh rate, etc. Devices like computers can automatically adjust the parameters of the output signal by reading the EDID to ensure that the display shows images in the best state.

Generally speaking, when devices such as computers, laptops, and game consoles are connected to a display, they will automatically read the EDID to set appropriate display parameters, avoiding problems such as blurry images and flickering, and providing users with a clear and stable visual experience.

The EDID configuration in GL.iNet KVM aims to automatically match the optimal parameters of the display. When GL.iNet KVM is connected to the controlled device, it can automatically adjust the display output to present the best picture by reading the EDID of the display. 

## How to set EDID for GL.iNet KVM

In the GLKVM panel -> Settings -> EDID, there are some preset EDID configuration. 

![edid preset](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/edid_preset.jpg){class="glboxshadow"}

**The default EDID configuration of GL.iNet KVM is already suitable for most scenarios and usually does not need to be modified**.

In case of special situations, such as to configure UEFI/BIOS or customize the resolution/refresh rate, you can select a preset value, e.g., 1920×1280/AUO/60HZ, or switch to Customize and enter the custom EDID code.

You may refer to [this link](https://github.com/linuxhw/EDID){target="blank"} or steps below to customize EDID configuration.

1. Find a suitable EDID configuration in [this link](https://github.com/linuxhw/EDID){target="blank"}.

    ![edid code](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/edid_code.jpg){class="glboxshadow"}

2. Go to the GLKVM control panel -> Settings -> EDID, switch to Customize mode, copy the parameters to the input box. Click Set Custom to apply the EDID settings.

    ![edid customize](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/edid_customize.png){class="glboxshadow"}

!!! Note

    1. The resolution shall not exceed 2560x1440/60. For example, the setting of 2560x1600/60 cannot be used.
    2. The maximum resolution/recommended resolution shall not exceed 60FPS.
    3. Avoid including interlaced resolutions, otherwise it will cause the image to display abnormally.
    4. The input EDID code block shall not exceed two.
    5. Basic audio support is required. Otherwise the sound card may not be selectable in the controlled device, resulting in no sound. 

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
