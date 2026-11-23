# GL.iNet KVM を工場出荷時の設定に戻す方法 {#how-do-i-factory-reset-my-glinet-kvm}

## 方法 1：本体のリセットボタンを使う {#method-1-use-the-physical-reset-button}

KVM の電源が入っており、起動が完了していることを確認します。

本体の RESET ボタンを **8～10 秒間**押し続けてから放します。KVM にリセット用の穴がある場合は、ピンで穴の中のボタンを 8 秒間押し続けてから放します。Comet X（GL-RM4PE）では、前面パネルの切り替えボタンを使用します。

KVM が自動的に再起動するまで待ちます。リセット中は電源を切らないでください。

KVM の電源を入れるときにリセットボタンを押し続けないでください。接続先のコンピューターや ATX ボードのリセットボタンは使用しないでください。

## 方法 2：ローカル Web インターフェースを使う {#method-2-use-the-local-web-interface}

コンピューターと KVM を同じローカルネットワークに接続します。ブラウザで KVM のローカル IP アドレスを開き、ログインします。詳しくは [ブラウザ経由で KVM にローカルでアクセスする方法](local_access_via_browser.md) を参照してください。

KVM のファームウェアが v1.10 以降の場合は、右上の **Settings** を開き、**System** -> **Reset Device** に移動します。**Reset** をクリックして確定し、KVM が自動的に再起動するまで待ちます。リセット中は電源を切らないでください。

![reset 1](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset1.png){class="glboxshadow"}

KVM のファームウェアが v1.9 以前の場合は、左上の **Settings** を開き、**System** -> **Reset KVM** に移動します。**Reset** をクリックして確定し、KVM が自動的に再起動するまで待ちます。リセット中は電源を切らないでください。

![reset 2](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset2.png){class="glboxshadow"}

## リセット後 {#after-the-reset}

工場出荷時の設定に戻すと、KVM のカスタム設定が消去されます。再起動後に KVM のローカル IP アドレスが変わる場合があります。ローカル Web インターフェースを開き直し、初期設定の案内に従って管理者パスワードを設定してから、必要な項目を手動で設定し直します。

---

まだ質問がありますか？ [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
