# 動的コードを介してKVMをクラウドにバインドする方法

> 注: この機能を使用する前に、KVM ファームウェアをバージョン 1.7 にアップグレードしてください。

このチュートリアルでは、動的コードを通じて GL.iNet KVM をクラウドに簡単にバインドする方法を紹介します。

## バインド手順

1. ドメインまたは IP アドレスを使用して、ローカルで GL.iNet KVM にログインします。詳細は[こちら](../faq/local_access_via_browser.md)をクリックしてください。

2. ログイン後、右上隅の **Cloud Service** に移動し、**Bind With Code** をクリックします。

    ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. デバイス バインド用に 60 秒間有効な 8 桁の動的コードをランダムに生成します。コードをクリックしてコピーします。

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

7. デバイスはクラウド アカウントに正常にバインドされます。 「**Done**」をクリックします。

    ![bind with code 7](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_7.png){class="glboxshadow"}

    デバイスリストにKVMが表示されます。クラウドサービス経由でリモートアクセスできるようになりました。

    ![bind with code 8](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_8.png){class="glboxshadow"}

8. リモート アクセスするデバイスをクリックします。新しく開いた Web ページで、管理者パスワードを入力してログインします。

    ![remote access admin](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_3.png){class="glboxshadow"}

    そうすると、クラウド経由でKVMと被制御デバイスにリモートアクセスできるようになります。

    ![remote access success](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_cloud/remote_access_4.png){class="glboxshadow"}

## FAQ

1. **Q: 動的コードの有効期間はどのくらいですか?有効期限が切れたらどうすればよいですか?**

    A: 動的コードは 60 秒以内に有効です。動的コードの有効期限が切れた場合は、KVM コンソールに戻り、**Regenerate Code** をクリックして新しいコードを取得します。

    ![regenerate code](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/regenerate_code.png){class="glboxshadow"}

2. **Q: 動的コードを生成できない場合はどうすればよいですか?**

    A: 動的コードを生成できない場合は、ネットワークが不安定であるか、アップストリームの DNS 構成が原因である可能性があります。

    - ネットワークが安定しているかどうかを確認するか、別のネットワークに切り替えて再試行してください。

    - アップストリーム DNS 設定を変更し、コードを再生成します。

    問題が解決しない場合は、[support@gl-inet.com](mailto:support@gl-inet.com) にお問い合わせください。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
