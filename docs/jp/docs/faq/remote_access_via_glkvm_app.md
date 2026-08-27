# GLKVM アプリ経由で KVM にリモートでアクセスする方法

始める前に、被制御デバイスが GL.iNet KVM に正しく接続されており、KVM が安定したネットワークに接続されていることを確認してください。

GLKVM アプリを介して KVM および被制御デバイスにリモートでアクセスするには、以下の手順に従ってください。

## インストールしてログイン

1. [GLKVM アプリ](https://www.gl-inet.com/app-rm/){target="_blank"} を制御側デバイスにインストールします。

2. GLKVM アプリを開き、GL.iNet アカウントでログインします。

    ![log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_login.jpg){class="glboxshadow"}

    GL.iNet アカウントをお持ちでない場合は、アカウントを作成してログインしてください。

    ![sign up](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/app_signup.png){class="glboxshadow"}

## KVM をバインドします

ログイン後、以下のようなページが表示されます。 「**Add Device**」をクリックします。

KVM をバインドするには、自動検出、S/N コード、および動的バインディング コードの 3 つの方法があります。

![add device](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device.png){class="glboxshadow"}

### 自動検出

これはローカル ネットワーク内で行う必要があります。 KVM と制御側デバイスが同じ LAN 上にあることを確認してください。

1. 「**Auto Discover**」をクリックします。利用可能な KVM デバイスの検索が自動的に開始されます。

    ![auto discover 1](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_1.png){class="glboxshadow"}

2. KVM を見つけて、その **Device ID** を入力してアカウントにバインドします。

    ![auto discover 2](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_auto_2.png){class="glboxshadow"}

### S/N コード

この方法は、KVM が検出されない、または同じ LAN 上にないが、シリアル番号 (S/N) はわかっているというシナリオに適用されます。

1. 「**S/N Code**」をクリックします。

2. ポップアップ ウィンドウで、デバイスの名前を入力し、KVM デバイスのラベル下部に印刷されている S/N を入力します。

    ![sn code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_sn_code.png){class="glboxshadow"}

### 動的バインディング コード

この機能を使用する前に、KVM ファームウェアを v1.7 にアップグレードしてください。

これはローカル ネットワーク内で行う必要があります。 KVM と制御側デバイスが同じ LAN 上にあることを確認してください。

1. ドメインまたは IP アドレスを使用してローカルで KVM にログインします。詳細は[こちら](../faq/local_access_via_browser.md)をクリックしてください。

2. ログイン後、右上隅の**Cloud Service**に移動し、**Bind With Code**をクリックします。

    ![bind with code 1](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_1.png){class="glboxshadow"}

3. デバイス バインド用に 60 秒間有効な 8 桁の動的コードをランダムに生成します。コードをクリックしてコピーします。

    ![bind with code 2](https://static.gl-inet.com/docs/kvm/tutorials/bind_to_cloud_via_code/bind_with_code_2.png){class="glboxshadow"}

4. GLKVM アプリに戻り、動的バインディング コードを入力して、**Bind** をクリックします。

    ![dynamic code](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/add_device_dynamic_code.png){class="glboxshadow"}

## リモート アクセス

KVM デバイスがアカウントにバインドされると、アプリに「オンライン」と表示されます。

![device online](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/device_online.png){class="glboxshadow"}

KVM デバイスをクリックします。新しいウィンドウが開き、接続が開始されます。

![connecting](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connecting.png){class="glboxshadow"}

接続したら、管理者パスワードを入力してログインします。

![connected log in](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_login.png){class="glboxshadow"}

KVM デバイスにアクセスできるようになり、これを介して制御対象のデバイスにアクセスできるようになります。

![connected access](https://static.gl-inet.com/docs/kvm/faq/remote_access_controlled_device_via_glkvm_app/connected_access.png){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
