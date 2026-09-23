# ファームウェア v1.9

このリリースでは、新機能、操作性の向上、プライバシー保護の強化、ネットワーク接続の安定性向上により、より安全で快適なリモート KVM 操作を実現します。

最新のファームウェアは[ファームウェアダウンロードセンター](https://dl.gl-inet.com/kvm){target="_blank"}から入手できます。

## レイテンシーモード

このファームウェアでは、入力への応答速度と映像の滑らかさを調整する **Latency Mode** が導入されました。用途に応じて Lowest Latency または Smooth Display を選択できます。

![latency mode](https://static.gl-inet.com/docs/kvm/features_update/1.9/latency_mode.png){class="glboxshadow" width="360"}

- Lowest Latency: 入力レイテンシーを最小限に抑え、キーボードとマウスのフィードバックをよりスムーズにします。
- スムーズ ディスプレイ: 視覚出力を最適化して途切れやフレーム ドロップを排除し、安定した再生を実現します。

## マウス操作

マウスの使いやすさを向上させるために、新しいプライマリ マウス ボタン スワップ オプション **Primary Button** が追加されました。個人の使用習慣に合わせて、左ボタンまたは右ボタンのいずれかを主クリックとして設定できます。

![primary button](https://static.gl-inet.com/docs/kvm/features_update/1.9/primary_button.png){class="glboxshadow" width="360"}

## 画面表示

画面ロック、壁紙、時間形式 (24 時間/12 時間)、日付形式など、タッチスクリーンを介して KVM の **Screen Display** 設定をカスタマイズできます。この機能はタッチスクリーン搭載モデルのみの機能です。

さらに、数回タップするだけで、Tailscale や NetBird などのオーバーレイ ツールをタッチスクリーンから直接すばやく設定できます。この機能は、以前のファームウェア リリースでは利用できませんでした。

![screen display](https://static.gl-inet.com/docs/kvm/features_update/1.9/screen_display.png){class="glboxshadow" width="360"}

## 言語

以前のファームウェア バージョンは中国語と英語のみをサポートしていました。このビルドでは、ネイティブ **Japanese** 言語サポートが追加され、日本のユーザーのアクセシビリティが向上します。

![language](https://static.gl-inet.com/docs/kvm/features_update/1.9/language.png){class="glboxshadow" width="360"}

## 拡張機能

このリリースでは、安全なプライベート ホーム ネットワークとビジネス ネットワークを構築するためのオープンソースのゼロトラスト ネットワーキング プラットフォームである [**NetBird**](https://netbird.io/){target="_blank"} が統合されています。 WireGuard® 上に構築されたこのオーバーレイ ソリューションにより、NetBird 仮想ネットワークを介してどこからでも KVM への安全なリモート アクセスが可能になります。
セットアップ手順については、[こちら](../faq/remote_access_via_netbird.md){target="_blank"}を参照してください。

![netbird](https://static.gl-inet.com/docs/kvm/features_update/1.9/nerbird.png){class="glboxshadow"}

## その他の機能強化

- Beta ファームウェア プログラム: ユーザーは、ベータ プログラムにオプトインして、プレリリース機能をテストできます。

- テキスト認識: 光学式文字認識 (OCR) を利用したこのツールを使用すると、リモート ディスプレイ上の選択した領域からテキストをキャプチャできます。中国語、英語、中国語と英語のバイリンガルモードに対応しています。詳しくは[こちら](../tutorials/how_to_capture_text_from_remote_screen.md)をご覧ください。

- 都市ベースのタイムゾーン: 対象の都市を選択してタイムゾーンを設定します。

- Login セッション セキュリティ: ログイン トークンは、セッション終了後 12 時間で期限切れになります (トークンは以前は永続的でした)。

- システム ログ セキュリティ: すべてのシステム ログに機密データのマスキングが実装されました。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
