# Een gebrickte KVM herstellen met RKDevTool {#how-to-unbrick-kvm-via-rkdevtool}

In deze handleiding leest u hoe u een gebrickte GL.iNet KVM herstelt met RKDevTool. Deze methode is bedoeld voor situaties waarin de KVM gebrickt is en niet kan worden hersteld via een gewone firmware-update of de U-Boot-failsafemodus.

## Voorbereiding {#preparation}

Zorg voor de volgende hulpmiddelen voor het herstel.

- Een Windows-computer
- Een USB-datakabel
- Een voedingsadapter (voor het KVM-apparaat)

!!! Note "Opmerking"

    Koppel de USB-kabel NIET los en schakel de KVM NIET uit tijdens het herstel, omdat het apparaat hierdoor beschadigd kan raken.
    
    Het wordt aanbevolen een back-up van belangrijke gegevens te maken voordat u met het herstel begint.

## Stappen voor herstel {#unbrick-steps}

Volg de stappen in de aangegeven volgorde om te voorkomen dat het herstel mislukt.

1. Schakel uw KVM-apparaat uit.

2. Download de nieuwste firmware voor uw KVM-apparaat [hier](https://dl.gl-inet.com/kvm){target="_blank"} naar uw computer.

3. Download het stuurprogrammapakket [hier](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/DriverAssitant_v5.11.zip) naar uw computer en pak het uit in een willekeurige map.

4. Dubbelklik op het .exe-bestand om het installatieprogramma voor het stuurprogramma uit te voeren.

    ![Stuurprogramma installeren](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_1.png){class="glboxshadow"}

    ![Stuurprogramma installeren](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_2.png){class="glboxshadow"}

5. Download **RKDevTool** [hier](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/RKDevTool_Release_v3.37.zip) naar uw computer en pak het uit in een gemakkelijk bereikbare map.

6. Dubbelklik op het .exe-bestand om de flashtool op uw computer te starten.

    ![RKDevTool starten](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_1.png){class="glboxshadow"}

    ![RKDevTool starten](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_2.png){class="glboxshadow"}

7. Verbind de Type-C OTG-poort van de KVM met een USB-datakabel met de USB-poort van de computer.

    Neem de Comet (GL-RM1) als voorbeeld. De Type-C OTG-poort ziet u hieronder.

    ![USB-kabel aansluiten](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/otg-port-rm1.png){class="glboxshadow gl-60-desktop"}

8. Houd de RESET-knop **10 seconden** ingedrukt terwijl u de voedingskabel op de KVM aansluit. Laat de knop daarna los. Uw KVM-apparaat gaat nu naar de Loader-modus.

    ![Resetknop](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/reset_button_rm1.jpg){class="glboxshadow" width="433"}

9. Ga naar het venster van RKDevTool, ga naar **Upgrade Firmware** -> **Firmware** en selecteer de firmware die u in stap 2 hebt gedownload om deze te uploaden.

    ![Firmware selecteren](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/select_firmware.png){class="glboxshadow"}

    Ga vervolgens naar het tabblad **Upgrade** naast het tabblad Firmware. Er verschijnt "Found Loader Device" en het flashen van de firmware begint.

    ![Venster van RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/rkdevtool_panel.jpg){class="glboxshadow"}

    Het KVM-apparaat wordt automatisch opnieuw opgestart zodra de upgrade is voltooid.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
