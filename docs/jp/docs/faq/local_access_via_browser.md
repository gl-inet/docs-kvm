# ブラウザ経由で KVM にローカルでアクセスする方法

開始する前に、制御側デバイスと KVM が同じ LAN 上にあることを確認してください。

Web ブラウザーを介してローカルで KVM にアクセスするには、ドメイン名を使用する方法と IP アドレスを使用する方法の 2 つがあります。

## ドメイン経由のローカル アクセス

1. 制御側デバイスでブラウザを開きます。互換性を高めるために Chrome または Edge をお勧めします。

2. アドレスバーに「`glkvm.local`」と入力します。 GLKVM ログイン ページが表示されます。管理者パスワードを入力します。

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_1.png){class="glboxshadow"}

    これで、KVM コンソールにローカルでアクセスできるようになり、制御対象のデバイスにアクセスできるようになります。

    ![local access via domain](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_domain_2.jpg){class="glboxshadow"}

## IP アドレスによるローカル アクセス

上流ネットワーク (ルーターなど) で KVM の IP アドレスを見つけて、ブラウザにこの IP アドレスを入力します。これで、KVM にローカルでアクセスできるようになり、被制御デバイスにアクセスできるようになります。

**GL-AXT1800** (ルーター) と **GL-RM1 Comet** (KVM) を例に挙げます。Comet は、イーサネット ケーブルを介して GL-AXT1800 ルーターの LAN ポートに接続されています。被制御デバイスは、HD ケーブルおよび USB ケーブルを介して Comet に正しく接続されています。

以下の手順に従って、KVM コンソールにアクセスします。

1. GL-AXT1800 Web 管理パネルにログインします。このルーターはインターネットにアクセスできるように設定する必要があります。

    ![log in router](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/log_in_router.png){class="glboxshadow"}

2. ルーターの管理パネルで、**Client** に移動し、クライアント リストで Comet の IP アドレスを見つけます。以下に示すように、Comet の IP は **192.168.8.197** です。

    ![find glkvm ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/find_glkvm_ip.png){class="glboxshadow"}

3. ブラウザで新しいタブを開き、アドレス バーに Comet の IP **192.168.8.197** を入力します。 

    GLKVM ログイン ページが表示されます。管理者パスワードを入力します。

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_1.jpg){class="glboxshadow"}

    これで、KVM コンソールにローカルでアクセスできるようになり、被制御デバイスにアクセスできるようになります。

    ![local access via ip](https://static.gl-inet.com/docs/kvm/faq/local_access_controlled_device_via_browser/local_access_ip_2.jpg){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
