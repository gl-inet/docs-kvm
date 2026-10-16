# Advertencia de privacidad al acceder al KVM mediante un navegador {#privacy-error-when-accessing-kvm-via-browser}

Al acceder al KVM GL.iNet mediante un navegador, puede aparecer la advertencia **Your connection isn't private**.

![Advertencia de privacidad](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

Esta advertencia indica que el navegador no puede validar el certificado SSL/TLS que presenta el KVM. Por ejemplo, puede que no lo haya emitido una autoridad de certificación de confianza para el navegador o que no coincida con la dirección IP o el nombre de host utilizado para acceder a la consola.

## Por qué aparece esta advertencia {#why-do-i-get-this-warning}

En el ejemplo anterior, **192.168.8.11** es la IP local del KVM, asignada dinámicamente por el router mediante DHCP.

!!! Note "Nota"

    Si la puerta de enlace del router al que está conectado el KVM GL.iNet es "192.168.x.1", donde x suele ser 0, 1 u 8 en las redes privadas, la IP local del KVM debe ser "192.168.x.y", donde y es una dirección de equipo válida en la subred.

Esta IP local se utiliza para acceder a la consola KVM GL.iNet, no a un sitio web público.

El KVM utiliza un certificado TLS predeterminado para el acceso HTTPS desde el navegador. Los navegadores validan los certificados de las consolas locales igual que los de los sitios web públicos: el certificado debe ser de confianza, ser válido y coincidir con la dirección de acceso.

Si el navegador no confía en el certificado predeterminado, o si este no incluye la IP local o el nombre de host introducido, se muestra una advertencia. Esto no significa que el KVM carezca de certificado. HTTPS puede seguir cifrando la conexión, pero el navegador no puede verificar la identidad del KVM.

## Cómo resolver la advertencia {#how-to-resolve-the-warning}

Para el acceso local, confirme primero que la dirección pertenece a su KVM. Después, haga clic en **Advanced** y en **Continue to "192.168.8.11"** (el texto exacto varía según el navegador).

![Continuar a 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

Se abrirá la consola del KVM GL.iNet.

![Acceso local a la administración del KVM](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## Puedo utilizar mi propio certificado {#can-i-use-my-own-certificate}

Sí. Puede instalar y utilizar su propio certificado SSL/TLS en el KVM. Siga estos pasos.

1. Obtenga un certificado SSL/TLS que incluya el nombre de host o la dirección IP que utiliza para acceder al KVM. Para evitar las advertencias del navegador, el certificado debe ser válido y estar emitido por una autoridad de certificación de confianza para el navegador. Un certificado autofirmado seguirá generando una advertencia a menos que configure expresamente el dispositivo de control para que confíe en él.

2. Inicie sesión en la consola KVM. Haga clic en el icono de escudo de la esquina superior derecha para acceder a **Security** -> **TLS Certificate**.

    ![Configuración de certificado personalizado](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert1.png){class="glboxshadow"}

    En la ventana emergente, seleccione **Custom Certificate** y cargue el archivo de certificado y la clave privada. Esta función está disponible desde el firmware v1.8.0.

    ![Cargar un certificado personalizado](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert2.png){class="glboxshadow"}

    También puede sustituir el certificado y la clave privada del KVM mediante un terminal SSH o WinSCP. Ambos se encuentran en el siguiente directorio:

    `/etc/kvmd/user/ssl`

    Sustitúyalos por su nuevo certificado SSL y su clave privada.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
