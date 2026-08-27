# Comet 5G (GL-RM10RC) クイックセットアップ

このビデオを見るか、以下の手順に従って Comet 5G をセットアップしてください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/whAUMBcIIZs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## デバイスを接続する

明確にするために、デバイス A は制御側デバイスを指し、デバイス B は制御側デバイスを指します。

![connect devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/connect_device.png){class="glboxshadow"}

1. SIM カードを Comet 5G に挿入し、電源を入れます。

    ![insert sim power on](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/01-insert-sim-power-on.jpg){class="glboxshadow"}

2. Comet 5G の HDMI IN ポートをデバイス B の HDMI ポートに接続します。必要に応じて、別の HDMI ケーブルを使用して、Comet 5G の HDMI OUT ポートを外部モニターに接続します。

    ![Connect the HDMI cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/02-hdmi-cable.jpg){class="glboxshadow"}

3. USB-C ケーブルを使用して、Comet 5G の Type-C ポートをデバイス B の Type-C インターフェイスに接続します。

    ![Connect the USB cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/03-usb-cable.jpg){class="glboxshadow"}

4. Comet 5G をネットワーク ソースに接続します。

    - 5G: SIM カードが挿入されている場合、システム起動時に 5G 接続が自動的に確立されます。

    - Wi-Fi: タッチスクリーンを左にスワイプし、Comet 5G を既存の Wi-Fi ネットワーク (2.4G および 5G をサポート) に接続します。

        ![Connect via wifi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/04-network-wifi.png){class="glboxshadow"}

    - イーサネット: Comet 5G のイーサネット ポートをネットワーク ソースに接続します。

        ![Connect via ethernet](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/04-network-ethernet.png){class="glboxshadow"}

    !!! note
        接続の優先順位は、**Ethernet** > **Wi-Fi** > **5G** です。 WAN ネットワーク検出とフェイルオーバーの完全なロジックについては、[**こちら**](../../faq/wan_network_detection_and_failover_logic_of_comet5g.md) を参照してください。

5. デバイスの接続が完了しました。これで、近くのコントロール、ローカル アクセス、またはリモート アクセスを介して Comet 5G のコンソールにアクセスできるようになります。

## 近くのコントロール

Nearby Control は、Comet 5G の近くにいるときの素早いセットアップと管理に最適です。

タッチスクリーンで、Wi-Fi ネットワーク モードを **AP Mode** に切り替えるだけで、一意の Wi-Fi SSID が生成され、ネットワークの詳細が画面に表示されます。

![nearby access](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/nearby_access1.png){class="glboxshadow gl-80-desktop"}

デバイスをこの Wi-Fi SSID に接続すると、Web ブラウザからデフォルトの IP アドレス (192.168.8.1) を介して Comet 5G のコンソールにアクセスできます。

![nearby access](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/quick_setup/nearby_access2.png){class="glboxshadow"}

## ローカル アクセス

ローカル ネットワーク上で Comet 5G にアクセスするには、ドメイン名または IP アドレスを使用する 2 つの方法があります。

アクセスする前に、制御側デバイスが Comet 5G と同じ LAN 上にあることを確認してください。

### ドメイン

1. 制御側デバイスでブラウザを起動します。互換性を高めるために Chrome または Edge をお勧めします。

2. アドレスバーに「`glkvm.local`」と入力します。 GLKVM ログイン ページが表示されます。管理者パスワードを入力します。

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Note**: 初めてアクセスするときは、管理者パスワードを設定する必要があります。

3. これで、Comet 5G のコンソールにローカルでアクセスし、被制御デバイスにアクセスできるようになります。

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### IP アドレス

1. タッチスクリーンで Comet 5G の IP アドレスを見つけます。この例では、Comet 5G の IP アドレスは `192.168.8.197` です。

2. ブラウザを起動し、アドレス バーにこの IP を入力します。 GLKVM ログイン ページが表示されます。管理者パスワードを入力します。

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Note**: 初めてアクセスするときは、管理者パスワードを設定する必要があります。

3. これで、Comet 5G のコンソールにローカルでアクセスし、被制御デバイスにアクセスできるようになります。

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## リモート アクセス

Comet 5G にリモートでアクセスするには、クラウド サービス、GLKVM アプリ、Tailscale、ZeroTier、NetBird 経由など、複数の方法があります。

### クラウド サービス

1. デバイスを KVM クラウドにバインドします。これはローカル ネットワーク上で行う必要があります。

    KVM をクラウドにバインドするには、通常のバインドと動的コード バインドの 2 つの方法があります。ここでは例として通常のバインドを取り上げます。動的コード バインディングを希望する場合は、[ここ](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} をクリックして詳細を確認してください。

    まず、ローカルで Comet 5G にアクセスし、右上隅の **Cloud Service** に移動します。 「**Bind To Cloud**」をクリックします。

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    ログイン ページにリダイレクトされます。 glinet クラウド アカウントでログインします。

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    次に、デバイス情報を確認し、**Bind** をクリックします。

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    少しお待ちください。Comet 5G がアカウントに正常にバインドされます。 「**Done**」をクリックします。

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

2. クラウドサービス経由のリモートアクセス。

    ブラウザを開き (Google Chrome を例にします)、アドレス バーに「`glkvm.com`」と入力します。ログインページが表示されます。 glinet アカウントを使用してログインします。

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    ログイン後、アカウントにバインドされているデバイスが表示されます。リモートアクセスしたいデバイスをクリックします。

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    新しく開いた Web ページで、管理者パスワードを入力してログインします。

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    これで、アプリをインストールしなくても、Comet 5G と制御対象のデバイスにクラウド経由でリモートからアクセスできるようになります。

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

### GLKVM アプリ

1. [GLKVM アプリ](https://www.gl-inet.com/app-rm/){target="_blank"} を制御側デバイスにインストールします。

2. GL.iNet アカウントでログインします。

    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    お持ちでない場合は、まずサインアップしてログインしてください。

    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

3. デバイスをバインドします。

    ログイン後、以下のページが表示されます。 「**Add Device**」をクリックします。

    ![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

    自動検出、S/N コード、動的バインディング コードの 3 つの方法でデバイスをバインドできます。

    ??? "Auto Discover"

        これはローカル ネットワークで行う必要があります。制御側デバイスが Comet 5G と同じ LAN 上にあることを確認してください。

        「**Auto Discover**」をクリックします。自動的に検索が始まります。

        ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

        KVM を見つけて、そのデバイス ID を入力してアカウントにバインドします。

        ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

    ??? "S/N Code"

        これは、KVM が検出されないか、同じ LAN 上にないが、シリアル番号 (S/N) はわかっているというシナリオに当てはまります。

        「**S/N Code**」をクリックします。ポップアップ ウィンドウで、デバイス名をカスタマイズし、KVM デバイスのラベル下部に印刷されている S/N を入力します。

        ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        これはローカル ネットワークで行う必要があります。制御側デバイスが Comet 5G と同じ LAN 上にあることを確認してください。

        1. ドメインまたは IP アドレスを使用して、ローカルで KVM にログインします。詳細は[こちら](../../faq/local_access_via_browser.md)をクリックしてください。

        2. 右上隅の **Cloud Service** に移動し、**Bind With Code** をクリックします。

            ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

        3. デバイス バインド用に 8 桁の動的コードがランダムに生成され、有効期間は 60 秒です。コードをクリックしてコピーします。

            ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

        4. GLKVM アプリに戻り、動的バインディング コードを入力して、**Bind** をクリックします。

            ![dynamic code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

4. GLKVM アプリ経由のリモート アクセス。

    KVM デバイスがアカウントにバインドされると、アプリに「オンライン」と表示されます。

    ![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

    KVM デバイスをクリックします。新しいウィンドウが開き、接続が開始されます。

    ![connecting](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

    接続したら、管理者パスワードを入力してデバイスにログインします。

    ![connected log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

    その後、KVM デバイスにアクセスし、これを通じて制御対象のデバイスにアクセスできます。

    ![connected access](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

### Tailscale

Comet 5G は Tailscale と統合されており、Tailscale 仮想ネットワーク経由でリモート アクセスできるようになります。

コンソールで、**Apps Center** -> **Tailscale** に移動し、有効にして、Comet 5G を Tailscale アカウントにバインドします。

次に、制御側デバイスを同じアカウントにバインドします。その後、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **Tailscale 仮想 IP** を入力することで、Comet 5G にリモート アクセスできるようになります。

詳細は[こちら](../../faq/remote_access_via_tailscale.md){target="_blank"}をご参照ください。

### ZeroTier

Comet 5G は ZeroTier と統合されており、ZeroTier 仮想ネットワーク経由でリモート アクセスできるようになります。

コンソールで、**Apps Center** -> **ZeroTier** に移動し、有効にします。

次に、Comet 5G と制御側デバイスの両方を同じ ZeroTier ネットワークに参加させます (16 文字の英数字のネットワーク ID を使用)。その後、GLKVM アプリをインストールせずに、制御側デバイスの Web ブラウザーに **ZeroTier IP** を入力することで、Comet 5G にリモート アクセスできます。

詳細は[こちら](../../faq/remote_access_via_zerotier.md){target="_blank"}をご参照ください。

### NetBird

Comet 5G は NetBird と統合されており、NetBird 仮想ネットワーク経由でリモート アクセスできるようになります。

コンソールで、**Apps Center** -> **NetBird** に移動し、有効にして、Comet 5G を NetBird アカウントにバインドします。

次に、制御側デバイスを同じアカウントにバインドします。その後、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **NetBird 仮想 IP** を入力することで、Comet 5G にリモート アクセスできるようになります。

詳細は[こちら](../../faq/remote_access_via_netbird.md){target="_blank"}をご参照ください。
