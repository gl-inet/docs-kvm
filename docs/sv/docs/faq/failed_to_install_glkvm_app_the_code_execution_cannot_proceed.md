# Det går inte att installera GLKVM-appen i Windows: "The code execution cannot proceed" {#failed-to-install-glkvm-app-on-windows-the-code-execution-cannot-proceed}

När du installerar GLKVM-appen i Windows kan följande fel uppstå: "The code execution cannot proceed because VCRUNTIME140_1.dll was not found".

![Systemfel](https://static.gl-inet.com/docs/kvm/faq/failed_to_install_glkvm_app/system_error.png){class="glboxshadow"}

Felet beror på att beroenden för Visual C++-körmiljön saknas. Appen kräver vissa DLL-filer som tillhandahålls av paketet Visual C++ Redistributable.

Gör så här:

1. Ladda ned den senaste versionen av Visual C++ Redistributable för Visual Studio från Microsofts officiella webbplats [här](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170){target="_blank"}.

2. Installera paketet och starta om datorn.

    Inaktivera antivirusprogramvaran tillfälligt, eftersom vissa säkerhetsverktyg felaktigt kan blockera installationsfiler.

    ??? "Hur kontrollerar jag att beroendena för Visual C++ är korrekt installerade?"

        1. Gå till Kontrollpanelen > Program > Program och funktioner i Windows.

        2. Leta efter poster som "Microsoft Visual C++ 2015-2022 Redistributable" (x64/x86). Om de saknas installerar du dem via länken ovan.

3. Kör installationsprogrammet för GLKVM-appen igen.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
