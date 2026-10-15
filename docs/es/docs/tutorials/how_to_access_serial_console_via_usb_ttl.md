# Cómo acceder a la consola serie mediante un adaptador USB TTL {#how-to-access-serial-console-via-usb-ttl}

Siga estos pasos para utilizar el adaptador USB TTL en la depuración por puerto serie:

1. Conecte el adaptador USB TTL al puerto USB del KVM.
2. Ejecute este comando para abrir la conexión del puerto serie:

```bash
minicom -D /dev/ttyUSB0 -b 115200
```

El comando establece una conexión serie con `/dev/ttyUSB0` a una velocidad de `115200` baudios.

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
