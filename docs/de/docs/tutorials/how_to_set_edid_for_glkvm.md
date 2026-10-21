# EDID für GL.iNet KVM festlegen {#how-to-set-edid-for-glinet-kvm}

## Was ist EDID {#what-is-edid}

EDID, also Extended Display Identification Data, ist ein von der Video Electronics Standards Association (VESA) definiertes Standarddatenformat. Es wird im nichtflüchtigen Speicher des Displays abgelegt und enthält wichtige Display-Informationen wie Hersteller, maximale Auflösung, Bildwiederholrate usw. Geräte wie Computer können durch Auslesen der EDID die Parameter des Ausgangssignals automatisch anpassen, damit das Display Bilder optimal darstellt.

Wenn Geräte wie Computer, Laptops oder Spielkonsolen mit einem Display verbunden werden, lesen sie im Allgemeinen automatisch die EDID aus, um passende Anzeigeparameter festzulegen. Dadurch werden Probleme wie unscharfe Bilder oder Flackern vermieden und eine klare, stabile Darstellung erreicht.

Die EDID-Einstellungen in GL.iNet KVM dienen dazu, automatisch die optimalen Parameter des Displays abzustimmen. Wenn ein GL.iNet KVM mit dem gesteuerten Gerät verbunden ist, kann es durch Auslesen der EDID des Displays die Anzeigeausgabe automatisch anpassen, um das beste Bild darzustellen.

## Voreingestellte EDID {#preset-edid}

Navigieren Sie in der GL.iNet KVM-Konsole zu **Settings** -> **Video** -> **EDID**. Dort gibt es einige voreingestellte EDID-Einstellungen.

![edid preset](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_preset.jpg){class="glboxshadow"}

**Die Standard-EDID von GL.iNet KVM ist bereits für die meisten Szenarien geeignet und muss normalerweise nicht geändert werden**.

In besonderen Situationen, z. B. zum Konfigurieren von UEFI/BIOS oder zum Anpassen von Auflösung/Bildwiederholrate, können Sie einen voreingestellten Wert auswählen, z. B. 1920×1280/AUO/60HZ.

## Benutzerdefinierte EDID {#custom-edid}

Wenn Sie keinen passenden EDID-Code finden, können Sie [diesen Link](https://github.com/linuxhw/EDID){target="_blank"} oder die folgenden Schritte verwenden, um die EDID-Konfiguration anzupassen.

!!! Tip

    Eine EDID zu finden, die genau Ihrer gewünschten Auflösung und Bildwiederholrate entspricht, kann schwierig sein. Sie können EDID-Bearbeitungstools wie **RTDtool** oder **EEditZ** verwenden, um eine vorhandene EDID an Ihre spezifischen Anforderungen anzupassen.

1. Suchen Sie [hier](https://github.com/linuxhw/EDID){target="_blank"} eine passende EDID und kopieren Sie sie.

2. Melden Sie sich an der GL.iNet KVM-Konsole an und navigieren Sie zu **Settings** -> **EDID**. Wechseln Sie in den Modus **Customize**, fügen Sie die Parameter in das Eingabefeld ein und klicken Sie auf **Set Custom**, um die Einstellungen anzuwenden.

    ![edid customize](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_customize.png){class="glboxshadow"}

!!! Note

    1. Die Auflösung darf 2560×1440@60Hz nicht überschreiten. Eine Auflösung von 2560×1600@60Hz wird beispielsweise nicht unterstützt.
    2. Die maximal unterstützte Bildwiederholrate beträgt 60Hz. Für Auflösungen über 1920x1080 wird eine Bildrate von 60FPS oder niedriger empfohlen.
    3. Vermeiden Sie interlaced Auflösungen, da dies zu einer fehlerhaften Bildanzeige führen kann.
    4. Der eingegebene EDID-Codeblock darf höchstens zwei Blöcke umfassen.
    5. Grundlegende Audiounterstützung ist erforderlich. Andernfalls ist die Soundkarte auf dem gesteuerten Gerät möglicherweise nicht auswählbar, was zu fehlendem Ton führt.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
