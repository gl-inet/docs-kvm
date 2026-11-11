# リモート会議で双方向オーディオを使うにはどうすればよいですか？ {#how-can-i-use-two-way-audio-for-remote-meetings}

在宅勤務中は、KVMでオフィスのコンピューターにアクセスし、Zoom、Microsoft Teamsなどのアプリで音声会議に参加できます。GL.iNet KVMの双方向オーディオ機能を使うと、ローカルコンピューターのマイクで話し、そのスピーカーやヘッドホンで他の参加者の声を聞くことができます。

## クイックセットアップ {#quick-setup}

Zoomの会議を例に、リモート会議でローカルデバイスのマイクとスピーカーを使う手順を説明します。

1. 会議に参加する前に、制御側コンピューターでKVMにログインし、**Session** -> **Audio & Camera** に移動します。**Speaker** と **Microphone** を有効にし、右下の両方のアイコンが有効になっていることを確認します。

    ![スピーカーとマイクを有効にする](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/enable-speaker-and-microphone.png){class="glboxshadow"}

    例えば、**Microphone** を有効にすると、ブラウザーからマイクへのアクセス許可を求められる場合があります。使用するマイクを選択し、アクセスを許可します。

    ![マイクへのアクセス許可ダイアログ](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/microphone-permission-popup.png){class="glboxshadow"}

2. 被制御コンピューターでZoomを開き、会議に参加します。オーディオボタンの横にある矢印をクリックし、例に示すように次のデバイスを選択します。

    - **Microphone**: Microphone (6-Comet Microphone)

    - **Speaker**: EPSON PJ (HD Audio Driver for Display Audio)

    ![マイクとスピーカーを選択する](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/select-microphone-and-speaker.png){class="glboxshadow"}

    他の参加者と話すには、マイクのミュートを解除します。他の参加者の声は、制御側コンピューターのスピーカーまたはヘッドホンで聞くことができます。

    ローカルカメラの映像も参加者と共有する場合は、[カメラパススルーのガイド](../faq/use_camera_passthrough_for_remote_meetings.md)を参照してください。

## トラブルシューティング {#troubleshooting}

??? note "他の参加者に自分の声が聞こえない場合はどうすればよいですか？"

    被制御コンピューターで **Settings** -> **System** -> **Sound** に移動し、**Input** にKVMの仮想マイクがあるか確認します。この例では **Comet Microphone** と表示されます。会議アプリでもこのマイクが選択されていることを確認します。

    ![入力を確認する](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-input.png){class="glboxshadow"}

    - KVMの仮想マイクが表示されない場合は、KVMと被制御コンピューター間のUSBデータ接続を確認します。マイクの音声は、この接続を通じて被制御コンピューターに送信されます。

    - KVMの仮想マイクが表示され、選択されていても音声が入力されない場合は、制御側コンピューターと被制御コンピューター上の会議アプリの両方で、マイクのミュートが解除されていることを確認します。制御側コンピューターのシステムとブラウザーでマイクの権限を確認し、マイクを使用している可能性がある他のアプリやブラウザータブを閉じます。

??? note "他の参加者の声が聞こえない場合はどうすればよいですか？"

    被制御コンピューターで **Settings** -> **System** -> **Sound** に移動し、**Output** にKVMに接続されているHDMI音声出力があるか確認します。この例では **EPSON PJ** と表示されます。会議アプリで同じデバイスがスピーカーとして選択されていることを確認します。

    ![出力を確認する](https://static.gl-inet.com/docs/kvm/faq/how_to_use_audio_passthrough_for_remote_mettings/check-output.png){class="glboxshadow"}

    - HDMI音声出力が表示されない場合は、被制御コンピューターとKVM間のHDMI接続を確認します。被制御コンピューターの音声は、この接続を通じて送信されます。HDMIアダプターを使用している場合は、音声に対応していることを確認します。

    - HDMI音声出力が表示され、選択されていても他の参加者の声が聞こえない場合は、制御側コンピューター、ブラウザータブ、スピーカーまたはヘッドホンがミュートされていないことを確認します。

    詳しくは、[被制御デバイスから音声が出ない場合](../faq/no_audio_from_the_controlled_device.md)を参照してください。

??? note "ページの再読み込みや再接続の後に音声が途切れた場合はどうすればよいですか？"

    KVMコンソールで **Speaker** と **Microphone** を再確認します。ブラウザーのセキュリティポリシーにより、ページの再読み込みや再接続の後にスピーカーでの再生が無効になったり、マイクがミュートされたりすることがあります。

    詳しくは、[スピーカーとマイクの設定を維持できない場合](../faq/speaker_microphone_settings_cannot_be_retained.md)を参照してください。

??? note "「Microphone Access Denied」と表示された場合はどうすればよいですか？"

    制御側コンピューターで以下を確認します。

    - **システムの権限**：Windows 11で **Settings** -> **Privacy & security** -> **Microphone** に移動します。**Microphone access**、**Let apps access your microphone**、**Let desktop apps access your microphone** をオンにします。

    - **ブラウザーの権限**：KVMのウェブサイトによるマイクへのアクセスを許可します。以前にアクセスをブロックした場合は、そのサイトのマイクの権限を更新してページを再読み込みします。

    - **マイクの使用状況**：マイクを使用している可能性がある他のアプリやブラウザータブを閉じます。

    確認が完了したら、KVMコンソールで **Microphone** を再度有効にします。

---

まだ質問がありますか？ [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
