# キーボードが期待どおりに入力または出力しない場合はどうすればよいですか

制御機器と被制御デバイスで**異なる入力方法やキーボードレイアウト**を使用している場合、ローカルで入力された「!」、「@」、「#」などの記号や文字がリモート側で正しく表示されない場合があります。

## なぜそうなるのか

KVM は被制御デバイスのキーボードとみなされ、制御側デバイスのキーボードで押したキーは、対応するキーの位置に従って KVM に送信され、被制御デバイスにマッピングされます。 

ただし、制御側デバイスの入力方法/キーボードが被制御デバイスの入力方法/キーボードと一致しない場合、一部の記号/文字のキーボード上の位置が異なるため、被制御側の出力と制御側の入力が一致しなくなります。

![US JIS keyboard comparison](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/apple-keyboards-US-JIS.jpg){class="glboxshadow"}

## ソリューション

一貫したキー マッピングを実現するために、被制御デバイスに対応する言語の入力メソッドまたはキーボードをインストールできます。

??? "Windows"

    1. **Settings** -> **時刻と言語** -> **Language** -> **Preferred Language** に移動します。 [**言語を追加**] をクリックします。

        ![add a language](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/add_language.png){class="glboxshadow"}

    2. インストールする言語を選択してください。 

        ![choose a language](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/choose_language.png){class="glboxshadow"}

??? "MacOS"

    1. Mac で、**アップル メニュー** > **System Settings** を選択し、サイドバーで **Keyboard** をクリックします。 (下にスクロールする必要がある場合があります。)
    
    2. **Text Input** に移動し、**Edit** をクリックします。
    
    3. 「**Add**」ボタンをクリックして、言語を検索します。使用する言語ごとに 1 つ以上の入力ソースを選択し、**Add** をクリックします。
    
    4. 別の言語で書き込みを開始するには、メニュー バーの [入力] メニューで使用する言語を選択します。
    
        [入力] メニューの [**Show Keyboard Viewer**] をクリックすると、現在選択されている言語のキーボード レイアウトを確認できます。
        
        入力ソースを追加すると、メニュー バーに入力メニューが自動的に表示されます。入力ソースの言語は、言語と地域設定の優先言語のリストと、キーボード設定のディクテーション言語 (利用可能な場合) のリストに自動的に追加されます。 

    参考資料: [Mac で別の言語で書く – Apple サポート](https://support.apple.com/guide/mac-help/write-in-another-language-on-mac-mchlp1406/mac){target="_blank"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
