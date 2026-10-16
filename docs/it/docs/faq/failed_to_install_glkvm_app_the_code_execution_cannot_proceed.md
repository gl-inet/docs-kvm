# Installazione dell'app GLKVM su Windows non riuscita: "The code execution cannot proceed" {#failed-to-install-glkvm-app-on-windows-the-code-execution-cannot-proceed}

Durante l'installazione dell'app GLKVM su Windows, potrebbe comparire l'errore: "The code execution cannot proceed because VCRUNTIME140_1.dll was not found".

![system error](https://static.gl-inet.com/docs/kvm/faq/failed_to_install_glkvm_app/system_error.png){class="glboxshadow"}

Questo errore si verifica quando mancano alcune dipendenze del runtime Visual C++. L'app richiede specifici file DLL forniti dal pacchetto Visual C++ Redistributable.

Segui questi passaggi:

1. Scarica l'ultima versione di Visual C++ Redistributable per Visual Studio dal sito ufficiale di Microsoft, disponibile [qui](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170){target="_blank"}.

2. Installa il pacchetto e riavvia il computer.

    Disattiva temporaneamente l'antivirus, poiché alcuni strumenti di sicurezza potrebbero bloccare erroneamente i file di installazione.

    ??? "Come verificare che le dipendenze Visual C++ siano installate correttamente?"

        1. Su Windows, vai su Control Panel > Programs > Programs and Features.

        2. Cerca voci come "Microsoft Visual C++ 2015-2022 Redistributable" (x64/x86). Se mancano, installale tramite il link riportato sopra.

3. Esegui nuovamente il programma di installazione dell'app GLKVM.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
