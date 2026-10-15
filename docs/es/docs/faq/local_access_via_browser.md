# Cómo acceder al KVM de forma local mediante un navegador {#how-to-access-the-kvm-locally-via-browser}

Antes de empezar, asegúrese de que el dispositivo de control y el KVM estén en la misma red local.

Puede acceder al KVM de forma local desde un navegador mediante un nombre de dominio o una dirección IP.

## Acceso local mediante el dominio {#local-access-via-domain}

1. Abra un navegador en el dispositivo de control. Se recomienda Chrome o Edge para una mayor compatibilidad.

2. Introduzca `glkvm.local` en la barra de direcciones. Se abrirá la página de inicio de sesión de GLKVM. Introduzca la contraseña de administrador.

    ![Acceso local mediante el dominio](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    Ya puede acceder a la consola KVM de forma local y, desde ella, al dispositivo controlado.

    ![Consola mediante el dominio local](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

## Acceso local mediante la dirección IP {#local-access-via-ip-address}

Busque la dirección IP del KVM en la red a la que está conectado, por ejemplo en el router, e introdúzcala en el navegador. Así podrá acceder de forma local al KVM y al dispositivo controlado.

En este ejemplo se utilizan el router **GL-AXT1800** y el KVM **GL-RM1 Comet**. Comet está conectado al puerto LAN del router mediante un cable Ethernet. El dispositivo controlado está conectado correctamente a Comet mediante un cable HDMI y un cable USB.

Siga estos pasos para acceder a la consola KVM.

1. Inicie sesión en el panel de administración web del GL-AXT1800. El router debe estar configurado para acceder a Internet.

    ![Iniciar sesión en el router](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/log_in_router.png){class="glboxshadow"}

2. En el panel del router, vaya a **Client** y busque la IP de Comet en la lista de clientes. En este ejemplo, es **192.168.8.197**.

    ![Buscar la IP de GLKVM](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

3. Abra una nueva pestaña e introduzca la IP de Comet, **192.168.8.197**, en la barra de direcciones.

    Se abrirá la página de inicio de sesión de GLKVM. Introduzca la contraseña de administrador.

    ![Acceso local mediante la IP](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    Ya puede acceder a la consola KVM de forma local y, desde ella, al dispositivo controlado.

    ![Consola mediante la IP local](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
