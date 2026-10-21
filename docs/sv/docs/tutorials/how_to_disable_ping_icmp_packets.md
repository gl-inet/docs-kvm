# Så inaktiverar du utgående PING/ICMP-paket från KVM-enheten {#how-to-disable-outgoing-pingicmp-packets-from-kvm}

KVM-enheten skickar regelbundet PING-paket (ICMP) för att identifiera nätverksanslutningen. Det här dokumentet beskriver hur du inaktiverar beteendet och vilka sidoeffekter det har.

## För enheter med endast Ethernet {#for-ethernet-only-devices}

För enheter med endast Ethernet-anslutning, till exempel Comet (GL-RM1) och Comet PoE (GL-RM1PE), skickar systemet PING-paket till standardgatewayen för att kontrollera internetanslutningen. Resultatet visas via lysdiodens status.

Kör följande kommando för att tillfälligt inaktivera beteendet:

```bash
/etc/init.d/S23led stop
```

> **Obs!** Om du inaktiverar tjänsten blir även **återställningsknappen (Reset)** otillgänglig.

## För enheter med både Ethernet och Wi-Fi {#for-devices-with-both-ethernet-and-wi-fi}

För enheter med både Ethernet och Wi-Fi skickar systemet PING-paket till offentliga DNS-servrar för att verifiera internetåtkomsten för varje nätverksgränssnitt. Mekanismen används för dynamisk redundans (failover) mellan flera WAN-anslutningar, så att enheten kan växla till Wi-Fi om Ethernet-anslutningen förlorar internetåtkomsten.

Kör följande kommando för att tillfälligt inaktivera beteendet:

```bash
/etc/init.d/S98multi-wan stop
```

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
