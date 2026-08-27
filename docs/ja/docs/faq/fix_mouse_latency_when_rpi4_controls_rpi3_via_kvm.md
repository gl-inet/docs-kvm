# RPi4 が KVM 経由で RPi3 を制御するときにマウスの遅延を修正する方法

KVM 経由で RPi4 から RPi3 をリモート操作すると、マウスの遅延が発生する場合があり、通常は数秒続きます。

この問題を解決するには、制御対象の RPi3 の `/boot/cmdline.txt` または `/boot/firmware/cmdline.txt` のブート パラメーター行に `usbhid.mousepoll=0` を追加し、デバイスを再起動します。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
