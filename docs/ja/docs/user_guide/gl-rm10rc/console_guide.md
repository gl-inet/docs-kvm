# Comet 5G (GL-RM10RC) コンソール ガイド {#comet-5g-gl-rm10rc-console-guide}

## セッション {#session}

コンソールで、**Session** に移動します。このページには次の 4 つのセクションがあります。

- [ビデオ](#video)
- [オーディオとカメラ](#audio-camera)
- [キーボード](#keyboard)
- [マウス](#mouse)

### ビデオ {#video}

Session では、表示モード、ビデオ品質、ビデオ伝送方式、画面の向き、EDID などのビデオ設定をカスタマイズできます。

![settings-video](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session-video.png){class="glboxshadow"}

- **Transfer**: ビデオ伝送方式を WebRTC、WebRTC (FEC)、WebRTC (Native)、Direct の間で切り替えます。Direct 転送では音声を利用できません。

    !!! note "WebRTC、WebRTC (FEC)、WebRTC (Native)、Direct の違いは何ですか?"

        - **WebRTC**: リアルタイム リモート コントロールのために、滑らかなビデオと安定したオーディオのバランスをとります。

        - **WebRTC (FEC)**: 前方誤り訂正を追加して、貧弱なまたは不安定なネットワーク条件下での接続の安定性を向上させます。選択すると、少量の冗長データを送信することで失われたデータ パケットが自動的に修復され、画面のちらつきや遅延が軽減されます。

        - **WebRTC (Native)**: Google WebRTC Library を使用してストリーミング性能を向上させ、よりスムーズなリアルタイムのリモート操作を実現します。この伝送モードはファームウェア v1.10.0 で導入されました。

        - **Direct**: 最低の遅延とロスレスビデオ品質を提供しますが、オーディオ送信はサポートしていません。

- **Mode**: 必要に応じてスマート モードとノーマル モードを切り替えます。スマート モードは、特に弱いネットワークでの帯域幅の消費を削減するのに役立ちます。

- **Latency Mode**: デバイスの「最低遅延」と「スムーズ表示」のどちらかを選択できます。この機能はファームウェア v1.9.0 で導入されました。

    !!! note "最小遅延とスムーズ表示の違いは何ですか?"

        - **Lowest Latency**: 入力遅延を最小限に抑え、キーボードとマウスのよりきびきびした応答を実現します。

        - **Smooth Display**: 視覚パフォーマンスを最適化し、途切れやフレーム損失を排除し、安定した再生を実現します。

- **Quality**: ネットワーク環境と解像度要件に応じて、ビデオ品質を自動/低/中/高/超高/ロスレスに調整します。

- **FEC Packets**: ネットワークが不安定な場合に、少量の冗長データを送信して失われたデータパケットを自動的に修復し、画面のちらつきや遅延を軽減します。FEC の比率は 5%/10%/15%/20% に調整できます。

- **Orientation**: コンソールの回転角度を 0°/90°/180°/270° に調整します。

- **EDID**: Extended Display Identification Data の略で、最適な表示パラメータに自動的に一致します。

    デフォルト設定はほとんどのシナリオに適用され、通常は変更する必要はありません。詳細は[こちら](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}をご参照ください。 EDID 調整後に画面が更新されない場合は、被制御デバイスを再起動してください。

- **View**: この設定は、ブラウザ ウィンドウのサイズを変更するときの画面のスケーリングを決定します。利用可能なオプション: アダプティブ、最高画質、オリジナル ピクセル。この機能はファームウェア v1.8.0 で導入されました。

### オーディオとカメラ {#audio-camera}

被制御デバイスのオーディオとカメラの設定を調整できます。

![Audio_Camera](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session-audio-camera.png){class="glboxshadow"}

- **Speaker**: 被制御デバイスからのオーディオ出力を制御します（システム サウンド、ビデオ オーディオなど）。

- **Microphone**: ローカル オーディオ（ユーザーの声など）を制御側デバイスからリモート エンドに送信します。ワンクリックのミュート、およびマイクをアクティブにするための長押しショートカット（つまり、Press To Speak）をサポートしています。

    **注意**: ショートカットは、使用する前に [Settings](#usb-devices) で手動で設定する必要があります。

- **Camera**: 制御側デバイスでカメラを有効にすると、ローカルの映像フレームがリモートホストにパススルーで送信され、リモートホスト上で仮想 USB カメラがエミュレートされます。リモートホスト上のアプリケーション（会議ツールや FaceTime など）は、この映像を利用でき、物理カメラを直接接続した場合と同じように使用できます。

    **注意**: この機能はファームウェア v1.10.0 で導入され、WebRTC (FEC) モードでのみ利用できます。現在は Web ブラウザーからのみ利用でき、アプリとデスクトップクライアントには対応していません。

### キーボード {#keyboard}

被制御デバイスで使用するキーボードの設定を行えます。

![keyboard image](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session_keyboard.png){class="glboxshadow"}

- **Bad Link Mode**: つまり、すぐにキーを放します。各キーの押下は 1 回の素早い押して放す動作として送信され、リモート制御中のキーの固着や意図しない繰り返し入力を防ぎます。

- **Show Virtual Keyboard**: コンソールに仮想キーボードを表示して使用します。

    ![show virtual keyboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session_show_virtual_keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS**: この機能は、Cmd キーと Ctrl キーを交換して、さまざまなオペレーティング システム間でキーボードの互換性を確保します。

### マウス {#mouse}

被制御デバイスをより快適に操作できるように、マウスの設定を調整できます。

![mouse image](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session_mouse.png){class="glboxshadow"}

- **Show Local Cursor**: 現在のデバイスのマウスを画面上に表示します。

- **Mouse Jiggle**: マウス ジグル機能は、微妙な周期的なマウスの動きをシミュレートし、リモート会議やサーバー管理中など、長時間非アクティブな状態が続いて被制御デバイスがスリープ状態になるのを防ぎます。

- **Scroll Rate**: マウス ホイールのスクロール速度、またはホイール 1 回転ごとにスクロールされる行/単位数を指し、リモコン上でコンテンツが移動する速度に影響します。

- **Scroll Direction**: マウス ホイールを上下にスクロールすると、リモート画面上のコンテンツが同じ方向（自然スクロール）に移動するか、逆方向（従来のスクロール）に移動するかを決定します。

    標準、垂直反転、水平反転、両反転の 4 つの方向モードが利用可能です。

- **Mouse Mode**: 絶対モードと相対モードを切り替えて、さまざまなリモート コントロール シナリオでスムーズかつ正確なカーソル制御を保証します。

    !!! note "絶対モードと相対モードの違いは何ですか?"

        - **Relative Mode**: マウスの位置は、固定された画面座標ではなく動きに基づいて計算されます。マウスを制御するには、リモート ウィンドウ内をクリックする必要があります。カーソルがリモート画面内でロックされ、スムーズに移動できません。このモードでは、BIOS、古いシステム、および組み込みデバイスとの互換性が向上します。

        - **Absolute Mode**: マウスの位置は正確な画面座標に対応します。リモート カーソルはローカル カーソルをスムーズかつ正確に追従するため、ローカル画面とリモート画面の間でシームレスに移動できます。ネットワーク伝送により若干の遅延が発生する場合がありますが、日常のデスクトップ制御や正確な操作に最適です。

        つまり、日々の制御をスムーズに行うには、Absolute を使用します。 BIOS アクセス、絶対位置をサポートしていない一部の古いデバイス、または誤ったカーソルの移動を避けるために相対を使用します。

- **Relative Sensitivity**: マウス モードが相対の場合に使用できます。

- **Primary Button**: プライマリ クリックとして左ボタンまたは右ボタンを選択します。この機能はファームウェア v1.9.0 で導入されました。

## ツールボックス {#toolbox}

コンソールで、**Toolbox**に移動します。ツールボックス ページには、次の 5 つのセクションが含まれています。

- [クリップボード](#clipboard)
- [OCR](#ocr)
- [ショートカット](#shortcut)
- [ウェイク オン ラン](#wake-on-lan)
- [端末](#terminal)

### クリップボード {#clipboard}

クリップボードを使用すると、ファイルを転送することなく、制御側デバイスから被制御デバイスにテキストを簡単に貼り付けることができます。

![toolbox-clipboard](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_clipboard.png){class="glboxshadow"}

### OCR {#ocr}

OCR はテキスト認識機能で、リモート画面上の領域を選択してテキストを簡単に抽出できます。この機能はファームウェア v1.9.0 で導入されました。

これを使用するには、下向き矢印をクリックして、中国語、英語、バイリンガル (Zh/En) などの優先認識言語を選択します。

![recognition language](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_ocr.png){class="glboxshadow"}

次に、**Capture** をクリックすると、リモート画面が暗くなります。抽出したいテキストの周りにボックスを描くと、システムが自動的にそれを識別します。必要に応じて、認識されたテキストをコピーできます。

![copy text](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/ocr_copy_text.png){class="glboxshadow"}

この機能を使用すると、リモート画面（つまり、被制御デバイス）からテキストを簡単にキャプチャし、それをローカル制御側デバイスにコピーできます。

### ショートカット {#shortcut}

ショートカットを使用すると、仮想キーボードを使用せずにアクションをより速く実行できるため、より効率的に作業し、日常業務の時間を節約できます。ここでいくつかの一般的なショートカットを見つけることができます。

![toolbox-shortcut-1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_shorcut.png){class="glboxshadow"}

**Modify** をクリックして、必要に応じてショートカット オプションを調整します。

![toolbox-shortcut-2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_shorcut_modify.png){class="glboxshadow"}

### ウェイク オン ラン {#wake-on-lan}

Wake-on-LAN (WOL) は、被制御デバイスの電源をリモートでオンにしたり、低電力状態から復帰したりできるテクノロジーです。

**Add Device** をクリックし、同じ LAN からデバイスを選択します。

![toolbox-wol](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_wake_on_lan.png){class="glboxshadow"}

![wol-add-device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/wol-add-device.png){class="glboxshadow" width=400}

追加したいデバイスがリストにない場合は、**Add Manually** をクリックし、デバイス名と MAC アドレスを入力します。

![wol-add-manually](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/wol-add-manually.png){class="glboxshadow" width=400}

### ターミナル {#terminal}

Comet 5Gの端末にアクセスして詳細設定を行うことができます。 「**Access**」をクリックします。

![toolbox-terminal-1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_terminal_1.png){class="glboxshadow"}

GLKVM ターミナルにリダイレクトされます。

![toolbox-terminal-2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_terminal_2.png){class="glboxshadow"}

## アクセサリー {#accessories}

GL.iNet は、デバイスの電源オン/オフをリモート制御するためのオプションの KVM アクセサリを提供します。

まず、対応するユーザー ガイドを参照して、アクセサリを被制御デバイスに接続します。

- [フィンガーボット（FGB-01）ユーザーガイド](../gl-fgb-01/index.md){target="_blank"}

- [ATX ボード (GL-ATXPC) ユーザーガイド](../gl-atx-board/index.md){target="_blank"}

2 番目に、KVM コンソールにログインし、**Accessories** に移動します。アクセサリの設定は、アクセサリをインストールした後にのみ使用できます。

### フィンガーボット {#fingerbot}

Fingerbot は、被制御デバイスの物理的な電源ボタンに貼り付けられ、被制御デバイスの電源の遠隔制御を実現します。

本体の設定に従って動作します。

![accessories fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/fingerbot.png){class="glboxshadow"}

- **Time**: フィンガーボットの押し続け時間。 0.5秒/3秒/8秒に設定できます。

- **Strength**:押す強さは軽く押す、強く押すの2段階あります。

    - **Lightly Press**: 短いボタンまたはソフトタッチのボタンに最適です。

    - **Firmly Press**: 深いボタンやしっかりしたボタンに最適です。

    ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/press_mode.png){class="glboxshadow gl-70-desktop"}

### ATX 電源 {#atx-power}

ATX ボードはコンピューターのケースに取り付けられており、デバイスの電源オン/オフ/再起動をリモートで制御します。

本体の設定に従って動作します。

![accessories atxpower](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/atxboard.png){class="glboxshadow"}

- **電源 (短く押す)**: 通常の電源投入またはシステムのウェイクアップに使用されます。

- **電源 (長押し)**: 強制シャットダウン操作を実行します。

- **Restart**: デバイスを再起動します。

## 仮想メディア {#virtual-media}

コンソールで、**Virtual Media**に移動します。ここでは次の操作を実行できます。

- [ファイル共有](#file-sharing)
- [画像取付](#image-mounting)
- [ストレージドライブの交換](#replace-storage-drive)
- [ディスクのフォーマット](#format-disk)

![virtual media](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/virtual-media.png){class="glboxshadow"}

### ファイル共有 {#file-sharing}

Comet 5G は、読み取り/書き込み USB ドライブをエミュレートできるため、制御側デバイスと制御側デバイスの間でファイルを共有および管理できます。

**制御側デバイスから被制御デバイスにファイルを共有するには、以下の手順に従ってください。**

1. ボックスをドラッグまたはクリックして、制御側デバイスからファイルをアップロードするか、URL からアップロードします。

    アップロードされると、以下のようにファイルが表示されます。

    ![upload files](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing1.png){class="glboxshadow"}

2. 「**Mount To Remote**」→「**File Sharing**」をクリックします。

    ![file sharing](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing2.png){class="glboxshadow"}
以下に示すように、

3. A ウィンドウがコンソールにポップアップ表示され、ファイル共有の手順が示されます。

    ![file sharing tips](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing3.png){class="glboxshadow"}

4. 少し待つと、**"GLKVM"** という名前のドライブが画面に自動的に表示されます。以前に制御側デバイスから Comet 5G にアップロードしたファイルが、制御側デバイスに共有されていることがわかります。これで、被制御デバイス上のこのドライブ内のファイルを表示、移動、または削除できるようになります。

    ![glkvm disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing4.png){class="glboxshadow"}

    **Tips**: ドライブが自動的にポップアップしない場合は、被制御デバイスの **This PC** に移動します。

    ![this pc](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/thispc.png){class="glboxshadow"}

    次に、**GLKVM** という名前のドライブを見つけます。これで、このドライブ内のファイルを表示、移動、または削除できるようになります。

5. 共有を停止する場合は、ツールバーの **Virtual Media** をクリックし、**Stop Sharing** をクリックします。

    ![stop sharing 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/stop-sharing1.png){class="glboxshadow"}

**被制御デバイスから制御側デバイスにファイルを共有するには、以下の手順に従ってください。**

1. 被制御デバイスで、共有するファイルをドライブ **GLKVM** に移動またはコピーします。

    たとえば、「slate7pro_datasheet」という名前の PDF ファイルが、被制御デバイスのデスクトップからディスク **GLKVM** に移動されました。

    ![move file to disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing5.png){class="glboxshadow"}

2. Comet 5G のコンソールに移動し、ツールバーの **Virtual Media** をクリックし、**Stop Sharing** をクリックします。

    ![stop sharing 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/stop-sharing2.png){class="glboxshadow"}

3. このファイルは、次に示すように、**Virtual Media** の下に表示されます。これで、このファイルを Comet 5G から制御側デバイスにダウンロードできます。

    ![file shared](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing6.png){class="glboxshadow"}

### イメージのマウント {#image-mounting}

Comet 5G は、被制御デバイス上の読み取り専用の仮想 CD/DVD またはディスク ドライブをシミュレートできます。 BIOS または UEFI 起動プロセス中にこのドライブにアクセスできます。

この機能は、オペレーティング システムを再インストールしたり、ISO をマウントして制御対象のデバイスにアプリケーションをインストールしたり、その他のタスクを実行したりするのに役立ちます。

1. ボックスをドラッグまたはクリックしてファイルをアップロードします。 **このファイルが ISO 形式としてマウントできることを確認してください**。

    アップロードされると、以下のようにファイルが表示されます。

    ![image mounting 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting1.png){class="glboxshadow"}

2. 「**Mount To Remote**」→「**Image Mounting**」をクリックします。

    ![image mounting 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting2.png){class="glboxshadow"}

3. ポップアップ ウィンドウでファイルを選択し、**Mount Image** をクリックします。

    ![image mounting 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting3.png){class="glboxshadow"}
以下に示すように、

4. A ウィンドウがコンソールにポップアップ表示され、取り付け手順が示されます。

    ![image mounting 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting4.png){class="glboxshadow"}

5. これで、被制御デバイスの CD ドライブからこのファイルを使用できるようになります。

    ![image mounting 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting5.png){class="glboxshadow"}

### ストレージ ドライブを交換する {#replace-storage-drive}

USB ストレージ デバイスを KVM USB ポートに挿入して、内部ストレージを置き換えることができます。

![replace storage drive](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/replace-storage.png){class="glboxshadow"}

### ディスクをフォーマットします {#format-disk}

ワンクリックでディスクをフォーマットしたり、仮想メディアを無効にしたりできます。

![format disk](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/format-storage.png){class="glboxshadow"}

- **Format**: ディスク上のすべてのデータを消去し、ファイル システム構造を再初期化します。

- **Disable**: 仮想メディアを無効にすると、KVM デバイスがすぐに再起動されます。

## アプリ センター {#apps-center}

コンソールで、**Apps Center**に移動します。統合されたアプリケーションはここにあります。

![apps center](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} は、ポート転送や複雑なファイアウォール設定を行わずに、デバイス間で暗号化されたピアツーピア プライベート ネットワークを構築する WireGuard ベースのメッシュ VPN サービスです。

Comet 5G は Tailscale と統合され、Tailscale 仮想ネットワーク経由でリモート アクセスできるようになります。

Comet 5G と制御側デバイスを同じ Tailscale アカウントにバインドするだけで、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **Tailscale 仮想 IP** を入力することで、Comet 5G にリモート アクセスできます。詳細は[こちら](../../faq/remote_access_via_tailscale.md){target="_blank"}をご参照ください。

バインド後、コンソールにはリンクされた Tailscale アカウントが表示され、出口ノードやサブネット ルートなどの高度な機能のロックが解除されます。

![tailscale enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} は、暗号化されたオーバーレイ仮想ネットワークを作成し、分散したデバイスをあたかも同じローカル エリア ネットワーク内にあるかのようにグローバルに接続します。

Comet 5G は ZeroTier と統合され、ZeroTier 仮想ネットワーク経由でリモート アクセスできるようになります。

Comet 5G と制御側デバイスを同じ ZeroTier ネットワークに参加させるだけで、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **ZeroTier IP** を入力することで、Comet 5G にリモート アクセスできます。詳細は[こちら](../../faq/remote_access_via_zerotier.md){target="_blank"}をご参照ください。

バインド後、コンソールには ZeroTier ネットワーク ID と仮想 IP が表示されます。

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/apps-zerotier-enabled.png){class="glboxshadow"}

### NetBird {#netbird}

[NetBird](https://netbird.io/){target="_blank"} は、家庭用およびビジネス用の安全なプライベート ネットワークを構築できるオープンソースのゼロトラスト ネットワーキング プラットフォームです。 WireGuard® ベースのオーバーレイ ネットワークとして、NetBird は、いつでもどこでもデバイスへの安全なアクセスを可能にします。

Comet 5G は NetBird と統合されており、NetBird 仮想ネットワーク経由でリモート アクセスできるようになります。詳細は[こちら](../../faq/remote_access_via_netbird.md){target="_blank"}をご参照ください。

バインド後、コンソールには NetBird 仮想 IP が表示されます。

![netbird enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/apps-netbird-enabled.png){class="glboxshadow"}

## ヘルプ {#help}

コンソールで、**Help**に移動します。ここでは、GL.iNet KVM に関する詳細情報とヘルプ ドキュメント、およびトラブルシューティングのためのログをエクスポートできます。

![help](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/help.png){class="glboxshadow"}

## ツールバー {#toolbar}

コンソールで、右上隅に移動して次のツールにアクセスします。

- [ツールバーを折りたたむ](#collapse)
- [フルスクリーン](#fullscreen)
- [アップグレード](#upgrade)
- [接続統計](#connection-stats)
- [クラウドサービス](#cloud-service)
- [ログアウト](#logout)

### 折りたたむ {#collapse}

右上隅の上向き矢印アイコンをクリックして、ツールバーを折りたたみます。

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_collapse_1.png){class="glboxshadow"}

ツールバーが折りたたまれている場合、上部の下向き矢印アイコンをクリックして展開します。

![collapse](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_collapse_2.png){class="glboxshadow"}

### フルスクリーン {#fullscreen}

右上隅にある全画面アイコン（四角形）をクリックして、全画面モードに切り替えます。

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_fullscreen_1.png){class="glboxshadow"}

全画面表示を終了するには、**Esc** キーを押し続けるか、右上隅にある全画面表示を終了するアイコン（格子状）をクリックします。

![fullscreen](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_fullscreen_2.png){class="glboxshadow"}

### アップグレード {#upgrade}

右上隅にあるファームウェアのバージョンをクリックして、アップデートを確認します。

![firmware upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_upgrade_1.png){class="glboxshadow"}

ポップアップウィンドウで **Local Upgrade** をクリックすると、ファームウェアファイルをアップロードできます。

![firmware upgrade 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_upgrade_2.png){class="glboxshadow" width=400}

![firmware upgrade 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_upgrade_3.png){class="glboxshadow" width=400}

ローカル アップグレードを実行する前に、[ファームウェア ダウンロード センター](https://dl.gl-inet.com/kvm){target="_blank"} から最新のファームウェアをダウンロードしてください。

### 接続統計 {#connection-stats}

Connection Stats には、レイテンシー、ジッターなどのリアルタイムの指標を監視する Data Dashboard があります。

リストアイコンをクリックすると、デバイスの状態とリアルタイムのデータを表示します。

![data dashboard 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/data_dashboard_1.png){class="glboxshadow"}

グラフアイコンをクリックすると、ネットワークのレイテンシー、ジッター、パケット損失率、リアルタイムのフレームレート、再生遅延などの統計データを確認できます。

![data dashboard 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/data_dashboard_2.png){class="glboxshadow"}

### クラウド サービス {#cloud-service}

GL.iNet KVM クラウドを使用すると、制御対象のデバイスにリモートからアクセスできます。詳細は[こちら](../../faq/remote_access_via_cloud.md){target="_blank"}をご参照ください。

Comet 5G がクラウドにバインドされると、コンソールには次のようにクラウドのステータスが表示されます。

![cloud service](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/cloud-services.png){class="glboxshadow"}

### ログアウト {#logout}

ログアウトするには、Logout アイコンをクリックします。

![layout](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/logout.png){class="glboxshadow"}

## 設定 {#settings}

コンソールのナビゲーションバーにある Settings アイコンをクリックすると、次の設定ページが開きます。この機能はファームウェア v1.10.0 で導入されました。

- [USB デバイス](#usb-devices)
- [環境設定](#preferences)
- [ネットワーク](#network)
- [セキュリティ](#security)
- [クラウド](#cloud)
- [システム](#system)

![Settings](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting.png){class="glboxshadow"}

### USB デバイス {#usb-devices}

USB Devices では、USB エミュレーションデバイスを一元管理できます。このページから仮想周辺機器を有効または無効にして、被制御デバイスとの互換性を向上させることができます。

![USB Emulated Devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_usb_devices.png){class="glboxshadow"}

- **Microphone**

    マイクがミュートされているときに、Settings をクリックして使い方に合わせたショートカットを設定できます。割り当てたショートカットキーを長押しすると音声を送信し、キーを放すと再びミュートになります。

    ![mic settings 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/mic_setting_1.png){class="glboxshadow" width=600}

    ![mic settings 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/mic_setting_2.png){class="glboxshadow" width=434}

- **Device Identity**

    被制御デバイスによって認識される KVM の ID をカスタマイズまたは変更します。 EDID とデバイス ID は同期されたままであることに注意してください。どちらかを変更すると、もう一方も自動的に更新され、デバイスが正しく認識されるようになります。

    ![Device Identity](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/settings_device_identity.png){class="glboxshadow" width=350}

### 環境設定 {#preferences}

Preferences では、Layout Preferences、System Settings、Device Screen の設定を管理できます。

![Preferences](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_preference.png){class="glboxshadow"}

- **Layout Preferences**: 必要に応じて、フルスクリーン時のツールバー表示とウィンドウモード時のステータスバー表示を設定できます。

- **System Settings**: ブラウザーの Tab Title、Language（中国語、英語、日本語）、Color Mode（Light、Dark）、お住まいの地域に合わせた Timezone を選択して、システム設定をカスタマイズできます。

- **Device Screen**: デバイスの画面を管理し、プレビューできます。Lock Screen モード（World Clock、Clock Only、Wallpaper Only）、Time Format、Date Format、Wallpaper を設定できます。

### ネットワーク {#network}

ホスト名や IP アドレスなど、Comet 5G のネットワークの詳細を確認および変更できます。

![network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network.png){class="glboxshadow"}

- **Hostname**: デバイスのホスト名はコンソールで直接変更できます。この機能はファームウェア v1.7.0 で導入されました。

    ![modify hostname](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_hostname.png){class="glboxshadow" width=600}

- **Ethernet Settings**: Comet 5G がイーサネットケーブル経由で上流のネットワークデバイスに接続すると、そのイーサネット接続の詳細がここに表示されます。

    プロトコルが DHCP の場合、ページは次のように表示されます。

    ![ethernet dhcp](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_dhcp.png){class="glboxshadow" width=600}

    静的 IP アドレスを設定する場合は、プロトコルを **Static** に切り替え、必要なネットワーク パラメーター（IP アドレス、ネットマスク、ゲートウェイなど）をそれに応じて入力します。

    ![ethernet static](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_static.png){class="glboxshadow" width=600}

- **Wireless**: Comet 5G は、**Station Mode** および **AP Mode** の 2 つのワイヤレス動作モードをサポートし、さまざまなネットワーク アクセス要件に対応します。

    **Modify** をクリックすると、ネットワークモードを切り替えたり、IP アドレス、ゲートウェイ、MAC アドレスを確認したりできます。

    ![modify wifi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_modify_wifi.png){class="glboxshadow" width=600}

    - **Station Mode**

        このモードは、Comet 5G が接続できる既存のワイヤレスネットワークがある場合に適しています。

        このモードでは、Comet 5G はワイヤレス クライアントとして機能し、上流の Wi-Fi ホットスポット（ルーターなど）をスキャンして接続し、ネットワーク アクセスを取得できます。

        ![wifi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_wifi.png){class="glboxshadow"}

        別の Wi‑Fi ネットワークに接続する場合は、下部の **Switch Wi-Fi** をクリックします。

        ![switch wifi 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/switch_wifi_1.png){class="glboxshadow"}

        次に、利用可能なネットワークのリストから Wi-Fi を選択します。

        ![switch wifi 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/switch-wifi2.png){class="glboxshadow"}

    - **AP Mode**

        このモードはローカル エリア ネットワークのセットアップに最適で、外部ネットワークを必要とせずに KVM のオフライン近距離制御を可能にします。

        このモードでは、Comet 5G 自体が Wi-Fi ホットスポットとして機能し、スマートフォンやラップトップなどの端末デバイスが接続するための信号をブロードキャストします。ただし、Wi-Fi 経由でアップストリーム ネットワークにアクセスすることはできなくなります。

        ![wifi ap](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/wifi-ap-mode.png){class="glboxshadow"}

- **Cellular**: Comet 5G にはセルラーモジュールが内蔵されており、SIM カード経由でモバイル ネットワーク アクセスが可能です。

    SIM カードが検出されたら、**Modify** をクリックして、セルラー接続の詳細（キャリア情報、電話番号、ICCID、現在の APN プロファイルなど）を確認できます。

    ![modify cellular](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/celluar_modify.png){class="glboxshadow" width=600}

    ![cellular](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_cellular.png){class="glboxshadow"}

    - **SIM Settings** を使用すると、携帯電話の設定を管理できます（APN や MTU の調整など）。

    - **AT コマンド** を使用すると、AT コマンドを実行してモデム関連の出力を取得できます。

    - **Cellular Firewall** は、携帯電話ネットワークのファイアウォール ルールを設定するために使用されます。

    要約すると、セルラー接続は、イーサネットまたは Wi-Fi 接続が利用できない場合の堅牢なバックアップ ネットワーク オプションとして機能します。

### セキュリティ {#security}

セキュリティにより、管理者パスワードの変更、2 要素認証の有効化、TLS 証明書のカスタマイズが可能になります。

![security](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_security.png){class="glboxshadow"}

- 管理者パスワードを変更します。

    ![change admin password](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/change-password.png){class="glboxshadow" width="434"}

- 2FA: アカウントを保護するために 2 要素認証を有効にします。

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/2fa.png){class="glboxshadow"}

- TLS 証明書

    システムは、ブラウザー アクセスにプリインストールされたデフォルトの証明書を使用します。 Web ブラウザー アクセス用の TLS 証明書をカスタマイズする場合は、TLS Certificate の **Custom** をクリックして、**証明書ファイルと秘密キー ファイル**をアップロードします。

    ![TLS certificate custom](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_security_custom.png){class="glboxshadow"}

### クラウド {#cloud}

Cloud では、クラウドサービスを利用してデバイスにリモートアクセスし、管理できます。

URL を使用してデバイスをクラウドにバインドできます。**More Settings** には、Bind With Code や App Download などのオプションがあります。必要に応じて無効にすることもできます。

![Cloud 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_cloud_1.png){class="glboxshadow"}

バインドが完了すると、バインド先のクラウドアカウント情報を確認できます。**Access Cloud** をクリックしてデバイスを管理したり、**More Settings** をクリックして必要に応じて無効にしたり、バインドを解除したりできます。

![Cloud 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_cloud_2.png){class="glboxshadow"}

上部ツールバーの Cloud Service からも、同じ管理操作を行えます。

### システム {#system}

System の設定では、次の項目を設定できます。

![system](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_system.png){class="glboxshadow"}

- **System**: **Reboot** をクリックするとデバイスが再起動します。**Reset** をクリックすると現在のデバイス設定が消去され、デバイスを再設定できます。

- **Upgrade**: Beta Center を有効にしてベータ版ファームウェアの更新を受け取るか、Local Upgrade を使用してローカルファイルから手動でインストールできます。

    ![local Upgrade](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setthing_system_local_update.png){class="glboxshadow" width=400}

- **Help & Support**: Export Log Files では、トラブルシューティングやアフターサポートに使用するデバイスの実行ログを保存できます。Help Document からは、ユーザーガイド、FAQ、トラブルシューティングのドキュメントにアクセスできます。
