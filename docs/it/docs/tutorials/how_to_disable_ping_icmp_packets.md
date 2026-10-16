# Come disattivare l'invio di pacchetti PING/ICMP dal KVM {#how-to-disable-outgoing-pingicmp-packets-from-kvm}

Il dispositivo KVM invia periodicamente pacchetti PING (ICMP) per verificare la connettività di rete. Questo documento spiega come disattivare tale comportamento e quali effetti collaterali comporta.

## Dispositivi con sola connessione Ethernet {#for-ethernet-only-devices}

Sui dispositivi dotati soltanto di connessione Ethernet, come Comet (GL-RM1) e Comet PoE (GL-RM1PE), il sistema invia pacchetti PING al gateway predefinito per verificare la connettività Internet. Il risultato viene indicato dallo stato del LED.

Per disattivare temporaneamente questo comportamento, esegui il comando seguente:

```bash
/etc/init.d/S23led stop
```

> **Nota:** la disattivazione di questo servizio rende inutilizzabile anche il **pulsante Reset**.

## Dispositivi con Ethernet e Wi-Fi {#for-devices-with-both-ethernet-and-wi-fi}

Sui dispositivi dotati sia di Ethernet sia di Wi-Fi, il sistema invia pacchetti PING a server DNS pubblici per verificare l'accesso a Internet di ciascuna interfaccia di rete. Questo meccanismo consente il failover dinamico multi-WAN, permettendo al dispositivo di passare al Wi-Fi se la connessione Ethernet perde l'accesso a Internet.

Per disattivare temporaneamente questo comportamento, esegui il comando seguente:

```bash
/etc/init.d/S98multi-wan stop
```

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
