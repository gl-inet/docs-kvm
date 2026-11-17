# Cosa fare se il puntatore locale e quello remoto non coincidono? {#what-should-i-do-if-the-local-and-remote-cursors-dont-match}

Se il puntatore locale (sul dispositivo di controllo) non coincide con quello remoto (sul dispositivo controllato), segui i passaggi qui sotto per risolvere il problema.

![cursor misalignment](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/mouse_cursor.png){class="glboxshadow"}

1. Se i puntatori si allineano correttamente quando il mouse è fermo ma perdono la sincronizzazione durante il movimento, controlla la rete su entrambi i dispositivi e assicurati che la connessione sia stabile.

    Puoi anche nascondere il puntatore locale, in modo che nella schermata di controllo compaia solo quello remoto, evitando il problema del disallineamento.

    Nella console del KVM, vai su **Settings** -> **Remote Device Settings** -> **Show Local Cursor** e disattiva l'opzione.

    ![hide local cursor](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/hide_local_cursor.jpg){class="glboxshadow"}

2. Se i puntatori non coincidono nemmeno quando il mouse è fermo e il tuo KVM è un Comet Q (GL-RMQ1), seleziona nuovamente il tipo di dispositivo nella console del KVM. Se il problema persiste, passa al punto successivo.

    ![device type](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/device_type.png){class="glboxshadow"}

3. Se il dispositivo controllato è un portatile, la causa è probabilmente una risoluzione dello schermo errata.

    Verifica il rapporto d'aspetto dello schermo del portatile, quindi regola la risoluzione sul portatile controllato oppure modifica l'impostazione EDID del dispositivo KVM.

    ??? note "Regolare la risoluzione sul portatile controllato"

        **Per macOS**:

        1. Vai su **Settings** -> **Displays** -> **Optimize for**.

            ![mac displays](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos1.png){class="glboxshadow" width="582"}

        2. Seleziona **GLKVM**.

            ![select glkvm](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos2.png){class="glboxshadow" width="582"}

        3. Scegli la risoluzione corrispondente e verifica se i puntatori del mouse si sovrappongono.

            ![resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/macos3.png){class="glboxshadow"}

        **Per Windows**:

        1. Vai su **Settings** -> **System** -> **Displays**.

            ![windows display](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows1.png){class="glboxshadow"}

        2. Scorri fino a **Display resolution** e fai clic sul riquadro a destra.

            ![display resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows2.png){class="glboxshadow"}

        3. Seleziona la risoluzione appropriata, quindi fai clic su **Keep changes** nella finestra visualizzata per applicarla.

            ![display resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows3.png){class="glboxshadow"}

            ![display resolution](https://static.gl-inet.com/docs/kvm/faq/cursor_misalignment/windows4.png){class="glboxshadow"}

    ??? note "Modificare l'impostazione EDID del dispositivo KVM"

        EDID, acronimo di Extended Display Identification Data, consente di selezionare automaticamente i parametri di visualizzazione ottimali. L'EDID predefinito è adatto alla maggior parte delle situazioni e in genere non richiede modifiche. Consulta [Come configurare l'EDID per un KVM GL.iNet](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} per i dettagli.

        Se hai modificato l'EDID ma lo schermo non si aggiorna, prova a riavviare il dispositivo controllato.

4. Se il dispositivo controllato non è un portatile, ad esempio un PC desktop collegato a un monitor esterno, verifica il rapporto d'aspetto del suo schermo principale e imposta l'EDID del KVM di conseguenza. Consulta [Come configurare l'EDID per un KVM GL.iNet](../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} per i dettagli.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
