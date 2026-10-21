# Vad gör jag om fjärrskärmen inte visar BIOS-gränssnittet? {#what-should-i-do-if-the-remote-screen-does-not-show-the-bios-interface}

Om fjärrskärmen inte visar BIOS-gränssnittet (t.ex. No HDMI Signal) när du kommer åt den styrda enheten via KVM-enheten beror det på att BIOS-gränssnittet vanligtvis bara visas på den primära skärmen. Här är några förslag.

## Bärbar dator {#laptop}

Om den styrda enheten är en bärbar dator fungerar den inbyggda skärmen som primär skärm, och därför kan den externa KVM-enheten inte visa BIOS-gränssnittet.

## Stationär dator {#desktop}

För stationära datorer ansluter du den primära skärmen till DisplayPort-porten om en sådan finns. Det beror på att de flesta grafikkort och moderkort prioriterar DP-utgången framför HDMI vid uppstart.

Använd metoderna nedan för att göra BIOS-gränssnittet synligt via KVM-enheten.

- Växla mellan olika skärmportar. Anslut GL.iNet KVM till den port som är inställd som primär skärmutgång på datorn.

- Använd en HDMI-splitter med en ingång och två utgångar (ingår inte) för att duplicera den primära skärmsignalen till KVM-enheten.

> **Obs!** Problemet kan även uppstå när den styrda enheten startar i **Windows PE**, eftersom BIOS-signalerna bara skickas till den primära skärmen och inte kan visas på KVM-enhetens fjärrskärm.

> Vi rekommenderar att du testar med en extra skärm. Om den sekundära skärmen fortfarande inte får någon signal kan KVM-enheten inte fånga BIOS-skärmen. Du kan lösa detta genom att manuellt integrera eller installera skärmdrivrutiner i WinPE-systemet.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
