# Snabba svar om GL.iNet KVM {#quick-faqs-about-glinet-kvm}

Det här är en kort samling frågor och svar om GL.iNet KVM med snabba svar på några vanliga grundläggande frågor.

## Grundläggande information {#basic-information}

**F1. Vilka enheter kan GL.iNet KVM styra?**

S1. GL.iNet KVM kan styra alla enheter som använder HDMI-utgång och USB-ingång, till exempel bärbara datorer, stationära datorer, Raspberry Pi och minidatorer.

Dessutom kan Comet Q (GL-RMQ1) styra alla enheter vars USB-C-port stöder DisplayPort Alt Mode för videoutgång, och ingen HDMI-port behövs. Detta omfattar bland annat vissa iPhone- och iPad-modeller, Android-telefoner, MacBook, Mac mini och de flesta moderna bärbara Windows-datorer. Klicka [här](../user_guide/gl-rmq1/product_overview.md#compatibility) för mer information.

---

**F2. Behöver jag installera någon programvara för att använda GL.iNet KVM?**

S2. Ingen programvara behöver installeras på den styrda enheten, och den kan köra Windows, macOS, ChromeOS, Linux osv.

Om programvara behöver installeras på den styrande enheten beror på hur du vill komma åt KVM-enheten.

??? "Styrning på nära håll (endast Comet 5G)"

    **Obs!** Metoden är bara tillgänglig på Comet 5G (GL-RM10RC).

    Comet 5G har funktionen Wi-Fi Nearby Control, som möjliggör snabb lokal hantering utan trådbundna anslutningar. Växla bara Comet 5G:s Wi-Fi-nätverksläge till AP-läge, så skapar den ett unikt Wi-Fi-SSID. Anslut till detta SSID för att få säker åtkomst till Comet 5G:s konsol. Klicka [här](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control) för mer information.

    När AP-läget aktiveras kopplas Comet 5G bort från sitt överordnade Wi-Fi-nätverk och ger endast åtkomst på nära håll (utan internetanslutning).

??? "Lokal styrning (endast Comet X)"

    **Obs!** Metoden är bara tillgänglig på Comet X (GL-RM4PE).

    Comet X har en HDMI OUT-port och två extra USB-portar, vilket är idealiskt för lokal felsökning, konfiguration och OS-installation. Anslut bara skärm, mus och tangentbord för lokal hårdvarustyrning med plug-and-play. Klicka [här](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control) för mer information.

??? "LAN-åtkomst"

    Om du vill komma åt KVM-enheten i samma lokala nätverk (LAN) behöver du inte installera någon programvara på den styrande enheten.

    Öppna bara en webbläsare på den styrande enheten och ange KVM-enhetens IP-adress eller `glkvm.local` i adressfältet för att komma åt KVM-enheten lokalt.

    Klicka [här](local_access_via_browser.md){target="_blank"} för mer information.

??? "Fjärråtkomst"

    - **GLKVM-appen**

        Om den styrande enheten kör Windows, macOS, Android eller iOS kan du installera [GLKVM-appen](https://www.gl-inet.com/app-rm/){target="_blank"} på den och komma åt din KVM på distans och därmed den styrda enheten.

        Klicka [här](remote_access_via_glkvm_app.md){target="_blank"} för mer information.

    - **Molntjänst**

        Metoden passar dig som inte kan eller vill installera GLKVM-appen.

        Koppla din KVM till molntjänsten. Därefter kan du komma åt KVM-enheten på distans genom att skriva `glkvm.com` i en webbläsare på den styrande enheten och därmed nå den styrda enheten, utan att installera GLKVM-appen.

        Klicka [här](remote_access_via_cloud.md){target="_blank"} för mer information.

    - **Tailscale**

        Metoden passar dig som inte kan eller vill använda GLKVM-appen eller molntjänsten, men den kräver fler steg.

        Koppla KVM-enheten och den styrande enheten till samma Tailscale-konto. Därefter kan du komma åt KVM-enheten på distans genom att skriva KVM-enhetens virtuella Tailscale-IP-adress i en webbläsare på den styrande enheten och därmed nå den styrda enheten.

        Klicka [här](remote_access_via_tailscale.md){target="_blank"} för mer information.

    - **ZeroTier**

        Metoden passar dig som inte kan eller vill använda GLKVM-appen eller molntjänsten, men den kräver fler steg.

        Anslut KVM-enheten och den styrande enheten till samma ZeroTier-nätverk. Därefter kan du komma åt KVM-enheten på distans genom att skriva KVM-enhetens ZeroTier-IP-adress i en webbläsare på den styrande enheten och därmed nå den styrda enheten.

        Klicka [här](remote_access_via_zerotier.md){target="_blank"} för mer information.

    - **NetBird**

        Metoden passar dig som inte kan eller vill använda GLKVM-appen eller molntjänsten, men den kräver fler steg.

        [NetBird](https://netbird.io/){target="_blank"} är en nätverksplattform med öppen källkod baserad på nolltillit (zero trust) som låter dig bygga säkra privata nätverk för hem- och företagsbruk. Som ett WireGuard®-baserat overlay-nätverk ger NetBird säker åtkomst till dina enheter när som helst och var som helst.

        GL.iNet KVM har integrerat stöd för NetBird, så att du kan koppla enheten till det virtuella NetBird-nätverket för fjärråtkomst.

        Klicka [här](remote_access_via_netbird.md){target="_blank"} för mer information.

---

**F3. Hur kommer jag åt GL.iNet KVM?**

S3. I regel kan du komma åt GL.iNet KVM lokalt eller på distans på olika sätt:

- [LAN-åtkomst via webbläsare](local_access_via_browser.md){target="_blank"}
- [Fjärråtkomst via molntjänsten](remote_access_via_cloud.md){target="_blank"}
- [Fjärråtkomst via GLKVM-appen](remote_access_via_glkvm_app.md){target="_blank"}
- [Fjärråtkomst via Tailscale](remote_access_via_tailscale.md){target="_blank"}
- [Fjärråtkomst via ZeroTier](remote_access_via_zerotier.md){target="_blank"}
- [Fjärråtkomst via NetBird](remote_access_via_netbird.md){target="_blank"}

Dessutom stöder vissa GL.iNet KVM-modeller styrning på nära håll eller lokal styrning, så att du kan komma åt dem på plats utan att ansluta till någon annan router.

- [Styrning på nära håll (endast Comet 5G)](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control){target="_blank"}
- [Lokal styrning (endast Comet X)](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control){target="_blank"}

---

**F4. Behöver jag öppna portar (exponerade mot WAN) för att få fjärråtkomst till GL.iNet KVM?**

S4. Nej. Inga öppna portar och inte ens en publik IP-adress behövs.

---

**F5. Stöder GLKVM-appen ChromeOS/Linux?**

S5. Nej. För närvarande kan GLKVM-appen inte installeras på ChromeOS eller Linux.

Om den styrande enheten kör ChromeOS/Linux kan GLKVM-appen inte installeras, och därför stöds inte fjärråtkomst till den styrda enheten via GLKVM-appen.

Du kan dock använda <u>molntjänsten</u>, <u>Tailscale</u>, <u>ZeroTier</u> eller <u>NetBird</u> för fjärråtkomst. Mer information finns under F3 ovan.

Du kan också komma åt KVM-enheten lokalt via en webbläsare. Mer information finns under F3 ovan.

---

**F6. Kan Comet (GL-RM1) anslutas till ett trådlöst nätverk?**

S6. Nej. Comet (GL-RM1) stöder inte trådlös nätverksanslutning.

Den måste anslutas till en nätverksenhet (t.ex. en router) med en Ethernet-kabel för internetåtkomst.

Om du föredrar en KVM med stöd för Wi-Fi kan du överväga följande modeller:

* [Comet Pro (GL-RM10)](https://www.gl-inet.com/products/gl-rm10/){target="_blank"}
* [Comet 5G (GL-RM10RC)](https://www.gl-inet.com/products/gl-rm10rc/){target="_blank"}
* [Comet Q (GL-RMQ1)](https://www.gl-inet.com/products/gl-rmq1/){target="_blank"}

---

## Strömstyrning {#power-control}

**F1. Kan en GL.iNet KVM starta och stänga av målenheten på distans?**

S1. Med GL.iNet KVM kan du starta och stänga av målenheten på distans på följande sätt:

- Wake-on-LAN (inbyggd programvarutjänst)

- [ATX-kort](../user_guide/gl-atx-board/index.md){target="_blank"} (säljs separat, fungerar inte med Comet Q)

- [Fingerbot](../user_guide/gl-fgb-01/index.md){target="_blank"} (säljs separat, fungerar inte med Comet Q)

---

**F2. Hur använder jag ATX-kortet för fjärrstyrning av strömmen?**

S2. Se [användarhandboken för ATX-kortet](../user_guide/gl-atx-board/index.md){target="_blank"}.

---

## Funktioner {#features}

!!! Tip "Tips"

    Nedan finns vanliga frågor om några vanliga funktioner. Se respektive [användarhandbok](../user_guide/index.md) för fullständig information om funktionerna.

**F1. Måste jag använda KVM Cloud?**

S1. Nej. Molntjänsten är valfri.

Om du inte vill använda molnet för fjärråtkomst kan du använda overlay-nätverksverktyg från tredje part, till exempel Tailscale, ZeroTier och NetBird.

---

**F2. Kan jag använda en enda GL.iNet KVM för att styra flera enheter?**

S2. Följande GL.iNet KVM-enheter kan bara styra en målenhet:

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)
* Comet Q (GL-RMQ1)

Comet X (GL-RM4PE) kan däremot anslutas till upp till fyra målenheter samtidigt, men endast en enhet åt gången kan styras. Du kan snabbt växla mellan de fyra anslutna enheterna med den fysiska knappen på frontpanelen när du är på plats, eller via fjärrkonsolen när du är på annan plats.

Comet X (GL-RM4PE) har fyra oberoende kanaler på baksidan. Varje kanal har en HDMI-port för överföring av videosignal, en Type-C-port för överföring av tangentbords- och mussignaler och en USB 2.0-port för USB-kringutrustning (t.ex. Fingerbot eller ATX-kort).

---

**F3. Vad är Wake-on-LAN?**

S3. Wake-on-LAN (WOL) är en teknik som gör det möjligt att starta en dator eller enhet på distans, eller väcka den från ett energisparläge, via ett nätverk. Den fungerar genom att skicka ett "magiskt paket" med målenhetens MAC-adress, vilket får enheten att starta. Vanliga användningsområden är fjärradministration, energisparande vänteläge och central systemhantering.

---

**F4. Stöder GL.iNet KVM Mouse Jiggle?**

S4. Ja. Du kan aktivera Mouse Jiggle i KVM-konsolen.

Funktionen Mouse Jiggle simulerar små, periodiska musrörelser för att förhindra att datorn (dvs. den styrda enheten) går i viloläge efter långvarig inaktivitet, till exempel under fjärrmöten och serverhantering.

---

**F5. Stöder GL.iNet KVM tvåvägsljud?**

S5. Ja. Du kan aktivera högtalare och mikrofon i KVM-konsolen för tvåvägsöverföring av ljud.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
