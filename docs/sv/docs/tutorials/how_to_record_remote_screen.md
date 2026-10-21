# Så spelar du in fjärrskärmen {#how-to-record-remote-screen}

Du kan spela in den styrda enhetens skärm och lagra videofilen lokalt på KVM-enheten.

Kör följande kommando via SSH för att starta skärminspelningen:

```bash
ustreamer-dump --sink kvmd::ustreamer::h264 --output - | ffmpeg -use_wallclock_as_timestamps 1 -i pipe: -c:v copy /userdata/media/my_video.mp4
```

De inspelade videorna sparas här:

`/userdata/media/my_video.mp4`

Du kan överföra och ladda ned videofilen via funktionen [Virtual Media](../tutorials/how_to_share_files_between_controlling_device_and_controlled_device.md).

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
