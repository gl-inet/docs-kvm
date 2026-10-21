# Come ripristinare il KVM tramite RKDevTool {#how-to-unbrick-kvm-via-rkdevtool}

Questo tutorial spiega come ripristinare un KVM GL.iNet con RKDevTool. Si applica ai casi in cui il KVM è bloccato e non può essere ripristinato tramite un normale aggiornamento del firmware o la modalità di ripristino U-Boot.

## Preparazione {#preparation}

Prepara i seguenti strumenti per il ripristino.

- Un computer Windows
- Un cavo USB per il trasferimento dati
- Un alimentatore (per il dispositivo KVM)

!!! Note "Nota"

    NON scollegare il cavo USB e non spegnere il KVM durante il ripristino, poiché il dispositivo potrebbe danneggiarsi.

    Si consiglia di eseguire il backup dei dati importanti prima di iniziare il ripristino.

## Procedura di ripristino {#unbrick-steps}

Per evitare che il ripristino non riesca, segui i passaggi nell'ordine indicato.

1. Spegni il dispositivo KVM.

2. Scarica sul computer il firmware più recente per il dispositivo KVM da [questa pagina](https://dl.gl-inet.com/kvm){target="_blank"}.

3. Scarica sul computer il pacchetto dei driver da [questo link](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/DriverAssitant_v5.11.zip) ed estrailo in una cartella a scelta.

4. Fai doppio clic sul file .exe per completare l'installazione del driver.

    ![Installazione del driver](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_1.png){class="glboxshadow"}

    ![Installazione del driver](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_2.png){class="glboxshadow"}

5. Scarica sul computer **RKDevTool** da [questo link](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/RKDevTool_Release_v3.37.zip) ed estrailo in una cartella facilmente accessibile.

6. Fai doppio clic sul file .exe per avviare lo strumento di scrittura del firmware sul computer.

    ![Avvio di RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_1.png){class="glboxshadow"}

    ![Avvio di RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_2.png){class="glboxshadow"}

7. Collega la porta Type-C OTG del KVM alla porta USB del computer con un cavo USB per il trasferimento dati.

    Di seguito viene utilizzato Comet (GL-RM1) come esempio. La porta Type-C OTG è mostrata nell'immagine.

    ![Collegamento del cavo USB](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/otg-port-rm1.png){class="glboxshadow gl-60-desktop"}

8. Tieni premuto il pulsante RESET per **10 secondi** mentre colleghi il cavo di alimentazione al KVM. Quindi rilascia il pulsante. Il dispositivo KVM entrerà in modalità Loader.

    ![Pulsante di ripristino](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/reset_button_rm1.jpg){class="glboxshadow" width="433"}

9. Nel pannello di RKDevTool, vai su **Upgrade Firmware** -> **Firmware** e seleziona il firmware scaricato al passaggio 2 per caricarlo.

    ![Selezione del firmware](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/select_firmware.png){class="glboxshadow"}

    Quindi passa alla scheda **Upgrade** accanto a Firmware. Comparirà "Found Loader Device" e inizierà la scrittura del firmware.

    ![Pannello di RKDevTool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/rkdevtool_panel.jpg){class="glboxshadow"}

    Il dispositivo KVM si riavvierà automaticamente al termine dell'aggiornamento.

---

Hai ancora domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
