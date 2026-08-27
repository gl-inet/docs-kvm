# KVM の電源が入らない場合はどうすればよいですか

電源ケーブルを接続した状態で KVM デバイスが起動しない場合は、次の方法を使用してトラブルシューティングを行ってください。

1. 電源ケーブルが適切な USB Type-C ポートに接続されていることを確認してください。

    Comet (GL-RM1) を例に挙げます。 2 つの USB Type-C ポートがあります。1 つは電源入力用 (電源アダプターに接続)、もう 1 つは信号送信用 (USB ケーブルを介して被制御デバイスに接続)。  

    2 つのポートが逆の場合、KVM の電源がオンにならず、マウスとキーボードが入力に応答しなくなります。  

    電源ケーブルをイーサネット ポートの隣の USB Type-C ポートに差し込んでください。

    ![plug in power cable](https://static.gl-inet.com/docs/kvm/faq/power_cable_connected_but_device_unpowered/plug_in_power_cable.jpg){class="glboxshadow"}

2. 一般的な 5V 2A 電源アダプターを使用して、LED が点灯するかどうかをテストして確認します。

    PD プロトコル電源アダプターの使用は避けてください。

    A 青色の LED の点灯は、デバイスが起動していることを示します。

3. リセット ボタンを 8 秒以上押して、工場出荷時の設定に戻します。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
