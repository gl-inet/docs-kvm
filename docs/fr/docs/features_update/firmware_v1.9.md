# Micrologiciel v1.9 {#firmware-v19}

Cette version apporte de nouvelles fonctionnalités, améliore les interactions, renforce la protection de la confidentialité et fiabilise les connexions réseau pour une expérience KVM à distance plus complète, stable et sécurisée.

Téléchargez le dernier micrologiciel depuis le [centre de téléchargement des micrologiciels](https://dl.gl-inet.com/kvm){target="_blank"}.

## Mode de latence {#latency-mode}

Ce micrologiciel introduit **Latency Mode**, qui permet d’adapter la réactivité des commandes et la fluidité vidéo. Choisissez Lowest Latency ou Smooth Display pour optimiser les performances du contrôle à distance.

![Mode de latence](https://static.gl-inet.com/docs/kvm/features_update/1.9/latency_mode.png){class="glboxshadow" width="360"}

- Lowest Latency : réduit au minimum la latence des entrées pour améliorer la réactivité du clavier et de la souris.
- Smooth Display : optimise l’affichage pour éliminer les saccades et les pertes d’images et assurer une lecture fluide.

## Utilisation de la souris {#mouse-usability}

La nouvelle option **Primary Button** améliore l’utilisation de la souris. Elle permet de choisir le bouton gauche ou droit comme bouton principal selon vos habitudes.

![Bouton principal](https://static.gl-inet.com/docs/kvm/features_update/1.9/primary_button.png){class="glboxshadow" width="360"}

## Affichage de l’écran {#screen-display}

Vous pouvez personnaliser les paramètres **Screen Display** du KVM depuis l’écran tactile : verrouillage de l’écran, fond d’écran, format de l’heure (24 heures / 12 heures) et format de la date. Cette fonction est réservée aux modèles équipés d’un écran tactile.

Vous pouvez également configurer rapidement des outils de réseau superposé, comme Tailscale et NetBird, directement depuis l’écran tactile en quelques pressions. Cette fonction n’était pas disponible dans les versions précédentes du micrologiciel.

![Affichage de l’écran](https://static.gl-inet.com/docs/kvm/features_update/1.9/screen_display.png){class="glboxshadow" width="360"}

## Langue {#language}

Les versions précédentes du micrologiciel prenaient uniquement en charge le chinois et l’anglais. Cette version ajoute la prise en charge native du **japonais** pour faciliter l’utilisation par les utilisateurs japonais.

![Langue](https://static.gl-inet.com/docs/kvm/features_update/1.9/language.png){class="glboxshadow" width="360"}

## Extensions {#extensions}

Cette version intègre [NetBird](https://netbird.io/){target="_blank"}, une plateforme réseau open source fondée sur le modèle Zero Trust pour créer des réseaux privés sécurisés à domicile ou en entreprise. Cette solution de réseau superposé basée sur WireGuard® permet d’accéder à votre KVM en toute sécurité depuis n’importe où via les réseaux virtuels NetBird. Consultez [ce guide](../faq/remote_access_via_netbird.md){target="_blank"} pour connaître la procédure de configuration.

![NetBird](https://static.gl-inet.com/docs/kvm/features_update/1.9/netbird.png){class="glboxshadow"}

## Autres améliorations {#other-enhancements}

- Programme de micrologiciels bêta : les utilisateurs peuvent rejoindre le programme bêta pour tester des fonctionnalités avant leur publication.

- Reconnaissance de texte : cet outil de reconnaissance optique de caractères (OCR) permet de récupérer le texte de toute zone sélectionnée sur l’écran distant. Il prend en charge le chinois, l’anglais et le mode bilingue chinois-anglais. Consultez [ce guide](../tutorials/how_to_capture_text_from_remote_screen.md) pour plus de détails.

- Fuseau horaire par ville : définissez votre fuseau horaire en sélectionnant une ville.

- Sécurité des sessions de connexion : les jetons de connexion expirent désormais 12 heures après la fin de la session ; ils étaient auparavant permanents.

- Sécurité des journaux système : les données sensibles sont désormais masquées dans tous les journaux système.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
