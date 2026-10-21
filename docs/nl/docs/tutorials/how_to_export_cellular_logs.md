# Logboeken van het mobiele netwerk exporteren {#how-to-export-cellular-logs}

In deze handleiding leest u hoe u logboeken over het mobiele netwerk van een KVM-apparaat exporteert voor probleemoplossing.

In de volgende stappen wordt de Comet 5G (GL-RM10RC) als voorbeeld gebruikt.

1. Meld u aan bij de KVM-console, ga naar **Virtual Media** en controleer of deze functie is ingeschakeld.

2. Ga naar **Toolbox** -> **Terminal**. Klik op **Access** om de KVM-terminal te openen.

    ![Terminal openen](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/access_terminal.png){class="glboxshadow"}

3. Voer in het terminalvenster de volgende opdracht uit om het programma QLog te starten.

    ```
    QLog_1.5.22 -s /userdata/media/ -f /etc/HN_default.cfg & ubus call modem at '{"AT":"AT+QCFG=\"DBGCTL\",0"}'
    ```

    ![QLog 1](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog1.jpg){class="glboxshadow"}

    De pagina toont dan de initialisatie van QLog, gevolgd door realtime statistieken (bijvoorbeeld de ontvangen hoeveelheid gegevens en de verstreken tijd), zoals hieronder weergegeven.

    ![QLog 2](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog2.jpg){class="glboxshadow"}

4. Druk op Enter en voer de volgende opdrachten na elkaar uit om de modem opnieuw op te starten, zodat het apparaat de logboeken van het volledige opstartproces vastlegt.

    ```
    ubus call modem at '{"AT":"AT+CFUN=0"}'
    ```

    ```
    ubus call modem at '{"AT":"AT+CFUN=1"}'
    ```

    ![QLog 3](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog3.png){class="glboxshadow"}

5. Wacht 3-5 minuten zodat er voldoende loggegevens worden verzameld. Voer daarna de volgende opdracht in om het QLog-proces te stoppen.

    ```
    ps | grep QLog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![QLog 4](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog4.png){class="glboxshadow"}

6. Exporteer de logboeken.

    De logboeken van de mobiele modem worden opgeslagen in de map **/userdata/media/** met de bestandsextensie `xxx.qmdl`.

    Meld u aan bij de KVM-console, ga naar **Virtual Media** en zoek de bestanden met de extensie `xxx.qmdl`. Download deze bestanden en deel ze met de technische ondersteuning van GL.iNet.

    ![QLog 5](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog5.png){class="glboxshadow"}

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
