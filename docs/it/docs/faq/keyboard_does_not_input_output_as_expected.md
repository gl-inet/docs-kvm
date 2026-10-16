# Cosa fare se la tastiera non produce l'input o l'output previsto {#what-shoud-i-do-if-keyboard-does-not-input-or-output-as-expected}

Se il dispositivo di controllo e il dispositivo controllato usano **metodi di input o layout di tastiera diversi**, i simboli e i caratteri digitati localmente, come "!", "@" e "#", potrebbero non essere visualizzati correttamente sul dispositivo remoto.

## Perché succede {#why-does-it-happen}

Il dispositivo controllato riconosce il KVM come una tastiera. I tasti premuti sulla tastiera del dispositivo di controllo vengono trasmessi al KVM in base alla loro posizione e quindi associati ai tasti del dispositivo controllato.

Se però il metodo di input o il layout di tastiera non corrisponde tra i due dispositivi, alcuni simboli e lettere occupano posizioni diverse sulla tastiera. Di conseguenza, l'output del dispositivo controllato non corrisponde all'input del dispositivo di controllo.

![US JIS keyboard comparison](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/apple-keyboards-US-JIS.jpg){class="glboxshadow"}

## Soluzioni {#solutions}

Sul dispositivo controllato puoi installare il metodo di input o il layout di tastiera della lingua corrispondente, in modo da ottenere un'associazione coerente dei tasti.

??? "Windows"

    1. Vai su **Settings** -> **Time & Language** -> **Language** -> **Preferred Language**. Fai clic su **Add a language**.

        ![add a language](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/add_language.png){class="glboxshadow"}

    2. Scegli la lingua da installare.

        ![choose a language](https://static.gl-inet.com/docs/kvm/faq/keyboard_input_output_does_not_work_as_expected/choose_language.png){class="glboxshadow"}

??? "MacOS"

    1. Sul Mac, scegli **Apple menu** > **System Settings**, quindi fai clic su **Keyboard** nella barra laterale. Potrebbe essere necessario scorrere verso il basso.

    2. Vai su **Text Input**, quindi fai clic su **Edit**.

    3. Fai clic sul pulsante **Add** e cerca una lingua. Seleziona una o più sorgenti di input per ogni lingua che vuoi usare, quindi fai clic su **Add**.

    4. Per iniziare a scrivere in un'altra lingua, seleziona quella desiderata nel menu Input della barra dei menu.

        Puoi fare clic su **Show Keyboard Viewer** nel menu Input per visualizzare il layout della tastiera della lingua attualmente selezionata.

        Dopo aver aggiunto una sorgente di input, il menu Input viene mostrato automaticamente nella barra dei menu. La lingua della sorgente di input viene aggiunta automaticamente all'elenco delle lingue preferite nelle impostazioni Language & Region e all'elenco delle lingue di Dictation, se disponibile, nelle impostazioni Keyboard.

    Riferimento: [Scrivere in un'altra lingua sul Mac – Supporto Apple](https://support.apple.com/guide/mac-help/write-in-another-language-on-mac-mchlp1406/mac){target="_blank"}

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
