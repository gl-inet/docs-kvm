# Que faire si l’écran distant est noir ou n’affiche aucun signal HDMI ? {#what-should-i-do-if-the-remote-screen-goes-blank-or-shows-no-hdmi-signal}

Si l’écran distant devient noir ou n’affiche aucun signal HDMI lors de l’accès via le KVM, suivez les étapes ci-dessous.

![Écran blanc](https://static.gl-inet.com/docs/kvm/faq/blank_screen/white_screen.png){class="glboxshadow"}
<small>(Écran blanc)</small>

![Écran noir](https://static.gl-inet.com/docs/kvm/faq/blank_screen/black_screen.png){class="glboxshadow"}
<small>(Écran noir)</small>

Vérifiez d’abord si le problème est lié à la transmission vidéo. Connectez-vous au KVM, accédez à **Settings** -> **Video** -> **Transfer** et choisissez **Direct** comme mode de transfert.

![Modification du mode de transmission](https://static.gl-inet.com/docs/kvm/faq/blank_screen/change_transfer.png){class="glboxshadow" width="360"}

Si le problème persiste, vérifiez les causes possibles ci-dessous une par une.

## Vérifier les connexions matérielles {#check-hardware-connection}

1. **Câble HDMI défectueux**

    Un câble vieillissant, des connecteurs oxydés ou des fils internes coupés peuvent interrompre le signal. Remplacez le câble par un modèle de bonne qualité.

    Vous pouvez aussi vérifier le signal HDMI dans la console : regardez si l’icône d’écran en bas à droite affiche « No HDMI signal ».

    ![No HDMI Signal](https://static.gl-inet.com/docs/kvm/faq/blank_screen/no_hdmi_signal.png){class="glboxshadow"}

2. **Branchement incorrect**

    Sur un PC de bureau, reliez le port **HDMI IN** du KVM à la sortie HDMI OUT de la carte graphique ou de la carte mère. Vérifiez que les fiches sont bien insérées. Si plusieurs sorties HDMI existent (carte dédiée et carte mère, par exemple), essayez un autre port.

    Sur un ordinateur portable, reliez le port **HDMI IN** du KVM à la sortie HDMI OUT du portable.

    Conseil : certains KVM, comme le Comet Pro et le Comet 5G, disposent de deux ports HDMI. Branchez le câble de l’appareil contrôlé sur HDMI IN. Sur HDMI OUT, aucun signal HDMI ne sera détecté dans la console.

3. **Utilisation incorrecte d’un adaptateur**

    Si un adaptateur HDMI est nécessaire, utilisez un adaptateur **VGA vers HDMI** pour relier l’appareil contrôlé au port HDMI IN du KVM GL.iNet.

    Un adaptateur HDMI vers VGA ne transmettra pas correctement la vidéo dans ce sens et produira un écran noir.

    ![Comparaison des adaptateurs](https://static.gl-inet.com/docs/kvm/faq/blank_screen/adapter_comparison.png){class="glboxshadow"}

## Vérifier les paramètres du navigateur {#check-browser-settings}

Si l’écran reste noir lors d’un accès par navigateur, essayez les méthodes suivantes :

1. **Essayez plusieurs navigateurs.** Testez Chrome, Firefox, Edge, etc. pour déterminer si le problème est propre à un navigateur.

2. **Désactivez les extensions de protection ou de contrôle des fuites WebRTC.** Désactivez toute extension susceptible d’affecter les connexions WebRTC et réessayez. Dans Settings -> Privacy & Security du navigateur, vérifiez également que les connexions WebRTC sont autorisées.

    ![WebRTC](https://static.gl-inet.com/docs/kvm/faq/blank_screen/webrtc.png){class="glboxshadow"}

## Vérifier l’état et les paramètres de l’appareil contrôlé {#check-controlled-device-status-and-settings}

1. **Appareil éteint ou en veille**

    Vérifiez que l’appareil est allumé et n’est pas en veille ou en veille prolongée en raison des paramètres d’alimentation. Réveillez-le avec ses boutons si nécessaire.

2. **Pilote graphique défaillant sur l’appareil contrôlé**

    Un pilote absent ou endommagé peut empêcher la sortie vidéo. Mettez-le à jour ou réinstallez-le en vous connectant localement à l’appareil contrôlé.

3. **Mauvais branchement entre carte graphique dédiée et intégrée**

    Si l’appareil possède les deux types de carte, branchez le câble HDMI sur le bon port graphique, par exemple celui de la carte dédiée si elle est installée.

4. **Paramètres d’affichage anormaux sur l’appareil contrôlé (peu probable)**

    Lors de la connexion, le KVM GL.iNet adapte automatiquement la sortie vidéo en lisant l’EDID de l’écran. Dans la plupart des cas, la configuration EDID par défaut convient et ne nécessite aucune modification.

    Si l’appareil est compatible avec les écrans standard, des problèmes d’affichage via GLKVM sont peu probables. Certaines incompatibilités spécifiques, par exemple Linux avec un écran ASUS, peuvent toutefois produire un écran noir.

    Vérifiez si l’appareil contrôlé est compatible avec les écrans standard et s’il présente une incompatibilité avec un écran particulier.

5. **Problème de résolution**

    Avec certains systèmes, comme Proxmox VE Hypervisor, GLKVM peut mal négocier la résolution disponible, ce qui entraîne des problèmes d’affichage. Ajustez alors manuellement la résolution sur l’appareil contrôlé.

    Voici comment modifier la résolution de Proxmox VE Hypervisor.

    1. Ouvrez le terminal PVE et saisissez la commande ci-dessous pour modifier `/etc/default/grub`.

        ```
        nano /etc/default/grub
        ```

    2. Ajoutez la ligne suivante.

        ```
        GRUB_CMDLINE_LINUX_DEFAULT="quiet gfxpayload=text nomodeset"
        ```

    3. Décommentez la ligne `GRUB_GFXMODE` en retirant `#` et définissez la résolution souhaitée, par exemple `1024x768`.

        ```
        GRUB_GFXMODE=1024x768
        ```

    4. Appuyez sur `Ctrl + O`, puis sur Entrée pour enregistrer.

    5. Appuyez sur `Ctrl + X` pour quitter nano.

    6. Saisissez la commande ci-dessous pour appliquer la configuration.

        ```
        update-grub
        ```

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
