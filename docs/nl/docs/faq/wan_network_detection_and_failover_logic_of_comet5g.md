# Wat is de logica voor WAN-netwerkdetectie en failover van de Comet 5G? {#what-is-the-wan-network-detection-and-failover-logic-of-comet-5g}

1. Het systeem gebruikt detectie op basis van ping: elke **3 seconden** worden er tests naar alle interfaces verzonden en elke **9 seconden** worden de voorwaarden voor failover beoordeeld.  
   
2. Als binnen een periode van **9 seconden** alle pingtests naar de interface met hogere prioriteit mislukken, terwijl de interface met lagere prioriteit bereikbaar blijft, wordt na die periode een failover uitgevoerd. Als geen enkele interface bereikbaar is, vindt er geen failover plaats.  
   
3. Interfaces die als offline zijn gemarkeerd, blijven op de achtergrond pingtests ontvangen.  
   
4. Herstel: als de interface met hogere prioriteit binnen **9 seconden** weer via ping bereikbaar is, schakelt het systeem na die periode terug naar deze interface.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
