# Installer un système d’exploitation à distance sur l’ordinateur contrôlé avec Virtual Media {#how-to-install-an-os-on-the-controlled-computer-remotely-using-virtual-media}

Ce tutoriel explique comment installer un système d’exploitation à distance sur l’ordinateur contrôlé grâce à la fonction Virtual Media des KVM GL.iNet.

1. Connectez-vous à votre KVM GL.iNet et accédez à **Virtual Media**.

2. Importez le fichier ISO du système d’exploitation dans Virtual Media.

    ![Téléversement d’un fichier](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/upload_file.png){class="glboxshadow"}

3. Une fois l’importation terminée, cliquez sur **Mount To Remote**, puis sélectionnez **Image mounting** pour monter l’image ISO.

    ![Montage d’image](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-1.png){class="glboxshadow"}

    Sélectionnez le fichier image et cliquez sur **Mount Image**.

    ![Montage d’image](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/image-mounting-2.png){class="glboxshadow"}

4. Redémarrez l’ordinateur contrôlé à distance et **appuyez immédiatement sur la touche appropriée** pendant le démarrage (par exemple DEL dans cet exemple) pour accéder au BIOS/UEFI.

    ![Accès au BIOS](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/enter_bios.png){class="glboxshadow"}

5. Dans le menu de démarrage, définissez **« Glinet Flash Drive 1.00 »** comme **Boot Option #1**.

    ![Définition de la priorité des options de démarrage](https://static.gl-inet.com/docs/kvm/tutorials/install_os_remotely/set_boot_option_priority.png){class="glboxshadow"}

6. Enregistrez les réglages et quittez le BIOS. Le système démarre depuis l’ISO monté pour lancer l’installation du système d’exploitation.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
