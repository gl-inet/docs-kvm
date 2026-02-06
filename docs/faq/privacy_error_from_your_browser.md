# Privacy error when accessing KVM via browser

When accessing the GL.iNet KVM via browser, you may encounter a browser alert: **Your connection isn't private**.

![privacy error](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

This is a standard security warning that browsers issue when they detect a website lacking an SSL/TLS certificate, as HTTPS connections rely on certificates to verify server identity and encrypt data.

## Why do I get this warning?

In the example above, **192.168.8.11** is the KVM's local IP address dynamically assigned by the upper router via DHCP. 

!!! Note

    If the gateway of your router that your GL.iNet KVM is connected to is "192.168.x.1" (where x is typically 0, 1, or 8 in private networks), the local IP of your KVM should be "192.168.x.y" (where y is a valid host address in the subnet).

This local IP address is used to access the GL.iNet KVM console, instead of a public website.

However, browsers usually do not distinguish between local console and normal public websites; they treat all IP addresses as websites and expect HTTPS connections to be secured by SSL/TLS certificates.

A genuinely secure website uses an SSL/TLS certificate, so when browsers access a local console (which does not have a certificate), they trigger a security alert due to the missing certificate.

## What can I do with this alert?

Please click **Advanced** and **Continue to "192.168.8.11"**.

![Continue to 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

Then you will be re-directed to the GL.iNet KVM console.

![local access to kvm admin](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## Can I use an SSL certificate in the KVM?

Yes, you can use your SSL certificate in the GL.iNet KVM.

Firstly, please apply for an SSL cert or use a self-signed SSL cert. 

Secondly, access KVM's terminal or use WinSCP (recommended) to modify files on your KVM. The automatically generated certificate and key are storaged in this path: `/etc/kvmd/nginx/ssl ` (which has been changed to `/etc/kvmd/user/ssl` since firmware v1.4.0). 

Please replace them with the new SSL certificate and key.

**Note**: 

1. Prior to firmware v1.4.0, the KVM certificate is automatically regenerated after each firmware upgrade, and uploaded SSL certificates are not backed up.

    If necessary, please re-upload the SSL certificate to replace the auto-generated one after a firmware upgrade.

2. Starting from firmware v1.4.0, firmware upgrades will not cause the KVM certificate to be regenerated, unless the firmware is manually reset.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.