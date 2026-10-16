# Guide de la console de Comet Pro (GL-RM10) {#comet-pro-gl-rm10-console-guide}

## Session {#session}

Dans la console, accédez à **Session**. Cette page de paramètres comprend quatre sections :

- [Vidéo](#video)
- [Audio et caméra](#audio-camera)
- [Clavier](#keyboard)
- [Souris](#mouse)

### Vidéo {#video}

Dans **Session**, vous pouvez personnaliser les paramètres vidéo : mode d’affichage, qualité vidéo, transmission vidéo, orientation de l’écran et EDID.

![Paramètres vidéo](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session-video.png){class="glboxshadow"}

- **Transfer** : sélectionnez la méthode de transmission vidéo : WebRTC, WebRTC (FEC), WebRTC (Native) ou Direct. La transmission Direct ne prend pas en charge le son.

    !!! note "Quelle est la différence entre WebRTC, WebRTC (FEC), WebRTC (Native) et Direct ?"

        - **WebRTC** : associe une vidéo fluide et un son stable pour le contrôle à distance en temps réel.

        - **WebRTC (FEC)** : ajoute une correction d’erreurs anticipée pour améliorer la stabilité de la connexion lorsque le réseau est de mauvaise qualité ou instable. Ce mode corrige automatiquement les pertes de paquets en transmettant une petite quantité de données redondantes, ce qui réduit les scintillements et les ralentissements.

        - **WebRTC (Native)** : utilise la bibliothèque Google WebRTC pour améliorer les performances de diffusion et la fluidité du contrôle à distance en temps réel. Ce mode de transmission a été introduit dans le micrologiciel v1.10.0.

        - **Direct** : offre la latence la plus faible et une qualité vidéo sans perte, mais ne prend pas en charge la transmission audio.

- **Mode** : choisissez le mode Smart ou Normal selon vos besoins. Le mode Smart réduit la consommation de bande passante, notamment lorsque le réseau est de mauvaise qualité.

- **Latency Mode** : choisissez entre Lowest Latency et Smooth Display pour l’appareil. Cette fonction a été introduite dans le micrologiciel v1.9.0.

    !!! note "Quelle est la différence entre Lowest Latency et Smooth Display ?"

        - **Lowest Latency** : réduit au minimum la latence des entrées pour améliorer la réactivité du clavier et de la souris.

        - **Smooth Display** : optimise l’affichage pour éliminer les saccades et les pertes d’images et assurer une lecture fluide.

- **Quality** : réglez la qualité vidéo sur Auto/Low/Medium/High/Ultra-high/Lossless selon votre réseau et vos besoins en matière de résolution.

- **FEC Packets** : lorsque le réseau est instable, cette fonction corrige automatiquement les pertes de paquets en envoyant une petite quantité de données redondantes, ce qui réduit les scintillements et les ralentissements. Vous pouvez régler le taux de FEC sur 5%/10%/15%/20%.

- **Orientation** : réglez l’angle de rotation de la console sur 0°/90°/180°/270°.

- **EDID** : abréviation de Extended Display Identification Data, cette fonction sélectionne automatiquement les paramètres d’affichage optimaux.

    Le réglage par défaut convient à la plupart des situations et ne nécessite généralement aucune modification. Consultez [ce guide](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} pour plus de détails. Si l’écran ne s’actualise pas après une modification de l’EDID, redémarrez l’appareil contrôlé.

- **View** : ce paramètre détermine la mise à l’échelle de l’écran lorsque vous redimensionnez la fenêtre du navigateur. Options disponibles : Adaptive, Best Picture Quality et Original Pixel. Cette fonction a été introduite dans le micrologiciel v1.8.0.

- **Screen Privacy** : lorsque cette fonction de confidentialité est activée, l’écran externe connecté à HDMI-OUT n’affiche plus de contenu, afin de préserver la confidentialité des opérations à distance.

### Audio et caméra {#audio-camera}

Vous pouvez régler les paramètres audio et de caméra de l’appareil contrôlé.

![Audio et caméra](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_audio_camera.png){class="glboxshadow"}

- **Speaker** : contrôlez la sortie audio de l’appareil contrôlé, par exemple les sons système ou le son des vidéos.

- **Microphone** : transmettez le son local, par exemple votre voix, de l’appareil de contrôle vers l’appareil distant. Vous pouvez couper le son en un clic et activer le microphone en maintenant un raccourci enfoncé (Press To Speak).

    **Remarque** : vous devez configurer manuellement le raccourci dans les [paramètres](#usb-devices) avant de l’utiliser.

- **Camera** : lorsque la caméra est activée sur l’appareil de contrôle, les images vidéo locales sont transmises directement à l’hôte distant, sur lequel une caméra USB virtuelle est émulée. Les applications de l’hôte distant, comme les outils de visioconférence et FaceTime, peuvent utiliser ce flux vidéo comme si une caméra physique y était directement connectée.

    **Remarque** : cette fonction a été introduite dans le micrologiciel v1.10.0 et fonctionne uniquement en mode WebRTC (FEC). Elle est actuellement accessible uniquement depuis un navigateur web ; elle n’est pas encore prise en charge dans l’application ni dans le client de bureau.

### Clavier {#keyboard}

La section **Keyboard** permet de configurer l’utilisation du clavier sur l’appareil contrôlé.

![Paramètres du clavier](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_keyboard.png){class="glboxshadow"}

- **Bad Link Mode** : relâche immédiatement les touches. Chaque frappe est envoyée sous la forme d’un bref appui suivi d’un relâchement, ce qui évite les touches bloquées ou les saisies répétées involontaires lors du contrôle à distance.

- **Show Virtual Keyboard** : affichez et utilisez le clavier virtuel dans la console.

    ![Affichage du clavier virtuel](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_show_virtual_keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS** : permute les touches Cmd et Ctrl pour assurer la compatibilité du clavier entre les différents systèmes d’exploitation.

### Souris {#mouse}

Vous pouvez régler les paramètres de la souris pour améliorer son utilisation sur l’appareil contrôlé.

![Paramètres de la souris](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/session_mouse.png){class="glboxshadow"}

- **Show Local Cursor** : affichez le curseur de l’appareil actuel à l’écran.

- **Mouse Jiggle** : simule de petits mouvements périodiques de la souris pour empêcher l’appareil contrôlé de se mettre en veille lors d’une inactivité prolongée, par exemple pendant des réunions à distance ou la gestion de serveurs.

- **Scroll Rate** : règle la vitesse de défilement de la molette, ou le nombre de lignes ou d’unités parcourues par rotation, et donc la vitesse à laquelle le contenu défile sur l’appareil distant.

- **Scroll Direction** : détermine si le défilement de la molette vers le haut ou le bas fait défiler le contenu distant dans le même sens (défilement naturel) ou dans le sens opposé (défilement traditionnel).

    Quatre modes sont disponibles : Standard, Vertical Invert, Horizontal Invert et Both Invert.

- **Mouse Mode** : permet de choisir le mode de souris absolue (Absolute Mode) ou relative (Relative Mode) pour un contrôle fluide et précis du curseur dans différentes situations.

    !!! note "Quelle est la différence entre le mode de souris absolue et relative ?"

        - **Relative Mode** : la position de la souris est calculée à partir de ses déplacements, plutôt que de coordonnées fixes à l’écran. Vous devez cliquer dans la fenêtre distante pour contrôler la souris. Le curseur reste capturé dans l’écran distant et ne peut pas en sortir librement. Ce mode offre une meilleure compatibilité avec le BIOS, les systèmes anciens et les appareils embarqués.

        - **Absolute Mode** : la position de la souris correspond à des coordonnées précises à l’écran. Le curseur distant suit le curseur local de manière fluide et précise, ce qui permet de passer librement de l’écran local à l’écran distant. Ce mode convient au contrôle quotidien du bureau et aux opérations précises, bien qu’un léger délai puisse survenir en raison de la transmission réseau.

        Utilisez le mode Absolute pour un contrôle quotidien fluide. Choisissez Relative pour accéder au BIOS, utiliser certains appareils anciens qui ne prennent pas en charge le positionnement absolu ou éviter les déplacements accidentels du curseur.

- **Relative Sensitivity** : ce réglage est disponible lorsque **Mouse Mode** est défini sur Relative.

- **Primary Button** : choisissez le bouton gauche ou droit comme bouton principal. Cette fonction a été introduite dans le micrologiciel v1.9.0.

## Boîte à outils {#toolbox}

Dans la console, accédez à **Toolbox**. Cette page comprend cinq sections :

- [Presse-papiers](#clipboard)
- [OCR](#ocr)
- [Raccourcis](#shortcut)
- [Wake-on-LAN](#wake-on-lan)
- [Terminal](#terminal)

### Presse-papiers {#clipboard}

Le presse-papiers permet de coller facilement du texte de l’appareil de contrôle sur l’appareil contrôlé, sans transférer de fichiers.

![Presse-papiers](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_clipboard.png){class="glboxshadow"}

### OCR {#ocr}

L’OCR est une fonction de reconnaissance de texte. Elle permet de sélectionner une zone de l’écran distant et d’en extraire facilement le texte. Cette fonction a été introduite dans le micrologiciel v1.9.0.

Pour l’utiliser, cliquez sur la flèche vers le bas et sélectionnez la langue de reconnaissance souhaitée, par exemple le chinois, l’anglais ou le mode bilingue (Zh/En).

![Langue de reconnaissance](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_ocr.png){class="glboxshadow"}

Cliquez ensuite sur **Capture**. L’écran distant s’assombrit. Tracez un cadre autour du texte à extraire : le système le reconnaît automatiquement. Vous pouvez alors copier le texte reconnu selon vos besoins.

![Copie du texte](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/ocr_copy_text.png){class="glboxshadow"}

Cette fonction permet de récupérer facilement du texte de l’écran distant, c’est-à-dire de l’appareil contrôlé, et de le copier sur l’appareil de contrôle local.

### Raccourcis {#shortcut}

Les raccourcis permettent d’effectuer des actions plus rapidement sans utiliser le clavier virtuel et de gagner du temps dans vos tâches quotidiennes. Cette section regroupe des raccourcis courants.

![Raccourcis 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_shorcut.png){class="glboxshadow"}

Cliquez sur **Modify** pour adapter les raccourcis à vos besoins.

![Raccourcis 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_shorcut_modify.png){class="glboxshadow"}\

### Wake-on-LAN {#wake-on-lan}

Wake-on-LAN (WOL) est une technologie qui permet d’allumer l’appareil contrôlé à distance ou de le sortir d’un état de faible consommation.

Cliquez sur **Add Device** et choisissez un appareil du même réseau local.

![Wake-on-LAN](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_wake_on_lan.png){class="glboxshadow"}

![Ajout d’un appareil Wake-on-LAN](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/wol-add-device.png){class="glboxshadow"}

Si l’appareil à ajouter ne figure pas dans la liste, cliquez sur **Add Manually**, puis saisissez son nom et son adresse MAC.

![Ajout manuel Wake-on-LAN](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/wol-add-manually.png){class="glboxshadow"}

### Terminal {#terminal}

Vous pouvez accéder au terminal de Comet Pro pour effectuer des réglages avancés. Cliquez sur **Access**.

![Terminal 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox_terminal.png){class="glboxshadow"}

Le terminal GLKVM s’ouvre.

![Terminal 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/toolbox-terminal-2.png){class="glboxshadow"}

## Accessoires {#accessories}

GL.iNet propose des accessoires KVM en option pour allumer et éteindre l’appareil à distance.

Consultez d’abord le guide d’utilisation correspondant pour connecter l’accessoire à votre appareil contrôlé.

- [Guide d’utilisation du Fingerbot (FGB-01)](../gl-fgb-01/index.md){target="_blank"}

- [Guide d’utilisation de la carte ATX (GL-ATXPC)](../gl-atx-board/index.md){target="_blank"}

Connectez-vous ensuite à la console KVM et accédez à **Accessories**. Les paramètres de l’accessoire ne sont disponibles qu’une fois celui-ci installé.

### Fingerbot {#fingerbot}

Le Fingerbot se fixe sur le bouton d’alimentation physique de l’appareil contrôlé pour commander son alimentation à distance.

Son fonctionnement dépend des paramètres définis dans la console.

![Accessoire Fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/accessories-fgb.png){class="glboxshadow"}

- **Time** : durée d’appui du Fingerbot. Vous pouvez la régler sur 0.5s/3s/8s.

- **Strength** : deux niveaux de force d’appui sont disponibles : Lightly Press et Firmly Press.

    - **Lightly Press** : convient aux boutons à course courte ou souples.

    - **Firmly Press** : convient aux boutons à course longue ou résistants.

    ![Force d’appui](https://static.gl-inet.com/docs/kvm/user_guide/gl-fgb-01/press_mode.png){class="glboxshadow gl-70-desktop"}

### Alimentation ATX {#atx-power}

La carte ATX s’installe dans le boîtier de l’ordinateur pour commander à distance son allumage, son extinction et son redémarrage.

Son fonctionnement dépend des paramètres définis dans la console.

![Accessoire d’alimentation ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/accessories-atx.png){class="glboxshadow"}

- **Power (Short Press)** : sert à allumer normalement l’appareil ou à sortir le système de veille.

- **Power (Long Press)** : force l’arrêt de l’appareil.

- **Restart** : redémarre l’appareil.

## Supports virtuels {#virtual-media}

Dans la console, accédez à **Virtual Media**. Vous pouvez y effectuer les opérations suivantes :

- [Partage de fichiers](#file-sharing)
- [Montage d’images](#image-mounting)
- [Remplacement du support de stockage](#replace-storage-drive)
- [Formatage du disque](#format-disk)

![Supports virtuels](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/virtual-media.png){class="glboxshadow"}

### Partage de fichiers {#file-sharing}

Comet Pro émule un support USB accessible en lecture et en écriture afin de partager et gérer des fichiers entre l’appareil de contrôle et l’appareil contrôlé.

**Pour partager des fichiers de l’appareil de contrôle vers l’appareil contrôlé, suivez les étapes ci-dessous.**

1. Faites glisser des fichiers dans la zone prévue ou cliquez dessus pour les téléverser depuis votre appareil de contrôle. Vous pouvez également les importer depuis une URL.

    Une fois téléversés, les fichiers s’affichent comme ci-dessous.

    ![Téléversement de fichiers](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-uploaded.png){class="glboxshadow"}

2. Cliquez sur **Mount To Remote** -> **File Sharing**.

    ![Partage de fichiers](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount1.png){class="glboxshadow"}

3. Une fenêtre présente les étapes du partage de fichiers dans la console, comme illustré ci-dessous.

    ![Instructions de partage de fichiers](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount2-prompt.png){class="glboxshadow"}

4. Patientez un instant : un lecteur nommé **« GLKVM »** apparaît automatiquement à l’écran. Les fichiers que vous avez téléversés de l’appareil de contrôle vers Comet Pro sont alors partagés avec l’appareil contrôlé. Vous pouvez les consulter, les déplacer ou les supprimer depuis ce lecteur sur l’appareil contrôlé.

    ![Lecteur GLKVM pour le partage de fichiers](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mount3.png){class="glboxshadow"}

    **Conseil** : si le lecteur ne s’ouvre pas automatiquement, accédez à **This PC** sur l’appareil contrôlé.

    ![This PC](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-thispc.png){class="glboxshadow"}

    Recherchez ensuite le lecteur **GLKVM**. Vous pouvez consulter, déplacer ou supprimer les fichiers qu’il contient.

5. Pour arrêter le partage, cliquez sur **Virtual Media** dans la barre d’outils, puis sur **Stop Sharing**.

    ![Arrêt du partage](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/stop-sharing1.png){class="glboxshadow"}

**Pour partager des fichiers de l’appareil contrôlé vers l’appareil de contrôle, suivez les étapes ci-dessous.**

1. Sur l’appareil contrôlé, déplacez ou copiez les fichiers à partager dans le lecteur **GLKVM**.

    Par exemple, une image nommée « slate7-pro_gl-be10000 » a été déplacée du bureau de l’appareil contrôlé vers le lecteur **GLKVM**.

    ![Déplacement d’un fichier vers le lecteur](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-sharing-copy.png){class="glboxshadow"}

2. Revenez à la console de Comet Pro, cliquez sur **Virtual Media** dans la barre d’outils, puis sur **Stop Sharing**.

    ![Arrêt du partage](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/stop-sharing2.png){class="glboxshadow"}

3. Le fichier apparaît alors dans **Virtual Media**, comme illustré ci-dessous. Vous pouvez maintenant le télécharger depuis Comet Pro vers votre appareil de contrôle.

    ![Fichier partagé](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/file-shared.png){class="glboxshadow"}

### Montage d’images {#image-mounting}

Comet Pro peut émuler un lecteur CD/DVD virtuel ou un lecteur de disque en lecture seule sur l’appareil contrôlé. Vous pouvez accéder à ce lecteur pendant le démarrage du BIOS ou de l’UEFI.

Cette fonction permet notamment de réinstaller le système d’exploitation ou de monter une image ISO pour installer des applications sur l’appareil contrôlé.

1. Faites glisser un fichier dans la zone prévue ou cliquez dessus pour le téléverser. **Assurez-vous que le fichier peut être monté au format ISO**.

    Une fois téléversés, les fichiers s’affichent comme ci-dessous.

    ![Montage d’image 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount1.png){class="glboxshadow"}

2. Cliquez sur **Mount To Remote** -> **Image Mounting**.

    ![Montage d’image 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount2.png){class="glboxshadow"}

3. Dans la fenêtre qui s’ouvre, sélectionnez le fichier et cliquez sur **Mount Image**.

    ![Montage d’image 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount3.png){class="glboxshadow"}

4. Vous pouvez maintenant utiliser ce fichier depuis le lecteur CD de l’appareil contrôlé.

    ![Montage d’image 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/image-mount4.png){class="glboxshadow"}

### Remplacement du support de stockage {#replace-storage-drive}

Vous pouvez brancher un support de stockage USB sur le port USB du KVM pour remplacer le stockage interne.

![Remplacement du support de stockage](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/replace-storage.png){class="glboxshadow"}

### Formatage du disque {#format-disk}

Vous pouvez formater le disque ou désactiver les supports virtuels en un clic.

![Formatage du disque](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/format-storage.png){class="glboxshadow"}

- **Format** : efface toutes les données du disque et réinitialise la structure de son système de fichiers.

- **Disable** : la désactivation des supports virtuels redémarre immédiatement le KVM.

## Centre d’applications {#apps-center}

Dans la console, accédez à **Apps Center** pour retrouver les applications intégrées.

![Centre d’applications](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} est un service VPN maillé basé sur WireGuard. Il crée des réseaux privés chiffrés de pair à pair entre les appareils, sans redirection de ports ni configuration complexe du pare-feu.

Comet Pro intègre Tailscale, ce qui vous permet d’y accéder à distance via le réseau virtuel Tailscale.

Associez Comet Pro et votre appareil de contrôle au même compte Tailscale. Vous pourrez alors accéder à distance à votre Comet Pro en saisissant son **adresse IP virtuelle Tailscale** dans un navigateur sur l’appareil de contrôle, sans installer l’application GLKVM. Consultez [ce guide](../../faq/remote_access_via_tailscale.md){target="_blank"} pour plus de détails.

Après l’association, la console affiche le compte Tailscale lié et donne accès à des fonctions avancées, notamment Exit Node et Subnet Routes.

![Tailscale activé](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} crée des réseaux virtuels superposés et chiffrés pour relier des appareils répartis dans le monde comme s’ils se trouvaient sur le même réseau local.

Comet Pro intègre ZeroTier, ce qui vous permet d’y accéder à distance via le réseau virtuel ZeroTier.

Connectez Comet Pro et votre appareil de contrôle au même réseau ZeroTier. Vous pourrez alors accéder à distance à votre Comet Pro en saisissant son **adresse IP ZeroTier** dans un navigateur sur l’appareil de contrôle, sans installer l’application GLKVM. Consultez [ce guide](../../faq/remote_access_via_zerotier.md){target="_blank"} pour plus de détails.

Après l’association, la console affiche l’identifiant réseau et l’adresse IP virtuelle ZeroTier.

![zerotier enabled](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/zerotier-enabled.png){class="glboxshadow"}

### NetBird {#netbird}

[NetBird](https://netbird.io/){target="_blank"} est une plateforme réseau open source fondée sur le modèle Zero Trust, qui permet de créer des réseaux privés sécurisés pour un usage personnel ou professionnel. Ce réseau superposé basé sur WireGuard® vous permet d’accéder à vos appareils en toute sécurité, où que vous soyez et à tout moment.

Comet Pro intègre NetBird, ce qui vous permet d’y accéder à distance via le réseau virtuel NetBird. Consultez [ce guide](../../faq/remote_access_via_netbird.md){target="_blank"} pour plus de détails.

Après l’association, la console affiche l’adresse IP virtuelle NetBird.

![NetBird activé](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/netbird-enabled.png){class="glboxshadow"}

## Aide {#help}

Dans la console, accédez à **Help** pour consulter des informations sur les KVM GL.iNet et la documentation d’aide, ainsi que pour exporter les journaux à des fins de dépannage.

![Aide](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/help.png){class="glboxshadow"}

## Barre d’outils {#toolbar}

Dans la console, les outils suivants se trouvent dans l’angle supérieur droit :

- [Réduire la barre d’outils](#collapse)
- [Plein écran](#fullscreen)
- [Mise à jour](#upgrade)
- [Statistiques de connexion](#connection-stats)
- [Service cloud](#cloud-service)
- [Déconnexion](#logout)

### Réduction de la barre d’outils {#collapse}

Cliquez sur l’icône de flèche vers le haut dans l’angle supérieur droit pour réduire la barre d’outils.

![Réduction de la barre d’outils](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/collapse_1.png){class="glboxshadow"}

Lorsque la barre d’outils est réduite, cliquez sur l’icône de flèche vers le bas en haut de l’écran pour la développer.

![Réduction de la barre d’outils](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/collapse_2.png){class="glboxshadow"}

### Plein écran {#fullscreen}

Cliquez sur l’icône de plein écran, en forme de carré, dans l’angle supérieur droit pour passer en plein écran.

![Plein écran](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/fullscreen_1.png){class="glboxshadow"}

Pour quitter le plein écran, maintenez la touche **Esc** enfoncée ou cliquez sur l’icône de sortie du plein écran, en forme de grille, dans l’angle supérieur droit.

![Plein écran](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/fullscreen_2.png){class="glboxshadow"}

### Mise à jour {#upgrade}

Cliquez sur la version du micrologiciel dans l’angle supérieur droit pour rechercher des mises à jour.

![Mise à jour du micrologiciel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade_1.png){class="glboxshadow"}

Dans la fenêtre qui s’ouvre, cliquez sur **Local Upgrade** pour téléverser un fichier de micrologiciel.

![Mise à jour du micrologiciel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade_2.png){class="glboxshadow"}

![Mise à jour du micrologiciel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/upgrade_3.png){class="glboxshadow" width=350}

Téléchargez le dernier micrologiciel depuis le [centre de téléchargement des micrologiciels](https://dl.gl-inet.com/kvm){target="_blank"} avant d’effectuer une mise à jour locale.

### Statistiques de connexion {#connection-stats}

La section **Connection Stats** comprend un tableau de bord qui suit la latence, la gigue et d’autres mesures en temps réel.

Cliquez sur l’icône de liste pour afficher l’état de l’appareil et les données en temps réel.

![Tableau de bord des données 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/data_dashboard_1.png){class="glboxshadow"}

Cliquez sur l’icône de graphique pour consulter les statistiques : latence réseau, gigue réseau, taux de perte de paquets, fréquence d’images en temps réel et délai de lecture.

![Tableau de bord des données 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/data_dashboard_2.png){class="glboxshadow"}

### Service cloud {#cloud-service}

GL.iNet KVM Cloud vous permet d’accéder à l’appareil contrôlé à distance. Consultez [ce guide](../../faq/remote_access_via_cloud.md){target="_blank"} pour plus de détails.

Une fois votre Comet Pro associé au cloud, la console affiche l’état du service cloud comme ci-dessous.

![Service cloud](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/cloud.png){class="glboxshadow"}

### Déconnexion {#logout}

Pour vous déconnecter, cliquez sur l’icône **Logout**.
![Déconnexion](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/logout.png){class="glboxshadow"}

## Paramètres {#settings}
Dans la console, cliquez sur l’icône **Settings** dans la barre de navigation pour ouvrir la page de paramètres ci-dessous. Cette fonction a été introduite dans le micrologiciel v1.10.0.

- [Périphériques USB](#usb-devices)
- [Préférences](#preferences)
- [Réseau](#network)
- [Sécurité](#security)
- [Cloud](#cloud)
- [Système](#system)

![Paramètres](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting.png){class="glboxshadow"}

### Périphériques USB {#usb-devices}

La section **USB Device** centralise la gestion de tous les périphériques USB émulés. Vous pouvez y activer ou désactiver les périphériques virtuels pour améliorer la compatibilité avec l’hôte contrôlé.

![Périphériques USB émulés](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_usb_devices.png){class="glboxshadow"}

- **Microphone**

    Lorsque le microphone est coupé, cliquez sur **Settings** pour personnaliser les raccourcis selon vos habitudes. Maintenez le raccourci attribué enfoncé pour parler ; relâchez-le pour couper à nouveau le microphone.

    ![Paramètres du microphone 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mic_setting_1.png){class="glboxshadow" width=600}

    ![Paramètres du microphone 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/mic_setting_2.png){class="glboxshadow" width=434}

  - **Device Identity**

    Personnalisez ou modifiez l’identité du KVM reconnue par l’appareil contrôlé. L’EDID et l’identification de l’appareil restent synchronisés : toute modification de l’un met automatiquement à jour l’autre pour garantir une reconnaissance correcte de l’appareil.

    ![Identité de l’appareil](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/device_identification.png){class="glboxshadow" width=350}

### Préférences {#preferences}

La section **Preferences** permet de gérer les paramètres **Layout Preferences**, **System Settings** et **Device Screen**.

![Préférences](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_preference.png){class="glboxshadow"}

- **Layout Preferences** : choisissez d’afficher la barre d’outils en plein écran et la barre d’état en mode fenêtré selon vos besoins.

- **System Settings** : personnalisez le titre de l’onglet du navigateur (Tab Title), la langue (Language : chinois, anglais ou japonais), le mode de couleur (Color Mode : Light ou Dark) et le fuseau horaire (Timezone) selon votre région.

- **Device Screen** : gérez et prévisualisez l’écran de l’appareil. Les réglages disponibles comprennent le mode Lock Screen (World Clock, Clock Only ou Wallpaper Only), Time Format, Date Format et Wallpaper.

### Réseau {#network}

Vous pouvez consulter et modifier les paramètres réseau de Comet Pro, notamment son nom d’hôte et son adresse IP.

![Réseau](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network.png){class="glboxshadow"}

- **Hostname** : modifiez le nom d’hôte de l’appareil directement dans la console. Cette fonction a été introduite dans le micrologiciel v1.7.0.

    ![Modification du nom d’hôte](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_hostname.png){class="glboxshadow" width=600}

- **Ethernet Settings** : lorsque Comet Pro est connecté à un équipement réseau en amont à l’aide d’un câble Ethernet, les informations de sa connexion Ethernet s’affichent ici.

    Si le protocole est DHCP, la page s’affiche comme ci-dessous.

    ![Connexion Ethernet avec DHCP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_dhcp.png){class="glboxshadow" width=600}

    Pour définir une adresse IP statique, sélectionnez le protocole **Static** et renseignez les paramètres réseau requis, notamment l’adresse IP, le masque de réseau et la passerelle.

    ![Connexion Ethernet avec adresse IP statique](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_static.png){class="glboxshadow" width=600}

- **Wireless** : lorsque Comet Pro est connecté à un réseau Wi-Fi, son adresse IP, sa passerelle et son adresse MAC s’affichent ici.

    ![Configuration Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_wifi.png){class="glboxshadow" width=600}

    Pour connecter l’appareil à un autre réseau Wi-Fi, cliquez sur **Switch Wi-Fi** et sélectionnez un réseau dans la liste des réseaux disponibles.

    ![Connexion à un réseau Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_network_switch_network.png){class="glboxshadow" width=500}

### Sécurité {#security}

La section **Security** permet de modifier le mot de passe administrateur, d’activer l’authentification à deux facteurs et de personnaliser le certificat TLS.

![Sécurité](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_security.png){class="glboxshadow"}

- Modifier le mot de passe administrateur

    ![Modification du mot de passe administrateur](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/change-password.png){class="glboxshadow" width="434"}

- 2FA : activez l’authentification à deux facteurs pour protéger votre compte.

    ![2FA](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/2fa.png){class="glboxshadow"}

- Certificat TLS

    Le système utilise le certificat par défaut préinstallé pour l’accès depuis un navigateur. Pour utiliser un certificat TLS personnalisé, cliquez sur **Custom** dans **TLS Certificate**, puis téléversez votre **fichier de certificat et votre fichier de clé privée**.

    ![Certificat TLS personnalisé](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_security_custom.png){class="glboxshadow"}

### Cloud {#cloud}

La section **Cloud** permet d’accéder à votre appareil et de le gérer à distance via les services cloud.

Vous pouvez associer votre appareil au cloud via une URL. **More Settings** propose d’autres options, notamment Bind With Code et App Download. L’option Disable est également disponible si nécessaire.

![Cloud 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_cloud_1.png){class="glboxshadow"}

Une fois l’association effectuée, les informations du compte cloud associé s’affichent. Cliquez sur **Access Cloud** pour gérer les appareils ou sur **More Settings** pour désactiver le service ou supprimer l’association selon vos besoins.

![Cloud 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_cloud_2.png){class="glboxshadow"}

Vous pouvez également effectuer ces opérations depuis **Cloud Service** dans la barre d’outils supérieure.

### Système {#system}

Les paramètres **System** permettent de configurer les éléments suivants :

![Système](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setting_system.png){class="glboxshadow"}

- **System** : cliquez sur **Reboot** pour redémarrer l’appareil ou sur **Reset** pour effacer sa configuration actuelle et le configurer à nouveau.

- **Upgrade** : activez Beta Center pour recevoir les versions bêta du micrologiciel ou utilisez Local Upgrade pour installer manuellement une mise à jour à partir d’un fichier local.

    ![Mise à jour locale](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10/console/setthing_system_local_update.png){class="glboxshadow" width=400}

- **Help & Support** : Export Log Files permet d’enregistrer les journaux de fonctionnement de l’appareil pour le dépannage et le service après-vente. Help Document donne accès aux guides d’utilisation, aux FAQ et à la documentation de dépannage.
