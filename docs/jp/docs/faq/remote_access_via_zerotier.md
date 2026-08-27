# ZeroTier 経由で KVM にリモートでアクセスする方法

> 注: この機能を使用する前に、KVM ファームウェアを v1.8.0 にアップグレードしてください。

GL.iNet KVM は ZeroTier を統合し、リモート アクセスのために ZeroTier ネットワークにバインドできるようにします。GLKVM アプリをインストールしたり、クラウド サービスを使用したりする必要はありません。 

ZeroTier 経由で GL.iNet KVM にリモート アクセスするには、次の手順に従います。

## ZeroTier を有効にする

**始める前に、KVM と制御側デバイスを同じローカル ネットワークに接続してください。**

1. 制御側デバイスでブラウザを開きます。互換性を高めるために Chrome または Edge をお勧めします。
    
2. ドメインまたは IP アドレスを使用して、KVM コンソールにローカルでログインします。ここでは例としてローカル IP アドレスを使用します。

    KVM の **LAN IP アドレス** (タッチスクリーンまたはルーターに表示されます) をアドレス バーに入力します。 GLKVM ログイン ページが表示されます。管理者パスワードを入力します。

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/1_local_access.png){class="glboxshadow"}

3. ログイン後、**Apps Center** -> **ZeroTier** に進みます。 ZeroTier を有効にすると、以下に示すように黄色のプロンプトが表示されます。 

    ハイパーリンクまたは[ここ](https://my.zerotier.com/){target="_blank"}をクリックして、ZeroTier Central にサインインし、ZeroTier ネットワークを作成します。

    ![enable zerotier](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/2_enable_zerotier.png){class="glboxshadow"}
    
## KVM を ZeroTier にバインド

1. [ZeroTier](https://my.zerotier.com/){target="_blank"} に初めてサインインする場合は、ZeroTier Central を選択する必要がある場合があります。

    ![select central](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/3_select_central.png){class="glboxshadow"}

    適切なバージョンを選択して続行します。ここでは **New Central** を例として取り上げます。
    
    メールアドレスとパスワードを使用してサインインします。アカウントをお持ちでない場合は、まずサインアップしてください。

    ![zerotier signin](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/4_zerotier_signin.png){class="glboxshadow"}

2. サインイン後、組織を作成します。

    ![create organization](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/5_create_org.png){class="glboxshadow"}

3. プランを選択してください。ここでは例として、デバイス 10 台、ネットワーク管理者 1 人、ネットワーク 1 人を含む **Personal** プランを選択します。さらにネットワークを作成したり、デバイスを追加したり、カスタム ルートと DNS を追加したりする必要がある場合は、Essential プランまたは Scale プランを選択します。

    ![select plan](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/6_select_plan.png){class="glboxshadow"}

4. これで、ZeroTier ネットワークが作成されました。 16 文字の英数字文字列である **Network ID** をコピーします。これは、後で ZeroTier ネットワークにデバイスを追加するときに必要になります。このタブを開いたままにしてください。

    ![network id](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/7_copy_network_id.png){class="glboxshadow"}

5. KVM コンソールに戻り、**Apps Center** -> **ZeroTier** に移動します。 **Network ID** を見つけて、**Set** をクリックします。

    ![network id](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id1.png){class="glboxshadow"}

    ポップアップ ウィンドウで、**Network ID** を貼り付け、**Confirm** をクリックします。

    ![network id](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/8_set_network_id2.png){class="glboxshadow"}

    コンソールに黄色のプロンプトが表示され、このデバイスを認証する必要があることを示します。 

    ![authorize1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize1.png){class="glboxshadow"}

6. ZeroTier 中央に戻ります。承認を待っているデバイス (KVM) が表示されます。 「**Authorize**」をクリックします。

    ![authorize2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/9_authorize2.png){class="glboxshadow"}

    承認されると、以下に示すように、ステータスが緑色で承認済みに変わります。

    ![authorized1](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized1.png){class="glboxshadow"}

    KVM コンソールでは、以下に示すように、**Network ID** および **Virtual IP** も表示できます。

    ![authorized2](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/10_authorized2.png){class="glboxshadow"}

## 制御側デバイスをバインドする

以下の例は、Windows ラップトップ (制御側デバイスとして) を ZeroTier ネットワークにバインドする方法を示しています。

1. [こちら](https://www.zerotier.com/download/){target="_blank"}からラップトップにZeroTierをインストールします。 

2. ラップトップで ZeroTier を実行し、同じ ZeroTier ネットワークに追加します。 

    ZeroTier はデスクトップ上に別のウィンドウ/UI を表示しないことに注意してください。システム トレイ (右下隅) にアイコンとしてのみ存在します。すべての操作は右クリック メニューから実行されます。

    ZeroTier アイコンを右クリックし、**Join New Network** をクリックします。ポップアップ ウィンドウで同じ **Network ID** を入力して、この PC を同じ ZeroTier ネットワークに追加します。

    ![join network](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/11_pc_join_network.jpg){class="glboxshadow"}

    次に、ZeroTier Central に移動し、保留中のデバイスを罰金して承認します。

    ![authorize](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/12_authorize.png){class="glboxshadow"}

2. 承認されると、以下に示すように、ステータスが緑色で承認済みに変わります。

    ![authorized](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/13_authorized.png){class="glboxshadow"}

3. これで、KVM とラップトップの両方が同じ ZeroTier ネットワークに追加されました。以下に示すように、ネットワーク ID でわかります。

    ![same zt network](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/14_same_zt_network.png){class="glboxshadow"}

## ZeroTier 経由のリモート アクセス

以下の例は、ZeroTier IP アドレスを介して KVM コンソールにリモート アクセスする方法を示しています。

1. ラップトップで、自分のアカウントで ZeroTier Central にサインインし、KVM デバイスを見つけて、その **ZT IP** をクリックしてコピーします。

    ![zerotier ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/15_zerotier_ip.png){class="glboxshadow"}

2. 新しいブラウザー タブを開き、コピーした ZeroTier IP をアドレス バーに貼り付け、Enter キーを押します。 GLKVM ログイン ページにリダイレクトされます。 

    管理者パスワードを入力してログインします。これで、ZeroTier IP を介して、GL.iNet KVM および被制御デバイスにアクセスできるようになります。

    ![remote access](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_zerotier/16_remote_access.png){class="glboxshadow"}

    **Tip**: この ZeroTier IP に初めてアクセスすると、プライバシー エラーが表示される場合があります。 [**Advanced**] -> [**Proceed**] をクリックして続行します。詳細については、[ブラウザからのプライバシー エラー](privacy_error_from_your_browser.md){target="_blank"}を参照してください。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
