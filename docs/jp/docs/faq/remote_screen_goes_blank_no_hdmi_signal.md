# リモート画面が空白になるか、HDMI 信号が表示されない場合はどうすればよいですか

KVM を通じて被制御デバイスにアクセスするときに、リモート画面が空白になるか、HDMI 信号が表示されない場合は、次の手順に従ってトラブルシューティングを行ってください。

![white screen](https://static.gl-inet.com/docs/kvm/faq/blank_screen/white_screen.png){class="glboxshadow"}
<small>(白画面)</small>

![black screen](https://static.gl-inet.com/docs/kvm/faq/blank_screen/black_screen.png){class="glboxshadow"}
<small>(黒い画面)</small>

まず、これがビデオ送信に関連しているかどうかを確認します。 KVM にログインし、**Settings** -> **Video** -> **Transfer** に移動し、転送モードを **Direct** に設定します。

![change transfer](https://static.gl-inet.com/docs/kvm/faq/blank_screen/change_transfer.png){class="glboxshadow" width="360"}

問題が解決しない場合は、以下に挙げる考えられる原因を 1 つずつ確認してください。

## ハードウェア接続を確認してください

1. **Faulty HDMI Cable**

    経年劣化した HDMI ケーブル、酸化したコネクタ、または内部の破損により、信号伝送が中断される可能性があります。高品質の HDMI ケーブルに交換してください。

    HDMI 信号ステータスは、KVM コンソールでも確認できます。右下隅にあるモニターアイコンを見つけて、「HDMI信号がありません」と表示されているかどうかを確認します。

    ![no HDMI signal](https://static.gl-inet.com/docs/kvm/faq/blank_screen/no_hdmi_signal.png){class="glboxshadow"}

2. **Incorrect Connection**

    被制御デバイスがデスクトップ PC の場合は、KVM の **HDMI IN** ポートがデスクトップのグラフィックス カードまたはマザーボードの HDMI OUT ポートに接続されていることを確認してください。プラグが完全に差し込まれ、しっかりと固定されていることを確認してください。複数の HDMI 出力 (例: 専用 GPU + マザーボード出力) を備えたデバイスの場合は、別のポートに切り替えてみてください。

    被制御デバイスがラップトップの場合、KVM の **HDMI IN** ポートがラップトップの HDMI OUT ポートに接続されていることを確認してください。

    ヒント: 一部の KVM モデル (Comet Pro や Comet 5G など) には、2 つの HDMI ポートがあります。被制御デバイスの HDMI ケーブルが KVM の HDMI IN ポートに接続されていることを確認してください。 HDMI OUT に接続すると、HDMI 信号は KVM コンソールで検出されません。

3. **Improper Use of Adapters**

    HDMI アダプターが必要な場合は、**VGA-to-HDMI** アダプターを使用して、被制御デバイスを GL.iNet KVM の HDMI IN ポートに接続します。

    この接続に HDMI - VGA アダプターを使用すると、ビデオ信号が適切に送信されず、空白の画面が表示されます。

    ![adapter comparison](https://static.gl-inet.com/docs/kvm/faq/blank_screen/adapter_comparison.png){class="glboxshadow"}

## ブラウザ設定を確認してください

ブラウザ経由で制御対象のデバイスにアクセスし、画面が空白になる問題が発生した場合は、次の方法を試してください。

1. **複数のブラウザでテストします。** Chrome、Firefox、Edge などを試して、問題がブラウザ固有のものであるかどうかを判断します。

2. **WebRTC リーク保護/制御拡張機能を無効にします。** WebRTC 接続に影響を与える可能性のある拡張機能/プラグインを Web ブラウザにインストールしている場合は、それらを無効にして再度テストしてください。ブラウザの [設定] -> [プライバシーとセキュリティ] に移動して、Web ブラウザが WebRTC 接続を許可していることを確認することもできます。

    ![webrtc](https://static.gl-inet.com/docs/kvm/faq/blank_screen/webrtc.png){class="glboxshadow"}

## 被制御デバイスのステータスと設定を確認する

1. **デバイスの電源が入っていないか、スリープ モードになっています**

    被制御デバイスの電源が完全にオンになっていて、電源管理設定によりスリープ/休止状態モードになっていないことを確認します (必要に応じてローカル ボタンを使用してスリープ解除します)。

2. **被制御デバイス上のグラフィック カード ドライバーが異常です**

    グラフィックス カード ドライバーがインストールされていないか破損していると、ビデオ出力ができない可能性があります。被制御デバイスのグラフィックス カード ドライバーを更新または再インストールします (ローカルにログインしている場合)。

3. **専用グラフィックスと統合グラフィックスの間違った接続**

    被制御デバイスに専用グラフィックス カードと統合グラフィックス カードの両方が搭載されている場合は、HDMI ケーブルが正しいグラフィックス ポートに接続されていることを確認してください (たとえば、HDMI ケーブルが取り付けられている場合は、専用グラフィックス ポートに接続します)。

4. **制御機器の表示設定異常(低確率)**

    GL.iNet KVM が被制御デバイスに接続すると、モニターの EDID を読み取って表示出力を自動的に調整し、最適なパフォーマンスを実現します。ほとんどの場合、デフォルトの EDID 構成はほとんどのシナリオに適しており、変更する必要はありません。

    被制御デバイスが標準モニターと互換性がある場合、GLKVM 経由でアクセスするときに空白の画面や表示の問題が発生する可能性はほとんどありません。ただし、いくつかの特定の互換性の問題 (Linux システム + ASUS モニターなど) により、GLKVM の使用時に空白の画面が表示される場合があります。

    被制御デバイスが標準モニターと互換性があるかどうか、また特定のモニターとの互換性に問題があるかどうかを確認してください。

5. **Resolution Issue**

    GLKVM が特定のオペレーティング システム (Proxmox VE Hypervisor など) に接続されている場合、利用可能なディスプレイ解像度を正しくネゴシエートできず、ディスプレイの問題が発生する場合があります。これは、被制御デバイスの解像度を手動で調整することで解決できます。

    ここでは、Proxmox VE Hypervisor でシステム解像度を変更する方法についてのガイドを参照してください。

    1. PVE ターミナルを開き、以下のコマンドを入力してファイル `/etc/default/grub` を編集します。

        ```
        nano /etc/default/grub
        ```

    2. 次の行を追加します。

        ```
        GRUB_CMDLINE_LINUX_DEFAULT="quiet gfxpayload=text nomodeset
        ```

    3. `#` を削除して `GRUB_GFXMODE` 行のコメントを解除し、`1024x768` などの目的の解像度を設定します。

        ```
        GRUB_GFXMODE=1024x768
        ```

    4. `Ctrl + O` を押して Enter を押し、構成を保存します。

    5. `Ctrl + X` を押して nano エディターを終了します。

    6. 以下のコマンドを入力して構成を適用します。

        ```
        update-grub
        ```
---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
