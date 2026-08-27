# GL.iNet KVM の EDID の設定方法

## EDIDとは

EDID、つまり拡張ディスプレイ識別データは、Video Electronics Standards Association (VESA) によって策定された標準データ形式です。これはディスプレイの不揮発性メモリに保存され、製造元、最大解像度、リフレッシュ レートなどのディスプレイの重要な情報が含まれています。コンピュータなどのデバイスは、EDID を読み取ることで出力信号のパラメータを自動的に調整し、ディスプレイに画像が最適な状態で表示されるようにすることができます。

一般的に、コンピューター、ラップトップ、ゲーム機などのデバイスがディスプレイに接続されると、自動的に EDID を読み取って適切な表示パラメーターを設定し、ぼやけた画像やちらつきなどの問題を回避し、鮮明で安定した視覚体験をユーザーに提供します。

GL.iNet KVM の EDID 設定は、ディスプレイの最適なパラメーターを自動的に一致させることを目的としています。 GL.iNet KVM が被制御デバイスに接続されている場合、ディスプレイの EDID を読み取ることで、ディスプレイ出力を自動的に調整して最高の画像を表示できます。 

## プリセット EDID

GL.iNet KVM コンソールで、**Settings** -> **Video** -> **EDID** に移動します。いくつかのプリセット EDID 設定があります。 

![edid preset](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_preset.jpg){class="glboxshadow"}

**デフォルトの EDID または GL.iNet KVM はすでにほとんどのシナリオに適しており、通常は変更する必要はありません**。

UEFI/BIOS の構成や解像度/リフレッシュ レートのカスタマイズなどの特別な状況の場合は、プリセット値 (例: 1920×1280/AUO/60HZ) を選択できます。

## カスタム EDID

適切な EDID コードが見つからない場合は、[このリンク](https://github.com/linuxhw/EDID){target="blank"} または以下の手順を参照して、EDID 構成をカスタマイズしてください。

!!! tip

    希望の解像度とリフレッシュ レートに正確に一致する EDID を見つけるのは難しい場合があります。 **RTDtool** や **EEditZ** などの EDID 編集ツールを使用して、特定のニーズに合わせて既存の EDID を変更できます。

1. 適切な EDID [こちら ](https://github.com/linuxhw/EDID){target="blank"} を見つけてコピーします。

2. GL.iNet KVM コンソールにログインし、**Settings** -> **EDID** に移動します。 **Customize** モードに切り替え、パラメータを入力ボックスに貼り付け、**Set Custom** をクリックして設定を適用します。

    ![edid customize](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_customize.png){class="glboxshadow"}

!!! note

    1. 解像度は 2560×1440@60Hz を超えてはなりません。たとえば、2560×1600@60Hz の解像度はサポートされていません。
    2. サポートされる最大リフレッシュ レートは 60Hz です。 1920x1080 を超える解像度の場合は、60FPS 以下のフレーム レートが推奨されます。
    3. インターレース解像度を含めないでください。そうしないと、画像が異常に表示されます。
    4. 入力 EDID コード ブロックは 2 を超えてはなりません。
    5. 基本的なオーディオ サポートが必要です。そうしないと、被制御デバイスでサウンド カードが選択できなくなり、音が出なくなる可能性があります。 

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
