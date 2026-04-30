---
hide:
  - navigation
  - toc
---

# How to Record Screen

You can record the screen of the controlled device and save the video file to the KVM device.

Run the following command via SSH to start recording:

```bash
ustreamer-dump --sink kvmd::ustreamer::h264 --output - | ffmpeg -use_wallclock_as_timestamps 1 -i pipe: -c:v copy /userdata/media/my_video.mp4
```

The recorded video will be saved to `/userdata/media/my_video.mp4`.

You can download the video file through the [Virtual Media](../tutorials/how_to_share_files_between_controlling_device_and_controlled_device.md) feature.
