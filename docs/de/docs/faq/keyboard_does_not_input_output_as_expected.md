# Was tun, wenn die Tastatureingabe oder -ausgabe nicht wie erwartet funktioniert

Wenn steuerndes und gesteuertes Gerät **unterschiedliche Eingabemethoden oder Tastaturlayouts** verwenden, werden lokal eingegebene Symbole und Zeichen wie "!", "@", "#" auf der Remote-Seite möglicherweise nicht korrekt angezeigt.

## Warum tritt das auf

Das KVM wird vom gesteuerten Gerät als Tastatur erkannt. Die Tasten, die Sie auf der Tastatur des steuernden Geräts drücken, werden entsprechend den jeweiligen Tastenpositionen an das KVM übertragen und anschließend dem gesteuerten Gerät zugeordnet.

Wenn Eingabemethode oder Tastaturlayout des steuernden Geräts jedoch nicht mit denen des gesteuerten Geräts übereinstimmen, befinden sich manche Symbole oder Buchstaben auf unterschiedlichen Tastenpositionen. Dadurch kann die Ausgabe auf dem gesteuerten Gerät von der Eingabe auf dem steuernden Gerät abweichen.

![US JIS keyboard comparison](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/apple-keyboards-US-JIS.jpg){class="glboxshadow"}

## Lösungen

Installieren Sie auf dem gesteuerten Gerät die Eingabemethode oder Tastatur für die entsprechende Sprache, damit die Tastenzuordnung übereinstimmt.

??? "Windows"

    1. Gehen Sie zu **Settings** -> **Time & Language** -> **Language** -> **Preferred Language**. Klicken Sie auf **Add a language**.

        ![add a language](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/add_language.png){class="glboxshadow"}

    2. Wählen Sie eine zu installierende Sprache aus.

        ![choose a language](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/choose_language.png){class="glboxshadow"}

??? "MacOS"

    1. Wählen Sie auf Ihrem Mac **Apple menu** > **System Settings** und klicken Sie anschließend in der Seitenleiste auf **Keyboard**. (Möglicherweise müssen Sie nach unten scrollen.)

    2. Gehen Sie zu **Text Input** und klicken Sie auf **Edit**.

    3. Klicken Sie auf die Schaltfläche **Add**, suchen Sie nach einer Sprache, wählen Sie eine oder mehrere Eingabequellen für jede gewünschte Sprache aus und klicken Sie anschließend auf **Add**.

    4. Um in einer anderen Sprache zu schreiben, wählen Sie im Input-Menü in der Menüleiste die gewünschte Sprache aus.

        Sie können im Input-Menü auf **Show Keyboard Viewer** klicken, um das Tastaturlayout der aktuell ausgewählten Sprache anzuzeigen.

        Nachdem Sie eine Eingabequelle hinzugefügt haben, wird das Input-Menü automatisch in der Menüleiste angezeigt. Die Sprache der Eingabequelle wird automatisch Ihrer Liste bevorzugter Sprachen in den Einstellungen Language & Region sowie Ihrer Liste der Dictation-Sprachen in den Keyboard-Einstellungen hinzugefügt, sofern verfügbar.

    Referenz: [Write in another language on Mac – Apple Support](https://support.apple.com/guide/mac-help/write-in-another-language-on-mac-mchlp1406/mac){target="_blank"}

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
