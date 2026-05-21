# How to record remote screen?

You can capture the screen of the controlled device and store the video file locally on your KVM device.

Run the following command via SSH to start screen recording:

```bash
ustreamer-dump --sink kvmd::ustreamer::h264 --output - | ffmpeg -use_wallclock_as_timestamps 1 -i pipe: -c:v copy /userdata/media/my_video.mp4
```

The recorded videos will be saved to this directory: 

`/userdata/media/my_video.mp4`

You can transfer and download the video file via the [Virtual Media](../tutorials/how_to_share_files_between_controlling_device_and_controlled_device.md) feature.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.