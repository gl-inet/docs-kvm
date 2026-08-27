# デバイスの USB-C ポートが DP Alt モードをサポートしているかどうかを確認する方法

## DP Alt モードとは

DP 代替モード (または DisplayPort 代替モード) は、特定の USB-C ポートに組み込まれた機能で、通常処理するデータと電力に加えて、高品質のビデオ信号の送信を可能にします。

簡単に言うと、1 本の USB-C ケーブルで、携帯電話、タブレット、ラップトップから直接モニター、テレビ、またはプロジェクターにビデオを送信できます。特別なアダプターやドッキング ステーションは必要ありません。 DP Alt モードがない場合、ポートはデータの転送と電力の供給のみが可能です。外部ディスプレイにビデオを出力することはできません。

## なぜそれが重要なのか

DP Alt モードは、**Comet Q** にとって重要です。Comet Q はデバイスからビデオを受信するために Alt モードに依存しているためです。 USB-C ポートがサポートしている場合、Comet Q はプラグ アンド プレイで動作します。そうしないと、どの外部ディスプレイ アダプタもこの制限を解決できません。

すべての USB-C ポートが同じように作成されているわけではありません。データと電力だけを運ぶものもあります。他の人はビデオを出力することもできます。コネクタの形状は同じですが、その背後にある機能は異なります。 2 つの USB-C ポートは、見た目は同じでも動作が大きく異なる場合があります。だからこそ、USB-C ディスプレイ アクセサリを購入する前に確認することが重要です。

## DP Alt モードを確認する一般的な方法

1. **仕様書を確認してください**。

    メーカーの Web サイトで正確なモデルを検索してください。 DisplayPort、DP Alt Mode、ビデオ出力、Thunderbolt などのキーワードを検索します。

2. **ポートのマーキング**を探します。

    A USB-C ポートの横にある D 型の DisplayPort ロゴまたは Thunderbolt 稲妻アイコンは、ビデオ出力機能を示します。

3. **システム設定を確認してください**。

    ご使用のオペレーティング システムは、USB-C ポートが外部ディスプレイ出力をサポートしているかどうかを検出できます。以下のプラットフォーム固有の手順を参照してください。

    - [Windows での確認方法](#how-to-check-on-windows)
    - [Macでの確認方法](#how-to-check-on-mac)
    - [Androidでの確認方法](#how-to-check-on-android)
    - [iPhone＆iPadでの確認方法](#how-to-check-on-iphone-and-ipad)
    - [ハンドヘルド、タブレット、その他のデバイス](#handhelds-tablets-and-other-devices)

4. **簡単なテストを実行します**。

    USB-C - HDMI / DisplayPort ケーブルを介してデバイスをモニターまたはテレビに接続します。画面がディスプレイをミラーリングまたは拡張している場合、DP Alt モードは適切に機能しています。

---

## Windows での確認方法

1. `Win + X`を押して、**Device Manager**を開きます。
2. **ユニバーサル シリアル バス コントローラー**を展開し、*"USB4"*、*"Thunderbolt"*、または *"DisplayLink"* を含むエントリを探します。
3. または、**Settings** > **System** > **Display** > **複数のディスプレイ**を開きます。 Comet Q (または別のディスプレイ) を接続すると、モニターが表示されるはずです。
4. ラップトップのユーザー マニュアルまたはメーカーの製品ページを確認することもできます。*「DisplayPort over USB-C」* または *「DP Alt Mode」* を検索してください。

**Note**: ラップトップに複数の USB-C ポートがある場合、一部のポートのみがビデオ出力をサポートする可能性があります。各ポートを個別に確認してください。

## Macでの確認方法

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

## Androidでの確認方法

1. 携帯電話の **Settings** を開き、*「ディスプレイ」*、*「HDMI」*、または *「デスクトップ モード」* を検索します。
2. **Samsung DeX**、**Motorola Ready For**、**Huawei EasyProjection**、または *「外部ディスプレイ」* などの機能を探します。存在する場合、デバイスの USB-C ポートは DP Alt モードをサポートしています。
3. 携帯電話がサポートしている場合は、通常、モニターに接続すると *「外部ディスプレイが接続されました」* のような通知が表示されます。
4. *USB Device Info* などの無料アプリをインストールして、ポートの機能を検査することもできます。

**Note**: 多くの低価格 Android スマートフォンは、USB-C を搭載しているにもかかわらず、DP Alt モードを省略しています。 Comet Qご購入前に必ずご確認ください。

!!! note "Samsung を例として、サポートされているモデルを次に示します。"

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
        - ギャラクシー Z フリップ
        - Galaxy Z Fold2
        - Galaxy Z Fold3
        - Galaxy Z Fold4
        - Galaxy Z Fold7

## iPhone、iPadでの確認方法

1. iPhone 15 シリーズ以降はすべて、USB-C ポートを通じて DisplayPort Alt モードをサポートしています。
2. iPhone 14 以前は Lightning を使用しているため、互換性がありません。
3. USB-C を備えたすべての iPad モデル (iPad Pro、iPad Air 第 4 世代以降、iPad mini 第 6 世代以降、iPad 第 10 世代以降) はビデオ出力をサポートしています。
4. 古いLightningポートを搭載したiPadには互換性がありません。

!!! note "対応機種はこちら"

    - iPhone
        - iPhone 17 Pro
        - iPhone 17 Pro Max
        - iPhone 17
        - iPhone 16 Pro
        - iPhone 16 Pro Max
        - iPhone 16
        - iPhone 16 プラス
        - iPhone 15 Pro
        - iPhone 15 ProMax
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

## ハンドヘルド、タブレット、その他のデバイス

1. **Steam Deck**、**ROG Ally**、**Lenovo Legion Go** — すべて DP Alt モードをサポートします。
2. **Nintendo Switch / Switch 2** — DP Alt モードをサポートします (これがドックからテレビへの出力方法です)。
3. **USB-C を搭載したほとんどの Windows タブレット** (Surface Pro 8 以降など) — サポートされています。
4. その他については、公式仕様ページを確認し、キーワード *「DisplayPort」*、*「Alt Mode」*、*「video Output」*、または *「Thunderbolt」* を検索してください。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
