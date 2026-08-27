# リモート画面にデスクトップの壁紙しか表示されない場合はどうすればよいですか

KVM 経由で被制御デバイスにアクセスするときに、デスクトップの壁紙のみが表示され、操作が応答しない場合は、被制御デバイスが **Extend Displays** モードで構成された複数のモニターを使用している可能性があります。

この問題を解決するには、被制御デバイスの表示モードを **複製表示** (Windows) または **ミラー表示** (macOS) に切り替える必要があります。

オペレーティング システムに応じて、対応するソリューションを選択します。

=== 「ウィンドウズ」
    Windows10 を例に挙げます。 **これらのディスプレイを拡張** が有効になっている場合は、以下の手順に従って **複製ディスプレイ** に切り替えます。

    ![extend display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/extend_displays.jpg){class="glboxshadow"}

    1. 被制御デバイスで、**Settings** -> **System** -> **Display** に移動します。

        ![win10 system settings](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/win10_system_settings.png){class="glboxshadow"}

    2. [ディスプレイ] ページで、下にスクロールして [**複数のディスプレイ**] を見つけます。

    3. 拡張ディスプレイから**複製ディスプレイ**に切り替えます。

        ![duplicate display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/duplicate_displays.jpg){class="glboxshadow"}

    4. [**変更を維持**] をクリックします。

        ![keep changes](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/keep_changes.png){class="glboxshadow"}

    次に、被制御デバイスに正常にアクセスできるか確認してください。

=== 「マコス」
    1. 画面の左上隅にあるアップル メニューをクリックし、**System Settings** を選択します。

    2. サイドバーを下にスクロールして、**Displays** を選択します。

        ![mac system settings](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-system-settings.png){class="glboxshadow"}

    3. レイアウト ビューで、**外部ディスプレイ**をクリックします。 MacBook の画面と接続されているモニターが表示されます。

    4. **使用方法** ドロップダウン メニューをクリックし、**ミラー モード** (通常は内蔵ディスプレイのミラー) を選択します。

        ![mac mirror display](https://static.gl-inet.com/docs/kvm/faq/can_only_see_desktop_wallpaper_when_using_glkvm/mac-mirror-display.png){class="glboxshadow"}

    セットアップ後は、被制御デバイス上のデスクトップ全体とすべてのアプリケーション ウィンドウにリモートからアクセスできるようになります。

!!! note
    この解決策は、拡張表示モードによって引き起こされる表示の問題にのみ適用されます。ミラーリングを有効にしても問題が解決しない場合は、デバイスがローカル ユーザー ログインを完了し、システム ログイン画面でスタックしていないことを確認してください。

---

まだ質問がありますか? [コミュニティ フォーラム](https://forum.gl-inet.com){target="_blank"} または [お問い合わせ](https://www.gl-inet.com/contacts/){target="_blank"} にアクセスしてください。
