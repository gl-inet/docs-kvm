# Auf die serielle Konsole ueber USB TTL zugreifen

Fuehren Sie die folgenden Schritte aus, um den USB TTL-Adapter fuer serielles Debugging zu verwenden:

1. Stecken Sie den USB TTL-Adapter in den USB-Port Ihres KVM-Geraets.
2. Fuehren Sie den folgenden Befehl aus, um die serielle Verbindung zu oeffnen:

```bash
minicom -D /dev/ttyUSB0 -b 115200
```

Dieser Befehl stellt eine serielle Verbindung zu `/dev/ttyUSB0` mit einer Baudrate von `115200` her.

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
