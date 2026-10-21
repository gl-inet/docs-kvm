# Hur fungerar identifiering av WAN-nätverk och redundans (failover) i Comet 5G? {#what-is-the-wan-network-detection-and-failover-logic-of-comet-5g}

1. Systemet använder ping-baserad identifiering. Det skickar testpaket till alla gränssnitt var **3:e sekund** och utvärderar villkoren för redundansväxling var **9:e sekund**.

2. Om alla ping-tester till gränssnittet med högre prioritet misslyckas under en period på **9 sekunder** medan gränssnittet med lägre prioritet fortfarande kan nås, utlöses en redundansväxling efter den perioden. Ingen redundansväxling sker om inget gränssnitt kan nås.

3. Gränssnitt som har markerats som offline fortsätter att ta emot ping-testpaket i bakgrunden.

4. Återställning: om gränssnittet med högre prioritet åter svarar på ping inom **9 sekunder** växlar systemet tillbaka till det efter den perioden.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
