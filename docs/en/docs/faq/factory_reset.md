# How do I factory reset my GL.iNet KVM?

## Method 1: Use the physical reset button

Make sure your KVM is powered on and has finished starting up.

Press and hold the physical RESET/SWITCH button for **8 seconds**, then release it. If your KVM has a reset pinhole, use a pin to press and hold the button inside the pinhole for 8 seconds, then release it. On Comet X (GL-RM4PE), use the switch button on the front panel.

Wait for the KVM to restart automatically. **Do not disconnect power during the reset**.

Do not hold the reset button while powering on the KVM. Do not use the reset button on the connected computer or the ATX board.

## Method 2: Use the local web interface

Connect your computer and the KVM to the same isolated local network. Open the KVM's local IP address in a browser and sign in. See [How to access the KVM locally via a web browser](local_access_via_browser.md).

In the KVM console, go to **Settings** -> **Preferences** -> **System** -> **Reset KVM**.

Confirm the reset and wait for the KVM to restart automatically. If you do not see Reset KVM, use Method 1.

## After the reset

A factory reset clears the KVM's custom settings. The KVM's local IP address may change after it restarts. Open the local web interface again, follow the initial setup prompts to set an administrator password, and reconfigure the settings you need manually.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.