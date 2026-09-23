# Comet PoE (GL-RM1PE) コンソール ガイド

## セッション

コンソールで Session アイコンをクリックし、**Session Settings** を開きます。このページには次の 4 つのセクションがあります。

- [ビデオ](#video)
- [オーディオとカメラ](#audio--camera)
- [キーボード](#keyboard)
- [マウス](#mouse)

### ビデオ {#video}

Session Settings では、表示モード、画質、ビデオ転送方式、画面の向き、EDID などのビデオ設定をカスタマイズできます。

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/session_video.png){class="glboxshadow"}

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

### オーディオとカメラ {#audio--camera}

被制御デバイスのオーディオとカメラの設定を調整できます。

![Audio_Camera](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/session_audio_camera.png){class="glboxshadow"}

- **Speaker**: 被制御デバイスからの音声出力（システム音や動画の音声など）を制御します。

- **Microphone**: 制御側デバイスのローカル音声（ユーザーの声など）をリモート側に送信します。ワンクリックのミュートと、長押しショートカットでマイクを有効にする Press To Speak に対応しています。

    **注**: 使用前に [Settings](#usb-devices) でショートカットを手動で設定する必要があります。

- **Camera**: 制御側デバイスでカメラを有効にすると、ローカルの映像フレームがパススルーでリモートホストに送信され、仮想 USB カメラとしてエミュレートされます。リモートホスト上のアプリケーション（会議ツールや FaceTime など）はこの映像を使用でき、物理カメラをリモートホストに直接接続した場合と同様に利用できます。

    **Note**: この機能はファームウェア v1.10.0 で導入され、WebRTC (FEC) モードでのみ使用できます。現在は Web ブラウザーからのみ利用でき、アプリやデスクトップクライアントには対応していません。

### キーボード {#keyboard}

被制御デバイスで使用するキーボードの設定を行えます。

![keyboard image](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/session_keyboard.png){class="glboxshadow"}

- **Bad Link Mode**: キーを直ちに放すモードです。キー操作ごとに 1 回の短い押下と解放として送信し、リモート制御中のキーの固着や意図しない連続入力を防ぎます。

- **Show Virtual Keyboard**: コンソールに仮想キーボードを表示して使用します。

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/session_virtual_keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: Cmd キーと Ctrl キーを入れ替え、異なるオペレーティングシステム間でキーボードの互換性を確保します。

### マウス {#mouse}

被制御デバイスをより快適に操作できるよう、マウス設定を調整できます。

![mouse image](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/session_mouse.png){class="glboxshadow"}

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

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_clipboard.png){class="glboxshadow"}

### OCR {#ocr}

OCR はテキスト認識機能です。リモート画面で範囲を選択し、その中のテキストを簡単に抽出できます。この機能はファームウェア v1.9.0 で導入されました。

使用するには、下向き矢印をクリックし、中国語、英語、バイリンガル（Zh/En）などの認識言語を選択します。

![recognition language](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_ocr_language.png){class="glboxshadow"}

次に **Capture** をクリックすると、リモート画面が暗くなります。抽出するテキストを囲むように範囲を指定すると、システムが自動的に認識します。認識したテキストは必要に応じてコピーできます。

![copy text](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_ocr_copy_text.png){class="glboxshadow"}

この機能を使うと、リモート画面（被制御デバイス）からテキストを取得し、ローカルの制御側デバイスにコピーできます。

### ショートカット {#shortcut}

ショートカットを使用すると、仮想キーボードを使用せずにアクションをより速く実行できるため、より効率的に作業し、日常業務の時間を節約できます。ここでいくつかの一般的なショートカットを見つけることができます。

![toolbox-shortcut1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_shortcut_1.png){class="glboxshadow"}

**Modify** をクリックして、必要に応じてショートカット オプションを調整します。

![toolbox-shortcut2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_shortcut_2.png){class="glboxshadow"}

### ウェイク オン ラン {#wake-on-lan}

Wake-on-LAN (WOL) は、被制御デバイスの電源をリモートでオンにしたり、低電力状態から復帰したりできるようにするテクノロジーです。

**Add Device** をクリックし、同じ LAN からデバイスを選択します。

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_wol.png){class="glboxshadow"}

![wol-add-device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/wol-add-device.png){class="glboxshadow" width=500}

追加したいデバイスがリストにない場合は、**Add Manually** をクリックしてデバイス名と MAC アドレスを入力します。

![wol-add-manually](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/wol-add-manually.png){class="glboxshadow" width=500}

### ターミナル {#terminal}

Comet PoE のターミナルにアクセスして高度な設定を行えます。**Access** をクリックします。

![toolbox-terminal1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_terminal_1.png){class="glboxshadow"}

GLKVM ターミナルにリダイレクトされます。

![toolbox-terminal2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbox_terminal_2.png){class="glboxshadow"}

## アクセサリー

GL.iNet は、デバイスの電源オン/オフをリモート制御するためのオプションの KVM アクセサリを提供します。

まず、アクセサリを被制御デバイスに接続するための対応するユーザー ガイドを参照してください。

- [フィンガーボット(FGB-01) ユーザーガイド](../gl-fgb-01/index.md){target="_blank"}

- [ATX ボード (GL-ATXPC) ユーザーガイド](../gl-atx-board/index.md){target="_blank"}

2 番目に、KVM コンソールにログインし、**Accessories** に移動します。アクセサリの設定は、アクセサリをインストールした後にのみ使用できます。

### フィンガーボット

Fingerbot は、被制御デバイスの物理的な電源ボタンに貼り付けられ、被制御デバイスの電源の遠隔制御を実現します。

本体の設定に従って動作します。

![accessories fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/fingerbot.png){class="glboxshadow"}

- **Time**: フィンガーボットの押し続ける時間。 0.5秒/3秒/8秒に設定できます。

- **Strength**:押す強さは軽く押す、強く押すの2段階あります。

    - **Lightly Press**: 短いボタンまたはソフトタッチのボタンに最適です。

    - **Firmly Press**: 深いボタンや硬いボタンに最適です。

    ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### ATX 電源

ATX ボードはコンピューター ケースに取り付けられており、デバイスの電源オン/オフ/再起動をリモートで制御します。

本体の設定に従って動作します。

![accessories atxpower](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/atxboard.png){class="glboxshadow"}

- **電源 (短く押す)**: 通常の電源投入またはシステムのウェイクアップに使用されます。

- **電源 (長押し)**: 強制シャットダウン操作を実行します。

- **Restart**: デバイスを再起動します。

## 仮想メディア

コンソールで、**Virtual Media**に移動します。ここでは次の操作を実行できます。

- [ファイルを共有](#file-sharing)
- [マウント画像](#image-mounting)
- [ストレージドライブの交換](#replace-storage-drive)
- [ディスクのフォーマット](#format-disk)

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/virtual-media.png){class="glboxshadow"}

### ファイル共有

Comet PoE は、読み取り/書き込み USB ドライブをエミュレートできるため、制御側デバイスと制御側デバイスの間でファイルを共有および管理できます。

**制御側デバイスから被制御デバイスにファイルを共有するには、以下の手順に従ってください。**

1. ボックスをドラッグまたはクリックして、制御側デバイスからファイルをアップロードするか、URL からアップロードします。

    アップロードされると、以下のようにファイルが表示されます。

    ![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/file-sharing1.png){class="glboxshadow"}

2. 「**Mount To Remote**」→「**File Sharing**」をクリックします。

    ![file sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/file-sharing2.png){class="glboxshadow"}
以下に示すように、

3. A ウィンドウがコンソールにポップアップ表示され、ファイル共有手順が示されます。

    ![file sharing tips](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/file-sharing3.png){class="glboxshadow"}

4. 少し待つと、**"GLKVM"** という名前のドライブが画面に自動的に表示されます。以前に制御側デバイスから Comet PoE にアップロードしたファイルが、制御側デバイスに共有されていることがわかります。これで、被制御デバイス上のこのドライブ内のファイルを表示、移動、または削除できるようになります。

    ![glkvm disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/file-sharing4.png){class="glboxshadow"}

    **Tips**: ドライブが自動的にポップアップしない場合は、被制御デバイスの **This PC** に移動します。

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/thispc.png){class="glboxshadow"}

    次に、**GLKVM** という名前のドライブを見つけます。これで、このドライブ内のファイルを表示、移動、または削除できるようになります。

5. 共有を停止する場合は、ツールバーの **Virtual Media** をクリックし、**Stop Sharing** をクリックします。

    ![stop sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/stop-sharing1.png){class="glboxshadow"}

**被制御デバイスから制御側デバイスにファイルを共有するには、以下の手順に従ってください。**

1. 被制御デバイスで、共有するファイルをドライブ **GLKVM** に移動またはコピーします。

    たとえば、「slate7pro_datasheet」という名前の PDF ファイルが、被制御デバイスのデスクトップからディスク **GLKVM** にコピーされています。

    ![move file to disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/file-sharing5.png){class="glboxshadow"}

2. Comet PoE のコンソールに移動し、ツールバーの **Virtual Media** をクリックして、**Stop Sharing** をクリックします。

    ![stop sharing 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/stop-sharing2.png){class="glboxshadow"}

3. このファイルは、次に示すように、**Virtual Media** の下に表示されます。これで、このファイルを Comet PoE から制御側デバイスにダウンロードできます。

    ![file shared](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/file-sharing6.png){class="glboxshadow"}

### イメージのマウント

Comet PoE は、被制御デバイス上の読み取り専用の仮想 CD/DVD またはディスク ドライブをシミュレートできます。このドライブには、BIOS または UEFI の起動プロセス中にアクセスできます。

この機能は、オペレーティング システムを再インストールしたり、ISO をマウントして制御対象のデバイスにアプリケーションをインストールしたり、その他のタスクを実行したりするのに役立ちます。

1. ボックスをドラッグまたはクリックしてファイルをアップロードします。 **このファイルが ISO 形式としてマウントできることを確認してください**。

    アップロードされると、以下のようにファイルが表示されます。

    ![image mounting 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/image-mounting1.png){class="glboxshadow"}

2. 「**Mount To Remote**」→「**Image Mounting**」をクリックします。

    ![image mounting 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/image-mounting2.png){class="glboxshadow"}

3. ポップアップ ウィンドウでファイルを選択し、**Mount Image** をクリックします。

    ![image mounting 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/image-mounting3.png){class="glboxshadow"}
以下に示すように、

4. A ウィンドウがコンソールにポップアップ表示され、取り付け手順が示されます。

    ![image mounting 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/image-mounting4.png){class="glboxshadow"}

5. これで、被制御デバイスの CD ドライブからこのファイルを使用できるようになります。

    ![image mounting 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/image-mounting5.png){class="glboxshadow"}

### ストレージ ドライブを交換する

USB ストレージ デバイスを KVM USB ポートに挿入して、内部ストレージを置き換えることができます。

![replace storage drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/replace-storage.png){class="glboxshadow"}

### ディスクをフォーマットします

ワンクリックでディスクをフォーマットしたり、仮想メディアを無効にしたりできます。

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/format-disable.png){class="glboxshadow"}

- **Format**: ディスク上のすべてのデータを消去し、ファイル システム構造を再初期化します。

- **Disable**: 仮想メディアを無効にすると、KVM デバイスがすぐに再起動されます。

## アプリ センター

コンソールで、**Apps Center**に移動します。統合されたアプリケーションはここにあります。

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/apps-center.png){class="glboxshadow"}

### Tailscale

[Tailscale](https://tailscale.com/){target="_blank"} は、ポート転送や複雑なファイアウォール設定を行わずに、デバイス間で暗号化されたピアツーピア プライベート ネットワークを構築する WireGuard ベースのメッシュ VPN サービスです。

Comet PoE は Tailscale と統合され、Tailscale 仮想ネットワーク経由でリモート アクセスできるようになります。

Comet PoE と制御側デバイスを同じ Tailscale アカウントにバインドするだけで、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **Tailscale 仮想 IP** を入力することで、Comet PoE にリモート アクセスできます。詳細は[こちら](../../faq/remote_access_via_tailscale.md){target="_blank"}をご覧ください。

バインド後、コンソールにはリンクされた Tailscale アカウントが表示され、出口ノードやサブネット ルートなどの高度な機能のロックが解除されます。

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/app-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier

[ZeroTier](https://www.zerotier.com/){target="_blank"} は、暗号化されたオーバーレイ仮想ネットワークを作成し、分散したデバイスをあたかも同じローカル エリア ネットワーク内にあるかのようにグローバルに接続します。

Comet PoE は ZeroTier と統合されており、ZeroTier 仮想ネットワーク経由でリモート アクセスできるようになります。

Comet PoE と制御側デバイスを同じ ZeroTier ネットワークに参加させるだけで、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **ZeroTier IP** を入力することで、Comet PoE にリモート アクセスできます。詳細は[こちら](../../faq/remote_access_via_zerotier.md){target="_blank"}をご参照ください。

バインド後、コンソールには ZeroTier ネットワーク ID と仮想 IP が表示されます。

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/app-zerotier-enabled.png){class="glboxshadow"}

### NetBird

[NetBird](https://netbird.io/){target="_blank"} は、家庭用およびビジネス用の安全なプライベート ネットワークを構築できるオープンソースのゼロトラスト ネットワーキング プラットフォームです。 WireGuard® ベースのオーバーレイ ネットワークとして、NetBird は、いつでもどこでもデバイスへの安全なアクセスを可能にします。

Comet PoE は NetBird と統合されており、NetBird 仮想ネットワーク経由でリモート アクセスできるようになります。詳細は[こちら](../../faq/remote_access_via_netbird.md){target="_blank"}をご参照ください。

バインド後、コンソールには NetBird 仮想 IP が表示されます。

![netbird enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/app-netbird-enabled.png){class="glboxshadow"}

## ヘルプ

コンソールで、**Help** に移動します。ここでは、GL.iNet KVM に関する詳細情報とヘルプ ドキュメント、およびトラブルシューティング用のログをエクスポートできます。

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/help.png){class="glboxshadow"}

## ツールバー

コンソールの右上には、次のツールがあります。

- [ツールバーを折りたたむ](#collapse)
- [フルスクリーン](#fullscreen)
- [アップグレード](#upgrade)
- [接続統計](#connection-stats)
- [クラウドサービス](#cloud-service)
- [ログアウト](#logout)

### 折りたたむ {#collapse}

右上隅の上向き矢印アイコンをクリックして、ツールバーを折りたたみます。

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_collapse_1.png){class="glboxshadow"}

ツールバーが折りたたまれている場合、上部の下向き矢印アイコンをクリックして展開します。

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_collapse_2.png){class="glboxshadow"}

### フルスクリーン {#fullscreen}

右上隅にある全画面アイコン (四角形) をクリックして、全画面モードに切り替えます。

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_fullscreen_1.png){class="glboxshadow"}

全画面表示を終了するには、**Esc** キーを押し続けるか、右上隅にある全画面表示を終了するアイコン (格子状) をクリックします。

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_fullscreen_2.png){class="glboxshadow"}

### アップグレード {#upgrade}

右上隅にあるファームウェアのバージョンをクリックして、アップデートを確認します。

![firmware upgrade 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_upgrade_1.png){class="glboxshadow"}

ポップアップウィンドウで **Local Upgrade** をクリックし、ファームウェアファイルをアップロードできます。

![firmware upgrade 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_upgrade_2.png){class="glboxshadow"}

![firmware upgrade 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_upgrade_3.png){class="glboxshadow" width=350}

ローカルアップグレードを実行する前に、[ファームウェアダウンロードセンター](https://dl.gl-inet.com/kvm){target="_blank"} から最新のファームウェアをダウンロードしてください。

### 接続統計 {#connection-stats}

Connection Stats には、遅延、ジッター、その他のリアルタイムメトリクスを監視する Data Dashboard があります。

List アイコンをクリックすると、デバイスの状態とリアルタイムデータが表示されます。

![data dashboard 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_data_dashboard_1.png){class="glboxshadow"}

チャートアイコンをクリックすると、ネットワーク遅延、ネットワークジッター、パケットロス率、リアルタイムフレームレート、再生遅延などの統計データを確認できます。

![data dashboard 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_data_dashboard_2.png){class="glboxshadow"}

### クラウドサービス {#cloud-service}

GL.iNet KVM クラウドを使用すると、制御対象のデバイスにリモートからアクセスできます。詳細は[こちら](../../faq/remote_access_via_cloud.md){target="_blank"}をご参照ください。

Comet PoE をクラウドにバインドすると、コンソールにクラウドのステータスが次のように表示されます。

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/toolbar_cloud_service.png){class="glboxshadow"}

### ログアウト {#logout}

ログアウトするには、Logout アイコンをクリックします。

![layout](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/logout.png){class="glboxshadow"}

## 設定

コンソールでナビゲーションバーの Settings アイコンをクリックすると、次の Settings ページが開きます。この機能はファームウェア v1.10.0 で導入されました。

- [USB デバイス](#usb-devices)
- [環境設定](#preferences)
- [ネットワーク](#network)
- [セキュリティ](#security)
- [クラウド](#cloud)
- [システム](#system)

![Settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/settings.png){class="glboxshadow"}

### USB デバイス {#usb-devices}

USB Devices ページでは、すべての USB エミュレーションデバイスを一元管理できます。このページから仮想周辺機器のオンとオフを切り替え、被制御ホストとの互換性を高めることができます。

![USB Emulated Devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/settings_usb_devices.png){class="glboxshadow"}

- **Microphone**

    マイクがミュートのときに Settings をクリックすると、利用方法に合わせてショートカットをカスタマイズできます。割り当てたショートカットキーを押し続けると音声の送信が開始され、放すと再びミュートになります。

    ![mic settings 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/mic_settings_1.png){class="glboxshadow" width=600}

    ![mic settings 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/mic_settings_2.png){class="glboxshadow" width=434}

  - **Device Identity**

    被制御デバイスによって認識される KVM のデバイス ID をカスタマイズまたは変更できます。EDID とデバイス ID は同期されます。いずれかを変更するともう一方も自動的に更新され、デバイスが正しく認識されるようになります。

    ![Device Identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/settings_device_identity.png){class="glboxshadow" width=350}

### 環境設定 {#preferences}

Preferences では、Layout Preferences、System Settings、Device Screen を管理できます。

![Preferences](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences**: 全画面モードでのツールバー表示と、ウィンドウモードでのステータスバー表示を必要に応じて設定できます。

- **System Settings**: ブラウザーの Tab Title、Language（Chinese、English、Japanese）、Color Mode（Light または Dark）、地域に合わせた Timezone を選択できます。


- **Device Screen**: デバイス画面を管理およびプレビューできます。Lock Screen モード（World Clock、Clock Only、Wallpaper Only）、Time Format、Date Format、Wallpaper を設定できます。

### ネットワーク {#network}

Comet PoE のホスト名や IP アドレスなどのネットワーク情報を確認、変更できます。

![network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_network.png){class="glboxshadow"}

- **Hostname**: デバイスのホスト名をコンソール上で直接変更できます。この機能はファームウェア v1.7.0 で導入されました。

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_network_hostname.png){class="glboxshadow" width=600}

- **Ethernet Settings**: Comet PoE が Ethernet ケーブルで上流のネットワークデバイスに接続されると、ここに Ethernet の情報が表示されます。

    プロトコルが DHCP の場合、ページは次のように表示されます。

    ![ethernet dhcp](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_network_dhcp.png){class="glboxshadow" width=600}

    静的 IP アドレスを設定するには、プロトコルを **Static** に切り替え、必要なネットワークパラメーター（IP アドレス、ネットマスク、ゲートウェイなど）を入力します。

    ![ethernet static](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_network_static.png){class="glboxshadow" width=600}

### セキュリティ {#security}

セキュリティにより、管理者パスワードの変更、2 要素認証の有効化、TLS 証明書のカスタマイズが可能になります。

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_security.png){class="glboxshadow"}

- Change Admin Password

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/change-password.png){class="glboxshadow" width="434"}

- 2FA: アカウントを保護するために 2 要素認証を有効にします。

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/2fa.png){class="glboxshadow"}

- TLS Certificate

    システムは、ブラウザーアクセスにプリインストール済みのデフォルト証明書を使用します。Web ブラウザーアクセス用の TLS 証明書をカスタマイズする場合は、TLS Certificate の **Custom** をクリックし、**証明書ファイルと秘密鍵ファイル**をアップロードします。

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_security_custom.png){class="glboxshadow" width=600}

### クラウド {#cloud}

Cloud では、クラウドサービスを通じてデバイスにリモートアクセスし、管理できます。

URL 経由でデバイスをクラウドにバインドできます。**More Settings** には Bind With Code、App Download、Disable などのオプションがあります。

![Cloud 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_cloud_1.png){class="glboxshadow"}

バインドが完了すると、バインド済みのクラウドアカウント情報を確認できます。**Access Cloud** をクリックして Devices を管理するか、**More Settings** をクリックして必要に応じて無効化またはバインド解除できます。

![Cloud 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_cloud_2.png){class="glboxshadow"}

同じ管理操作は、上部ツールバーの Cloud Service からも実行できます。

### システム {#system}

System 設定では、次の設定を行えます。

![system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setting_system.png){class="glboxshadow"}

- **System**: **Reboot** をクリックするとデバイスが再起動します。**Reset** をクリックすると現在のデバイス設定が消去され、再セットアップできます。

- **Upgrade**: Beta Center を有効にしてベータ版ファームウェアの更新を受け取るか、Local Upgrade を使用してローカルファイルから手動でインストールできます。

    ![local Upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1pe/console/setthing_system_local_update.png){class="glboxshadow" width=400}

- **Help & Support**: Export Log Files では、トラブルシューティングやアフターサービスに使用するデバイスの実行ログを保存できます。Help Document からは、ユーザーガイド、FAQ、トラブルシューティングドキュメントにアクセスできます。
