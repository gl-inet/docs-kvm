# Cosa fare se non riesci a controllare il mouse e la tastiera {#what-should-i-do-if-i-cannot-control-the-mouse-and-keyboard}

Se non riesci a controllare il mouse e la tastiera del dispositivo controllato tramite KVM anche quando tutti i cavi sono collegati correttamente, prova le seguenti soluzioni.

1. Controlla i collegamenti.

    Prendiamo come esempio Comet (GL-RM1), che dispone di due porte USB Type-C:

    - Quella laterale è contrassegnata con "5V 2A" ed è destinata all'alimentazione, tramite un alimentatore.
    - Quella posteriore presenta le icone del mouse e della tastiera e va collegata alla porta USB del dispositivo controllato per ricevere i segnali di tastiera e mouse.

    Se inverti questi due collegamenti, il dispositivo KVM non si avvierà e il mouse e la tastiera non risponderanno.

    Verifica che queste due porte Type-C siano collegate correttamente.

    ![gl-rm1 ports](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/gl-rm1-ports.png){class="glboxshadow gl-80-desktop"}

2. Controlla il cavo USB.

    Usa il cavo USB incluso. Assicurati che colleghi la porta USB del dispositivo controllato alla porta USB del KVM e che supporti il trasferimento dei dati.

    Solo i cavi che supportano il trasferimento dei dati consentono di controllare la tastiera e il mouse del dispositivo remoto.

    Ricollega il cavo USB e riavvia il dispositivo controllato.

3. Imposta la modalità del mouse su Relative.

    Accedi al KVM, vai su Settings -> Mouse Mode, seleziona Relative e verifica se il problema si risolve.

    ![mouse mode](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/mouse_mode.jpg){class="glboxshadow"}

4. Disattiva Virtual Media.

    Accedi al KVM, vai su Virtual Media, fai clic sull'icona con i tre puntini e disattiva la funzione.

    ![disable virtual media](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/disable_virtual_media.png){class="glboxshadow" width="422"}

    Quando Virtual Media è attivo, il KVM può simulare un'unità di archiviazione USB collegata al dispositivo controllato. Alcuni dispositivi, tuttavia, disattivano tutti gli ingressi USB quando rilevano un'unità USB sconosciuta, impedendo così al mouse e alla tastiera di rispondere.

5. Modifica l'identità del dispositivo.

    Accedi al KVM, vai su Settings -> System -> Device Identity e modifica l'identità con cui il dispositivo controllato riconosce il KVM.

    ![change device identity](https://static.gl-inet.com/docs/kvm/faq/cannot_control_mouse/change_device_identity.png){class="glboxshadow"}

6. Aggiorna il firmware del KVM all'ultima versione. [Centro download del firmware KVM](https://dl.gl-inet.com/kvm){target="_blank"}

7. Controlla in Gestione dispositivi sul computer controllato se sono presenti driver malfunzionanti.

8. Verifica se il dispositivo controllato è bloccato da un software di sicurezza IT.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
