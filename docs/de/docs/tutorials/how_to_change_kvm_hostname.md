# KVM-Hostname ändern {#how-to-change-kvm-hostname}

Der Standard-Hostname von GL.iNet KVM lautet **glkvm**. Wenn Sie mit demselben Netzwerk verbunden sind, können Sie lokal über die Domain `glkvm.local` darauf zugreifen.

Dieses Tutorial stellt zwei Methoden zum Ändern des Hostnamens vor: über die KVM-Konsole oder über Terminalbefehle. 

## Methode 1. KVM-Konsole {#method-1-kvm-console}

> **Hinweis**: Diese Funktion ist ab Firmware-Version 1.7.0 verfügbar.

### Firmware v1.10 und neuer {#firmware-v110-and-above}

1. Melden Sie sich an Ihrem KVM an und klicken Sie in der Navigationsleiste auf das Symbol Settings, um die Seite Settings zu öffnen.

    ![settings network](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings-network.png){class="glboxshadow"}

2. Navigieren Sie zu **Network** und geben Sie den gewünschten Hostnamen ein. Die Änderung wird sofort wirksam.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify-hostname.png){class="glboxshadow"}

### Firmware v1.9 und älter {#firmware-v19-and-earlier}

1. Melden Sie sich an Ihrem KVM an und navigieren Sie zu **Settings** -> **Network**. Klicken Sie auf den Hostnamen oder das Pfeilsymbol nach rechts. 

    ![settings network](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings_network.png){class="glboxshadow"}

2. Passen Sie den Hostnamen an und klicken Sie auf **Apply**.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify_hostname.png){class="glboxshadow"}

## Methode 2. Terminalbefehle {#method-2-terminal-commands}

1. Melden Sie sich an Ihrem KVM an und navigieren Sie zu **Toolbox** -> **Terminal**. Klicken Sie auf **Access**. 

    ![access terminal](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_terminal.png){class="glboxshadow"}

2. Geben Sie im Terminal den folgenden Befehl ein und drücken Sie Enter. Ersetzen Sie "example" durch den gewünschten Hostnamen. Danach startet Ihr KVM neu.

    `echo example > /etc/hostname && reboot`

    ![input command](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/input_command.png){class="glboxshadow"}

3. Warten Sie, bis das Gerät neu gestartet ist. Danach können Sie über den neuen Hostnamen auf Ihr KVM zugreifen.

    ![access new hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_new_hostname.png){class="glboxshadow"}

    Wenn Sie den Hostnamen vergessen haben oder prüfen möchten, ob die Änderung wirksam ist, geben Sie im Terminal den folgenden Befehl ein, um den aktuellen Hostnamen anzuzeigen.

    `cat /etc/hostname`

    ![verify hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/verify_hostname.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
