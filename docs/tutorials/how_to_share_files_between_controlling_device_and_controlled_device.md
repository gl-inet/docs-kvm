# How to share files between controlling and controlled devices

GL.iNet KVM supports Virtual Media, allowing you to share and manage files between the controlling device and the controlled device.

Take Comet (GL-RM1) as an example. 

Log in to Comet and navigate to **Virtual Media**.

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/virtual_media.png){class="glboxshadow"}

Drag or click the box to upload files from your controlling device, or upload from URL. 

As an example, two images have been uploaded from the controlling device to the Comet here.

![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/upload_files_example.png){class="glboxshadow"}

Click **Mount To Remote**, and you will see two options: **File Sharing** and **Image Mounting**. 

![mount to remote](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/mount_to_remote.jpg){class="glboxshadow"}
    
Click **File Sharing**. A window will pop up in the control panel to indicate file sharing steps. Click "Don't remind me" to hide it.
    
![file sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/file_sharing_1.png){class="glboxshadow"}

Now the Comet is emulating a read-write USB drive on the controlled device.

Turn to the Comet's control panel and access the controlled device. Go to **This PC** and find a Drive named **GLKVM**. Now you can view, move or delete the files in this drive.

![file sharing 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/ui-screenshot-no-fw/file_sharing_2.png){class="glboxshadow"}

If you want to share files from the controlled device to the controlling device, simply place the files into this drive. Those files will be displayed under the Virtual Media in the Comet's control panel after you stop the file sharing.

For example, a PDF file named "gl-rm1_datasheet" has been placed into this drive. In the Comet's control panel, go to Virtual Media and click **Stop Sharing**.

![file sharing 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/file_sharing_3.png){class="glboxshadow"}

This file will be displayed under the Virtual Media, as shown below. Now you can download this file from Comet to your controlling device.

![file sharing 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/file_sharing_4.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.