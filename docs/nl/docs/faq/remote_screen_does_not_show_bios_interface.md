# Wat moet ik doen als het externe scherm de BIOS-interface niet toont? {#what-should-i-do-if-the-remote-screen-does-not-show-the-bios-interface}

Als het externe scherm bij toegang tot het bestuurde apparaat via de KVM de BIOS-interface niet toont (bijvoorbeeld No HDMI Signal), komt dit doordat de BIOS-interface doorgaans alleen naar het primaire beeldscherm wordt uitgevoerd. Hieronder vindt u enkele suggesties.

## Laptop {#laptop}

Als het bestuurde apparaat een laptop is, fungeert het ingebouwde scherm als primair beeldscherm, waardoor de externe KVM de BIOS-interface niet kan weergeven.

## Desktop {#desktop}

Sluit bij desktopapparaten de primaire monitor indien mogelijk aan op de DisplayPort-poort. De meeste grafische kaarten en moederborden geven tijdens het opstarten namelijk voorrang aan DP-uitvoer boven HDMI.

Gebruik de onderstaande methoden om de BIOS-interface via de KVM zichtbaar te maken.
    
- Probeer verschillende monitorpoorten. Sluit de GL.iNet KVM aan op de poort die op uw computer als primaire beelduitvoer is ingesteld.
    
- Gebruik een HDMI-splitter van 1 naar 2 (niet meegeleverd) om het signaal van het primaire beeldscherm te dupliceren naar het KVM-apparaat.

> **Opmerking**: Dit probleem kan ook optreden wanneer het bestuurde apparaat opstart in **Windows PE**, omdat BIOS-signalen alleen naar de primaire monitor worden verzonden en niet op het externe KVM-scherm kunnen worden weergegeven.

> Het is raadzaam om te testen met een extra monitor. Als het tweede beeldscherm nog steeds geen signaal ontvangt, kan de KVM het BIOS-scherm ook niet vastleggen. U kunt dit oplossen door handmatig beeldschermstuurprogramma's in het WinPE-systeem te integreren of te installeren.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
