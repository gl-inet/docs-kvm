# KVM mit RKDevTool debricken {#how-to-unbrick-kvm-via-rkdevtool}

In diesem Tutorial erfahren Sie, wie Sie ein GL.iNet KVM mit RKDevTool debricken. Es gilt für Fälle, in denen das KVM nicht mehr startet und weder über reguläre Firmware-Updates noch über den U-Boot-Failsafe-Modus wiederhergestellt werden kann.

## Vorbereitung {#preparation}

Bereiten Sie die folgenden Werkzeuge für das Debricking vor.

- Einen Windows-Computer
- Ein USB-Datenkabel
- Ein Netzteil für das KVM-Gerät

!!! Note

    Trennen Sie während des Debricking-Vorgangs NICHT das USB-Kabel und schalten Sie das KVM nicht aus. Andernfalls kann das Gerät beschädigt werden.

    Es wird empfohlen, wichtige Daten zu sichern, bevor Sie mit dem Debricking beginnen.

## Debricking-Schritte {#unbrick-steps}

Um Fehler beim Debricking zu vermeiden, führen Sie die Schritte bitte der Reihe nach aus.

1. Schalten Sie Ihr KVM-Gerät aus.

2. Laden Sie die neueste Firmware für Ihr KVM-Gerät [hier](https://dl.gl-inet.com/kvm){target="_blank"} auf Ihren Computer herunter.

3. Laden Sie das Treiberpaket [hier](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/DriverAssitant_v5.11.zip) auf Ihren Computer herunter und entpacken Sie es in ein beliebiges Verzeichnis.

4. Doppelklicken Sie auf die .exe-Datei, um die Treiberinstallation abzuschließen.

    ![install driver](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_1.png){class="glboxshadow"}

    ![install driver](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_2.png){class="glboxshadow"}

5. Laden Sie das **RKDevTool** [hier](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/RKDevTool_Release_v3.37.zip) auf Ihren Computer herunter und entpacken Sie es in ein leicht zugängliches Verzeichnis.

6. Doppelklicken Sie auf die .exe-Datei, um das Flash-Tool auf Ihrem Computer zu starten.

    ![run rkdevtool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_1.png){class="glboxshadow"}

    ![run rkdevtool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_2.png){class="glboxshadow"}

7. Verbinden Sie den Type-C-OTG-Port des KVM über ein USB-Datenkabel mit dem USB-Port des Computers.

    Im folgenden Beispiel wird Comet (GL-RM1) verwendet. Der Type-C-OTG-Port ist unten dargestellt.

    ![connect usb cable](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/otg-port-rm1.png){class="glboxshadow gl-60-desktop"}

8. Halten Sie die RESET-Taste **10 Sekunden** lang gedrückt, während Sie das Stromkabel an das KVM anschließen. Lassen Sie die Taste danach los. Ihr KVM-Gerät wechselt in den Loader-Modus.

    ![reset button](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/reset_button_rm1.jpg){class="glboxshadow" width="433"}

9. Wechseln Sie im RKDevTool zum Bereich **Upgrade Firmware** -> **Firmware** und wählen Sie die in Schritt 2 heruntergeladene Firmware zum Hochladen aus.

    ![select firmware](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/select_firmware.png){class="glboxshadow"}

    Wechseln Sie anschließend zum Tab **Upgrade** neben dem Firmware-Tab. Dort wird "Found Loader Device" angezeigt und das Tool beginnt mit dem Flashen der Firmware.

    ![rkdevtool panel](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/rkdevtool_panel.jpg){class="glboxshadow"}

    Das KVM-Gerät startet automatisch neu, sobald das Upgrade abgeschlossen ist.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
