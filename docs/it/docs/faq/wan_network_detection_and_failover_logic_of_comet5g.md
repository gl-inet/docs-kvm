# Come funzionano il rilevamento della rete WAN e il failover su Comet 5G {#what-is-the-wan-network-detection-and-failover-logic-of-comet-5g}

1. Il sistema usa un rilevamento basato su ping: invia richieste di verifica a tutte le interfacce ogni **3 secondi** e valuta le condizioni di failover ogni **9 secondi**.

2. Se tutti i test ping sull'interfaccia con priorità più alta falliscono nell'arco di **9 secondi**, mentre quella con priorità più bassa rimane raggiungibile, al termine del periodo viene attivato il failover. Se tutte le interfacce sono irraggiungibili, il failover non viene eseguito.

3. Le interfacce contrassegnate come offline continuano a ricevere richieste ping in background.

4. Ripristino: se l'interfaccia con priorità più alta torna raggiungibile tramite ping nell'arco di **9 secondi**, al termine del periodo il sistema torna a usarla.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
