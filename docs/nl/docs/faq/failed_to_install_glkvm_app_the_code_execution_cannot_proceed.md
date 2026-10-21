# Installatie van de GLKVM-app op Windows mislukt: "The code execution cannot proceed" {#failed-to-install-glkvm-app-on-windows-the-code-execution-cannot-proceed}

Bij het installeren van de GLKVM-app op Windows kan de volgende fout optreden: "The code execution cannot proceed because VCRUNTIME140_1.dll was not found".

![Systeemfout](https://static.gl-inet.com/docs/kvm/faq/failed_to_install_glkvm_app/system_error.png){class="glboxshadow"}

Deze fout treedt op doordat runtime-afhankelijkheden van Visual C++ ontbreken. De app heeft specifieke DLL-bestanden nodig uit het pakket Visual C++ Redistributable.

Volg deze stappen:

1. Download de nieuwste Visual C++ Redistributable voor Visual Studio [hier](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170){target="_blank"} van de officiële website van Microsoft.

2. Installeer het pakket en start uw computer opnieuw op.

    Schakel antivirussoftware tijdelijk uit, omdat sommige beveiligingsprogramma's installatiebestanden ten onrechte kunnen blokkeren.

    ??? "Hoe controleer ik of de afhankelijkheden van Visual C++ correct zijn geïnstalleerd?"

        1. Ga in Windows naar Configuratiescherm > Programma's > Programma's en onderdelen.
        
        2. Zoek naar items zoals "Microsoft Visual C++ 2015-2022 Redistributable" (x64/x86). Als deze ontbreken, installeert u ze via de bovenstaande link.

3. Voer het installatieprogramma van de GLKVM-app opnieuw uit.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
