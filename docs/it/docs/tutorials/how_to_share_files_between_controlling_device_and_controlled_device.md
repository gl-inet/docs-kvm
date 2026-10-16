# Come condividere file tra il dispositivo di controllo e il dispositivo controllato {#how-to-share-files-between-controlling-and-controlled-devices}

Il KVM GL.iNet emula un'unità USB con accesso in lettura e scrittura, consentendo di condividere e gestire file tra il dispositivo di controllo e il dispositivo controllato.

Nei passaggi seguenti useremo Comet (GL-RM1) come esempio.

## Inviare file al dispositivo controllato {#send-files-to-controlled-device}

Per condividere file dal dispositivo di controllo al dispositivo controllato, segui i passaggi indicati di seguito.

1. Nella console, vai su **Virtual Media**. Trascina i file nel riquadro oppure fai clic su di esso per caricarli dal dispositivo di controllo; in alternativa, caricali da un URL.

    Una volta caricati, i file verranno visualizzati come mostrato di seguito.

    ![upload files](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing1.png){class="glboxshadow"}

2. Fai clic su **Mount To Remote** -> **File Sharing**.

    ![file sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing2.png){class="glboxshadow"}

3. Nella console comparirà una finestra con le istruzioni per la condivisione dei file, come mostrato di seguito.

    ![file sharing tips](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing3.png){class="glboxshadow"}

4. Attendi un momento: sullo schermo comparirà automaticamente un'unità chiamata **"GLKVM"**. Comet sta ora emulando un'unità USB con accesso in lettura e scrittura sul dispositivo controllato, dove saranno visibili i file caricati in precedenza.

    Ora puoi visualizzare, spostare o eliminare i file di questa unità dal dispositivo controllato.

    ![file shared](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing4.png){class="glboxshadow"}

    **Suggerimento**: se l'unità non compare automaticamente, apri **This PC** sul dispositivo controllato.

    ![this pc](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/thispc.png){class="glboxshadow"}

    Trova l'unità chiamata **"GLKVM"**. Ora puoi visualizzare, spostare o eliminare i file che contiene.

5. Per interrompere la condivisione, fai clic su **Virtual Media** nella barra degli strumenti, quindi su **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing1.png){class="glboxshadow"}

## Ricevere file dal dispositivo controllato {#get-files-from-controlled-device}

Per ricevere file dal dispositivo controllato, segui i passaggi indicati di seguito.

1. Sul dispositivo controllato, sposta o copia nell'unità **GLKVM** i file che vuoi condividere.

    Nell'esempio seguente, un file è stato spostato dal desktop del dispositivo controllato all'unità **GLKVM**.

    ![copy file to disk](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing5.png){class="glboxshadow"}

2. Torna alla console di Comet, fai clic su **Virtual Media** nella barra degli strumenti, quindi su **Stop Sharing**.

    ![stop sharing](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing2.png){class="glboxshadow"}

3. Il file verrà visualizzato in **Virtual Media**, come mostrato di seguito. Ora puoi scaricarlo da Comet sul dispositivo di controllo.

    ![file shared](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing6.png){class="glboxshadow"}

---

Hai altre domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
