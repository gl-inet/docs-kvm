# Comet X (GL-RM4PE) クイックセットアップ

## デバイスを接続する

明確にするために、デバイス A は制御側デバイスを指し、デバイス B は制御側デバイスを指します。

![connect1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect1.png){class="glboxshadow"}

1. イーサネット ケーブルを使用して Comet X を PoE スイッチに接続するか、5V/3A 電源アダプターで電力を供給します。

    ![connect2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect2.png){class="glboxshadow"}

    ***Note**: 電源アダプターを使用して電源を供給する場合は、インターネット アクセス用のイーサネット ケーブルを介して Comet X をネットワーク デバイス (ルーターなど) に接続します。

2. HDMI ケーブルを使用して、Comet X の **HDMI IN** ポートをデバイス B に接続します。これにより映像信号の伝送が可能となります。

    ![connect3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect3.png){class="glboxshadow"}

3. USB ケーブルを使用して、Comet X の **USB-C** ポートをデバイス B に接続します。キーボードとマウスの信号を適切に送信するには、この USB-C ポートを対応する HDMI IN ポートとペアにする必要があります。

    ![connect4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/connect4.png){class="glboxshadow"}

4. (オプション) Comet X の **HDMI OUT** ポートを外部モニターに接続して、ディスプレイを複製します (ビデオ ループアウト)。詳細については、[ローカルコントロール](#local-control)を参照してください。

5. 接続が完了しました。これで、Comet X のコンソールにローカルまたはリモートでアクセスできるようになりました。

## ラックマウント

必要に応じて、Comet X をサーバー ラック レールに取り付けます。

1. 付属のネジを使用して、取り付けブラケットをComet Xに取り付けます。

    ![install1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install1.png){class="glboxshadow"}

2. Comet X をラック ネジでラック レールに固定します。 **ラックネジは付属しません**。

    ![install2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/install2.png){class="glboxshadow"}

## ローカルコントロール

物理ケーブル経由でデバイスを直接制御します。ネットワーク、IP アドレス、ドメイン名は必要ありません。

Comet X は、HDMI OUT ポートと 2 つの追加の USB ポートを備えており、ローカルのトラブルシューティング、構成、OS のインストールに最適です。モニター、マウス、キーボードを接続するだけで、プラグアンドプレイのローカルハードウェア制御が可能になります。

1. Comet X の背面パネルの **HDMI OUT** ポートを外部モニターに接続して、ディスプレイを複製します (ビデオ ループアウト)。

    ![local control1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control1.png){class="glboxshadow"}

2. キーボードとマウスを前面パネルの Comet X の USB ポートに接続します。

    ![local control2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_control2.png){class="glboxshadow"}

3. ビデオ信号がローカル モニターにループアウトされている間、ローカルのキーボードとマウスで接続されたデバイスを制御できるようになりました。

## LAN アクセス

ローカル ネットワーク上で Comet X にアクセスするには、ドメイン名または IP アドレスを使用する 2 つの方法があります。

アクセスする前に、制御側デバイスが Comet X と同じ LAN 上にあることを確認してください。

### ドメイン

1. 制御側デバイスでブラウザを起動します。互換性を高めるために Chrome または Edge をお勧めします。

2. アドレスバーに「`glkvm.local`」と入力します。 GLKVM ログイン ページが表示されます。管理者パスワードを入力します。

    ![local access via domain](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain1.png){class="glboxshadow"}

    ***Note**: 初めてアクセスするときは、管理者パスワードを設定する必要があります。*

3. これで、Comet X のコンソールにローカルでアクセスし、被制御デバイスにアクセスできるようになります。

    ![local access via domain](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_domain2.png){class="glboxshadow"}

### IP アドレス

1. タッチスクリーンで Comet X の IP アドレスを見つけます。この例では、Comet X の IP アドレスは `192.168.8.197` です。

2. ブラウザを起動し、アドレス バーにこの IP を入力します。 GLKVM ログイン ページが表示されます。管理者パスワードを入力します。

    ![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip1.png){class="glboxshadow"}

    ***Note**: 初めてアクセスするときは、管理者パスワードを設定する必要があります。*

3. その後、Comet X のコンソールにローカルでアクセスし、被制御デバイスにアクセスできるようになります。

    ![local access via ip](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/local_ip2.png){class="glboxshadow"}

## リモート アクセス

Comet X にリモートでアクセスするには、クラウド サービス、GLKVM アプリ、Tailscale、ZeroTier 経由など、複数の方法があります。

### クラウド サービス

1. デバイスを KVM クラウドにバインドします。これはローカル ネットワーク上で行う必要があります。

    KVM をクラウドにバインドするには、通常のバインドと動的コード バインドの 2 つの方法があります。ここでは例として通常のバインドを取り上げます。動的コード バインディングを希望する場合は、[ここ](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} をクリックして詳細を確認してください。

    まず、ローカルで Comet X にアクセスし、右上隅の **Cloud Service** に移動します。 「**Bind To KVMCloud**」をクリックします。

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_to_cloud.png){class="glboxshadow"}

    ログイン ページにリダイレクトされます。 glinet クラウド アカウントでログインします。

    ![cloud bind device1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind1.png){class="glboxshadow"}

    次に、デバイス情報を確認し、**Bind** をクリックします。

    ![cloud bind device2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind2.png){class="glboxshadow"}

    ちょっと待ってください。 Comet X はアカウントにバインドされます。 「**Done**」をクリックします。

    ![cloud bind device success](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_bind_success.png){class="glboxshadow"}

2. クラウドサービス経由のリモートアクセス。

    「完了」をクリックすると、ドメイン `glkvm.com` のサイトにリダイレクトされ、デバイスが表示されます。

    ![cloud devices list](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_devices.png){class="glboxshadow"}

    ***Tip**: リダイレクトされない場合は、アドレス バーに `glkvm.com` を手動で入力し、glinet アカウントにログインします。ログイン後、デバイスがアカウントにバインドされていることがわかります。*

    リモート アクセスするデバイスをクリックします。

    ![cloud access](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access.png){class="glboxshadow"}

    新しい Web ページが開きます。管理者パスワードを入力してログインします。

    ![cloud access1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access1.png){class="glboxshadow"}

    これで、Comet X と被制御デバイスにクラウド経由でリモートからアクセスできるようになります。

    ![cloud access2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/cloud_access2.png){class="glboxshadow"}

### GLKVM アプリ

1. [GLKVM アプリ](https://www.gl-inet.com/app-rm/){target="_blank"} を制御側デバイスにインストールします。

2. GL.iNet アカウントでログインします。

    ![log in](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_login.jpg){class="glboxshadow"}

    お持ちでない場合は、まずサインアップしてログインしてください。

    ![sign up](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_signup.png){class="glboxshadow"}

3. デバイスをバインドします。

    ログイン後、以下のページが表示されます。 「**Add Device**」をクリックします。

    ![add device](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_add_device.png){class="glboxshadow"}

    自動検出、S/N コード、動的バインディング コードの 3 つの方法でデバイスをバインドできます。

    ??? "Auto Discover"

        これはローカル ネットワークで行う必要があります。制御側デバイスが Comet X と同じ LAN 上にあることを確認し、KVM デバイス ID を用意してください。

        「**Auto Discover**」をクリックします。検索が始まります。

        ![auto discover 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover1.png){class="glboxshadow"}

        KVM を見つけて、その **Device ID** を入力してアカウントにバインドします。

        ![auto discover 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover2.png){class="glboxshadow"}

        ![auto discover 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/auto_discover3.png){class="glboxshadow"}

    ??? "S/N Code"

        これは、KVM が検出されないか、同じ LAN 上にないが、シリアル番号 (S/N) はわかっているというシナリオに当てはまります。

        「**S/N Code**」をクリックします。ポップアップ ウィンドウでデバイス名を設定し、KVM デバイスの下部に印刷されている S/N を入力します。

        ![sn code](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/add_sncode.png){class="glboxshadow"}

    ??? "Dynamic Binding Code"

        これはローカル ネットワークで行う必要があります。制御側デバイスが Comet X と同じ LAN 上にあることを確認してください。

        1. ドメインまたは IP アドレスを使用して、ローカルで KVM にログインします。詳細は[こちら](#lan-access)をクリックしてください。

        2. 右上隅の **Cloud Service** に移動し、**Bind With Code** をクリックします。

            ![bind with code 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code1.png){class="glboxshadow"}

        3. デバイス バインド用に 8 桁の動的コードがランダムに生成され、60 秒間有効です。コードをクリックしてコピーします。

            ![bind with code 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code2.png){class="glboxshadow"}

        4. GLKVM アプリに戻り、動的バインディング コードを入力して、**Bind** をクリックします。

            ![dynamic code](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/bind_with_code3.png){class="glboxshadow"}

4. GLKVM アプリ経由のリモート アクセス。

    KVM デバイスがアカウントにバインドされると、アプリに「オンライン」と表示されます。

    ![app device online](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_devices.png){class="glboxshadow"}

    KVM デバイスをクリックします。新しいウィンドウが開き、接続が開始されます。

    ![app connecting](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_connecting.png){class="glboxshadow"}

    接続したら、管理者パスワードを入力してデバイスにログインします。

    ![app access1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access1.png){class="glboxshadow"}

    その後、KVM デバイスにアクセスし、これを通じて制御対象のデバイスにアクセスできます。

    ![app access2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm4pe/quick_setup/app_access2.png){class="glboxshadow"}

### Tailscale

Comet X は Tailscale と統合され、Tailscale 仮想ネットワーク経由でリモート アクセスできるようになります。

コンソールで、**Apps Center** -> **Tailscale** に移動し、有効にして、Comet X を Tailscale アカウントにバインドします。

次に、制御側デバイスを同じアカウントにバインドします。その後、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **Tailscale 仮想 IP** を入力することで、Comet X にリモート アクセスできるようになります。

詳しくは[こちら](../../faq/remote_access_via_tailscale.md){target="_blank"}をご覧ください。

### ZeroTier

Comet X は ZeroTier と統合されており、ZeroTier 仮想ネットワーク経由でリモート アクセスできるようになります。

コンソールで、**Apps Center** -> **ZeroTier** に移動し、有効にします。

次に、Comet X と制御側デバイスの両方を同じ ZeroTier ネットワーク (16 文字の英数字のネットワーク ID を使用) に参加させます。その後、GLKVM をインストールせずに、制御側デバイスの Web ブラウザーに **ZeroTier IP** を入力することで、Comet X にリモート アクセスできます。アプリ。

詳しくは[こちら](../../faq/remote_access_via_zerotier.md){target="_blank"}をご覧ください。
