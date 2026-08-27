# RPi4 が RPi3 を制御するときにマウスの遅延を修正する方法

Raspberry Pi4 を使用して GL.iNet KVM 経由で Raspberry Pi3 を制御すると、マウスの遅延の問題が発生する可能性があり、通常は数秒続きます。

これを修正するには、管理対象サーバー (つまり、この場合は RPI3) 上の `/boot/cmdline.txt` (または `/boot/firmware/cmdline.txt`) のブート行に `usbhid.mousepoll=0` を追加し、再起動します。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
