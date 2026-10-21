# Firmware v1.9 {#firmware-v19}

Den här versionen ger helt nya funktionstillägg, bättre interaktivitet, starkare integritetsskydd och mer tillförlitliga nätverksanslutningar – allt för att ge en mer heltäckande, stabil och säker fjärr-KVM-upplevelse.

Hämta den senaste firmwaren från [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"}

## Latensläge {#latency-mode}

Den här firmwaren introducerar **Latency Mode**, som balanserar inmatningsrespons och videoflyt. Du kan ställa in Latency Mode på antingen Lowest Latency eller Smooth Display för att optimera fjärrstyrningens prestanda.

![Latensläge](https://static.gl-inet.com/docs/kvm/features_update/1.9/latency_mode.png){class="glboxshadow" width="360"}

- Lowest Latency: minimerar inmatningslatensen för snabbare respons från tangentbord och mus.
- Smooth Display: optimerar bildutmatningen för att eliminera hack och tappade bildrutor, vilket ger jämn uppspelning.

## Användbarhet för musen {#mouse-usability}

Ett nytt alternativ, **Primary Button**, har lagts till för att förbättra musens användbarhet. Du kan ange vänster eller höger knapp som primär klickknapp efter dina egna vanor.

![Primär knapp](https://static.gl-inet.com/docs/kvm/features_update/1.9/primary_button.png){class="glboxshadow" width="360"}

## Skärmvisning {#screen-display}

Du kan anpassa KVM-enhetens inställningar för **Screen Display** via pekskärmen, bland annat skärmlås, bakgrundsbild, tidsformat (24 timmar/12 timmar) och datumformat. Funktionen är endast tillgänglig på modeller med pekskärm.

Dessutom kan du snabbt konfigurera overlay-verktyg som Tailscale och NetBird direkt från pekskärmen med några få tryck – en funktion som inte fanns i tidigare firmwareversioner.

![Skärmvisning](https://static.gl-inet.com/docs/kvm/features_update/1.9/screen_display.png){class="glboxshadow" width="360"}

## Språk {#language}

Tidigare firmwareversioner hade bara stöd för kinesiska och engelska. Den här versionen lägger till inbyggt stöd för **japanska** för att förbättra tillgängligheten för japanska användare.

![Språk](https://static.gl-inet.com/docs/kvm/features_update/1.9/language.png){class="glboxshadow" width="360"}

## Tillägg {#extensions}

Den här versionen integrerar [NetBird](https://netbird.io/){target="_blank"}, en nätverksplattform med öppen källkod baserad på nolltillit (zero trust) för att bygga säkra privata nätverk för hem och företag. Overlay-lösningen bygger på WireGuard® och ger säker fjärråtkomst till din KVM var du än befinner dig via virtuella NetBird-nätverk. Instruktioner för konfigurationen finns [här](../faq/remote_access_via_netbird.md){target="_blank"}.

![NetBird](https://static.gl-inet.com/docs/kvm/features_update/1.9/netbird.png){class="glboxshadow"}

## Övriga förbättringar {#other-enhancements}

- Betaprogram för firmware: användare kan gå med i betaprogrammet för att testa funktioner före lansering.

- Textigenkänning: verktyget bygger på optisk teckenigenkänning (OCR) och låter dig fånga text från valfritt markerat område på fjärrskärmen. Språk som stöds är kinesiska, engelska och tvåspråkigt läge kinesiska-engelska. Mer information finns [här](../tutorials/how_to_capture_text_from_remote_screen.md).

- Stadsbaserad tidszon: ställ in tidszonen genom att välja en stad.

- Säkerhet för inloggningssessioner: inloggningstoken upphör nu att gälla 12 timmar efter att sessionen avslutats (tidigare var token permanenta).

- Säkerhet för systemloggar: maskering av känsliga data har införts i alla systemloggar.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
