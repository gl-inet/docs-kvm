# KVM ホスト名を変更する方法

GL.iNet KVM のデフォルトのホスト名は **glkvm** です。これは、同じネットワークに接続されている場合、ドメイン `glkvm.local` 経由でローカルにアクセスできることを意味します。

このチュートリアルでは、ホスト名を変更するための 2 つの方法 (KVM コンソール経由またはターミナル コマンド経由) を紹介します。

## 方法 1. KVM コンソール

> **Note**: この機能はファームウェア バージョン 1.7.0 以降で利用できます。

1. KVM にログインし、**Settings** -> **Network** に移動します。ホスト名または右矢印アイコンをクリックします。

    ![settings network](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings_network.png){class="glboxshadow"}

2. ホスト名をカスタマイズし、**Apply** をクリックします。

    ![modify hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify_hostname.png){class="glboxshadow"}

## 方法 2. 端末コマンド

1. KVM にログインし、**Toolbox** -> **Terminal** に移動します。 「**Access**」をクリックします。

    ![access terminal](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_terminal.png){class="glboxshadow"}

2. ターミナルで次のコマンドを入力し、Enter キーを押します (「example」を希望のホスト名に置き換えます)。その後、KVM が再起動します。

    `echo example > /etc/hostname && reboot`

    ![input command](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/input_command.png){class="glboxshadow"}

3. 再起動するまで待ちます。その後、新しいホスト名を使用して KVM にアクセスできるようになります。

    ![access new hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_new_hostname.png){class="glboxshadow"}

    ホスト名を忘れた場合、または変更が有効になったかどうかを確認する必要がある場合は、ターミナルに次のコマンドを入力して現在のホスト名を表示します。

    `cat /etc/hostname`

    ![verify hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/verify_hostname.png){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
