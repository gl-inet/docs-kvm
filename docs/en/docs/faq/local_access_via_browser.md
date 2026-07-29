# How to access the KVM locally via browser

Before you begin, please ensure the controlling device and the KVM are on the same LAN.

There are two ways to access the KVM locally via a web browser: using a domain name or an IP address.

## Local access via Domain

1. Open a browser on the controlling device. Chrome or Edge is recommended for better compatibility.

2. Enter `glkvm.local` in the address bar. You will be directed to the GLKVM login page. Enter your admin password.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    You can now access your KVM console locally, and thus access the controlled device.

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

## Local access via IP address

Find the IP address of your KVM in the upstream network (e.g., your router), and enter this IP address in the browser. You will then be able to access your KVM locally, thus access the controlled device.

Take **GL-AXT1800** (the router) and **GL-RM1 Comet** (the KVM) as an example: Comet is connected to the LAN port of GL-AXT1800 router via an Ethernet cable. The controlled device is connected to Comet correctly via HD cable and USB cable.

Follow the steps below to access the KVM console.

1. Log in to the GL-AXT1800 web admin panel. This router needs to be configured for Internet access.

    ![log in router](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/log_in_router.png){class="glboxshadow"}

2. On the router's admin panel, go to **Client** and find the Comet's IP address in the Client list. As shown below, the Comet's IP is **192.168.8.197**.

    ![find glkvm ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

3. Open a new tab in the browser, enter Comet's IP **192.168.8.197** in the address bar. 

    You will be directed to the GLKVM login page. Enter your admin password.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    You can now access your KVM console locally, and thus access the controlled device.

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
