# KVM デバイスをクラウドからバインド解除する方法

KVM デバイスをクラウドからバインド解除するには、ローカル アクセス、GLKVM アプリ、またはクラウドの 3 つの方法があります。

## ローカル アクセスによるバインド解除

1. コンピューターが KVM デバイスと同じローカル エリア ネットワーク上にあることを確認します。

2. コンピューターで Web ブラウザーを起動します (互換性を高めるために Chrome または Edge をお勧めします)。アドレス バーに `glkvm.local` または KVM の IP アドレスを入力して、GLKVM ローカル ログイン ページにアクセスします。管理者パスワードを入力してログインします。

3. ログイン後、右上隅の **Cloud Service** に移動し、歯車アイコンをクリックして、**Unbind** を選択します。

    ![unbind via local](https://static.gl-inet.com/docs/kvm/faq/unbind/local_unbind.png){class="glboxshadow"}

## GLKVM アプリ経由でバインド解除

1. GLKVM アプリにログインし、デバイスの右上隅にある **Manage** をクリックします。

    ![unbind via app](https://static.gl-inet.com/docs/kvm/faq/unbind/app_unbind_1.png){class="glboxshadow"}

2. **More** をクリックし、**Unbind** を選択します。

    ![app unbinding](https://static.gl-inet.com/docs/kvm/faq/unbind/app_unbind_2.png){class="glboxshadow"}

## クラウド経由でバインド解除

1. コンピューターで Web ブラウザーを起動します (互換性を高めるために Chrome または Edge をお勧めします)。アドレスバーに「`glkvm.com`」と入力し、クラウドアカウントでログインします。

2. ログイン後、デバイスの右下隅にある 3 点アイコンをクリックし、**Device Detail** をクリックします。

    ![unbind via cloud](https://static.gl-inet.com/docs/kvm/faq/unbind/cloud_unbind_1.png){class="glboxshadow"}

3. 詳細ページで、**Unbind** をクリックします。

    ![unbind via cloud](https://static.gl-inet.com/docs/kvm/faq/unbind/cloud_unbind_2.png){class="glboxshadow gl-80-desktop"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
