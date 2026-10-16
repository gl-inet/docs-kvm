# Come impostare l'EDID del KVM GL.iNet {#how-to-set-edid-for-glinet-kvm}

## Che cos'è l'EDID {#what-is-edid}

EDID, acronimo di Extended Display Identification Data, è un formato di dati standard definito dalla Video Electronics Standards Association (VESA). Viene memorizzato nella memoria non volatile dello schermo e contiene informazioni essenziali come produttore, risoluzione massima e frequenza di aggiornamento. Dispositivi come i computer possono leggere l'EDID per regolare automaticamente i parametri del segnale di uscita e ottenere la migliore visualizzazione possibile.

In genere, quando computer, portatili e console di gioco vengono collegati a uno schermo, ne leggono automaticamente l'EDID per impostare parametri video appropriati, evitando problemi come immagini sfocate e sfarfallio e offrendo una visualizzazione nitida e stabile.

Le impostazioni EDID del KVM GL.iNet consentono di selezionare automaticamente i parametri ottimali dello schermo. Quando il KVM è collegato al dispositivo controllato, può regolare automaticamente l'uscita video leggendo l'EDID dello schermo per ottenere la migliore immagine possibile.

## EDID predefiniti {#preset-edid}

Nella console del KVM GL.iNet, vai su **Settings** -> **Video** -> **EDID**. Sono disponibili alcune impostazioni EDID predefinite.

![edid preset](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_preset.jpg){class="glboxshadow"}

**L'EDID predefinito del KVM GL.iNet è già adatto alla maggior parte delle situazioni e in genere non richiede modifiche**.

In situazioni particolari, ad esempio per configurare UEFI/BIOS o personalizzare risoluzione e frequenza di aggiornamento, puoi selezionare un valore predefinito, come 1920×1280/AUO/60HZ.

## EDID personalizzato {#custom-edid}

Se non trovi un codice EDID adatto, consulta [questo link](https://github.com/linuxhw/EDID){target="blank"} oppure segui i passaggi indicati di seguito per personalizzare la configurazione EDID.

!!! Tip "Suggerimento"

    Trovare un EDID che corrisponda esattamente alla risoluzione e alla frequenza di aggiornamento desiderate può essere difficile. Puoi usare strumenti di modifica EDID come **RTDtool** o **EEditZ** per adattare un EDID esistente alle tue esigenze.

1. Trova un EDID adatto [qui](https://github.com/linuxhw/EDID){target="blank"} e copialo.

2. Accedi alla console del KVM GL.iNet e vai su **Settings** -> **EDID**. Passa alla modalità **Customize**, incolla i parametri nel campo di input e fai clic su **Set Custom** per applicare le impostazioni.

    ![edid customize](https://static.gl-inet.com/docs/kvm/tutorials/edid/edid_customize.png){class="glboxshadow"}

!!! Note "Nota"

    1. La risoluzione non deve superare 2560×1440@60Hz. Ad esempio, 2560×1600@60Hz non è supportata.
    2. La frequenza di aggiornamento massima supportata è 60Hz. Per risoluzioni superiori a 1920x1080, è consigliata una frequenza di 60FPS o inferiore.
    3. Evita di includere risoluzioni interlacciate, poiché causerebbero una visualizzazione anomala delle immagini.
    4. Il codice EDID inserito non deve superare due blocchi.
    5. È necessario il supporto audio di base. In caso contrario, la scheda audio potrebbe non essere selezionabile sul dispositivo controllato, impedendo la riproduzione del suono.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
