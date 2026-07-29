# Kurze FAQs zu GL.iNet KVM

Dies ist eine kurze Q&A-Sammlung zu GL.iNet KVM mit schnellen Antworten auf häufige grundlegende Fragen.

## Grundlegende Informationen

**Q1. Welche Geräte kann GL.iNet KVM steuern?**

A1. GL.iNet KVM kann jedes Gerät steuern, das HDMI-Ausgabe und USB-Eingabe verwendet, z. B. Laptops, Desktops, Raspberry Pi, Mini-Hosts usw.

Zusätzlich kann Comet Q (GL-RMQ1) jedes Gerät steuern, dessen USB-C-Anschluss DisplayPort Alt Mode für die Videoausgabe unterstützt; ein HDMI-Anschluss ist nicht erforderlich. Dazu gehören unter anderem bestimmte iPhones, iPads, Android-Telefone, MacBooks, Mac minis und die meisten modernen Windows-Laptops. Details finden Sie [hier](../user_guide/gl-rmq1/product_overview.md#compatibility).

---

**Q2. Muss ich Software installieren, um GL.iNet KVM zu verwenden?**

A2. Auf dem gesteuerten Gerät muss keine Software installiert werden. Es kann Windows, macOS, ChromeOS, Linux usw. verwenden.

Ob auf dem steuernden Gerät Software installiert werden muss, hängt davon ab, wie Sie auf das KVM zugreifen möchten.

??? "Nearby Control (for Comet 5G only)"

    **Hinweis**: Diese Methode ist nur auf Comet 5G (GL-RM10RC) verfügbar.

    Comet 5G bietet Wi-Fi Nearby Control für schnelle lokale Verwaltung ohne kabelgebundene Verbindungen. Schalten Sie den WLAN-Netzwerkmodus des Comet 5G einfach in den AP-Modus. Daraufhin erzeugt das Gerät eine eindeutige WLAN-SSID. Verbinden Sie sich mit dieser SSID, um sicher auf die Konsole des Comet 5G zuzugreifen. Details finden Sie [hier](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control).

    Durch Aktivieren des AP-Modus wird Comet 5G von seinem vorgelagerten WLAN getrennt und stellt nur Zugriff in der Nähe bereit, ohne Internetverbindung.

??? "Local Control (for Comet X only)"

    **Hinweis**: Diese Methode ist nur auf Comet X (GL-RM4PE) verfügbar.

    Comet X bietet einen HDMI OUT-Anschluss und zwei zusätzliche USB-Anschlüsse und eignet sich damit gut für lokale Fehlerbehebung, Konfiguration und Betriebssysteminstallation. Schließen Sie einfach Monitor, Maus und Tastatur an, um lokale Plug-and-play-Hardwaresteuerung zu nutzen. Details finden Sie [hier](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control).

??? "LAN Access"

    Wenn Sie über dasselbe lokale Netzwerk (LAN) auf KVM zugreifen möchten, muss auf dem steuernden Gerät keine Software installiert werden.

    Öffnen Sie einfach einen Browser auf dem steuernden Gerät und geben Sie entweder die IP-Adresse des KVM oder `glkvm.local` in die Adressleiste ein, um lokal auf KVM zuzugreifen.

    Details finden Sie [hier](local_access_via_browser.md){target="_blank"}.

??? "Remote Access"

    - **GLKVM App**

        Wenn auf Ihrem steuernden Gerät Windows, macOS, Android oder iOS läuft, können Sie darauf die [GLKVM App](https://www.gl-inet.com/app-rm/){target="_blank"} installieren und remote auf Ihr KVM zugreifen. So können Sie auch auf das gesteuerte Gerät zugreifen.

        Details finden Sie [hier](remote_access_via_glkvm_app.md){target="_blank"}.

    - **Cloud Service**

        Diese Methode ist ideal, wenn Sie die GLKVM App nicht installieren können oder nicht verwenden möchten.

        Binden Sie Ihr KVM an den Cloud-Dienst. Danach können Sie auf dem steuernden Gerät in einem Webbrowser `glkvm.com` eingeben, um ohne Installation der GLKVM App remote auf Ihr KVM und damit auf das gesteuerte Gerät zuzugreifen.

        Details finden Sie [hier](remote_access_via_cloud.md){target="_blank"}.

    - **Tailscale**

        Diese Methode eignet sich, wenn Sie die GLKVM App oder den Cloud-Dienst nicht verwenden können oder nicht verwenden möchten. Sie erfordert jedoch mehr Schritte.

        Binden Sie Ihr KVM und das steuernde Gerät an dasselbe Tailscale-Konto. Danach können Sie auf dem steuernden Gerät die virtuelle Tailscale-IP des KVM in einen Webbrowser eingeben, um remote auf Ihr KVM und damit auf das gesteuerte Gerät zuzugreifen.

        Details finden Sie [hier](remote_access_via_tailscale.md){target="_blank"}.

    - **ZeroTier**

        Diese Methode eignet sich, wenn Sie die GLKVM App oder den Cloud-Dienst nicht verwenden können oder nicht verwenden möchten. Sie erfordert jedoch mehr Schritte.

        Fügen Sie Ihr KVM und das steuernde Gerät demselben ZeroTier-Netzwerk hinzu. Danach können Sie auf dem steuernden Gerät die ZeroTier-IP des KVM in einen Webbrowser eingeben, um remote auf Ihr KVM und damit auf das gesteuerte Gerät zuzugreifen.

        Details finden Sie [hier](remote_access_via_zerotier.md){target="_blank"}.

    - **NetBird**

        Diese Methode eignet sich, wenn Sie die GLKVM App oder den Cloud-Dienst nicht verwenden können oder nicht verwenden möchten. Sie erfordert jedoch mehr Schritte.

        [NetBird](https://netbird.io/){target="_blank"} ist eine Open-Source-Zero-Trust-Netzwerkplattform, mit der Sie sichere private Netzwerke für den privaten und geschäftlichen Einsatz erstellen können. Als WireGuard®-basiertes Overlay-Netzwerk ermöglicht NetBird jederzeit und überall sicheren Zugriff auf Ihre Geräte.

        GL.iNet KVM integriert NetBird, sodass Sie es für den Fernzugriff an das virtuelle NetBird-Netzwerk binden können.

        Details finden Sie [hier](remote_access_via_netbird.md){target="_blank"}.

---

**Q3. Wie greife ich auf GL.iNet KVM zu?**

A3. Grundsätzlich können Sie auf GL.iNet KVM lokal oder remote über verschiedene Wege zugreifen:

- [LAN-Zugriff per Webbrowser](local_access_via_browser.md){target="_blank"}
- [Fernzugriff über Cloud-Dienst](remote_access_via_cloud.md){target="_blank"}
- [Fernzugriff über GLKVM App](remote_access_via_glkvm_app.md){target="_blank"}
- [Fernzugriff über Tailscale](remote_access_via_tailscale.md){target="_blank"}
- [Fernzugriff über ZeroTier](remote_access_via_zerotier.md){target="_blank"}
- [Fernzugriff über NetBird](remote_access_via_netbird.md){target="_blank"}

Außerdem unterstützen einige GL.iNet KVM-Modelle Nearby Control oder Local Control, sodass Sie vor Ort auf sie zugreifen können, ohne eine Verbindung zu einem anderen Router herzustellen.

- [Nearby Control (for Comet 5G only)](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control){target="_blank"}
- [Local Control (for Comet X only)](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control){target="_blank"}

---

**Q4. Muss ich Ports öffnen (gegenüber WAN freigeben), damit GL.iNet KVM Fernzugriff ermöglicht?**

A4. Nein. Es werden keine offenen Ports und nicht einmal eine öffentliche IP benötigt.

---

**Q5. Unterstützt die GLKVM App ChromeOS/Linux?**

A5. Nein. Derzeit unterstützt die GLKVM App keine Installation auf ChromeOS oder Linux OS.

Wenn auf Ihrem steuernden Gerät ChromeOS/Linux OS läuft, kann die GLKVM App nicht installiert werden. Fernzugriff auf das gesteuerte Gerät über die GLKVM App wird daher nicht unterstützt.

Sie können jedoch <u> Cloud Service</u>, <u>Tailscale</u>, <u>ZeroTier</u> oder <u>NetBird</u> verwenden, um Fernzugriff zu erreichen. Details finden Sie oben in Q3.

Alternativ können Sie lokal per Webbrowser auf das KVM zugreifen. Details finden Sie oben in Q3.

---

**Q7. Kann Comet (GL-RM1) eine Verbindung zu einem drahtlosen Netzwerk herstellen?**

A7. Nein. Comet (GL-RM1) unterstützt keine drahtlose Netzwerkverbindung.

Für den Internetzugang muss es über ein Ethernet-Kabel mit einem Netzwerkgerät (z. B. einem Router) verbunden werden.

Wenn Sie ein KVM bevorzugen, das WLAN unterstützt, können Sie die folgenden Modelle in Betracht ziehen:

* [Comet Pro (GL-RM10)](https://www.gl-inet.com/products/gl-rm10/){target="_blank"}
* [Comet 5G (GL-RM10RC)](https://www.gl-inet.com/products/gl-rm10rc/){target="_blank"}
* [Comet Q (GL-RMQ1)](https://www.gl-inet.com/products/gl-rmq1/){target="_blank"}

---

## Stromsteuerung

**Q1. Kann ein GL.iNet KVM das Zielgerät remote ein- und ausschalten?**

A1. GL.iNet KVM ermöglicht das remote Ein- und Ausschalten des Zielgeräts über die folgenden Methoden:

- Wake-on-LAN (integrierter Softwaredienst)

- [ATX board](../user_guide/gl-atx-board/index.md){target="_blank"} (separat erhältlich; funktioniert nicht mit Comet Q.)

- [FingerBot](../user_guide/gl-fgb-01/index.md){target="_blank"} (separat erhältlich; funktioniert nicht mit Comet Q.)

---

**Q2. Wie verwende ich ATX Board für Remote-Stromsteuerung?**

A2. Bitte lesen Sie das [ATX Board User Guide](../user_guide/gl-atx-board/index.md){target="_blank"}.

---

## Funktionen

!!! Tip

    Unten finden Sie FAQs zu mehreren häufig verwendeten Funktionen. Vollständige Funktionsdetails finden Sie im jeweiligen [Benutzerhandbuch](../user_guide/index.md).

**Q1. Muss ich KVM Cloud Service verwenden?**

A1. Nein. Der Cloud Service ist optional.

Wenn Sie für Fernzugriff nicht auf die Cloud angewiesen sind, können Sie Drittanbieter-Overlay-Netzwerktools wie Tailscale, ZeroTier und NetBird verwenden.

---

**Q2. Kann ich mit einem einzelnen GL.iNet KVM mehrere Geräte steuern?**

A2. Die folgenden GL.iNet KVMs können nur ein Zielgerät steuern:

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)
* Comet Q (GL-RMQ1)

Comet X (GL-RM4PE) kann jedoch mit bis zu vier Zielgeräten gleichzeitig verbunden werden, wobei jeweils nur ein Gerät gesteuert werden kann. Sie können vor Ort über die physische Taste an der Vorderseite oder unterwegs über die Remote-Konsole schnell zwischen den vier verbundenen Geräten wechseln.

Comet X (GL-RM4PE) verfügt auf der Rückseite über vier unabhängige Kanäle. Jeder Kanal besitzt einen HDMI-Anschluss für die Videosignalübertragung, einen Type-C-Anschluss für Tastatur- und Maussignalübertragung und einen USB 2.0-Anschluss für USB-Peripheriegeräte (z. B. Fingerbot oder ATX board).

---

**Q3. Was ist Wake-on-Lan?**

A3. Wake-on-LAN (WOL) ist eine Technologie, mit der ein Computer oder Gerät über ein Netzwerk remote eingeschaltet oder aus einem Energiesparzustand geweckt werden kann. Dazu wird ein "magic packet" mit der MAC-Adresse des Zielgeräts gesendet, wodurch das Gerät gestartet wird. Typische Anwendungen sind Remote-Administration, energiesparende Standby-Konfigurationen und zentrale Systemverwaltung.

---

**Q4. Unterstützt GL.iNet KVM Mouse Jiggle?**

A4. Ja. Sie können Mouse Jiggle in der KVM-Konsole aktivieren.

Die Mouse Jiggler-Funktion simuliert unauffällige, regelmäßige Mausbewegungen, um zu verhindern, dass der Computer (also das gesteuerte Gerät) bei längerer Inaktivität in den Ruhezustand wechselt, z. B. während Remote-Meetings oder Serververwaltung.

---

**Q5. Unterstützt GL.iNet KVM Zwei-Wege-Audio?**

A5. Ja. Sie können Speaker und Microphone in der KVM-Konsole aktivieren, um Zwei-Wege-Audioübertragung zu nutzen.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
