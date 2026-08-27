# Comet X (GL-RM4PE) コンソール ガイド

## 設定

コンソールで、**Settings**に移動します。設定ページには 4 つのセクションが含まれています。

- [ビデオ](#video)
- [リモートデバイス設定](#remote-device-settings)
- [システム](#system)
- [ネットワーク](#network)

### クイック検索

[設定] ページの上部にキーワードを入力すると、必要な設定をすぐに見つけることができます。

![quick search](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/quick-search.png){class="glboxshadow"}

### ビデオ

表示モード、ビデオ送信、画面の向き、EDID など、本体のビデオ設定をカスタマイズできます。

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings-video.png){class="glboxshadow"}

- **Mode**: 必要に応じてスマート モードとノーマル モードを切り替えます。スマート モードは、特に弱いネットワークでの帯域幅の消費を削減するのに役立ちます。

- **Transfer**: ビデオ伝送方式を WebRTC、WebRTC (FEC)、ダイレクトの間で切り替えます。ダイレクト転送では音が出ませんのでご注意ください。

    !!! note "WebRTC、WebRTC (FEC) とダイレクトの違いは何ですか?"

        - **WebRTC**: リアルタイム リモート コントロールのために、滑らかなビデオと安定したオーディオのバランスをとります。

        - **WebRTC (FEC)**: 前方誤り訂正を追加して、貧弱または不安定なネットワーク条件下での接続の安定性を向上させます。選択すると、少量の冗長データを送信することで失われたデータ パケットが自動的に修復され、画面のちらつきや遅延が軽減されます。

        - **Direct**: 最低の遅延とロスレスビデオ品質を提供しますが、オーディオ送信はサポートしていません。

- **Orientation**: コンソールの回転角度を 0°/90°/180°/270° に調整します。

- **EDID**: Extended Display Identification Data の略で、最適な表示パラメータに自動的に一致します。

    デフォルト設定はほとんどのシナリオに適用され、通常は変更する必要はありません。詳細は[こちら](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}をご覧ください。 EDID 調整後に画面が更新されない場合は、被制御デバイスを再起動してください。

- **View**: この設定は、ブラウザ ウィンドウのサイズを変更するときの画面のスケーリングを決定します。利用可能なオプション: アダプティブ、最高画質、オリジナル ピクセル。

### リモートデバイスの設定

被制御デバイスの関連設定を調整できます。

![settings-remote device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings-remote-device.png){class="glboxshadow"}

- **Speaker**: 被制御デバイスからのオーディオ出力を制御します (システム サウンド、ビデオ オーディオなど)。

- **Microphone**: ローカル オーディオ (ユーザーの声など) を制御側デバイスからリモート エンドに送信します。ワンクリックのミュート、およびマイクをアクティブにするための長押しショートカット (つまり、Press To Speak) をサポートしています。

    ![mic settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/mic-settings.png){class="glboxshadow"}

    ![press to speak](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/press-to-speak.png){class="glboxshadow"}

- **Keyboard**: 被制御デバイスのキーボードをオンまたはオフにします。

- **Bad Link Mode**: つまり、すぐにキーを放します。各キーの押下は 1 回の素早い押して放す動作として送信され、リモート制御中のキーの固着や意図しない繰り返し入力を防ぎます。

- **Show Virtual Keyboard**: コンソールに仮想キーボードを表示して使用します。

    ![virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/virtual-keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: この機能は、Cmd キーと Ctrl キーを交換して、さまざまなオペレーティング システム間でキーボードの互換性を確保します。

- **Mouse**: 被制御デバイスのマウスをオンまたはオフにします。

- **Show Local Cursor**: 現在のデバイスのマウスを画面上に表示します。

- **Mouse Jiggle**: マウス ジグル機能は、微妙な周期的なマウスの動きをシミュレートし、リモート会議やサーバー管理中など、長時間非アクティブな状態が原因で被制御デバイスがスリープ状態になるのを防ぎます。

- **Scroll Rate**: マウス ホイールのスクロール速度、またはホイール 1 回転ごとにスクロールされる行/単位数を指し、リモコン上でコンテンツが移動する速度に影響します。

- **Scroll Direction**: マウス ホイールを上下にスクロールすると、リモート画面上のコンテンツが同じ方向 (自然スクロール) に移動するか、逆方向 (従来のスクロール) に移動するかを決定します。

    標準、垂直反転、水平反転、両反転の 4 つの方向モードが利用可能です。

- **Mouse Mode**: 絶対モードと相対モードを切り替えて、さまざまなリモート コントロール シナリオでスムーズかつ正確なカーソル制御を保証します。

    !!! note "絶対モードと相対モードの違いは何ですか?"

        - **Relative Mode**: マウスの位置は、固定された画面座標ではなく動きに基づいて計算されます。マウスを制御するには、リモート ウィンドウ内をクリックする必要があります。カーソルがリモート画面内でロックされ、スムーズに移動できません。このモードでは、BIOS、古いシステム、組み込みデバイスとの互換性が向上します。

        - **Absolute Mode**: マウスの位置は正確な画面座標に対応します。リモート カーソルはローカル カーソルをスムーズかつ正確に追従するため、ローカル画面とリモート画面の間でシームレスに移動できます。ネットワーク伝送により若干の遅延が発生する場合がありますが、日常のデスクトップ制御や正確な操作に最適です。

        要するに、毎日の制御をスムーズに行うには、Absolute を使用します。 BIOS アクセス、絶対位置をサポートしていない一部の古いデバイス、または誤ったカーソルの移動を避けるために相対を使用します。

- **Relative Sensitivity**: マウス モードが相対の場合に使用できます。

### システム

コンソールのシステム表示設定をカスタマイズしたり、ワンクリックでデバイスをリセットしたりできます。

![settings-system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings-system.png){class="glboxshadow"}

- **Device Identity**: 被制御デバイスによって認識される KVM の ID をカスタマイズまたは変更します。 EDID とデバイス ID は同期されたままであることに注意してください。どちらかを変更すると、もう一方も自動的に更新され、デバイスが正しく認識されるようになります。

    ![device identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/device-identity.png){class="glboxshadow"}

- **Language**: コンソールの言語を中国語または英語に設定します。

- **Color Mode**: テーマの色をライト モードまたはダーク モードにカスタマイズします。

- **Time Zone**: KVM コンソールのタイムゾーンをカスタマイズします。

- **Reset KVM**: ワンクリックで KVM を出荷時設定にリセットします。

### ネットワーク

Comet X のホスト名や IP アドレスなどのネットワークの詳細を確認および変更できます。

![settings-network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings-network.png){class="glboxshadow"}

- **Hostname**: デバイスのホスト名はコンソールで直接変更できます。

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/hostname.png){class="glboxshadow"}

- **Ethernet**: Comet X がイーサネット ケーブル経由でネットワーク デバイスに接続すると、ここに IP アドレスが表示されます。 IP アドレスまたは右矢印をクリックして、イーサネットの詳細を表示します。

    プロトコルが DHCP の場合、ページは次のように表示されます。

    ![ethernet dhcp](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/eth-dhcp.png){class="glboxshadow"}

    静的 IP アドレスを設定する場合は、プロトコルを **Static** に切り替え、必要なネットワーク パラメーター (IP アドレス、ネットマスク、ゲートウェイなど) をそれに応じて入力します。

    ![ethernet static](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/eth-static.png){class="glboxshadow"}

## ツールボックス

コンソールで、**Toolbox**に移動します。ツールボックス ページには、次の 4 つのセクションが含まれています。

- [クリップボード](#clipboard)
- [ショートカット](#shortcut)
- [ウェイク オン ラン](#wake-on-lan)
- [端末](#terminal)

### クリップボード

クリップボードを使用すると、ファイルを転送することなく、制御側デバイスから被制御デバイスにテキストを簡単に貼り付けることができます。

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox-clipboard.png){class="glboxshadow"}

### ショートカット

ショートカットを使用すると、仮想キーボードを使用せずにアクションをより速く実行できるため、より効率的に作業し、日常業務の時間を節約できます。ここでいくつかの一般的なショートカットを見つけることができます。

![toolbox-shortcut1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox-shortcut1.png){class="glboxshadow"}

**Modify** をクリックして、必要に応じてショートカット オプションを調整します。

![toolbox-shortcut2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox-shortcut2.png){class="glboxshadow"}

### ウェイク オン ラン

Wake-on-LAN (WOL) は、被制御デバイスの電源をリモートでオンにしたり、低電力状態から復帰したりできるようにするテクノロジーです。

**Add Device** をクリックし、同じ LAN からデバイスを選択します。

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox-wol.png){class="glboxshadow"}

![wol-add-device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/wol-add-device.png){class="glboxshadow"}

追加したいデバイスがリストにない場合は、**Add Manually** をクリックしてデバイス名と MAC アドレスを入力します。

![wol-add-manually](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/wol-add-manually.png){class="glboxshadow"}

### ターミナル

Comet Xの端末にアクセスして、詳細な設定を行うことができます。 「**Access**」をクリックします。

![toolbox-terminal1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox-terminal1.png){class="glboxshadow"}

GLKVM ターミナルにリダイレクトされます。

![toolbox-terminal2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox-terminal2.png){class="glboxshadow"}

## アクセサリー

GL.iNet は、デバイスの電源オン/オフをリモート制御するためのオプションの KVM アクセサリを提供します。

まず、対応するユーザー ガイドを参照して、アクセサリを被制御デバイスに接続します。 Comet X は同時に 4 つの Fingerbot または ATX ボードに接続できますが、一度に制御できるのは 1 つだけであることに注意してください。

- [フィンガーボット(FGB-01) ユーザーガイド](../gl-fgb-01/index.md){target="_blank"}

- [ATX ボード (GL-ATXPC) ユーザーガイド](../gl-atx-board/index.md){target="_blank"}

2 番目に、KVM コンソールにログインし、**Accessories** に移動します。アクセサリの設定は、アクセサリをインストールした後にのみ使用できます。

### フィンガーボット

Fingerbot は、被制御デバイスの物理的な電源ボタンに貼り付けられ、被制御デバイスの電源の遠隔制御を実現します。

本体の設定に従って動作します。

![accessories fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/accessories-fgb.png){class="glboxshadow"}

- **Time**: フィンガーボットの押し続ける時間。 0.5秒/3秒/8秒に設定できます。

- **Strength**:押す強さは「軽く押す」と「しっかり押す」の2段階です。

    - **Lightly Press**: 短いボタンまたはソフトタッチのボタンに最適です。

    - **Firmly Press**: 深いボタンやしっかりとしたボタンに最適です。

    ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### ATX 電源

ATX ボードはコンピューターのケースに取り付けられており、デバイスの電源オン/オフ/再起動をリモートで制御します。

本体の設定に従って動作します。

- **電源 (短く押す)**: 通常の電源投入またはシステムのウェイクアップに使用されます。

- **電源 (長押し)**: 強制シャットダウン操作を実行します。

- **Restart**: デバイスを再起動します。

## 仮想メディア

コンソールで、**Virtual Media**に移動します。ここでは次の操作を実行できます。

- [ファイル共有](#file-sharing)
- [画像取付](#image-mounting)
- [ディスクのフォーマット](#format-disk)

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/virtual-media.png){class="glboxshadow"}

### ファイル共有

Comet X は、読み取り/書き込み USB ドライブをエミュレートできるため、制御側デバイスと制御側デバイスの間でファイルを共有および管理できます。

**制御側デバイスから被制御デバイスにファイルを共有するには、以下の手順に従ってください。**

1. ボックスをドラッグまたはクリックして、制御側デバイスからファイルをアップロードするか、URL からアップロードします。

    アップロードされると、以下のようにファイルが表示されます。

    ![file sharing1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file-sharing1.png){class="glboxshadow"}

2. 「**Mount To Remote**」→「**File Sharing**」をクリックします。

    ![file sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file-sharing2.png){class="glboxshadow"}
以下に示すように、

3. A ウィンドウがコンソールにポップアップ表示され、ファイル共有の手順が示されます。

    ![file sharing3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file-sharing3.png){class="glboxshadow"}

4. 少し待つと、**"GLKVM"** という名前のドライブが画面に自動的に表示されます。以前に制御側デバイスから Comet X にアップロードしたファイルが、制御側デバイスに共有されていることがわかります。これで、被制御デバイス上のこのドライブ内のファイルを表示、移動、または削除できるようになります。

    ![file sharing4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file-sharing4.png){class="glboxshadow"}

    **Tips**: ドライブが自動的にポップアップしない場合は、被制御デバイスの **This PC** に移動します。

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/thispc.png){class="glboxshadow"}

    次に、**GLKVM** という名前のドライブを見つけます。これで、このドライブ内のファイルを表示、移動、または削除できるようになります。

5. 共有を停止する場合は、ツールバーの **Virtual Media** をクリックし、**Stop Sharing** をクリックします。

    ![stop sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/stop-sharing1.png){class="glboxshadow"}

**被制御デバイスから制御側デバイスにファイルを共有するには、以下の手順に従ってください。**

1. 被制御デバイスで、共有するファイルをドライブ **GLKVM** に移動またはコピーします。

    たとえば、「gl-rm10_datasheet」という名前のイメージが、被制御デバイスのデスクトップからドライブ **GLKVM** に移動されました。

    ![file sharing5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file-sharing5.png){class="glboxshadow"}

2. Comet X のコンソールに移動し、ツールバーの **Virtual Media** をクリックして、**Stop Sharing** をクリックします。

    ![stop sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/stop-sharing2.png){class="glboxshadow"}

3. このファイルは、次に示すように、**Virtual Media** の下に表示されます。これで、このファイルを Comet X から制御側デバイスにダウンロードできるようになります。

    ![file sharing6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file-sharing6.png){class="glboxshadow"}

### イメージのマウント

Comet X は、被制御デバイス上の読み取り専用の仮想 CD/DVD またはディスク ドライブをシミュレートできます。 BIOS または UEFI 起動プロセス中にこのドライブにアクセスできます。

この機能は、オペレーティング システムを再インストールしたり、ISO をマウントして制御対象のデバイスにアプリケーションをインストールしたり、その他のタスクを実行したりするのに役立ちます。

1. ボックスをドラッグまたはクリックしてファイルをアップロードします。 **このファイルが ISO 形式としてマウントできることを確認してください**。

    アップロードされると、以下のようにファイルが表示されます。

    ![image mount1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/image-mount1.png){class="glboxshadow"}

2. 「**Mount To Remote**」→「**Image Mounting**」をクリックします。

    ![image mount2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/image-mount2.png){class="glboxshadow"}

3. ポップアップ ウィンドウでファイルを選択し、**Mount Image** をクリックします。

    ![image mount3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/image-mount3.png){class="glboxshadow"}

4. これで、被制御デバイスの CD ドライブからこのファイルを使用できるようになります。

    ![image mount4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/image-mount4.png){class="glboxshadow"}

### ディスクをフォーマットします

ワンクリックでディスクをフォーマットしたり、仮想メディアを無効にしたりできます。

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/format-disable.png){class="glboxshadow"}

- **Format**: ディスク上のすべてのデータを消去し、ファイル システム構造を再初期化します。

- **Disable**: 仮想メディアを無効にすると、KVM デバイスがすぐに再起動されます。

## アプリ センター

コンソールで、**Apps Center**に移動します。統合されたアプリケーションはここにあります。

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/apps-center.png){class="glboxshadow"}

### Tailscale

[Tailscale](https://tailscale.com/){target="_blank"} は、ポート転送や複雑なファイアウォール設定を行わずに、デバイス間で暗号化されたピアツーピア プライベート ネットワークを構築する WireGuard ベースのメッシュ VPN サービスです。

Comet X は Tailscale と統合されており、Tailscale 仮想ネットワーク経由でリモート アクセスできるようになります。

Comet X と制御側デバイスを同じ Tailscale アカウントにバインドするだけで、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **Tailscale 仮想 IP** を入力することで、Comet X にリモート アクセスできます。詳細は[こちら](../../faq/remote_access_via_tailscale.md){target="_blank"}をご参照ください。

バインド後、コンソールにはリンクされた Tailscale アカウントが表示され、出口ノードやサブネット ルートなどの高度な機能のロックが解除されます。

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier

[ZeroTier](https://www.zerotier.com/){target="_blank"} は、暗号化されたオーバーレイ仮想ネットワークを作成し、分散したデバイスをあたかも同じローカル エリア ネットワーク内にあるかのようにグローバルに接続します。

Comet X は ZeroTier と統合され、ZeroTier 仮想ネットワーク経由でリモート アクセスできるようになります。

Comet X と制御側デバイスを同じ ZeroTier ネットワークに参加させるだけで、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **ZeroTier IP** を入力することで、Comet X にリモート アクセスできます。詳細は[こちら](../../faq/remote_access_via_zerotier.md){target="_blank"}をご参照ください。

バインド後、コンソールには ZeroTier ネットワーク ID と仮想 IP が表示されます。

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/apps-zerotier-enabled.png){class="glboxshadow"}

## ヘルプ

コンソールで、**Help**に移動します。ここでは、GL.iNet KVM に関する詳細情報とヘルプ ドキュメント、およびトラブルシューティング用のログをエクスポートできます。

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/help.png){class="glboxshadow"}

## ツールバー

コンソールで、右上隅に移動して次のツールにアクセスします。

- [スイッチ信号](#switch-signal)
- [ツールバーを折りたたむ](#collapse)
- [フルスクリーン](#fullscreen)
- [アップグレード](#upgrade)
- [クラウドサービス](#cloud-service)
- [セキュリティ](#security)
- 再起動
- ログアウト

### スイッチ信号

Comet X は、ローカルまたはリモート制御のために最大 4 台のサーバーに接続できます。接続されている他のすべてのサーバーはスタンバイ モードのままですが、一度に制御できるサーバーは 1 台だけです。

タッチスクリーンまたはKVMコンソールを介して信号ソースをすばやく切り替えることができます。以下は、KVM コンソールで信号ソースを切り替える手順です。

1. 右上隅の **Port** ボタンをクリックします。

2. 対象の信号ソースを選択します。切り替え中は機能が利用できなくなりますのでご注意ください。

    ![switch signal](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/switch-signal.png){class="glboxshadow"}

3. (オプション) 必要に応じてポート名をカスタマイズします。

    ![port edit 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/port-edit1.png){class="glboxshadow"}

    ![port edit 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/port-edit2.png){class="glboxshadow"}

### 折りたたむ

右上隅の上向き矢印アイコンをクリックして、ツールバーを折りたたみます。

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/collapse1.png){class="glboxshadow"}

ツールバーが折りたたまれている場合、上部の下向き矢印アイコンをクリックして展開します。

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/collapse2.png){class="glboxshadow"}

### フルスクリーン

右上隅にある全画面アイコン (四角形) をクリックして、全画面モードに切り替えます。

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/fullscreen1.png){class="glboxshadow"}

全画面表示を終了するには、**Esc** キーを押し続けるか、右上隅にある全画面表示を終了するアイコン (格子状) をクリックします。

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/fullscreen2.png){class="glboxshadow"}

### アップグレード

右上隅にあるファームウェアのバージョンをクリックして、アップデートを確認します。

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/upgrade1.png){class="glboxshadow"}

新しいファームウェアが利用可能な場合は、ポップアップ ウィンドウでオンライン アップグレードを実行できます。または、[ファームウェア ダウンロード センター](https://dl.gl-inet.com/kvm){target="_blank"} から最新のファームウェアをダウンロードし、必要に応じてローカル アップグレードを実行します。

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/upgrade2.png){class="glboxshadow"}

### クラウド サービス

GL.iNet KVM クラウドを使用すると、制御対象のデバイスにリモートからアクセスできます。詳細は[こちら](../../faq/remote_access_via_cloud.md){target="_blank"}をご参照ください。

Comet X がクラウドにバインドされると、コンソールには次のようにクラウドのステータスが表示されます。

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/cloud.png){class="glboxshadow"}

### セキュリティ

セキュリティにより、管理者パスワードの変更、2 要素認証の有効化、TLS 証明書のカスタマイズが可能になります。

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/security.png){class="glboxshadow"}

- Change Admin Password

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/admin-password.png){class="glboxshadow" width="434"}

- 2FA: アカウントを保護するために 2 要素認証を有効にします。

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/2fa.png){class="glboxshadow"}

- TLS Certificate

    システムは、ブラウザー アクセスにプリインストールされたデフォルトの証明書を使用します。 Web ブラウザー アクセス用の TLS 証明書をカスタマイズする場合は、コンソールの右上隅にある **TLS Certificate** をクリックし、**Custom Certificate** を選択して、**証明書ファイルと秘密キー ファイル**をアップロードします。

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/tls-certificate.png){class="glboxshadow"}
