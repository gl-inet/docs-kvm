# Firmware v1.9

This release brings brand-new functional extensions, improved interactivity, enhanced privacy protection and more reliable network connections — all built to deliver a more comprehensive, stable and secure remote KVM experience. [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"}

## Video Display

This firmware introduces **Latency Mode**, which balances input responsiveness and video fluidity. You can configure Latency Mode to either Lowest Latency or Smooth Display to optimize remote control performance.
    
- Lowest Latency: Minimizes input latency for snappier keyboard and mouse feedback.
- Smooth Display: Optimizes visual output to eliminate stuttering and frame drops for steady playback.

## Mouse Control

A new primary mouse button swap option **Primary Button** is added to improve mouse usability. You can set either the left or right button as your primary click to match your personal usage habits.

## Touchscreen

You may customize the KVM's **Screen Display** settings via the touchscreen, including screen lock, wallpaper, time format (24-hour / 12-hour), and date format. This feature is exclusive to touchscreen-equipped models.

Additionally, you can quickly configure overlay tools such as Tailscale and NetBird directly from the touchscreen with just a few taps — functionality unavailable in prior firmware releases.

## Language

Previous firmware versions only supported Chinese and English; this build adds native **Japanese** language support to improve accessibility for Japanese users.

## Extensions

This release integrates [**NetBird**](https://netbird.io/){target="_blank"}, an open-source zero-trust networking platform for building secure private home and business networks. Built on WireGuard®, this overlay solution enables secure remote access to your KVM from anywhere over NetBird virtual networks.
See [here](../faq/remote_access_via_netbird.md){target="_blank"} for setup instructions.

## Other Enhancements

- Beta Firmware Program: Users may opt into the beta program to test pre-release features.

- Text Recognition: Powered by Optical Character Recognition (OCR), this tool lets you capture text from any selected area on the remote display. Supported languages include Chinese, English, and Chinese-English bilingual mode.

- City-Based Timezone: Set your timezone by selecting a target city.

- Login Session Security: Login tokens now expire 12 hours after session termination (tokens were previously permanent).

- System Log Security: Sensitive data masking has been implemented for all system logs.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.