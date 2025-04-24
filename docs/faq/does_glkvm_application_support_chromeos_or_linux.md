# Does GLKVM application support ChromeOS/Linux?

The GLKVM application is designed for the controlling device (i.e. the Host). Currently the GLKVM app does not support installation on Chrome or Linux OS, so if your controlling device is running Chrome/Linux OS, the GLKVM app cannot be installed, thus remote access to controlled device via GLKVM app is not supported. 

However, you may use Tailscale to achieve remote access, which is integrated in Comet (GL-RM1). In this way, you can directly access Comet by typing its Tailscale virtual IP into a browser, without installing GLKVM app.

Alternatively, you can locally access the controlled device through a web browser in the local LAN network. 

As to the remotely-controlled device, no need to install any software on it. That is to say, it can be Windows, macOS, ChromeOS, Linux, etc.
