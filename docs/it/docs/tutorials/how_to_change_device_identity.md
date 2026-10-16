# Come modificare l'identità del dispositivo KVM {#how-to-change-kvm-device-identity}

## Che cos'è l'identità del dispositivo KVM {#what-is-kvm-device-identity}

L'identità del dispositivo KVM GL.iNet è l'identificativo che permette al dispositivo collegato di riconoscere e distinguere il KVM durante la comunicazione.

In genere, il KVM dispone di una porta Type-C, come mostrato di seguito, che si collega alla porta USB del dispositivo controllato per simulare periferiche, ad esempio tastiera, mouse, unità USB e microfono, oltre a un lettore CD-ROM.

![gl-rm1 type-c](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/gl-rm1-type-c.png){class="glboxshadow gl-60-desktop"}

Quando fai clic con il mouse, digiti sulla tastiera o usi il microfono sul dispositivo di controllo, questi segnali vengono trasmessi da remoto al dispositivo KVM fisico. Il KVM li inoltra quindi al dispositivo controllato tramite la sua porta Type-C.

Il KVM viene pertanto generalmente riconosciuto come un dispositivo composito che emula diverse periferiche collegate alle porte USB del dispositivo controllato.

![device identity principle](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/principle.png){class="glboxshadow"}

!!! Note "Nota"

    Se il metodo di input o il layout di tastiera del dispositivo di controllo non corrisponde a quello del dispositivo controllato, alcuni simboli e lettere potrebbero occupare posizioni diverse sulla tastiera. L'output del dispositivo controllato può quindi differire dall'input del dispositivo di controllo. Fai clic [qui](../faq/keyboard_does_not_input_output_as_expected.md) per i dettagli.

## Perché modificare l'identità del dispositivo {#why-change-device-identity}

Poiché il KVM GL.iNet emula contemporaneamente più dispositivi di interazione, il dispositivo controllato lo riconosce come un insieme di periferiche: un monitor, diversi dispositivi USB come mouse e tastiera e un'unità USB.

L'identità predefinita del dispositivo è **GLKVM**. Nelle impostazioni di sistema del dispositivo controllato, quindi, viene visualizzato come GLKVM o Glinet Composite Device. In genere questo non crea inconvenienti, perché tali impostazioni sono visibili solo agli utenti stessi.

![device identity default](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_default.png){class="glboxshadow"}
<small>(Impostazioni Bluetooth & devices)</small>

![speaker settings](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/speaker.png){class="glboxshadow"}
<small>(Impostazioni dell'altoparlante)</small>

Potrebbe tuttavia essere necessario modificare l'identità del KVM nei seguenti casi.

??? "Scenario 1: evitare gli avvisi del software di monitoraggio sul computer dell'ufficio"

    Se il dispositivo controllato è un computer dell'ufficio, potrebbe disporre di software di monitoraggio integrato o installato. Questi strumenti possono considerare l'accesso remoto tramite KVM un'attività anomala, generare avvisi e perfino inviare segnalazioni ai sistemi IT.

    Modificare l'identità del KVM può contribuire a evitare queste notifiche superflue, mantenendo le normali funzioni di controllo remoto.

??? "Scenario 2: nascondere l'uso remoto del KVM durante la condivisione dello schermo nelle riunioni online"

    Durante una riunione online con condivisione dello schermo, le impostazioni di sistema del dispositivo controllato, ad esempio Bluetooth & devices, possono mostrare l'identità predefinita del KVM. Questo può rivelare ai partecipanti l'uso dell'accesso remoto tramite KVM, cosa che alcuni utenti potrebbero preferire evitare.

    Modificando l'identità del dispositivo, il KVM rimane nascosto nelle schermate condivise.

    ![screen sharing](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/screen_sharing.png){class="glboxshadow"}
    <small>(Condivisione dello schermo)</small>

??? "Scenario 3: risolvere la mancata risposta di mouse e tastiera sul dispositivo controllato"

    Se non riesci a controllare il mouse e la tastiera del dispositivo controllato tramite KVM, prova a modificare l'identità del KVM per evitare problemi di compatibilità e consentire una corretta trasmissione dei segnali tra i dispositivi.

## Limiti della personalizzazione dell'identità del dispositivo {#limitations-of-device-identity-customization}

!!! Warning "I software di rilevamento comportamentale possono comunque identificare il KVM"

    Indipendentemente da come personalizzi l'identità USB, la **struttura** dei dispositivi virtualizzati, come tastiera, mouse, microfono e fotocamera, può comunque apparire sospetta ai software di rilevamento comportamentale.

    Il problema di fondo è che tutte queste periferiche virtualizzate appartengono a un **unico dispositivo USB composito**. Un dispositivo composito che include solo tastiera e mouse è abbastanza comune: molti ricevitori wireless per tastiera e mouse, come Logitech Unifying, presentano una struttura simile. Un unico dispositivo USB composito che include contemporaneamente **tastiera, mouse e microfono**, invece, è estremamente raro nell'uso reale.

    Modificare soltanto l'identità del dispositivo **potrebbe quindi non essere sufficiente** a evitare il rilevamento da parte di software avanzati di monitoraggio o analisi comportamentale.

## Come modificare l'identità del dispositivo {#how-to-change-device-identity}

### Firmware v1.10 e versioni successive {#firmware-v110-and-above}

1. Accedi al KVM e vai su **Settings** in alto a destra. Nella sezione **USB Devices**, individua **Device Identity** e personalizzala.

    ![identity customize1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize1.png){class="glboxshadow"}

2. Nella finestra visualizzata, fai clic su **Confirm** per riavviare.

    ![identity customize2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize2.png){class="glboxshadow"}

3. Dopo il riavvio, Device Identity risulterà modificata nella console del KVM.

    ![identity customize3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize3.png){class="glboxshadow"}

4. Verifica l'identità del dispositivo. Nell'esempio seguente, il dispositivo controllato usa Windows 11 Pro.

    Sul dispositivo controllato, vai su **Settings** -> **Bluetooth & devices**. I dispositivi di input e audio verranno riconosciuti con le identità impostate.

    ![identity customize4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/1.10_customize4.png){class="glboxshadow"}

### Firmware v1.9 e versioni precedenti {#firmware-v19-and-earlier}

1. Accedi al KVM e vai su **Settings** -> **System** -> **Device Identity**. Seleziona un'identità predefinita dal menu a discesa.

    ![identity customize1](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize1.jpg){class="glboxshadow"}

    In alternativa, fai clic su **Customize** e inserisci i parametri desiderati nella finestra visualizzata.

    ![identity customize2](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize2.jpg){class="glboxshadow"}

2. Nella finestra visualizzata, fai clic su **Confirm** per riavviare.

    ![identity customize3](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize3.png){class="glboxshadow"}

3. Dopo il riavvio, Device Identity risulterà modificata nella console del KVM.

    ![identity customize4](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/customize4.jpg){class="glboxshadow"}

4. Verifica l'identità del dispositivo. Nell'esempio seguente, il dispositivo controllato usa Windows 10 Pro.

    Sul dispositivo controllato, vai su **Settings** -> **Bluetooth & devices**. I dispositivi di input e audio verranno riconosciuti con le identità impostate.

    ![identity customize5](https://static.gl-inet.com/docs/kvm/tutorials/customize_device_identity/identity_modified.png){class="glboxshadow"}

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
