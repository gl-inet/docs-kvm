# Windows への GLKVM アプリのインストールに失敗しました: 「コードの実行を続行できません」

Windows に GLKVM アプリをインストールすると、「VCRUNTIME140_1.dll が見つからないため、コードの実行を続行できません」というエラーが発生する場合があります。

![system error](https://static.gl-inet.com/docs/kvm/faq/failed_to_install_glkvm_app/system_error.png){class="glboxshadow"}

このエラーは、Visual C++ ランタイムの依存関係が欠落しているために発生します。アプリには、Visual C++ 再頒布可能パッケージによって提供される特定の DLL ファイルが必要です。

次の手順に従います。

1. Microsoft の公式 Web サイト [こちら ](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170){target="_blank"} から、Visual Studio 用の最新の Visual C++ 再頒布可能パッケージをダウンロードします。

2. パッケージをインストールし、コンピューターを再起動します。

    一部のセキュリティ ツールがインストール ファイルを誤ってブロックする可能性があるため、ウイルス対策ソフトウェアを一時的に無効にします。

    ??? "Visual C++ の依存関係が正しくインストールされているかどうかを確認するにはどうすればよいですか?"

        1. Windows では、[コントロール パネル] > [プログラム] > [プログラムと機能] に移動します。

        2. 「Microsoft Visual C++ 2015-2022 Redistributable」(x64/x86) のようなエントリを探します。見つからない場合は、上のリンクからインストールしてください。

3. GLKVM アプリ インストーラーを再実行します。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
