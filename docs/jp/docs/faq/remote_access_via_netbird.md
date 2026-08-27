# NetBird 経由で KVM にリモートでアクセスする方法

> 注: この機能を使用する前に、KVM ファームウェアを v1.9.0 にアップグレードしてください。

[NetBird](https://netbird.io/){target="_blank"} は、家庭用およびビジネス用の安全なプライベート ネットワークを構築できるオープンソースのゼロトラスト ネットワーキング プラットフォームです。 WireGuard® ベースのオーバーレイ ネットワークとして、NetBird は、いつでもどこでもデバイスへの安全なアクセスを可能にします。

GL.iNet KVM は NetBird を統合し、リモート アクセスのために NetBird 仮想ネットワークにバインドできるようにします。GLKVM アプリをインストールしたり、クラウド サービスを使用したりする必要はありません。

NetBird 経由で GL.iNet KVM にリモート アクセスするには、次の手順に従います。

## KVM を NetBird にバインド

**始める前に、KVM と制御側デバイスを同じローカル ネットワークに接続してください。**

1. ドメインまたは IP アドレスを使用して KVM コンソールにローカルでログインし、**Apps Center** -> **NetBird** に移動します。 NetBird を有効にして、**Bind Device** をクリックします。

    ![bind device](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/1-bind-device.png){class="glboxshadow"}

2. デバイス確認ページにリダイレクトされます。 「**Confirm**」をクリックします。

    ![confirm device](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/2-confirm.png){class="glboxshadow"}

3. NetBird アカウントにサインインします。アカウントをお持ちでない場合は、まずサインアップしてください。

    ![netbird sign in](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/3-signin.png){class="glboxshadow"}

4. サインイン後、KVM デバイスは自動的にアカウントにバインドされます。

    ![kvm connected](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/4-connected.png){class="glboxshadow"}

    NetBird ダッシュボードでは、**Peers** ページにリストされている KVM も確認できます。

    ![netbird dashboard](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/5-dashboard.png){class="glboxshadow"}

## 制御側デバイスをバインドする

以下の例は、Windows ラップトップ (制御側デバイスとして) を NetBird ネットワークにバインドする方法を示しています。

1. [ここから](https://app.netbird.io/install){target="_blank"} からラップトップに NetBird をインストールします。

    ![install netbird](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/6-install.png){class="glboxshadow"}

2. ラップトップで NetBird を実行し、同じ NetBird ネットワークに追加します。

    NetBird はデスクトップ上に別のウィンドウ/UI を表示しません。システム トレイ (右下隅) にアイコンとしてのみ存在します。すべての操作は右クリック メニューから実行されます。

    NetBird アイコンを右クリックし、**Connect** をクリックします。

    ![pc connect](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/7-pc-connect.png){class="glboxshadow gl-50-desktop"}

3. ポップアップ ウィンドウで、**Accept** をクリックして承認します。

    ![authorize](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/8-authorize.png){class="glboxshadow"}

    ラップトップは自動的にアカウントにバインドされ、同じ NetBird ネットワークに追加されます。

    ![pc connected](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/9-login-success.png){class="glboxshadow"}

4. NetBird ダッシュボードの **Peers** ページには、KVM と制御するラップトップという 2 つのデバイスがあります。

    ![netbird dashboard](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/10-dashboard.png){class="glboxshadow"}

## NetBird 経由のリモート アクセス

以下の例は、NetBird 仮想 IP アドレスを介して KVM コンソールにリモート アクセスする方法を示しています。

1. ラップトップで、NetBird ダッシュボードにサインインし、**Peers** に移動します。

    KVM デバイスを見つけて、その **NetBird IP** (この例では `100.100.141.229`) をクリックして仮想 IP をコピーします。

    ![kvm netbird ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/11-kvm-netbird-ip.png){class="glboxshadow"}

    IP アドレスの上にカーソルを置くと、パブリック IP、ドメイン、地域などの詳細が表示されます。

2. 新しいブラウザー タブを開き、コピーした NetBird IP をアドレス バーに貼り付け、Enter キーを押します。 GLKVM ログイン ページにリダイレクトされます。

    ![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-login.png){class="glboxshadow"}

    管理者パスワードを入力してログインします。これで、GL.iNet KVM および被制御デバイスに NetBird IP 経由でアクセスできるようになります。

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_via_netbird/12-ip-access.png){class="glboxshadow"}

    **Tip**: この NetBird IP に初めてアクセスすると、プライバシー エラーが表示される場合があります。 **Advanced** -> **Proceed** をクリックして続行します。詳細については、[ブラウザからのプライバシー エラー](privacy_error_from_your_browser.md){target="_blank"}を参照してください。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
