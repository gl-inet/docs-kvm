# Micrologiciel v1.10 {#firmware-v110}

Cette version introduit WebRTC natif, le suivi des données en temps réel, la gestion centralisée des périphériques USB et un nouveau centre de paramètres. Elle améliore également la rapidité de démarrage, la sécurité et la stabilité du microphone pour une expérience KVM à distance plus fluide et fiable.

Téléchargez le dernier micrologiciel depuis le [centre de téléchargement des micrologiciels](https://dl.gl-inet.com/kvm){target="_blank"}.

## Mode WebRTC (Native) {#webrtc-native-mode}
Ce micrologiciel introduit le mode **WebRTC (Native)**. Il utilise la bibliothèque Google WebRTC pour améliorer les performances de diffusion et la fluidité du contrôle à distance en temps réel.

![Mode WebRTC](https://static.gl-inet.com/docs/kvm/features_update/1.10/webrtc_native_mode.png){class="glboxshadow" width=400}

## Statistiques de connexion {#connection-stats}

**Connection Stats** affiche les informations de connexion en temps réel et des graphiques d’évolution : latence réseau, gigue, taux de perte de paquets, débit binaire, fréquence d’images et délai de lecture.

Cliquez sur l’icône de liste pour consulter les données de connexion en temps réel et l’état de l’appareil.

![Statistiques de connexion 1](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_1.png){class="glboxshadow"}

Cliquez sur l’icône de graphique pour afficher l’évolution de la latence réseau, de la gigue et du taux de perte de paquets.

![Statistiques de connexion 2](https://static.gl-inet.com/docs/kvm/features_update/1.10/data_dashboard_2.png){class="glboxshadow"}

## Centre de paramètres {#settings-center}

Cette version ajoute un nouveau **Settings Center**, qui centralise les paramètres des périphériques USB, les préférences et les paramètres réseau, de sécurité, cloud et système. Les options existantes, comme la configuration du nom d’hôte, la gestion du cloud et les mises à jour du micrologiciel, sont désormais regroupées et plus faciles d’accès.

### Périphériques USB {#usb-devices}

La section **USB Devices** centralise la gestion des périphériques USB émulés. Vous pouvez y activer ou désactiver des périphériques virtuels pour améliorer la compatibilité avec l’hôte contrôlé.

![Périphériques USB](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_usb_devices.png){class="glboxshadow"}

- **USB Emulated Devices** : activez ou désactivez les périphériques USB émulés, notamment la souris, le clavier, le microphone, la caméra et les supports virtuels. Certains périphériques ne peuvent pas être activés simultanément. Leur disponibilité est mise à jour automatiquement.

- **Device Identity** : personnalisez ou modifiez l’identité du KVM reconnue par l’appareil contrôlé. L’EDID et l’identification de l’appareil restent synchronisés : toute modification de l’un met automatiquement à jour l’autre pour garantir une reconnaissance correcte de l’appareil.

### Préférences {#preferences}

La section **Preferences** permet de gérer les préférences de disposition, les paramètres système et les réglages de l’écran de l’appareil.

![Préférences](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_preferences.png){class="glboxshadow"}

- **Layout Preferences** : configurez la barre d’outils en plein écran et la barre d’état en mode fenêtré.

- **System Settings** : définissez le titre de l’onglet du navigateur, la langue de l’interface, le mode de couleur et le fuseau horaire.

- **Device Screen** : prévisualisez et configurez l’écran intégré de l’appareil, notamment le mode de verrouillage, le format de l’heure, le format de la date et le fond d’écran.

    **Remarque** : cette fonction est disponible uniquement sur les modèles dotés d’un écran intégré.

### Réseau {#network}

Vous pouvez consulter et gérer les paramètres réseau de l’appareil, notamment son nom d’hôte, sa connexion Ethernet et les informations du réseau sans fil.

![Réseau](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_network.png){class="glboxshadow"}

- **Hostname** : modifiez le nom d’hôte de l’appareil directement dans la console. Cette fonction a été introduite dans le micrologiciel v1.7.0.

- **Ethernet Settings** : consultez et configurez la connexion Ethernet. Utilisez DHCP pour obtenir automatiquement les paramètres réseau ou sélectionnez **Static** pour saisir manuellement l’adresse IP, le masque de réseau, la passerelle et les autres paramètres requis.

- **Wireless** : l’adresse IP, la passerelle et l’adresse MAC s’affichent une fois l’appareil connecté à un réseau Wi-Fi.

    **Remarque** : la fonction Wireless est disponible uniquement sur les modèles compatibles.

### Sécurité {#security}

La section **Security** permet de modifier le mot de passe administrateur, d’activer l’authentification à deux facteurs et de personnaliser le certificat TLS.

![Sécurité](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_security.png){class="glboxshadow"}

- **Access Password** : gérez le mot de passe administrateur ou activez l’authentification à deux facteurs (2FA) pour sécuriser l’accès à l’appareil.

- **TLS Certificate** : utilisez le certificat par défaut ou téléversez un certificat personnalisé et une clé privée pour l’accès depuis un navigateur.

### Cloud {#cloud}

Les appareils peuvent être associés aux services cloud via une URL ou un code pour y accéder et les gérer à distance. Vous pouvez également télécharger l’application mobile, gérer la connexion ou supprimer l’association de l’appareil selon vos besoins.

![Cloud](https://static.gl-inet.com/docs/kvm/features_update/1.10/settings_cloud.png){class="glboxshadow"}

### Système {#system}

Dans **System**, vous pouvez accéder aux options de gestion du système, de mise à jour du micrologiciel et d’assistance.

![Système](https://static.gl-inet.com/docs/kvm/features_update/1.10/setting_system.png){class="glboxshadow"}

- **System** : redémarrez l’appareil ou rétablissez ses paramètres d’usine.

- **Upgrade** : activez Beta Center pour recevoir les versions bêta du micrologiciel ou utilisez **Local Upgrade** pour installer un micrologiciel à partir d’un fichier local.

- **Help & Support** : exportez les journaux de l’appareil pour le dépannage et accédez aux guides d’utilisation, aux FAQ et aux autres documents d’assistance.

## Autres améliorations {#other-enhancements}

- **Performances au démarrage** : démarrage plus rapide de l’appareil.

- **Politique de mot de passe** : politique renforcée pour améliorer la sécurité, avec un minimum de 10 caractères comprenant au moins deux types de caractères.

- **Indicateur de verrouillage des majuscules** : ajout d’un indicateur d’état de la touche Caps Lock de l’appareil contrôlé.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
