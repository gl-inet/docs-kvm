# Uitgaande PING/ICMP-pakketten van de KVM uitschakelen {#how-to-disable-outgoing-pingicmp-packets-from-kvm}

Het KVM-apparaat verzendt periodiek PING-pakketten (ICMP) om de netwerkverbinding te controleren. In dit document leest u hoe u dit gedrag uitschakelt en wat de bijbehorende neveneffecten zijn.

## Voor apparaten met alleen ethernet {#for-ethernet-only-devices}

Bij apparaten met alleen een ethernetverbinding, zoals de Comet (GL-RM1) en de Comet PoE (GL-RM1PE), verzendt het systeem PING-pakketten naar de standaardgateway om de internetverbinding te controleren. Het resultaat wordt aangegeven met de ledstatus.

Voer de volgende opdracht uit om dit gedrag tijdelijk uit te schakelen:

```bash
/etc/init.d/S23led stop
```

> **Opmerking:** Als u deze service uitschakelt, is ook de **resetknop** niet meer beschikbaar.

## Voor apparaten met ethernet en wifi {#for-devices-with-both-ethernet-and-wi-fi}

Bij apparaten met zowel ethernet als wifi verzendt het systeem PING-pakketten naar openbare DNS-servers om voor elke netwerkinterface de internettoegang te controleren. Dit mechanisme wordt gebruikt voor dynamische multi-WAN-failover, zodat het apparaat naar wifi kan overschakelen als de ethernetverbinding geen internettoegang meer heeft.

Voer de volgende opdracht uit om dit gedrag tijdelijk uit te schakelen:

```bash
/etc/init.d/S98multi-wan stop
```

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
