# Så ställer du in EDID för GL.iNet KVM {#how-to-set-edid-for-glinet-kvm}

## Vad är EDID? {#what-is-edid}

EDID (Extended Display Identification Data) är ett standardiserat dataformat som har tagits fram av Video Electronics Standards Association (VESA). Det lagras i skärmens icke-flyktiga minne och innehåller viktig information om skärmen, till exempel tillverkare, maximal upplösning och uppdateringsfrekvens. Enheter som datorer kan automatiskt justera utsignalens parametrar genom att läsa EDID, så att skärmen visar bilden på bästa sätt.

När datorer, bärbara datorer och spelkonsoler ansluts till en skärm läser de i regel automatiskt EDID för att ställa in lämpliga visningsparametrar. Det förhindrar problem som suddig bild och flimmer och ger användaren en tydlig och stabil bild.

EDID-inställningarna i GL.iNet KVM är utformade för att automatiskt matcha skärmens optimala parametrar. När en GL.iNet KVM ansluts till den styrda enheten kan den automatiskt justera bildutgången för att visa bästa möjliga bild genom att läsa skärmens EDID.

## Förinställt EDID {#preset-edid}

Gå till **Settings** -> **Video** -> **EDID** i GL.iNet KVM-konsolen. Där finns några förinställda EDID-inställningar.

![Förinställt EDID](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_preset.jpg){class="glboxshadow"}

**Standard-EDID för GL.iNet KVM passar redan de flesta scenarier och behöver normalt inte ändras**.

I särskilda situationer, till exempel när du ska konfigurera UEFI/BIOS eller anpassa upplösning/uppdateringsfrekvens, kan du välja ett förinställt värde, t.ex. 1920×1280/AUO/60HZ.

## Anpassat EDID {#custom-edid}

Om du inte hittar någon lämplig EDID-kod kan du använda [den här länken](https://github.com/linuxhw/EDID){target="blank"} eller stegen nedan för att anpassa EDID-konfigurationen.

!!! Tip "Tips"

    Det kan vara svårt att hitta ett EDID som exakt matchar önskad upplösning och uppdateringsfrekvens. Du kan använda verktyg för att redigera EDID, till exempel **RTDtool** eller **EEditZ**, för att ändra ett befintligt EDID efter dina behov.

1. Leta upp ett lämpligt EDID [här](https://github.com/linuxhw/EDID){target="blank"} och kopiera det.

2. Logga in på GL.iNet KVM-konsolen och gå till **Settings** -> **EDID**. Växla till läget **Customize**, klistra in parametrarna i inmatningsrutan och klicka på **Set Custom** för att tillämpa inställningarna.

    ![Anpassat EDID](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_customize.png){class="glboxshadow"}

!!! Note "Obs!"

    1. Upplösningen får inte överstiga 2560×1440@60Hz. En upplösning på 2560×1600@60Hz stöds till exempel inte.
    2. Den högsta uppdateringsfrekvensen som stöds är 60 Hz. För upplösningar högre än 1920x1080 rekommenderas en bildfrekvens på 60FPS eller lägre.
    3. Undvik att inkludera sammanflätade (interlaced) upplösningar, eftersom bilden annars visas felaktigt.
    4. Den inmatade EDID-koden får inte innehålla fler än två block.
    5. Grundläggande ljudstöd krävs. Annars kanske ljudkortet inte går att välja på den styrda enheten, vilket leder till att inget ljud hörs.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
