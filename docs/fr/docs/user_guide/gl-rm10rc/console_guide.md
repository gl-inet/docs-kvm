# Guide de la console du Comet 5G (GL-RM10RC) {#comet-5g-gl-rm10rc-console-guide}

## Session {#session}

Dans la console, accédez à **Session**. Cette page de paramètres comprend quatre sections :

- [Vidéo](#video)
- [Audio et caméra](#audio-camera)
- [Clavier](#keyboard)
- [Souris](#mouse)

### Vidéo {#video}

Dans **Session**, vous pouvez personnaliser les paramètres vidéo : mode d’affichage, qualité vidéo, transmission vidéo, orientation de l’écran et EDID.

![Paramètres vidéo](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session-video.png){class="glboxshadow"}

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

### Audio et caméra {#audio-camera}

Vous pouvez régler les paramètres audio et de caméra de l’appareil contrôlé.

![Paramètres audio et caméra](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session-audio-camera.png){class="glboxshadow"}

- **Speaker** : contrôlez la sortie audio de l’appareil contrôlé, par exemple les sons système ou le son des vidéos.

- **Microphone** : transmettez le son local, par exemple votre voix, de l’appareil de contrôle vers l’appareil distant. Vous pouvez couper le son en un clic et activer le microphone en maintenant un raccourci enfoncé (Press To Speak).

    **Remarque** : vous devez configurer manuellement le raccourci dans les [paramètres](#usb-devices) avant de l’utiliser.

- **Camera** : lorsque la caméra est activée sur l’appareil de contrôle, les images vidéo locales sont transmises directement à l’hôte distant, sur lequel une caméra USB virtuelle est émulée. Les applications de l’hôte distant, comme les outils de visioconférence et FaceTime, peuvent utiliser ce flux vidéo comme si une caméra physique y était directement connectée.

    **Remarque** : cette fonction a été introduite dans le micrologiciel v1.10.0 et fonctionne uniquement en mode WebRTC (FEC). Elle est actuellement accessible uniquement depuis un navigateur web ; elle n’est pas encore prise en charge dans l’application ni dans le client de bureau.

### Clavier {#keyboard}

La section **Keyboard** permet de configurer l’utilisation du clavier sur l’appareil contrôlé.

![Paramètres du clavier](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session_keyboard.png){class="glboxshadow"}

- **Bad Link Mode** : relâche immédiatement les touches. Chaque frappe est envoyée sous la forme d’un bref appui suivi d’un relâchement, ce qui évite les touches bloquées ou les saisies répétées involontaires lors du contrôle à distance.

- **Show Virtual Keyboard** : affichez et utilisez le clavier virtuel dans la console.

    ![Affichage du clavier virtuel](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session_show_virtual_keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS** : permute les touches Cmd et Ctrl pour assurer la compatibilité du clavier entre les différents systèmes d’exploitation.

### Souris {#mouse}

Vous pouvez régler les paramètres de la souris pour améliorer son utilisation sur l’appareil contrôlé.

![Paramètres de la souris](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/session_mouse.png){class="glboxshadow"}

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

![Presse-papiers de la boîte à outils](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_clipboard.png){class="glboxshadow"}

### OCR {#ocr}

L’OCR est une fonction de reconnaissance de texte. Elle permet de sélectionner une zone de l’écran distant et d’en extraire facilement le texte. Cette fonction a été introduite dans le micrologiciel v1.9.0.

Pour l’utiliser, cliquez sur la flèche vers le bas et sélectionnez la langue de reconnaissance souhaitée, par exemple le chinois, l’anglais ou le mode bilingue (Zh/En).

![Langue de reconnaissance du texte](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_ocr.png){class="glboxshadow"}

Cliquez ensuite sur **Capture**. L’écran distant s’assombrit. Tracez un cadre autour du texte à extraire : le système le reconnaît automatiquement. Vous pouvez alors copier le texte reconnu selon vos besoins.

![Copie du texte reconnu](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/ocr_copy_text.png){class="glboxshadow"}

Cette fonction permet de récupérer facilement du texte de l’écran distant, c’est-à-dire de l’appareil contrôlé, et de le copier sur l’appareil de contrôle local.

### Raccourcis {#shortcut}

Les raccourcis permettent d’effectuer des actions plus rapidement sans utiliser le clavier virtuel et de gagner du temps dans vos tâches quotidiennes. Cette section regroupe des raccourcis courants.

![Raccourcis de la boîte à outils 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_shorcut.png){class="glboxshadow"}

Cliquez sur **Modify** pour adapter les raccourcis à vos besoins.

![Raccourcis de la boîte à outils 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_shorcut_modify.png){class="glboxshadow"}

### Wake-on-LAN {#wake-on-lan}

Wake-on-LAN (WOL) est une technologie qui permet d’allumer l’appareil contrôlé à distance ou de le sortir d’un état de faible consommation.

Cliquez sur **Add Device** et choisissez un appareil du même réseau local.

![Réveil à distance dans la boîte à outils](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_wake_on_lan.png){class="glboxshadow"}

![Ajout d’un appareil pour le réveil à distance](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/wol-add-device.png){class="glboxshadow" width=400}

Si l’appareil à ajouter ne figure pas dans la liste, cliquez sur **Add Manually**, puis saisissez son nom et son adresse MAC.

![Ajout manuel d’un appareil pour le réveil à distance](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/wol-add-manually.png){class="glboxshadow" width=400}

### Terminal {#terminal}

Vous pouvez accéder au terminal de Comet 5G pour effectuer des réglages avancés. Cliquez sur **Access**.

![Terminal de la boîte à outils 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_terminal_1.png){class="glboxshadow"}

Le terminal GLKVM s’ouvre.

![Terminal de la boîte à outils 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbox_terminal_2.png){class="glboxshadow"}

## Accessoires {#accessories}

GL.iNet propose des accessoires KVM en option pour allumer et éteindre l’appareil à distance.

Consultez d’abord le guide d’utilisation correspondant pour connecter l’accessoire à votre appareil contrôlé.

- [Guide d’utilisation du Fingerbot (FGB-01)](../gl-fgb-01/index.md){target="_blank"}

- [Guide d’utilisation de la carte ATX (GL-ATXPC)](../gl-atx-board/index.md){target="_blank"}

Connectez-vous ensuite à la console KVM et accédez à **Accessories**. Les paramètres de l’accessoire ne sont disponibles qu’une fois celui-ci installé.

### Fingerbot {#fingerbot}

Le Fingerbot se fixe sur le bouton d’alimentation physique de l’appareil contrôlé pour commander son alimentation à distance.

Son fonctionnement dépend des paramètres définis dans la console.

![Paramètres de l’accessoire Fingerbot](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/fingerbot.png){class="glboxshadow"}

- **Time** : durée d’appui du Fingerbot. Vous pouvez la régler sur 0.5s/3s/8s.

- **Strength** : deux niveaux de force d’appui sont disponibles : Lightly Press et Firmly Press.

    - **Lightly Press** : convient aux boutons à course courte ou souples.

    - **Firmly Press** : convient aux boutons à course longue ou résistants.

    ![Mode d’appui](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/press_mode.png){class="glboxshadow gl-70-desktop"}

### Alimentation ATX {#atx-power}

La carte ATX s’installe dans le boîtier de l’ordinateur pour commander à distance son allumage, son extinction et son redémarrage.

Son fonctionnement dépend des paramètres définis dans la console.

![Paramètres d’alimentation ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/atxboard.png){class="glboxshadow"}

- **Power (Short Press)** : sert à allumer normalement l’appareil ou à sortir le système de veille.

- **Power (Long Press)** : force l’arrêt de l’appareil.

- **Restart** : redémarre l’appareil.

## Supports virtuels {#virtual-media}

Dans la console, accédez à **Virtual Media**. Vous pouvez y effectuer les opérations suivantes :

- [Partage de fichiers](#file-sharing)
- [Montage d’images](#image-mounting)
- [Remplacement du support de stockage](#replace-storage-drive)
- [Formatage du disque](#format-disk)

![Supports virtuels](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/virtual-media.png){class="glboxshadow"}

### Partage de fichiers {#file-sharing}

Comet 5G peut émuler un support USB accessible en lecture et en écriture afin de partager et gérer des fichiers entre l’appareil de contrôle et l’appareil contrôlé.

**Pour partager des fichiers de l’appareil de contrôle vers l’appareil contrôlé, suivez les étapes ci-dessous.**

1. Faites glisser des fichiers dans la zone prévue ou cliquez dessus pour les téléverser depuis votre appareil de contrôle. Vous pouvez également les importer depuis une URL.

    Une fois téléversés, les fichiers s’affichent comme ci-dessous.

    ![Téléversement de fichiers](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing1.png){class="glboxshadow"}

2. Cliquez sur **Mount To Remote** -> **File Sharing**.

    ![Partage de fichiers](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing2.png){class="glboxshadow"}

3. Une fenêtre présente les étapes du partage de fichiers dans la console, comme illustré ci-dessous.

    ![Instructions de partage de fichiers](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing3.png){class="glboxshadow"}

4. Patientez un instant : un lecteur nommé **« GLKVM »** apparaît automatiquement à l’écran. Les fichiers que vous avez téléversés de l’appareil de contrôle vers Comet 5G sont alors partagés avec l’appareil contrôlé. Vous pouvez les consulter, les déplacer ou les supprimer depuis ce lecteur sur l’appareil contrôlé.

    ![Lecteur GLKVM](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing4.png){class="glboxshadow"}

    **Conseil** : si le lecteur ne s’ouvre pas automatiquement, accédez à **This PC** sur l’appareil contrôlé.

    ![Lecteur GLKVM dans This PC](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/thispc.png){class="glboxshadow"}

    Recherchez ensuite le lecteur **GLKVM**. Vous pouvez consulter, déplacer ou supprimer les fichiers qu’il contient.

5. Pour arrêter le partage, cliquez sur **Virtual Media** dans la barre d’outils, puis sur **Stop Sharing**.

    ![Arrêt du partage 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/stop-sharing1.png){class="glboxshadow"}

**Pour partager des fichiers de l’appareil contrôlé vers l’appareil de contrôle, suivez les étapes ci-dessous.**

1. Sur l’appareil contrôlé, déplacez ou copiez les fichiers à partager dans le lecteur **GLKVM**.

    Par exemple, un fichier PDF nommé « slate7pro_datasheet » a été déplacé du Bureau de l’appareil contrôlé vers le lecteur **GLKVM**.

    ![Déplacement d’un fichier vers le lecteur](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing5.png){class="glboxshadow"}

2. Revenez à la console de Comet 5G, cliquez sur **Virtual Media** dans la barre d’outils, puis sur **Stop Sharing**.

    ![Arrêt du partage 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/stop-sharing2.png){class="glboxshadow"}

3. Le fichier apparaît alors dans **Virtual Media**, comme illustré ci-dessous. Vous pouvez maintenant le télécharger depuis Comet 5G vers votre appareil de contrôle.

    ![Fichier partagé](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/file-sharing6.png){class="glboxshadow"}

### Montage d’images {#image-mounting}

Comet 5G peut émuler un lecteur CD/DVD virtuel ou un lecteur de disque en lecture seule sur l’appareil contrôlé. Vous pouvez accéder à ce lecteur pendant le démarrage du BIOS ou de l’UEFI.

Cette fonction permet notamment de réinstaller le système d’exploitation ou de monter une image ISO pour installer des applications sur l’appareil contrôlé.

1. Faites glisser un fichier dans la zone prévue ou cliquez dessus pour le téléverser. **Assurez-vous que le fichier peut être monté au format ISO**.

    Une fois téléversés, les fichiers s’affichent comme ci-dessous.

    ![Montage d’une image disque 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting1.png){class="glboxshadow"}

2. Cliquez sur **Mount To Remote** -> **Image Mounting**.

    ![Montage d’une image disque 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting2.png){class="glboxshadow"}

3. Dans la fenêtre qui s’ouvre, sélectionnez le fichier et cliquez sur **Mount Image**.

    ![Montage d’une image disque 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting3.png){class="glboxshadow"}

4. Une fenêtre présente les étapes du montage dans la console, comme illustré ci-dessous.

    ![Montage d’une image disque 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting4.png){class="glboxshadow"}

5. Vous pouvez maintenant utiliser ce fichier depuis le lecteur CD de l’appareil contrôlé.

    ![Montage d’une image disque 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/image-mounting5.png){class="glboxshadow"}

### Remplacement du support de stockage {#replace-storage-drive}

Vous pouvez brancher un support de stockage USB sur le port USB du KVM pour remplacer le stockage interne.

![Remplacement du support de stockage](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/replace-storage.png){class="glboxshadow"}

### Formatage du disque {#format-disk}

Vous pouvez formater le disque ou désactiver les supports virtuels en un clic.

![Formatage du disque](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/format-storage.png){class="glboxshadow"}

- **Format** : efface toutes les données du disque et réinitialise la structure de son système de fichiers.

- **Disable** : la désactivation des supports virtuels redémarre immédiatement le KVM.

## Centre d’applications {#apps-center}

Dans la console, accédez à **Apps Center** pour retrouver les applications intégrées.

![Centre d’applications](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} est un service VPN maillé basé sur WireGuard. Il crée des réseaux privés chiffrés de pair à pair entre les appareils, sans redirection de ports ni configuration complexe du pare-feu.

Comet 5G intègre Tailscale, ce qui vous permet d’y accéder à distance via le réseau virtuel Tailscale.

Associez Comet 5G et votre appareil de contrôle au même compte Tailscale. Vous pourrez alors accéder à distance à votre Comet 5G en saisissant son **adresse IP virtuelle Tailscale** dans un navigateur sur l’appareil de contrôle, sans installer l’application GLKVM. Consultez [ce guide](../../faq/remote_access_via_tailscale.md){target="_blank"} pour plus de détails.

Après l’association, la console affiche le compte Tailscale lié et donne accès à des fonctions avancées, notamment Exit Node et Subnet Routes.

![Tailscale activé](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} crée des réseaux virtuels superposés et chiffrés pour relier des appareils répartis dans le monde comme s’ils se trouvaient sur le même réseau local.

Comet 5G intègre ZeroTier, ce qui vous permet d’y accéder à distance via le réseau virtuel ZeroTier.

Connectez Comet 5G et votre appareil de contrôle au même réseau ZeroTier. Vous pourrez alors accéder à distance à votre Comet 5G en saisissant son **adresse IP ZeroTier** dans un navigateur sur l’appareil de contrôle, sans installer l’application GLKVM. Consultez [ce guide](../../faq/remote_access_via_zerotier.md){target="_blank"} pour plus de détails.

Après l’association, la console affiche l’identifiant réseau et l’adresse IP virtuelle ZeroTier.

![ZeroTier activé](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/apps-zerotier-enabled.png){class="glboxshadow"}

### NetBird {#netbird}

[NetBird](https://netbird.io/){target="_blank"} est une plateforme réseau open source fondée sur le modèle Zero Trust, qui permet de créer des réseaux privés sécurisés pour un usage personnel ou professionnel. Ce réseau superposé basé sur WireGuard® vous permet d’accéder à vos appareils en toute sécurité, où que vous soyez et à tout moment.

Comet 5G intègre NetBird, ce qui vous permet d’y accéder à distance via le réseau virtuel NetBird. Consultez [ce guide](../../faq/remote_access_via_netbird.md){target="_blank"} pour plus de détails.

Après l’association, la console affiche l’adresse IP virtuelle NetBird.

![NetBird activé](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/apps-netbird-enabled.png){class="glboxshadow"}

## Aide {#help}

Dans la console, accédez à **Help** pour consulter des informations sur les KVM GL.iNet et la documentation d’aide, ainsi que pour exporter les journaux à des fins de dépannage.

![Aide](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/help.png){class="glboxshadow"}

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

![Réduction de la barre d’outils 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_collapse_1.png){class="glboxshadow"}

Lorsque la barre d’outils est réduite, cliquez sur l’icône de flèche vers le bas en haut de l’écran pour la développer.

![Réduction de la barre d’outils 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_collapse_2.png){class="glboxshadow"}

### Plein écran {#fullscreen}

Cliquez sur l’icône de plein écran, en forme de carré, dans l’angle supérieur droit pour passer en plein écran.

![Mode plein écran](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_fullscreen_1.png){class="glboxshadow"}

Pour quitter le plein écran, maintenez la touche **Esc** enfoncée ou cliquez sur l’icône de sortie du plein écran, en forme de grille, dans l’angle supérieur droit.

![Mode plein écran](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_fullscreen_2.png){class="glboxshadow"}

### Mise à jour {#upgrade}

Cliquez sur la version du micrologiciel dans l’angle supérieur droit pour rechercher des mises à jour.

![Mise à niveau du micrologiciel 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_upgrade_1.png){class="glboxshadow"}

Dans la fenêtre qui s’ouvre, cliquez sur **Local Upgrade** pour téléverser un fichier de micrologiciel.

![Mise à niveau du micrologiciel 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_upgrade_2.png){class="glboxshadow" width=400}

![Mise à niveau du micrologiciel 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/toolbar_upgrade_3.png){class="glboxshadow" width=400}

Téléchargez le dernier micrologiciel depuis le [centre de téléchargement des micrologiciels](https://dl.gl-inet.com/kvm){target="_blank"} avant d’effectuer une mise à jour locale.

### Statistiques de connexion {#connection-stats}

La section **Connection Stats** comprend un tableau de bord qui suit la latence, la gigue et d’autres mesures en temps réel.

Cliquez sur l’icône de liste pour afficher l’état de l’appareil et les données en temps réel.

![Tableau de bord des données de connexion 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/data_dashboard_1.png){class="glboxshadow"}

Cliquez sur l’icône de graphique pour consulter les statistiques : latence réseau, gigue réseau, taux de perte de paquets, fréquence d’images en temps réel et délai de lecture.

![Tableau de bord des données de connexion 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/data_dashboard_2.png){class="glboxshadow"}

### Service cloud {#cloud-service}

GL.iNet KVM Cloud vous permet d’accéder à l’appareil contrôlé à distance. Consultez [ce guide](../../faq/remote_access_via_cloud.md){target="_blank"} pour plus de détails.

Une fois votre Comet 5G associé au cloud, la console affiche l’état du service cloud comme ci-dessous.

![Service Cloud](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/cloud-services.png){class="glboxshadow"}

### Déconnexion {#logout}

Pour vous déconnecter, cliquez sur l’icône **Logout**.
![Disposition de l’interface](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/logout.png){class="glboxshadow"}

## Paramètres {#settings}
Dans la console, cliquez sur l’icône **Settings** dans la barre de navigation pour ouvrir la page de paramètres ci-dessous. Cette fonction a été introduite dans le micrologiciel v1.10.0.

- [Périphériques USB](#usb-devices)
- [Préférences](#preferences)
- [Réseau](#network)
- [Sécurité](#security)
- [Cloud](#cloud)
- [Système](#system)

![Paramètres](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting.png){class="glboxshadow"}

### Périphériques USB {#usb-devices}

La section **USB Device** centralise la gestion de tous les périphériques USB émulés. Vous pouvez y activer ou désactiver les périphériques virtuels pour améliorer la compatibilité avec l’hôte contrôlé.

![Périphériques USB émulés](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_usb_devices.png){class="glboxshadow"}

- **Microphone**

    Lorsque le microphone est coupé, cliquez sur **Settings** pour personnaliser les raccourcis selon vos habitudes. Maintenez le raccourci attribué enfoncé pour parler ; relâchez-le pour couper à nouveau le microphone.

    ![Paramètres du microphone 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/mic_setting_1.png){class="glboxshadow" width=600}

    ![Paramètres du microphone 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/mic_setting_2.png){class="glboxshadow" width=434}

- **Device Identity**

    Personnalisez ou modifiez l’identité du KVM reconnue par l’appareil contrôlé. L’EDID et l’identification de l’appareil restent synchronisés : toute modification de l’un met automatiquement à jour l’autre pour garantir une reconnaissance correcte de l’appareil.

    ![Identité de l’appareil](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/settings_device_identity.png){class="glboxshadow" width=350}

### Préférences {#preferences}

La section **Preferences** permet de gérer les paramètres **Layout Preferences**, **System Settings** et **Device Screen**.

![Préférences](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_preference.png){class="glboxshadow"}

- **Layout Preferences** : choisissez d’afficher la barre d’outils en plein écran et la barre d’état en mode fenêtré selon vos besoins.

- **System Settings** : personnalisez le titre de l’onglet du navigateur (Tab Title), la langue (Language : chinois, anglais ou japonais), le mode de couleur (Color Mode : Light ou Dark) et le fuseau horaire (Timezone) selon votre région.

- **Device Screen** : gérez et prévisualisez l’écran de l’appareil. Les réglages disponibles comprennent le mode Lock Screen (World Clock, Clock Only ou Wallpaper Only), Time Format, Date Format et Wallpaper.

### Réseau {#network}

Vous pouvez consulter et modifier les paramètres réseau de Comet 5G, notamment son nom d’hôte et son adresse IP.

![Réseau](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network.png){class="glboxshadow"}

- **Hostname** : modifiez le nom d’hôte de l’appareil directement dans la console. Cette fonction a été introduite dans le micrologiciel v1.7.0.

    ![Modification du nom d’hôte](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_hostname.png){class="glboxshadow" width=600}

- **Ethernet Settings** : lorsque Comet 5G est connecté à un équipement réseau en amont à l’aide d’un câble Ethernet, les informations de sa connexion Ethernet s’affichent ici.

    Si le protocole est DHCP, la page s’affiche comme ci-dessous.

    ![Paramètres Ethernet en DHCP](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_dhcp.png){class="glboxshadow" width=600}

    Pour définir une adresse IP statique, sélectionnez le protocole **Static** et renseignez les paramètres réseau requis, notamment l’adresse IP, le masque de réseau et la passerelle.

    ![Paramètres Ethernet avec adresse IP statique](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_static.png){class="glboxshadow" width=600}

- **Wireless** : le Comet 5G prend en charge deux modes sans fil, **Station Mode** et **AP Mode**, pour répondre à différents besoins d’accès réseau.

    Cliquez sur **Modify** pour changer le mode réseau ou consulter son adresse IP, sa passerelle et son adresse MAC.

    ![Modification des paramètres Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_modify_wifi.png){class="glboxshadow" width=600}

    - **Station Mode**

        Ce mode convient lorsque le Comet 5G peut se connecter à un réseau sans fil existant.

        Dans ce mode, le Comet 5G fonctionne comme un client sans fil. Il recherche un point d’accès Wi-Fi amont (par exemple, un routeur) et s’y connecte pour accéder au réseau.

        ![Paramètres Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_wifi.png){class="glboxshadow"}

        Pour vous connecter à un autre réseau Wi-Fi, cliquez sur **Switch Wi-Fi** en bas de la page.

        ![Changement de réseau Wi-Fi 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/switch_wifi_1.png){class="glboxshadow"}

        Sélectionnez ensuite un réseau Wi-Fi dans la liste des réseaux disponibles.

        ![Changement de réseau Wi-Fi 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/switch-wifi2.png){class="glboxshadow"}

    - **AP Mode**

        Ce mode permet de créer un réseau local pour contrôler votre KVM à proximité, hors ligne et sans réseau externe.

        Dans ce mode, le Comet 5G fait lui-même office de point d’accès Wi-Fi auquel peuvent se connecter des appareils tels que des smartphones ou des ordinateurs portables. Il ne peut cependant plus accéder au réseau amont via le Wi-Fi.

        ![Wi-Fi en mode point d’accès](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/wifi-ap-mode.png){class="glboxshadow"}

- **Cellular** : le Comet 5G dispose d’un module cellulaire intégré pour accéder au réseau mobile à l’aide d’une carte SIM.

    Une fois la carte SIM détectée, cliquez sur **Modify** pour consulter les détails de la connexion cellulaire (par exemple, les informations de l’opérateur, le numéro de téléphone, l’ICCID et le profil APN actuel).

    ![Modification des paramètres cellulaires](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/celluar_modify.png){class="glboxshadow" width=600}

    ![Paramètres cellulaires](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_network_cellular.png){class="glboxshadow"}

    - **SIM Settings** permet de gérer les paramètres cellulaires (par exemple, l’APN et la MTU).

    - **AT command** permet d’exécuter des commandes AT et d’obtenir les réponses du modem.

    - **Cellular Firewall** permet de définir les règles de pare-feu pour les réseaux cellulaires.

    La connexion cellulaire offre ainsi un réseau de secours fiable lorsque les connexions Ethernet ou Wi-Fi ne sont pas disponibles.

### Sécurité {#security}

La section **Security** permet de modifier le mot de passe administrateur, d’activer l’authentification à deux facteurs et de personnaliser le certificat TLS.

![Paramètres de sécurité](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_security.png){class="glboxshadow"}

- Modifier le mot de passe administrateur

    ![Modification du mot de passe administrateur](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/change-password.png){class="glboxshadow" width="434"}

- 2FA : activez l’authentification à deux facteurs pour protéger votre compte.

    ![Authentification à deux facteurs](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/2fa.png){class="glboxshadow"}

- Certificat TLS

    Le système utilise le certificat par défaut préinstallé pour l’accès depuis un navigateur. Pour utiliser un certificat TLS personnalisé, cliquez sur **Custom** dans **TLS Certificate**, puis téléversez votre **fichier de certificat et votre fichier de clé privée**.

    ![Certificat TLS personnalisé](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_security_custom.png){class="glboxshadow"}

### Cloud {#cloud}

La section **Cloud** permet d’accéder à votre appareil et de le gérer à distance via les services cloud.

Vous pouvez associer votre appareil au cloud via une URL. **More Settings** propose d’autres options, notamment Bind With Code et App Download. L’option Disable est également disponible si nécessaire.

![Service Cloud 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_cloud_1.png){class="glboxshadow"}

Une fois l’association effectuée, les informations du compte cloud associé s’affichent. Cliquez sur **Access Cloud** pour gérer les appareils ou sur **More Settings** pour désactiver le service ou supprimer l’association selon vos besoins.

![Service Cloud 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_cloud_2.png){class="glboxshadow"}

Vous pouvez également effectuer ces opérations depuis **Cloud Service** dans la barre d’outils supérieure.

### Système {#system}

Les paramètres **System** permettent de configurer les éléments suivants :

![Paramètres système](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setting_system.png){class="glboxshadow"}

- **System** : cliquez sur **Reboot** pour redémarrer l’appareil ou sur **Reset** pour effacer sa configuration actuelle et le configurer à nouveau.

- **Upgrade** : activez Beta Center pour recevoir les versions bêta du micrologiciel ou utilisez Local Upgrade pour installer manuellement une mise à jour à partir d’un fichier local.

    ![Mise à niveau locale](https://static.gl-inet.com/docs/kvm/user_guide/gl-rm10rc/console/setthing_system_local_update.png){class="glboxshadow" width=400}

- **Help & Support** : Export Log Files permet d’enregistrer les journaux de fonctionnement de l’appareil pour le dépannage et le service après-vente. Help Document donne accès aux guides d’utilisation, aux FAQ et à la documentation de dépannage.
