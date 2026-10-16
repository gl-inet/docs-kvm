# Cosa fare se lo schermo remoto non mostra l'interfaccia del BIOS {#what-should-i-do-if-the-remote-screen-does-not-show-the-bios-interface}

Se, durante l'accesso al dispositivo controllato tramite KVM, lo schermo remoto non mostra l'interfaccia del BIOS, ad esempio indicando No HDMI Signal, la causa è che il BIOS in genere invia il segnale solo al monitor principale. Di seguito trovi alcuni suggerimenti.

## Portatile {#laptop}

Se il dispositivo controllato è un portatile, lo schermo integrato è il display principale e il KVM esterno non può visualizzare l'interfaccia del BIOS.

## PC desktop {#desktop}

Per i computer desktop, collega il monitor principale alla porta DisplayPort, se disponibile. La maggior parte delle schede grafiche e delle schede madri, infatti, dà priorità all'uscita DP rispetto a HDMI durante l'avvio.

Usa i metodi seguenti per rendere visibile l'interfaccia del BIOS tramite KVM.

- Prova le diverse porte per il monitor. Collega il KVM GL.iNet alla porta impostata come uscita dello schermo principale del computer.

- Usa uno splitter HDMI da 1 a 2, non incluso, per duplicare il segnale dello schermo principale sul dispositivo KVM.

> **Nota**: questo problema può verificarsi anche quando il dispositivo controllato si avvia in **Windows PE**, poiché i segnali del BIOS vengono trasmessi solo al monitor principale e non sono visibili sullo schermo remoto del KVM.

> È consigliato fare una prova con un monitor aggiuntivo. Se anche lo schermo secondario non riceve il segnale, il KVM non riuscirà ad acquisire la schermata del BIOS. Per risolvere il problema, puoi integrare o installare manualmente i driver video nel sistema WinPE.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
