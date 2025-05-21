# How to set a static IP for Comet (GL-RM1)

If you need to set a static IP for Comet, but its upstream router cannot allocate a static IP or does not have DHCP, you can customize network parameters on Comet's terminal and set a static IP for it.

1. In the GLKVM app, navigate to Toolbox -> Terminal -> Access Terminal.

    ![toolbox](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/toolbox.png){class="glboxshadow gl-50-desktop"}

    ![access terminal](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/access_terminal.png){class="glboxshadow gl-50-desktop"}

2. Input the commands.

    - **Configure IP**: 
    
        *connmanctl config `connmanctl services |grep ethernet|awk -F' '  '{print $3}'` --ipv4 manual 192.168.113.131 255.255.255.0 192.168.113.1*

        Note: The three values are IP address, subnet mask, and gateway respectively.

    - **Configure DNS**:

        *connmanctl config `connmanctl services |grep ethernet|awk -F' '  '{print $3}'` nameservers 8.8.8.8*

        Note: The above value 8.8.8.8 is the DNS server. 
        
        If multiple DNS servers need to be configured, please separate them with spaces, e.g. 
        
        *connmanctl config `connmanctl services |grep ethernet|awk -F' '  '{print $3}'` nameservers 8.8.8.8 1.1.1.1*

    - **Configure DHCP**:

        *connmanctl config `connmanctl services |grep ethernet|awk -F' '  '{print $3}'` --ipv4 dhcp*

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.