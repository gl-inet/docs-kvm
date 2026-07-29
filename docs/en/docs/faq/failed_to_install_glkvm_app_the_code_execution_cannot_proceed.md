# Failed to install GLKVM app on Windows: "The code execution cannot proceed"

When installing the GLKVM app on Windows, an error may occur: "The code execution cannot proceed because VCRUNTIME140_1.dll was not found".

![system error](https://static.gl-inet.com/docs/kvm/faq/failed_to_install_glkvm_app/system_error.png){class="glboxshadow"}

This error occurs due to missing Visual C++ runtime dependencies. The app requires specific DLL files provided by the Visual C++ Redistributable package.

Follow these steps:

1. Download the latest Visual C++ Redistributable for Visual Studio from the official Microsoft website [here](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170){target="_blank"}.

2. Install the package and restart your computer.

    Temporarily disable antivirus software as some security tools may block installation files incorrectly.

    ??? "How do I verify if Visual C++ dependencies are installed correctly?"

        1. On Windows, go to Control Panel > Programs > Programs and Features.
        
        2. Look for entries like "Microsoft Visual C++ 2015-2022 Redistributable" (x64/x86). If missing, install them via the link above.

3. Re-run the GLKVM app installer.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.