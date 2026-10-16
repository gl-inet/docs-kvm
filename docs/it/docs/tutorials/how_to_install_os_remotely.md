# Come installare un sistema operativo da remoto sul computer controllato tramite Virtual Media

Questo tutorial spiega come installare da remoto un sistema operativo sul computer controllato utilizzando Virtual Media, una funzionalità dei KVM GL.iNet.

1. Accedi al KVM GL.iNet e vai su **Virtual Media**.

2. Carica il file ISO del sistema operativo in Virtual Media.

    ![Caricamento del file](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/upload_file.png){class="glboxshadow"}

3. Al termine del caricamento, fai clic su **Mount To Remote** e seleziona **Image mounting** per montare l'immagine ISO.

    ![Montaggio dell'immagine](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-1.png){class="glboxshadow"}

    Seleziona il file immagine e fai clic su **Mount Image**.

    ![Montaggio dell'immagine](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-2.png){class="glboxshadow"}

4. Riavvia il computer controllato da remoto e **premi subito il tasto appropriato** durante l'avvio (ad esempio DEL in questo caso) per accedere al BIOS/UEFI.

    ![Accesso al BIOS](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/enter_bios.png){class="glboxshadow"}

5. Nel menu di avvio, imposta **"Glinet Flash Drive 1.00"** come Boot Option #1.

    ![Impostazione della priorità di avvio](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/set_boot_option_priority.png){class="glboxshadow"}

6. Salva le modifiche ed esci dal BIOS. Il sistema si avvierà dall'ISO montata per iniziare l'installazione del sistema operativo.

---

Hai ancora domande? Visita il nostro [forum della community](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
