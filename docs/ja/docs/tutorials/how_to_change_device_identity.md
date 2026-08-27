# KVM デバイス ID を変更する方法

## KVM デバイス ID とは

GL.iNet KVM のデバイス ID は、通信中に接続されたデバイスが KVM を認識および区別できるようにする識別子を指します。

通常、KVM には、以下に示すように Type-C ポートが装備されており、被制御デバイスの USB ポートに接続して、周辺機器 (キーボード、マウス、USB ドライブ、マイクなど) および CD-ROM をシミュレートします。

![gl-rm1 type-c](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

制御側でマウスをクリックしたり、キーボードを入力したり、マイクを使用したりすると、これらの信号は物理的な KVM デバイスにリモートで送信されます。KVM は、それらを Type-C ポート経由で被制御デバイスに転送します。

したがって、KVM は通常、被制御デバイスの USB ポートに接続された複数の周辺機器をエミュレートする複合デバイスとみなされます。

![device identity principle](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/principle.png){class="glboxshadow"}

!!! note

    制御側デバイスの入力方法/キーボードが被制御デバイスの入力方法/キーボードと一致していない場合、一部の記号/文字がキーボード上で異なる位置にある可能性があり、これにより被制御側の出力が制御側の入力と不一致になる可能性があります。詳細は[こちら](../faq/keyboard_does_not_input_output_as_expected.md)をクリックしてください。

## デバイス ID を変更する理由

GL.iNet KVM は、ユーザー操作用の複数のデバイスを組み合わせてエミュレートするため、被制御デバイスに接続すると、モニター、マウスやキーボードなどの複数の USB デバイス、および USB ドライブを含む一連のデバイスとして認識されます。

デフォルトのデバイス ID は **GLKVM** です。そのため、被制御デバイスのシステム設定では GLKVM または Glinet Composite Device と表示されます。これらの設定はユーザー本人にしか表示されないため、通常は不都合を生じません。

![device identity default](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}
<small>(Bluetooth & devices の設定)</small>

![speaker settings](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(Speaker の設定)</small>

ただし、次のシナリオでは、ユーザーは KVM のデバイス ID を変更する必要がある場合があります。

??? "シナリオ 1: オフィスのコンピューター上の監視ソフトウェアからのアラートを回避する"

    被制御デバイスがオフィス コンピュータの場合、監視ソフトウェアが内蔵またはインストールされている場合があります。これらのツールは、KVM リモート アクセスを異常なアクティビティとしてマークし、アラートをトリガーし、IT システムに報告することもあります。

    KVM のデバイス ID を変更すると、通常のリモート コントロール機能を維持しながら、このような不要な通知を防ぐことができます。

??? "シナリオ 2: オンライン会議の画面共有中に KVM のリモート使用を非表示にする"

    画面共有が必要なオンライン会議中、被制御デバイスのシステム設定 (Bluetooth やデバイスなど) に KVM のデフォルト ID が表示される場合があります。これにより、KVM リモート アクセスの使用状況が会議参加者に公開される可能性があり、一部のユーザーにとっては望ましくない可能性があります。

    デバイス ID を変更すると、KVM が共有画面で非表示のままになります。

    ![screen sharing](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/screen_sharing.png){class="glboxshadow"}
    <small>(画面共有)</small>

??? "シナリオ 3: 被制御デバイス上で応答しないマウス/キーボード コントロールを解決する"

    KVM を介して被制御デバイスのマウスとキーボードを制御できない場合は、KVM のデバイス ID を変更して互換性の問題を回避し、KVM と被制御デバイス間のスムーズな信号伝送を可能にしてみてください。

## デバイス ID カスタマイズの制限事項

!!! warning "行動検出ソフトウェアは依然として KVM を識別する可能性がある"

    USB デバイス ID をカスタマイズする方法に関係なく、仮想化デバイス (キーボード、マウス、マイク、カメラなど) の USB **構造**は、動作検出ソフトウェアにとって依然として不審に見える可能性があります。

    根本的な問題は、これらすべての仮想化ペリフェラルが **単一の複合 USB デバイス**に属していることです。キーボードとマウスのみを含む複合デバイスは比較的一般的ですが、多くのワイヤレス キーボード/マウス レシーバー (Logicool Unifying など) は同様の構造を示していますが、**キーボード、マウス、マイク**を同時に含む単一の複合 USB デバイスは、実際には非常にまれです。

    したがって、デバイス ID を変更するだけでは、高度な監視ソフトウェアや動作分析ソフトウェアによる検出を回避するには**十分ではない可能性があります**。

## デバイス ID を変更する方法

### ファームウェア v1.10 以降

1. KVM にログインし、右上の **Settings** に移動します。**USB Devices** で **Device Identity** を見つけ、カスタマイズします。

    ![identity customize1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize1.png){class="glboxshadow"}

2. ポップアップ ウィンドウで **Confirm** をクリックして再起動します。

    ![identity customize2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize2.png){class="glboxshadow"}

3. 再起動後、KVM コンソールで Device Identity が変更されていることを確認します。

    ![identity customize3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize3.png){class="glboxshadow"}

4. デバイス ID を確認します。以下では、Windows 11 Pro を被制御デバイスとして使用します。

    被制御デバイスで **Settings** -> **Bluetooth & devices** に移動します。入力デバイスとオーディオ デバイスが、設定したデバイスとして認識されています。

    ![identity customize4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize4.png){class="glboxshadow"}

### ファームウェア v1.9 以前

1. KVM にログインし、**Settings** -> **System** -> **Device Identity** に移動します。ドロップダウン リストからプリセット ID を選択します。

    ![identity customize1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    または、**Customize** をクリックして、ポップアップ ウィンドウに必要なパラメータを入力します。

    ![identity customize2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. ポップアップ ウィンドウで **Confirm** をクリックして再起動します。

    ![identity customize3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. 再起動後、KVM コンソールで Device Identity が変更されていることを確認します。

    ![identity customize4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

4. デバイス ID を確認します。以下では、Windows 10 Pro を被制御デバイスとして使用します。

    被制御デバイスで **Settings** -> **Bluetooth & devices** に移動します。入力デバイスとオーディオ デバイスが、設定したデバイスとして認識されています。

    ![identity customize5](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
