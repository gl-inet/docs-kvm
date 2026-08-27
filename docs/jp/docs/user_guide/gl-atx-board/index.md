# ATX ボード (GL-ATXPC) ユーザーガイド

ATX ボードは、GL.iNet KVM デバイスのオプションのアクセサリです。スマート電源管理モジュールとして、物理的な電源ボタン操作 (電源オン/オフ/再起動) をシミュレートすることで、被制御デバイスの電源を遠隔制御できます。 

ATX ボードは被制御デバイスのシャーシに取り付けられ、より隠蔽された安定した電源管理を提供します。

**Note**: Comet Q (GL-RMQ1) は ATX ボードでは動作しません。

![rm1-and-atx-borad](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/rm1-and-atx-borad.jpg){class="glboxshadow"}

## パッケージ内容

![inside the box](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/inside-the-box.png){class="glboxshadow gl-80-desktop"}

- 1 x ATX メインボード
- 1 x 9 ピン ワイヤー セット
- 1 x ネジパッケージ
- 1 x USB-A - Type-C ケーブル
- 1 x ATX ブラケット セット

## ピンアウト

![pinout](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/pinout.jpg){class="glboxshadow gl-80-desktop"}

インターフェイスの説明:

1. Type-C インターフェイス: KVM デバイスに接続します。
2. ファームウェア アップグレード ボタン: ATX メイン ボード上のシングルチップ マイクロコンピューター用。
3. リセット ボタン。
4. コンピューターパネルの制御線に接続します。
5. コンピューターの F_PANEL インターフェイスに接続します。

!!! note

    1. インターフェイス 4 と 5 は相互に接続できます。つまり、インターフェイス 5 はコンピュータ パネルの制御ラインに接続でき、インターフェイス 4 は F_PANEL に接続できます。 
    
    2. ATX ボードには 2 つの LED があり、両方の LED の動作は電源 LED と同じです (青は ATX システムを示し、緑は PC の電源を示します)。 ATX ボードには HDD LED がありません。ボード上の LED ステータスは、コンピュータ パネルの電源 LED ステータスと一致します。 

インターフェイス 4/5 図:

![interface](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface.png){class="glboxshadow gl-60-desktop"}

## インストール

ATX ボードを取り付けるには、このビデオを視聴するか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/3VEjZgzgI44" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1。 ATX ボードとブラケットをネジで固定する

ATX ボードと ATX ブラケット セットを付属のネジで固定します。

![screwing](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/screwing.jpg){class="glboxshadow gl-90-desktop"}

### 2。 ATXボードをPCケースに取り付ける

インターフェース 4 と 5 をそれぞれ制御対象 PC の制御ラインと F_PANEL インターフェースに接続します。

![interface connect](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface_connect.jpg){class="glboxshadow gl-90-desktop"}

ATX パッケージで提供される 9 ピン ワイヤ セットを使用すると、ATX ボード インターフェイス 4/5 の 1 つを、制御対象のコンピュータの制御ラインまたは F_PANEL インターフェイスに接続できます。
    
別の ATX ボード インターフェイス 4/5 を制御対象コンピュータの制御ラインまたは F_PANEL インターフェイスに接続するには、コンピュータ ケースに含まれているワイヤ セットを使用する必要があります。

**Note**: インターフェースの極性は PC ケースによって異なる場合があります。取り付け前にもう一度ご確認ください。

以下に、参考までに、インターフェース 4/5 を制御対象コンピュータの F_PANEL インターフェースに接続する例をいくつか示します。

??? "10-1ピンPANEL用"

    コントロール パネルへの接続に使用される、制御対象のコンピューターのマザーボード上のピンの列が、以下に示すように 10-1 ピン PANEL である場合。

    ![10-1pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_1.png){class="glboxshadow"}

    接続については、下の図を参照してください。シルクスクリーン印刷 (つまり、HDDLED±、RESET SW、POWER SW、POWERLED+ などの文字) が外側に向かって見え、内側に向かって隠れていないことを確認してください。

    ![10-1pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_2.jpg){class="glboxshadow"}
    <small>正面図</small>

    ![10-1pin panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_3.jpg){class="glboxshadow"}
    <small>背面図</small>

    次に、コンピューター ケースに同梱されているワイヤー セットを使用して、別の ATX ボード インターフェイスをコンピューターの制御ラインに接続します。

??? "20-5ピンPANEL用"

    コントロール パネルへの接続に使用される、制御対象のコンピューターのマザーボード上のピンの列が、以下に示すように 20-5 ピン PANEL である場合。

    ![20-5pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_1.jpg){class="glboxshadow"}

    接続については、下の図を参照してください。シルクスクリーン印刷 (つまり、HDDLED±、RESET SW、POWER SW、POWERLED+ などの文字) が外側に向かって見え、内側に向かって隠れていないことを確認してください。

    ![20-5pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_2.jpg){class="glboxshadow"}
    <small>正面図</small>

    ![20-5pin panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_3.png){class="glboxshadow"}
    <small>背面図</small>

    次に、コンピューター ケースに同梱されているワイヤー セットを使用して、別の ATX ボード インターフェイスをコンピューターの制御ラインに接続します。

??? "20-8ピンPANEL用"

    コントロール パネルへの接続に使用される制御対象コンピューターのマザーボード上のピンの列が、以下に示すように 20-8 ピン PANEL である場合。

    ![20-8pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_1.jpg){class="glboxshadow"}

    接続については、下の図を参照してください。シルクスクリーン印刷 (つまり、HDDLED±、RESET SW、POWER SW、POWERLED+ などの文字) が外側に向かって見え、内側に向かって隠れていないことを確認してください。

    ![20-8pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_2.png){class="glboxshadow"}

    次に、コンピューター ケースに同梱されているワイヤー セットを使用して、別の ATX ボード インターフェイスをコンピューターの制御ラインに接続します。

最終的に接続された ATX ボードを以下に示します。

![atx board connected](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected1.png){class="glboxshadow gl-90-desktop"}

![atx board connected](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected2.png){class="glboxshadow gl-90-desktop"}

次に、ATX ボード ブラケットをコンピュータ ケースに取り付けます。

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install1.png){class="glboxshadow gl-90-desktop"}

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install2.png){class="glboxshadow gl-90-desktop"}

### 3。 ATXボードとKVMを接続します

付属の USB ケーブルを使用して、ATX ボードの Type-C ポートを KVM デバイス (Comet GL-RM1 など) の USB-A ポートに接続します。

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install3.png){class="glboxshadow gl-90-desktop"}

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install4.png){class="glboxshadow gl-90-desktop"}

これでATXボードの取り付けは完了です。

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install5.png){class="glboxshadow gl-90-desktop"}

これで、KVM にログインし、**Accessories** に移動して ATX 電源を制御できるようになりました。

![atx power](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/atx_power.png){class="glboxshadow gl-90-desktop"}

## FAQ

**Q1. GL-ATXPC ボードを GL.iNet 以外の KVM デバイスで使用できますか?**

A1.いいえ。GL-ATXPC ボードは、GL.iNet KVM デバイスのアクセサリです。 GL.iNet KVM と組み合わせて使用​​する必要があります。

---

**Q2. ATX ボードを取り付けた後、KVM を介してリモート デバイスの電源 (オン/オフ) を制御できない場合はどうすればよいですか?**

A2.以下の方法をお試しください。

- PC ケースのフロント パネルにある物理的な電源ボタンを押したときに、被制御デバイスの電源が正常にオン/オフできることを確認します。

- 配線の極性を確認してください。誤った配線を避けるために、被制御デバイスのマザーボード上の POWER SW コネクタの極性を反転してみてください。

    ![connector polarity](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/power-sw-connector.png){class="glboxshadow gl-90-desktop"}

- 被制御デバイスのマザーボード上の F_PANEL インターフェイスに接続するときは、シルクスクリーン印刷 (HDDLED±、RESET SW、POWER SW、POWERLED+ など) が内側に向かって隠れず、外側に向かって見えるようにしてください。

- KVM のファームウェアをアップグレードします。

---

**Q3.単一の GL.iNet KVM を使用して複数の ATX ボードを制御できますか?**

A3。次の GL.iNet KVM は 1 つの ATX ボードのみを制御できます。

* Comet(GL-RM1)
* Comet PoE (GL-RM1PE)
* Cometプロ(GL-RM10)
* Comet 5G (GL-RM10RC)

ただし、Comet X (GL-RM4PE) は、最大 4 枚の ATX ボードを同時にサポートします。 Comet X はリアパネルに 4 つの独立したチャンネルを提供します。各チャンネルには、ビデオ信号送信用の HDMI ポート、キーボードおよびマウス信号送信用の Type-C ポート、および USB 周辺機器 (Fingerbot や ATX ボードなど) 用の USB 2.0 ポートが付属しています。

**Note**: Comet Q (GL-RMQ1) は ATX ボードでは動作しません。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
