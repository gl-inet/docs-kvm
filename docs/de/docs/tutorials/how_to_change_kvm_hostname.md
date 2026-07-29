# KVM-Hostname aendern

Der Standard-Hostname von GL.iNet KVM lautet **glkvm**. Wenn Sie mit demselben Netzwerk verbunden sind, koennen Sie lokal ueber die Domain `glkvm.local` darauf zugreifen.

Dieses Tutorial stellt zwei Methoden zum Aendern des Hostnamens vor: ueber die KVM-Konsole oder ueber Terminalbefehle. 

## Methode 1. KVM-Konsole

> **Hinweis**: Diese Funktion ist ab Firmware-Version 1.7.0 verfuegbar.

1. Melden Sie sich an Ihrem KVM an und navigieren Sie zu **Settings** -> **Network**. Klicken Sie auf den Hostnamen oder das Pfeilsymbol nach rechts. 

    ![settings network](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings_network.png){class="glboxshadow"}

2. Passen Sie den Hostnamen an und klicken Sie auf **Apply**.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify_hostname.png){class="glboxshadow"}

## Methode 2. Terminalbefehle

1. Melden Sie sich an Ihrem KVM an und navigieren Sie zu **Toolbox** -> **Terminal**. Klicken Sie auf **Access**. 

    ![access terminal](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_terminal.png){class="glboxshadow"}

2. Geben Sie im Terminal den folgenden Befehl ein und druecken Sie Enter. Ersetzen Sie "example" durch den gewuenschten Hostnamen. Danach startet Ihr KVM neu.

    `echo example > /etc/hostname && reboot`

    ![input command](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/input_command.png){class="glboxshadow"}

3. Warten Sie, bis das Geraet neu gestartet ist. Danach koennen Sie ueber den neuen Hostnamen auf Ihr KVM zugreifen.

    ![access new hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_new_hostname.png){class="glboxshadow"}

    Wenn Sie den Hostnamen vergessen haben oder pruefen moechten, ob die Aenderung wirksam ist, geben Sie im Terminal den folgenden Befehl ein, um den aktuellen Hostnamen anzuzeigen.

    `cat /etc/hostname`

    ![verify hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/verify_hostname.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
