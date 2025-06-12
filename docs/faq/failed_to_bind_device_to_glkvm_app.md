# What should I do if I failed to bind device to the GLKVM app?

To remotely access a controlled device via the GLKVM app, you must first bind your GL.iNet KVM device (e.g., Comet) to the app. However, binding failures may occur during this process.

![binding failed](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_windows.png){class="glboxshadow"}

Here are some suggestions for troubleshooting.

1. Check the LED and ensure your KVM device is connected to Internet.

    Take Comet (GL-RM1) as an exmaple. A solid while LED indicates stable Internet connection.

2. Ensure the Cloud service is enabled. 

    The Cloud service is enabled by default, but if you disable it manually in the GLKVM app, device re-binding will fail. In that case, please access your KVM device locally via web browser and re-enable the Cloud service.

3. Ensure you install the correct [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} for your operating system.

If problem persists, please contact us at [support@gl-inet.com](mailto:support@glinet.biz) and provide Device Model, Firmware version and MAC address.
