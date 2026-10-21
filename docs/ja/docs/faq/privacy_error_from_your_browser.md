# ブラウザ経由で KVM にアクセスするとプライバシー エラーが発生する {#privacy-error-when-accessing-kvm-via-browser}

ブラウザ経由で GL.iNet KVM にアクセスすると、ブラウザの警告が表示される場合があります: **接続はプライベートではありません**。

![privacy error](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

この警告は、KVM が提示した SSL/TLS 証明書をブラウザが検証できないことを示します。たとえば、ブラウザが信頼する認証局によって発行されていない場合や、コンソールへのアクセスに使用した IP アドレスまたはホスト名と証明書が一致しない場合に表示されます。

## この警告が表示されるのはなぜですか？ {#why-do-i-get-this-warning}

上記の例では、**192.168.8.11** は、DHCP 経由で上位ルーターによって動的に割り当てられる KVM ローカル IP アドレスです。

!!! note

    GL.iNet KVM が接続されているルーターのゲートウェイが「192.168.x.1」（プライベート ネットワークでは x は通常 0、1、または 8）の場合、KVM のローカル IP は「192.168.x.y」（y は有効なホスト アドレス）である必要があります。サブネット内）。

このローカル IP アドレスは、公開 Web サイトではなく、GL.iNet KVM コンソールにアクセスするために使用されます。

KVM は、ブラウザからの HTTPS アクセスにデフォルトの TLS 証明書を使用します。ブラウザは、公開 Web サイトと同様にローカルコンソールの証明書も検証します。証明書は信頼されており、有効で、アクセス先のアドレスと一致している必要があります。

デフォルトの証明書をブラウザが信頼していない場合や、入力したローカル IP アドレスまたはホスト名が証明書の対象に含まれていない場合、警告が表示されます。この警告は、KVM に証明書がないことを意味するものではありません。HTTPS による通信の暗号化は可能ですが、ブラウザは KVM の身元を確認できません。

## 警告を解決するにはどうすればよいですか？ {#how-to-resolve-the-warning}

ローカルアクセスでは、まずアドレスがご使用の KVM のものであることを確認してください。その後、**Advanced**、**Continue to "192.168.8.11"** の順にクリックします（表示される文言はブラウザによって異なります）。

![Continue to 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

その後、GL.iNet KVM コンソールにリダイレクトされます。

![local access to kvm admin](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## 独自の証明書を使用できますか？ {#can-i-use-my-own-certificate}

はい。独自の SSL/TLS 証明書を KVM にインストールして使用できます。以下の手順に従ってください。

1. KVM へのアクセスに使用するホスト名または IP アドレスを対象とする SSL/TLS 証明書を取得します。ブラウザの警告を回避するには、証明書が有効で、ブラウザが信頼する認証局によって発行されている必要があります。自己署名証明書は、制御側デバイスでその証明書を信頼するよう明示的に設定しない限り、引き続き警告の原因となります。

2. KVM コンソールにログインします。右上隅の盾アイコンをクリックして、**Security** -> **TLS Certificate** に移動します。

    ![custom cert 1](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert1.png){class="glboxshadow"}

    ポップアップ ウィンドウで **Custom Certificate** を選択し、証明書ファイルと秘密キーをアップロードします。この機能はファームウェア v1.8.0 以降で利用可能です。

    ![custom cert 2](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert2.png){class="glboxshadow"}

    または、SSH ターミナルや WinSCP 経由で KVM 上の証明書と秘密キーを置き換えることもできます。証明書と秘密キーは次のディレクトリに保存されています。

    `/etc/kvmd/user/ssl`

    これらを新しい SSL 証明書と秘密キーに置き換えます。

---

まだ質問がありますか？ [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
