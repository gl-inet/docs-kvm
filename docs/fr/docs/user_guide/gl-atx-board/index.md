# Guide d’utilisation de la carte ATX (GL-ATXPC) {#atx-board-gl-atxpc-user-guide}

La carte ATX est un accessoire optionnel pour les appareils KVM GL.iNet. Ce module de gestion intelligente de l’alimentation permet de contrôler à distance l’alimentation de l’appareil contrôlé en simulant des appuis sur son bouton physique (allumage, arrêt et redémarrage).

La carte ATX s’installe dans le boîtier de l’appareil contrôlé pour une gestion de l’alimentation plus discrète et plus stable.

**Remarque** : le Comet Q (GL-RMQ1) n’est pas compatible avec la carte ATX.

![Comet et carte ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/rm1-and-atx-borad.jpg){class="glboxshadow"}

## Contenu de l’emballage {#package-contents}

![Contenu de l’emballage](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/inside-the-box.png){class="glboxshadow gl-80-desktop"}

- 1 x carte principale ATX
- 1 x jeu de câbles à 9 broches
- 1 x sachet de vis
- 1 x câble USB-A vers Type-C
- 1 x ensemble de supports ATX

## Brochage {#pin-out}

![Brochage](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/pinout.jpg){class="glboxshadow gl-80-desktop"}

Description des connecteurs et des boutons :

1. Connecteur Type-C : à raccorder à l’appareil KVM.
2. Bouton de mise à niveau du micrologiciel du microcontrôleur de la carte principale ATX.
3. Bouton de réinitialisation.
4. Connecteur pour les câbles de commande de la façade de l’ordinateur.
5. Connecteur pour l’embase F_PANEL de l’ordinateur.

!!! note

    1. Les connecteurs 4 et 5 sont interchangeables. Vous pouvez donc raccorder le connecteur 5 aux câbles de commande de la façade de l’ordinateur et le connecteur 4 à l’embase F_PANEL.

    2. La carte ATX comporte deux voyants qui suivent tous deux le comportement du voyant d’alimentation (le bleu indique le système ATX ; le vert indique l’alimentation du PC). La carte ATX ne dispose d’aucun voyant HDD. L’état des voyants de la carte correspond à celui du voyant d’alimentation de la façade de l’ordinateur.

Schéma des connecteurs 4/5 :

![Connecteur](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface.png){class="glboxshadow gl-60-desktop"}

## Installation {#installation}

Regardez cette vidéo pour installer la carte ATX, ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3VEjZgzgI44" title="Lecteur vidéo YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Visser la carte ATX et son support {#1-screw-atx-board-and-bracket}

Fixez la carte ATX et son support avec les vis fournies.

![Vissage](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/screwing.jpg){class="glboxshadow gl-90-desktop"}

### 2. Installer la carte ATX dans le boîtier du PC {#2-install-atx-board-into-pc-case}

Raccordez les connecteurs 4 et 5 respectivement aux câbles de commande du PC contrôlé et à son embase F_PANEL.

![Raccordement des connecteurs](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/interface_connect.jpg){class="glboxshadow gl-90-desktop"}

Le jeu de câbles à 9 broches fourni avec la carte ATX permet de raccorder l’un des connecteurs 4/5 de la carte aux câbles de commande ou à l’embase F_PANEL de l’ordinateur contrôlé.

Utilisez les câbles fournis avec le boîtier de l’ordinateur pour raccorder l’autre connecteur 4/5 aux câbles de commande ou à l’embase F_PANEL de l’ordinateur contrôlé.

**Remarque** : la polarité des connecteurs peut varier selon le boîtier du PC. Vérifiez-la attentivement avant l’installation.

Voici quelques exemples de raccordement d’un connecteur 4/5 à l’embase F_PANEL de l’ordinateur contrôlé.

??? "Pour une embase PANEL à 10-1 broches"

    Cet exemple concerne les cartes mères dont l’embase de raccordement à la façade comporte 10-1 broches, comme illustré ci-dessous.

    ![Embase à 10-1 broches 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_1.png){class="glboxshadow"}

    Suivez le schéma ci-dessous pour le raccordement. Veillez à ce que les inscriptions sérigraphiées (HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) soient orientées vers l’extérieur et visibles, plutôt que masquées vers l’intérieur.

    ![Embase à 10-1 broches 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_2.jpg){class="glboxshadow"}
    <small>Vue de face</small>

    ![Embase à 10-1 broches 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/10-1pin_panel_3.jpg){class="glboxshadow"}
    <small>Vue arrière</small>

    Utilisez ensuite les câbles fournis avec le boîtier de l’ordinateur pour raccorder l’autre connecteur de la carte ATX aux câbles de commande de l’ordinateur.

??? "Pour une embase PANEL à 20-5 broches"

    Cet exemple concerne les cartes mères dont l’embase de raccordement à la façade comporte 20-5 broches, comme illustré ci-dessous.

    ![Embase à 20-5 broches 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_1.jpg){class="glboxshadow"}

    Suivez le schéma ci-dessous pour le raccordement. Veillez à ce que les inscriptions sérigraphiées (HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) soient orientées vers l’extérieur et visibles, plutôt que masquées vers l’intérieur.

    ![Embase à 20-5 broches 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_2.jpg){class="glboxshadow"}
    <small>Vue de face</small>

    ![Embase à 20-5 broches 3](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-5pin_panel_3.png){class="glboxshadow"}
    <small>Vue arrière</small>

    Utilisez ensuite les câbles fournis avec le boîtier de l’ordinateur pour raccorder l’autre connecteur de la carte ATX aux câbles de commande de l’ordinateur.

??? "Pour une embase PANEL à 20-8 broches"

    Cet exemple concerne les cartes mères dont l’embase de raccordement à la façade comporte 20-8 broches, comme illustré ci-dessous.

    ![Embase à 20-8 broches 1](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_1.jpg){class="glboxshadow"}

    Suivez le schéma ci-dessous pour le raccordement. Veillez à ce que les inscriptions sérigraphiées (HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) soient orientées vers l’extérieur et visibles, plutôt que masquées vers l’intérieur.

    ![Embase à 20-8 broches 2](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/20-8pin_panel_2.png){class="glboxshadow"}

    Utilisez ensuite les câbles fournis avec le boîtier de l’ordinateur pour raccorder l’autre connecteur de la carte ATX aux câbles de commande de l’ordinateur.

La carte ATX entièrement raccordée est illustrée ci-dessous.

![Carte ATX raccordée](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected1.png){class="glboxshadow gl-90-desktop"}

![Carte ATX raccordée](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/connected2.png){class="glboxshadow gl-90-desktop"}

Installez ensuite le support de la carte ATX dans le boîtier de l’ordinateur.

![Installation de la carte ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install1.png){class="glboxshadow gl-90-desktop"}

![Installation de la carte ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install2.png){class="glboxshadow gl-90-desktop"}

### 3. Raccorder la carte ATX au KVM {#3-connect-atx-board-and-kvm}

Raccordez le port Type-C de la carte ATX au port USB-A de l’appareil KVM (par exemple, Comet GL-RM1) à l’aide du câble USB fourni.

![Installation de la carte ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install3.png){class="glboxshadow gl-90-desktop"}

![Installation de la carte ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install4.png){class="glboxshadow gl-90-desktop"}

L’installation de la carte ATX est terminée.

![Installation de la carte ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/install5.png){class="glboxshadow gl-90-desktop"}

Connectez-vous maintenant à votre KVM, puis accédez à **Accessories** pour contrôler l’alimentation ATX.

![Alimentation ATX](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/atx_power.png){class="glboxshadow gl-90-desktop"}

## FAQ {#faq}

**Q1. Puis-je utiliser la carte GL-ATXPC avec des appareils KVM d’autres marques que GL.iNet ?**

R1. Non. La carte GL-ATXPC est un accessoire pour les appareils KVM GL.iNet. Elle doit être utilisée avec un KVM GL.iNet.

---

**Q2. Après l’installation de la carte ATX, que faire si je ne peux pas allumer ou éteindre l’appareil distant depuis le KVM ?**

R2. Essayez les solutions suivantes.

- Vérifiez que l’appareil contrôlé s’allume et s’éteint normalement lorsque vous appuyez sur le bouton physique de la façade du boîtier.

- Vérifiez la polarité des câbles. Essayez d’inverser le connecteur POWER SW sur la carte mère de l’appareil contrôlé pour corriger un éventuel mauvais raccordement.

    ![Polarité du connecteur](https://static.gl-inet.com/docs/kvm/user_guide/gl-atx-board/power-sw-connector.png){class="glboxshadow gl-90-desktop"}

- Lors du raccordement à l’embase F_PANEL de la carte mère, veillez à ce que les inscriptions sérigraphiées (HDDLED±, RESET SW, POWER SW, POWERLED+, etc.) soient orientées vers l’extérieur et visibles, plutôt que masquées vers l’intérieur.

- Mettez à niveau le micrologiciel du KVM.

---

**Q3. Puis-je utiliser un seul KVM GL.iNet pour contrôler plusieurs cartes ATX ?**

R3. Les KVM GL.iNet suivants ne peuvent contrôler qu’une seule carte ATX.

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)

Le Comet X (GL-RM4PE) prend toutefois en charge jusqu’à quatre cartes ATX simultanément. Son panneau arrière dispose de quatre canaux indépendants. Chaque canal comprend un port HDMI pour le signal vidéo, un port Type-C pour les signaux du clavier et de la souris, ainsi qu’un port USB 2.0 pour les périphériques USB (par exemple, un Fingerbot ou une carte ATX).

**Remarque** : le Comet Q (GL-RMQ1) n’est pas compatible avec la carte ATX.

---

Vous avez d’autres questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
