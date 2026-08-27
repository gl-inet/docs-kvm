# マウス カーソルの位置が合わない場合はどうすればよいですか

制御側デバイスのマウス カーソルが制御側デバイスのマウス カーソルと一致しない場合は、以下のトラブルシューティング手順に従ってください。

![cursor misalignment](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/mouse_cursor.png){class="glboxshadow"}

1. **マウスの移動時に問題が発生するか、アイドル時に発生するかを確認します。**

    <u>ケース1</u>。マウスがアイドル状態のときはカーソルが正しく位置合わせされているが、移動中に同期が失われる場合は、両端のネットワークをチェックして、接続が安定していることを確認してください。

    さらに、ローカル カーソルを非表示にして、コントロール画面にリモート カーソルのみが表示されるようにして、カーソルの位置ずれの問題を防ぐことができます。

    KVM コンソールで、**Settings** -> **Remote Device Settings** -> **Show Local Cursor** に移動して無効にします。

    ![hide local cursor](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/hide_local_cursor.jpg){class="glboxshadow"}

    <u>ケース2</u>。マウスがアイドル状態でもカーソルの位置が合わない場合は、KVM コンソールでデバイス タイプを再選択してください (Comet Q / GL-RMQ1 のみ)。

    ![device type](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/device_type.png){class="glboxshadow"}

    問題が解決しない場合は、次の手順に進みます。

2. **被制御デバイスがラップトップの場合、これはディスプレイ解像度が正しくないことが原因である可能性があります。**

    ラップトップの画面アスペクト比を確認し、制御されているラップトップの解像度を調整するか、KVM デバイスの EDID 設定を変更できます。

    ??? note "制御されているラップトップの解像度を調整する"

        **macOS の場合**:

        1. **Settings** -> **Displays** -> **Optimize for** に進みます。

            ![mac displays](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos1.png){class="glboxshadow" width="582"}

        2. **GLKVM**に変更します。

            ![select glkvm](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos2.png){class="glboxshadow" width="582"}

        3. 対応する解像度を選択し、マウス カーソルを重ねることができるかどうかを確認します。

            ![resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos3.png){class="glboxshadow"}

        **For Windows**:

        1. **Settings** -> **System** -> **Displays** に進みます。

            ![windows display](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows1.png){class="glboxshadow"}

        2. 下にスクロールして **ディスプレイ解像度** を見つけ、右側のボックスをクリックします。

            ![display resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows2.png){class="glboxshadow"}

        3. 適切なディスプレイ解像度を選択し、ポップアップ ウィンドウで **変更を維持** をクリックして適用します。

            ![display resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows3.png){class="glboxshadow"}

            ![display resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows4.png){class="glboxshadow"}

    ??? note "KVM デバイスの EDID 設定を変更します"

        EDID (Extended Display Identification Data) は、最適なディスプレイ パラメーターを自動的に照合します。デフォルトの EDID はほとんどのシナリオに適しており、通常は変更する必要はありません。詳細は[こちら](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}をご参照ください。

        EDIDを変更しても画面が更新されない場合は、制御対象機器を再起動してみてください。

3. **制御されるデバイスがラップトップではない場合 (例: 外部モニターに接続されたデスクトップ PC)**、プライマリ ディスプレイ アスペクト比を確認し、それに応じて EDID を KVM に切り替えます。詳細は[こちら](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"}をご覧ください。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
