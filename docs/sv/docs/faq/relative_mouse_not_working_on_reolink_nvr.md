# Vad gör jag om relativt musläge inte fungerar på Reolink NVR? {#what-should-i-do-if-relative-mouse-mode-doesnt-work-on-reolink-nvr}

När du använder GL.iNet KVM för att styra en Reolink NVR (särskilt modeller som inte stöder två möss) eller vissa äldre datorer (till exempel datorer utan USB-gränssnitt) kanske relativt musläge inte fungerar. Vanliga problem är att läget inte fungerar alls, eller att musrörelserna registreras men klicken inte svarar.

Problemet beror främst på bristande kompatibilitet mellan KVM-enhetens musemulering och de begränsade funktionerna hos enheter som Reolink NVR:

- **Före firmware v1.4.0**: KVM-enheten var utformad för att emulera endast en mus. För att växla mellan relativt och absolut läge måste du starta om KVM-enheten, men det fungerade bra med de flesta äldre eller specialiserade enheter.

- **Efter firmware v1.4.0**: För att möjliggöra sömlös växling mellan lägena utan omstart ändrades standardlogiken så att två möss emuleras samtidigt (en för relativt läge och en för absolut läge). Reolink NVR och vissa äldre datorer saknar dock stöd för två möss, vilket leder till två vanliga problem:

    - Relativt musläge fungerar inte alls.
    - Musen rör sig fortfarande, men klick ger ingen respons.

Du kan lösa problemet genom att tvinga fram relativt musläge i terminalen. Gör så här:

1. Öppna KVM-konsolen och gå till **Toolbox** -> **Terminal**. Klicka på **Access** för att öppna KVM-terminalen.

2. Öppna konfigurationsfilen med följande kommando:

    `vi /etc/kvmd/override.yaml`

3. Lägg till följande konfiguration för att tvinga fram relativt musläge:

    ```
    kvmd:
        hid:
            mouse:
                absolute: false
    ```

4. Spara filen och stäng redigeraren.

5. Starta om KVM-enheten för att tillämpa ändringarna.

!!! note "Obs!"

    1. Om metoden ovan inte fungerar kan du prova att återställa KVM-enhetens firmware till en version före v1.4 (om sådan finns). Den stöder emulering av en enda mus och är kompatibel med äldre enheter.

    2. Den fristående GLKVM-appen för macOS stöder inte relativt musläge på grund av begränsningar i webbläsarmotorn (saknat stöd för API:t requestPointerLock). Använd webbkonsolen i stället.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
