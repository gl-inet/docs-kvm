# スピーカーとマイクの設定を維持できないのはなぜですか

KVM コンソール ([設定] -> [リモート デバイス設定]) でスピーカーまたはマイクを有効にすると、再起動したり、KVM に再ログインしたり、Web ページを更新したり (ローカル アクセスで) したときに、これらの設定が保持されないことに気づくかもしれません。

代わりに、スピーカーは自動的に無効になり、マイクは、デバイスを再起動するか Web ページを更新した後も有効として表示されますが、ミュートになります。

![speaker mic settings](https://static.gl-inet.com/docs/kvm/faq/speaker_microphone_settings_cannot_be_retained/speaker_microphone_settings.png){class="glboxshadow"}

これは、ブラウザのセキュリティ ポリシーにより、再起動、KVM への再ログイン、または Web ページの更新 (ローカル アクセスの場合) を行うたびに、スピーカーとマイクがデフォルトで無効/ミュートになるためです。必要に応じて手動で有効にすることができます。

以下に示すように、初めてマイクを有効にする場合は認証が必要です。

![browser](https://static.gl-inet.com/docs/kvm/faq/speaker_microphone_settings_cannot_be_retained/google-browser.jpg){class="glboxshadow"}

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
