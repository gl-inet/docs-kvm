# Mauslatenz beheben, wenn RPi4 RPi3 über KVM steuert

Wenn Sie RPi3 remote von RPi4 über KVM bedienen, kann eine Mausverzoegerung auftreten, die normalerweise mehrere Sekunden dauert.

Um das Problem zu beheben, fuegen Sie auf dem gesteuerten RPi3 `usbhid.mousepoll=0` zur Boot-Parameterzeile in `/boot/cmdline.txt` oder `/boot/firmware/cmdline.txt` hinzu und starten Sie das Gerät anschließend neu.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
