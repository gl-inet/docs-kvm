# Så återställer du en obrukbar KVM via RKDevTool {#how-to-unbrick-kvm-via-rkdevtool}

Den här guiden visar hur du återställer en obrukbar GL.iNet KVM med verktyget RKDevTool. Den gäller när KVM-enheten har blivit obrukbar och inte kan återställas via vanliga firmwareuppdateringar eller U-Boot-felsäkerhetsläget.

## Förberedelser {#preparation}

Förbered följande verktyg för återställningen.

- En Windows-dator
- En USB-datakabel
- En nätadapter (för KVM-enheten)

!!! Note "Obs!"

    Koppla INTE bort USB-kabeln och stäng INTE av KVM-enheten under återställningen, eftersom det kan skada enheten.

    Vi rekommenderar att du säkerhetskopierar viktiga data innan du påbörjar återställningen.

## Steg för återställning {#unbrick-steps}

Följ stegen i ordning för att undvika att återställningen misslyckas.

1. Stäng av KVM-enheten.

2. Ladda ned den senaste firmwaren för din KVM-enhet [här](https://dl.gl-inet.com/kvm){target="_blank"} till datorn.

3. Ladda ned drivrutinspaketet [här](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/DriverAssitant_v5.11.zip) till datorn och packa upp det i valfri katalog.

4. Dubbelklicka på .exe-filen för att slutföra installationen av drivrutinen.

    ![Installera drivrutinen](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_1.png){class="glboxshadow"}

    ![Installera drivrutinen](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_2.png){class="glboxshadow"}

5. Ladda ned **RKDevTool** [här](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/RKDevTool_Release_v3.37.zip) till datorn och packa upp det i en lättåtkomlig katalog.

6. Dubbelklicka på .exe-filen för att köra flashverktyget på datorn.

    ![Kör RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_1.png){class="glboxshadow"}

    ![Kör RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_2.png){class="glboxshadow"}

7. Anslut KVM-enhetens Type-C OTG-port till datorns USB-port med en USB-datakabel.

    Vi tar Comet (GL-RM1) som exempel. Type-C OTG-porten visas nedan.

    ![Anslut USB-kabeln](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/otg-port-rm1.png){class="glboxshadow gl-60-desktop"}

8. Håll in återställningsknappen (RESET) i **10 sekunder** medan du ansluter strömkabeln till KVM-enheten. Släpp sedan knappen. KVM-enheten går in i Loader-läge.

    ![Återställningsknapp](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/reset_button_rm1.jpg){class="glboxshadow" width="433"}

9. Gå till RKDevTool-panelen, gå till **Upgrade Firmware** -> **Firmware** och välj den firmware som du laddade ned i steg 2 för att ladda upp den.

    ![Välj firmware](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/select_firmware.png){class="glboxshadow"}

    Gå sedan till fliken **Upgrade** bredvid fliken Firmware. Där visas "Found Loader Device" och flashningen av firmwaren startar.

    ![RKDevTool-panelen](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/rkdevtool_panel.jpg){class="glboxshadow"}

    KVM-enheten startas om automatiskt när uppgraderingen är klar.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
