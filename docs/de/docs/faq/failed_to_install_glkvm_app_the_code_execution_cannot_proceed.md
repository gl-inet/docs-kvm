# Installation der GLKVM App unter Windows fehlgeschlagen: "The code execution cannot proceed"

Bei der Installation der GLKVM App unter Windows kann folgender Fehler auftreten: "The code execution cannot proceed because VCRUNTIME140_1.dll was not found".

![system error](https://static.gl-inet.com/docs/kvm/faq/failed_to_install_glkvm_app/system_error.png){class="glboxshadow"}

Dieser Fehler entsteht durch fehlende Visual-C++-Laufzeitabhängigkeiten. Die App benötigt bestimmte DLL-Dateien, die vom Visual C++ Redistributable-Paket bereitgestellt werden.

Gehen Sie wie folgt vor:

1. Laden Sie das neueste Visual C++ Redistributable for Visual Studio von der offiziellen Microsoft-Website [hier](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170){target="_blank"} herunter.

2. Installieren Sie das Paket und starten Sie Ihren Computer neu.

    Deaktivieren Sie vorübergehend die Antivirensoftware, da manche Sicherheitsprogramme Installationsdateien fälschlicherweise blockieren können.

    ??? "How do I verify if Visual C++ dependencies are installed correctly?"

        1. Gehen Sie unter Windows zu Control Panel > Programs > Programs and Features.

        2. Suchen Sie nach Einträgen wie "Microsoft Visual C++ 2015-2022 Redistributable" (x64/x86). Falls diese fehlen, installieren Sie sie über den oben angegebenen Link.

3. Führen Sie das Installationsprogramm der GLKVM App erneut aus.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
