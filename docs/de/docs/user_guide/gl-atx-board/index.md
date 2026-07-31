# ATX Board (GL-ATXPC) Benutzerhandbuch

Das ATX Board ist optionales Zubehör für GL.iNet KVM-Geräte. Als intelligentes Stromverwaltungsmodul ermöglicht es die Fernsteuerung der Stromversorgung des gesteuerten Geräts, indem es physische Betätigungen des Ein-/Aus-Schalters simuliert (Einschalten/Ausschalten/Neustart).

Das ATX Board wird im Gehäuse des gesteuerten Geräts installiert und bietet dadurch eine unauffälligere und stabilere Stromverwaltung.

**Hinweis**: Comet Q (GL-RMQ1) funktioniert nicht mit dem ATX Board.

![rm1-and-atx-borad](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/rm1-and-atx-borad.jpg){class="glboxshadow"}

## Lieferumfang

![inside the box](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/inside-the-box.png){class="glboxshadow gl-80-desktop"}

- 1 x ATX-Hauptplatine
- 1 x 9-PIN-Kabelsatz
- 1 x Schraubensatz
- 1 x USB-A-auf-Type-C-Kabel
- 1 x ATX-Halterungssatz

## Pinbelegung

![pinout](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/pinout.jpg){class="glboxshadow gl-80-desktop"}

Erklärung der Schnittstellen:

1. Type-C-Schnittstelle: Verbindung zum KVM-Gerät.
2. Firmware-Upgrade-Taste: Für den Mikrocontroller auf der ATX-Hauptplatine.
3. Reset-Taste.
4. Verbindung zur Steuerleitung des Computer-Frontpanels.
5. Verbindung zur F_PANEL-Schnittstelle des Computers.

!!! note

    1. Die Schnittstellen 4 und 5 können austauschbar verbunden werden. Das heißt, Schnittstelle 5 kann mit der Steuerleitung des Computer-Frontpanels verbunden werden, während Schnittstelle 4 mit F_PANEL verbunden wird.
    
    2. Auf dem ATX Board befinden sich zwei LEDs. Beide LEDs verhalten sich wie die Power-LED (Blau steht für das ATX-System, Grün für die PC-Stromversorgung). Auf dem ATX Board gibt es keine HDD-LED. Der LED-Status auf der Platine entspricht dem Status der Power-LED am Computer-Frontpanel.

Diagramm der Schnittstellen 4/5:

![interface](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface.png){class="glboxshadow gl-60-desktop"}

## Installation

Sehen Sie sich dieses Video zur Installation des ATX Board an, oder folgen Sie den Schritten unten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3VEjZgzgI44" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. ATX Board und Halterung verschrauben

Befestigen Sie das ATX Board und den ATX-Halterungssatz mit den mitgelieferten Schrauben.

![screwing](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/screwing.jpg){class="glboxshadow gl-90-desktop"}

### 2. ATX Board im PC-Gehäuse installieren

Verbinden Sie die Schnittstellen 4 und 5 jeweils mit der Steuerleitung und der F_PANEL-Schnittstelle des gesteuerten PCs.

![interface connect](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface_connect.jpg){class="glboxshadow gl-90-desktop"}

Mit dem im ATX-Paket enthaltenen 9-PIN-Kabelsatz können Sie eine der Schnittstellen 4/5 des ATX Board mit der Steuerleitung oder der F_PANEL-Schnittstelle des gesteuerten Computers verbinden.
    
Verwenden Sie den Kabelsatz aus Ihrem Computergehäuse, um die andere Schnittstelle 4/5 des ATX Board mit der Steuerleitung oder der F_PANEL-Schnittstelle des gesteuerten Computers zu verbinden.

**Hinweis**: Die Polarität der Schnittstelle kann je nach PC-Gehäuse variieren. Prüfen Sie sie vor der Installation sorgfältig.

Unten finden Sie einige Beispiele, wie Schnittstelle 4/5 mit der F_PANEL-Schnittstelle des gesteuerten Computers verbunden wird.

??? "Für 10-1 pin PANEL"

    Wenn die Pinreihe auf dem Mainboard Ihres gesteuerten Computers, die mit dem Bedienfeld verbunden wird, ein 10-1 pin PANEL ist, wie unten dargestellt:

    ![10-1pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_1.png){class="glboxshadow"}

    Beachten Sie für den Anschluss das Diagramm unten. Stellen Sie sicher, dass die Siebdruckbeschriftung (z. B. HDDLED±, RESET SW, POWER SW, POWERLED+ usw.) nach außen sichtbar ist und nicht nach innen verdeckt wird.

    ![10-1pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_2.jpg){class="glboxshadow"}
    <small>Vorderansicht</small>

    ![10-1pin panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_3.jpg){class="glboxshadow"}
    <small>Rückansicht</small>

    Verwenden Sie anschließend den Kabelsatz aus Ihrem Computergehäuse, um die andere ATX-Board-Schnittstelle mit der Computer-Steuerleitung zu verbinden.

??? "Für 20-5 pin PANEL"

    Wenn die Pinreihe auf dem Mainboard Ihres gesteuerten Computers, die mit dem Bedienfeld verbunden wird, ein 20-5 pin PANEL ist, wie unten dargestellt:

    ![20-5pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_1.jpg){class="glboxshadow"}

    Beachten Sie für den Anschluss das Diagramm unten. Stellen Sie sicher, dass die Siebdruckbeschriftung (z. B. HDDLED±, RESET SW, POWER SW, POWERLED+ usw.) nach außen sichtbar ist und nicht nach innen verdeckt wird.

    ![20-5pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_2.jpg){class="glboxshadow"}
    <small>Vorderansicht</small>

    ![20-5pin panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_3.png){class="glboxshadow"}
    <small>Rückansicht</small>

    Verwenden Sie anschließend den Kabelsatz aus Ihrem Computergehäuse, um die andere ATX-Board-Schnittstelle mit der Computer-Steuerleitung zu verbinden.

??? "Für 20-8 pin PANEL"

    Wenn die Pinreihe auf dem Mainboard Ihres gesteuerten Computers, die mit dem Bedienfeld verbunden wird, ein 20-8 pin PANEL ist, wie unten dargestellt:

    ![20-8pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_1.jpg){class="glboxshadow"}

    Beachten Sie für den Anschluss das Diagramm unten. Stellen Sie sicher, dass die Siebdruckbeschriftung (z. B. HDDLED±, RESET SW, POWER SW, POWERLED+ usw.) nach außen sichtbar ist und nicht nach innen verdeckt wird.

    ![20-8pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_2.png){class="glboxshadow"}

    Verwenden Sie anschließend den Kabelsatz aus Ihrem Computergehäuse, um die andere ATX-Board-Schnittstelle mit der Computer-Steuerleitung zu verbinden.

Das vollständig angeschlossene ATX Board ist unten dargestellt.

![atx board connected](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected1.png){class="glboxshadow gl-90-desktop"}

![atx board connected](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected2.png){class="glboxshadow gl-90-desktop"}

Installieren Sie anschließend die Halterung des ATX Board im Computergehäuse.

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install1.png){class="glboxshadow gl-90-desktop"}

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install2.png){class="glboxshadow gl-90-desktop"}

### 3. ATX Board und KVM verbinden

Verbinden Sie den Type-C-Anschluss des ATX Board über das mitgelieferte USB-Kabel mit dem USB-A-Anschluss des KVM-Geräts (z. B. Comet GL-RM1).

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install3.png){class="glboxshadow gl-90-desktop"}

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install4.png){class="glboxshadow gl-90-desktop"}

Damit ist die Installation des ATX Board abgeschlossen.

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install5.png){class="glboxshadow gl-90-desktop"}

Sie können sich jetzt bei Ihrem KVM anmelden und zu **Accessories** navigieren, um die ATX-Stromversorgung zu steuern.

![atx power](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/atx_power.png){class="glboxshadow gl-90-desktop"}

## FAQ

**F1. Kann ich das GL-ATXPC Board mit KVM-Geräten verwenden, die nicht von GL.iNet stammen?**

A1. Nein. Das GL-ATXPC Board ist Zubehör für GL.iNet KVM-Geräte. Es sollte zusammen mit GL.iNet KVM verwendet werden.

---

**F2. Was kann ich tun, wenn ich nach der Installation des ATX Board die Stromversorgung des gesteuerten Geräts (Ein/Aus) nicht über das KVM steuern kann?**

A2. Versuchen Sie die folgenden Methoden.

- Stellen Sie sicher, dass das gesteuerte Gerät normal ein- und ausgeschaltet werden kann, wenn der physische Ein-/Aus-Schalter am Frontpanel des PC-Gehäuses gedrückt wird.

- Prüfen Sie die Verkabelungspolarität. Versuchen Sie, die Polarität des POWER SW-Steckers auf dem Mainboard des gesteuerten Geräts umzudrehen, um eine falsche Verkabelung auszuschließen.

    ![connector polarity](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/power-sw-connector.png){class="glboxshadow gl-90-desktop"}

- Stellen Sie beim Anschluss an die F_PANEL-Schnittstelle auf dem Mainboard des gesteuerten Geräts sicher, dass die Siebdruckbeschriftung (z. B. HDDLED±, RESET SW, POWER SW, POWERLED+ usw.) nach außen sichtbar ist und nicht nach innen verdeckt wird.

- Aktualisieren Sie die Firmware des KVM.

---

**F3. Kann ich mit einem einzelnen GL.iNet KVM mehrere ATX Boards steuern?**

A3. Die folgenden GL.iNet KVM-Geräte können nur ein ATX Board steuern.

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)

Comet X (GL-RM4PE) unterstützt jedoch bis zu vier ATX Boards gleichzeitig. Comet X bietet vier unabhängige Kanäle auf der Rückseite. Jeder Kanal verfügt über einen HDMI-Anschluss zur Übertragung des Videosignals, einen Type-C-Anschluss zur Übertragung von Tastatur- und Maussignalen sowie einen USB-2.0-Anschluss für USB-Peripheriegeräte (z. B. Fingerbot oder ATX Board).

**Hinweis**: Comet Q (GL-RMQ1) funktioniert nicht mit dem ATX Board.

## Sicherheitshinweise
 
Lesen Sie vor der Verwendung des Geräts alle nachstehenden Sicherheitsinformationen sorgfältig durch. Die nachfolgenden Sicherheitsempfehlungen können nicht sämtliche möglicherweise auftretenden Gefahrensituationen abdecken.

Installieren oder verwenden Sie das Gerät nicht in Umgebungen mit hohen Temperaturen, starker Staubentwicklung, schädlichen Gasen, Brandgefahr, Explosionsgefahr, starken elektromagnetischen Störungen, instabiler Netzspannung, starken Vibrationen oder starker Lärmeinwirkung.

Installieren oder verwenden Sie das Gerät nicht in feuchten Umgebungen, in denen Wasseransammlungen, eindringendes Wasser, Tropfwasser oder Kondensat auftreten können, da dies einen Stromschlag verursachen kann.

Elektromagnetische Störungen können von jedem Gerät ausgehen, das elektromagnetische Signale aussendet. Um Störungen medizinischer Geräte zu vermeiden, befolgen Sie beim Betrieb dieses Geräts insbesondere in Krankenhäusern, ambulanten Gesundheitszentren, Arztpraxen und sonstigen medizinischen Einrichtungen die Anweisungen und Vorgaben des autorisierten Personals, um eine Beeinflussung empfindlicher medizinischer Geräte auszuschließen.

Sofern das Gerät mit einem Netzteil ausgeliefert wird, verwenden Sie zur Stromversorgung ausschließlich das mitgelieferte Netzteil.

Sofern das Gerät mit einem Bildschirm ausgestattet ist und dieser Risse oder Beschädigungen aufweist, verwenden Sie das Gerät nicht weiter. Gebrochenes Glas oder gebrochener Kunststoff kann zu Verletzungen an Händen oder im Gesicht führen.

Sofern das Gerät mit einer Batterie ausgestattet ist, verwenden Sie ausschließlich Batterien, die den Anforderungen der Spezifikation entsprechen. Weist die Batterie sichtbare Beschädigungen auf, tauschen Sie sie aus, da es andernfalls zu Personenschäden kommen kann. Funkendgeräte dürfen nur bei geschlossener Batterieabdeckung betrieben werden.

Bewahren Sie kleine Batterien und Kleinteile, die verschluckt werden könnten, für Kinder unzugänglich auf. Das Verschlucken einer Batterie kann schwere Verletzungen verursachen; nehmen Sie in diesem Fall unverzüglich ärztliche Hilfe in Anspruch.

Vermeiden Sie ein häufiges Umstellen des Geräts. Schalten Sie vor jedem Bewegen oder Transportieren sämtliche Stromversorgungen aus und ziehen Sie alle Netz- und Anschlusskabel ab.

Überlastete Steckdosen, Verlängerungskabel und Steckdosenleisten können Brände und Stromschläge verursachen.

Durch Wärmestau kann sich das Gerät übermäßig erhitzen. Stellen Sie das Gerät daher nicht auf Teppiche oder weiche Unterlagen und sorgen Sie für eine ausreichende Luftzirkulation im Umfeld des Geräts. Stellen Sie das Gerät nicht auf Oberflächen von Gegenständen, die empfindlich auf Wärme reagieren.

Um den einwandfreien Betrieb des Geräts zu gewährleisten, beachten Sie die in den technischen Daten angegebene zulässige Betriebsumgebungstemperatur des Geräts.

Unsachgemäßes Öffnen oder unsachgemäße Instandsetzung kann den Benutzer des Geräts gefährden.

Schalten Sie bei einem Störfall zuerst den Netzschalter aus.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
