# GLKVM アプリ経由のリモート アクセス時に接続が失敗しました

GLKVM アプリを介してリモートにアクセスすると、KVM デバイスが GLKVM アプリでオンラインと表示されているにもかかわらず、クリックすると「接続中」のままになるという問題が発生することがあります。

![device online](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/device_online.png){class="glboxshadow"}

![connecting](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/connecting.png){class="glboxshadow"}

トラブルシューティング ガイド:

1. 安定したネットワーク接続を確保します。

    KVM が安定したインターネットに接続されていることを確認してください。 LED が白色に点灯している場合は、ネットワーク接続が正常であることを示します。

2. ネットワーク ファイアウォール ルールを確認してください。

    ローカル ファイアウォールを一時的に無効にするか、GL.iNet 関連のドメイン (glkvm.com など) をファイアウォールの許可リストに追加します。変更を適用した後、接続を再試行します。

    以下は、Sky Network のファイアウォール ルールを変更する手順です。参考にしてください。

    ??? note "Sky ネットワーク (例: Sky Max Hub)"

        Sky Network のセキュリティメカニズムにより、ドメイン名 `glkvm.com` が不審なサイトとして識別され、アクセスがブロックされる場合があります。 Sky アプリを通じて制限を解除できます。<br>

        1. MySky アプリを開き、**Broadband** -> **Advanced Security** に移動し、GL.iNet 関連のドメインが制限されているかどうかを確認します。

            ![mysky-1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-1.png){class="glboxshadow"}

        2. ドメインがブロックされていることがわかった場合は、下向き矢印をクリックして詳細を表示し、**Allow Access** を選択して制限を解除します。

            ![mysky-2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/mysky-2.png){class="glboxshadow" width="300"}

3. 制御側デバイスで VPN/プロキシを無効にします。

    GLKVM アプリを実行しているデバイスで VPN サービスやプロキシ サービスが有効になっていないことを確認してください。これらのサービスは接続を妨げる可能性があります。

4. 可能であれば、KVM を再起動します。

    可能であれば、KVM デバイスでハードウェアの再起動を実行し、一時的なネットワークまたはソフトウェアの問題を解決します。

    KVM デバイスの近くにいない場合は、GLKVM アプリを介してリモートで再起動できます。

    1. デバイス リストで、デバイスの右上隅にある **Manage** をクリックします。

        ![app reboot 1](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_1.png){class="glboxshadow"}

    2. **More** をクリックし、**Reboot** を選択します。

        ![app reboot 2](https://static.gl-inet.com/docs/kvm/faq/connection_failed_when_remotely_accessing_via_glkvm/app_reboot_2.png){class="glboxshadow"}

追加の技術ノート:

1. ドメインの DNS 解決が機能していることを確認します。

2. 標準の KVM/リモート アクセス ポートへの送信トラフィックがブロックされていないことを確認します。

3. エンタープライズ ネットワークの場合、潜在的なトラフィック フィルタリング ポリシーについて IT 管理者に相談してください。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
