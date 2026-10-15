# Advertencia de privacidad al acceder al KVM mediante un navegador {#privacy-error-when-accessing-kvm-via-browser}

Al acceder al KVM GL.iNet mediante un navegador, puede aparecer la advertencia **Your connection isn't private**.

![Advertencia de privacidad](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

Es una advertencia de seguridad habitual que los navegadores muestran al detectar un sitio sin certificado SSL/TLS, ya que las conexiones HTTPS dependen de estos certificados para verificar la identidad del servidor y cifrar los datos.

## Por qué aparece esta advertencia {#why-do-i-get-this-warning}

En el ejemplo anterior, **192.168.8.11** es la IP local del KVM, asignada dinámicamente por el router mediante DHCP.

!!! Note "Nota"

    Si la puerta de enlace del router al que está conectado el KVM GL.iNet es "192.168.x.1", donde x suele ser 0, 1 u 8 en las redes privadas, la IP local del KVM debe ser "192.168.x.y", donde y es una dirección de equipo válida en la subred.

Esta IP local se utiliza para acceder a la consola KVM GL.iNet, no a un sitio web público.

Sin embargo, los navegadores normalmente no distinguen entre una consola local y un sitio web público. Tratan las direcciones IP como sitios web y esperan que las conexiones HTTPS estén protegidas por certificados SSL/TLS.

Un sitio web seguro utiliza un certificado SSL/TLS. Por ello, al acceder a una consola local que no tiene certificado, el navegador muestra una advertencia de seguridad por la ausencia del certificado.

## Cómo resolver la advertencia {#how-to-resolve-the-warning}

Haga clic en **Advanced** y en **Continue to "192.168.8.11"**.

![Continuar a 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

Se abrirá la consola del KVM GL.iNet.

![Acceso local a la administración del KVM](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## Puedo utilizar mi propio certificado {#can-i-use-my-own-certificate}

Sí. Puede instalar y utilizar su propio certificado SSL/TLS en el KVM. Siga estos pasos.

1. Solicite un certificado SSL/TLS o utilice uno autofirmado.

2. Inicie sesión en la consola KVM. Haga clic en el icono de escudo de la esquina superior derecha para acceder a **Security** -> **TLS Certificate**.

    ![Configuración de certificado personalizado](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert1.png){class="glboxshadow"}

    En la ventana emergente, seleccione **Custom Certificate** y cargue el archivo de certificado y la clave privada. Esta función está disponible desde el firmware v1.8.0.

    ![Cargar un certificado personalizado](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert2.png){class="glboxshadow"}

    También puede editar los archivos de configuración del KVM mediante un terminal SSH o WinSCP. El certificado y la clave generados automáticamente se encuentran en:

    `/etc/kvmd/user/ssl`

    Sustitúyalos por su nuevo certificado SSL y su clave privada.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
