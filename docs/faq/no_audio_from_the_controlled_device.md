# What should I do if I cannot hear audio from the controlled device?

After connecting the KVM and the controlled device, if you fail to hear the audio from the controlled device, for example, cannot hear the audio while playing video on the controlled device, here are some troubleshooting tips:

1. Ensure the Audio is enabled in GLKVM app.

    In GLKVM app (on your controlling device), navigate to Settings -> Remote Device Settings -> Audio, make sure it is enabled, and the audio icon in the bottom right corner is green on.

    ![audio settings](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/audio_settings.png){class="glboxshadow"}

    ![audio icon](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/audio_icon.jpg){class="glboxshadow"}

2. Ensure all cables are firmly connected between the KVM and the controlled device. Loose wiring may affect the audio output.

3. Check whether an HDMI converter is connected. Some converters do not support audio.

    It is recommended to use the HDMI cable that comes in the box, as some older-standard HDMI cables may not support audio transmission.

4. Check whether the controlling device and the controlled device are set to mute.

5. Check the output settings of your controlled device and ensure the output device is GLKVM.

    ??? "macOS"

        On your controlled device, go to **Settings** -> **Sound** -> **Output & Input** -> **Output**, switch the output device to **GLKVM**.

        ![mac output settings](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/mac_output_settings.png){class="glboxshadow"}

    ??? "Windows"

        On your controlled device, go to **Settings** -> **Sound** -> **Output**, switch the output device to **GLKVM**.

        ![wins output settings 1](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_1.png){class="glboxshadow"}

        ![wins output settings 2](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_2.png){class="glboxshadow"}

        Alternatively, you can click on the sound icon in the bottom right corner of your controlled device, and select the playback device as **GLKVM**.

        ![wins output settings 3](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_3.png){class="glboxshadow"}

6. Check the graphics card driver of the controlled device. If the controlled computer does not have a graphics card driver, it will not be able to output audio, thus the sound cannot be heard at the controlling end.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.