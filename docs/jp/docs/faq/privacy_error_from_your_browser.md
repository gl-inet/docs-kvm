# ブラウザ経由で KVM にアクセスするとプライバシー エラーが発生する

ブラウザ経由で GL.iNet KVM にアクセスすると、ブラウザの警告が表示される場合があります: **接続はプライベートではありません**。

![privacy error](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

HTTPS 接続は証明書に依存してサーバー ID を検証し、データを暗号化するため、これはブラウザーが SSL/TLS 証明書のない Web サイトを検出したときに発行する標準のセキュリティ警告です。

## この警告が表示されるのはなぜですか?

上記の例では、**192.168.8.11** は、DHCP 経由で上位ルーターによって動的に割り当てられる KVM ローカル IP アドレスです。

!!! note

    GL.iNet KVM が接続されているルーターのゲートウェイが「192.168.x.1」(プライベート ネットワークでは x は通常 0、1、または 8) の場合、KVM のローカル IP は「192.168.x.y」(y は有効なホスト アドレス) である必要があります。サブネット内)。

このローカル IP アドレスは、公開 Web サイトではなく、GL.iNet KVM コンソールにアクセスするために使用されます。

ただし、ブラウザは通常、ローカル コンソールと通常の公開 Web サイトを区別しません。すべての IP アドレスを Web サイトとして扱い、HTTPS 接続が SSL/TLS 証明書によって保護されることを期待します。

本当に安全な Web サイトでは SSL/TLS 証明書が使用されるため、ブラウザーがローカル コンソール (証明書を持たない) にアクセスすると、証明書がないためにセキュリティ アラートがトリガーされます。

## 警告を解決するにはどうすればよいですか?

**Advanced** をクリックし、**「192.168.8.11」に進みます**。

![Continue to 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

その後、GL.iNet KVM コンソールにリダイレクトされます。

![local access to kvm admin](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## 独自の証明書を使用できますか?

はい。独自の SSL/TLS 証明書を KVM にインストールして使用できます。以下の手順に従ってください。

1. SSL/TLS 証明書を申請するか、自己署名証明書を使用します。

2. KVM コンソールにログインします。右上隅の盾アイコンをクリックして、**Security** -> **TLS Certificate** に移動します。

    ![custom cert 1](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert1.png){class="glboxshadow"}

    ポップアップ ウィンドウで **Custom Certificate** を選択し、証明書ファイルと秘密キーをアップロードします。この機能はファームウェア v1.8.0 以降で利用可能です。

    ![custom cert 2](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert2.png){class="glboxshadow"}

    または、SSH ターミナルまたは WinSCP 経由で KVM の構成ファイルを編集することもできます。自動生成された証明書とキーは次のパスに保存されます。

    `/etc/kvmd/user/ssl`

    これらを新しい SSL 証明書と秘密キーに置き換えます。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
