# Comet X (GL-RM4PE) コンソール ガイド

## セッション

コンソールで Session アイコンをクリックし、**Session Settings** を開きます。このページには次の 4 つのセクションがあります。

- [ビデオ](#video)
- [オーディオとカメラ](#audio--camera)
- [キーボード](#keyboard)
- [マウス](#mouse)

### ビデオ {#video}

Session Settings では、表示モード、画質、ビデオ転送方式、画面の向き、EDID などのビデオ設定をカスタマイズできます。

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/session_video.png){class="glboxshadow"}

- **Transfer**: ビデオ転送方式を WebRTC、WebRTC (FEC)、WebRTC (Native)、Direct から選択します。Direct では音声が伝送されません。

    !!! note "WebRTC、WebRTC (FEC)、WebRTC (Native)、Direct の違い"

        - **WebRTC**: リアルタイムのリモート制御に適した、滑らかな映像と安定した音声のバランスを提供します。

        - **WebRTC (FEC)**: 前方誤り訂正により、不安定なネットワーク環境での接続安定性を高めます。少量の冗長データを送信してパケットロスを自動的に補完し、画面のちらつきや遅延を軽減します。

        - **WebRTC (Native)**: Google WebRTC Library を使用し、ストリーミング性能とリアルタイムのリモート制御体験を向上させます。この転送モードはファームウェア v1.10.0 で導入されました。

        - **Direct**: 最小の遅延とロスレスの映像品質を提供しますが、音声伝送には対応しません。

- **Mode**: 必要に応じて Smart と Normal を切り替えます。Smart は、特にネットワーク環境が不安定な場合に、帯域幅の消費を抑えるのに役立ちます。

- **Latency Mode**: Lowest Latency または Smooth Display を選択できます。この機能はファームウェア v1.9.0 で導入されました。

    !!! note "Lowest Latency と Smooth Display の違い"

        - **Lowest Latency**: 入力遅延を最小化し、キーボードとマウスの応答性を高めます。

        - **Smooth Display**: 表示パフォーマンスを最適化し、カクつきやフレーム落ちを抑えて安定した再生を実現します。

- **Quality**: ネットワーク環境と解像度の要件に合わせて、画質を Auto/Low/Medium/High/Ultra-high/Lossless から選択します。

- **FEC Packets**: ネットワークが不安定なときに少量の冗長データを送信し、パケットロスを自動的に補完して画面のちらつきや遅延を軽減します。FEC 比率は 5%/10%/15%/20% から選択できます。

- **Orientation**: コンソールの回転角度を 0°/90°/180°/270° に調整します。

- **EDID**: Extended Display Identification Data の略称で、最適な表示パラメーターを自動的に適用します。

    デフォルト設定はほとんどの利用環境に適しており、通常は変更する必要がありません。詳細は[こちら](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}をご覧ください。EDID 調整後に画面が更新されない場合は、被制御デバイスを再起動してください。

- **View**: ブラウザウィンドウのサイズ変更時に、画面をどのようにスケーリングするかを指定します。Adaptive、Best Picture Quality、Original Pixel から選択できます。この機能はファームウェア v1.8.0 で導入されました。

- **Screen Privacy**: プライバシー画面を有効にすると、HDMI-OUT 接続の外部ディスプレイにコンテンツが表示されなくなり、リモート操作のプライバシーを保護できます。

### オーディオとカメラ {#audio--camera}

被制御デバイスのオーディオとカメラの設定を調整できます。

![Audio_Camera](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/session_audio_camera.png){class="glboxshadow"}

- **Speaker**: 被制御デバイスからの音声出力（システム音や動画の音声など）を制御します。

- **Microphone**: 制御側デバイスのローカル音声（ユーザーの声など）をリモート側に送信します。ワンクリックのミュートと、長押しショートカットでマイクを有効にする Press To Speak に対応しています。

    **Note**: 使用前に [Settings](#usb-devices) でショートカットを手動で設定する必要があります。

- **Camera**: 制御側デバイスでカメラを有効にすると、ローカルの映像フレームがパススルーでリモートホストに送信され、仮想 USB カメラとしてエミュレートされます。リモートホスト上のアプリケーション（会議ツールや FaceTime など）はこの映像を使用でき、物理カメラをリモートホストに直接接続した場合と同様に利用できます。

    **Note**: この機能はファームウェア v1.10.0 で導入され、WebRTC (FEC) モードでのみ使用できます。現在は Web ブラウザーからのみ利用でき、アプリやデスクトップクライアントには対応していません。

### キーボード {#keyboard}

被制御デバイスで使用するキーボードの設定を行えます。

![keyboard image](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/session_keyboard.png){class="glboxshadow"}

- **Bad Link Mode**: キーを直ちに放すモードです。キー操作ごとに 1 回の短い押下と解放として送信し、リモート制御中のキーの固着や意図しない連続入力を防ぎます。

- **Show Virtual Keyboard**: コンソールに仮想キーボードを表示して使用します。

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/session_virtual_keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: Cmd キーと Ctrl キーを入れ替え、異なるオペレーティングシステム間でキーボードの互換性を確保します。

### マウス {#mouse}

被制御デバイスをより快適に操作できるよう、マウス設定を調整できます。

![mouse image](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/session_mouse.png){class="glboxshadow"}

- **Show Local Cursor**: 制御側デバイスのマウスカーソルを画面に表示します。

- **Mouse Jiggle**: 微小なマウス操作を定期的にシミュレートし、リモート会議やサーバー管理などで長時間操作しない場合に、被制御デバイスがスリープ状態に入るのを防ぎます。

- **Scroll Rate**: マウスホイールのスクロール速度または 1 回転あたりのスクロール量を設定し、リモート画面のコンテンツが移動する速さを調整します。

- **Scroll Direction**: マウスホイールを上下にスクロールしたとき、リモート画面のコンテンツを同じ方向（ナチュラルスクロール）または逆方向（従来のスクロール）に移動させるかを設定します。

    Standard、Vertical Invert、Horizontal Invert、Both Invert の 4 つのモードがあります。

- **Mouse Mode**: 絶対マウスと相対マウスを切り替え、リモート制御の用途に応じて滑らかで正確なカーソル操作を実現します。

    !!! note "絶対マウスと相対マウスの違い"

        - **Relative Mode**: マウスの位置を固定画面座標ではなく移動量に基づいて計算します。マウスを操作するにはリモートウィンドウ内をクリックする必要があります。カーソルはリモート画面内にロックされ、画面外へ滑らかに移動できません。BIOS、古いシステム、組み込みデバイスとの互換性に優れています。

        - **Absolute Mode**: マウスの位置が正確な画面座標に対応します。リモートカーソルはローカルカーソルに滑らかで正確に追従し、ローカル画面とリモート画面の間をシームレスに移動できます。ネットワーク転送によりわずかな遅延が生じることはありますが、通常のデスクトップ操作や精密操作に適しています。

        通常の操作を滑らかに行う場合は Absolute、BIOS へのアクセス、絶対座標に対応していない古いデバイス、または意図しないカーソル移動を避ける場合は Relative を使用してください。

- **Relative Sensitivity**: Mouse Mode が Relative の場合に使用できます。

- **Primary Button**: 主ボタンとして左ボタンまたは右ボタンを選択します。この機能はファームウェア v1.9.0 で導入されました。

## ツールボックス

コンソールで **Toolbox** に移動します。ツールボックスページには、次の 5 つのセクションがあります。

- [クリップボード](#clipboard)
- [OCR](#ocr)
- [ショートカット](#shortcut)
- [ウェイク オン ラン](#wake-on-lan)
- [端末](#terminal)

### クリップボード {#clipboard}

クリップボードを使用すると、ファイルを転送することなく、制御側デバイスから被制御デバイスにテキストを簡単に貼り付けることができます。

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_clipboard.png){class="glboxshadow"}

### OCR {#ocr}

OCR はテキスト認識機能です。リモート画面で範囲を選択し、その中のテキストを簡単に抽出できます。この機能はファームウェア v1.9.0 で導入されました。

使用するには、下向き矢印をクリックし、中国語、英語、バイリンガル（Zh/En）などの認識言語を選択します。

![recognition language](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_ocr_language.png){class="glboxshadow"}

次に **Capture** をクリックすると、リモート画面が暗くなります。抽出するテキストを囲むように範囲を指定すると、システムが自動的に認識します。認識したテキストは必要に応じてコピーできます。

![copy text](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_ocr_copy_text.png){class="glboxshadow"}

この機能を使うと、リモート画面（被制御デバイス）からテキストを取得し、ローカルの制御側デバイスにコピーできます。

### ショートカット {#shortcut}

ショートカットを使用すると、仮想キーボードを使用せずにアクションをより速く実行できるため、より効率的に作業し、日常業務の時間を節約できます。ここでいくつかの一般的なショートカットを見つけることができます。

![toolbox-shortcut1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_shortcut_1.png){class="glboxshadow"}

**Modify** をクリックして、必要に応じてショートカット オプションを調整します。

![toolbox-shortcut2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_shortcut_2.png){class="glboxshadow"}

### ウェイク オン ラン {#wake-on-lan}

Wake-on-LAN (WOL) は、被制御デバイスの電源をリモートでオンにしたり、低電力状態から復帰したりできるようにするテクノロジーです。

**Add Device** をクリックし、同じ LAN からデバイスを選択します。

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_wol.png){class="glboxshadow"}

![wol-add-device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_wol_add_devices.png){class="glboxshadow" width=500}

追加したいデバイスがリストにない場合は、**Add Manually** をクリックしてデバイス名と MAC アドレスを入力します。

![wol-add-manually](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox_add_manually.png){class="glboxshadow" width=500}

### ターミナル {#terminal}

Comet Pro のターミナルにアクセスして高度な設定を行えます。**Access** をクリックします。

![toolbox-terminal1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox-terminal_1.png){class="glboxshadow"}

GLKVM ターミナルにリダイレクトされます。

![toolbox-terminal2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbox-terminal_2.png){class="glboxshadow"}

## アクセサリー

GL.iNet は、デバイスの電源オン/オフをリモート制御するためのオプションの KVM アクセサリを提供します。

まず、対応するユーザー ガイドを参照して、アクセサリを被制御デバイスに接続します。 Comet X は同時に 4 つの Fingerbot または ATX ボードに接続できますが、一度に制御できるのは 1 つだけであることに注意してください。

- [フィンガーボット(FGB-01) ユーザーガイド](../gl-fgb-01/index.md){target="_blank"}

- [ATX ボード (GL-ATXPC) ユーザーガイド](../gl-atx-board/index.md){target="_blank"}

2 番目に、KVM コンソールにログインし、**Accessories** に移動します。アクセサリの設定は、アクセサリをインストールした後にのみ使用できます。

### フィンガーボット

Fingerbot は、被制御デバイスの物理的な電源ボタンに貼り付けられ、被制御デバイスの電源の遠隔制御を実現します。

本体の設定に従って動作します。

![accessories fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/accessories_fingerbot.png){class="glboxshadow"}

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

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/virtual_media.png){class="glboxshadow"}

### ファイル共有 {#file-sharing}

Comet X は、読み取り/書き込み USB ドライブをエミュレートできるため、制御側デバイスと制御側デバイスの間でファイルを共有および管理できます。

**制御側デバイスから被制御デバイスにファイルを共有するには、以下の手順に従ってください。**

1. ボックスをドラッグまたはクリックして、制御側デバイスからファイルをアップロードするか、URL からアップロードします。

    アップロードされると、以下のようにファイルが表示されます。

    ![file sharing1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file_sharing_1.png){class="glboxshadow"}

2. 「**Mount To Remote**」→「**File Sharing**」をクリックします。

    ![file sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file_sharing_2.png){class="glboxshadow"}

3. A ウィンドウがコンソールにポップアップ表示され、ファイル共有の手順が示されます。

    ![file sharing3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file_sharing_3.png){class="glboxshadow"}

4. 少し待つと、**"GLKVM"** という名前のドライブが画面に自動的に表示されます。以前に制御側デバイスから Comet X にアップロードしたファイルが、制御側デバイスに共有されていることがわかります。これで、被制御デバイス上のこのドライブ内のファイルを表示、移動、または削除できるようになります。

    ![file sharing4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file_sharing_4.png){class="glboxshadow"}

    **Tips**: ドライブが自動的にポップアップしない場合は、被制御デバイスの **This PC** に移動します。

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/this_pc.png){class="glboxshadow"}

    次に、**GLKVM** という名前のドライブを見つけます。これで、このドライブ内のファイルを表示、移動、または削除できるようになります。

5. 共有を停止する場合は、ツールバーの **Virtual Media** をクリックし、**Stop Sharing** をクリックします。

    ![stop sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/stop_sharing_1.png){class="glboxshadow"}

**被制御デバイスから制御側デバイスにファイルを共有するには、以下の手順に従ってください。**

1. 被制御デバイスで、共有するファイルをドライブ **GLKVM** に移動またはコピーします。

    たとえば、「gl-rm10_datasheet」という名前のイメージが、被制御デバイスのデスクトップからドライブ **GLKVM** に移動されました。

    ![file sharing5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file_sharing_5.png){class="glboxshadow"}

2. Comet X のコンソールに移動し、ツールバーの **Virtual Media** をクリックして、**Stop Sharing** をクリックします。

    ![stop sharing2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/stop_sharing_2.png){class="glboxshadow"}

3. このファイルは、次に示すように、**Virtual Media** の下に表示されます。これで、このファイルを Comet X から制御側デバイスにダウンロードできるようになります。

    ![file sharing6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/file_sharing_6.png){class="glboxshadow"}

### イメージのマウント {#image-mounting}

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

### ディスクのフォーマット {#format-disk}

ワンクリックでディスクをフォーマットしたり、仮想メディアを無効にしたりできます。

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/format_disk.png){class="glboxshadow"}

- **Format**: ディスク上のすべてのデータを消去し、ファイル システム構造を再初期化します。

- **Disable**: 仮想メディアを無効にすると、KVM デバイスがすぐに再起動されます。

## アプリ センター

コンソールで、**Apps Center**に移動します。統合されたアプリケーションはここにあります。

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/app_center.png){class="glboxshadow"}

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

### NetBird

[NetBird](https://netbird.io/){target="_blank"} は、家庭や企業向けの安全なプライベートネットワークを構築できる、オープンソースのゼロトラストネットワーキングプラットフォームです。WireGuard® ベースのオーバーレイネットワークにより、いつでもどこからでもデバイスに安全にアクセスできます。

Comet X は NetBird と統合されており、NetBird 仮想ネットワーク経由でリモートアクセスできます。詳細は[こちら](../../faq/remote_access_via_netbird.md){target="_blank"}をご覧ください。

バインド後、コンソールに NetBird 仮想 IP が表示されます。

![netbird enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/apps-netbird-enabled.png){class="glboxshadow"}

## ヘルプ

コンソールで、**Help**に移動します。ここでは、GL.iNet KVM に関する詳細情報とヘルプ ドキュメント、およびトラブルシューティング用のログをエクスポートできます。

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/help.png){class="glboxshadow"}

## ツールバー

コンソールの右上には、次のツールがあります。

- [スイッチ信号](#switch-signal)
- [ツールバーを折りたたむ](#collapse)
- [フルスクリーン](#fullscreen)
- [アップグレード](#upgrade)
- [接続統計](#connection-stats)
- [クラウドサービス](#cloud-service)
- [ログアウト](#logout)

### スイッチ信号 {#switch-signal}

Comet X は、ローカルまたはリモート制御のために最大 4 台のサーバーに接続できます。接続されている他のすべてのサーバーはスタンバイ モードのままですが、一度に制御できるサーバーは 1 台だけです。

タッチスクリーンまたはKVMコンソールを介して信号ソースをすばやく切り替えることができます。以下は、KVM コンソールで信号ソースを切り替える手順です。

1. 右上隅の **Port** ボタンをクリックします。

2. 対象の信号ソースを選択します。切り替え中は機能が利用できなくなりますのでご注意ください。

    ![switch signal](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/switch-signal.png){class="glboxshadow"}

3. (オプション) 必要に応じてポート名をカスタマイズします。

    ![port edit 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/port_edit1.png){class="glboxshadow"}

    ![port edit 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/port_edit2.png){class="glboxshadow" width=500}

### 折りたたむ {#collapse}

右上隅の上向き矢印アイコンをクリックして、ツールバーを折りたたみます。

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_collapse_1.png){class="glboxshadow"}

ツールバーが折りたたまれている場合、上部の下向き矢印アイコンをクリックして展開します。

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_collapse_2.png){class="glboxshadow"}

### フルスクリーン {#fullscreen}

右上隅にある全画面アイコン (四角形) をクリックして、全画面モードに切り替えます。

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_fullscreen_1.png){class="glboxshadow"}

全画面表示を終了するには、**Esc** キーを押し続けるか、右上隅にある全画面表示を終了するアイコン (格子状) をクリックします。

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_fullscreen_2.png){class="glboxshadow"}

### アップグレード {#upgrade}

右上隅にあるファームウェアのバージョンをクリックして、アップデートを確認します。

![firmware upgrade 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_upgrade_1.png){class="glboxshadow"}

ポップアップウィンドウで **Local Upgrade** をクリックし、ファームウェアファイルをアップロードできます。

![firmware upgrade 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_upgrade_2.png){class="glboxshadow"}

![firmware upgrade 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_upgrade_3.png){class="glboxshadow" width=350}

ローカルアップグレードを実行する前に、[ファームウェアダウンロードセンター](https://dl.gl-inet.com/kvm){target="_blank"} から最新のファームウェアをダウンロードしてください。

### 接続統計 {#connection-stats}

Connection Stats には、遅延、ジッター、その他のリアルタイムメトリクスを監視する Data Dashboard があります。

List アイコンをクリックすると、デバイスの状態とリアルタイムデータが表示されます。

![data dashboard 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/data_dashboard_1.png){class="glboxshadow"}

チャートアイコンをクリックすると、ネットワーク遅延、ネットワークジッター、パケットロス率、リアルタイムフレームレート、再生遅延などの統計データを確認できます。

![data dashboard 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/data_dashboard_2.png){class="glboxshadow"}

### クラウドサービス {#cloud-service}

GL.iNet KVM クラウドを使用すると、制御対象のデバイスにリモートからアクセスできます。詳細は[こちら](../../faq/remote_access_via_cloud.md){target="_blank"}をご参照ください。

Comet Pro をクラウドにバインドすると、コンソールにクラウドのステータスが次のように表示されます。

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_cloud_service.png){class="glboxshadow"}

### ログアウト {#logout}

ログアウトするには、Logout アイコンをクリックします。

![layout](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/toolbar_layout.png){class="glboxshadow"}

## 設定

コンソールでナビゲーションバーの Settings アイコンをクリックすると、次の Settings ページが開きます。この機能はファームウェア v1.10.0 で導入されました。

- [USB デバイス](#usb-devices)
- [環境設定](#preferences)
- [ネットワーク](#network)
- [セキュリティ](#security)
- [クラウド](#cloud)
- [システム](#system)

![Settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings.png){class="glboxshadow"}

### USB デバイス {#usb-devices}

USB Devices ページでは、すべての USB エミュレーションデバイスを一元管理できます。このページから仮想周辺機器のオンとオフを切り替え、被制御ホストとの互換性を高めることができます。

![USB Emulated Devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_usb_devices.png){class="glboxshadow"}

- **Microphone**

    マイクがミュートのときに Settings をクリックすると、利用方法に合わせてショートカットをカスタマイズできます。割り当てたショートカットキーを押し続けると音声の送信が開始され、放すと再びミュートになります。

    ![mic settings 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_microphone_1.png){class="glboxshadow" width=600}

    ![mic settings 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_microphone_2.png){class="glboxshadow" width=434}

  - **Device Identity**

    被制御デバイスによって認識される KVM のデバイス ID をカスタマイズまたは変更できます。EDID とデバイス ID は同期されます。いずれかを変更するともう一方も自動的に更新され、デバイスが正しく認識されるようになります。

    ![Device Identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_device_identity.png){class="glboxshadow" width=350}

### 環境設定 {#preferences}

Preferences では、Layout Preferences、System Settings、Device Screen を管理できます。

![Preferences](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences**: 全画面モードでのツールバー表示と、ウィンドウモードでのステータスバー表示を必要に応じて設定できます。

- **System Settings**: ブラウザーの Tab Title、Language（Chinese、English、Japanese）、Color Mode（Light または Dark）、地域に合わせた Timezone を選択できます。

- **Device Screen**: デバイス画面を管理およびプレビューできます。Lock Screen モード（World Clock、Clock Only、Wallpaper Only）、Time Format、Date Format、Wallpaper を設定できます。

### ネットワーク {#network}

Comet Pro のホスト名や IP アドレスなどのネットワーク情報を確認、変更できます。

![network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_network.png){class="glboxshadow"}

- **Hostname**: デバイスのホスト名をコンソール上で直接変更できます。この機能はファームウェア v1.7.0 で導入されました。

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_network_hostname.png){class="glboxshadow" width=600}

- **Ethernet Settings**: Comet Pro が Ethernet ケーブルで上流のネットワークデバイスに接続されると、ここに Ethernet の情報が表示されます。

    プロトコルが DHCP の場合、ページは次のように表示されます。

    ![ethernet dhcp](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_network_dhcp.png){class="glboxshadow" width=600}

    静的 IP アドレスを設定するには、プロトコルを **Static** に切り替え、必要なネットワークパラメーター（IP アドレス、ネットマスク、ゲートウェイなど）を入力します。

    ![ethernet static](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_network_static.png){class="glboxshadow" width=600}

### セキュリティ {#security}

セキュリティにより、管理者パスワードの変更、2 要素認証の有効化、TLS 証明書のカスタマイズが可能になります。

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/setting_security.png){class="glboxshadow"}

- Change Admin Password

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_change_password.png){class="glboxshadow" width="434"}

- 2FA: アカウントを保護するために 2 要素認証を有効にします。

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_security_2fa.png){class="glboxshadow"}

- TLS Certificate

    システムは、ブラウザーアクセスにプリインストール済みのデフォルト証明書を使用します。Web ブラウザーアクセス用の TLS 証明書をカスタマイズする場合は、TLS Certificate の **Custom** をクリックし、**証明書ファイルと秘密鍵ファイル**をアップロードします。

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_tls_certificate.png){class="glboxshadow" width=600}

### クラウド {#cloud}

Cloud では、クラウドサービスを通じてデバイスにリモートアクセスし、管理できます。

URL 経由でデバイスをクラウドにバインドできます。**More Settings** には Bind With Code、App Download、Disable などのオプションがあります。

![Cloud 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_cloud_1.png){class="glboxshadow"}

バインドが完了すると、バインド済みのクラウドアカウント情報を確認できます。**Access Cloud** をクリックして Devices を管理するか、**More Settings** をクリックして必要に応じて無効化またはバインド解除できます。

![Cloud 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/settings_cloud_2.png){class="glboxshadow"}

同じ管理操作は、上部ツールバーの Cloud Service からも実行できます。

### システム {#system}

System 設定では、次の設定を行えます。

![system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/setting_system.png){class="glboxshadow"}

- **System**: **Reboot** をクリックするとデバイスが再起動します。**Reset** をクリックすると現在のデバイス設定が消去され、再セットアップできます。

- **Upgrade**: Beta Center を有効にしてベータ版ファームウェアの更新を受け取るか、Local Upgrade を使用してローカルファイルから手動でインストールできます。

    ![local Upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/console/setthing_system_local_update.png){class="glboxshadow" width=400}

- **Help & Support**: Export Log Files では、トラブルシューティングやアフターサービスに使用するデバイスの実行ログを保存できます。Help Document からは、ユーザーガイド、FAQ、トラブルシューティングドキュメントにアクセスできます。
