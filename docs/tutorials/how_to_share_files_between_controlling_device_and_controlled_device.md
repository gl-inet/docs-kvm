# How to share files between controlling and controlled devices

GL.iNet KVM supports Virtual Media, allowing you to share and manage files between the controlling device and the controlled device.

In the following steps, we will take Comet (GL-RM1) as an example. 

**To share files from the controlling device to the controlled one, follow the steps below.**

1. In the control panel, navigate to **Virtual Media**. Drag or click the box to upload files from your controlling device, or upload from URL. 

    ![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/virtual_media.png){class="glboxshadow"}

    Once uploaded, the files will be displayed as follows.

    ![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/virtual_media_upload.png){class="glboxshadow"}

2. Click **Mount To Remote** -> **File Sharing**. 

    ![file sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/file_sharing.png){class="glboxshadow"}

    A window will pop up in the control panel to indicate file sharing steps, as shown below.
    
    ![file sharing apply](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/file_sharing_apply.png){class="glboxshadow"}

    Now the Comet is emulating a read-write USB drive on the controlled device.

3. In the Comet's control panel, access your controlled device and go to **This PC**. 

    ![file sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/file_sharing_1.png){class="glboxshadow"}

4. Find a Drive named **GLKVM**, and you will see the files you uploaded previously from the controlling device to Comet have been shared to the controlled device. Now you can view, move or delete the files in this drive.

    ![file sharing 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/file_sharing_2.png){class="glboxshadow"}

---

**To share files from the controlled device to the controlling one, follow the steps below.**

1. Copy the files you want to share into the drive **GLKVM**. 

    For example, a PDF file named "gl-rm1_datasheet" has been copied from the controlled device's Desktop into the drive **GLKVM**. 

    ![file sharing 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/file_sharing_3.png){class="glboxshadow"}
    
2. Turn to the Comet's control panel -> **Virtual Media**, click **Stop Sharing**.

    ![file sharing 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/file_sharing_4.png){class="glboxshadow"}
    
3. Then this file will be displayed under the Virtual Media, as shown below. Now you can download this file from Comet to your controlling device.

    ![file sharing 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/file_sharing_5.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.