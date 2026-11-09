# ローカルカメラをリモート会議で共有するにはどうすればよいですか？（Camera Passthrough） {#how-can-i-share-the-local-camera-with-remote-meetings-camera-passthrough}

**注**: この機能はファームウェアv1.10.0で導入され、WebRTC (FEC) モードでのみサポートされています。現在、Webブラウザーとデスクトップクライアントで利用できますが、モバイルアプリではまだサポートされていません。

---

在宅勤務中は、KVMでオフィスのコンピューターにアクセスし、Zoom、Microsoft Teamsなどのアプリでビデオ会議に参加できます。ただし、カメラには自分ではなくオフィスだけが映る場合があります。

GL.iNet KVMの **Camera** 機能を使用すると、自宅のコンピューターのカメラ映像を、仮想USBカメラとしてオフィスのコンピューターに送信できます。会議アプリでこのカメラを選択すると、オフィスのコンピューターのファイルやアプリケーションを共有しながら、他の参加者に自分の姿を見せることができます。

## クイックセットアップ {#quick-setup}

Zoomのビデオ会議を例に、以下の手順でCamera機能を使用します。

1. 会議に参加する前に、制御側コンピューターでKVMにログインし、**Session** -> **Audio & Camera** に移動します。Cameraを有効にしてから、カメラアイコンをクリックして開始します。

    ![enable camera 1](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera.png){class="glboxshadow"}

    Cameraを有効にする際にUSBリソースの制限に関するメッセージが表示された場合は、**Settings** -> **USB Devices** に移動し、使用していないUSBエミュレートデバイスを無効にしてリソースを確保します。その後、Cameraを有効にして再試行してください。

    ![enable camera 3](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-3.png){class="glboxshadow"}

    ブラウザーでカメラへのアクセスを求められる場合があります。使用するカメラを選択し、映像のプレビューを確認してアクセスを許可します。

    ![enable camera 2](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/enable-camera-2.png){class="glboxshadow"}

2. 被制御コンピューターでZoomを開き、会議に参加します。ビデオボタンの横にある矢印をクリックし、**UVC camera** を選択します。

    ![uvc-camera](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/uvc-camera.png){class="glboxshadow"}

    次にビデオをオンにすると、制御側デバイスのカメラ映像が他の参加者に表示されます。

    **注**: 会議中に滑らかで鮮明な映像を送信できるよう、安定したネットワーク接続を確保してください。

## トラブルシューティング {#troubleshooting}

??? note "カメラ映像が被制御コンピューターに届かない場合はどうすればよいですか？"

    被制御コンピューターがKVMの仮想カメラを認識しているか確認します。

    被制御コンピューターで **Settings** -> **Bluetooth & devices** -> **Cameras** に移動し、Connected camerasにUVC Cameraがあるか確認します。

    ![check camera settings](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/check-camera-settings.png){class="glboxshadow"}

    表示されない場合は、KVMと被制御コンピューター間のUSBデータ接続が外れているか、緩んでいる可能性があります。

??? note "KVMコンソールでCameraを有効にしたときに「Camera Access Denied」と表示された場合はどうすればよいですか？"

    ![camera access denied](https://static.gl-inet.com/docs/kvm/faq/use-camera-for-remote-meeting/camera-access-denied.png){class="glboxshadow"}

    制御側コンピューターで以下を確認します。

    - **カメラの使用可否**: カメラが接続され、動作していることを確認します。システムのカメラアプリでテストし、再試行する前にそのアプリを閉じます。

    - **システムの権限**: Windows 11でSettings -> Privacy & security -> Cameraに移動し、Camera access、Let apps access your camera、Let desktop apps access your cameraをオンにします。

    - **ブラウザーの権限**: KVMのウェブサイトによるカメラへのアクセスを許可します。以前にアクセスをブロックした場合は、ウェブサイトのカメラ権限を更新してページを再読み込みします。

    - **カメラの使用状況**: ZoomやMicrosoft Teamsなど、カメラを使用している可能性がある他のアプリやブラウザータブを閉じます。

    これらの確認後、KVMコンソールでCameraを再度有効にします。

---

まだ質問がありますか？ [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
