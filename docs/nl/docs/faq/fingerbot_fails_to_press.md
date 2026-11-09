# Wat moet ik doen als "Press Failed" verschijnt bij het gebruik van Fingerbot? {#what-should-i-do-if-i-see-press-failed-when-using-fingerbot}

Als de KVM-console "Press Failed" weergeeft wanneer u Fingerbot gebruikt, is er mogelijk een probleem met de koppeling tussen Fingerbot en uw KVM-apparaat.

Volg de onderstaande stappen om de bestaande koppeling te verwijderen en Fingerbot opnieuw te koppelen.

1. Meld u aan bij uw KVM en ga naar **Toolbox** -> **Terminal** -> **Access Terminal** om de terminal te openen.

2. Voer de volgende opdrachten achtereenvolgens uit:

    ```
    bluetoothctl
    ```
    ```
    scan on
    ```

    ![open bluetoothctl](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/bluetoothctl.png){class="glboxshadow"}

    Wacht even en voer vervolgens `scan off` uit om het scannen te stoppen.

3. Voer `devices` uit om alle gedetecteerde Bluetooth-apparaten te bekijken. Zoek uw Fingerbot (vermeld als FGB) en noteer het MAC-adres.

    ![devices](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/devices.png){class="glboxshadow"}

4. Voer `exit` in om de bluetoothctl-sessie te verlaten. Voer vervolgens de onderstaande opdracht uit om de oude koppelingsregistratie te verwijderen. Vervang dit MAC-adres door het werkelijke MAC-adres van uw Fingerbot.

    ```
    bluetoothctl remove E1:2D:B2:75:D5:BC
    ```

5. Koppel Fingerbot opnieuw met de volgende opdracht. Vervang dit MAC-adres door het werkelijke MAC-adres van uw Fingerbot.

    ```
    fingerbot pair E1:2D:B2:75:D5:BC
    ```

    ![repair fingerbot](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/repair.png){class="glboxshadow"}

    Als de bewerking slaagt, verschijnt **Done** in de terminal. Probeer Fingerbot daarna opnieuw te gebruiken.

6. Als het probleem aanhoudt, neem dan contact met ons op via [support@gl-inet.com](mailto:support@gl-inet.com) en verstrek de onderstaande informatie voor verdere probleemoplossing.

    - De uitvoer van de volgende opdrachten:

        ```
        fingerbot action
        ```
        ```
        ls -l /
        ```

    - De meest recente KVM-logboeken, geëxporteerd via **Help** > **Export Log Files**.

        ![export logs](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/export_logs.png){class="glboxshadow"}

---

Hebt u nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
