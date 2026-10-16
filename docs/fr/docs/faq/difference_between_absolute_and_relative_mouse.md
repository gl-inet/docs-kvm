# Différence entre souris absolue et souris relative {#what-is-the-difference-between-absolute-mouse-and-relative-mouse}

Dans la console des KVM GL.iNet, **Mouse Mode** propose deux options : **Absolute** et **Relative**. Elles diffèrent par le comportement du contrôle, les usages et l’expérience utilisateur. Les détails ci-dessous vous aideront à choisir le mode adapté à vos besoins.

![Mode de souris](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/mouse_mode.jpg){class="glboxshadow"}

## Souris absolue {#absolute-mouse}

Le mode absolu vise à synchroniser le contrôle de la souris entre l’ordinateur local et l’appareil cible. Les deux pointeurs utilisent le même système de coordonnées. Vous pouvez déplacer la souris locale de manière fluide entre la console du KVM et l’écran distant : le pointeur distant suit en temps réel les déplacements du pointeur local.

Un léger retard peut se produire en raison de la transmission réseau et de l’encodage vidéo. Le pointeur distant est alors légèrement en retard sur le pointeur local, sans nuire à la fluidité générale.

![Souris absolue](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/absolute.gif)

## Souris relative {#relative-mouse}

Le mode relatif ne synchronise pas les coordonnées des pointeurs local et distant : ils fonctionnent sur des plans distincts. Avant de contrôler l’appareil cible, vous devez cliquer dans la fenêtre distante pour capturer le pointeur.

Dans ce mode, le pointeur distant reste « confiné » à la fenêtre distante et ne peut pas passer librement sur le Bureau local. Les bords de la fenêtre limitent ses déplacements à l’environnement contrôlé. Pour libérer le pointeur et reprendre le contrôle de l’ordinateur local, appuyez sur `Esc`.

![Souris relative](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative.gif)

En mode relatif, vous pouvez régler **Relative Sensitivity** de 0.1 à 2.0.

![Sensibilité de la souris relative](https://static.gl-inet.com/docs/kvm/faq/difference_between_absolute_and_relative_mouse/relative_sensitivity.jpg){class="glboxshadow"}

## Principales différences {#key-differences}

| Caractéristique | Souris absolue | Souris relative |
| --- | --- | --- |
| Coordination des pointeurs | Pointeurs local et distant synchronisés (même système de coordonnées) | Pointeurs sur des plans distincts (sans synchronisation des coordonnées) |
| Contrôle | Aucun clic nécessaire pour capturer le pointeur ; déplacement fluide entre les écrans | Clic nécessaire dans l’écran distant ; passage entre les écrans non fluide |
| Retard | Léger retard (réseau et encodage vidéo) | Presque aucun retard (seuls les déplacements relatifs sont envoyés) |
| Usages | Contrôle fluide sur plusieurs écrans, changements fréquents, positionnement précis (télétravail, graphisme) | Appareils anciens / BIOS / UEFI sans prise en charge du mode absolu ; prévention des clics accidentels ; réseaux instables (latence réduite) |

## Récapitulatif {#summary}

Le mode absolu privilégie une expérience de contrôle fluide et intégrée, tandis que le mode relatif privilégie la compatibilité et la stabilité.

Pour la plupart des usages quotidiens du KVM GL.iNet à distance, le mode absolu est recommandé par défaut. Choisissez le mode relatif en cas de problème de compatibilité ou de besoin particulier.

- Utilisez **Absolute Mouse** pour un contrôle à distance fluide au quotidien.
- Utilisez **Relative Mouse** pour accéder au BIOS, contrôler des appareils anciens sans positionnement absolu ou éviter les clics accidentels.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
