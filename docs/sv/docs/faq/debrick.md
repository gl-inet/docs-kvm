# Återställ en obrukbar KVM med U-Boot {#using-u-boot-to-unbrick-your-kvm}

Om din KVM har blivit obrukbar på grund av egna projekt eller installation av fel firmware kanske den inte startar korrekt. I så fall kan du installera om firmwaren med hjälp av U-Boot-felsäkerhetsläget.

## Förberedelser {#preparation}

Förbered en stationär eller bärbar dator med en Ethernet-port. Om datorn saknar Ethernet-port behöver du en USB-Ethernet-adapter.

## Steg för återställning {#unbrick-steps}

Följ stegen nedan noggrant för att undvika att återställningen misslyckas.

1. Ladda ned firmwaren [här](https://dl.gl-inet.com/kvm){target="_blank"} till datorn.

2. Koppla bort strömmen från KVM-enheten. Anslut datorn till KVM-enhetens Ethernet-port.

3. Håll återställningsknappen (Reset) stadigt intryckt **och slå samtidigt på strömmen till KVM-enheten**.

    Vänta tills lysdioden har blinkat i ett regelbundet mönster flera gånger. Släpp återställningsknappen **efter** att blinkmönstret har ändrats.

    !!! note "Blinkmönster för lysdioden per enhetsmodell"

        - **Comet (GL-RM1)**: medan du håller in återställningsknappen blinkar den blå lysdioden 5 gånger. Släpp återställningsknappen efter de 5 blinkningarna, så lyser den blå lysdioden med fast sken.

        - **Comet PoE (GL-RM1PE)**: medan du håller in återställningsknappen blinkar den blå lysdioden 5 gånger. Släpp återställningsknappen efter de 5 blinkningarna, så lyser den blå lysdioden med fast sken.

        - **Comet Pro (GL-RM10)**: håll in återställningsknappen i cirka 5 sekunder och slå samtidigt på strömmen till KVM-enheten under tiden. Släpp sedan knappen. Enheten går in i U-Boot-läge.

        - **Comet 5G (GL-RM10RC)**: håll in återställningsknappen i cirka 5 sekunder och slå samtidigt på strömmen till KVM-enheten under tiden. Släpp sedan knappen. Enheten går in i U-Boot-läge.

4. Ange datorns IP-adress manuellt till **192.168.1.2**. Se stegvisa instruktioner för olika operativsystem nedan.

    ??? "Windows 7 / Windows 10"

        1. Gå till **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Högerklicka på **Local Area Connection** -> **Properties**.

        3. Klicka på **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Ange **IP adress** manuellt till `192.168.1.2`.

        5. Ange **Subnet mask** till `255.255.255.0`.

            ![Egenskaper för IPv4](https://static.gl-inet.com/docs/kvm/faq/debrick/win7_set_ip.jpg){class="glboxshadow"}

        6. Klicka på knappen **OK**.

    ??? "Windows 11"

        1. Öppna Inställningar.

        2. Klicka på **Network & Internet**.

        3. Klicka på fliken **Ethernet**.

            ![Ethernet i Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet.png){class="glboxshadow"}

        4. Klicka på knappen **Edit** under avsnittet "IP assignment".

            ![Redigera Ethernet i Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit1.png){class="glboxshadow"}

        5. Välj alternativet **Manual**.

            ![Redigera Ethernet i Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit2.png){class="glboxshadow"}

        6. Slå på reglaget **IPv4**.

        7. Ange den statiska **IP address** till **192.168.1.2**.

            ![Redigera Ethernet i Windows 11](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit3.png){class="glboxshadow"}

        8. Ange **Subnet mask** till **255.255.255.0**.

        9. Klicka på knappen **Save**.

    ??? "macOS"

        1. Klicka på **Apple**-ikonen i skärmens övre vänstra hörn och välj **System Preferences**.

            ![Systeminställningar i macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences.png){class="glboxshadow"}

        2. Klicka på **Network**.

            ![Nätverk i systeminställningarna i macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences_network.png){class="glboxshadow"}

        3. Klicka på **Ethernet** till vänster, klicka sedan på listrutan bredvid **Configure IPv4** och välj **Manually**. Om du använder en USB-Ethernet-adapter kanske Ethernet inte visas, utan i stället namnet på USB-Ethernet-adaptern.

            ![Manuell IP-adress i macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_1.png){class="glboxshadow"}

        4. Ange **IPv4 Address** till `192.168.1.2`, **Subnet Mask** till `255.255.255.0` och **Router** till `192.168.1.1`, och klicka sedan på knappen Apply i det nedre högra hörnet.

            ![Manuell IP-adress i macOS](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_2.png){class="glboxshadow"}

5. Gå till **http://192.168.1.1** i webbläsaren. Detta är U-Boots webbgränssnitt.

    ![U-Boots webbgränssnitt](https://static.gl-inet.com/docs/kvm/faq/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    **Obs!** U-Boots webbgränssnitt ovan kanske inte ser exakt likadant ut som det du ser, eftersom U-Boot-versionen skiljer sig mellan olika tillverkningsdatum. Av säkerhetsskäl tillhandahåller vi för närvarande inga separata U-Boot-uppgraderingar. Om en uppdatering behövs integrerar vi den i den nya firmwaren.

6. Klicka på **Choose file** och välj firmwarefilen. Klicka sedan på knappen **Update firmware**.

7. Vänta i cirka 3 minuter. **Stäng INTE av KVM-enheten under uppdateringen.**

    KVM-enheten är klar när lysdioden **blinkar vitt**.

8. Återställ de IP-inställningar på datorn som du gjorde i steg 4.

9. Koppla bort Ethernet-kabeln mellan datorn och KVM-enheten och anslut sedan KVM-enheten till en nätverkskälla (t.ex. en router eller en nätverksswitch) med Ethernet-kabeln eller via Wi-Fi.

    Vänta i cirka 1 minut så att KVM-enheten hinner få internetåtkomst. Därefter kan du komma åt din KVM igen.

    **Obs!** Konfigurationsinställningarna behålls i regel. De återställs dock till standardvärdena om det var ett konfigurationsfel som orsakade systemfelet som krävde återställningen.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
