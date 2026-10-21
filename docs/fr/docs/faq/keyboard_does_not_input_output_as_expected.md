# Que faire si le clavier ne produit pas la saisie attendue ? {#what-should-i-do-if-keyboard-does-not-input-or-output-as-expected}

Si les appareils de contrôle et contrôlé utilisent des **méthodes de saisie ou des dispositions de clavier différentes**, les symboles et caractères comme « ! », « @ » ou « # » saisis localement peuvent s’afficher incorrectement à distance.

## Pourquoi cela se produit-il ? {#why-does-it-happen}

L’appareil contrôlé considère le KVM comme un clavier. Les touches pressées sur le clavier de l’appareil de contrôle sont transmises au KVM selon leur position, puis reproduites sur l’appareil contrôlé.

Si les méthodes de saisie ou les dispositions ne correspondent pas, certains symboles ou lettres occupent des positions différentes. La sortie côté appareil contrôlé diffère alors de la saisie côté contrôle.

![Comparaison des claviers US et JIS](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/apple-keyboards-US-JIS.jpg){class="glboxshadow"}

## Solutions {#solutions}

Installez la méthode de saisie ou la disposition de clavier de la langue correspondante sur l’appareil contrôlé pour obtenir une correspondance cohérente des touches.

??? "Windows"

    1. Accédez à **Settings** -> **Time & Language** -> **Language** -> **Preferred Language**. Cliquez sur **Add a language**.

        ![Ajout d’une langue](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/add_language.png){class="glboxshadow"}

    2. Choisissez la langue à installer.

        ![Sélection d’une langue](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/choose_language.png){class="glboxshadow"}

??? "macOS"

    1. Sur votre Mac, choisissez **Apple menu** > **System Settings**, puis cliquez sur **Keyboard** dans la barre latérale (faites défiler si nécessaire).

    2. Accédez à **Text Input**, puis cliquez sur **Edit**.

    3. Cliquez sur **Add**, puis recherchez une langue. Sélectionnez une ou plusieurs sources de saisie pour chaque langue souhaitée et cliquez sur **Add**.

    4. Pour écrire dans une autre langue, sélectionnez-la dans le menu de saisie de la barre des menus.

        Cliquez sur **Show Keyboard Viewer** dans le menu de saisie pour afficher la disposition de la langue sélectionnée.

        Après l’ajout d’une source de saisie, le menu de saisie apparaît automatiquement dans la barre des menus. La langue est également ajoutée aux langues préférées de Language & Region et aux langues de Dictation dans les réglages Keyboard, si disponibles.

    Référence : [Écrire dans une autre langue sur Mac – Assistance Apple](https://support.apple.com/guide/mac-help/write-in-another-language-on-mac-mchlp1406/mac){target="_blank"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
