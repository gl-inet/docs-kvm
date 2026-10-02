# ファームウェア v1.10

このリリースでは、ネイティブ WebRTC、リアルタイムのデータ監視、USB デバイスの一元管理、新しい Settings Center が導入されました。また、起動性能、セキュリティ、マイクの安定性も向上し、よりスムーズで信頼性の高いリモート KVM 操作を実現します。

最新のファームウェアは[ファームウェアダウンロードセンター](https://dl.gl-inet.com/kvm){target="_blank"}から入手できます。

## WebRTC (Native) Mode
このファームウェアでは、**WebRTC (Native) Mode** が導入されました。Google WebRTC Library を使用してストリーミング性能を向上させ、よりスムーズなリアルタイムのリモート操作を実現します。

![webrtc mode](https://static.gl-inet.com/docs/kvm/features_update/1.10/webrtc_native_mode.png){class="glboxshadow" width=400}

## Connection Stats

**Connection Stats** では、ネットワークのレイテンシー、ジッター、パケット損失率、ビットレート、フレームレート、再生遅延など、リアルタイムの接続情報と推移グラフを表示します。

- リストアイコンをクリックすると、リアルタイムの接続データとデバイスの状態を確認できます。

    ![Connection Stats 1](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_1.png){class="glboxshadow"}

- グラフアイコンをクリックすると、ネットワークのレイテンシー、ジッター、パケット損失率の推移グラフを確認できます。

    ![Connection Stats 2](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_2.png){class="glboxshadow"}

## Settings Center

このリリースでは、USB デバイス、環境設定、ネットワーク、セキュリティ、クラウド、システムの設定を一元管理する新しい **Settings Center** が追加されました。ホスト名の設定、クラウド管理、ファームウェアアップグレードなど、既存の設定にも一か所からアクセスしやすくなりました。

### USB Devices

**USB Devices** では、USB エミュレーションデバイスを一元管理できます。このページから仮想周辺機器を有効または無効にして、被制御デバイスとの互換性を向上させることができます。

![usb devices](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_usb_devices.png){class="glboxshadow"}

- **USB Emulated Devices**: マウス、キーボード、マイク、カメラ、仮想メディアなどの USB エミュレーションデバイスを有効または無効にします。一部のデバイスは同時に有効にできません。有効にできるデバイスは自動的に更新されます。

- **Device Identity**: 被制御デバイスが認識する KVM の識別情報をカスタマイズまたは変更します。EDID とデバイスの識別情報は常に同期されます。どちらかを変更すると、デバイスが正しく認識されるように、もう一方も自動的に更新されます。

### Preferences

**Preferences** では、レイアウト設定、システム設定、デバイスの画面設定を管理できます。

![preferences](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences**: 全画面モードのツールバーとウィンドウモードのステータスバーを設定します。

- **System Settings**: ブラウザーのタブタイトル、UI 言語、カラーモード、タイムゾーンを設定します。

- **Device Screen**: デバイスの内蔵ディスプレイをプレビューし、画面ロックモード、時刻形式、日付形式、壁紙などを設定します。

    **注**: この機能は、ディスプレイを内蔵したモデルでのみ利用できます。

### Network

ホスト名、イーサネット接続、ワイヤレスネットワーク情報など、デバイスのネットワーク設定を確認・管理できます。

![network](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_network.png){class="glboxshadow"}

- **Hostname**: コンソールからデバイスのホスト名を直接変更します。この機能はファームウェア v1.7.0 で導入されました。

- **Ethernet Settings**: イーサネット接続を確認・設定します。DHCP を使用してネットワーク設定を自動的に取得するか、**Static** を選択して IP アドレス、ネットマスク、ゲートウェイ、その他の必要なパラメーターを手動で入力できます。

- **Wireless**: デバイスが Wi‑Fi ネットワークに接続すると、IP アドレス、ゲートウェイ、MAC アドレスが表示されます。

    **注**: Wireless 機能は、対応モデルでのみ利用できます。

### Security

**Security** では、管理者パスワードの変更、二要素認証の有効化、TLS 証明書のカスタマイズができます。

![security](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_security.png){class="glboxshadow"}

- **Access Password**: 管理者パスワードを管理するか、二要素認証 (2FA) を有効にして、デバイスへのアクセスを保護します。

- **TLS Certificate**: ブラウザーからのアクセスにデフォルトの証明書を使用するか、カスタム証明書と秘密鍵をアップロードします。

### Cloud

URL またはコードを使用してデバイスをクラウドサービスにバインドし、リモートアクセスと管理を行えます。また、必要に応じてモバイルアプリのダウンロード、接続の管理、デバイスのバインド解除もできます。

![cloud](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_cloud.png){class="glboxshadow"}

### System

**System** では、システム管理、ファームウェアアップグレード、サポートの各項目にアクセスできます。

![system](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_system.png){class="glboxshadow"}

- **System**: デバイスを再起動するか、工場出荷時の設定にリセットします。

- **Upgrade**: Beta Center を有効にしてベータ版ファームウェアのアップデートを受け取るか、**Local Upgrade** を使用してローカルファイルからファームウェアをインストールします。

- **Help & Support**: トラブルシューティング用にデバイスのログをエクスポートし、ユーザーガイド、FAQ、その他のサポート文書にアクセスします。

## その他の機能強化

- **起動性能**: デバイスの起動速度が向上しました。

- **パスワードポリシー**: セキュリティを強化するため、パスワードポリシーが強化されました。パスワードは 10 文字以上で、少なくとも 2 種類の文字を含む必要があります。

- **Caps Lock インジケーター**: 被制御デバイスの Caps Lock の状態を示すインジケーターが追加されました。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
