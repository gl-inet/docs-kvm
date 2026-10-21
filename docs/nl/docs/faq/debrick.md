# Een gebrickte KVM herstellen met U-Boot {#using-u-boot-to-unbrick-your-kvm}

Als uw KVM door een doe-het-zelfproject of het flashen van verkeerde firmware gebrickt is, start het apparaat mogelijk niet meer goed op. In dat geval kunt u de firmware opnieuw installeren met de U-Boot-failsafe.

## Voorbereiding {#preparation}

Zorg voor een computer of laptop met een ethernetpoort. Als uw computer geen ethernetpoort heeft, hebt u een USB-naar-ethernetadapter nodig.

## Stappen voor herstel {#unbrick-steps}

Volg de onderstaande stappen nauwkeurig om te voorkomen dat het herstel mislukt.

1. Download de firmware [hier](https://dl.gl-inet.com/kvm){target="_blank"} naar uw computer.

2. Koppel de voeding van de KVM los. Sluit uw computer aan op de ethernetpoort van de KVM.

3. Houd de resetknop stevig ingedrukt en **schakel tegelijkertijd uw KVM in**.

    Wacht tot de led enkele keren in een regelmatig patroon heeft geknipperd. Laat de resetknop pas los **nadat** het knipperpatroon is veranderd.

    !!! note "Knipperpatronen van de led per model"

        - **Comet (GL-RM1)**: terwijl u de resetknop ingedrukt houdt, knippert de blauwe led 5 keer. Laat de resetknop na de 5 keer knipperen los; de blauwe led blijft dan continu branden.

        - **Comet PoE (GL-RM1PE)**: terwijl u de resetknop ingedrukt houdt, knippert de blauwe led 5 keer. Laat de resetknop na de 5 keer knipperen los; de blauwe led blijft dan continu branden.

        - **Comet Pro (GL-RM10)**: houd de resetknop ongeveer 5 seconden ingedrukt, schakel in die tijd tegelijkertijd uw KVM in en laat de knop daarna los. Het apparaat gaat dan naar de U-Boot-modus.

        - **Comet 5G (GL-RM10RC)**: houd de resetknop ongeveer 5 seconden ingedrukt, schakel in die tijd tegelijkertijd uw KVM in en laat de knop daarna los. Het apparaat gaat dan naar de U-Boot-modus.

4. Stel het IP-adres van uw computer handmatig in op **192.168.1.2**. Hieronder vindt u stapsgewijze instructies voor de verschillende besturingssystemen.

    ??? "Windows 7 / Windows 10"

        1. Ga naar **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Klik met de rechtermuisknop op **Local Area Connection** -> **Properties**.

        3. Klik op **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Stel het **IP address** handmatig in op `192.168.1.2`.

        5. Stel het **Subnet mask** in op `255.255.255.0`.

            ![IPv4-eigenschappen](https://static.gl-inet.com/docs/kvm/faq/debrick/win7_set_ip.jpg){class="glboxshadow"}

        6. Klik op de knop **OK**.

    ??? "Windows 11"

        1. Open Instellingen.

        2. Klik op **Network & Internet**.

        3. Klik op het tabblad **Ethernet**.

            ![Ethernet in Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet.png){class="glboxshadow"}

        4. Klik onder "IP assignment" op de knop **Edit**.

            ![Ethernet bewerken in Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit1.png){class="glboxshadow"}

        5. Selecteer de optie **Manual**.

            ![Ethernet bewerken in Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit2.png){class="glboxshadow"}

        6. Zet de schakelaar **IPv4** aan.

        7. Stel het statische **IP address** in op **192.168.1.2**.

            ![Ethernet bewerken in Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit3.png){class="glboxshadow"}

        8. Stel het **Subnet mask** in op **255.255.255.0**.

        9. Klik op de knop **Save**.

    ??? "macOS"
    
        1. Klik linksboven in het scherm op het **Apple**-pictogram en selecteer **System Preferences**.

            ![Systeemvoorkeuren in macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences.png){class="glboxshadow"}

        2. Klik op **Network**.

            ![Netwerk in de systeemvoorkeuren van macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences_network.png){class="glboxshadow"}

        3. Klik links op **Ethernet**, klik vervolgens op de vervolgkeuzelijst naast **Configure IPv4** en selecteer **Manually**. Als u een USB-ethernetadapter gebruikt, wordt Ethernet mogelijk niet gevonden en wordt in plaats daarvan de naam van de USB-ethernetadapter weergegeven.

            ![Handmatig IP-adres in macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_1.png){class="glboxshadow"}

        4. Stel **IPv4 Address** in op `192.168.1.2`, **Subnet Mask** op `255.255.255.0` en **Router** op `192.168.1.1` en klik rechtsonder op de knop Apply.

            ![Handmatig IP-adres in macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_2.png){class="glboxshadow"}

5. Ga in de browser naar **http://192.168.1.1**. Dit is de webinterface van U-Boot.

    ![Webinterface van U-Boot](https://static.gl-inet.com/docs/kvm/faq/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    **Opmerking:** De bovenstaande webinterface van U-Boot kan afwijken van wat u ziet, omdat de U-Boot-versie per productiedatum verschilt. Om veiligheidsredenen bieden we momenteel geen afzonderlijke U-Boot-upgrades aan. Als een update nodig is, nemen we deze op in nieuwe firmware.

6. Klik op **Choose file** en selecteer het firmwarebestand. Klik vervolgens op de knop **Update firmware**.

7. Wacht ongeveer 3 minuten. **Schakel uw KVM NIET uit tijdens de update.**

    De KVM is klaar wanneer de led **wit knippert**.

8. Zet de IP-instellingen van de computer die u in stap 4 hebt gewijzigd weer terug.

9. Koppel de ethernetkabel tussen uw computer en de KVM los en verbind uw KVM via deze ethernetkabel of via wifi met een netwerkbron (bijvoorbeeld een router of netwerkswitch).

    Wacht ongeveer 1 minuut zodat de KVM internettoegang kan krijgen. Daarna kunt u uw KVM weer openen.

    **Opmerking:** De configuratie-instellingen blijven doorgaans behouden. Ze worden echter teruggezet naar de standaardwaarden als een configuratiefout de systeemstoring veroorzaakte waarvoor herstel nodig was.

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
