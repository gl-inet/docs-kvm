# Betriebssystem per Fernzugriff mit virtuellen Medien auf dem gesteuerten Computer installieren

Dieses Tutorial zeigt, wie Sie mit der GL.iNet KVM-Funktion virtuelle Medien per Fernzugriff ein Betriebssystem auf dem gesteuerten Computer installieren.

1. Melden Sie sich an Ihrem GL.iNet KVM an und navigieren Sie zu **Virtual Media**.

2. Laden Sie die OS-ISO-Datei in Virtual Media hoch.

    ![upload file](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/upload_file.png){class="glboxshadow"}

3. Klicken Sie nach dem Hochladen auf **Mount To Remote** und waehlen Sie **Image mounting**, um das ISO-Image einzubinden.

    ![image mounting](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-1.png){class="glboxshadow"}

    Waehlen Sie die Image-Datei aus und klicken Sie auf **Mount Image**.

    ![image mounting](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-2.png){class="glboxshadow"}

4. Starten Sie den per Fernzugriff gesteuerten Computer neu und **druecken Sie waehrend des Bootvorgangs sofort die passende Taste** (in diesem Beispiel DEL), um BIOS/UEFI aufzurufen.

    ![enter bios](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/enter_bios.png){class="glboxshadow"}

5. Legen Sie im Boot-Menue **"Glinet Flash Drive 1.00"** als Boot Option #1 fest.

    ![set boot option priority](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/set_boot_option_priority.png){class="glboxshadow"}

6. Speichern Sie die Einstellungen und verlassen Sie das BIOS. Das System startet anschliessend vom eingebundenen ISO und beginnt mit der OS-Installation.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
