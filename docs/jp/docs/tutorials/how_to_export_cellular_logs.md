# セルラーログをエクスポートする方法

このチュートリアルでは、トラブルシューティングのために KVM デバイスからセルラー関連のログをエクスポートする手順を紹介します。

次の手順では、Comet 5G (GL-RM10RC) を例に説明します。

1. KVM コンソールにログインし、**Virtual Media** に移動して有効になっていることを確認します。

2. **Toolbox** -> **Terminal** に移動します。 **Access** をクリックして、KVM ターミナルに入ります。

    ![access terminal](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/access_terminal.png){class="glboxshadow"}

3. ターミナル ウィンドウで次のコマンドを実行して QLog プログラムを起動します。

    ```
    QLog_1.5.22 -s /userdata/media/ -f /etc/HN_default.cfg & ubus call modem at '{"AT":"AT+QCFG=\"DBGCTL\",0"}'
    ```

    ![qlog 1](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog1.jpg){class="glboxshadow"}

    ページには、以下に示すように、QLog の起動に関連する初期化が表示され、続いてリアルタイムのデータ統計 (受信したデータ量や経過時間など) が表示されます。

    ![qlog 2](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog2.jpg){class="glboxshadow"}

4. Enter キーを押して次のコマンドを順番に実行してモデムを再起動し、デバイスが完全な起動プロセス ログを確実にキャプチャできるようにします。

    ```
    ubus call modem at '{"AT":"AT+CFUN=0"}'
    ```

    ```
    ubus call modem at '{"AT":"AT+CFUN=1"}'
    ```

    ![qlog 3](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog3.png){class="glboxshadow"}

5. 十分なログ データが収集されるまで 3 ～ 5 分間待ちます。その後、次のコマンドを入力して QLog プロセスを停止します。

    ```
    ps | grep QLog | grep -v grep | awk '{print $1}' | xargs kill -9
    ```

    ![qlog 4](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog4.png){class="glboxshadow"}

6. ログをエクスポートします。

    セルラー モデム ログは、ファイル名サフィックス `xxx.qmdl` とともに **/userdata/media/** ディレクトリに保存されます。

    KVM コンソールにログインし、**Virtual Media** に移動して、接尾辞 `xxx.qmdl` を持つターゲット ファイルを見つけます。これらのファイルをダウンロードして、GL.iNet テクニカル サポートと共有してください。

    ![qlog 5](https://static.gl-inet.com/docs/kvm/tutorials/export_cellular_logs/qlog5.png){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
