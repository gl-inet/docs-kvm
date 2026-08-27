# フィンガーボット (FGB-01) ユーザーガイド

Fingerbot FGB-01 は、リモート電源管理の利便性を高めるための GL.iNet KVM デバイスのアクセサリです。

Fingerbot は物理ボタン エミュレータとして、ターゲット デバイスの電源をリモートでオン/オフするように設計されています。簡単な貼り付け式の取り付け、毎日の使用で 1 年間のバッテリー寿命が特徴で、複雑なセットアップは必要ありません。

**Note**: Comet Q (GL-RMQ1) は Fingerbot では動作しません。

![overview](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/overview.png){class="glboxshadow"}

## パッケージ内容

![package contents](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/package_contents.png){class="glboxshadow"}

- 1×FGB-01
- 1 x ラップトップ スタンド
- 1 x アドオン
-  CR2電池×1個（FGB-01に搭載）
- 1 × 粘着テープ
- 1 x ユーザーガイド

Fingerbot の開封ビデオを以下でご覧ください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/Aeu5yiDEt0Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## インストール

Fingerbot をインストールするには、このビデオを視聴するか、以下の手順に従ってください。

<iframe width="560" height="315" src="https://www.youtube.com/embed/_ExhJHhEcwg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. プラスチック製のバッテリー分離タブを取り外します。

    ![install 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install1.png){class="glboxshadow"}

2. フィンガーボット上部の切り込みから蓋を開けます。

    ![install 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install2.png){class="glboxshadow"}

3. USB Bluetooth レシーバーを見つけて、GL.iNet KVM (例: Comet GL-RM1) の USB ポートに挿入し、フィンガーボットに蓋を戻します。

    ![install 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install3.png){class="glboxshadow"}

    ![install 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install4.png){class="glboxshadow"}

4. 被制御デバイスの電源ボタンの表面を掃除します。

    ![install 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install5.png){class="glboxshadow"}

5. Fingerbot の底部にある粘着テープから保護ステッカーを剥がします。

    ![install 6](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install6.png){class="glboxshadow"}

6. フィンガーボットを被制御デバイスの電源ボタンの近くに貼り付け、ロボット アームが押されたときに物理的な電源ボタンに届くようにします。

    ![install 7](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install7.png){class="glboxshadow"}

7. 被制御デバイスがラップトップの場合は、電源ボタンの近くにブラケット (同梱) を固定し、締めます。 
    
    注: ブラケットは、電源ボタンが側端にある場合にのみ使用してください。

    ![install 8](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install8.png){class="glboxshadow"}

    次に、フィンガーボットをブラケットに貼り付け、ロボット アームが物理的な電源ボタンを押したときに確実に届くようにします。

    ![install 9](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install9.png){class="glboxshadow"}

8. インストールが完了しました。以下に示すように、Fingerbot のロボット アームを押すと電源ボタンに触れ、電源の遠隔制御が可能になります。
    
    ![install 10](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/install10.jpg){class="glboxshadow"}

## セットアップ

1. GL.iNet KVM コンソールにログインします。

2. KVM コンソールで、**Accessories** に移動します。押す時間と強さを調整することで、さまざまな効果を得ることができます。

    ![accessories](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/accessories.jpg){class="glboxshadow"}

    **Note**: アクセサリ設定はインストール後にのみ表示されます。

    - Time: Fingerbot が押す時間。

    - 強さ: 押す強さは軽く押すモードと強く押すモードの 2 段階があります。

        - ライトプレスモード: 短いボタンまたはソフトタッチボタンに最適です。
        
        - 強押しモード: 深いボタンまたはしっかりとしたボタンに最適です。

        ![press mode](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow"}

        **Test Button** (Fingerbot 内、上部カバーを取り外した後に表示) を使用して、好みのプレス レベルを見つけることもできます。

        ![test button](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/test-button.png){class="glboxshadow"}

        1. 初めて押す: フィンガーボットがライトプレスまで拡張されます。

        2. 2 回目のプレス: フィンガーボットがハードプレスまで拡張されます。

        3. 3 回押すと、フィンガーボットが引っ込みます。

## FAQ

**Q1. GL-Fingerbot の USB 受信機はどのプロトコルを使用しますか?**

A1。 Bluetooth プロトコルを使用します。

---

**Q2. Fingerbot 本体は USB Bluetooth レシーバーとペアリングされていますか? USB Bluetooth レシーバーを紛失した場合、別のレシーバーを使用できますか?**

A2。 Fingerbot とその USB Bluetooth レシーバーは独自にペアリングされています。バインドのため、他の受信機をフィンガーボットと一緒に使用することはできません。

---

**Q3. GL-Fingerbot は非 GL.iNet KVM デバイスと互換性がありますか?**

A3。いいえ。GL-Fingerbot は、GL.iNet KVM デバイスのオプションのアクセサリです。 GL.iNet KVM と組み合わせて使用​​する必要があります。

---

**Q4.単一の GL.iNet KVM を使用して複数のフィンガーボットを制御できますか?**

A4。次の GL.iNet KVM は 1 つの Fingerbot のみを制御できます。

* Comet(GL-RM1)
* Comet PoE (GL-RM1PE)
* Cometプロ(GL-RM10)
* Comet 5G (GL-RM10RC)

ただし、Comet X (GL-RM4PE) は、最大 4 つのフィンガーボットを同時にサポートします。 Comet X はリアパネルに 4 つの独立したチャンネルを提供します。各チャンネルには、ビデオ信号送信用の HDMI ポート、キーボードおよびマウス信号送信用の Type-C ポート、および USB 周辺機器 (Fingerbot や ATX ボードなど) 用の USB 2.0 ポートが付属しています。

**Note**: Comet Q (GL-RMQ1) は Fingerbot では動作しません。

---

**Q5.アドオンは何のためにあるのでしょうか?使い方は?**

A5。アドオンは、照明スイッチなどの通常の電源スイッチを制御するように設計されています。 Fingerbot の指はスイッチの一方の側を指し、アドオンはもう一方の側に取り付けられます。 Fingerbot が押し下げられると、スイッチがオンになります。引き戻すとスイッチがオフになります。

ただし、Fingerbot は現在、GL.iNet KVM デバイスでのみ使用できます。 Fingerbot 内の USB Bluetooth レシーバーを見つけ、GL.iNet KVM の USB ポートに挿入すると、GL.iNet KVM を介して Fingerbot をリモートで制御できるようになります。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
