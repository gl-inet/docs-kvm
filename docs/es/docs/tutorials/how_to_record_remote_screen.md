# Cómo grabar la pantalla remota {#how-to-record-remote-screen}

Puede grabar la pantalla del dispositivo controlado y guardar el vídeo de forma local en el KVM.

Ejecute este comando mediante SSH para iniciar la grabación:

```bash
ustreamer-dump --sink kvmd::ustreamer::h264 --output - | ffmpeg -use_wallclock_as_timestamps 1 -i pipe: -c:v copy /userdata/media/my_video.mp4
```

El vídeo grabado se guardará en esta ruta:

`/userdata/media/my_video.mp4`

Puede transferir y descargar el archivo mediante la función [Virtual Media](../tutorials/how_to_share_files_between_controlling_device_and_controlled_device.md).

---

¿Tiene más preguntas? Visite nuestro [foro de la comunidad](https://forum.gl-inet.com){target="_blank"} o [póngase en contacto con nosotros](https://www.gl-inet.com/contacts/){target="_blank"}.
