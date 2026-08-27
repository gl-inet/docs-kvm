# GL.iNet KVM に関する簡単なよくある質問

これは、GL.iNet KVM の簡単な Q&A コレクションで、一般的な基本的な質問にすぐに答えられるように設計されています。

## 基本情報

**Q1. GL.iNet KVM はどのようなデバイスを制御できますか?**

A1. GL.iNet KVM は、ラップトップ、デスクトップ、Raspberry Pi、ミニホストなど、HDMI 出力と USB 入力を使用する任意のデバイスを制御できます。

さらに、Comet Q (GL-RMQ1) は、USB‑C ポートがビデオ出力の DisplayPort Alt Mode をサポートする任意のデバイスを制御できます。 HDMI ポートは必要ありません。これには、特定の iPhone、iPad、Android 携帯電話、MacBook、Mac mini、およびほとんどの最新の Windows ラップトップが含まれますが、これらに限定されません。詳細は[こちら](../user_guide/gl-rmq1/product_overview.md#compatibility)をクリックしてください。

---

**Q2. GL.iNet KVM を使用するには、何らかのソフトウェアをインストールする必要がありますか?**

A2.被制御デバイスにソフトウェアをインストールする必要はなく、Windows、macOS、ChromeOS、Linux などを使用できます。

制御側デバイスに関しては、ソフトウェアをインストールする必要があるかどうかは、KVM にアクセスする方法によって異なります。

??? "近くのコントロール (Comet 5G のみ)"

    **Note**: この方法は、Comet 5G (GL-RM10RC) でのみ使用できます。

    Comet 5G は Wi-Fi Nearby Control を備えており、有線接続を使用せずに迅速なローカル管理を可能にします。 Comet 5G の Wi-Fi ネットワーク モードを AP モードに切り替えるだけで、固有の Wi-Fi SSID が生成されます。 Comet 5G のコンソールに安全にアクセスするには、この SSID に接続します。詳細は[こちら](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control)をクリックしてください。

    AP モードをアクティブにすると、Comet 5G が上流の Wi-Fi から切断され、近くのアクセスのみが提供されます (インターネット接続なし)。

??? "ローカルコントロール(Comet Xのみ)"

    **Note**: この方法は、Comet X (GL-RM4PE) でのみ使用できます。

    Comet X は、ローカルのトラブルシューティング、構成、OS のインストールに最適な、HDMI OUT ポートと 2 つの追加の USB ポートを提供します。モニター、マウス、キーボードを接続するだけで、プラグアンドプレイのローカルハードウェア制御が可能になります。詳細は[こちら](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control)をクリックしてください。

??? "LAN アクセス"

    同じローカル エリア ネットワーク (LAN) 経由で KVM にアクセスする場合は、制御側デバイスにソフトウェアをインストールする必要はありません。

    制御側デバイスでブラウザを開き、アドレス バーに KVM の IP アドレスまたは `glkvm.local` を入力するだけで、KVM にローカルでアクセスできます。
    
    詳しくは[こちら](local_access_via_browser.md){target="_blank"}
    
??? "リモートアクセス"

    - **GLKVM App**
    
        制御側デバイスが Windows、macOS、Android、または iOS を実行している場合は、[GLKVM アプリ ](https://www.gl-inet.com/app-rm/){target="_blank"} をそれにインストールし、KVM にリモートでアクセスし、制御側デバイスにアクセスできます。
        
        詳しくは[こちら](remote_access_via_glkvm_app.md){target="_blank"}
        
    - **Cloud Service**
    
        この方法は、GLKVM アプリをインストールできない、またはインストールしたくない人に最適です。

        KVM をクラウド サービスにバインドすると、制御側デバイスの Web ブラウザに `glkvm.com` と入力することで、KVM にリモートでアクセスできるようになり、GLKVM アプリをインストールしなくても制御側デバイスにアクセスできます。

        詳しくは[こちら](remote_access_via_cloud.md){target="_blank"}
    
    - **Tailscale**
    
        この方法は、手順が多くなりますが、GLKVM アプリやクラウド サービスを使用できない、または使用したくない人に適しています。

        KVM と制御側デバイスを同じ Tailscale アカウントにバインドすると、制御側デバイスの Web ブラウザに KVM の Tailscale 仮想 IP を入力して、制御側デバイスにアクセスすることで、KVM にリモートでアクセスできます。
    
        詳しくは[こちら](remote_access_via_tailscale.md){target="_blank"}

    - **ZeroTier**
    
        この方法は、手順が多くなりますが、GLKVM アプリやクラウド サービスを使用できない、または使用したくない人に適しています。

        KVM と制御側デバイスを同じ ZeroTier ネットワークに参加すると、制御側デバイスの Web ブラウザに KVM の ZeroTier IP を入力して、制御側デバイスにアクセスすることで、KVM にリモートでアクセスできます。
    
        詳しくは[こちら](remote_access_via_zerotier.md){target="_blank"}

    - **NetBird**

        この方法は、手順が増えますが、GLKVM アプリやクラウド サービスを使用できない、または使用したくない人に適しています。

        [NetBird](https://netbird.io/){target="_blank"} は、家庭用およびビジネス用の安全なプライベート ネットワークを構築できるオープンソースのゼロトラスト ネットワーキング プラットフォームです。 WireGuard® ベースのオーバーレイ ネットワークとして、NetBird は、いつでもどこでもデバイスへの安全なアクセスを可能にします。
        
        GL.iNet KVM は NetBird を統合し、リモート アクセス用に NetBird 仮想ネットワークにバインドできるようにします。 

        詳しくは[こちら](remote_access_via_netbird.md){target="_blank"}

---

**Q3. GL.iNet KVM にアクセスするにはどうすればよいですか?**

A3。通常、GL.iNet KVM には、さまざまな方法でローカルまたはリモートでアクセスできます。

- [LAN Web ブラウザ経由でアクセス](local_access_via_browser.md){target="_blank"}
- [クラウドサービスによるリモートアクセス](remote_access_via_cloud.md){target="_blank"}
- [GLKVM アプリ経由のリモート アクセス](remote_access_via_glkvm_app.md){target="_blank"}
- [Tailscale 経由のリモート アクセス](remote_access_via_tailscale.md){target="_blank"}
- [ZeroTier 経由のリモート アクセス](remote_access_via_zerotier.md){target="_blank"}
- [NetBird 経由のリモート アクセス](remote_access_via_netbird.md){target="_blank"}

さらに、一部の GL.iNet KVM モデルは、Nearby Control または Local Control をサポートしており、他のルーターに接続せずにオンサイトでアクセスできます。

- [ニアバイコントロール(Comet 5Gのみ)](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control){target="_blank"}
- [ローカルコントロール(Comet Xのみ)](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control){target="_blank"}

---

**Q4.リモート アクセスを実現するには、GL.iNet KVM のポート (WAN に公開) を開く必要がありますか?**

A4。いいえ。開いているポートやパブリック IP さえも必要ありません。

---

**Q5. GLKVM アプリは ChromeOS/Linux をサポートしていますか?**

A5。いいえ。現在、GLKVM アプリは Chrome または Linux OS へのインストールをサポートしていません。 

制御側デバイスが Chrome/Linux OS を実行している場合、GLKVM アプリをインストールできないため、GLKVM アプリを介した制御側デバイスへのリモート アクセスはサポートされません。

ただし、<u> クラウド サービス</u>、<u>Tailscale</u>、<u>ZeroTier</u>、または <u>NetBird</u> を使用して、リモートアクセスを実現します。詳細については、上記の Q3 を参照してください。

または、Web ブラウザを介してローカルで KVM にアクセスすることもできます。詳細については、上記の Q3 を参照してください。

---

**Q7. Comet (GL-RM1) はワイヤレス ネットワークに接続できますか?**

A7。 No. Comet (GL-RM1) はワイヤレスネットワーク接続をサポートしていません。

インターネットにアクセスするには、イーサネット ケーブルを介してネットワーク デバイス (ルーターなど) に接続する必要があります。

Wi-Fi をサポートする KVM をご希望の場合は、次のモデルを検討してください。

* [Comet Pro (GL-RM10)](https://www.gl-inet.com/products/gl-rm10/){target="_blank"}
* [Comet 5G (GL-RM10RC)](https://www.gl-inet.com/products/gl-rm10rc/){target="_blank"}
* [Comet Q (GL-RMQ1)](https://www.gl-inet.com/products/gl-rmq1/){target="_blank"}

---

## 電力制御

**Q1. GL.iNet KVM はターゲット デバイスの電源をリモートでオン/オフできますか?**

A1。 GL.iNet KVM を使用すると、以下の方法でターゲット デバイスの電源をリモートでオン/オフできます。

- Wake-on-LAN (組み込みソフトウェア サービス)

- [ATX ボード](../user_guide/gl-atx-board/index.md){target="_blank"} (別売り。Comet Q では動作しません。)

- [FingerBot](../user_guide/gl-fgb-01/index.md){target="_blank"} (別売り。Comet Q では動作しません。)

---

**Q2. ATX ボードを使用してリモート電源制御を行うにはどうすればよいですか?**

A2。 [ATX ボード ユーザーガイド](../user_guide/gl-atx-board/index.md){target="_blank"}を参照してください。

---

## 特長

!!! tip

    以下は、いくつかの一般的な機能に関する FAQ です。全機能の詳細については、対応する[ユーザーガイド](../user_guide/index.md)を参照してください。

**Q1. KVM クラウド サービスを使用する必要がありますか?**

A1。いいえ。クラウド サービスはオプションです。 

リモート アクセスにクラウドに依存しない場合は、Tailscale、ZeroTier、NetBird などのサードパーティのオーバーレイ ネットワーク ツールを使用できます。

---

**Q2.単一の GL.iNet KVM を使用して複数のデバイスを制御できますか?**

A2。次の GL.iNet KVM は 1 つのターゲット デバイスのみを制御できます。

* Comet(GL-RM1)
* Comet PoE (GL-RM1PE)
* Cometプロ(GL-RM10)
* Comet 5G (GL-RM10RC)
* CometQ(GL-RMQ1)

ただし、Comet X (GL-RM4PE) は、同時に最大 4 台のターゲット デバイスに接続できますが、一度に制御できるデバイスは 1 台のみです。現場にいる場合はフロント パネルの物理ボタンを使用して、または離れている場合はリモート コンソールを使用して、接続された 4 つのデバイスをすばやく切り替えることができます。

Comet X (GL-RM4PE) は、リアパネルに 4 つの独立したチャンネルを備えています。各チャンネルには、ビデオ信号送信用の HDMI ポート、キーボードおよびマウス信号送信用の Type-C ポート、および USB 周辺機器 (Fingerbot や ATX ボードなど) 用の USB 2.0 ポートが付属しています。

---

**Q3. Wake-on-Lan とは何ですか?**

A3。 Wake-on-LAN (WOL) は、ネットワーク経由でコンピューターまたはデバイスの電源をリモートでオンにしたり、低電力状態から復帰したりできるようにするテクノロジーです。これは、ターゲット デバイスの MAC アドレスを含む「マジック パケット」を送信することで機能し、デバイスの起動をトリガーします。一般的な用途には、リモート管理、省エネスタンバイ構成、集中システム管理などがあります。

---

**Q4. GL.iNet KVM はマウス ジグルをサポートしていますか?**

A4。はい。 KVM コンソールでマウス ジグルを有効にできます。

マウス ジグラー機能は、マウスの微妙な周期的な動きをシミュレートし、リモート会議やサーバー管理中など、長時間非アクティブな状態が続いてコンピューター (つまり、制御対象のデバイス) がスリープ状態になるのを防ぎます。

---

**Q5. GL.iNet KVM は双方向オーディオをサポートしていますか?**

A5。はい。 KVM コンソールでスピーカーとマイクを有効にして、双方向オーディオ伝送を実現できます。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
