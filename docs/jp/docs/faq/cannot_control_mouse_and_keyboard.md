# マウスとキーボードを制御できない場合はどうすればよいですか

すべてのケーブルが正しく接続されている場合でも、KVM を介して被制御デバイスのマウスとキーボードを制御できない場合は、次のような提案があります。

1. 配線を確認してください。 

    Comet (GL-RM1) を例に挙げます。 USB Type-C ポートが 2 つあります。  

    - 側面にあるものは、電源入力 (電源アダプターに接続) 用に「5V 2A」とラベルが付いています。  
    - 背面のもう 1 つはマウスとキーボードのロゴがあり、被制御デバイスの USB ポートに接続してキーボードとマウスの信号を受信します。 

    これら 2 つの接続を混同すると、KVM デバイスが起動せず、マウスとキーボードが応答しなくなります。
    
    これら 2 つの Type-C インターフェイスが正しく接続されているかどうかを確認してください。

    ![gl-rm1 ports](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/gl-rm1-ports.png){class="glboxshadow gl-80-desktop"}

2. USB ケーブルを確認してください。 

    付属のUSBケーブルをご使用ください。被制御デバイスの USB ポートが KVM の USB ポートに接続され、データ送信がサポートされていることを確認します。

    データ転送が可能なケーブルのみで、リモート デバイスのキーボードとマウスの制御が可能になります。

    USB ケーブルを再接続し、被制御デバイスを再起動します。

3. マウス モードを相対モードに切り替えます。 

    KVM にログインし、[設定] -> [マウス モード] に移動し、[相対] に切り替えて、問題が解決できるかどうかを確認します。

    ![mouse mode](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/mouse_mode.jpg){class="glboxshadow"}

4. 仮想メディアを無効にします。

    KVM にログインし、仮想メディアに移動し、3 点アイコンをクリックして無効にします。

    ![disable virtual media](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/disable_virtual_media.png){class="glboxshadow" width="422"}

    これは、仮想メディアが有効になっている場合、KVM は、制御対象のデバイスに接続されている USB ストレージ ドライブをシミュレートできるためです。ただし、一部のデバイスでは、不明な USB ストレージ ドライブが検出されると、すべての USB 入力が無効になり、マウスとキーボードが応答しなくなる場合があります。

5. デバイス ID を変更します。

    KVM にログインし、[設定] -> [システム] -> [デバイス ID] に移動し、被制御デバイスによって認識される KVM の ID を変更します。

    ![change device identity](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/change_device_identity.png){class="glboxshadow"}

6. KVM のファームウェアを最新バージョンにアップグレードします。 [KVM ファームウェア ダウンロード センター](https://dl.gl-inet.com/kvm){target="_blank"}

7. 制御されているコンピューターのデバイス マネージャーで、誤動作しているドライバーがないか確認してください。

8. 被制御デバイスがITセキュリティソフトウェアによってブロックされていないか確認してください。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
