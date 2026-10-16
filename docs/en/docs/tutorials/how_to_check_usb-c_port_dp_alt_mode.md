# How to check if your device's USB-C port supports DP Alt Mode

## What is DP Alt Mode

DP Alt Mode (or DisplayPort Alternate Mode) is a feature built into certain USB-C ports that enables them to transmit a high-quality video signal — in addition to the data and power they normally handle.

In plain terms: it allows a single USB-C cable to transmit video from your phone, tablet, or laptop straight to a monitor, TV, or projector — no special adapter or docking station required. Without DP Alt Mode, the port can only transfer data and supply power; it cannot output video to an external display.

## Why it matters

DP Alt Mode matters for **Comet Q**, as Comet Q relies on it to receive video from your device. The controlled device must support native video output through its USB-C port. Note that a DisplayLink adapter may not add this capability for a direct connection to Comet Q.

Not every USB-C port is created equal. Some only carry data and power; others can also output video. The shape of the connector is the same, but the capabilities behind it are not. Two USB-C ports can look identical and behave very differently — which is why it pays to check before buying any USB-C display accessory.

## General methods to verify DP Alt Mode

1. **Check the spec sheet**.

    Look up your exact model on the manufacturer's website. Search for keywords such as DisplayPort, DP Alt Mode, video output, or Thunderbolt.

2. **Look for port markings**.

    A D-shaped DisplayPort logo or Thunderbolt lightning icon next to the USB-C port indicates video output capability.

3. **Check system settings**.

    System settings can help identify a connected display, but they do not always establish whether a specific USB-C port supports native DP Alt Mode. Combine these checks with the manufacturer's specifications and a direct connection test. See platform-specific instructions below.

    - [How to check on Windows](#how-to-check-on-windows)
    - [How to check on Mac](#how-to-check-on-mac)
    - [How to check on Android](#how-to-check-on-android)
    - [How to check on iPhone & iPad](#how-to-check-on-iphone-and-ipad)
    - [Handhelds, tablets & other devices](#handhelds-tablets-and-other-devices)

4. **Perform a quick test**.

    Connect your device to a monitor or TV using a USB-C to HDMI / DisplayPort cable or adapter that explicitly requires DP Alt Mode. If the screen mirrors or extends your display, native video output is working on that port. Do not use a DisplayLink adapter for this test.

---

## How to check on Windows

1. Press `Win + X` and open **Device Manager**.
2. Look for entries mentioning *"USB4"* or *"Thunderbolt"*. These can help identify the hardware, but Device Manager alone does not confirm DP Alt Mode support on a specific port.
3. Check your laptop's user manual or the manufacturer's product page for the exact port — search for *"DisplayPort over USB-C"* or *"DP Alt Mode"*.
4. Connect Comet Q directly, or connect a display using an adapter that explicitly requires DP Alt Mode. Open **Settings** > **System** > **Display** > **Multiple displays** to check whether the display is detected.

**Note**:

1. **DisplayLink is not proof of DP Alt Mode support.** DisplayLink transmits video over USB data and can also work through USB-A. A DisplayLink entry in Device Manager, or a working display connected through a DisplayLink dock, does not establish native USB-C video output. See [Synaptics: USB-C with DisplayLink](https://www.synaptics.com/products/displaylink-graphics/usb-c){target="_blank"}.

2. If your laptop has multiple USB-C ports, only some may support video output. Check each port individually.

## How to check on Mac

1. Click the **Apple menu** > **About This Mac** > **More Info**.
2. Scroll down and click **System Report**.
3. Under **Hardware**, select **Thunderbolt / USB4** or **USB**.
4. Any USB-C port listed under Thunderbolt / USB4 supports DisplayPort Alt Mode by default.

**Tip**: All modern Macs with USB-C / Thunderbolt ports support DisplayPort Alt Mode out of the box. 

!!! note "Here are the supported models"

    - MacBook Neo (A18 Pro)
    - MacBook Air
        - MacBook Air 13-in. (M5)
        - MacBook Air 15-in. (M5)
        - MacBook Air 13-in. (M4)
        - MacBook Air 13-in. (M3)
        - MacBook Air 13-in. (M2)
        - MacBook Air 13-in. (M1, 2020)
        - MacBook Air 15-in. (M4)
        - MacBook Air 15-in. (M3)
        - MacBook Air 15-in. (M2, 2023)
        - MacBook Air (Intel, 2020)
    - MacBook Pro
        - MacBook Pro 14-in. (M5)
        - MacBook Pro 14-in. (M5 Pro)
        - MacBook Pro 14-in. (M5 Max)
        - MacBook Pro 16-in. (M5 Pro)
        - MacBook Pro 16-in. (M5 Max)
        - MacBook Pro 13-in. (M2, 2022)
        - MacBook Pro 13-in. (M1, 2020)
        - MacBook Pro 13-in. (Intel, two ports, 2020)
        - MacBook Pro 13-in. (Intel, four ports, 2020)
        - MacBook Pro 14-in. (M4 Max)
        - MacBook Pro 14-in. (M4 Pro)
        - MacBook Pro 14-in. (M4)
        - MacBook Pro 14-in. (M3)
        - MacBook Pro 14-in. (M3 Pro or M3 Max)
        - MacBook Pro 14-in. (M2 Pro or M2 Max, 2023)
        - MacBook Pro 14-in. (M1 Pro or M1 Max, 2021)
        - MacBook Pro 16-in. (M4 Max)
        - MacBook Pro 16-in. (M4 Pro)
        - MacBook Pro 16-in. (M3 Pro or M3 Max)
        - MacBook Pro 16-in. (M2 Pro or M2 Max, 2023)
        - MacBook Pro 16-in. (M1 Pro or M1 Max, 2021)
        - MacBook Pro 16-in. (Intel, 2019)
    - iMac
        - iMac (M4, two ports)
        - iMac (M4, four ports)
        - iMac (M3, two ports)
        - iMac (M3, four ports)
        - iMac 21.5-in. (Intel, 2019)
        - iMac 21.5-in. (Intel, 2017)
        - iMac 24-in. (M1, two ports, 2021)
        - iMac 24-in. (M1, four ports, 2021)
        - iMac27-in. (Intel,2020)
        - iMac Pro (Intel, 2017)
    - Mac mini
        - Mac mini (M4)
        - Mac mini (M4 Pro)
        - Mac mini (M2 or M2 Pro)
        - Mac mini (M1, 2020)
        - Mac mini (Intel, 2018)
    - Mac Studio
        - Mac Studio (M4 Max)
        - Mac Studio (M3 UIitra)
        - Mac Studio (M2 Max or M2 UItra)
        - Mac Studio (M1 Max or M1 UItra, 2022)
    - Mac Pro
        - Mac Pro (M2 UItra)
        - Mac Pro (Intel, 2019)

## How to check on Android

1. Open your phone's **Settings** and search for *"display"*, *"HDMI"*, or *"desktop mode"*.
2. Look for features such as **Samsung DeX**, **Motorola Ready For**, **Huawei EasyProjection**, or *"External display"*. Check the manufacturer's documentation to confirm that the exact model supports a **wired USB-C display connection**; a wireless display feature alone is not proof of DP Alt Mode support.
3. If your phone supports it, you'll typically see a notification like *"External display connected"* when you plug into a monitor.
4. Confirm video output with a direct connection to Comet Q or a display using an adapter that requires DP Alt Mode. USB information apps alone cannot reliably establish native video output support.

**Note**: Many budget Android phones omit DP Alt Mode even though they have USB-C. Always confirm before purchasing Comet Q.

!!! note "Examples of Samsung devices with wired display output"

    The Samsung entries below were checked against [Samsung's DeX compatibility information](https://www.samsung.com/us/support/answer/ANS10001955/){target="_blank"}.

    - Galaxy A90 5G
    - Galaxy Book
    - Galaxy Fold
    - Galaxy Note
        - Galaxy Note 8
        - Galaxy Note 9
        - Galaxy Note 10 range
        - Galaxy Note20 range
    - Galaxy S
        - Galaxy Tab S7 / 7+
        - Galaxy Tab S8 / 8+ / S8 Ultra
        - Galaxy S8 and S8+
        - Galaxy S9 and S9+
        - Galaxy S10 range
        - Galaxy S20 range
        - Galaxy S21 range
        - Galaxy S22 range
        - Galaxy S23 range
        - Galaxy S24 range
        - Galaxy S25 range
    - Galaxy Tab
        - Galaxy Tab S4
        - Galaxy Tab S5e
        - Galaxy Tab S6
    - Galaxy Z
        - Galaxy Z Flip7
        - Galaxy Z Flip8
        - Galaxy Z Fold2
        - Galaxy Z Fold3
        - Galaxy Z Fold4
        - Galaxy Z Fold7

## How to check on iPhone and iPad

1. iPhone 15 series and newer (except iPhone 16e and iPhone 17e) support DisplayPort Alt Mode through their USB-C port. Check [Apple's display connection documentation](https://support.apple.com/en-ie/105099#displays){target="_blank"} for your exact model.
2. iPhone 14 and earlier use Lightning and are not compatible.
3. All iPad models with USB-C (iPad Pro, iPad Air 4th gen and later, iPad mini 6th gen and later, iPad 10th gen and later) support video output.
4. iPads with the older Lightning port are not compatible.

!!! note "Examples of models with USB-C video output"

    The iPhone entries below were checked against [Apple's external-display documentation](https://support.apple.com/en-ie/105099#displays){target="_blank"}.

    - iPhone
        - iPhone 18 Pro
        - iPhone 18 Pro Max
        - iPhone 17 Pro
        - iPhone 17 Pro Max
        - iPhone 17
        - iPhone 16 Pro
        - iPhone 16 Pro Max
        - iPhone 16
        - iPhone 16 Plus
        - iPhone 15 Pro
        - iPhone 15 Pro Max
        - iPhone 15
        - iPhone 15 Plus
    - iPad
        - iPad (A16)
        - iPad (10th generation)
    - iPad mini
        - iPad mini (6th generation)
        - iPad mini (A17 Pro)
    - iPad Air
        - iPad Air (5th generation)
        - iPad Air (4th generation)
        - iPad Air 11-inch (M4)
        - iPad Air 11-inch (M3)
        - iPad Air 11-inch (M2)
        - iPad Air 13-inch (M4)
        - iPad Air 13‑inch (M3)
        - iPad Air 13-inch (M2)
    - iPad Pro
        - iPad Pro 11‑inch (M5)
        - iPad Pro 11‑inch (M4)
        - iPad Pro 11-inch (4th generation)
        - iPad Pro 11-inch (3rd generation)
        - iPad Pro 12.9-inch (5th generation)
        - iPad Pro 12.9-inch (6th generation)
        - iPad Pro 13‑inch (M5)
        - iPad Pro 13‑inch (M4)

## Handhelds, tablets and other devices

1. **Steam Deck**, **ROG Ally**, **Lenovo Legion Go** — all support DP Alt Mode.
2. **Most Windows tablets** with USB-C (Surface Pro 8 and newer, etc.) — supported.
3. For anything else, check the official spec page and search for the keywords *"DisplayPort"*, *"Alt Mode"*, *"video output"*, or *"Thunderbolt"*.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.