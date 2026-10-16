# Come registrare lo schermo remoto {#how-to-record-remote-screen}

Puoi acquisire lo schermo del dispositivo controllato e salvare il file video localmente sul dispositivo KVM.

Esegui il comando seguente tramite SSH per avviare la registrazione dello schermo:

```bash
ustreamer-dump --sink kvmd::ustreamer::h264 --output - | ffmpeg -use_wallclock_as_timestamps 1 -i pipe: -c:v copy /userdata/media/my_video.mp4
```

Il video registrato verrà salvato nel seguente percorso:

`/userdata/media/my_video.mp4`

Puoi trasferire e scaricare il file video tramite la funzione [Virtual Media](../tutorials/how_to_share_files_between_controlling_device_and_controlled_device.md).

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
