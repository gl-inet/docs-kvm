# RKDevTool 経由で KVM を解除する方法

このチュートリアルでは、RKDevTool を使用して GL.iNet KVM のブリックを解除する方法を紹介します。これは、KVM がブリックされ、通常のファームウェア更新または U-Boot フェールセーフ モードでは回復できないシナリオに適用されます。

## 準備

アンブロックには以下の工具をご用意ください。

- A Windows コンピューター
- A USB データ ケーブル
- A 電源アダプター (KVM デバイス用)

!!! note

    デバイスが損傷する可能性があるため、ブリック解除プロセス中に USB ケーブルを取り外したり、KVM の電源を切ったりしないでください。
    
    ブロック解除プロセスを開始する前に、重要なデータをバックアップすることをお勧めします。

## 復旧手順

ブリック解除の失敗を避けるために、次の手順に従ってください。 

1. KVM デバイスの電源を切ります。

2. KVM デバイスの最新ファームウェアを [こちら](https://dl.gl-inet.com/kvm){target="_blank"} からコンピューターにダウンロードします。

3. [ここから](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/DriverAssitant_v5.11.zip) からドライバー パッケージをコンピューターにダウンロードし、任意のディレクトリに解凍します。

4. .exe ファイルをダブルクリックして、ドライバー インストール プログラムを完了します。

    ![install driver](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_1.png){class="glboxshadow"}

    ![install driver](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/install_driver_2.png){class="glboxshadow"}

5. [ここ](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/RKDevTool_Release_v3.37.zip) から **RKDevTool** をコンピューターにダウンロードし、簡単にアクセスできるディレクトリに解凍します。

6. .exe ファイルをダブルクリックして、コンピューター上でフラッシュ ツールを実行します。

    ![run rkdevtool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_1.png){class="glboxshadow"}

    ![run rkdevtool](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/run_rkdevtool_2.png){class="glboxshadow"}

7. USB データ ケーブルを介して、KVM の Type-C OTG ポートをコンピューターの USB ポートに接続します。

    Comet (GL-RM1) を例に挙げます。 Type-C OTG ポートを以下に示します。

    ![connect usb cable](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/otg-port-rm1.png){class="glboxshadow gl-60-desktop"}

8. 電源ケーブルを KVM に接続している間、**10 seconds** の RESET ボタンを押し続けます。その後、ボタンを放します。 KVM デバイスはローダー モードに入ります。

    ![reset button](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/reset_button_rm1.jpg){class="glboxshadow" width="433"}

9. RKDevTool パネルに移動し、**Upgrade Firmware** -> **Firmware** に移動し、手順 2 でダウンロードしたファームウェアを選択してアップロードします。

    ![select firmware](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/select_firmware.png){class="glboxshadow"}

    次に、「ファームウェア」タブの隣にある「**Upgrade**」タブに移動すると、「Found Loader Device」と表示され、ファームウェアのフラッシュが開始されます。

    ![rkdevtool panel](https://static.gl-inet.com/docs/kvm/tutorials/debrick_via_rkdriver/rkdevtool_panel.jpg){class="glboxshadow"}

    アップグレードが完了すると、KVM デバイスは自動的に再起動します。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
