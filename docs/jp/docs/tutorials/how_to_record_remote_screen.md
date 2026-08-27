# リモート画面を録画する方法

被制御デバイスの画面をキャプチャし、ビデオ ファイルを KVM デバイスにローカルに保存できます。

SSH 経由で次のコマンドを実行して、画面の記録を開始します。

```bash
ustreamer-dump --sink kvmd::ustreamer::h264 --output - | ffmpeg -use_wallclock_as_timestamps 1 -i pipe: -c:v copy /userdata/media/my_video.mp4
```

録画されたビデオは次のディレクトリに保存されます。

`/userdata/media/my_video.mp4`

[仮想メディア](../tutorials/how_to_share_files_between_controlling_device_and_controlled_device.md)機能を使用して、ビデオ ファイルを転送およびダウンロードできます。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
