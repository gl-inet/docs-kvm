# Remote-Bildschirm aufzeichnen

Sie koennen den Bildschirm des gesteuerten Geraets aufnehmen und die Videodatei lokal auf Ihrem KVM-Geraet speichern.

Fuehren Sie den folgenden Befehl per SSH aus, um die Bildschirmaufzeichnung zu starten:

```bash
ustreamer-dump --sink kvmd::ustreamer::h264 --output - | ffmpeg -use_wallclock_as_timestamps 1 -i pipe: -c:v copy /userdata/media/my_video.mp4
```

Die aufgezeichneten Videos werden in folgendem Verzeichnis gespeichert: 

`/userdata/media/my_video.mp4`

Sie koennen die Videodatei ueber die Funktion [virtuelle Medien](../tutorials/how_to_share_files_between_controlling_device_and_controlled_device.md) uebertragen und herunterladen.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
