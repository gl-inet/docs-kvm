# Mauslatenz beheben, wenn RPi4 RPi3 steuert

Wenn Sie einen Raspberry Pi4 verwenden, um einen Raspberry Pi3 ueber GL.iNet KVM zu steuern, koennen Mauslatenzprobleme auftreten, die typischerweise einige Sekunden dauern.

Um das Problem zu beheben, fuegen Sie auf dem gesteuerten Geraet, in diesem Fall RPi3, `usbhid.mousepoll=0` an die Boot-Zeile in `/boot/cmdline.txt` oder `/boot/firmware/cmdline.txt` an und starten Sie es neu.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
