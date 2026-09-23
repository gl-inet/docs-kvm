# KVM デバイスをほかのユーザーと共有する方法

クラウド経由のデバイス共有は、ほかのユーザーに KVM デバイスへのリモートアクセスを許可し、アクセス権を遠隔で管理できるプレミアム機能です。

**注:** この機能を使用する前に、KVM のファームウェアをバージョン 1.7 にアップグレードしてください。

次の手順で KVM デバイスを共有します。

1. KVM デバイスを Cloud にバインドします。詳しくは、[KVM を Cloud にバインドする](../faq/remote_access_via_cloud.md#kvm_1)をご覧ください。

    ![cloud login](https://static.gl-inet.com/docs/kvm/tutorials/how_to_use_share_devices/cloud_login.png){class="glboxshadow"}

2. バインド後、[https://glkvm.com/](https://glkvm.com/){target="_blank"} にログインします。バインド済みデバイスが一覧に表示されます。デバイスがオンラインであることを確認してください。

    ![device list](https://static.gl-inet.com/docs/kvm/tutorials/how_to_use_share_devices/device_list.png){class="glboxshadow"}

3. デバイスカードの三点メニューをクリックし、**Share Device** をクリックします。

    ![share device 1](https://static.gl-inet.com/docs/kvm/tutorials/how_to_use_share_devices/share_devices_1.png){class="glboxshadow"}

4. 共有相手として登録済みユーザーのメールアドレスまたはユーザー名を入力し、**Invite** をクリックします。

    ![share device 2](https://static.gl-inet.com/docs/kvm/tutorials/how_to_use_share_devices/share_devices_2.png){class="glboxshadow"}

    ![share device 3](https://static.gl-inet.com/docs/kvm/tutorials/how_to_use_share_devices/share_devices_3.png){class="glboxshadow"}

5. 招待されたユーザーのクラウド画面にデバイス共有の招待ダイアログが表示されます。**Accept** をクリックします。

    ![accept share](https://static.gl-inet.com/docs/kvm/tutorials/how_to_use_share_devices/accept_share.png){class="glboxshadow"}

    招待を承諾すると、共有されたデバイスにアクセスできます。

    ![access device](https://static.gl-inet.com/docs/kvm/tutorials/how_to_use_share_devices/access_device.png){class="glboxshadow"}

6. クラウド画面で共有状態を確認できます。

    ![share successfully](https://static.gl-inet.com/docs/kvm/tutorials/how_to_use_share_devices/share_successfully.png){class="glboxshadow"}

    共有を終了するには、**Terminate** をクリックします。終了後、共有相手はそのデバイスにアクセスできなくなります。

    ![terminate](https://static.gl-inet.com/docs/kvm/tutorials/how_to_use_share_devices/terminate.png){class="glboxshadow"}

---

ご不明な点は、[コミュニティフォーラム](https://forum.gl-inet.com){target="_blank"}または[お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"}をご利用ください。
