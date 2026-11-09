# Was soll ich tun, wenn bei der Verwendung von Fingerbot „Press Failed“ angezeigt wird? {#what-should-i-do-if-i-see-press-failed-when-using-fingerbot}

Wenn die KVM-Konsole bei der Verwendung von Fingerbot „Press Failed“ anzeigt, liegt möglicherweise ein Kopplungsproblem zwischen Fingerbot und Ihrem KVM-Gerät vor.

Führen Sie die folgenden Schritte aus, um die bestehende Kopplung zu entfernen und Fingerbot erneut zu koppeln.

1. Melden Sie sich bei Ihrem KVM an und öffnen Sie das Terminal über **Toolbox** -> **Terminal** -> **Access Terminal**.

2. Führen Sie die folgenden Befehle nacheinander aus:

    ```
    bluetoothctl
    ```
    ```
    scan on
    ```

    ![open bluetoothctl](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/bluetoothctl.png){class="glboxshadow"}

    Warten Sie einen Moment und führen Sie dann `scan off` aus, um die Suche zu beenden.

3. Führen Sie `devices` aus, um alle erkannten Bluetooth-Geräte anzuzeigen. Suchen Sie Ihren Fingerbot (als FGB aufgeführt) und notieren Sie seine MAC-Adresse.

    ![devices](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/devices.png){class="glboxshadow"}

4. Geben Sie `exit` ein, um die bluetoothctl-Sitzung zu verlassen. Führen Sie dann den folgenden Befehl aus, um den alten Kopplungseintrag zu entfernen. Ersetzen Sie diese MAC-Adresse durch die tatsächliche MAC-Adresse Ihres Fingerbot.

    ```
    bluetoothctl remove E1:2D:B2:75:D5:BC
    ```

5. Koppeln Sie Fingerbot mit dem folgenden Befehl erneut. Ersetzen Sie diese MAC-Adresse durch die tatsächliche MAC-Adresse Ihres Fingerbot.

    ```
    fingerbot pair E1:2D:B2:75:D5:BC
    ```

    ![repair fingerbot](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/repair.png){class="glboxshadow"}

    Bei erfolgreicher Ausführung wird im Terminal **Done** angezeigt. Versuchen Sie anschließend erneut, Fingerbot zu verwenden.

6. Wenn das Problem weiterhin besteht, kontaktieren Sie uns unter [support@gl-inet.com](mailto:support@gl-inet.com) und stellen Sie die folgenden Informationen zur weiteren Fehlerbehebung bereit.

    - Die Ausgabe der folgenden Befehle:

        ```
        fingerbot action
        ```
        ```
        ls -l /
        ```

    - Die aktuellen KVM-Protokolle, exportiert über **Help** > **Export Log Files**.

        ![export logs](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/export_logs.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
