# STUN-Erkennung der öffentlichen IP seltener ausführen {#how-to-reduce-stun-public-ip-detection-frequency}

Das KVM-Gerät verwendet STUN-Anfragen, um seine öffentliche IP-Adresse für den Fernzugriff zu erkennen. Standardmäßig sendet das Gerät in regelmäßigen Abständen STUN-Erkennungsanfragen. Wenn Sie nur über ein lokales Netzwerk oder VPN auf das KVM zugreifen, können Sie die Konfiguration anpassen, um die STUN-Anfragehäufigkeit zu reduzieren.

Melden Sie sich per SSH am KVM an oder öffnen Sie **Toolbox** > **Terminal** in der KVM-Konsole. Sichern Sie die vorhandene Override-Datei, bevor Sie sie bearbeiten:

```bash
cp -p /etc/kvmd/override.yaml /etc/kvmd/override.yaml.bak
vi /etc/kvmd/override.yaml
```

Wenn bereits eine Sicherung namens `override.yaml.bak` vorhanden ist, wählen Sie einen anderen Dateinamen, um diese zu erhalten. Falls `override.yaml` nicht existiert, überspringen Sie den Sicherungsbefehl und erstellen Sie die Datei im Editor.

Fügen Sie die folgende Einstellung in die Datei ein und behalten Sie alle vorhandenen Overrides bei:

```yaml
janus:
    check:
        retries: 10000
```

Wenn bereits ein Abschnitt `janus` existiert, ergänzen oder aktualisieren Sie darin `check.retries`. Falls unter `janus` bereits `check` vorhanden ist, aktualisieren Sie dort den Wert `retries` oder fügen Sie ihn hinzu. Erstellen Sie keine doppelten Schlüssel `janus` oder `check`. Verwenden Sie Leerzeichen für die YAML-Einrückung und speichern Sie die Datei anschließend.

> **Hinweis:** Diese Konfiguration reduziert die Anzahl der von Janus initiierten STUN-Anfragen erheblich. Sie kann jedoch auch die Erfolgsrate von STUN Hole Punching für externe Netzwerknutzung verringern. **Wenden Sie dies nur an, wenn Sie ausschließlich über ein lokales Netzwerk oder VPN auf das KVM zugreifen.**

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
