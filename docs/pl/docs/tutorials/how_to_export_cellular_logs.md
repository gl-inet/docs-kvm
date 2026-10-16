# Jak wyeksportować logi sieci komórkowej

Ten poradnik przedstawia kroki eksportowania logów związanych z siecią komórkową z urządzenia KVM na potrzeby rozwiązywania problemów.

W poniższym przykładzie użyto Comet 5G (GL-RM10RC).

1. Zaloguj się do konsoli KVM, przejdź do **Virtual Media** i upewnij się, że ta funkcja jest włączona.

2. Przejdź do **Toolbox** -> **Terminal**. Kliknij **Access**, aby otworzyć terminal KVM.

    ![Dostęp do terminala](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/access_terminal.png){class="glboxshadow"}

3. W oknie terminala wykonaj poniższe polecenie, aby uruchomić program QLog.

    ```
    QLog_1.5.22 -s /userdata/media/ -f /etc/HN_default.cfg & ubus call modem at '{"AT":"AT+QCFG=\"DBGCTL\",0"}'
    ```

    ![Uruchamianie QLog](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog1.jpg){class="glboxshadow"}

    Na stronie pojawią się informacje o inicjalizacji QLog, a następnie statystyki danych w czasie rzeczywistym (np. ilość odebranych danych i czas, który upłynął), jak pokazano poniżej.

    ![Statystyki QLog](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog2.jpg){class="glboxshadow"}

4. Naciśnij Enter i wykonaj kolejno poniższe polecenia, aby uruchomić modem ponownie i zebrać logi całego procesu uruchamiania.

    ```
    ubus call modem at '{"AT":"AT+CFUN=0"}'
    ```

    ```
    ubus call modem at '{"AT":"AT+CFUN=1"}'
    ```

    ![Ponowne uruchamianie modemu](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog3.png){class="glboxshadow"}

5. Poczekaj 3–5 minut, aby zebrać wystarczającą ilość danych logów. Następnie wpisz poniższe polecenie, aby zatrzymać proces QLog.

    ```
    ps | grep QLog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![Zatrzymywanie QLog](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog4.png){class="glboxshadow"}

6. Wyeksportuj logi.

    Logi modemu komórkowego są zapisywane w katalogu **/userdata/media/** w plikach o nazwach zakończonych na `xxx.qmdl`.

    Zaloguj się do konsoli KVM, przejdź do **Virtual Media** i znajdź odpowiednie pliki z końcówką `xxx.qmdl`. Pobierz je i przekaż pomocy technicznej GL.iNet.

    ![Eksportowanie logów](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog5.png){class="glboxshadow"}

---

Masz pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
