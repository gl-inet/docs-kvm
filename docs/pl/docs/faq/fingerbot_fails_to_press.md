# Co zrobić, jeśli podczas korzystania z Fingerbot pojawia się komunikat „Press Failed”? {#what-should-i-do-if-i-see-press-failed-when-using-fingerbot}

Jeśli konsola KVM wyświetla komunikat „Press Failed” podczas korzystania z Fingerbot, może to oznaczać problem z parowaniem między Fingerbot a urządzeniem KVM.

Wykonaj poniższe kroki, aby usunąć istniejące parowanie i ponownie sparować Fingerbot.

1. Zaloguj się do KVM i przejdź do **Toolbox** -> **Terminal** -> **Access Terminal**, aby otworzyć terminal.

2. Uruchom kolejno następujące polecenia:

    ```
    bluetoothctl
    ```
    ```
    scan on
    ```

    ![open bluetoothctl](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/bluetoothctl.png){class="glboxshadow"}

    Poczekaj chwilę, a następnie uruchom `scan off`, aby zatrzymać skanowanie.

3. Uruchom `devices`, aby wyświetlić wszystkie wykryte urządzenia Bluetooth. Znajdź swój Fingerbot (widoczny jako FGB) i zanotuj jego adres MAC.

    ![devices](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/devices.png){class="glboxshadow"}

4. Wpisz `exit`, aby opuścić sesję bluetoothctl. Następnie uruchom poniższe polecenie, aby usunąć stary wpis parowania. Zastąp ten adres MAC rzeczywistym adresem MAC swojego Fingerbot.

    ```
    bluetoothctl remove E1:2D:B2:75:D5:BC
    ```

5. Ponownie sparuj Fingerbot za pomocą następującego polecenia. Zastąp ten adres MAC rzeczywistym adresem MAC swojego Fingerbot.

    ```
    fingerbot pair E1:2D:B2:75:D5:BC
    ```

    ![repair fingerbot](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/repair.png){class="glboxshadow"}

    Jeśli operacja się powiedzie, w terminalu pojawi się **Done**. Następnie spróbuj ponownie użyć Fingerbot.

6. Jeśli problem nadal występuje, skontaktuj się z nami pod adresem [support@gl-inet.com](mailto:support@gl-inet.com) i przekaż poniższe informacje w celu dalszej diagnostyki.

    - Wyniki następujących poleceń:

        ```
        fingerbot action
        ```
        ```
        ls -l /
        ```

    - Najnowsze dzienniki KVM, wyeksportowane przez **Help** > **Export Log Files**.

        ![export logs](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/export_logs.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
