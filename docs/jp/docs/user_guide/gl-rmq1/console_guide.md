# Comet Q (GL-RMQ1) コンソール ガイド

## 設定

コンソールで、**Settings**に移動します。設定ページには 4 つのセクションが含まれています。 

- [ビデオ](#video)
- [オーディオ&キーボード&マウス](#audiokeyboardmouse)
- [システム](#system)
- [ネットワーク](#network)

### クイック検索

[設定] ページの上部にキーワードを入力すると、必要な設定をすぐに見つけることができます。

![quick search](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/quick-search.png){class="glboxshadow"}

### ビデオ

EDID、ビデオ品質、ビデオ送信、画面の向きなど、コンソールのビデオ設定をカスタマイズできます。

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-video.png){class="glboxshadow"}

- **Type**: 被制御デバイスのタイプを選択します。 

    システムは、推奨されるマウス モードと EDID 設定を自動的に適用して、最高のディスプレイ アスペクト比と制御精度を実現します。デバイスが正しく認識されない場合、またはカスタム タイプを使用する必要がある場合は、このオプションを切り替えます。

- **EDID**: Extended Display Identification Data の略で、最適な表示パラメータに自動的に一致します。

    デフォルト設定はほとんどのシナリオに適用され、通常は変更する必要はありません。詳細は[こちら](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}をご覧ください。 EDID 調整後に画面が更新されない場合は、被制御デバイスを再起動してください。

- **Mode**: 必要に応じてスマート モードとノーマル モードを切り替えます。スマート モードは、特に弱いネットワークでの帯域幅の消費を削減するのに役立ちます。

- **Quality**: ネットワーク環境と解像度の要件に応じて、ビデオ品質を低/中/高/超高/ロスレスに調整します。

- **Transfer**: ビデオ伝送方式を WebRTC、WebRTC (FEC)、ダイレクトの間で切り替えます。ダイレクト転送では音が出ませんのでご注意ください。

    !!! note "WebRTC、WebRTC (FEC) とダイレクトの違いは何ですか?"

        - **WebRTC**: リアルタイム リモート コントロールのために、滑らかなビデオと安定したオーディオのバランスをとります。
        
        - **WebRTC (FEC)**: 前方誤り訂正を追加して、ネットワーク状態が劣悪または不安定な場合の接続の安定性を向上させます。選択すると、少量の冗長データを送信することで失われたデータ パケットが自動的に修復され、画面のちらつきや遅延が軽減されます。
        
        - **Direct**: 最低の遅延とロスレスビデオ品質を提供しますが、オーディオ送信はサポートしていません。

- **Orientation**: コンソールの回転角度を 0°/90°/180°/270° に調整します。

- **View**: この設定は、ブラウザ ウィンドウのサイズを変更するときの画面のスケーリングを決定します。利用可能なオプション: アダプティブ、最高画質、オリジナル ピクセル。

### オーディオ&キーボード&マウス

オーディオ、キーボード、マウスの関連設定を調整できます。

![audio keyboard mouse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/audio-keyboard-mouse.png){class="glboxshadow"}

- **Speaker**: 被制御デバイスからのオーディオ出力を制御します (システム サウンド、ビデオ オーディオなど)。

- **Microphone**: ローカル オーディオ (ユーザーの声など) を制御側デバイスからリモート エンドに送信します。ワンクリックのミュート、およびマイクをアクティブにするための長押しショートカット (つまり、Press To Speak) をサポートしています。

    ![mic settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/mic-settings.png){class="glboxshadow"}

    ![press to speak](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/press-to-speak.png){class="glboxshadow"}

- **Keyboard**: 被制御デバイスのキーボードをオンまたはオフにします。

- **Bad Link Mode**: つまり、すぐにキーを放します。各キーの押下は 1 回の素早い押して放す動作として送信され、リモート制御中のキーの固着や意図しない繰り返し入力を防ぎます。

- **Show Virtual Keyboard**: コンソールに仮想キーボードを表示して使用します。

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: この機能は、Cmd キーと Ctrl キーを交換して、さまざまなオペレーティング システム間でキーボードの互換性を確保します。

- **Mouse**: 被制御デバイスのマウスをオンまたはオフにします。

- **Show Local Cursor**: 現在のデバイスのマウスを画面上に表示します。

- **Mouse Jiggle**: マウス ジグル機能は、微妙な周期的なマウスの動きをシミュレートし、リモート会議やサーバー管理中など、長時間非アクティブな状態が続いて被制御デバイスがスリープ状態になるのを防ぎます。

- **Scroll Rate**: マウス ホイールのスクロール速度、またはホイール 1 回転ごとにスクロールされる行/単位数を指し、リモコン上でコンテンツが移動する速度に影響します。

- **Scroll Direction**: マウス ホイールを上下にスクロールすると、リモート画面上のコンテンツが同じ方向 (自然スクロール) に移動するか、逆方向 (従来のスクロール) に移動するかを決定します。 

    標準、垂直反転、水平反転、両反転の 4 つの方向モードが利用可能です。  

- **Mouse Mode**: 絶対モードと相対モードを切り替えて、さまざまなリモート コントロール シナリオでスムーズかつ正確なカーソル制御を保証します。

    !!! note "絶対モードと相対モードの違いは何ですか?"

        - **Relative Mode**: マウスの位置は、固定された画面座標ではなく動きに基づいて計算されます。マウスを制御するには、リモート ウィンドウ内をクリックする必要があります。カーソルがリモート画面内でロックされ、スムーズに移動できません。このモードでは、BIOS、古いシステム、および組み込みデバイスとの互換性が向上します。

        - **Absolute Mode**: マウスの位置は正確な画面座標に対応します。リモート カーソルはローカル カーソルをスムーズかつ正確に追従するため、ローカル画面とリモート画面の間でシームレスに移動できます。ネットワーク伝送により若干の遅延が発生する場合がありますが、日常のデスクトップ制御や正確な操作に最適です。

        要するに、毎日の制御をスムーズに行うには、Absolute を使用します。 BIOS アクセス、絶対位置をサポートしていない一部の古いデバイス、または誤ったカーソルの移動を避けるために相対を使用します。

- **Relative Sensitivity**: マウス モードが相対の場合に使用できます。

### システム

コンソールのシステム表示設定をカスタマイズしたり、ワンクリックでデバイスをリセットしたりできます。

![settings-system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-system.png){class="glboxshadow"}

- **Device Identity**: 被制御デバイスによって認識される KVM の ID をカスタマイズまたは変更します。 EDID とデバイス ID は同期されたままであることに注意してください。どちらかを変更すると、もう一方も自動的に更新され、デバイスが正しく認識されるようになります。

    ![device identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/device-identity.png){class="glboxshadow"}

- **Language**: コンソールの言語を中国語または英語に設定します。

- **Color Mode**: テーマの色をライト モードまたはダーク モードにカスタマイズします。

- **Time Zone**: KVM コンソールのタイムゾーンをカスタマイズします。 

- **Reset KVM**: ワンクリックで KVM を工場出荷時設定にリセットします。

### ネットワーク

Comet Q のホスト名や IP アドレスなどのネットワークの詳細を確認および変更できます。

![settings-network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-network.png){class="glboxshadow"}

- **Hostname**: デバイスのホスト名はコンソールで直接変更できます。

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/hostname.png){class="glboxshadow"}

- **Wi-Fi**: Comet Q が Wi-Fi ネットワークに接続すると、ここに Wi-Fi IP アドレスが表示されます。 Wi-Fi SSID または右矢印をクリックして、SSID、割り当てられた IP アドレス、ゲートウェイ、Comet Q が接続に使用する MAC アドレスなどの Wi-Fi の詳細を表示します。

    ![wifi config](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/wifi-config.png){class="glboxshadow"}

    別の Wi-Fi ネットワークに接続する場合は、**Switch Wi-Fi** をクリックし、利用可能なネットワーク リストから Wi-Fi を選択します。

## ツールボックス

コンソールで、**Toolbox**に移動します。ツールボックス ページには、次の 3 つのセクションが含まれています。 

- [クリップボード](#clipboard)
- [ショートカット](#shortcut)
- [端末](#terminal)

### クリップボード

クリップボードを使用すると、ファイルを転送することなく、制御側デバイスから被制御デバイスにテキストを簡単に貼り付けることができます。

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-clipboard.png){class="glboxshadow"}

### ショートカット

ショートカットを使用すると、仮想キーボードを使用せずにアクションをより速く実行できるため、より効率的に作業し、日常業務の時間を節約できます。ここでいくつかの一般的なショートカットを見つけることができます。

![toolbox-shortcut1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut1.png){class="glboxshadow"}

**Modify** をクリックして、必要に応じてショートカット オプションを調整します。

![toolbox-shortcut2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut2.png){class="glboxshadow"}  

### ターミナル

Comet Q の端末にアクセスして、詳細な設定を行うことができます。 「**Access**」をクリックします。

![toolbox-terminal1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal1.png){class="glboxshadow"}

GLKVM ターミナルにリダイレクトされます。

![toolbox-terminal2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal2.png){class="glboxshadow"}

## 仮想メディア

コンソールで、**Virtual Media**に移動します。 Comet Q は、読み取り/書き込み USB ドライブをエミュレートできるため、制御側デバイスと制御側デバイスの間でファイルを共有および管理できます。

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-media.png){class="glboxshadow"}

### ファイル共有

**制御側デバイスから被制御デバイスにファイルを共有するには、以下の手順に従ってください。**

1. ボックスをドラッグまたはクリックして、制御側デバイスからファイルをアップロードするか、URL からアップロードします。 

    アップロードされると、以下のようにファイルが表示されます。

    ![file-sharing1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing1.png){class="glboxshadow"}

2. 「**Mount To Remote**」→「**File Sharing**」をクリックします。 

    ![file-sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing2.png){class="glboxshadow"}
以下に示すように、

3. A ウィンドウがコンソールにポップアップ表示され、ファイル共有の手順が示されます。
    
    ![file-sharing3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing3.png){class="glboxshadow"}

4. 少し待つと、**"GLKVM"** という名前のドライブが画面に自動的に表示されます。以前に制御側デバイスから Comet Q にアップロードしたファイルが、制御側デバイスに共有されていることがわかります。これで、被制御デバイス上のこのドライブ内のファイルを表示、移動、または削除できるようになります。

    ![file-sharing4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing4.png){class="glboxshadow"}

    **Tips**: ドライブが自動的にポップアップしない場合は、被制御デバイスの **This PC** に移動します。

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/thispc.png){class="glboxshadow"}
    
    次に、**GLKVM** という名前のドライブを見つけます。これで、このドライブ内のファイルを表示、移動、または削除できるようになります。

5. 共有を停止する場合は、ツールバーの **Virtual Media** をクリックし、**Stop Sharing** をクリックします。

    ![stop sharing1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing1.png){class="glboxshadow"}

**被制御デバイスから制御側デバイスにファイルを共有するには、以下の手順に従ってください。**

1. 被制御デバイスで、共有するファイルをドライブ **GLKVM** に移動またはコピーします。 

    たとえば、「gl-rm10_datasheet」という名前の PDF ファイルが、被制御デバイスのデスクトップからドライブ **GLKVM** に移動されました。 

    ![file-sharing5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing5.png){class="glboxshadow"}
    
2. Comet Q のコンソールに移動し、ツールバーの **Virtual Media** をクリックして、**Stop Sharing** をクリックします。

    ![stop sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing2.png){class="glboxshadow"}
    
3. このファイルは、次に示すように、**Virtual Media** の下に表示されます。これで、このファイルを Comet Q から制御側デバイスにダウンロードできるようになります。

    ![file sharing6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing6.png){class="glboxshadow"}

### ディスクをフォーマットします

ワンクリックでディスクをフォーマットしたり、仮想メディアを無効にしたりできます。

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/format-disable.png){class="glboxshadow"}

- **Format**: ディスク上のすべてのデータを消去し、ファイル システム構造を再初期化します。

- **Disable**: 仮想メディアを無効にすると、KVM デバイスがすぐに再起動されます。 

## アプリ センター

コンソールで、**Apps Center**に移動します。統合されたアプリケーションはここにあります。

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-center.png){class="glboxshadow"}

### Tailscale

[Tailscale](https://tailscale.com/){target="_blank"} は、ポート転送や複雑なファイアウォールの設定を行わずに、デバイス間で暗号化されたピアツーピア プライベート ネットワークを構築する WireGuard ベースのメッシュ VPN サービスです。

Comet Q は Tailscale と統合され、Tailscale 仮想ネットワーク経由でリモート アクセスできるようになります。

Comet Q と制御側デバイスを同じ Tailscale アカウントにバインドするだけで、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **Tailscale 仮想 IP** を入力することで、Comet Q にリモート アクセスできます。詳細は[こちら](../../faq/remote_access_via_tailscale.md){target="_blank"}をご参照ください。

バインド後、コンソールにはリンクされた Tailscale アカウントが表示され、出口ノードやサブネット ルートなどの高度な機能のロックが解除されます。

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier

[ZeroTier](https://www.zerotier.com/){target="_blank"} は、暗号化されたオーバーレイ仮想ネットワークを作成し、分散したデバイスをあたかも同じローカル エリア ネットワーク内にあるかのようにグローバルに接続します。

Comet Q は ZeroTier と統合されており、ZeroTier 仮想ネットワーク経由でリモート アクセスできるようになります。

Comet Q と制御側デバイスを同じ ZeroTier ネットワークに参加させるだけで、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **ZeroTier IP** を入力することで、Comet Q にリモート アクセスできます。詳細は[こちら](../../faq/remote_access_via_zerotier.md){target="_blank"}をご参照ください。

バインド後、コンソールには ZeroTier ネットワーク ID と仮想 IP が表示されます。

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-zerotier-enabled.png){class="glboxshadow"}

## ヘルプ

コンソールで、**Help**に移動します。ここでは、GL.iNet KVM に関する詳細情報とヘルプ ドキュメント、およびトラブルシューティング用のログをエクスポートできます。

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/help.png){class="glboxshadow"}

## ツールバー

コンソールで、右上隅に移動して次のツールにアクセスします。

- [ツールバーを折りたたむ](#collapse)
- [フルスクリーン](#fullscreen)
- [アップグレード](#upgrade)
- [クラウドサービス](#cloud-service)
- [セキュリティ](#security)
- 再起動
- ログアウト

### 折りたたむ

右上隅の上向き矢印アイコンをクリックして、ツールバーを折りたたみます。

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse1.png){class="glboxshadow"}

ツールバーが折りたたまれている場合、上部の下向き矢印アイコンをクリックして展開します。

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse2.png){class="glboxshadow"}

### フルスクリーン

右上隅の全画面アイコン (四角形) をクリックして、全画面モードに切り替えます。

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen1.png){class="glboxshadow"}

全画面表示を終了するには、**Esc** キーを押し続けるか、右上隅にある全画面表示を終了するアイコン (格子状) をクリックします。 

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen2.png){class="glboxshadow"}

### アップグレード

右上隅にあるファームウェアのバージョンをクリックして、アップデートを確認します。

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade1.png){class="glboxshadow"}

新しいファームウェアが利用可能な場合は、ポップアップ ウィンドウでオンライン アップグレードを実行できます。または、[ファームウェア ダウンロード センター](https://dl.gl-inet.com/kvm){target="_blank"} から最新のファームウェアをダウンロードし、必要に応じてローカル アップグレードを実行します。

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade2.png){class="glboxshadow"}

### クラウド サービス

GL.iNet KVM クラウドを使用すると、制御対象のデバイスにリモートからアクセスできます。詳細は[こちら](../../faq/remote_access_via_cloud.md){target="_blank"}をご参照ください。

Comet Q がクラウドにバインドされると、コンソールには次のようにクラウドのステータスが表示されます。

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/cloud.png){class="glboxshadow"}

### セキュリティ

セキュリティにより、管理者パスワードの変更、2 要素認証の有効化、TLS 証明書のカスタマイズが可能になります。 

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/security.png){class="glboxshadow"}

- 管理者パスワードの変更

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/admin-password.png){class="glboxshadow" width="434"}

- 2FA: アカウントを保護するために 2 要素認証を有効にします。

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/2fa.png){class="glboxshadow"}

- TLS 証明書

    システムは、ブラウザー アクセスにプリインストールされたデフォルトの証明書を使用します。 Web ブラウザー アクセス用の TLS 証明書をカスタマイズする場合は、コンソールの右上隅にある **TLS Certificate** をクリックし、**Custom Certificate** を選択して、**証明書ファイルと秘密キー ファイル**をアップロードします。

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/tls-certificate.png){class="glboxshadow"}
