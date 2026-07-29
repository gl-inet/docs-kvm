# EDID fuer GL.iNet KVM festlegen

## Was ist EDID

EDID, also Extended Display Identification Data, ist ein von der Video Electronics Standards Association (VESA) definiertes Standarddatenformat. Es wird im nichtfluechtigen Speicher des Displays abgelegt und enthaelt wichtige Display-Informationen wie Hersteller, maximale Aufloesung, Bildwiederholrate usw. Geraete wie Computer koennen durch Auslesen der EDID die Parameter des Ausgangssignals automatisch anpassen, damit das Display Bilder optimal darstellt.

Wenn Geraete wie Computer, Laptops oder Spielkonsolen mit einem Display verbunden werden, lesen sie im Allgemeinen automatisch die EDID aus, um passende Anzeigeparameter festzulegen. Dadurch werden Probleme wie unscharfe Bilder oder Flackern vermieden und eine klare, stabile Darstellung erreicht.

Die EDID-Einstellungen in GL.iNet KVM dienen dazu, automatisch die optimalen Parameter des Displays abzustimmen. Wenn ein GL.iNet KVM mit dem gesteuerten Geraet verbunden ist, kann es durch Auslesen der EDID des Displays die Anzeigeausgabe automatisch anpassen, um das beste Bild darzustellen. 

## Preset EDID

Navigieren Sie in der GL.iNet KVM-Konsole zu **Settings** -> **Video** -> **EDID**. Dort gibt es einige voreingestellte EDID-Einstellungen. 

![edid preset](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_preset.jpg){class="glboxshadow"}

**Die Standard-EDID von GL.iNet KVM ist bereits fuer die meisten Szenarien geeignet und muss normalerweise nicht geaendert werden**.

In besonderen Situationen, z. B. zum Konfigurieren von UEFI/BIOS oder zum Anpassen von Aufloesung/Bildwiederholrate, koennen Sie einen voreingestellten Wert auswaehlen, z. B. 1920×1280/AUO/60HZ.

## Custom EDID

Wenn Sie keinen passenden EDID-Code finden, koennen Sie [diesen Link](https://github.com/linuxhw/EDID){target="blank"} oder die folgenden Schritte verwenden, um die EDID-Konfiguration anzupassen.

!!! Tip

    Eine EDID zu finden, die genau Ihrer gewuenschten Aufloesung und Bildwiederholrate entspricht, kann schwierig sein. Sie koennen EDID-Bearbeitungstools wie **RTDtool** oder **EEditZ** verwenden, um eine vorhandene EDID an Ihre spezifischen Anforderungen anzupassen.

1. Suchen Sie [hier](https://github.com/linuxhw/EDID){target="blank"} eine passende EDID und kopieren Sie sie.

2. Melden Sie sich an der GL.iNet KVM-Konsole an und navigieren Sie zu **Settings** -> **EDID**. Wechseln Sie in den Modus **Customize**, fuegen Sie die Parameter in das Eingabefeld ein und klicken Sie auf **Set Custom**, um die Einstellungen anzuwenden.

    ![edid customize](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_customize.png){class="glboxshadow"}

!!! Note

    1. Die Aufloesung darf 2560×1440@60Hz nicht ueberschreiten. Eine Aufloesung von 2560×1600@60Hz wird beispielsweise nicht unterstuetzt.
    2. Die maximal unterstuetzte Bildwiederholrate betraegt 60Hz. Fuer Aufloesungen ueber 1920x1080 wird eine Bildrate von 60FPS oder niedriger empfohlen.
    3. Vermeiden Sie interlaced Aufloesungen, da dies zu einer fehlerhaften Bildanzeige fuehren kann.
    4. Der eingegebene EDID-Codeblock darf hoechstens zwei Bloecke umfassen.
    5. Grundlegende Audiounterstuetzung ist erforderlich. Andernfalls ist die Soundkarte auf dem gesteuerten Geraet moeglicherweise nicht auswaehlbar, was zu fehlendem Ton fuehrt. 

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
