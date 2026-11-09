# Fingerbotの使用時に「Press Failed」と表示された場合はどうすればよいですか？ {#what-should-i-do-if-i-see-press-failed-when-using-fingerbot}

Fingerbotの使用時にKVMコンソールに「Press Failed」と表示される場合、FingerbotとKVMデバイスのペアリングに問題がある可能性があります。

以下の手順で既存のペアリングを削除し、Fingerbotを再度ペアリングしてください。

1. KVMにログインし、**Toolbox** -> **Terminal** -> **Access Terminal** に移動してターミナルを開きます。

2. 以下のコマンドを順番に実行します。

    ```
    bluetoothctl
    ```
    ```
    scan on
    ```

    ![open bluetoothctl](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/bluetoothctl.png){class="glboxshadow"}

    しばらく待ってから `scan off` を実行し、スキャンを停止します。

3. `devices` を実行して、検出されたすべてのBluetoothデバイスを表示します。Fingerbot（FGBと表示）を探し、MACアドレスを記録します。

    ![devices](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/devices.png){class="glboxshadow"}

4. `exit` を入力してbluetoothctlセッションを終了します。次に以下のコマンドを実行し、古いペアリング記録を削除します。このMACアドレスを実際のFingerbotのMACアドレスに置き換えてください。

    ```
    bluetoothctl remove E1:2D:B2:75:D5:BC
    ```

5. 以下のコマンドでFingerbotを再度ペアリングします。このMACアドレスを実際のFingerbotのMACアドレスに置き換えてください。

    ```
    fingerbot pair E1:2D:B2:75:D5:BC
    ```

    ![repair fingerbot](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/repair.png){class="glboxshadow"}

    操作が成功すると、ターミナルに **Done** と表示されます。その後、Fingerbotを再度使用してみてください。

6. 問題が解決しない場合は、[support@gl-inet.com](mailto:support@gl-inet.com) にお問い合わせのうえ、詳しい調査のために以下の情報を提供してください。

    - 以下のコマンドの出力：

        ```
        fingerbot action
        ```
        ```
        ls -l /
        ```

    - **Help** > **Export Log Files** からエクスポートした最新のKVMログ。

        ![export logs](https://static.gl-inet.com/docs/kvm/faq/fingerbot_fails_to_press/export_logs.png){class="glboxshadow"}

---

まだ質問がありますか？ [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
