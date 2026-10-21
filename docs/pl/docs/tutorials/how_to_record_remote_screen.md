# Jak nagrać zdalny ekran {#how-to-record-remote-screen}

Możesz nagrywać ekran sterowanego urządzenia i zapisywać plik wideo lokalnie na urządzeniu KVM.

Uruchom poniższe polecenie przez SSH, aby rozpocząć nagrywanie ekranu:

```bash
ustreamer-dump --sink kvmd::ustreamer::h264 --output - | ffmpeg -use_wallclock_as_timestamps 1 -i pipe: -c:v copy /userdata/media/my_video.mp4
```

Nagranie zostanie zapisane pod następującą ścieżką:

`/userdata/media/my_video.mp4`

Możesz przesłać i pobrać plik wideo za pomocą funkcji [Virtual Media](../tutorials/how_to_share_files_between_controlling_device_and_controlled_device.md).

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
