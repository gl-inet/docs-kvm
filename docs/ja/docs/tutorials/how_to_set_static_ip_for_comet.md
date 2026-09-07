# KVM の静的 IP を設定する方法

このチュートリアルでは、上流のルーターが静的 IP を割り当てることができない場合に、コンソール上で GL.iNet KVM の静的 IP を直接設定する手順を紹介します。

ファームウェアバージョンに応じた手順を選択してください。

## Firmware v1.9 以前

次の手順では、Comet (GL-RM1) を例に説明します。

1. Comet コンソールにログインし、**Settings** -> **Network** に移動します。 IP アドレスまたは右矢印アイコンをクリックします。

    ![settings-network](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/settings-network.png){class="glboxshadow"}

2. **Static**に切り替えます。サブネット プール内の IP アドレスと、Comet のネットマスク、ゲートウェイ、および DNS サーバーを入力し、[**Confirm**] をクリックします。

    ![ethernet-settings-static](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/ethernet-settings-static.png){class="glboxshadow"}

## Firmware v1.10 以降

次の手順では、Comet Pro (GL-RM10) を例に説明します。

1. Comet Pro コンソールにログインし、ナビゲーションバーの Settings アイコンをクリックして Settings ページを開きます。

    ![setting network](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/setting_network.png){class="glboxshadow"}

2. **Network** に移動し、Ethernet Settings の **Static** ボタンをクリックします。サブネットプール内の IP アドレスと、Comet Pro のネットマスク、ゲートウェイ、DNS サーバーを入力し、**Confirm** をクリックします。

    ![ethernet settings static](https://static.gl-inet.com/docs/kvm/tutorials/set_static_ip/ethernet_settings_static.png){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
