# デバイスを GLKVM アプリにバインドできなかった場合はどうすればよいですか

[GLKVM アプリ](https://www.gl-inet.com/app-rm/){target="_blank"} を使用すると、コントローラー デバイスから被制御デバイスへのリモート アクセスが可能になります。コントローラーデバイスにアプリをインストールし、GL.iNet KVM デバイスをバインドするだけで、いつでもどこでも制御側デバイスにリモートでアクセスできます。

ただし、さまざまな理由により、デバイスのバインドが失敗する可能性があります。

対応する解決策については、以下のエラー メッセージをクリックしてください。

??? "バインドに失敗しました。基本的な KVM デバイス情報を取得できません。"

    ![binding failed device info error](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_device_info_error.png){class="glboxshadow"}

    1. LEDの状態を確認してください。 LED が白色に点灯し、KVM デバイスがインターネットに接続されていることを確認します。
    2. KVM デバイスを再起動し、2 分間待ってから再度バインドしてみます。
    3. S/N コードでデバイスを追加する場合は、正しい S/N を入力してください。
    4. **Ping**コマンドでネットワークを確認するには、以下の手順に従います。

        1. 制御側デバイスを KVM と同じネットワークに接続します。

        2. 制御側デバイスでブラウザ (Chrome または Edge を推奨) を起動し、アドレス バーに `glkvm.local` と入力します。管理者パスワードを入力してログインします。

            ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. ログイン後、**Toolbox** -> **Terminal** に移動し、**Access** をクリックして端末にログインします。

            ![access terminal](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. `google.com` に Ping して、ネットワークのステータスを確認します。

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            ネットワークが正常に動作している場合は、次のような結果が得られます。

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            ネットワークが不安定または利用できない場合は、ISP またはルーターのサポートにお問い合わせください。

??? "デバイスのネットワーク エラー、バインドに失敗しました。"

    ![binding failed network error](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_network_error.png){class="glboxshadow"}

    1. LEDの状態を確認してください。 LED が白色に点灯し、KVM デバイスがインターネットに接続されていることを確認します。
    2. KVM デバイスを再起動し、2 分間待ってから再度バインドしてみます。
    3. クラウド サービスが有効になっていることを確認します。

        クラウド サービスはデフォルトで有効になっていますが、以前に手動で無効にしていた場合、GLKVM アプリへのデバイスの再バインドは失敗します。クラウド サービスを再度有効にするには、ドメインまたは IP アドレスを介して KVM デバイスにローカルにアクセスしてください。

    4. **Ping**コマンドでネットワークを確認するには、以下の手順に従います。

        1. 制御側デバイスを KVM と同じネットワークに接続します。

        2. 制御側デバイスでブラウザ (Chrome または Edge を推奨) を起動し、アドレス バーに `glkvm.local` と入力します。管理者パスワードを入力してログインします。

            ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

        3. ログイン後、**Toolbox** -> **Terminal** に移動し、**Access** をクリックして端末にログインします。

            ![access terminal](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/access_terminal.png){class="glboxshadow"}

        4. `google.com` に Ping して、ネットワークのステータスを確認します。

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_test.png){class="glboxshadow"}

            ネットワークが正常に動作している場合は、次のような結果が得られます。

            ![ping](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/ping_success.png){class="glboxshadow"}

            ネットワークが不安定または利用できない場合は、ISP またはルーターのサポートにお問い合わせください。

??? "バインドに失敗しました。KVM はすでに他のユーザーによってバインドされています。"

    ![binding failed bound by others](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_failed_bound_by_others.png){class="glboxshadow"}

    これは、KVM デバイスが別のアカウントにバインドされていることを意味します。

    1. 別のメール アドレスにバインドされているかどうかを確認してください。他のアカウントがあれば試してください。

    2. S/N コードでデバイスを追加する場合は、正しい S/N を入力してください。

??? "動的バインディング コードが正しくありません。残り 4 回の試行があります。"

    ![incorrect binding code](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_binding_code.png){class="glboxshadow"}

    これは、無効または期限切れのバインド コードを入力したことを意味します。

    1. ローカルで KVM 管理コンソールにログインし、右上隅の **Cloud Service** に移動して、**Bind with Code** をクリックして動的バインディング コードを取得します。

    2. GL-RM10 (Comet Pro) モデルの場合は、タッチスクリーンでもコードを取得できます。 **Cloud Service** 画面にスライドして **Generate Binding Code** をクリックすると、タッチスクリーンに動的バインディング コードが表示されます。このバインド コードを GLKVM アプリに入力して、バインドを完了します。

        ![generate binding code](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/binding_code_screen.png){class="glboxshadow"}

    3. バインド コードの有効期限が切れた場合は、**Regenerate** をクリックして新しいコードを取得します。

??? "デバイスIDが間違っています。残り 4 回の試行があります。"

    ![incorrect device id](https://static.gl-inet.com/docs/kvm/faq/failed_to_bind_device_to_glkvm_app/incorrect_device_id.png){class="glboxshadow"}

    これは、間違ったデバイス ID を入力したことを意味します。

    1. 正しいデバイス ID については、下部のラベルを確認してください。

    2. 下部のラベルを確認できない場合は、ローカル アクセス経由でデバイスをバインドしてみてください。

        KVM 管理コンソールにローカルでログインし、右上隅の **Cloud Service** に移動して、**Bind To KVM Cloud** をクリックします。その後、一意のトークンを含むバインディング ページにリダイレクトされます。 Cloudアカウントでログインし、デバイス情報を確認してバインドを完了します。

??? "他の"

    GLKVM アプリがインストールされている制御側デバイスで VPN が有効になっているかどうかを確認します。

    AstroWarp、Tailscale、ZeroTier などの VPN またはプロキシ ソフトウェアを無効にしてから、KVM を GLKVM アプリに再度バインドしてみてください。

問題が解決しない場合は、[support@gl-inet.com](mailto:support@gl-inet.com) までご連絡いただき、デバイス モデル、ファームウェア バージョン、MAC アドレスをお知らせください。
