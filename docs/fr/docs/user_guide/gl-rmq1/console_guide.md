# Guide de la console du Comet Q (GL-RMQ1) {#comet-q-gl-rmq1-console-guide}

## Paramètres {#settings}

Dans la console, accédez à **Settings**. La page des paramètres comprend quatre sections :

- [Vidéo](#video)
- [Audio, clavier et souris](#audiokeyboardmouse)
- [Système](#system)
- [Réseau](#network)

### Recherche rapide {#quick-search}

Pour trouver rapidement un paramètre, saisissez des mots-clés en haut de la page Settings.

![Recherche rapide](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/quick-search.png){class="glboxshadow"}

### Vidéo {#video}

Vous pouvez personnaliser les paramètres vidéo dans la console : EDID, qualité vidéo, transmission vidéo et orientation de l’écran.

![Paramètres vidéo](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-video.png){class="glboxshadow"}

- **Type** : sélectionnez le type de votre appareil contrôlé.

    Le système applique automatiquement le mode de souris et les paramètres EDID recommandés pour offrir le meilleur rapport d’affichage et une commande précise. Modifiez cette option si l’appareil n’est pas reconnu correctement ou si vous devez utiliser un type personnalisé.

- **EDID** : abréviation de Extended Display Identification Data, cette fonction sélectionne automatiquement les paramètres d’affichage optimaux.

    Le réglage par défaut convient à la plupart des situations et ne nécessite généralement aucune modification. Consultez [ce guide](../../tutorials/how_to_set_edid_for_glkvm.md){target="_blank"} pour plus de détails. Si l’écran ne s’actualise pas après une modification de l’EDID, redémarrez l’appareil contrôlé.

- **Mode** : choisissez le mode Smart ou Normal selon vos besoins. Le mode Smart réduit la consommation de bande passante, notamment lorsque le réseau est de mauvaise qualité.

- **Quality** : réglez la qualité vidéo sur Low/Medium/High/Ultra-high/Lossless selon votre environnement réseau et vos besoins en résolution.

- **Transfer** : choisissez le mode de transmission vidéo entre WebRTC, WebRTC (FEC) et Direct. Le mode Direct ne transmet pas le son.

    !!! note "Quelle est la différence entre WebRTC, WebRTC (FEC) et Direct ?"

        - **WebRTC** : associe une vidéo fluide et un son stable pour le contrôle à distance en temps réel.

        - **WebRTC (FEC)** : ajoute une correction d’erreurs anticipée pour améliorer la stabilité de la connexion lorsque le réseau est de mauvaise qualité ou instable. Ce mode corrige automatiquement les pertes de paquets en transmettant une petite quantité de données redondantes, ce qui réduit les scintillements et les ralentissements.

        - **Direct** : offre la latence la plus faible et une qualité vidéo sans perte, mais ne prend pas en charge la transmission audio.

- **Orientation** : réglez l’angle de rotation de la console sur 0°/90°/180°/270°.

- **View** : ce paramètre détermine la mise à l’échelle de l’écran lorsque la fenêtre du navigateur est redimensionnée. Options disponibles : Adaptive, Best Picture Quality et Original Pixel.

### Audio, clavier et souris {#audiokeyboardmouse}

Vous pouvez ajuster les paramètres audio, du clavier et de la souris.

![Paramètres audio, du clavier et de la souris](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/audio-keyboard-mouse.png){class="glboxshadow"}

- **Speaker** : contrôlez la sortie audio de l’appareil contrôlé, par exemple les sons système ou le son des vidéos.

- **Microphone** : transmettez le son local, par exemple votre voix, de l’appareil de contrôle vers l’appareil distant. Vous pouvez couper le son en un clic et activer le microphone en maintenant un raccourci enfoncé (Press To Speak).

    ![Paramètres du microphone](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/mic-settings.png){class="glboxshadow"}

    ![Maintien du raccourci pour parler](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/press-to-speak.png){class="glboxshadow"}

- **Keyboard** : activez ou désactivez le clavier de l’appareil contrôlé.

- **Bad Link Mode** : relâche immédiatement les touches. Chaque frappe est envoyée sous la forme d’un bref appui suivi d’un relâchement, ce qui évite les touches bloquées ou les saisies répétées involontaires lors du contrôle à distance.

- **Show Virtual Keyboard** : affichez et utilisez le clavier virtuel dans la console.

    ![Affichage du clavier virtuel](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-keyboard.png){class="glboxshadow"}

- **Swap Command and Ctrl for MacOS** : permute les touches Cmd et Ctrl pour assurer la compatibilité du clavier entre les différents systèmes d’exploitation.

- **Mouse** : activez ou désactivez la souris de l’appareil contrôlé.

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

### Système {#system}

Vous pouvez personnaliser les paramètres d’affichage système de la console ou réinitialiser l’appareil en un clic.

![Paramètres système](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-system.png){class="glboxshadow"}

- **Device Identity** : personnalisez ou modifiez l’identité du KVM présentée à l’appareil contrôlé. L’EDID et l’identification de l’appareil restent synchronisés : modifier l’un met automatiquement l’autre à jour pour garantir la bonne reconnaissance de l’appareil.

    ![Identité de l’appareil](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/device-identity.png){class="glboxshadow"}

- **Language** : définissez la langue de la console sur Chinese ou English.

- **Color Mode** : choisissez le thème Light ou Dark.

- **Time Zone** : personnalisez le fuseau horaire de la console KVM.

- **Reset KVM** : rétablissez les paramètres d’usine de votre KVM en un clic.

### Réseau {#network}

Vous pouvez consulter et modifier les paramètres réseau de Comet Q, notamment son nom d’hôte et son adresse IP.

![Paramètres réseau](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/settings-network.png){class="glboxshadow"}

- **Hostname** : modifiez le nom d’hôte de l’appareil directement dans la console.

    ![Modification du nom d’hôte](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/hostname.png){class="glboxshadow"}

- **Wi-Fi** : l’adresse IP Wi-Fi du Comet Q s’affiche ici lorsqu’il est connecté à un réseau Wi-Fi. Cliquez sur le SSID Wi-Fi ou sur la flèche à droite pour consulter les détails de la connexion : SSID, adresse IP attribuée, passerelle et adresse MAC utilisée par votre Comet Q pour cette connexion.

    ![Configuration Wi-Fi](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/wifi-config.png){class="glboxshadow"}

    Pour vous connecter à un autre réseau Wi-Fi, cliquez sur **Switch Wi-Fi**, puis sélectionnez un réseau dans la liste des réseaux disponibles.

## Boîte à outils {#toolbox}

Dans la console, accédez à **Toolbox**. La boîte à outils comprend trois sections :

- [Presse-papiers](#clipboard)
- [Raccourcis](#shortcut)
- [Terminal](#terminal)

### Presse-papiers {#clipboard}

Le presse-papiers permet de coller facilement du texte de l’appareil de contrôle sur l’appareil contrôlé, sans transférer de fichiers.

![Presse-papiers de la boîte à outils](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-clipboard.png){class="glboxshadow"}

### Raccourcis {#shortcut}

Les raccourcis permettent d’effectuer des actions plus rapidement sans utiliser le clavier virtuel et de gagner du temps dans vos tâches quotidiennes. Cette section regroupe des raccourcis courants.

![Raccourcis de la boîte à outils 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut1.png){class="glboxshadow"}

Cliquez sur **Modify** pour adapter les raccourcis à vos besoins.

![Raccourcis de la boîte à outils 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-shortcut2.png){class="glboxshadow"}

### Terminal {#terminal}

Vous pouvez accéder au terminal de Comet Q pour effectuer des réglages avancés. Cliquez sur **Access**.

![Terminal de la boîte à outils 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal1.png){class="glboxshadow"}

Le terminal GLKVM s’ouvre.

![Terminal de la boîte à outils 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/toolbox-terminal2.png){class="glboxshadow"}

## Supports virtuels {#virtual-media}

Dans la console, accédez à **Virtual Media**. Le Comet Q peut émuler un lecteur USB accessible en lecture et en écriture pour partager et gérer des fichiers entre l’appareil de contrôle et l’appareil contrôlé.

![Supports virtuels](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/virtual-media.png){class="glboxshadow"}

### Partage de fichiers {#file-sharing}

**Pour partager des fichiers de l’appareil de contrôle vers l’appareil contrôlé, suivez les étapes ci-dessous.**

1. Faites glisser des fichiers dans la zone prévue ou cliquez dessus pour les téléverser depuis votre appareil de contrôle. Vous pouvez également les importer depuis une URL.

    Une fois téléversés, les fichiers s’affichent comme ci-dessous.

    ![Partage de fichiers 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing1.png){class="glboxshadow"}

2. Cliquez sur **Mount To Remote** -> **File Sharing**.

    ![Partage de fichiers 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing2.png){class="glboxshadow"}

3. Une fenêtre présente les étapes du partage de fichiers dans la console, comme illustré ci-dessous.

    ![Partage de fichiers 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing3.png){class="glboxshadow"}

4. Patientez un instant. Un lecteur nommé **« GLKVM »** peut apparaître automatiquement à l’écran. Les fichiers téléversés depuis l’appareil de contrôle vers le Comet Q sont alors partagés avec l’appareil contrôlé. Vous pouvez consulter, déplacer ou supprimer les fichiers de ce lecteur depuis l’appareil contrôlé.

    ![Partage de fichiers 4](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing4.png){class="glboxshadow"}

    **Conseil** : si le lecteur ne s’ouvre pas automatiquement, accédez à **This PC** sur l’appareil contrôlé.

    ![Lecteur GLKVM dans This PC](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/thispc.png){class="glboxshadow"}

    Recherchez ensuite le lecteur **GLKVM**. Vous pouvez consulter, déplacer ou supprimer les fichiers qu’il contient.

5. Pour arrêter le partage, cliquez sur **Virtual Media** dans la barre d’outils, puis sur **Stop Sharing**.

    ![Arrêt du partage 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing1.png){class="glboxshadow"}

**Pour partager des fichiers de l’appareil contrôlé vers l’appareil de contrôle, suivez les étapes ci-dessous.**

1. Sur l’appareil contrôlé, déplacez ou copiez les fichiers à partager dans le lecteur **GLKVM**.

    Par exemple, un fichier PDF nommé « gl-rm10_datasheet » a été déplacé du Bureau de l’appareil contrôlé vers le lecteur **GLKVM**.

    ![Partage de fichiers 5](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing5.png){class="glboxshadow"}

2. Revenez à la console de Comet Q, cliquez sur **Virtual Media** dans la barre d’outils, puis sur **Stop Sharing**.

    ![Arrêt du partage 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/stop-sharing2.png){class="glboxshadow"}

3. Le fichier apparaît alors dans **Virtual Media**, comme illustré ci-dessous. Vous pouvez maintenant le télécharger depuis Comet Q vers votre appareil de contrôle.

    ![Partage de fichiers 6](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/file-sharing6.png){class="glboxshadow"}

### Formatage du disque {#format-disk}

Vous pouvez formater le disque ou désactiver les supports virtuels en un clic.

![Formatage du disque](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/format-disable.png){class="glboxshadow"}

- **Format** : efface toutes les données du disque et réinitialise la structure de son système de fichiers.

- **Disable** : la désactivation des supports virtuels redémarre immédiatement le KVM.

## Centre d’applications {#apps-center}

Dans la console, accédez à **Apps Center** pour retrouver les applications intégrées.

![Centre d’applications](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-center.png){class="glboxshadow"}

### Tailscale {#tailscale}

[Tailscale](https://tailscale.com/){target="_blank"} est un service VPN maillé basé sur WireGuard. Il crée des réseaux privés chiffrés de pair à pair entre les appareils, sans redirection de ports ni configuration complexe du pare-feu.

Comet Q intègre Tailscale, ce qui vous permet d’y accéder à distance via le réseau virtuel Tailscale.

Associez Comet Q et votre appareil de contrôle au même compte Tailscale. Vous pourrez alors accéder à distance à votre Comet Q en saisissant son **adresse IP virtuelle Tailscale** dans un navigateur sur l’appareil de contrôle, sans installer l’application GLKVM. Consultez [ce guide](../../faq/remote_access_via_tailscale.md){target="_blank"} pour plus de détails.

Après l’association, la console affiche le compte Tailscale lié et donne accès à des fonctions avancées, notamment Exit Node et Subnet Routes.

![Tailscale activé](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-tailscale-enabled.png){class="glboxshadow"}

### ZeroTier {#zerotier}

[ZeroTier](https://www.zerotier.com/){target="_blank"} crée des réseaux virtuels superposés et chiffrés pour relier des appareils répartis dans le monde comme s’ils se trouvaient sur le même réseau local.

Comet Q intègre ZeroTier, ce qui vous permet d’y accéder à distance via le réseau virtuel ZeroTier.

Connectez Comet Q et votre appareil de contrôle au même réseau ZeroTier. Vous pourrez alors accéder à distance à votre Comet Q en saisissant son **adresse IP ZeroTier** dans un navigateur sur l’appareil de contrôle, sans installer l’application GLKVM. Consultez [ce guide](../../faq/remote_access_via_zerotier.md){target="_blank"} pour plus de détails.

Après l’association, la console affiche l’identifiant réseau et l’adresse IP virtuelle ZeroTier.

![ZeroTier activé](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/apps-zerotier-enabled.png){class="glboxshadow"}

## Aide {#help}

Dans la console, accédez à **Help** pour consulter des informations sur les KVM GL.iNet et la documentation d’aide, ainsi que pour exporter les journaux à des fins de dépannage.

![Aide](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/help.png){class="glboxshadow"}

## Barre d’outils {#toolbar}

Dans la console, les outils suivants se trouvent dans l’angle supérieur droit :

- [Réduire la barre d’outils](#collapse)
- [Plein écran](#fullscreen)
- [Mise à jour](#upgrade)
- [Service cloud](#cloud-service)
- [Sécurité](#security)
- Redémarrer
- Se déconnecter

### Réduction de la barre d’outils {#collapse}

Cliquez sur l’icône de flèche vers le haut dans l’angle supérieur droit pour réduire la barre d’outils.

![Réduction de la barre d’outils](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse1.png){class="glboxshadow"}

Lorsque la barre d’outils est réduite, cliquez sur l’icône de flèche vers le bas en haut de l’écran pour la développer.

![Réduction de la barre d’outils](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/collapse2.png){class="glboxshadow"}

### Plein écran {#fullscreen}

Cliquez sur l’icône de plein écran, en forme de carré, dans l’angle supérieur droit pour passer en plein écran.

![Mode plein écran](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen1.png){class="glboxshadow"}

Pour quitter le plein écran, maintenez la touche **Esc** enfoncée ou cliquez sur l’icône de sortie du plein écran, en forme de grille, dans l’angle supérieur droit.

![Mode plein écran](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/fullscreen2.png){class="glboxshadow"}

### Mise à jour {#upgrade}

Cliquez sur la version du micrologiciel dans l’angle supérieur droit pour rechercher des mises à jour.

![Mise à niveau du micrologiciel](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade1.png){class="glboxshadow"}

Dans la fenêtre qui s’ouvre, vous pouvez effectuer une mise à niveau en ligne si une version plus récente du micrologiciel est disponible. Vous pouvez également télécharger le dernier micrologiciel depuis le [centre de téléchargement des micrologiciels](https://dl.gl-inet.com/kvm){target="_blank"}, puis effectuer une mise à niveau locale.

![Mise à niveau du micrologiciel](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/upgrade2.png){class="glboxshadow"}

### Service cloud {#cloud-service}

GL.iNet KVM Cloud vous permet d’accéder à l’appareil contrôlé à distance. Consultez [ce guide](../../faq/remote_access_via_cloud.md){target="_blank"} pour plus de détails.

Une fois votre Comet Q associé au cloud, la console affiche l’état du service cloud comme ci-dessous.

![Service Cloud](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/cloud.png){class="glboxshadow"}

### Sécurité {#security}

La section **Security** permet de modifier le mot de passe administrateur, d’activer l’authentification à deux facteurs et de personnaliser le certificat TLS.

![Paramètres de sécurité](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/security.png){class="glboxshadow"}

- Modifier le mot de passe administrateur

    ![Modification du mot de passe administrateur](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/admin-password.png){class="glboxshadow" width="434"}

- 2FA : activez l’authentification à deux facteurs pour protéger votre compte.

    ![Authentification à deux facteurs](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/2fa.png){class="glboxshadow"}

- Certificat TLS

    Le système utilise le certificat par défaut préinstallé pour l’accès par navigateur. Pour personnaliser le certificat TLS, cliquez sur **TLS Certificate** dans le coin supérieur droit de la console, sélectionnez **Custom Certificate**, puis téléversez votre **fichier de certificat et votre fichier de clé privée**.

    ![Certificat TLS personnalisé](https://static.gl-inet.com/docs/kvm/user_guide/gl-rmq1/console/tls-certificate.png){class="glboxshadow"}
