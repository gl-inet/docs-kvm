# Guida utente della scheda ATX (GL-ATXPC)

La scheda ATX è un accessorio opzionale per i dispositivi KVM GL.iNet. Questo modulo intelligente di gestione dell'alimentazione consente di controllare da remoto l'alimentazione del dispositivo controllato simulando la pressione del pulsante fisico di accensione (accensione/spegnimento/riavvio).

La scheda ATX si installa all'interno del case del dispositivo controllato, offrendo una gestione dell'alimentazione più discreta e stabile.

**Nota**: Comet Q (GL-RMQ1) non è compatibile con la scheda ATX.

![rm1-and-atx-borad](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/rm1-and-atx-borad.jpg){class="glboxshadow"}

## Contenuto della confezione { #package-contents }

![inside the box](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/inside-the-box.png){class="glboxshadow gl-80-desktop"}

- 1 x Scheda principale ATX
- 1 x Set di cavi a 9 pin
- 1 x Confezione di viti
- 1 x Cavo da USB-A a Type-C
- 1 x Kit staffa ATX

## Disposizione dei pin { #pin-out }

![pinout](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/pinout.jpg){class="glboxshadow gl-80-desktop"}

Descrizione delle interfacce:

1. Interfaccia Type-C: collegamento al dispositivo KVM.
2. Pulsante di aggiornamento firmware: per il microcontrollore sulla scheda principale ATX.
3. Pulsante di ripristino.
4. Collegamento al cablaggio del pannello di controllo del computer.
5. Collegamento all'interfaccia F_PANEL del computer.

!!! note "Nota"

    1. Le interfacce 4 e 5 sono intercambiabili: l'interfaccia 5 può essere collegata al cablaggio del pannello del computer e l'interfaccia 4 a F_PANEL.

    2. Sulla scheda ATX sono presenti due LED, entrambi con un comportamento analogo al LED di alimentazione (il blu indica il sistema ATX, il verde l'alimentazione del PC). La scheda ATX non dispone di un LED HDD. Lo stato dei LED sulla scheda corrisponde a quello del LED di alimentazione sul pannello del computer.

Schema delle interfacce 4/5:

![interface](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface.png){class="glboxshadow gl-60-desktop"}

## Installazione { #installation }

Guardare questo video per installare la scheda ATX oppure seguire i passaggi riportati di seguito.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3VEjZgzgI44" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Fissare la scheda ATX alla staffa { #1-screw-atx-board-and-bracket }

Fissare la scheda ATX alla staffa con le viti in dotazione.

![screwing](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/screwing.jpg){class="glboxshadow gl-90-desktop"}

### 2. Installare la scheda ATX nel case del PC { #2-install-atx-board-into-pc-case }

Collegare le interfacce 4 e 5 rispettivamente al cablaggio del pannello di controllo del PC controllato e all'interfaccia F_PANEL.

![interface connect](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface_connect.jpg){class="glboxshadow gl-90-desktop"}

Il set di cavi a 9 pin in dotazione consente di collegare una delle interfacce 4/5 della scheda ATX al cablaggio del pannello di controllo o all'interfaccia F_PANEL del computer controllato.

Per collegare l'altra interfaccia 4/5 della scheda ATX al cablaggio del pannello di controllo o all'interfaccia F_PANEL, usare i cavi inclusi nel case del computer.

**Nota**: La polarità delle interfacce può variare a seconda del case del PC. Verificarla con attenzione prima dell'installazione.

Di seguito sono riportati alcuni esempi di collegamento dell'interfaccia 4/5 all'interfaccia F_PANEL del computer controllato.

??? "Per PANEL a 10-1 pin"

    Se il connettore sulla scheda madre del computer controllato destinato al pannello di controllo è un PANEL a 10-1 pin, come mostrato di seguito:

    ![10-1pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_1.png){class="glboxshadow"}

    Per il collegamento, fare riferimento allo schema seguente. Assicurarsi che le scritte serigrafate (HDDLED±, RESET SW, POWER SW, POWERLED+, ecc.) siano rivolte verso l'esterno e visibili, anziché verso l'interno e nascoste.

    ![10-1pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_2.jpg){class="glboxshadow"}
    <small>Front View</small>

    ![10-1pin panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_3.jpg){class="glboxshadow"}
    <small>Rear View</small>

    Usare quindi i cavi inclusi nel case per collegare l'altra interfaccia della scheda ATX al cablaggio del pannello di controllo del computer.

??? "Per PANEL a 20-5 pin"

    Se il connettore sulla scheda madre del computer controllato destinato al pannello di controllo è un PANEL a 20-5 pin, come mostrato di seguito:

    ![20-5pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_1.jpg){class="glboxshadow"}

    Per il collegamento, fare riferimento allo schema seguente. Assicurarsi che le scritte serigrafate (HDDLED±, RESET SW, POWER SW, POWERLED+, ecc.) siano rivolte verso l'esterno e visibili, anziché verso l'interno e nascoste.

    ![20-5pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_2.jpg){class="glboxshadow"}
    <small>Front View</small>

    ![20-5pin panel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_3.png){class="glboxshadow"}
    <small>Rear View</small>

    Usare quindi i cavi inclusi nel case per collegare l'altra interfaccia della scheda ATX al cablaggio del pannello di controllo del computer.

??? "Per PANEL a 20-8 pin"

    Se il connettore sulla scheda madre del computer controllato destinato al pannello di controllo è un PANEL a 20-8 pin, come mostrato di seguito:

    ![20-8pin panel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_1.jpg){class="glboxshadow"}

    Per il collegamento, fare riferimento allo schema seguente. Assicurarsi che le scritte serigrafate (HDDLED±, RESET SW, POWER SW, POWERLED+, ecc.) siano rivolte verso l'esterno e visibili, anziché verso l'interno e nascoste.

    ![20-8pin panel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_2.png){class="glboxshadow"}

    Usare quindi i cavi inclusi nel case per collegare l'altra interfaccia della scheda ATX al cablaggio del pannello di controllo del computer.

La scheda ATX con tutti i collegamenti completati è mostrata di seguito.

![atx board connected](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected1.png){class="glboxshadow gl-90-desktop"}

![atx board connected](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected2.png){class="glboxshadow gl-90-desktop"}

Installare quindi la staffa della scheda ATX nel case del computer.

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install1.png){class="glboxshadow gl-90-desktop"}

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install2.png){class="glboxshadow gl-90-desktop"}

### 3. Collegare la scheda ATX al KVM { #3-connect-atx-board-and-kvm }

Collegare la porta Type-C della scheda ATX alla porta USB-A del dispositivo KVM, ad esempio Comet GL-RM1, con il cavo USB in dotazione.

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install3.png){class="glboxshadow gl-90-desktop"}

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install4.png){class="glboxshadow gl-90-desktop"}

L'installazione della scheda ATX è completata.

![atx board install](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install5.png){class="glboxshadow gl-90-desktop"}

Ora è possibile accedere al KVM e aprire **Accessories** per controllare l'alimentazione ATX.

![atx power](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/atx_power.png){class="glboxshadow gl-90-desktop"}

## Domande frequenti { #faq }

**D1. Posso usare la scheda GL-ATXPC con dispositivi KVM di altri produttori?**

R1. No. La scheda GL-ATXPC è un accessorio per i dispositivi KVM GL.iNet e deve essere usata insieme a un KVM GL.iNet.

---

**D2. Dopo aver installato la scheda ATX, cosa devo fare se non riesco ad accendere o spegnere il dispositivo remoto tramite il KVM?**

R2. Provare le seguenti soluzioni.

- Verificare che il dispositivo controllato si accenda e si spenga normalmente premendo il pulsante fisico di accensione sul pannello anteriore del case.

- Verificare la polarità dei collegamenti. Provare a invertire la polarità del connettore POWER SW sulla scheda madre del dispositivo controllato per escludere un collegamento errato.

    ![connector polarity](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/power-sw-connector.png){class="glboxshadow gl-90-desktop"}

- Quando si effettua il collegamento a F_PANEL sulla scheda madre del dispositivo controllato, verificare che le scritte serigrafate (HDDLED±, RESET SW, POWER SW, POWERLED+, ecc.) siano rivolte verso l'esterno e visibili, anziché verso l'interno e nascoste.

- Aggiornare il firmware del KVM.

---

**D3. Posso usare un solo KVM GL.iNet per controllare più schede ATX?**

R3. I seguenti KVM GL.iNet possono controllare una sola scheda ATX.

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)

Comet X (GL-RM4PE) supporta invece fino a quattro schede ATX contemporaneamente. Sul pannello posteriore sono presenti quattro canali indipendenti; ciascuno dispone di una porta HDMI per il segnale video, una porta Type-C per i segnali di tastiera e mouse e una porta USB 2.0 per le periferiche USB, ad esempio Fingerbot o scheda ATX.

**Nota**: Comet Q (GL-RMQ1) non è compatibile con la scheda ATX.

---

Per altre domande, visitare il [forum della community](https://forum.gl-inet.com){target="_blank"} o [contattarci](https://www.gl-inet.com/contacts/){target="_blank"}.
