# Så kommer du åt den seriella konsolen via USB TTL {#how-to-access-serial-console-via-usb-ttl}

Följ stegen nedan för att använda USB TTL-adaptern för seriell felsökning:

1. Anslut USB TTL-adaptern till USB-porten på KVM-enheten.
2. Kör följande kommando för att öppna den seriella anslutningen:

```bash
minicom -D /dev/ttyUSB0 -b 115200
```

Kommandot upprättar en seriell anslutning till `/dev/ttyUSB0` med en överföringshastighet på `115200` baud.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
