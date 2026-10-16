# Come esportare i log della connessione cellulare {#how-to-export-cellular-logs}

Questo tutorial spiega come esportare dal dispositivo KVM i log relativi alla connessione cellulare per la risoluzione dei problemi.

I passaggi seguenti usano Comet 5G (GL-RM10RC) come esempio.

1. Accedi alla console del KVM, vai su **Virtual Media** e assicurati che la funzione sia attiva.

2. Vai su **Toolbox** -> **Terminal**. Fai clic su **Access** per entrare nel terminale del KVM.

    ![access terminal](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/access_terminal.png){class="glboxshadow"}

3. Nella finestra del terminale, esegui il comando seguente per avviare il programma QLog.

    ```
    QLog_1.5.22 -s /userdata/media/ -f /etc/HN_default.cfg & ubus call modem at '{"AT":"AT+QCFG=\"DBGCTL\",0"}'
    ```

    ![qlog 1](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog1.jpg){class="glboxshadow"}

    La pagina mostrerà le informazioni di inizializzazione di QLog, seguite dalle statistiche in tempo reale, come il volume dei dati ricevuti e il tempo trascorso, come mostrato di seguito.

    ![qlog 2](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog2.jpg){class="glboxshadow"}

4. Premi Invio ed esegui in sequenza i comandi seguenti per riavviare il modem e consentire al dispositivo di acquisire i log dell'intera procedura di avvio.

    ```
    ubus call modem at '{"AT":"AT+CFUN=0"}'
    ```

    ```
    ubus call modem at '{"AT":"AT+CFUN=1"}'
    ```

    ![qlog 3](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog3.png){class="glboxshadow"}

5. Attendi 3-5 minuti per raccogliere una quantità sufficiente di dati nei log. Quindi esegui il comando seguente per arrestare il processo QLog.

    ```
    ps | grep QLog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![qlog 4](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog4.png){class="glboxshadow"}

6. Esporta i log.

    I log del modem cellulare vengono salvati nella directory **/userdata/media/** con il suffisso del nome file `xxx.qmdl`.

    Accedi alla console del KVM, vai su **Virtual Media** e individua i file con suffisso `xxx.qmdl`. Scaricali e condividili con l'assistenza tecnica GL.iNet.

    ![qlog 5](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog5.png){class="glboxshadow"}

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
