# Tailscale 経由で KVM にリモートでアクセスする方法

GL.iNet KVM は Tailscale を統合し、リモート アクセスのために Tailscale 仮想ネットワークにバインドできるようにします。GLKVM アプリをインストールしたり、クラウド サービスを使用したりする必要はありません。これは、制御側デバイスが Windows、macOS、Android、または iOS を実行していない場合 (したがって、GLKVM アプリをインストールできない場合)、または GLKVM アプリやクラウド サービスを使用したくない場合に特に便利です。

Tailscale 経由で GL.iNet KVM にリモート アクセスするには、次の手順に従います。

## KVM を Tailscale にバインド

**始める前に、KVM と制御側デバイスを同じローカル ネットワークに接続してください。**

1. 制御側デバイスでブラウザを開きます。互換性を高めるために Chrome または Edge をお勧めします。

2. ドメインまたは IP アドレスを使用して、ローカルで KVM コンソールにログインします。ここでは例としてデフォルトのドメインを使用します。

    アドレスバーに「`glkvm.local`」と入力します。 GLKVM ログイン ページが表示されます。管理者パスワードを入力します。

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

3. ログイン後、**Apps Center** -> **Tailscale** に進みます。 Tailscale を有効にして、**Bind Device** をクリックします。

    ![enable tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enable_tailscale.png){class="glboxshadow"}

4. Tailscale ログイン ページが表示されます。メールアドレスを入力してログインします。

    ![log in tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

5. ログイン後、デバイス glkvm をテールネットに接続しようとしていることがページに表示されます。 「**Connect**」をクリックします。

    ![connect kvm to tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_kvm_to_tailscale.png){class="glboxshadow"}

    KVM デバイスはテールネットに正常にバインドされます。

    ![bind kvm successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_kvm_successful.png){class="glboxshadow"}

6. Tailscale コンソールにリダイレクトされ、**glkvm** というラベルのデバイスが **Machines** の下に表示されます。

    ![tailscale console 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_1.png){class="glboxshadow"}

## 制御側デバイスをバインドする

以下の例は、Windows ラップトップ (制御側デバイスとして) を Tailscale ネットワークにバインドする方法を示しています。

1. [ここから](https://tailscale.com/download){target="_blank"}からラップトップにTailscaleをインストールします。

2. ラップトップで Tailscale を実行し、同じ電子メールでログインします。

    ![log in tailscale](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/log_in_tailscale.png){class="glboxshadow"}

3. ログイン後、ラップトップ (制御側デバイスなど) をテールネットに接続しようとしていることがページに表示されます。 「**Connect**」をクリックします。

    ![connect pc to tailnet](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/connect_pc_to_tailscale.png){class="glboxshadow"}

    ラップトップはテールネットに正常にバインドされます。

    ![bind pc successful](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/bind_pc_successful.png){class="glboxshadow"}

4. Tailscale コンソールにリダイレクトされ、制御側デバイスも **Machines** の下に表示されます。

    ![tailscale console 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/tailscale_panel_2.png){class="glboxshadow"}

## Tailscale 経由のリモート アクセス

Tailscale コンソールで、glkvm の **Address** (この例では `100.104.185.26`) をクリックします。

![get vittual ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/get_vitual_ip.png){class="glboxshadow"}

次の 4 つの値が表示されます。

- glkvm (デバイス名)
- glkvm.tail1fd0.ts.net (Tailscale が割り当てたドメイン)
- fd7a:115c:a1e0:301:b92f (仮想 IPv6)
- 100.104.185.26 (仮想 IPv4)。

これらは、デバイスの識別と仮想ネットワーク通信のために Tailscale によって割り当てられます。 Tailscale が割り当てたドメイン、仮想 IPv4 および仮想 IPv6 を使用して、KVM デバイスにリモート アクセスできます。

仮想 IPv4 を例に挙げます。

1. KVM デバイスの仮想 IPv4 アドレスをコピーします。

2. 新しいタブを開き、IP アドレスをアドレス バーに貼り付けます。

    ![access vitual ip](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/enter_vitual_ip.png){class="glboxshadow"}

    A プライバシー エラーが表示される場合があります。 [このプライバシー エラーが発生するのはなぜですか?](privacy_error_from_your_browser.md){target="_blank"}

    ![privacy error](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/privacy_error.png){class="glboxshadow"}

    **Advanced** をクリックし、**100.104.185.26 に進みます**。 GLKVM ログイン ページにリダイレクトされます。

    ![proceed](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/proceed.png){class="glboxshadow"}

3. 管理者パスワードを入力してログインします。これで、Tailscale 仮想 IP を介して、GL.iNet KVM および被制御デバイスにアクセスできるようになります。

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_tailscale/remote_access_via_tailscale.png){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
