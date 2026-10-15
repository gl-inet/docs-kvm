# Error al instalar la aplicación GLKVM en Windows: "The code execution cannot proceed" {#failed-to-install-glkvm-app-on-windows-the-code-execution-cannot-proceed}

Al instalar la aplicación GLKVM en Windows, puede aparecer el error: "The code execution cannot proceed because VCRUNTIME140_1.dll was not found".

![Error del sistema](https://static.gl-inet.com/docs/kvm/faq/failed_to_install_glkvm_app/system_error.png){class="glboxshadow"}

Este error se debe a que faltan dependencias del entorno de ejecución de Visual C++. La aplicación necesita archivos DLL específicos incluidos en el paquete Visual C++ Redistributable.

Siga estos pasos:

1. Descargue la versión más reciente de Visual C++ Redistributable para Visual Studio desde el sitio oficial de Microsoft, [aquí](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170){target="_blank"}.

2. Instale el paquete y reinicie el equipo.

    Desactive temporalmente el antivirus, ya que algunas herramientas de seguridad pueden bloquear por error los archivos de instalación.

    ??? "¿Cómo comprobar si las dependencias de Visual C++ están instaladas correctamente?"

        1. En Windows, vaya a Control Panel > Programs > Programs and Features.

        2. Busque entradas como "Microsoft Visual C++ 2015-2022 Redistributable" (x64/x86). Si no aparecen, instálelas mediante el enlace anterior.

3. Vuelva a ejecutar el instalador de la aplicación GLKVM.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
