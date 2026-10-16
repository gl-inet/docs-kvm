# Partager des fichiers entre les appareils de contrôle et contrôlé {#how-to-share-files-between-controlling-and-controlled-devices}

Le KVM GL.iNet émule une clé USB accessible en lecture et en écriture, ce qui permet de partager et de gérer des fichiers entre l’appareil de contrôle et l’appareil contrôlé.

Les étapes suivantes prennent le Comet (GL-RM1) comme exemple.

## Envoyer des fichiers à l’appareil contrôlé {#send-files-to-controlled-device}

Pour partager des fichiers de l’appareil de contrôle vers l’appareil contrôlé, suivez les étapes ci-dessous.

1. Dans la console, accédez à **Virtual Media**. Déposez les fichiers de votre appareil de contrôle dans la zone prévue, cliquez sur celle-ci pour les sélectionner ou importez-les depuis une URL.

    Une fois importés, les fichiers s’affichent comme ci-dessous.

    ![Téléversement de fichiers](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing1.png){class="glboxshadow"}

2. Cliquez sur **Mount To Remote** -> **File Sharing**.

    ![Partage de fichiers](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing2.png){class="glboxshadow"}

3. Une fenêtre s’ouvre dans la console pour indiquer les étapes du partage, comme illustré ci-dessous.

    ![Étapes du partage de fichiers](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing3.png){class="glboxshadow"}

4. Patientez un instant : un lecteur nommé **« GLKVM »** apparaît automatiquement à l’écran. Le Comet émule désormais une clé USB accessible en lecture et en écriture sur l’appareil contrôlé. Les fichiers importés précédemment y sont disponibles.

    Vous pouvez consulter, déplacer ou supprimer les fichiers de ce lecteur sur l’appareil contrôlé.

    ![Fichier partagé](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing4.png){class="glboxshadow"}

    **Conseil :** Si le lecteur n’apparaît pas automatiquement, ouvrez **This PC** sur l’appareil contrôlé.

    ![This PC](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/thispc.png){class="glboxshadow"}

    Trouvez le lecteur nommé **« GLKVM »**. Vous pouvez y consulter, déplacer ou supprimer les fichiers.

5. Pour arrêter le partage, cliquez sur **Virtual Media** dans la barre d’outils, puis sur **Stop Sharing**.

    ![Arrêt du partage](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing1.png){class="glboxshadow"}

## Récupérer des fichiers de l’appareil contrôlé {#get-files-from-controlled-device}

Pour recevoir des fichiers de l’appareil contrôlé, suivez les étapes ci-dessous.

1. Sur l’appareil contrôlé, déplacez ou copiez les fichiers à partager dans le lecteur **GLKVM**.

    Dans l’exemple ci-dessous, un fichier a été déplacé du Bureau de l’appareil contrôlé vers le lecteur **GLKVM**.

    ![Copie d’un fichier vers le lecteur](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing5.png){class="glboxshadow"}

2. Revenez à la console du Comet, cliquez sur **Virtual Media** dans la barre d’outils, puis sur **Stop Sharing**.

    ![Arrêt du partage](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/stop-sharing2.png){class="glboxshadow"}

3. Le fichier apparaît alors dans **Virtual Media**, comme ci-dessous. Vous pouvez le télécharger depuis le Comet vers votre appareil de contrôle.

    ![Fichier partagé](https://static.gl-inet.com/docs/kvm/tutorials/share_files_via_virtual_media/file-sharing6.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
