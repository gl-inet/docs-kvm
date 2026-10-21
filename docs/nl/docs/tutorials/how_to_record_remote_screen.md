# Het externe scherm opnemen {#how-to-record-remote-screen}

U kunt het scherm van het bestuurde apparaat opnemen en het videobestand lokaal op uw KVM-apparaat opslaan.

Voer de volgende opdracht uit via SSH om de schermopname te starten:

```bash
ustreamer-dump --sink kvmd::ustreamer::h264 --output - | ffmpeg -use_wallclock_as_timestamps 1 -i pipe: -c:v copy /userdata/media/my_video.mp4
```

De opgenomen video's worden in deze map opgeslagen:

`/userdata/media/my_video.mp4`

U kunt het videobestand overzetten en downloaden met de functie [Virtual Media](../tutorials/how_to_share_files_between_controlling_device_and_controlled_device.md).

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
