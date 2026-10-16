# Enregistrer l’écran distant {#how-to-record-remote-screen}

Vous pouvez enregistrer l’écran de l’appareil contrôlé et stocker le fichier vidéo localement sur votre KVM.

Exécutez la commande suivante en SSH pour démarrer l’enregistrement de l’écran :

```bash
ustreamer-dump --sink kvmd::ustreamer::h264 --output - | ffmpeg -use_wallclock_as_timestamps 1 -i pipe: -c:v copy /userdata/media/my_video.mp4
```

Les vidéos enregistrées sont sauvegardées à cet emplacement :

`/userdata/media/my_video.mp4`

Vous pouvez transférer et télécharger le fichier vidéo grâce à la fonction [Virtual Media](../tutorials/how_to_share_files_between_controlling_device_and_controlled_device.md).

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
