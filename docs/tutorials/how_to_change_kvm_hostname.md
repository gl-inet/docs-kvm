# How to change KVM hostname

The default hostname of GL.iNet KVM is **glkvm**, which means you can locally access it via the domain `glkvm.local` when connected to the same network.

If you want to change the hostname, there are two methods: through the settings on the web control panel or via terminal commands. 

## Method 1. Control Panel Settings

1. Log in to your KVM, navigate to **Settings** -> **Network** -> **Hostname**, and click **Modify**. 

    ![hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings-hostname.png){class="glboxshadow"}

2. Customize hostname and click **Apply**.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify-hostname.png){class="glboxshadow"}

## Method 2. Terminal Commands

1. Log in to your KVM, navigate to Toolbox -> Terminal, and click **Access**. 

    ![access terminal](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_terminal.png){class="glboxshadow"}

2. In the terminal, input the following command and press Enter (replace "example" with your desired hostname). Then your KVM will restart.

    `echo example > /etc/hostname && reboot`

    ![input command](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/input_command.png){class="glboxshadow"}

3. Wait for it to restart. Then you will be able to access your KVM using the new hostname.

    ![access new hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_new_hostname.png){class="glboxshadow"}

    If you forget the hostname or need to check if the change has taken effect, enter the following command in the terminal to view the current hostname.

    `cat /etc/hostname`

    ![verify hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/verify_hostname.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.