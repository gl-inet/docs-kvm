# Mobilfunkprotokolle exportieren

Dieses Tutorial beschreibt die Schritte zum Exportieren mobilfunkbezogener Protokolle vom KVM-Geraet fuer die Fehlerbehebung.

Die folgenden Schritte verwenden Comet 5G (GL-RM10RC) als Beispiel.

1. Melden Sie sich an der KVM-Konsole an, navigieren Sie zu **Virtual Media** und stellen Sie sicher, dass es aktiviert ist.

2. Navigieren Sie zu **Toolbox** -> **Terminal**. Klicken Sie auf **Access**, um das KVM-Terminal zu oeffnen.

    ![access terminal](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/access_terminal.png){class="glboxshadow"}

3. Fuehren Sie im Terminalfenster den folgenden Befehl aus, um das QLog-Programm zu starten.

    ```
    QLog_1.5.22 -s /userdata/media/ -f /etc/HN_default.cfg & ubus call modem at '{"AT":"AT+QCFG=\"DBGCTL\",0"}'
    ```

    ![qlog 1](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog1.jpg){class="glboxshadow"}

    Die Seite zeigt anschliessend die Initialisierung des QLog-Starts und danach Echtzeit-Datenstatistiken an, z. B. empfangenes Datenvolumen und verstrichene Zeit, wie unten dargestellt.

    ![qlog 2](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog2.jpg){class="glboxshadow"}

4. Druecken Sie die Enter-Taste und fuehren Sie die folgenden Befehle nacheinander aus, um das Modem neu zu starten. So wird sichergestellt, dass das Geraet vollstaendige Protokolle des Startvorgangs erfasst.

    ```
    ubus call modem at '{"AT":"AT+CFUN=0"}'
    ```

    ```
    ubus call modem at '{"AT":"AT+CFUN=1"}'
    ```

    ![qlog 3](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog3.png){class="glboxshadow"}

5. Warten Sie 3-5 Minuten, damit ausreichend Protokolldaten gesammelt werden. Geben Sie danach den folgenden Befehl ein, um den QLog-Prozess zu beenden.

    ```
    ps | grep QLog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![qlog 4](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog4.png){class="glboxshadow"}

6. Protokolle exportieren.

    Mobilfunkmodem-Protokolle werden im Verzeichnis **/userdata/media/** mit dem Dateinamensuffix `xxx.qmdl` gespeichert.

    Melden Sie sich an der KVM-Konsole an, navigieren Sie zu **Virtual Media** und suchen Sie die Zieldatei(en) mit dem Suffix `xxx.qmdl`. Laden Sie diese Dateien herunter und geben Sie sie an den technischen Support von GL.iNet weiter.

    ![qlog 5](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog5.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
