# How to check if your device's USB-C port supports DP Alt Mode?

## What is DP Alt Mode

DP Alt Mode (or DisplayPort Alternate Mode) is a feature built into certain USB-C ports that enables them to transmit a high-quality video signal — in addition to the data and power they normally handle.

In plain terms: it allows a single USB-C cable to transmit video from your phone, tablet, or laptop straight to a monitor, TV, or projector — no special adapter or docking station required. Without DP Alt Mode, the port can only transfer data and supply power; it cannot output video to an external display.

## Why it matters

DP Alt Mode matters for **Comet Q**, as Comet Q relies on it to receive video from your device. If your USB-C port supports it, Comet Q just works — plug and play. If not, no external display adapter can resolve this limitation.

Not every USB-C port is created equal. Some only carry data and power; others can also output video. The shape of the connector is the same, but the capabilities behind it are not. Two USB-C ports can look identical and behave very differently — which is why it pays to check before buying any USB-C display accessory.

## General methods to verify DP Alt Mode

1. **Check the spec sheet**.

    Look up your exact model on the manufacturer's website. Search for keywords such as DisplayPort, DP Alt Mode, video output, or Thunderbolt.

2. **Look for port markings**.

    A D-shaped DisplayPort logo or Thunderbolt lightning icon next to the USB-C port indicates video output capability.

3. **Check system settings**.

    Your operating system can detect whether the USB-C port supports external display output. See platform-specific instructions below.

    - [How to check on Windows](#how-to-check-on-windows)
    - [How to check on Mac](#how-to-check-on-mac)
    - [How to check on Android](#how-to-check-on-android)
    - [How to check on iPhone & iPad](#how-to-check-on-iphone-and-ipad)
    - [Handhelds, tablets & other devices](#handhelds-tablets-and-other-devices)

4. **Perform a quick test**.

    Connect your device to a monitor or TV via a USB-C to HDMI / DisplayPort cable. If the screen mirrors or extends your display, DP Alt Mode is functioning properly.

---

## How to check on Windows

1. Press `Win + X` and open **Device Manager**.
2. Expand **Universal Serial Bus controllers** and look for entries that mention *"USB4"*, *"Thunderbolt"*, or *"DisplayLink"*.
3. Alternatively, open **Settings** > **System** > **Display** > **Multiple displays**. With Comet Q (or another display) plugged in, your monitor should appear.
4. You can also check your laptop's user manual or the manufacturer's product page — search for *"DisplayPort over USB-C"* or *"DP Alt Mode"*.

**Note**: If your laptop has multiple USB-C ports, only some may support video output. Check each port individually.

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
2. Look for features such as **Samsung DeX**, **Motorola Ready For**, **Huawei EasyProjection**, or *"External display"*. If any are present, your device's USB-C port supports DP Alt Mode.
3. If your phone supports it, you'll typically see a notification like *"External display connected"* when you plug into a monitor.
4. You can also install a free app such as *USB Device Info* to inspect port capabilities.

**Note**: Many budget Android phones omit DP Alt Mode even though they have USB-C. Always confirm before purchasing Comet Q.

!!! note "Here are the supported models, using Samsung as example:"

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
        - Galaxy Z Flip
        - Galaxy Z Fold2
        - Galaxy Z Fold3
        - Galaxy Z Fold4

## How to check on iPhone and iPad

1. iPhone 15 series and newer all support DisplayPort Alt Mode through their USB-C port.
2. iPhone 14 and earlier use Lightning and are not compatible.
3. All iPad models with USB-C (iPad Pro, iPad Air 4th gen and later, iPad mini 6th gen and later, iPad 10th gen and later) support video output.
4. iPads with the older Lightning port are not compatible.

!!! note "Here are the supported models"

    - iPhone
        - iPhone 17 Pro
        - iPhone 17 Pro Max
        - iPhone 17
        - iPhone 16 Pro
        - iPhone 16 Pro Max
        - iPhone 16
        - iPhone 16 Plus
        - iPhone 15 Pro
        - iPhone 15 ProMax
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
2. **Nintendo Switch / Switch 2** — supports DP Alt Mode (this is how the dock outputs to your TV).
3. **Most Windows tablets** with USB-C (Surface Pro 8 and newer, etc.) — supported.
4. For anything else, check the official spec page and search for the keywords *"DisplayPort"*, *"Alt Mode"*, *"video output"*, or *"Thunderbolt"*.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.