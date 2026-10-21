# Så exporterar du mobilnätsloggar {#how-to-export-cellular-logs}

Den här guiden beskriver hur du exporterar loggar för mobilanslutningen från KVM-enheten för felsökning.

Stegen nedan använder Comet 5G (GL-RM10RC) som exempel.

1. Logga in på KVM-konsolen, gå till **Virtual Media** och kontrollera att funktionen är aktiverad.

2. Gå till **Toolbox** -> **Terminal**. Klicka på **Access** för att öppna KVM-terminalen.

    ![Öppna terminalen](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/access_terminal.png){class="glboxshadow"}

3. Kör följande kommando i terminalfönstret för att starta programmet QLog.

    ```
    QLog_1.5.22 -s /userdata/media/ -f /etc/HN_default.cfg & ubus call modem at '{"AT":"AT+QCFG=\"DBGCTL\",0"}'
    ```

    ![QLog 1](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog1.jpg){class="glboxshadow"}

    Sidan visar sedan initieringen vid start av QLog, följt av statistik i realtid (t.ex. mottagen datamängd och förfluten tid), enligt bilden nedan.

    ![QLog 2](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog2.jpg){class="glboxshadow"}

4. Tryck på Enter och kör följande kommandon i tur och ordning för att starta om modemet, så att enheten samlar in loggar för hela startprocessen.

    ```
    ubus call modem at '{"AT":"AT+CFUN=0"}'
    ```

    ```
    ubus call modem at '{"AT":"AT+CFUN=1"}'
    ```

    ![QLog 3](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog3.png){class="glboxshadow"}

5. Vänta i 3–5 minuter så att tillräckligt med loggdata samlas in. Ange sedan följande kommando för att stoppa QLog-processen.

    ```
    ps | grep QLog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![QLog 4](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog4.png){class="glboxshadow"}

6. Exportera loggarna.

    Loggarna från mobilmodemet sparas i katalogen **/userdata/media/** med filändelsen `xxx.qmdl`.

    Logga in på KVM-konsolen, gå till **Virtual Media** och leta upp filerna med filändelsen `xxx.qmdl`. Ladda ned filerna och dela dem med GL.iNets tekniska support.

    ![QLog 5](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog5.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
