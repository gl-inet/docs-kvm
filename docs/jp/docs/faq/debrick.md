# U-Boot を使用して KVM のブロックを解除します

DIY プロジェクトや間違ったファームウェアのフラッシュが原因で KVM をブリックした場合、KVM は正しく電源を入れることができない可能性があります。この場合、U-Boot フェイルセーフを使用してファームウェアを再インストールできます。

## 準備

イーサネットポートを備えたコンピューターまたはラップトップをご用意ください。コンピュータにイーサネット ポートがない場合は、追加の USB イーサネット アダプタが必要です。

## 復旧手順

ブリック解除の失敗を避けるために、以下の手順に厳密に従ってください。

1. ファームウェア[ここから](https://dl.gl-inet.com/kvm){target="_blank"}をコンピューターにダウンロードしてください。

2. KVM の電源を取り外します。コンピュータを KVM の Ethernet ポートに接続します。

3. リセット ボタンをしっかりと押し続け、**同時に KVM** の電源を入れます。

    LED が規則的なシーケンスで数回点滅するまで待ちます。点滅パターンが変化した後**、リセット ボタンを放します。

    !!! note "デバイスモデル別の LED 点滅パターン"

        - **Comet (GL-RM1)**: リセットボタンを押し続けると、青色の LED が 5 回点滅します。 5 が点滅したらリセット ボタンを放すと、青い LED が点灯したままになります。

        - **Comet PoE (GL-RM1PE)**: リセットボタンを押し続けると、青色の LED が 5 回点滅します。 5 が点滅したらリセット ボタンを放すと、青い LED が点灯したままになります。

        - **Comet Pro (GL-RM10)**: リセット ボタンを約 5 秒間押し続け、その間に KVM の電源も同時にオンになり、ボタンを放します。 U-Boot モードに入ります。

        - **Comet 5G (GL-RM10RC)**: リセット ボタンを約 5 秒間押し続け、その間に KVM の電源も同時にオンになり、ボタンを放します。 U-Boot モードに入ります。

4. コンピューターの IP アドレスを手動で **192.168.1.2** に設定します。以下のさまざまなオペレーティング システムのステップバイステップ ガイドをご確認ください。

    ??? "Windows 7 / Windows 10"

        1. **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **アダプター設定の変更** に移動します。

        2. **Local Area Connection** -> **Properties** を右クリックします。

        3. 「**Internet Protocol Version 4 (TCP/IPv4)**」→「**Properties**」をクリックします。

        4. **IP アドレス**を `192.168.1.2` に手動で設定します。

        5. **サブネット マスク**を `255.255.255.0` に設定します。

            ![ipv4 properties](https://static.gl-inet.com/docs/kvm/faq/debrick/win7_set_ip.jpg){class="glboxshadow"}

        6. **OK** ボタンをクリックします。

    ??? "Windows 11"

        1. 設定を開きます。

        2. **ネットワークとインターネット**をクリックします。

        3. 「**Ethernet**」タブをクリックします。

            ![windows 11 ethernet](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet.png){class="glboxshadow"}

        4. [IP 割り当て] セクションで、**Edit** ボタンをクリックします。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit1.png){class="glboxshadow"}

        5. **Manual** オプションを選択します。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit2.png){class="glboxshadow"}

        6. **IPv4 toggle** スイッチをオンにします。

        7. 静的 **IP アドレス**を **192.168.1.2** に設定します。

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/kvm/faq/debrick/win11_ethernet_ip_edit3.png){class="glboxshadow"}

        8. **サブネット マスク**を**255.255.255.0**として指定します。

        9. 「**Save**」ボタンをクリックします。

    ??? "macOS"
    
        1. 画面の左上隅にある **Apple** アイコンをクリックし、**System Preferences** を選択します。

            ![macos system preferences](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences.png){class="glboxshadow"}

        2. 「**Network**」をクリックします。

            ![macos system preferences network](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_system_preferences_network.png){class="glboxshadow"}

        4. 左側の **Ethernet** をクリックし、**Configure IPv4** の横にあるドロップダウン ボックスをクリックして、**Manually** を選択します。 USB イーサネット アダプターを使用している場合、イーサネットが見つからず、USB イーサネット アダプターの名前として表示される場合があります。

            ![macos ip manually](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_1.png){class="glboxshadow"}

        4. **IPv4 Address**～`192.168.1.2`、**Subnet Mask**～`255.255.255.0`、**Router**～`192.168.1.1`を入力し、右下の適用ボタンをクリックします。

            ![macos ip manually](https://static.gl-inet.com/docs/kvm/faq/debrick/mac_ip_manually_2.png){class="glboxshadow"}

5. ブラウザを使用して **http://192.168.1.1**. にアクセスします。これは U-Boot Web UI です。

    ![Uboot web ui](https://static.gl-inet.com/docs/kvm/faq/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    **注意:** U-Boot のバージョンは製造日によって異なるため、上記の U-Boot Web UI は、表示されるものとまったく同じではない可能性があります。セキュリティ上の理由から、現在、個別の U-Boot アップグレードは提供されていません。アップデートが必要な場合は、新しいファームウェアに統合されます。

6. **ファイルを選択** をクリックし、ファームウェア ファイルを選択します。次に、**ファームウェアの更新** ボタンをクリックします。

7. 3分ほど待ちます。 **更新中は KVM の電源を切らないでください。** 

    KVM の LED が **白色に点滅**すると準備完了です。

8. 手順 4 で行ったコンピューターの IP 設定を元に戻します。

9. コンピューターと KVM の間のイーサネット ケーブルを取り外し、このイーサネット ケーブルまたは Wi-Fi を介して KVM をネットワーク ソース (ルーターやネットワーク スイッチなど) に接続します。

    KVM がインターネット アクセスを取得できるようになるまで、約 1 分間待ちます。これで、再び KVM にアクセスできるようになります。

    **注:** 通常、構成設定は保持されます。ただし、設定エラーにより回復が必要なシステム障害が発生した場合は、デフォルトに戻ります。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
