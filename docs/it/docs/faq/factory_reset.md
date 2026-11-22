# Come ripristinare le impostazioni di fabbrica del KVM GL.iNet? {#how-do-i-factory-reset-my-glinet-kvm}

## Metodo 1 – Usa il pulsante fisico di ripristino {#method-1-use-the-physical-reset-button}

Assicurati che il KVM sia acceso e abbia completato l'avvio.

Tieni premuto il pulsante fisico RESET per **8-10 secondi**, quindi rilascialo. Se il KVM ha un foro di ripristino, usa uno spillo per tenere premuto il pulsante all'interno del foro per 8 secondi, quindi rilascialo. Su Comet X (GL-RM4PE), usa il pulsante di commutazione sul pannello anteriore.

Attendi che il KVM si riavvii automaticamente. Non scollegare l'alimentazione durante il ripristino.

Non tenere premuto il pulsante di ripristino mentre accendi il KVM. Non usare il pulsante di ripristino del computer collegato o della scheda ATX.

## Metodo 2 – Usa l'interfaccia web locale {#method-2-use-the-local-web-interface}

Collega il computer e il KVM alla stessa rete locale. Apri l'indirizzo IP locale del KVM in un browser e accedi. Consulta [Come accedere al KVM localmente tramite browser](local_access_via_browser.md).

Se sul KVM è installato il firmware v1.10 o successivo, apri **Settings** nell'angolo in alto a destra e vai a **System** -> **Reset Device**. Fai clic su **Reset**, conferma e attendi che il KVM si riavvii automaticamente. Non scollegare l'alimentazione durante il ripristino.

![reset 1](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset1.png){class="glboxshadow"}

Se sul KVM è installato il firmware v1.9 o precedente, apri **Settings** nell'angolo in alto a sinistra e vai a **System** -> **Reset KVM**. Fai clic su **Reset**, conferma e attendi che il KVM si riavvii automaticamente. Non scollegare l'alimentazione durante il ripristino.

![reset 2](https://static.gl-inet.com/docs/kvm/faq/factory_reset/reset2.png){class="glboxshadow"}

## Dopo il ripristino {#after-the-reset}

Il ripristino delle impostazioni di fabbrica cancella le impostazioni personalizzate del KVM. L'indirizzo IP locale del KVM potrebbe cambiare dopo il riavvio. Apri di nuovo l'interfaccia web locale, segui le istruzioni della configurazione iniziale per impostare una password di amministratore e riconfigura manualmente le impostazioni necessarie.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
