# Ausgehende PING/ICMP-Pakete vom KVM deaktivieren {#how-to-disable-outgoing-pingicmp-packets-from-kvm}

Das KVM-Gerät sendet regelmäßig PING (ICMP)-Pakete, um die Netzwerkverbindung zu prüfen. Dieses Dokument erklärt, wie Sie dieses Verhalten deaktivieren und welche Nebenwirkungen damit verbunden sind.

## Für reine Ethernet-Geräte {#for-ethernet-only-devices}

Bei Geräten mit ausschließlich Ethernet-Verbindung, z. B. Comet (GL-RM1) und Comet PoE (GL-RM1PE), sendet das System PING-Pakete an das Standard-Gateway, um die Internetverbindung zu prüfen. Das Ergebnis wird über den LED-Status angezeigt.

Führen Sie den folgenden Befehl aus, um dieses Verhalten temporär zu deaktivieren:

```bash
/etc/init.d/S23led stop
```

> **Hinweis:** Wenn dieser Dienst deaktiviert wird, ist auch die **Reset button** nicht verfügbar.

## Für Geräte mit Ethernet und Wi-Fi {#for-devices-with-both-ethernet-and-wi-fi}

Bei Geräten mit Ethernet und Wi-Fi sendet das System PING-Pakete an öffentliche DNS-Server, um den Internetzugriff für jede Netzwerkschnittstelle zu prüfen. Dieser Mechanismus dient dem dynamischen Multi-WAN-Failover und stellt sicher, dass das Gerät zu Wi-Fi wechseln kann, wenn die Ethernet-Verbindung den Internetzugriff verliert.

Führen Sie den folgenden Befehl aus, um dieses Verhalten temporär zu deaktivieren:

```bash
/etc/init.d/S98multi-wan stop
```

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
