# クラウド経由で KVM にリモートでアクセスする方法

始める前に、次のことを確認してください。

- 被制御デバイスはKVMに正しく接続されています。
    
- KVM は安定したネットワークに接続されています。

- クラウドへのデバイスのバインドはローカル ネットワーク内で行う必要があるため、KVM にローカルでアクセスできます。

クラウド サービス経由で KVM と被制御デバイスにリモートでアクセスするには、次の手順に従います。

## KVM をクラウドにバインドする

KVM をクラウドにバインドするには、通常のバインドと動的コード バインドの 2 つの方法があります。

- **Regular Binding**: KVM コンソールで [KVMCloud にバインド] をクリックすると、トークンを含むバインディング ページにリダイレクトされます。クラウドアカウントにログインし、デバイス情報を確認してバインドを完了します。

- **Dynamic Code Binding**: KVM コンソールで [コードでバインド] をクリックすると、デバイス バインド用の 8 桁の動的コードがランダムに生成されます。クラウド アカウントにログインし、コードを入力してバインドを完了します。

### 通常のバインド

IP アドレスまたはドメインを使用してローカルで KVM にログインし、右上隅の **Cloud Service** に移動します。 「**Bind To Cloud**」をクリックします。

![bind to cloud](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_to_cloud.png){class="glboxshadow"}

ログイン ページにリダイレクトされます。 glinet アカウントを入力し、「**Log In**」をクリックします。

![bind device login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_1.png){class="glboxshadow"}

デバイス情報を確認し、**Bind** をクリックします。

![bind device confirm](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_2.png){class="glboxshadow"}

少し待つと、デバイスがアカウントに正常にバインドされます。 「**Done**」をクリックします。

![bind device success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/bind_device_3.png){class="glboxshadow"}

### 動的コード バインディング

注: この機能を使用する前に、KVM ファームウェアをバージョン 1.7 にアップグレードしてください。

1. ドメインまたは IP アドレスを使用して、ローカルで GL.iNet KVM にログインします。詳細は[こちら](../faq/local_access_via_browser.md)をクリックしてください。 

2. ログイン後、右上隅の **Cloud Service** に移動し、**Bind With Code** をクリックします。

    ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. デバイス バインド用の 8 桁の動的コードがランダムに生成され、60 秒間有効です。コードをクリックしてコピーします。

    ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. [https://glkvm.com/](https://glkvm.com/){target="_blank"} にアクセスし、glinet クラウド アカウントでログインします。

    ![bind with code 3](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_3.png){class="glboxshadow"}

5. ログイン後、次のページが表示されます。

    ![bind with code 4](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_4.png){class="glboxshadow"}

    **Add Device** をクリックし、**Bind with Code** を選択します。

    ![bind with code 5](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_5.png){class="glboxshadow"}

6. ポップアップ ウィンドウで、8 桁の動的コードを入力し、**Bind** をクリックします。

    ![bind with code 6](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_6.png){class="glboxshadow"}

    **Note**: 動的コードは 60 秒以内に有効です。動的コードの有効期限が切れた場合は、KVM コンソールに戻り、**Regenerate Code** をクリックして新しいコードを取得します。

    ![regenerate code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

    デバイスはクラウド アカウントに正常にバインドされます。

## クラウド経由のリモート アクセス

ブラウザを開き (Google Chrome を例にします)、アドレス バーに「`glkvm.com`」と入力します。ログインページが表示されます。 glinet アカウントを使用してログインします。

![remote access login](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_1.png){class="glboxshadow"}

ログイン後、アカウントにバインドされているデバイスが表示されます。リモートアクセスしたいデバイスをクリックします。

![remote access select device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_2.jpg){class="glboxshadow"}

新しく開いた Web ページで、管理者パスワードを入力してログインします。

![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

KVM と被制御デバイスにクラウド経由でリモートからアクセスできるようになりました。

![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
