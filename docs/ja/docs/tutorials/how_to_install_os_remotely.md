# 仮想メディアを使用して、制御されているコンピューターにリモートで OS をインストールする方法

このチュートリアルでは、GL.iNet KVM の機能である仮想メディアを使用して、制御されているコンピューターにオペレーティング システムをリモートでインストールする方法を紹介します。

1. GL.iNet KVM にログインし、**Virtual Media** に移動します。

2. OS ISO ファイルを仮想メディアにアップロードします。

    ![upload file](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/upload_file.png){class="glboxshadow"}

3. アップロード後、**Mount To Remote** をクリックし、**イメージのマウント** を選択して ISO イメージをマウントします。

    ![image mounting](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-1.png){class="glboxshadow"}

    画像ファイルを選択し、**Mount Image**をクリックします。

    ![image mounting](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-2.png){class="glboxshadow"}

4. リモート制御されているコンピューターを再起動し、起動中に **すぐに適切なキーを押し** (この例では DEL など)、BIOS/UEFI に入ります。

    ![enter bios](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/enter_bios.png){class="glboxshadow"}

5. ブート メニューで、**「Glinet Flash Drive 1.00」**をブート オプション #1 として設定します。

    ![set boot option priority](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/set_boot_option_priority.png){class="glboxshadow"}

6. BIOS を保存して終了します。その後、システムはマウントされた ISO から起動して OS のインストールを開始します。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
