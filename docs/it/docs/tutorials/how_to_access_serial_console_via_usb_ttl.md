# Come accedere alla console seriale tramite USB TTL {#how-to-access-serial-console-via-usb-ttl}

Segui i passaggi indicati di seguito per usare l'adattatore USB TTL per il debug seriale:

1. Collega l'adattatore USB TTL alla porta USB del dispositivo KVM.
2. Esegui il comando seguente per aprire la connessione alla porta seriale:

```bash
minicom -D /dev/ttyUSB0 -b 115200
```

Questo comando stabilisce una connessione seriale con `/dev/ttyUSB0` a una velocità di `115200` baud.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
