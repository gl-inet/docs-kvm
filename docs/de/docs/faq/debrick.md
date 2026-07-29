# KVM mit U-Boot wiederherstellen

Wenn Ihr KVM durch DIY-Projekte oder das Flashen einer falschen Firmware nicht mehr funktioniert, kann es möglicherweise nicht mehr korrekt starten. In diesem Fall können Sie die Firmware über U-Boot-Failsafe neu installieren.

## Vorbereitung

Bitte bereiten Sie einen Computer oder Laptop mit Ethernet-Anschluss vor. Wenn Ihr Computer keinen Ethernet-Anschluss hat, benötigen Sie zusätzlich einen USB-Ethernet-Adapter.

## Schritte zur Wiederherstellung

Befolgen Sie die folgenden Schritte genau, um Fehler bei der Wiederherstellung zu vermeiden.

1. Laden Sie die Firmware [hier](https://dl.gl-inet.com/kvm){target="_blank"} auf Ihren Computer herunter.

2. Trennen Sie die Stromversorgung des KVM. Verbinden Sie Ihren Computer mit dem Ethernet-Anschluss des KVM.

3. Halten Sie die Reset-Taste fest gedrückt und **schalten Sie gleichzeitig Ihr KVM ein**.

    Warten Sie, bis die LED mehrmals in regelmäßiger Abfolge blinkt. Lassen Sie die Reset-Taste **erst los, nachdem** sich das Blinkmuster geändert hat.

    !!! note "LED-Blinkmuster nach Gerätemodell"

        - **Comet (GL-RM1)**: Wenn Sie die Reset-Taste gedrückt halten, blinkt die blaue LED 5-mal. Lassen Sie die Reset-Taste nach den 5 Blinksignalen los; die blaue LED leuchtet danach dauerhaft.

        - **Comet PoE (GL-RM1PE)**: Wenn Sie die Reset-Taste gedrückt halten, blinkt die blaue LED 5-mal. Lassen Sie die Reset-Taste nach den 5 Blinksignalen los; die blaue LED leuchtet danach dauerhaft.

        - **Comet Pro (GL-RM10)**: Halten Sie die Reset-Taste etwa 5 Sekunden gedrückt und schalten Sie das KVM gleichzeitig ein. Lassen Sie die Taste anschließend los. Das Gerät wechselt in den U-Boot-Modus.

        - **Comet 5G (GL-RM10RC)**: Halten Sie die Reset-Taste etwa 5 Sekunden gedrückt und schalten Sie das KVM gleichzeitig ein. Lassen Sie die Taste anschließend los. Das Gerät wechselt in den U-Boot-Modus.

4. Stellen Sie die IP-Adresse Ihres Computers manuell auf **192.168.1.2** ein. Unten finden Sie Schritt-für-Schritt-Anleitungen für verschiedene Betriebssysteme.

    ??? "Windows 7 / Windows 10"

        1. Gehen Sie zu **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Klicken Sie mit der rechten Maustaste auf **Local Area Connection** -> **Properties**.

        3. Klicken Sie auf **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Stellen Sie die **IP adress** manuell auf `192.168.1.2` ein.

        5. Stellen Sie die **Subnet mask** auf `255.255.255.0` ein.

            ![ipv4 properties](https://static.gl-inet.com/docs/kvm/faq/debrick/win7_set_ip.jpg){class="glboxshadow"}

        6. Klicken Sie auf **OK**.

    ??? "Windows 11"

        1. Öffnen Sie Settings.

        2. Klicken Sie auf **Network & Internet**.

        3. Klicken Sie auf die Registerkarte **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet.png){class="glboxshadow"}

        4. Klicken Sie im Abschnitt "IP assignment" auf **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit1.png){class="glboxshadow"}

        5. Wählen Sie **Manual**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit2.png){class="glboxshadow"}

        6. Aktivieren Sie den **IPv4 toggle**-Schalter.

        7. Stellen Sie die statische **IP address** auf **192.168.1.2** ein.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit3.png){class="glboxshadow"}

        8. Geben Sie als **Subnet mask** **255.255.255.0** an.

        9. Klicken Sie auf **Save**.

    ??? "macOS"

        1. Klicken Sie oben links auf dem Bildschirm auf das **Apple**-Symbol und wählen Sie **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences.png){class="glboxshadow"}

        2. Klicken Sie auf **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences_network.png){class="glboxshadow"}

        4. Klicken Sie links auf **Ethernet**, dann auf das Dropdown-Feld neben **Configure IPv4** und wählen Sie **Manually**. Wenn Sie einen USB-Ethernet-Adapter verwenden, wird Ethernet möglicherweise nicht angezeigt; stattdessen kann der Name des USB-Ethernet-Adapters erscheinen.

            ![macos ip manually](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_1.png){class="glboxshadow"}

        4. Geben Sie für **IPv4 Address** `192.168.1.2`, für **Subnet Mask** `255.255.255.0` und für **Router** `192.168.1.1` ein. Klicken Sie anschließend unten rechts auf Apply.

            ![macos ip manually](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_2.png){class="glboxshadow"}

5. Öffnen Sie im Browser **http://192.168.1.1**. Dies ist die U-Boot Web UI.

    ![Uboot web ui](https://static.gl-inet.com/docs/kvm/faq/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    **Hinweis:** Die oben gezeigte U-Boot Web UI kann je nach Produktionsdatum und U-Boot-Version von Ihrer Ansicht abweichen. Aus Sicherheitsgründen stellen wir derzeit keine separaten U-Boot-Upgrades bereit. Falls ein Update erforderlich ist, integrieren wir es in eine neue Firmware.

6. Klicken Sie auf **Choose file** und wählen Sie die Firmware-Datei aus. Klicken Sie anschließend auf **Update firmware**.

7. Warten Sie etwa 3 Minuten. **Schalten Sie Ihr KVM während des Updates NICHT aus.**

    Das KVM ist bereit, wenn seine LED **weiß blinkt**.

8. Setzen Sie die IP-Einstellungen des Computers zurück, die Sie in Schritt 4 geändert haben.

9. Ziehen Sie das Ethernet-Kabel zwischen Ihrem Computer und dem KVM ab. Verbinden Sie Ihr KVM anschließend über dieses Ethernet-Kabel oder per WLAN mit einer Netzwerkquelle (z. B. einem Router oder Netzwerk-Switch).

    Warten Sie etwa 1 Minute, damit das KVM Internetzugang erhält. Danach können Sie wieder auf Ihr KVM zugreifen.

    **Hinweis:** Konfigurationseinstellungen bleiben normalerweise erhalten. Sie werden jedoch auf die Standardwerte zurückgesetzt, wenn ein Konfigurationsfehler den Systemausfall verursacht hat, der die Wiederherstellung erforderlich machte.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
