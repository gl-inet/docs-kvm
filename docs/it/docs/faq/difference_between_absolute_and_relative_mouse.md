# Qual è la differenza tra mouse assoluto e mouse relativo {#what-is-the-difference-between-absolute-mouse-and-relative-mouse}

Nella console del KVM GL.iNet, **Mouse Mode** offre due opzioni: **Absolute** e **Relative**. Le due modalità differiscono per il comportamento del mouse, gli scenari di utilizzo e l'esperienza d'uso. Le sezioni seguenti ti aiutano a scegliere quella più adatta alle tue esigenze.

![mouse mode](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/mouse_mode.jpg){class="glboxshadow"}

## Mouse assoluto {#absolute-mouse}

La modalità Absolute consente di controllare il mouse in modo fluido e sincronizzato tra il computer locale e il dispositivo controllato. Quando è attiva, i puntatori del mouse dei due dispositivi vengono associati allo stesso sistema di coordinate. Puoi spostare il puntatore locale con continuità tra la console KVM e lo schermo remoto: il puntatore remoto seguirà il movimento di quello locale in tempo reale.

Durante l'uso può verificarsi un leggero ritardo, dovuto alla trasmissione di rete e alla codifica video. Questo ritardo rende il puntatore remoto leggermente più lento di quello locale, ma non compromette la fluidità complessiva delle operazioni.

![absolute](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/absolute.gif)

## Mouse relativo {#relative-mouse}

A differenza di Absolute, la modalità Relative non sincronizza le coordinate dei puntatori locale e remoto, che operano su livelli separati. Prima di controllare il dispositivo remoto, devi fare clic all'interno della finestra remota per acquisire il controllo del puntatore.

In questa modalità, il puntatore remoto rimane confinato nella finestra remota e non può passare direttamente al desktop locale. I bordi della finestra impediscono al puntatore di uscire dall'ambiente controllato. Per liberare il puntatore e tornare a controllare il computer locale, premi il tasto `Esc`.

![relative](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative.gif)

In modalità Relative puoi regolare **Relative Sensitivity**, con valori da 0.1 a 2.0.

![relative sensitivity](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative_sensitivity.jpg){class="glboxshadow"}

## Differenze principali {#key-differences}

| Caratteristica | Mouse assoluto | Mouse relativo |
| -------------------- | ------------------------------ | ----------------------------- |
| Coordinamento dei puntatori | I puntatori locale e remoto sono sincronizzati nello stesso sistema di coordinate | I puntatori locale e remoto operano su livelli separati, senza sincronizzazione delle coordinate |
| Controllo | Non occorre fare clic per acquisire il controllo; passaggio fluido tra gli schermi | Occorre fare clic sullo schermo remoto per acquisire il controllo; il passaggio tra gli schermi non è continuo |
| Ritardo | Leggero ritardo dovuto alla rete e alla codifica video | Ritardo quasi assente: vengono inviati solo gli incrementi di movimento |
| Scenari di utilizzo | Controllo fluido di più schermi, passaggi frequenti e posizionamento preciso, ad esempio per il lavoro da remoto e la grafica | Dispositivi meno recenti, BIOS o UEFI che non supportano il mouse assoluto; prevenzione dei clic accidentali; reti instabili con minore latenza |

## Riepilogo {#summary}

Il mouse assoluto privilegia un'esperienza di controllo fluida e integrata, mentre il mouse relativo punta sulla compatibilità e sulla stabilità.

Per la maggior parte delle attività quotidiane di controllo remoto con il KVM GL.iNet, la modalità Absolute è l'opzione predefinita consigliata. Puoi scegliere Relative in caso di problemi di compatibilità o esigenze operative particolari.

- Usa **Absolute Mouse** per un controllo remoto quotidiano fluido.
- Usa **Relative Mouse** per accedere al BIOS, utilizzare dispositivi meno recenti che non supportano il posizionamento assoluto o evitare clic accidentali.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
