# Comet (GL-RM1) V1/V2 クイックセットアップ

このビデオを見るか、以下の手順に従って Comet をセットアップしてください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/JDgflRaIHw0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## デバイスを接続する

明確にするために、デバイス A は制御側デバイスを指し、デバイス B は制御側デバイスを指します。

![connect devices](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/01_device_distinction.jpg){class="glboxshadow"}

1. Comet を電源に接続します。

    ![power on](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/02_power-on.jpg){class="glboxshadow"}

2. HDMI ケーブルを使用して、Comet の HD IN ポートをデバイス B の HD OUT ポートに接続します。

    ![Connect the HD cable](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/03_hdmi.jpg){class="glboxshadow"}

3. USB ケーブルを使用して、Comet の USB デバイス ポートをデバイス B の USB ポートに接続します。

    ![Connect the USB port](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/04_usb-cable.jpg){class="glboxshadow"}

4. Comet のイーサネット ポートをネットワーク ソースに接続します。

    ![Connect to network](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm1/quick_setup/05_ethernet.jpg){class="glboxshadow"}

5. デバイスの接続が完了しました。これで、Comet のコンソールにローカルまたはリモートでアクセスできるようになりました。

## ローカル アクセス

ローカル ネットワーク上で Comet にアクセスするには、ドメイン名または IP アドレスを使用する 2 つの方法があります。

アクセスする前に、制御側デバイスが Comet と同じ LAN 上にあることを確認してください。

### ドメイン

1. 制御側デバイスでブラウザを起動します。互換性を高めるために Chrome または Edge をお勧めします。

2. アドレスバーに「`glkvm.local`」と入力します。 GLKVM ログイン ページが表示されます。管理者パスワードを入力します。

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    **Note**: 初めてアクセスするときは、管理者パスワードを設定する必要があります。

3. これで、Comet のコンソールにローカルでアクセスし、被制御デバイスにアクセスできるようになります。

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

### IP アドレス

1. 上位ルーターで Comet の IP アドレスを見つけます。

    たとえば、Comet は、イーサネット ケーブルを介して GL.iNet ルーター GL-AXT1800 の LAN ポートに接続されています。
    
    GL-AXT1800 Web 管理パネルにログインし、以下に示すように、クライアント リストで Comet の IP アドレスを見つけます。

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

2. ブラウザで新しいタブを開き、アドレスバーにCometのIPを入力します。 GLKVM ログイン ページが表示されます。管理者パスワードを入力します。

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    **Note**: 初めてアクセスするときは、管理者パスワードを設定する必要があります。

3. これで、Comet のコンソールにローカルでアクセスし、被制御デバイスにアクセスできるようになります。

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

## リモート アクセス

Comet にリモートでアクセスするには、クラウド サービス、GLKVM アプリ、Tailscale、ZeroTier、NetBird 経由など、複数の方法があります。

### クラウド サービス

1. デバイスを KVM クラウドにバインドします。これはローカル ネットワーク上で行う必要があります。 

    KVM をクラウドにバインドするには、通常のバインドと動的コード バインドの 2 つの方法があります。ここでは例として通常のバインドを取り上げます。動的コード バインディングを希望する場合は、[ここ](../../tutorials/how_to_bind_kvm_to_the_cloud_via_dynamic_code.md){target="_blank"} をクリックして詳細を確認してください。
    
    まず、ローカルで Comet にアクセスし、右上隅の **Cloud Service** に移動します。 「**Bind To Cloud**」をクリックします。

    ![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

    ログイン ページにリダイレクトされます。 glinet クラウド アカウントでログインします。 

    ![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

    次に、デバイス情報を確認し、**Bind** をクリックします。

    ![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

    少し待つと、デバイスがアカウントに正常にバインドされます。 「**Done**」をクリックします。

    ![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}
    
2. クラウドサービス経由のリモートアクセス。

    ブラウザを開き (Google Chrome を例にします)、アドレス バーに「`glkvm.com`」と入力します。ログインページが表示されます。 glinet アカウントを使用してログインします。

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

    ログイン後、アカウントにバインドされているデバイスが表示されます。リモートアクセスしたいデバイスをクリックします。

    ![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

    新しく開いた Web ページで、管理者パスワードを入力してログインします。

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    これにより、アプリをインストールせずに、クラウド経由で KVM と被制御デバイスにリモート アクセスできるようになります。

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
    
        これはローカル ネットワークで行う必要があります。制御側デバイスが Comet と同じ LAN 上にあることを確認してください。
    
        「**Auto Discover**」をクリックします。自動的に検索が始まります。
    
        ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}
        
        KVM を見つけて、そのデバイス ID を入力してアカウントにバインドします。
    
        ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}
    
    ??? "S/N Code"
    
        これは、KVM が検出されないか、同じ LAN 上にないが、シリアル番号 (S/N) はわかっているというシナリオに当てはまります。
        
        「**S/N Code**」をクリックします。ポップアップ ウィンドウで、デバイス名をカスタマイズし、KVM デバイスのラベル下部に印刷されている S/N を入力します。
    
        ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}
    
    ??? "Dynamic Binding Code"
    
        これはローカル ネットワークで行う必要があります。制御側デバイスが Comet と同じ LAN 上にあることを確認してください。
    
        1. ドメインまたは IP アドレスを使用して、ローカルで KVM にログインします。詳細は[こちら](../../faq/local_access_via_browser.md)をクリックしてください。 
    
        2. 右上隅の **Cloud Service** に移動し、**Bind With Code** をクリックします。 
    
            ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}
    
        3. デバイス バインド用の 8 桁の動的コードがランダムに生成され、60 秒間有効です。コードをクリックしてコピーします。
    
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

Comet は Tailscale と統合され、Tailscale 仮想ネットワーク経由でリモート アクセスできるようになります。

Comet のコンソールで、**Apps Center** -> **Tailscale** に移動し、有効にして、Comet を Tailscale アカウントにバインドします。 

次に、制御側デバイスを同じアカウントにバインドします。その後、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **Tailscale 仮想 IP** を入力することで、Comet にリモート アクセスできるようになります。

詳細は[こちら](../../faq/remote_access_via_tailscale.md){target="_blank"}をご参照ください。

### ZeroTier

Comet は ZeroTier と統合され、ZeroTier 仮想ネットワーク経由でリモート アクセスできるようになります。

Comet のコンソールで、**Apps Center** -> **ZeroTier** に移動して有効にします。

次に、Comet と制御側デバイスの両方を同じ ZeroTier ネットワーク (16 文字の英数字のネットワーク ID を使用) に参加させます。その後、GLKVM をインストールせずに、制御側デバイスの Web ブラウザーに **ZeroTier IP** を入力することで、Comet にリモート アクセスできます。アプリ。

詳しくは[こちら](../../faq/remote_access_via_zerotier.md){target="_blank"}をご覧ください。

### NetBird

Comet は NetBird と統合されており、NetBird 仮想ネットワーク経由でリモート アクセスできるようになります。 

Comet のコンソールで、**Apps Center** -> **NetBird** に移動し、有効にして、Comet を NetBird アカウントにバインドします。 

次に、制御側デバイスを同じアカウントにバインドします。その後、GLKVM アプリをインストールしなくても、制御側デバイスの Web ブラウザーに **NetBird 仮想 IP** を入力することで、Comet にリモート アクセスできるようになります。

詳細は[こちら](../../faq/remote_access_via_netbird.md){target="_blank"}をご参照ください。
