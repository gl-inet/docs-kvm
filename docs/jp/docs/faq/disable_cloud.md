# クラウド サービスを無効にする方法

GL.iNet KVM クラウド サービスはデフォルトで有効になっており、ユーザーはリモート アクセスのために KVM デバイスをクラウド アカウントにバインドできます。

クラウド サービスを使用したくない場合は、手動で無効にすることができます。無効にすると、クラウド サービスおよび GLKVM アプリからのリモート アクセスが利用できなくなります。再度有効にするには、ドメインまたは IP アドレスを介してローカルで、または Tailscale を介してリモートで KVM にログインする必要があります。

必要に応じて、次の手順に従ってクラウド サービスを無効にします。

1. KVM デバイスにログインし、右上隅の **Cloud Service** に移動します。歯車アイコンをクリックし、「**Disable**」をクリックします。

    ![disable cloud](https://static.gl-inet.com/docs/kvm/faq/disable_cloud/disable_cloud_1.png){class="glboxshadow" width="400"}

2. 無効にすると、以下のようなページが表示されます。

    ![disable cloud](https://static.gl-inet.com/docs/kvm/faq/disable_cloud/disable_cloud_2.png){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
