# Vad gör jag om "Press Failed" visas när jag använder Fingerbot? {#what-should-i-do-if-i-see-press-failed-when-using-fingerbot}

Om KVM-konsolen visar "Press Failed" när du använder Fingerbot kan det finnas ett parkopplingsproblem mellan Fingerbot och din KVM-enhet.

Följ stegen nedan för att ta bort den befintliga parkopplingen och parkoppla Fingerbot igen.

1. Logga in på din KVM och gå till **Toolbox** -> **Terminal** -> **Access Terminal** för att öppna terminalen.

2. Kör följande kommandon i ordning:

    ```
    bluetoothctl
    ```
    ```
    scan on
    ```

    ![open bluetoothctl](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/bluetoothctl.png){class="glboxshadow"}

    Vänta en stund och kör sedan `scan off` för att stoppa sökningen.

3. Kör `devices` för att visa alla upptäckta Bluetooth-enheter. Leta upp din Fingerbot (visas som FGB) och anteckna dess MAC-adress.

    ![devices](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/devices.png){class="glboxshadow"}

4. Skriv `exit` för att lämna bluetoothctl-sessionen. Kör sedan kommandot nedan för att ta bort den gamla parkopplingsposten. Ersätt denna MAC-adress med din Fingerbots faktiska MAC-adress.

    ```
    bluetoothctl remove E1:2D:B2:75:D5:BC
    ```

5. Parkoppla Fingerbot igen med följande kommando. Ersätt denna MAC-adress med din Fingerbots faktiska MAC-adress.

    ```
    fingerbot pair E1:2D:B2:75:D5:BC
    ```

    ![repair fingerbot](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/repair.png){class="glboxshadow"}

    Om åtgärden lyckas visas **Done** i terminalen. Försök sedan använda Fingerbot igen.

6. Om problemet kvarstår kontaktar du oss på [support@gl-inet.com](mailto:support@gl-inet.com) och lämnar informationen nedan för fortsatt felsökning.

    - Utdata från följande kommandon:

        ```
        fingerbot action
        ```
        ```
        ls -l /
        ```

    - De senaste KVM-loggarna, exporterade via **Help** > **Export Log Files**.

        ![export logs](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/export_logs.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
