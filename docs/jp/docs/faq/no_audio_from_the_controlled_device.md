# 被制御デバイスから音声が聞こえない場合はどうすればよいですか

KVM と被制御デバイスを接続した後、被制御デバイスから音声が聞こえない場合 (デバイスでビデオを再生するときに音が出ないなど)、トラブルシューティングのヒントをいくつか示します。

1. KVM コンソールでスピーカーが有効になっていることを確認します。

    KVM コンソールで、**Settings** -> **Remote Device Settings** -> **Speaker** に移動し、スピーカーが有効になっていることを確認します。その間、右下隅のアイコンが点灯していることを確認します (アクティブであることを示します)。

    ![speaker](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/speaker.png){class="glboxshadow"}

2. KVM と被制御デバイスの間のすべてのケーブルがしっかりと接続されていることを確認します。配線が緩んでいると音声出力に影響を与える可能性があります。

3. HDMIコンバーターが接続されているか確認してください。一部のコンバーターはオーディオをサポートしていません。

    一部の古い標準の HDMI ケーブルは音声伝送をサポートしていない可能性があるため、同梱の HDMI ケーブルを使用することをお勧めします。

4. ホスト機器と被制御デバイスがミュートに設定されているか確認してください。

5. 被制御デバイスの出力設定を確認し、出力デバイスが **GLKVM** であることを確認します。

    ??? "macOS"

        被制御デバイスで、**Settings** -> **Sound** -> **出力と入力** -> **Output** に移動し、出力デバイスを **GLKVM** に切り替えます。

        ![mac output settings](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/mac_output_settings.png){class="glboxshadow"}

    ??? "Windows"

        被制御デバイスで、**Settings** -> **Sound** -> **Output** に移動し、出力デバイスを **GLKVM** に切り替えます。

        ![wins output settings 1](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_1.png){class="glboxshadow"}

        ![wins output settings 2](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_2.png){class="glboxshadow"}

        または、被制御デバイスの右下隅にあるサウンド アイコンをクリックし、再生デバイスを **GLKVM** として選択することもできます。

        ![wins output settings 3](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/wins_output_settings_3.png){class="glboxshadow"}

6. 被制御デバイスのグラフィックスカードドライバーを確認してください。被制御デバイスにグラフィックス カード ドライバーが搭載されていない場合、音声を出力できないため、制御側で音声を聞くことができません。

7. ホスト デバイスの詳細なサウンド設定を確認し、ブラウザにアクティブな音量出力があることを確認してください。 

    以下は、参考として Windows 10 Pro の詳細なサウンド設定の例です。

    **Settings** -> **Sound** -> **高度なサウンド オプション** に移動します。

    ![advanced sound options](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/advanced_sound_options.png){class="glboxshadow"}

    特定のアプリやシステムサウンドの音量を調整します。

    ![app volume](https://static.gl-inet.com/docs/kvm/faq/cannot_hear_audio/app_volume.png){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
