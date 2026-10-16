# Ripristinare il KVM con U-Boot {#using-u-boot-to-unbrick-your-kvm}

Se il KVM non si avvia più correttamente dopo modifiche fai da te o l'installazione di un firmware errato, puoi reinstallare il firmware usando la modalità di ripristino di U-Boot.

## Preparazione {#preparation}

Prepara un computer fisso o portatile con una porta Ethernet. Se il computer non dispone di una porta Ethernet, è necessario un adattatore USB-Ethernet.

## Procedura di ripristino {#unbrick-steps}

Per evitare che il ripristino non riesca, segui scrupolosamente i passaggi indicati di seguito.

1. Scarica il firmware sul computer da [qui](https://dl.gl-inet.com/kvm){target="_blank"}.

2. Scollega l'alimentazione del KVM. Collega il computer alla porta Ethernet del KVM.

3. Tieni premuto saldamente il pulsante Reset e, **contemporaneamente, accendi il KVM**.

    Attendi che il LED lampeggi più volte con una sequenza regolare. Rilascia il pulsante Reset **dopo** che la sequenza di lampeggio è cambiata.

    !!! note "Sequenze di lampeggio del LED per modello"

        - **Comet (GL-RM1)**: mentre tieni premuto il pulsante Reset, il LED blu lampeggia 5 volte. Rilascia il pulsante dopo i 5 lampeggi; il LED blu rimarrà acceso fisso.

        - **Comet PoE (GL-RM1PE)**: mentre tieni premuto il pulsante Reset, il LED blu lampeggia 5 volte. Rilascia il pulsante dopo i 5 lampeggi; il LED blu rimarrà acceso fisso.

        - **Comet Pro (GL-RM10)**: tieni premuto il pulsante Reset per circa 5 secondi, accendendo contemporaneamente il KVM, quindi rilascia il pulsante. Il dispositivo entrerà in modalità U-Boot.

        - **Comet 5G (GL-RM10RC)**: tieni premuto il pulsante Reset per circa 5 secondi, accendendo contemporaneamente il KVM, quindi rilascia il pulsante. Il dispositivo entrerà in modalità U-Boot.

4. Imposta manualmente l'indirizzo IP del computer su **192.168.1.2**. Consulta le istruzioni per il tuo sistema operativo riportate di seguito.

    ??? "Windows 7 / Windows 10"

        1. Vai su **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Fai clic con il pulsante destro del mouse su **Local Area Connection** -> **Properties**.

        3. Fai clic su **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Imposta manualmente **IP adress** su `192.168.1.2`.

        5. Imposta **Subnet mask** su `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/kvm/faq/debrick/win7_set_ip.jpg){class="glboxshadow"}

        6. Fai clic sul pulsante **OK**.

    ??? "Windows 11"

        1. Apri Settings.

        2. Fai clic su **Network & Internet**.

        3. Fai clic sulla scheda **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet.png){class="glboxshadow"}

        4. Nella sezione "IP assignment", fai clic sul pulsante **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit1.png){class="glboxshadow"}

        5. Seleziona l'opzione **Manual**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit2.png){class="glboxshadow"}

        6. Attiva l'interruttore **IPv4 toggle**.

        7. Imposta **IP address** statico su **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit3.png){class="glboxshadow"}

        8. Imposta **Subnet mask** su **255.255.255.0**.

        9. Fai clic sul pulsante **Save**.

    ??? "macOS"

        1. Fai clic sull'icona **Apple** nell'angolo in alto a sinistra dello schermo e seleziona **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences.png){class="glboxshadow"}

        2. Fai clic su **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences_network.png){class="glboxshadow"}

        4. Fai clic su **Ethernet** a sinistra, quindi sul menu a discesa accanto a **Configure IPv4** e seleziona **Manually**. Se usi un adattatore USB-Ethernet, la connessione potrebbe essere indicata con il nome dell'adattatore anziché con Ethernet.

            ![macos ip manually](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_1.png){class="glboxshadow"}

        4. Imposta **IPv4 Address** su `192.168.1.2`, **Subnet Mask** su `255.255.255.0` e **Router** su `192.168.1.1`, quindi fai clic sul pulsante Apply nell'angolo in basso a destra.

            ![macos ip manually](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_2.png){class="glboxshadow"}

5. Apri **http://192.168.1.1** nel browser per accedere all'interfaccia web di U-Boot.

    ![Uboot web ui](https://static.gl-inet.com/docs/kvm/faq/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    **Nota:** l'interfaccia web di U-Boot potrebbe essere diversa da quella mostrata sopra, perché la versione di U-Boot varia in base alla data di produzione. Per motivi di sicurezza, al momento non forniamo aggiornamenti separati di U-Boot. Se un aggiornamento è necessario, verrà integrato in un nuovo firmware.

6. Fai clic su **Choose file** e seleziona il file del firmware. Poi fai clic sul pulsante **Update firmware**.

7. Attendi circa 3 minuti. **NON spegnere il KVM durante l'aggiornamento.**

    Il KVM è pronto quando il LED **lampeggia in bianco**.

8. Ripristina le impostazioni IP del computer modificate al passaggio 4.

9. Scollega il cavo Ethernet tra il computer e il KVM, quindi collega il KVM a una rete, ad esempio a un router o a uno switch di rete, usando lo stesso cavo Ethernet oppure il Wi-Fi.

    Attendi circa 1 minuto affinché il KVM ottenga l'accesso a Internet. Potrai quindi accedere nuovamente al KVM.

    **Nota:** in genere le impostazioni di configurazione vengono mantenute. Tuttavia, se il guasto che ha richiesto il ripristino è stato causato da un errore di configurazione, verranno ripristinate le impostazioni predefinite.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
