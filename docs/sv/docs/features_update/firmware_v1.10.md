# Firmware v1.10 {#firmware-v110}

Den här versionen introducerar inbyggd WebRTC, dataövervakning i realtid, central hantering av USB-enheter och ett nytt inställningscenter. Den förbättrar även startprestanda, säkerhet och mikrofonstabilitet för en smidigare och mer tillförlitlig fjärr-KVM-upplevelse.

Hämta den senaste firmwaren från [Firmware Download Center](https://dl.gl-inet.com/kvm){target="_blank"}

## Läget WebRTC (Native) {#webrtc-native-mode}
Den här firmwaren introducerar läget **WebRTC (Native)**. Det använder Google WebRTC-biblioteket för att förbättra strömningsprestandan och ge en smidigare fjärrstyrning i realtid.

![WebRTC-läge](https://static.gl-inet.com/docs/kvm/features_update/1.10/webrtc_native_mode.png){class="glboxshadow" width=400}

## Anslutningsstatistik {#connection-stats}

**Connection Stats** visar anslutningsinformation och trenddiagram i realtid, bland annat nätverkslatens, jitter, paketförlust, bithastighet, bildfrekvens och uppspelningsfördröjning.

Klicka på listikonen för att visa anslutningsdata och enhetsstatus i realtid.

![Anslutningsstatistik 1](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_1.png){class="glboxshadow"}

Klicka på diagramikonen för att visa trenddiagram för nätverkslatens, jitter och paketförlust.

![Anslutningsstatistik 2](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_2.png){class="glboxshadow"}

## Inställningscenter {#settings-center}

Den här versionen lägger till ett nytt **Settings Center** som samlar inställningar för USB-enheter, preferenser, nätverk, säkerhet, moln och system. Befintliga alternativ, till exempel konfiguration av värdnamn, molnhantering och firmwareuppgraderingar, är nu lättare att nå på ett och samma ställe.

### USB-enheter {#usb-devices}

**USB Devices** ger central hantering av emulerade USB-enheter. På den här sidan kan du aktivera eller inaktivera virtuell kringutrustning för att förbättra kompatibiliteten med den styrda värden.

![USB-enheter](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_usb_devices.png){class="glboxshadow"}

- **USB Emulated Devices**: aktivera eller inaktivera emulerade USB-enheter, bland annat mus, tangentbord, mikrofon, kamera och virtuella medier. Vissa enheter kan inte aktiveras samtidigt. Tillgängligheten uppdateras automatiskt.

- **Device Identity**: anpassa eller ändra den KVM-identitet som den styrda enheten identifierar. Observera att EDID och enhetsidentiteten hålls synkroniserade. Om du ändrar den ena uppdateras den andra automatiskt, så att enheten identifieras korrekt.

### Preferenser {#preferences}

Under **Preferences** hanterar du layoutinställningar, systeminställningar och inställningar för enhetens skärm.

![Preferenser](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences**: konfigurera verktygsfältet i helskärmsläge och statusfältet i fönsterläge.

- **System Settings**: ange flikrubrik i webbläsaren, gränssnittsspråk, färgläge och tidszon.

- **Device Screen**: förhandsgranska och konfigurera enhetens inbyggda skärm, bland annat låsskärmsläge, tidsformat, datumformat och bakgrundsbild.

    **Obs!** Funktionen är bara tillgänglig på modeller med inbyggd skärm.

### Nätverk {#network}

Du kan visa och hantera enhetens nätverksinställningar, bland annat värdnamn, Ethernet-anslutning och information om det trådlösa nätverket.

![Nätverk](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_network.png){class="glboxshadow"}

- **Hostname**: ändra enhetens värdnamn direkt i konsolen. Funktionen introducerades i firmware v1.7.0.

- **Ethernet Settings**: visa och konfigurera Ethernet-anslutningen. Du kan använda DHCP för att hämta nätverksinställningarna automatiskt eller välja **Static** för att manuellt ange IP-adress, nätmask, gateway och andra parametrar som krävs.

- **Wireless**: IP-adress, gateway och MAC-adress visas när enheten har anslutits till ett Wi-Fi-nätverk.

    **Obs!** Funktionen Wireless är bara tillgänglig på modeller som stöder den.

### Säkerhet {#security}

Under **Security** kan du ändra administratörslösenordet, aktivera tvåfaktorsautentisering och anpassa TLS-certifikatet.

![Säkerhet](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_security.png){class="glboxshadow"}

- **Access Password**: hantera administratörslösenordet eller aktivera tvåfaktorsautentisering (2FA) för att skydda åtkomsten till enheten.

- **TLS Certificate**: använd standardcertifikatet eller ladda upp ett eget certifikat och en privat nyckel för åtkomst via webbläsare.

### Moln {#cloud}

Enheter kan kopplas till molntjänster via URL eller kod för fjärråtkomst och fjärrhantering. Du kan även ladda ned mobilappen, hantera anslutningen eller koppla från enheten vid behov.

![Moln](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_cloud.png){class="glboxshadow"}

### System {#system}

Under **System** hittar du alternativ för systemhantering, firmwareuppgradering och support.

![System](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_system.png){class="glboxshadow"}

- **System**: starta om enheten eller återställ den till fabriksinställningarna.

- **Upgrade**: aktivera Beta Center för att få betaversioner av firmware, eller använd **Local Upgrade** för att installera firmware från en lokal fil.

- **Help & Support**: exportera enhetsloggar för felsökning och få tillgång till användarhandböcker, vanliga frågor och annan supportdokumentation.

## Övriga förbättringar {#other-enhancements}

- **Startup Performance**: snabbare uppstart av enheten.

- **Password Policy**: skärpt lösenordspolicy (minst 10 tecken med minst två teckentyper) för ökad säkerhet.

- **Caps Lock Indicator**: en statusindikator för Caps Lock på den styrda enheten har lagts till.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
