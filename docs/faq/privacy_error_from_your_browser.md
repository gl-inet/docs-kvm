# Privacy error when accessing KVM via browser

When accessing the GL.iNet KVM via browser, you may encounter a browser alert: **Your connection isn't private**.

![privacy error](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

This is a standard security warning that browsers issue when they detect a website lacking an SSL/TLS certificate, as HTTPS connections rely on certificates to verify server identity and encrypt data.

## Why do I get this warning?

In the example above, **192.168.8.11** is the KVM local IP address dynamically assigned by the upper router via DHCP. 

!!! Note

    If the gateway of your router that your GL.iNet KVM is connected to is "192.168.x.1" (where x is typically 0, 1, or 8 in private networks), the local IP of your KVM should be "192.168.x.y" (where y is a valid host address in the subnet).

This local IP address is used to access the GL.iNet KVM console, instead of a public website.

However, browsers usually do not distinguish between local console and normal public websites; they treat all IP addresses as websites and expect HTTPS connections to be secured by SSL/TLS certificates.

A genuinely secure website uses an SSL/TLS certificate, so when browsers access a local console (which does not have a certificate), they trigger a security alert due to the missing certificate.

## What can I do with this alert?

Click **Advanced** and **Continue to "192.168.8.11"**.

![Continue to 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

Then you will be redirected to the GL.iNet KVM console.

![local access to kvm admin](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## Can I use my own certificate?

Yes. You may install and use your own SSL/TLS certificate on the KVM. Follow the steps below.

1. Apply for an SSL/TLS certificate or use a self-signed one.

2. Log in to your KVM console. Click the shield icon in the upper right corner to go to **Security** -> **TLS Certificate**.

    ![custom cert 1](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert1.png){class="glboxshadow"}

    In the pop-up window, select **Custom Certificate**, then upload your certificate file and private key. This feature has been available since firmware v1.8.0.

    ![custom cert 2](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert2.png){class="glboxshadow"}

    Alternatively, you can edit configuration files on the KVM via SSH terminal or WinSCP. The auto-generated certificate and key are stored in the following path:

    `/etc/kvmd/user/ssl`

    Replace them with your new SSL certificate and private key.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.