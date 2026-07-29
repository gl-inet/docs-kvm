# Ausgehende PING/ICMP-Pakete vom KVM deaktivieren

Das KVM-Geraet sendet regelmaessig PING (ICMP)-Pakete, um die Netzwerkverbindung zu pruefen. Dieses Dokument erklaert, wie Sie dieses Verhalten deaktivieren und welche Nebenwirkungen damit verbunden sind.

## Fuer reine Ethernet-Geraete

Bei Geraeten mit ausschliesslich Ethernet-Verbindung, z. B. Comet (GL-RM1) und Comet PoE (GL-RM1PE), sendet das System PING-Pakete an das Standard-Gateway, um die Internetverbindung zu pruefen. Das Ergebnis wird ueber den LED-Status angezeigt.

Fuehren Sie den folgenden Befehl aus, um dieses Verhalten temporaer zu deaktivieren:

```bash
/etc/init.d/S23led stop
```

> **Hinweis:** Wenn dieser Dienst deaktiviert wird, ist auch die **Reset button** nicht verfuegbar.

## Fuer Geraete mit Ethernet und Wi-Fi

Bei Geraeten mit Ethernet und Wi-Fi sendet das System PING-Pakete an oeffentliche DNS-Server, um den Internetzugriff fuer jede Netzwerkschnittstelle zu pruefen. Dieser Mechanismus dient dem dynamischen Multi-WAN-Failover und stellt sicher, dass das Geraet zu Wi-Fi wechseln kann, wenn die Ethernet-Verbindung den Internetzugriff verliert.

Fuehren Sie den folgenden Befehl aus, um dieses Verhalten temporaer zu deaktivieren:

```bash
/etc/init.d/S98multi-wan stop
```

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
