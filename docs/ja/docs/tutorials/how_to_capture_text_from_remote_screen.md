# リモート画面からテキストをキャプチャする方法

テキスト認識機能を使用すると、リモート画面上の領域を選択してテキストを簡単に抽出できます。これは光学式文字認識 (OCR) テクノロジーによって駆動され、ファームウェア v1.9.0 で導入されました。

この機能を使用すると、リモート画面 (つまり、被制御デバイス) からテキストを簡単にキャプチャし、それを制御側デバイスにコピーできます。

リモート画面からテキストをキャプチャするには、次の手順に従います。

## Firmware v1.10 以降

1. KVM コンソールにログインし、**Toolbox** -> **OCR** に移動します。下向き矢印をクリックし、中国語、英語、バイリンガル（Zh/En）など、使用する認識言語を選択します。

    ![OCR recognition 1](https://static.gl-inet.com/docs/kvm/tutorials/text_recognition/ocr_recognition_1.png){class="glboxshadow"}

2. **Capture** をクリックすると、リモート画面が暗くなります。テキストキャプチャを終了する場合は、**Cancel** をクリックします。

    ![OCR recognition 2](https://static.gl-inet.com/docs/kvm/tutorials/text_recognition/ocr_recognition_2.png){class="glboxshadow"}

3. 以下のように、抽出するテキストを囲むように範囲を指定します。

    ![OCR recognition 3](https://static.gl-inet.com/docs/kvm/tutorials/text_recognition/ocr_recognition_3.png){class="glboxshadow"}

4. 選択した領域内のテキストが自動的に認識されます。認識されたテキストは、必要に応じてコピーできます。

    ![OCR recognition 4](https://static.gl-inet.com/docs/kvm/tutorials/text_recognition/ocr_recognition_4.png){class="glboxshadow"}

## Firmware v1.9 以前

1. KVM コンソールにログインします。下向き矢印をクリックして、中国語、英語、バイリンガル (Zh/En) など、優先する認識言語を選択します。

    ![text recognition 1](https://static.gl-inet.com/docs/kvm/tutorials/text_recognition/1.png){class="glboxshadow"}

2. ツールバーの上部中央にある **"T"** アイコンをクリックすると、リモート画面が暗くなります。

    ![text recognition 2](https://static.gl-inet.com/docs/kvm/tutorials/text_recognition/2.png){class="glboxshadow"}

3. 以下に示すように、抽出するテキストの周囲にボックスを描画します。

    ![text recognition 3](https://static.gl-inet.com/docs/kvm/tutorials/text_recognition/3.png){class="glboxshadow"}

4. システムは、選択した領域内のテキストを自動的に識別します。必要に応じて、認識されたテキストをコピーできます。

    ![text recognition 4](https://static.gl-inet.com/docs/kvm/tutorials/text_recognition/4.png){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
