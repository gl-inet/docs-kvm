# KVM デバイス ID を変更する方法

## KVM デバイス ID とは

GL.iNet KVM のデバイス ID は、通信中に接続されたデバイスが KVM を認識および区別できるようにする識別子を指します。

GL.iNet KVM は、ユーザー操作用の複数のデバイスを組み合わせたエミュレーターとして動作するため、制御対象のデバイスに接続すると、モニター、マウスやキーボードなどの複数の USB デバイス、および USB ドライブを含む複数のデバイスのセットとして認識されます。

デフォルトでは、デバイス ID は **GLKVM** で、KVM コンソールで確認できます (**Settings** -> **System**)。

![device identity](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/device_identity.png){class="glboxshadow"}

通常、KVM には、以下に示すように Type-C ポートが装備されており、被制御デバイスの USB ポートに接続して、周辺機器 (キーボード、マウス、USB ドライブ、マイクなど) および CD-ROM をシミュレートします。

![gl-rm1 type-c](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

ユーザーがマウスをクリックしたり、キーボードを入力したり、制御側のマイクを使用したりすると、これらの信号は物理的な KVM デバイスにリモートで送信されます。次に、KVM は、Type-C ポートを介して被制御デバイスにそれらを転送します。したがって、KVM は通常、被制御デバイスの USB ポートに接続された複数の周辺デバイスをエミュレートする複合デバイスとみなされます。

!!! note

    制御側デバイスの入力方法/キーボードが被制御デバイスの入力方法/キーボードと一致していない場合、一部の記号/文字がキーボード上で異なる位置にある可能性があり、これにより被制御側の出力が制御側の入力と不一致になる可能性があります。詳細は[こちら](../faq/keyboard_does_not_input_output_as_expected.md)をクリックしてください。

GL.iNet KVM のデバイス ID はデフォルトで GLKVM であるため、被制御デバイス (Bluetooth やデバイスなど) のシステム設定では GLKVM または Glinet Composite Device として表示されます。

![device identity default](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}

## デバイス ID を変更する理由

デフォルトでは、GL.iNet KVM は、キーボード、マウス、マイク、モニターなどの周辺機器をエミュレートする複合デバイスとして被制御デバイスによって認識されます。これらの設定はユーザー自身のみに表示されるため、通常はこれによって不都合が生じることはありません。

![mic settings](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/mic.png){class="glboxshadow"}
<small>(マイク設定)</small>

![speaker settings](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(スピーカー設定)</small>

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

1. KVM にログインし、**Settings** -> **System** -> **Device Identity** に移動します。ドロップダウン リストからプリセット ID を選択します。

    ![customize1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    または、**Customize** をクリックして、ポップアップ ウィンドウに必要なパラメータを入力します。

    ![customize2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. 選択すると、再起動を求めるポップアップ ウィンドウが表示されます。 **Confirm** をクリックして再起動します。

    ![customize3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. 再起動後、KVM コンソールで、デバイス ID が変更されたものに変更されています。

    ![customize4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

    KVM 経由で被制御デバイスにアクセスし、**Settings** -> **Bluetooth とデバイス** に移動します (Windows 10 Pro を例にします)。入力デバイス (キーボードとマウス)、オーディオ デバイス (マイク)、およびディスプレイ (モニター) は、デフォルトの GLKVM ではなく、設定したカスタム デバイスとして認識されます。

    ![customize5](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
