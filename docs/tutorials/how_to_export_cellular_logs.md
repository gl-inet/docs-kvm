# How to export cellular logs?

This tutorial introduces the steps to export Cellular-related logs from KVM device for troubleshooting.

The following steps take Comet 5G (GL-RM10RC) as an example.

1. Log in to the KVM console, navigate to **Virtual Media** and make sure it is enabled.

2. Navigate to **Toolbox** -> **Terminal**. Click **Access** to enter the KVM Terminal.

    ![access terminal](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/access_terminal.png){class="glboxshadow"}

3. In the Terminal window, execute the following command to launch the QLog program.

    ```
    QLog_1.5.22 -s /userdata/media/ -f /etc/HN_default.cfg & ubus call modem at '{"AT":"AT+QCFG=\"DBGCTL\",0"}'
    ```

    ![qlog 1](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog1.jpg){class="glboxshadow"}

    The page will then display the initialization related to QLog startup, followed by the real-time data statistics (e.g., data volume received and time elapsed), as shown below.

    ![qlog 2](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog2.jpg){class="glboxshadow"}

4. Press Enter key and execute the following commands in sequence to restart the modem, ensuring the device captures complete startup process logs.

    ```
    ubus call modem at '{"AT":"AT+CFUN=0"}'
    ```

    ```
    ubus call modem at '{"AT":"AT+CFUN=1"}'
    ```

    ![qlog 3](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog3.png){class="glboxshadow"}

5. Wait for 3-5 minutes to ensure sufficient log data is collected. After that, enter the following command to stop the QLog process.

    ```
    ps | grep QLog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![qlog 4](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog4.png){class="glboxshadow"}

6. Export Logs.

    Cellular modem logs are saved in the **/userdata/media/** directory with the filename suffix `xxx.qmdl`.

    Log in to the KVM console, navigate to **Virtual Media** and locate the target file(s) with the suffix `xxx.qmdl`. Download these files and share them with GL.iNet technical support.

    ![qlog 5](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog5.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.