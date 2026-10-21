# Vad gör jag om fjärrskärmen blir svart eller visar ingen HDMI-signal? {#what-should-i-do-if-the-remote-screen-goes-blank-or-shows-no-hdmi-signal}

Om fjärrskärmen blir tom eller inte visar någon HDMI-signal när du kommer åt den styrda enheten via KVM-enheten följer du felsökningsstegen nedan.

![Vit skärm](https://static.gl-inet.com/docs/kvm/faq/blank_screen/white_screen.png){class="glboxshadow"}
<small>(Vit skärm)</small>

![Svart skärm](https://static.gl-inet.com/docs/kvm/faq/blank_screen/black_screen.png){class="glboxshadow"}
<small>(Svart skärm)</small>

Kontrollera först om problemet har med videoöverföringen att göra. Logga in på din KVM, gå till **Settings** -> **Video** -> **Transfer** och ställ in överföringsläget på **Direct**.

![Ändra överföringsläge](https://static.gl-inet.com/docs/kvm/faq/blank_screen/change_transfer.png){class="glboxshadow" width="360"}

Om problemet kvarstår kontrollerar du de möjliga orsakerna nedan en i taget.

## Kontrollera maskinvaruanslutningen {#check-hardware-connection}

1. **Defekt HDMI-kabel**

    Åldrade HDMI-kablar, oxiderade kontakter eller interna kabelbrott kan avbryta signalöverföringen. Byt till en HDMI-kabel av hög kvalitet.

    Du kan också kontrollera HDMI-signalens status i KVM-konsolen. Leta upp skärmikonen i det nedre högra hörnet och kontrollera om den visar "No HDMI signal".

    ![Ingen HDMI-signal](https://static.gl-inet.com/docs/kvm/faq/blank_screen/no_hdmi_signal.png){class="glboxshadow"}

2. **Felaktig anslutning**

    Om den styrda enheten är en stationär dator ska du kontrollera att KVM-enhetens **HDMI IN**-port är ansluten till HDMI OUT-porten på datorns grafikkort eller moderkort. Kontrollera att kontakten sitter i ordentligt. För enheter med flera HDMI-utgångar (t.ex. separat grafikkort + utgång på moderkortet) kan du prova att byta till en annan port.

    Om den styrda enheten är en bärbar dator ska du kontrollera att KVM-enhetens **HDMI IN**-port är ansluten till den bärbara datorns HDMI OUT-port.

    Tips: Vissa KVM-modeller (till exempel Comet Pro och Comet 5G) har två HDMI-portar. Kontrollera att HDMI-kabeln från den styrda enheten är ansluten till KVM-enhetens HDMI IN-port. Om den är ansluten till HDMI OUT identifieras ingen HDMI-signal i KVM-konsolen.

3. **Felaktig användning av adaptrar**

    Om en HDMI-adapter behövs använder du en adapter för **VGA till HDMI** för att ansluta den styrda enheten till GL.iNet KVM-enhetens HDMI IN-port.

    Om du använder en adapter för HDMI till VGA för den här anslutningen överförs videosignalen inte korrekt, vilket ger en tom skärm.

    ![Jämförelse av adaptrar](https://static.gl-inet.com/docs/kvm/faq/blank_screen/adapter_comparison.png){class="glboxshadow"}

## Kontrollera webbläsarinställningarna {#check-browser-settings}

Om du kommer åt den styrda enheten via en webbläsare och skärmen är tom kan du prova följande metoder:

1. **Testa med flera webbläsare.** Prova Chrome, Firefox, Edge osv. för att avgöra om problemet är specifikt för en viss webbläsare.

2. **Inaktivera tillägg för skydd mot WebRTC-läckor eller styrning av WebRTC.** Om du har installerat tillägg i webbläsaren som kan påverka WebRTC-anslutningar inaktiverar du dem och testar igen. Du kan också gå till webbläsarens inställningar för sekretess och säkerhet och kontrollera att webbläsaren tillåter WebRTC-anslutningar.

    ![WebRTC](https://static.gl-inet.com/docs/kvm/faq/blank_screen/webrtc.png){class="glboxshadow"}

## Kontrollera den styrda enhetens status och inställningar {#check-controlled-device-status-and-settings}

1. **Enheten är inte påslagen eller är i viloläge**

    Kontrollera att den styrda enheten är helt påslagen och inte är i vilo- eller viloläge med strömsparfunktion på grund av energiinställningarna (väck den vid behov med knapparna på plats).

2. **Felaktiga grafikkortsdrivrutiner på den styrda enheten**

    Avinstallerade eller skadade grafikkortsdrivrutiner kan leda till att ingen videosignal matas ut. Uppdatera eller installera om grafikkortsdrivrutinerna på den styrda enheten (när du är inloggad lokalt).

3. **Felaktig anslutning av separat och integrerat grafikkort**

    Om den styrda enheten har både ett separat och ett integrerat grafikkort ska du kontrollera att HDMI-kabeln är ansluten till rätt grafikport (t.ex. anslut HDMI-kabeln till porten på det separata grafikkortet om ett sådant är installerat).

4. **Felaktiga skärminställningar på den styrda enheten (låg sannolikhet)**

    När GL.iNet KVM ansluts till den styrda enheten justerar den automatiskt bildutgången genom att läsa skärmens EDID för optimal prestanda. I de flesta fall passar standardkonfigurationen för EDID de flesta scenarier och behöver inte ändras.

    Om den styrda enheten är kompatibel med vanliga skärmar är det osannolikt att tomma skärmar eller visningsproblem uppstår vid åtkomst via GLKVM. Vissa specifika kompatibilitetsproblem (t.ex. Linux-system + ASUS-skärm) kan dock ge tomma skärmar när GLKVM används.

    Kontrollera om den styrda enheten är kompatibel med vanliga skärmar och om den har kompatibilitetsproblem med en viss skärm.

5. **Problem med upplösningen**

    När GLKVM ansluts till vissa operativsystem (t.ex. Proxmox VE Hypervisor) kan den misslyckas med att förhandla fram en tillgänglig skärmupplösning korrekt, vilket leder till visningsproblem. Det kan lösas genom att justera upplösningen manuellt på den styrda enheten.

    Här är en guide som referens för hur du ändrar systemupplösningen i Proxmox VE Hypervisor.

    1. Öppna PVE-terminalen och ange kommandot nedan för att redigera filen `/etc/default/grub`.

        ```
        nano /etc/default/grub
        ```

    2. Lägg till följande rad.

        ```
        GRUB_CMDLINE_LINUX_DEFAULT="quiet gfxpayload=text nomodeset"
        ```

    3. Avkommentera raden `GRUB_GFXMODE` genom att ta bort `#` och ange önskad upplösning, till exempel `1024x768`.

        ```
        GRUB_GFXMODE=1024x768
        ```

    4. Tryck på `Ctrl + O` och sedan på Enter för att spara konfigurationen.

    5. Tryck på `Ctrl + X` för att avsluta redigeraren nano.

    6. Ange kommandot nedan för att tillämpa konfigurationen.

        ```
        update-grub
        ```

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
