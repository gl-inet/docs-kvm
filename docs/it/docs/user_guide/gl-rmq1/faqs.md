# Domande frequenti su Comet Q {#frequently-asked-questions-about-comet-q}

## Informazioni generali { #general }

1. **D: Cosa devo fare se lo schermo di controllo KVM mostra "Unable to Display" quando Comet Q è collegato al dispositivo controllato?**

    R: Il dispositivo controllato non supporta **USB-C DisplayPort Alt Mode**, quindi non può fornire il flusso video in uscita.

    Consultare [questa guida](../../tutorials/how_to_check_usb-c_port_dp_alt_mode.md) per verificare se il dispositivo supporta DisplayPort Alt Mode.

2. **D: Perché il dispositivo di controllo non mostra la tastiera per inserire la password quando lo schermo del dispositivo controllato è bloccato?**

    R: A causa delle restrizioni di sicurezza di iOS/Android, il sistema nasconde la pagina di inserimento della password durante la duplicazione dello schermo o il controllo remoto. Per sbloccare il dispositivo, è possibile inserire direttamente la password di sblocco dal dispositivo di controllo.

3. **D: Perché l'audio non viene trasmesso al dispositivo di controllo quando il dispositivo controllato effettua una chiamata vocale?**

    R: Questo problema si verifica comunemente sugli iPhone e su alcuni dispositivi Android. Quando sul dispositivo controllato vengono usate app per chiamate vocali, come WhatsApp o Microsoft Teams, le restrizioni di iOS/Android consentono l'uscita audio solo tramite gli altoparlanti locali del dispositivo controllato. L'audio non può quindi essere trasmesso al dispositivo di controllo tramite KVM.

    **Suggerimento**: Quando le app per chiamate vocali non sono attive, l'audio multimediale (video, musica, giochi, ecc.) può essere trasmesso normalmente al dispositivo di controllo tramite KVM.

## iOS {#ios}

1. **D: Perché non riesco a regolare il volume di sistema dei dispositivi iOS dopo il collegamento a Comet Q?**

    R: A causa delle limitazioni di iOS, quando un iPhone/iPad si collega a un dispositivo per la duplicazione dello schermo come GL.iNet KVM, impostato come uscita audio, il controllo del volume del sistema non è più disponibile.

2. **D: Perché il dispositivo iOS non mostra il video sul proprio schermo durante lo streaming tramite app video?**

    R: Quando un dispositivo iOS si collega a un dispositivo per la duplicazione dello schermo come GL.iNet KVM, alcune app video, ad esempio YouTube e Netflix, inviano il video tramite **AirPlay** per impostazione predefinita. Il video non viene quindi mostrato sullo schermo del dispositivo iOS. Questo comportamento non può essere disabilitato a livello di sistema.

    Per riprodurre i video anche sullo schermo del dispositivo controllato durante la duplicazione, usare un browser web.

3. **D: Cosa devo fare se la tastiera su schermo del dispositivo iOS scompare dopo il collegamento a Comet Q?**

    R: Probabilmente iOS riconosce Comet Q come una tastiera fisica esterna e nasconde automaticamente la tastiera su schermo. In questo caso, usare la tastiera del dispositivo di controllo o quella virtuale integrata nella console KVM.

    Se occorre comunque usare la tastiera su schermo di iOS, aprire **Settings** > **Accessibility** > **Touch** > **AssistiveTouch**, quindi abilitare **Show Onscreen Keyboard**.

    ![AssistiveTouch](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/assistive_touch.png){class="glboxshadow" width="360"}

4. **D: Durante la duplicazione di un iPhone/iPad in verticale o in orizzontale, il mouse sul dispositivo di controllo resta disallineato anche dopo aver modificato l'orientamento dello schermo nella console KVM. Cosa devo fare?**

    R: Per seguire con precisione il cursore su iPhone o iPad, l'orientamento del giroscopio del dispositivo deve corrispondere a quello dello schermo visualizzato. Durante il controllo remoto, il sistema potrebbe non rilevare correttamente lo stato del giroscopio, causando uno scostamento del mouse.

    Per risolvere il problema, attivare **Portrait Orientation Lock**/**Rotation Lock** sull'iPhone/iPad, in modo da garantire il corretto allineamento del cursore.

    ![Portrait Lock](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/faqs/portrait_lock.png){class="glboxshadow" width="360"}
<br><small>(Portrait Orientation Lock on iPhone)</small>

5. **D: Perché la tastiera non funziona correttamente sui dispositivi iOS, con alcuni tasti che non rispondono o il puntatore del mouse che si sposta da solo?**

    R: In genere questo problema è causato dall'attivazione della funzione **Mouse Keys** sul dispositivo iOS. Mouse Keys consente di spostare il puntatore del mouse usando la tastiera o il tastierino numerico.

    Per risolvere il problema, aprire **Settings** > **Accessibility** > **Touch** > **AssistiveTouch** > **Mouse Keys** e disattivare Mouse Keys.

## Android {#android}

1. **D: Perché non riesco a controllare il dispositivo in modalità mouse assoluta?**

    R: A causa delle limitazioni del sistema operativo Android, i dispositivi Android possono essere controllati solo in modalità mouse relativa.

    Quando si usa l'app mobile GLKVM, coprire completamente il puntatore del mouse con il dito per eseguire le operazioni.

2. **D: Cosa devo fare se lo schermo visualizzato sul dispositivo di controllo non corrisponde a quello del telefono Android controllato?**

    R: Alcuni telefoni Android riconoscono Comet Q come schermo esteso anziché come schermo duplicato. Per risolvere il problema, impostare la modalità di visualizzazione del telefono su **Screen Mirroring**.

    Ad esempio, sui dispositivi Samsung serie S:

    Aprire **Settings** > **Device Connections** > **Samsung DeX** > **Connected Display**, quindi selezionare **Screen Mirroring**.

---

Per altre domande, visitare il [forum della community](https://forum.gl-inet.com){target="_blank"} o [contattarci](https://www.gl-inet.com/contacts/){target="_blank"}.
