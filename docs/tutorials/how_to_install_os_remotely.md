# How to install an OS on the controlled computer remotely using Virtual Media?

This tutorial will introduce how to remotely install an operating system on the controlled computer using Virtual Media, a feature of GL.iNet KVM.

1. Log in to your GL.iNet KVM, and navigate to **Virtual Media**.

2. Upload the OS ISO file to Virtual Media.

    ![upload file](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/upload_file.png){class="glboxshadow"}

3. After uploaded, click **Mount To Remote** and select **Image mounting** to mount the ISO image.

    ![image mounting](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-1.png){class="glboxshadow"}

    Select the image file and click **Mount Image**.

    ![image mounting](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-2.png){class="glboxshadow"}

4. Reboot the remotely controlled computer and **press the appropriate key immediately** (e.g., DEL in this example) during boot to enter BIOS/UEFI.

    ![enter bios](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/enter_bios.png){class="glboxshadow"}

5. In the boot menu, set **"Glinet Flash Drive 1.00"** as Boot Option #1.

    ![set boot option priority](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/set_boot_option_priority.png){class="glboxshadow"}

6. Save and exit BIOS. The system will then boot from the mounted ISO to begin OS installation.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.