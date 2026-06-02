# How to share files between controlling and controlled devices

GL.iNet KVM emulates a read-write USB drive, allowing you to share and manage files between the controlling device and the controlled device.

In the following steps, we will take Comet (GL-RM1) as an example. 

## Send files to controlled device

To share files from the controlling device to the controlled one, follow the steps below.

1. On the console, navigate to **Virtual Media**. Drag or click the box to upload files from your controlling device or upload from URL. 

    Once uploaded, the files will be displayed as follows.

    ![upload files](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing1.png){class="glboxshadow"}

2. Click **Mount To Remote** -> **File Sharing**. 

    ![file sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing2.png){class="glboxshadow"}

3. A window will pop up on the console indicating the file sharing steps, as shown below. 
    
    ![file sharing tips](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing3.png){class="glboxshadow"}

4. Wait a second, and a drive named **"GLKVM"** will pop up on the screen automatically. The Comet is now emulating a read-write USB drive on the controlled device, and you will then see the files you previously uploaded have been shared to the controlled device. 

    Now you can view, move or delete the files in this drive on the controlled device.

    ![file shared](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing4.png){class="glboxshadow"}
    
    **Tip**: If the drive does not pop up automatically, go to **This PC** of your controlled device.

    ![this pc](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/thispc.png){class="glboxshadow"}

    Find a drive named **"GLKVM"**. Now you can view, move or delete the files in this drive.

5. If you want to stop sharing, click **Virtual Media** in the toolbar and click **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing1.png){class="glboxshadow"}

## Get files from controlled device

To receive files from the controlled device, follow the steps below.

1. On the controlled device, move or copy the files you want to share into the drive **GLKVM**.

    As shown below, a file has been moved from the controlled device's Desktop into the disk **GLKVM**.

    ![copy file to disk](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing5.png){class="glboxshadow"}
    
2. Turn to the Comet's console, click **Virtual Media** in the toolbar and click **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing2.png){class="glboxshadow"}
    
3. This file will then be displayed under the **Virtual Media** as follows. Now you can download this file from Comet to your controlling device.

    ![file shared](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing6.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.