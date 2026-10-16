# Errore di privacy durante l'accesso al KVM tramite browser {#privacy-error-when-accessing-kvm-via-browser}

Quando accedi al KVM GL.iNet tramite browser, potresti vedere l'avviso **Your connection isn't private**.

![privacy error](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_1.png){class="glboxshadow"}

Questo avviso indica che il browser non riesce a convalidare il certificato SSL/TLS presentato dal KVM. Ad esempio, il certificato potrebbe non essere stato emesso da un'autorità di certificazione attendibile per il browser, oppure potrebbe non corrispondere all'indirizzo IP o al nome host usato per accedere alla console.

## Perché viene visualizzato questo avviso? {#why-do-i-get-this-warning}

Nell'esempio precedente, **192.168.8.11** è l'indirizzo IP locale del KVM, assegnato dinamicamente dal router a monte tramite DHCP.

!!! Note "Nota"

    Se il gateway del router a cui è collegato il KVM GL.iNet è "192.168.x.1", dove x è generalmente 0, 1 o 8 nelle reti private, l'IP locale del KVM dovrebbe essere "192.168.x.y", dove y è un indirizzo host valido nella sottorete.

Questo indirizzo IP locale serve ad accedere alla console del KVM GL.iNet, anziché a un sito web pubblico.

Il KVM usa un certificato TLS predefinito per l'accesso tramite browser HTTPS. I browser convalidano i certificati delle console locali proprio come quelli dei siti web pubblici: il certificato deve essere attendibile, valido e corrispondere all'indirizzo a cui si accede.

Se il certificato predefinito non è attendibile per il browser o non include l'indirizzo IP locale o il nome host inserito, il browser mostra un avviso. Questo non significa che il KVM sia privo di certificato. HTTPS può comunque cifrare la connessione, ma il browser non può verificare l'identità del KVM.

## Come risolvere l'avviso? {#how-to-resolve-the-warning}

Per l'accesso locale, verifica prima che l'indirizzo appartenga al tuo KVM. Poi fai clic su **Advanced** e su **Continue to "192.168.8.11"**; il testo esatto varia in base al browser.

![Continue to 192.168.8.11](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/privacy_error_2.jpg){class="glboxshadow"}

Verrai quindi reindirizzato alla console del KVM GL.iNet.

![local access to kvm admin](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/local_access.png){class="glboxshadow"}

## Posso usare un certificato personale? {#can-i-use-my-own-certificate}

Sì. Puoi installare e usare un certificato SSL/TLS personale sul KVM. Segui i passaggi indicati di seguito.

1. Procurati un certificato SSL/TLS che includa il nome host o l'indirizzo IP usato per accedere al KVM. Per evitare gli avvisi del browser, il certificato deve essere valido ed emesso da un'autorità di certificazione attendibile per il browser. Un certificato autofirmato continuerà a generare un avviso, a meno che il dispositivo di controllo non sia configurato esplicitamente per considerarlo attendibile.

2. Accedi alla console del KVM. Fai clic sull'icona a forma di scudo nell'angolo in alto a destra per andare su **Security** -> **TLS Certificate**.

    ![custom cert 1](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert1.png){class="glboxshadow"}

    Nella finestra visualizzata, seleziona **Custom Certificate**, quindi carica il file del certificato e la chiave privata. Questa funzione è disponibile dal firmware v1.8.0.

    ![custom cert 2](https://static.gl-inet.com/docs/kvm/faq/privacy_error_from_your_browser/custom_cert2.png){class="glboxshadow"}

    In alternativa, puoi sostituire il certificato e la chiave privata sul KVM tramite un terminale SSH o WinSCP. Il certificato e la chiave si trovano nella seguente directory:

    `/etc/kvmd/user/ssl`

    Sostituiscili con il nuovo certificato SSL e la nuova chiave privata.

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
