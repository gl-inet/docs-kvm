# How to share files between controlling and controlled devices?

GL.iNet KVM emulates a read-write USB drive, allowing you to share and manage files between the controlling device and the controlled device.

In the following steps, we will take Comet (GL-RM1) as an example. 

**To share files from the controlling device to the controlled one, follow the steps below.**

1. On the console, navigate to **Virtual Media**. Drag or click the box to upload files from your controlling device or upload from URL. 

    Once uploaded, the files will be displayed as follows.

    ![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/control_panel/v1.7/vm-upload-file.png){class="glboxshadow"}

2. Click **Mount To Remote** -> **File Sharing**. 

    ![file sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/control_panel/v1.7/vm-file-sharing.png){class="glboxshadow"}

    A window will pop up on the console indicating the file sharing steps, as shown below. 
    
    Now the Comet is emulating a read-write USB drive on the controlled device.
    
    ![file sharing tips](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/control_panel/v1.7/vm-sharing-tips.png){class="glboxshadow"}

3. In the Comet's control screen, go to **This PC** of your controlled device. 

    ![go to this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/control_panel/v1.7/vm-thispc.png){class="glboxshadow"}

4. Find a disk named **GLKVM**, and you will see the files you uploaded previously from the controlling device to Comet have been shared to the controlled device.

    Now you can view, move or delete the files in this disk.

    ![glkvm disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/control_panel/v1.7/vm-glkvm-disk.png){class="glboxshadow"}

5. If you want to stop sharing, click **Virtual Media** in the toolbar and click **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/control_panel/v1.7/vm-stop-sharing1.png){class="glboxshadow"}

---

**To share files from the controlled device to the controlling one, follow the steps below.**

1. Save or copy the files you want to share into the disk **GLKVM**. 

    For example, a PDF file named "gl-rm10_datasheet" has been copied from the controlled device's Desktop into the disk **GLKVM**. 

    ![copy file to disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/control_panel/v1.7/vm-copy-file.png){class="glboxshadow"}
    
2. Turn to the Comet's console, click **Virtual Media** in the toolbar and click **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/control_panel/v1.7/vm-stop-sharing2.png){class="glboxshadow"}
    
3. Then this file will be displayed under the Virtual Media, as shown below. Now you can download this file from Comet to your controlling device.

    ![file shared](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/control_panel/v1.7/vm-file-shared.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.