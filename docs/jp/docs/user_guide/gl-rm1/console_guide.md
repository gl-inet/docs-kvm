# Comet (GL-RM1) V1/V2 コンソール ガイド

## 設定

コンソールで、**Settings**に移動します。設定ページには 4 つのセクションが含まれています。 

- [ビデオ](#video)
- [リモートデバイス設定](#remote-device-settings)
- [システム](#system)
- [ネットワーク](#network)

### クイック検索

[設定] ページの上部にキーワードを入力すると、必要な設定をすぐに見つけることができます。

![quick search](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/quick-search.png){class="glboxshadow"}

### ビデオ

表示モード、ビデオ品質、ビデオ送信、画面の向き、EDID など、本体のビデオ設定をカスタマイズできます。

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/settings-video.png){class="glboxshadow"}

- **Mode**: 必要に応じてスマート モードとノーマル モードを切り替えます。スマート モードは、特に弱いネットワークでの帯域幅の消費を削減するのに役立ちます。

- **Latency Mode**: デバイスの「最低遅延」と「スムーズ表示」のどちらかを選択できます。この機能はファームウェア v1.9.0 で導入されました。

    !!! note "最小遅延とスムーズ表示の違いは何ですか?"

        - **Lowest Latency**: 入力遅延を最小限に抑え、キーボードとマウスのよりきびきびした応答を実現します。

        - **Smooth Display**: 視覚パフォーマンスを最適化し、途切れやフレーム損失を排除し、安定した再生を実現します。

- **Quality**: ネットワーク環境と解像度要件に応じて、ビデオ品質を自動/低/中/高/超高/ロスレスに調整します。

- **Transfer**: 必要に応じて、ビデオ送信方法を WebRTC、WebRTC (FEC)、およびダイレクトの間で切り替えます。ダイレクト転送では音が出ませんのでご注意ください。

    !!! note "WebRTC、WebRTC (FEC) とダイレクトの違いは何ですか?"

        - **WebRTC**: リアルタイム リモート コントロールのために、滑らかなビデオと安定したオーディオのバランスをとります。
        
        - **WebRTC (FEC)**: 前方誤り訂正を追加して、貧弱なまたは不安定なネットワーク条件下での接続の安定性を向上させます。選択すると、少量の冗長データを送信することで失われたデータ パケットが自動的に修復され、画面のちらつきや遅延が軽減されます。
        
        - **Direct**: 最低の遅延とロスレスビデオ品質を提供しますが、オーディオ送信はサポートしていません。

- **Orientation**: コンソールの回転角度を 0°/90°/180°/270° に調整します。

- **EDID**: Extended Display Identification Data の略で、最適な表示パラメータに自動的に一致します。

    デフォルト設定はほとんどのシナリオに適用され、通常は変更する必要はありません。詳細は[こちら](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}をご参照ください。 EDID 調整後に画面が更新されない場合は、被制御デバイスを再起動してください。

- **View**: この設定は、ブラウザ ウィンドウのサイズを変更するときの画面のスケーリングを決定します。利用可能なオプション: アダプティブ、最高画質、オリジナル ピクセル。この機能はファームウェア v1.8.0 で導入されました。

### リモートデバイスの設定

被制御デバイスの関連設定を調整できます。

![settings-remote device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/settings-remote-device.png){class="glboxshadow"}

- **Speaker**: 被制御デバイスからのオーディオ出力を制御します (システム サウンド、ビデオ オーディオなど)。

- **Microphone**: ローカル オーディオ (ユーザーの声など) を制御側デバイスからリモート エンドに送信します。ワンクリックのミュート、およびマイクをアクティブにするための長押しショートカット (つまり、Press To Speak) をサポートしています。

    ![mic settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/mic-settings.png){class="glboxshadow"}

    ![press to speak](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/press-to-speak.png){class="glboxshadow"}

- **Keyboard**: 被制御デバイスのキーボードをオンまたはオフにします。

- **Bad Link Mode**: つまり、すぐにキーを放します。各キーの押下は 1 回の素早い押して放す動作として送信され、リモート制御中のキーの固着や意図しない繰り返し入力を防ぎます。

- **Show Virtual Keyboard**: コンソールに仮想キーボードを表示して使用します。

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/show-virtual-keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: この機能は、Cmd キーと Ctrl キーを交換して、さまざまなオペレーティング システム間でキーボードの互換性を確保します。

- **Mouse**: 被制御デバイスのマウスをオンまたはオフにします。

- **Show Local Cursor**: 制御側デバイスのマウスを画面上に表示します。

- **Mouse Jiggle**: マウス ジグル機能は、微妙な周期的なマウスの動きをシミュレートし、リモート会議やサーバー管理中など、長時間非アクティブな状態が続いて被制御デバイスがスリープ状態になるのを防ぎます。

- **Scroll Rate**: マウス ホイールのスクロール速度、またはホイール 1 回転ごとにスクロールされる行/単位数を指し、リモコン上でコンテンツが移動する速度に影響します。

- **Scroll Direction**: マウス ホイールを上下にスクロールすると、リモート画面上のコンテンツが同じ方向 (自然スクロール) に移動するか、逆方向 (従来のスクロール) に移動するかを決定します。 

    標準、垂直反転、水平反転、両反転の 4 つの方向モードが利用可能です。  

- **Mouse Mode**: 絶対モードと相対モードを切り替えて、さまざまなリモート コントロール シナリオでスムーズかつ正確なカーソル制御を保証します。

    !!! note "絶対モードと相対モードの違いは何ですか?"

        - **Relative Mode**: マウスの位置は、固定された画面座標ではなく動きに基づいて計算されます。マウスを制御するには、リモート ウィンドウ内をクリックする必要があります。カーソルがリモート画面内でロックされ、スムーズに移動できません。このモードでは、BIOS、古いシステム、および組み込みデバイスとの互換性が向上します。

        - **Absolute Mode**: マウスの位置は正確な画面座標に対応します。リモート カーソルはローカル カーソルをスムーズかつ正確に追従するため、ローカル画面とリモート画面の間でシームレスに移動できます。ネットワーク伝送により若干の遅延が発生する場合がありますが、日常のデスクトップ制御や正確な操作に最適です。

        つまり、日々の制御をスムーズに行うには、Absolute を使用します。 BIOS アクセス、絶対位置をサポートしていない一部の古いデバイス、または誤ったカーソルの移動を避けるために相対を使用します。

- **Relative Sensitivity**: マウス モードが相対の場合に使用できます。

- **Primary Button**: プライマリ クリックとして左ボタンまたは右ボタンを選択します。この機能はファームウェア v1.9.0 で導入されました。

### システム

コンソールのシステム表示設定をカスタマイズしたり、ワンクリックでデバイスをリセットしたりできます。

![settings-system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/settings-system.png){class="glboxshadow"}

- **Device Identity**: 被制御デバイスによって認識される KVM の ID をカスタマイズまたは変更します。 EDID とデバイス ID は同期されたままであることに注意してください。どちらかを変更すると、もう一方も自動的に更新され、デバイスが正しく認識されるようになります。

    ![device identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/device-identity.png){class="glboxshadow"}

- **Language**: コンソールの言語を中国語、英語、または日本語に設定します。

- **Color Mode**: テーマの色をライト モードまたはダーク モードにカスタマイズします。

- **Time Zone**: KVM コンソールのタイムゾーンをカスタマイズします。 

- **Reset KVM**: ワンクリックで KVM を出荷時設定にリセットします。

### ネットワーク

ここで、ホスト名やIPアドレスなど、Cometのネットワークの詳細を確認できます。

![settings-network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/settings-network.png){class="glboxshadow"}

- **Hostname**: デバイスのホスト名はコンソールで直接変更できます。この機能はファームウェア v1.7.0 で導入されました。

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/modify-hostname.png){class="glboxshadow"}

- **Ethernet**: Comet がイーサネット ケーブル経由で上流のネットワーク デバイスに接続すると、そのイーサネット IP アドレスがここに表示されます。 IP アドレスまたは右矢印をクリックすると、イーサネットの詳細が表示されます。

    プロトコルが DHCP の場合、ページは次のように表示されます。

    ![ethernet dhcp](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/eth-dhcp.png){class="glboxshadow"}
    
    静的 IP アドレスを設定する場合は、プロトコルを **Static** に切り替え、必要なネットワーク パラメーター (IP アドレス、ネットマスク、ゲートウェイなど) をそれに応じて入力します。

    ![ethernet static](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/eth-static.png){class="glboxshadow"}

## ツールボックス

コンソールで、**Toolbox**に移動します。ツールボックス ページには、次の 4 つのセクションが含まれています。 

- [クリップボード](#clipboard)
- [ショートカット](#shortcut)
- [ウェイク オン ラン](#wake-on-lan)
- [端末](#terminal)

### クリップボード

クリップボードを使用すると、ファイルを転送することなく、制御側デバイスから被制御デバイスにテキストを簡単に貼り付けることができます。

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-clipboard.png){class="glboxshadow"}

### ショートカット

ショートカットを使用すると、仮想キーボードを使用せずにアクションをより速く実行できるため、より効率的に作業し、日常業務の時間を節約できます。ここでいくつかの一般的なショートカットを見つけることができます。

![toolbox-shortcut](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-shortcut1.png){class="glboxshadow"}

**Modify** をクリックして、必要に応じてショートカット オプションを調整します。

![toolbox-shortcut-modify](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-shortcut2.png){class="glboxshadow"}  

### ウェイク オン ラン

Wake-on-LAN (WOL) は、被制御デバイスの電源をリモートでオンにしたり、低電力状態から復帰したりできるようにするテクノロジーです。

**Add Device** をクリックして、同じ LAN からデバイスを選択します。

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-wol.png){class="glboxshadow"}

![wol add device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/wol-add-device.png){class="glboxshadow"}

追加したいデバイスがリストにない場合は、**Add Manually** をクリックし、デバイス名と MAC アドレスを入力します。

![wol add manually](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/wol-add-manually.png){class="glboxshadow"}

### ターミナル

Comet の端末にアクセスして詳細設定を行うことができます。 「**Access**」をクリックします。

![toolbox-terminal-1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-terminal1.png){class="glboxshadow"}

GLKVM ターミナルにリダイレクトされます。

![toolbox-terminal-2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/toolbox-terminal2.png){class="glboxshadow"}

## アクセサリー

GL.iNet は、デバイスの電源オン/オフをリモート制御するためのオプションの KVM アクセサリを提供します。 

まず、アクセサリを被制御デバイスに接続するための対応するユーザー ガイドを参照してください。

- [フィンガーボット(FGB-01) ユーザーガイド](../gl-fgb-01/index.md){target="_blank"}

- [ATX ボード (GL-ATXPC) ユーザーガイド](../gl-atx-board/index.md){target="_blank"}

2 番目に、KVM コンソールにログインし、**Accessories** に移動します。アクセサリの設定は、アクセサリをインストールした後にのみ使用できます。

### フィンガーボット
    
Fingerbot は、被制御デバイスの物理的な電源ボタンに貼り付けられ、被制御デバイスの電源の遠隔制御を実現します。
    
本体の設定に従って動作します。

![accessories fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/fingerbot.png){class="glboxshadow"}

- **Time**: フィンガーボットの押し続ける時間。 0.5秒/3秒/8秒に設定できます。

- **Strength**:押す強さは軽く押す、強く押すの2段階あります。

    - **Lightly Press**: 短いボタンまたはソフトタッチのボタンに最適です。
    
    - **Firmly Press**: 深いボタンや硬いボタンに最適です。

    ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### ATX 電源

ATX ボードはコンピューター ケースに取り付けられており、デバイスの電源オン/オフ/再起動をリモートで制御します。

本体の設定に従って動作します。

![accessories atxpower](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/atx-board.png){class="glboxshadow"}

- **電源 (短く押す)**: 通常の電源投入またはシステムのウェイクアップに使用されます。

- **電源 (長押し)**: 強制シャットダウン操作を実行します。

- **Restart**: デバイスを再起動します。

## 仮想メディア

コンソールで、**Virtual Media**に移動します。ここでは次の操作を実行できます。

- [ファイルを共有](#file-sharing)
- [マウント画像](#image-mounting)
- [ストレージドライブの交換](#replace-storage-drive)
- [ディスクのフォーマット](#format-disk)

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/virtual-media.png){class="glboxshadow"}
    
### ファイル共有

Comet は、読み取り/書き込み USB ドライブをエミュレートできるため、制御側デバイスと制御側デバイスの間でファイルを共有および管理できます。

**制御側デバイスから被制御デバイスにファイルを共有するには、以下の手順に従ってください。**

1. ボックスをドラッグまたはクリックして、制御側デバイスからファイルをアップロードするか、URL からアップロードします。 

    アップロードされると、以下のようにファイルが表示されます。

    ![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing1.png){class="glboxshadow"}

2. 「**Mount To Remote**」→「**File Sharing**」をクリックします。

    ![file sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing2.png){class="glboxshadow"}
以下に示すように、

3. A ウィンドウがコンソールにポップアップ表示され、ファイル共有手順が示されます。
    
    ![file sharing tips](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing3.png){class="glboxshadow"}

4. 少し待つと、**"GLKVM"** という名前のドライブが画面に自動的に表示されます。以前に制御側デバイスから Comet にアップロードしたファイルが、制御側デバイスに共有されていることがわかります。これで、被制御デバイス上のこのドライブ内のファイルを表示、移動、または削除できるようになります。

    ![glkvm disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing4.png){class="glboxshadow"}

    **Tips**: ドライブが自動的にポップアップしない場合は、被制御デバイスの **This PC** に移動します。 

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/thispc.png){class="glboxshadow"}
    
    次に、**GLKVM** という名前のドライブを見つけます。これで、このドライブ内のファイルを表示、移動、または削除できるようになります。

5. 共有を停止する場合は、ツールバーの **Virtual Media** をクリックし、**Stop Sharing** をクリックします。

    ![stop sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/stop-sharing1.png){class="glboxshadow"}

**被制御デバイスから制御側デバイスにファイルを共有するには、以下の手順に従ってください。**

1. 被制御デバイスで、共有するファイルをドライブ **GLKVM** に移動またはコピーします。

    たとえば、「slate7pro_datasheet」という名前の PDF ファイルが、被制御デバイスのデスクトップからディスク **GLKVM** にコピーされています。 

    ![move file to disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing5.png){class="glboxshadow"}
    
2. Comet のコンソールに移動し、ツールバーの **Virtual Media** をクリックして、**Stop Sharing** をクリックします。

    ![stop sharing 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/stop-sharing2.png){class="glboxshadow"}
    
3. このファイルは、次に示すように、**Virtual Media** の下に表示されます。これで、このファイルを Comet から制御側デバイスにダウンロードできます。

    ![file shared](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/file-sharing6.png){class="glboxshadow"}

### イメージのマウント

Comet は、被制御デバイス上の読み取り専用の仮想 CD/DVD またはディスク ドライブをシミュレートできます。このドライブには、BIOS または UEFI の起動プロセス中にアクセスできます。 
    
この機能は、オペレーティング システムを再インストールしたり、ISO をマウントして制御対象のデバイスにアプリケーションをインストールしたり、その他のタスクを実行したりするのに役立ちます。
    
1. ボックスをドラッグまたはクリックしてファイルをアップロードします。 **このファイルが ISO 形式としてマウントできることを確認してください**。

    アップロードされると、以下のようにファイルが表示されます。

    ![image mounting 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting1.png){class="glboxshadow"}
    
2. 「**Mount To Remote**」→「**Image Mounting**」をクリックします。 

    ![image mounting 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting2.png){class="glboxshadow"}

3. ポップアップ ウィンドウでファイルを選択し、**Mount Image** をクリックします。

    ![image mounting 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting3.png){class="glboxshadow"}
以下に示すように、

4. A ウィンドウがコンソールにポップアップ表示され、取り付け手順が示されます。

    ![image mounting 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting4.png){class="glboxshadow"}

5. これで、被制御デバイスの CD ドライブからこのファイルを使用できるようになります。

    ![image mounting 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/image-mounting5.png){class="glboxshadow"}

### ストレージ ドライブを交換する

USB ストレージ デバイスを KVM USB ポートに挿入して、内部ストレージを置き換えることができます。

![replace storage drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/replace-storage.png){class="glboxshadow"}

### ディスクをフォーマットします

ワンクリックでディスクをフォーマットしたり、仮想メディアを無効にしたりできます。

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/format-disable.png){class="glboxshadow"}

- **Format**: ディスク上のすべてのデータを消去し、ファイル システム構造を再初期化します。

- **Disable**: 仮想メディアを無効にすると、KVM デバイスがすぐに再起動されます。 

## アプリ センター

コンソールで、**Apps Center**に移動します。統合されたアプリケーションはここにあります。

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/apps-center.png){class="glboxshadow"}

### Tailscale

[Tailscale](https://tailscale.com/){target="_blank"} は、ポート転送や複雑なファイアウォール設定を行わずに、デバイス間で暗号化されたピアツーピア プライベート ネットワークを構築する WireGuard ベースのメッシュ VPN サービスです。

Comet は Tailscale と統合されており、Tailscale 仮想ネットワーク経由でリモート アクセスできるようになります。

Comet と制御側デバイスを同じ Tailscale アカウントにバインドするだけで、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **Tailscale 仮想 IP** を入力することで、Comet にリモート アクセスできます。詳細は[こちら](../../faq/remote_access_via_tailscale.md){target="_blank"}をご覧ください。

バインド後、コンソールにはリンクされた Tailscale アカウントが表示され、出口ノードやサブネット ルートなどの高度な機能のロックが解除されます。

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier

[ZeroTier](https://www.zerotier.com/){target="_blank"} は、暗号化されたオーバーレイ仮想ネットワークを作成し、分散したデバイスをあたかも同じローカル エリア ネットワーク内にあるかのようにグローバルに接続します。

Comet は ZeroTier と統合されており、ZeroTier 仮想ネットワーク経由でリモート アクセスできるようになります。

Comet と制御側デバイスを同じ ZeroTier ネットワークに参加させるだけで、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **ZeroTier IP** を入力することで、Comet にリモート アクセスできます。詳細は[こちら](../../faq/remote_access_via_zerotier.md){target="_blank"}をご参照ください。

バインド後、コンソールには ZeroTier ネットワーク ID と仮想 IP が表示されます。

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/apps-zerotier-enabled.png){class="glboxshadow"}

### NetBird

[NetBird](https://netbird.io/){target="_blank"} は、家庭用およびビジネス用の安全なプライベート ネットワークを構築できるオープンソースのゼロトラスト ネットワーキング プラットフォームです。 WireGuard® ベースのオーバーレイ ネットワークとして、NetBird は、いつでもどこでもデバイスへの安全なアクセスを可能にします。

Comet は NetBird と統合され、NetBird 仮想ネットワーク経由でリモート アクセスできるようになります。詳細は[こちら](../../faq/remote_access_via_netbird.md){target="_blank"}をご参照ください。

バインド後、コンソールには NetBird 仮想 IP が表示されます。

![netbird enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/apps-netbird-enabled.png){class="glboxshadow"}

## ヘルプ

コンソールで、**Help**に移動します。ここでは、GL.iNet KVM に関する詳細情報とヘルプ ドキュメント、およびトラブルシューティング用のログをエクスポートできます。

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/help.png){class="glboxshadow"}

## ツールバー

コンソールで、右上隅に移動して次のツールにアクセスします。

- [テキスト認識](#text-recognition)
- [ツールバーを折りたたむ](#collapse)
- [フルスクリーン](#fullscreen)
- [アップグレード](#upgrade)
- [クラウドサービス](#cloud-service)
- [セキュリティ](#security)
- 再起動
- ログアウト

### テキスト認識

テキスト認識機能を使用すると、リモート画面上の領域を選択し、そこからテキストを簡単に抽出できます。これは光学式文字認識 (OCR) テクノロジーを搭載しており、ファームウェア v1.9.0 で導入されました。

これを使用するには、下向き矢印をクリックして、中国語、英語、バイリンガル (Zh/En) などの優先認識言語を選択します。

![recognition language](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/ocr_function.png){class="glboxshadow"}

次に、「T」アイコンをクリックすると、リモート画面が暗くなります。抽出したいテキストの周りにボックスを描くと、システムが自動的にそれを識別します。必要に応じて、認識されたテキストをコピーできます。

この機能を使用すると、リモート画面 (つまり、被制御デバイス) からテキストを簡単にキャプチャし、それを制御側デバイスにコピーして使用できます。

### 折りたたむ

右上隅の上向き矢印アイコンをクリックして、ツールバーを折りたたみます。

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/collapse1.png){class="glboxshadow"}

ツールバーが折りたたまれている場合、上部の下向き矢印アイコンをクリックして展開します。

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/collapse2.png){class="glboxshadow"}

### フルスクリーン

右上隅にある全画面アイコン (四角形) をクリックして、全画面モードに切り替えます。

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/fullscreen1.png){class="glboxshadow"}

全画面表示を終了するには、**Esc** キーを押し続けるか、右上隅にある全画面表示を終了するアイコン (格子状) をクリックします。 

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/fullscreen2.png){class="glboxshadow"}

### アップグレード

右上隅にあるファームウェアのバージョンをクリックして、アップデートを確認します。

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/upgrade1.png){class="glboxshadow"}

ポップアップ ウィンドウで **Update Settings** をクリックして、ローカル アップグレードを実行したり、ベータ プログラムに参加したり、現在の構成を保存したりできます。

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/upgrade2.png){class="glboxshadow"}

ローカル アップグレードを実行する前に、[ファームウェア ダウンロード センター](https://dl.gl-inet.com/kvm){target="_blank"} から最新のファームウェアをダウンロードしてください。

### クラウド サービス

GL.iNet KVM クラウドを使用すると、制御対象のデバイスにリモートからアクセスできます。詳細は[こちら](../../faq/remote_access_via_cloud.md){target="_blank"}をご参照ください。

Comet がクラウドにバインドされると、コンソールには次のようにクラウドのステータスが表示されます。

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/cloud.png){class="glboxshadow"}

### セキュリティ

セキュリティにより、管理者パスワードの変更、2 要素認証の有効化、TLS 証明書のカスタマイズが可能になります。 

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/security.png){class="glboxshadow"}

- 管理者パスワードを変更します。

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/admin-password.png){class="glboxshadow" width="434"}

- 2FA: アカウントを保護するために 2 要素認証を有効にします。

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/2fa.png){class="glboxshadow"}

- TLS 証明書

    システムは、ブラウザー アクセスにプリインストールされたデフォルトの証明書を使用します。 Web ブラウザー アクセス用の TLS 証明書をカスタマイズする場合は、コンソールの右上隅にある **TLS Certificate** をクリックし、**Custom Certificate** を選択して、**証明書ファイルと秘密キー ファイル**をアップロードします。

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/console/tls-certificate.png){class="glboxshadow"}
