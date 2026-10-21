# デバイスの USB-C ポートが DP Alt モードをサポートしているかどうかを確認する方法 {#how-to-check-if-your-devices-usb-c-port-supports-dp-alt-mode}

## DP Alt モードとは {#what-is-dp-alt-mode}

DP 代替モード (または DisplayPort 代替モード) は、特定の USB-C ポートに組み込まれた機能で、通常処理するデータと電力に加えて、高品質のビデオ信号の送信を可能にします。

簡単に言うと、1 本の USB-C ケーブルで、携帯電話、タブレット、ラップトップから直接モニター、テレビ、またはプロジェクターにビデオを送信できます。特別なアダプターやドッキング ステーションは必要ありません。 DP Alt モードがない場合、ポートはデータの転送と電力の供給のみが可能です。外部ディスプレイにビデオを出力することはできません。

## なぜそれが重要なのか {#why-it-matters}

DP Alt Mode は、**Comet Q** がデバイスから映像を受信するために必要です。被制御デバイスは、USB-C ポート経由のネイティブ映像出力に対応している必要があります。Comet Q に直接接続する場合、DisplayLink アダプタを使用しても、この機能を追加できるとは限りません。

すべての USB-C ポートが同じように作成されているわけではありません。データと電力だけを運ぶものもあります。他の人はビデオを出力することもできます。コネクタの形状は同じですが、その背後にある機能は異なります。 2 つの USB-C ポートは、見た目は同じでも動作が大きく異なる場合があります。だからこそ、USB-C ディスプレイ アクセサリを購入する前に確認することが重要です。

## DP Alt モードを確認する一般的な方法 {#general-methods-to-verify-dp-alt-mode}

1. **仕様書を確認してください**。

    メーカーの Web サイトで正確なモデルを検索してください。 DisplayPort、DP Alt Mode、ビデオ出力、Thunderbolt などのキーワードを検索します。

2. **ポートのマーキング**を探します。

    A USB-C ポートの横にある D 型の DisplayPort ロゴまたは Thunderbolt 稲妻アイコンは、ビデオ出力機能を示します。

3. **システム設定を確認してください**。

    システム設定は接続済みディスプレイの確認に役立ちますが、特定の USB-C ポートがネイティブの DP Alt Mode に対応しているかを常に判断できるわけではありません。メーカーの仕様と直接接続によるテストも併せて確認してください。各プラットフォームの手順は以下のとおりです。

    - [Windows での確認方法](#how-to-check-on-windows)
    - [Macでの確認方法](#how-to-check-on-mac)
    - [Androidでの確認方法](#how-to-check-on-android)
    - [iPhone＆iPadでの確認方法](#how-to-check-on-iphone-and-ipad)
    - [ハンドヘルド、タブレット、その他のデバイス](#handhelds-tablets-and-other-devices)

4. **簡単なテストを実行します**。

    DP Alt Mode を必要とすることが明記された USB-C - HDMI / DisplayPort ケーブルまたはアダプタを使用して、デバイスをモニターやテレビに接続します。画面のミラーリングや拡張ができれば、そのポートのネイティブ映像出力が機能しています。このテストでは DisplayLink アダプタを使用しないでください。

---

## Windows での確認方法 {#how-to-check-on-windows}

1. `Win + X`を押して、**Device Manager**を開きます。
2. *"USB4"* または *"Thunderbolt"* を含むエントリを探します。ハードウェアの特定には役立ちますが、Device Manager だけでは特定のポートの DP Alt Mode 対応を確認できません。
3. ノートパソコンのユーザーマニュアルやメーカーの製品ページで、対象ポートの仕様を確認します。*"DisplayPort over USB-C"* または *"DP Alt Mode"* を検索してください。
4. Comet Q を直接接続するか、DP Alt Mode を必要とすることが明記されたアダプタを使用してディスプレイを接続します。**Settings** > **System** > **Display** > **Multiple displays** を開き、ディスプレイが検出されるか確認します。

**注意**:

1. **DisplayLink は DP Alt Mode 対応の証拠にはなりません。** DisplayLink は USB データ通信で映像を転送し、USB-A でも動作します。Device Manager の DisplayLink エントリや、DisplayLink ドック経由で動作するディスプレイだけでは、ネイティブの USB-C 映像出力に対応しているとは判断できません。[Synaptics: USB-C と DisplayLink](https://www.synaptics.com/products/displaylink-graphics/usb-c){target="_blank"} を参照してください。

2. ノートパソコンに複数の USB-C ポートがある場合、映像出力に対応するポートは一部だけの可能性があります。各ポートを個別に確認してください。

## Macでの確認方法 {#how-to-check-on-mac}

1. **アップル メニュー** > **About This Mac** > **More Info** をクリックします。
2. 下にスクロールして、**System Report** をクリックします。
3. **Hardware** で、**Thunderbolt / USB4** または **USB** を選択します。
4. Thunderbolt / USB4 にリストされているすべての USB-C ポートは、デフォルトで DisplayPort Alt Mode をサポートします。

**Tip**: USB-C / Thunderbolt ポートを備えたすべての最新の Mac は、すぐに DisplayPort Alt Mode をサポートします。

!!! note "対応機種はこちら"

    - MacBook Neo (A18 Pro)
    - MacBook Air
        - MacBook Air 13 インチ(M5)
        - MacBook Air 15 インチ(M5)
        - MacBook Air 13 インチ(M4)
        - MacBook Air 13 インチ(M3)
        - MacBook Air 13 インチ(M2)
        - MacBook Air 13 インチ(M1、2020)
        - MacBook Air 15 インチ(M4)
        - MacBook Air 15 インチ(M3)
        - MacBook Air 15 インチ(M2、2023)
        - MacBook Air (インテル、2020)
    - MacBook Pro
        - MacBook Pro 14 インチ(M5)
        - MacBook Pro 14 インチ(M5プロ)
        - MacBook Pro 14 インチ(M5以下)
        - MacBook Pro 16 インチ(M5プロ)
        - MacBook Pro 16 インチ(M5以下)
        - MacBook Pro 13 インチ(M2、2022)
        - MacBook Pro 13 インチ(M1、2020)
        - MacBook Pro 13 インチ(インテル、2 ポート、2020)
        - MacBook Pro 13 インチ(インテル、4 ポート、2020)
        - MacBook Pro 14 インチ(M4以下)
        - MacBook Pro 14 インチ(M4プロ)
        - MacBook Pro 14 インチ(M4)
        - MacBook Pro 14 インチ(M3)
        - MacBook Pro 14 インチ(M3 Pro または M3 Max)
        - MacBook Pro 14 インチ(M2 Pro または M2 Max、2023)
        - MacBook Pro 14 インチ(M1 Pro または M1 Max、2021)
        - MacBook Pro 16 インチ(M4以下)
        - MacBook Pro 16 インチ(M4プロ)
        - MacBook Pro 16 インチ(M3 Pro または M3 Max)
        - MacBook Pro 16 インチ(M2 Pro または M2 Max、2023)
        - MacBook Pro 16 インチ(M1 Pro または M1 Max、2021)
        - MacBook Pro 16 インチ(インテル、2019 年)
    - iMac
        - iMac (M4、2 ポート)
        - iMac (M4、4 ポート)
        - iMac (M3、2 ポート)
        - iMac (M3、4 ポート)
        - iMac 21.5 インチ(インテル、2019 年)
        - iMac 21.5 インチ(インテル、2017 年)
        - iMac 24 インチ(M1、2 ポート、2021)
        - iMac 24 インチ(M1、4 ポート、2021)
        - iMac27 インチ(インテル、2020)
        - iMac Pro (インテル、2017)
    - Mac mini
        - Mac mini (M4)
        - Mac mini (M4 Pro)
        - Mac mini (M2 または M2 Pro)
        - Mac mini (M1、2020)
        - Mac mini (インテル、2018)
    - Mac スタジオ
        - Mac スタジオ (M4 Max)
        - Mac スタジオ (M3 UIitra)
        - Mac スタジオ (M2 Max または M2 UItra)
        - Mac Studio (M1 Max または M1 UItra、2022)
    - Mac Pro
        - Mac Pro (M2 UItra)
        - Mac Pro (インテル、2019)

## Androidでの確認方法 {#how-to-check-on-android}

1. 携帯電話の **Settings** を開き、*「ディスプレイ」*、*「HDMI」*、または *「デスクトップ モード」* を検索します。
2. **Samsung DeX**、**Motorola Ready For**、**Huawei EasyProjection**、*"External display"* などの機能を探します。メーカーの資料で、対象モデルが **USB-C による有線ディスプレイ接続**に対応していることを確認してください。ワイヤレス表示機能があるだけでは、DP Alt Mode 対応の証拠にはなりません。
3. 携帯電話がサポートしている場合は、通常、モニターに接続すると *「外部ディスプレイが接続されました」* のような通知が表示されます。
4. Comet Q に直接接続するか、DP Alt Mode を必要とするアダプタを使用してディスプレイに接続し、映像出力を確認してください。USB 情報アプリだけでは、ネイティブ映像出力への対応を確実には判断できません。

**Note**: 多くの低価格 Android スマートフォンは、USB-C を搭載しているにもかかわらず、DP Alt モードを省略しています。 Comet Qご購入前に必ずご確認ください。

!!! note "有線映像出力に対応する Samsung デバイスの例"

    以下の Samsung モデルは、[Samsung の DeX 互換性情報](https://www.samsung.com/us/support/answer/ANS10001955/){target="_blank"} に基づいて確認されています。

    - Galaxy A90 5G
    - ギャラクシーブック
    - ギャラクシーフォールド
    - ギャラクシーノート
        - ギャラクシーノート8
        - Galaxy Note 9
        - Galaxy Note 10 シリーズ
        - Galaxy Note20 シリーズ
    - ギャラクシー S
        - Galaxy Tab S7 / 7+
        - Galaxy Tab S8 / 8+ / S8 ウルトラ
        - Galaxy S8 および S8+
        - Galaxy S9 および S9+
        - Galaxy S10 範囲
        - Galaxy S20 範囲
        - Galaxy S21 範囲
        - Galaxy S22 範囲
        - Galaxy S23 範囲
        - Galaxy S24 範囲
        - Galaxy S25 範囲
    - ギャラクシー タブ
        - Galaxy Tab S4
        - Galaxy Tab S5e
        - Galaxy Tab S6
    - ギャラクシー Z
        - Galaxy Z Flip7
        - Galaxy Z Flip8
        - Galaxy Z Fold2
        - Galaxy Z Fold3
        - Galaxy Z Fold4
        - Galaxy Z Fold7

## iPhone、iPadでの確認方法 {#how-to-check-on-iphone-and-ipad}

1. iPhone 15 シリーズ以降（iPhone 16e と iPhone 17e を除く）は、USB-C ポート経由の DisplayPort Alt Mode に対応しています。対象モデルについては、[Apple のディスプレイ接続に関する資料](https://support.apple.com/en-ie/105099#displays){target="_blank"} を確認してください。
2. iPhone 14 以前は Lightning を使用しているため、互換性がありません。
3. USB-C を備えたすべての iPad モデル (iPad Pro、iPad Air 第 4 世代以降、iPad mini 第 6 世代以降、iPad 第 10 世代以降) はビデオ出力をサポートしています。
4. 古いLightningポートを搭載したiPadには互換性がありません。

!!! note "USB-C 映像出力に対応するモデルの例"

    以下の iPhone モデルは、[Apple の外部ディスプレイに関する資料](https://support.apple.com/en-ie/105099#displays){target="_blank"} に基づいて確認されています。

    - iPhone
        - iPhone 18 Pro
        - iPhone 18 Pro Max
        - iPhone 17 Pro
        - iPhone 17 Pro Max
        - iPhone 17
        - iPhone 16 Pro
        - iPhone 16 Pro Max
        - iPhone 16
        - iPhone 16 プラス
        - iPhone 15 Pro
        - iPhone 15 Pro Max
        - iPhone 15
        - iPhone 15 プラス
    - iPad
        - iPad (A16)
        - iPad (第 10 世代)
    - iPad mini
        - iPad mini (第 6 世代)
        - iPad mini (A17 Pro)
    - iPad Air
        - iPad Air (第 5 世代)
        - iPad Air (第 4 世代)
        - iPad Air 11 インチ (M4)
        - iPad Air 11 インチ (M3)
        - iPad Air 11 インチ (M2)
        - iPad Air 13 インチ (M4)
        - iPad Air 13 インチ (M3)
        - iPad Air 13 インチ (M2)
    - iPad Pro
        - iPad Pro 11 インチ (M5)
        - iPad Pro 11 インチ (M4)
        - iPad Pro 11 インチ (第 4 世代)
        - iPad Pro 11 インチ (第 3 世代)
        - iPad Pro 12.9 インチ (第 5 世代)
        - iPad Pro 12.9 インチ (第 6 世代)
        - iPad Pro 13 インチ (M5)
        - iPad Pro 13 インチ (M4)

## ハンドヘルド、タブレット、その他のデバイス {#handhelds-tablets-and-other-devices}

1. **Steam Deck**、**ROG Ally**、**Lenovo Legion Go** — すべて DP Alt モードをサポートします。
2. **USB-C を搭載したほとんどの Windows タブレット** (Surface Pro 8 以降など) — サポートされています。
3. その他については、公式仕様ページを確認し、キーワード *「DisplayPort」*、*「Alt Mode」*、*「video Output」*、または *「Thunderbolt」* を検索してください。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
