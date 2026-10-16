# Come cambiare il nome host del KVM {#how-to-change-kvm-hostname}

Il nome host predefinito del KVM GL.iNet è **glkvm**. Quando sei collegato alla stessa rete, puoi quindi accedervi localmente tramite il dominio `glkvm.local`.

Questo tutorial presenta due metodi per cambiare il nome host: dalla console del KVM o tramite comandi nel terminale.

## Metodo 1. Console del KVM {#method-1-kvm-console}

> **Nota**: questa funzione è disponibile a partire dal firmware 1.7.0.

### Firmware v1.10 e versioni successive {#firmware-v110-and-above}

1. Accedi al KVM e fai clic sull'icona Settings nella barra di navigazione per aprire la pagina delle impostazioni.

    ![settings network](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings-network.png){class="glboxshadow"}

2. Vai su **Network** e inserisci il nome host personalizzato; la modifica verrà applicata.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify-hostname.png){class="glboxshadow"}

### Firmware v1.9 e versioni precedenti {#firmware-v19-and-earlier}

1. Accedi al KVM e vai su **Settings** -> **Network**. Fai clic sul nome host o sull'icona della freccia verso destra.

    ![settings network](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/settings_network.png){class="glboxshadow"}

2. Personalizza il nome host e fai clic su **Apply**.

    ![modify hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/modify_hostname.png){class="glboxshadow"}

## Metodo 2. Comandi nel terminale {#method-2-terminal-commands}

1. Accedi al KVM e vai su **Toolbox** -> **Terminal**. Fai clic su **Access**.

    ![access terminal](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_terminal.png){class="glboxshadow"}

2. Nel terminale, inserisci il comando seguente e premi Invio, sostituendo "example" con il nome host desiderato. Il KVM si riavvierà.

    `echo example > /etc/hostname && reboot`

    ![input command](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/input_command.png){class="glboxshadow"}

3. Attendi il riavvio. Potrai quindi accedere al KVM usando il nuovo nome host.

    ![access new hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/access_new_hostname.png){class="glboxshadow"}

    Se dimentichi il nome host o vuoi verificare che la modifica sia stata applicata, esegui il comando seguente nel terminale per visualizzare il nome host corrente.

    `cat /etc/hostname`

    ![verify hostname](https://static.gl-inet.com/docs/kvm/tutorials/change_hostname/verify_hostname.png){class="glboxshadow"}

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
