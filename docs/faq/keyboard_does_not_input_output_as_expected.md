# What shoud I do if keyboard does not input/output as expected?

If your controlling device and the controlled device are not using the same imput method / keyboard, when you input certain symbols like "!" "@" "#" or letters on the controlling end, the controlled end may not be able to output the same symbols or letters.

## Why does it happen

The KVM is regarded as a keyboard for the controlled device, and the keys you press on the controlling device’s keyboard will be transmitted to KVM according to the corresponding key positions, and then mapped to the controlled device. 

However, if the input method/keyboard of the controlling device is not consistent with that of the controlled device, some symbols/letters will have different positions on the keyboard, resulting in the output by the controlled end being inconsistent with those input on the controlling end.

![US JIS keyboard comparison](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/apple-keyboards-US-JIS.jpg){class="glboxshadow gl-90-desktop"}

## Solutions

You can install input method or keyboard for the corresponding language on the controlled device to achieve consistent key mapping.

??? "Windows"

    1. Go to **Settings** -> **Time & Language** -> **Language** -> **Preferred Language**. Click **Add a language**.

        ![add a language](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/add_language.png){class="glboxshadow"}

    2. Choose a language to install. 

        ![choose a language](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/choose_language.png){class="glboxshadow"}

??? "MacOS"

    1. On your Mac, choose **Apple menu** > **System Settings**, then click **Keyboard** in the sidebar. (You may need to scroll down.)
    
    2. Go to **Text Input**, then click **Edit**.
    
    3. Click the **Add** button, then search for a language. Select one or more input sources for each language you want to use, then click **Add**.
    
    4. To begin writing in another language, select the language you want to use in the Input menu in the menu bar.
    
        You can click **Show Keyboard Viewer** in the Input menu to see the keyboard layout for the language that's currently selected.
        
        After you add an input source, the Input menu is automatically shown in the menu bar. The language of the input source is automatically added to your list of preferred languages in Language & Region settings and your list of Dictation languages (if available) in Keyboard settings. 

    References: [Write in another language on Mac – Apple Support](https://support.apple.com/guide/mac-help/write-in-another-language-on-mac-mchlp1406/mac){target="_blank"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
