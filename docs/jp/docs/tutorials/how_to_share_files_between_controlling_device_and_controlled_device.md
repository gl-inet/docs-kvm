# 制御側デバイスと制御側デバイス間でファイルを共有する方法

GL.iNet KVM は、読み取り/書き込み USB ドライブをエミュレートし、制御側デバイスと制御側デバイスの間でファイルを共有および管理できるようにします。

次の手順では、Comet (GL-RM1) を例に説明します。

## 被制御デバイスにファイルを送信する

制御側デバイスから被制御デバイスにファイルを共有するには、次の手順に従います。

1. コンソールで、**Virtual Media** に移動します。ボックスをドラッグまたはクリックして、制御側デバイスからファイルをアップロードするか、URL からアップロードします。

    アップロードされると、以下のようにファイルが表示されます。

    ![upload files](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing1.png){class="glboxshadow"}

2. 「**Mount To Remote**」→「**File Sharing**」をクリックします。

    ![file sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing2.png){class="glboxshadow"}
以下に示すように、

3. A ウィンドウがコンソールにポップアップ表示され、ファイル共有手順が示されます。

    ![file sharing tips](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing3.png){class="glboxshadow"}

4. 少し待つと、**"GLKVM"** という名前のドライブが画面に自動的に表示されます。 Comet は、被制御デバイス上で読み取り/書き込み USB ドライブをエミュレートしており、以前にアップロードしたファイルが被制御デバイスに共有されていることがわかります。

    これで、被制御デバイス上のこのドライブ内のファイルを表示、移動、または削除できるようになります。

    ![file shared](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing4.png){class="glboxshadow"}

    **Tip**: ドライブが自動的にポップアップしない場合は、被制御デバイスの **This PC** に移動します。

    ![this pc](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/thispc.png){class="glboxshadow"}

    **"GLKVM"** という名前のドライブを検索します。これで、このドライブ内のファイルを表示、移動、または削除できるようになります。

5. 共有を停止する場合は、ツールバーの **Virtual Media** をクリックし、**Stop Sharing** をクリックします。

    ![stop sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing1.png){class="glboxshadow"}

## 被制御デバイスからファイルを取得する

被制御デバイスからファイルを受信するには、次の手順に従います。

1. 被制御デバイスで、共有するファイルをドライブ **GLKVM** に移動またはコピーします。

    以下に示すように、ファイルは被制御デバイスのデスクトップからディスク **GLKVM** に移動されました。

    ![copy file to disk](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing5.png){class="glboxshadow"}

2. Comet のコンソールに移動し、ツールバーの **Virtual Media** をクリックして、**Stop Sharing** をクリックします。

    ![stop sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing2.png){class="glboxshadow"}

3. このファイルは、次のように **Virtual Media** の下に表示されます。これで、このファイルを Comet から制御側デバイスにダウンロードできるようになります。

    ![file shared](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing6.png){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
