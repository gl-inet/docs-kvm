# De seriële console openen via USB-TTL {#how-to-access-serial-console-via-usb-ttl}

Volg de onderstaande stappen om de USB-TTL-adapter te gebruiken voor seriële foutopsporing:

1. Steek de USB-TTL-adapter in de USB-poort van uw KVM-apparaat.
2. Voer de volgende opdracht uit om de seriële verbinding te openen:

```bash
minicom -D /dev/ttyUSB0 -b 115200
```

Met deze opdracht wordt een seriële verbinding met `/dev/ttyUSB0` tot stand gebracht met een baudrate van `115200`.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
