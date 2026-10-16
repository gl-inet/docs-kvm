# Questions fréquentes sur les KVM GL.iNet {#quick-faqs-about-glinet-kvm}

Cette courte collection de questions et réponses fournit des réponses rapides aux questions de base sur les KVM GL.iNet.

## Informations générales {#basic-information}

**Q1. Quels appareils un KVM GL.iNet peut-il contrôler ?**

R1. Un KVM GL.iNet peut contrôler tout appareil disposant d’une sortie HDMI et d’une entrée USB : ordinateur portable ou de bureau, Raspberry Pi, mini-PC, etc.

Le Comet Q (GL-RMQ1) peut également contrôler tout appareil dont le port USB-C prend en charge le DisplayPort Alt Mode pour la sortie vidéo, sans port HDMI. Cela inclut certains iPhone, iPad, téléphones Android, MacBook et Mac mini, ainsi que la plupart des ordinateurs portables Windows récents. Cliquez [ici](../user_guide/gl-rmq1/product_overview.md#compatibility) pour en savoir plus.

---

**Q2. Dois-je installer un logiciel pour utiliser un KVM GL.iNet ?**

R2. Aucun logiciel n’est nécessaire sur l’appareil contrôlé, qui peut fonctionner sous Windows, macOS, ChromeOS, Linux, etc.

Sur l’appareil de contrôle, l’installation d’un logiciel dépend du mode d’accès au KVM.

??? "Contrôle à proximité (Comet 5G uniquement)"

    **Remarque :** Cette méthode est réservée au Comet 5G (GL-RM10RC).

    Le Comet 5G permet un contrôle à proximité par Wi-Fi pour une gestion locale rapide sans connexion filaire. Passez son réseau Wi-Fi en mode AP pour créer un SSID unique, puis connectez-vous à ce SSID pour accéder à sa console en toute sécurité. Cliquez [ici](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control) pour en savoir plus.

    Le mode AP déconnecte le Comet 5G de son Wi-Fi en amont et fournit uniquement un accès à proximité, sans connexion Internet.

??? "Contrôle local (Comet X uniquement)"

    **Remarque :** Cette méthode est réservée au Comet X (GL-RM4PE).

    Le Comet X dispose d’un port HDMI OUT et de deux ports USB supplémentaires pour le dépannage local, la configuration et l’installation d’un système d’exploitation. Branchez un écran, une souris et un clavier pour un contrôle local immédiat. Cliquez [ici](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control) pour en savoir plus.

??? "Accès par le réseau local"

    Aucun logiciel n’est nécessaire sur l’appareil de contrôle si vous accédez au KVM depuis le même réseau local (LAN).

    Ouvrez un navigateur sur l’appareil de contrôle et saisissez l’adresse IP du KVM ou `glkvm.local` dans la barre d’adresse.

    Cliquez [ici](local_access_via_browser.md){target="_blank"} pour en savoir plus.

??? "Accès à distance"

    - **Application GLKVM**

        Si l’appareil de contrôle fonctionne sous Windows, macOS, Android ou iOS, installez l’[application GLKVM](https://www.gl-inet.com/app-rm/){target="_blank"} pour accéder à distance au KVM et à l’appareil contrôlé.

        Cliquez [ici](remote_access_via_glkvm_app.md){target="_blank"} pour en savoir plus.

    - **Service cloud**

        Cette méthode convient aux personnes qui ne peuvent pas ou ne souhaitent pas installer GLKVM.

        Associez le KVM au service cloud, puis saisissez `glkvm.com` dans un navigateur sur l’appareil de contrôle pour accéder à distance au KVM et à l’appareil contrôlé, sans installer GLKVM.

        Cliquez [ici](remote_access_via_cloud.md){target="_blank"} pour en savoir plus.

    - **Tailscale**

        Cette méthode convient si vous ne pouvez pas ou ne souhaitez pas utiliser GLKVM ou le cloud, mais elle nécessite davantage d’étapes.

        Associez le KVM et l’appareil de contrôle au même compte Tailscale. Saisissez ensuite l’adresse IP virtuelle Tailscale du KVM dans un navigateur sur l’appareil de contrôle pour accéder à distance au KVM et à l’appareil contrôlé.

        Cliquez [ici](remote_access_via_tailscale.md){target="_blank"} pour en savoir plus.

    - **ZeroTier**

        Cette méthode convient si vous ne pouvez pas ou ne souhaitez pas utiliser GLKVM ou le cloud, mais elle nécessite davantage d’étapes.

        Connectez le KVM et l’appareil de contrôle au même réseau ZeroTier. Saisissez ensuite l’adresse IP ZeroTier du KVM dans un navigateur sur l’appareil de contrôle pour accéder à distance au KVM et à l’appareil contrôlé.

        Cliquez [ici](remote_access_via_zerotier.md){target="_blank"} pour en savoir plus.

    - **NetBird**

        Cette méthode convient si vous ne pouvez pas ou ne souhaitez pas utiliser GLKVM ou le cloud, mais elle nécessite davantage d’étapes.

        [NetBird](https://netbird.io/){target="_blank"} est une plateforme réseau open source fondée sur le principe Zero Trust, qui permet de créer des réseaux privés sécurisés à la maison comme en entreprise. Son réseau superposé basé sur WireGuard® permet un accès sécurisé à vos appareils à tout moment et de n’importe où.

        Les KVM GL.iNet intègrent NetBird pour rejoindre son réseau virtuel et permettre l’accès à distance.

        Cliquez [ici](remote_access_via_netbird.md){target="_blank"} pour en savoir plus.

---

**Q3. Comment accéder à un KVM GL.iNet ?**

R3. Plusieurs méthodes permettent d’accéder au KVM localement ou à distance :

- [Accès local par navigateur Web](local_access_via_browser.md){target="_blank"}
- [Accès à distance via le service cloud](remote_access_via_cloud.md){target="_blank"}
- [Accès à distance via GLKVM](remote_access_via_glkvm_app.md){target="_blank"}
- [Accès à distance via Tailscale](remote_access_via_tailscale.md){target="_blank"}
- [Accès à distance via ZeroTier](remote_access_via_zerotier.md){target="_blank"}
- [Accès à distance via NetBird](remote_access_via_netbird.md){target="_blank"}

Certains modèles permettent aussi le contrôle à proximité ou le contrôle local sur place, sans connexion à un autre routeur.

- [Contrôle à proximité (Comet 5G uniquement)](../user_guide/gl-rm10rc/quick_setup_guide.md#nearby-control){target="_blank"}
- [Contrôle local (Comet X uniquement)](../user_guide/gl-rm4pe/quick_setup_guide.md#local-control){target="_blank"}

---

**Q4. Dois-je ouvrir des ports sur le WAN pour accéder au KVM GL.iNet à distance ?**

R4. Non. Aucun port ouvert ni adresse IP publique n’est nécessaire.

---

**Q5. GLKVM est-il compatible avec ChromeOS et Linux ?**

R5. Non. L’application GLKVM ne peut actuellement pas être installée sous ChromeOS ou Linux.

Si l’appareil de contrôle fonctionne sous ChromeOS ou Linux, l’accès à distance via GLKVM n’est donc pas pris en charge.

Vous pouvez toutefois utiliser le <u>service cloud</u>, <u>Tailscale</u>, <u>ZeroTier</u> ou <u>NetBird</u>. Consultez la question Q3 ci-dessus.

Vous pouvez également accéder au KVM localement depuis un navigateur Web. Consultez la question Q3 ci-dessus.

---

**Q6. Le Comet (GL-RM1) peut-il se connecter à un réseau sans fil ?**

R6. Non. Le Comet (GL-RM1) ne prend pas en charge les connexions réseau sans fil.

Il doit être relié à un équipement réseau, comme un routeur, par un câble Ethernet pour accéder à Internet.

Si vous préférez un KVM avec Wi-Fi, les modèles suivants sont disponibles :

* [Comet Pro (GL-RM10)](https://www.gl-inet.com/products/gl-rm10/){target="_blank"}
* [Comet 5G (GL-RM10RC)](https://www.gl-inet.com/products/gl-rm10rc/){target="_blank"}
* [Comet Q (GL-RMQ1)](https://www.gl-inet.com/products/gl-rmq1/){target="_blank"}

---

## Contrôle de l’alimentation {#power-control}

**Q1. Un KVM GL.iNet peut-il allumer et éteindre l’appareil cible à distance ?**

R1. Un KVM GL.iNet permet de contrôler l’alimentation à distance avec les méthodes suivantes :

- Wake-on-LAN (service logiciel intégré)

- [Carte ATX](../user_guide/gl-atx-board/index.md){target="_blank"} (vendue séparément ; incompatible avec le Comet Q)

- [FingerBot](../user_guide/gl-fgb-01/index.md){target="_blank"} (vendu séparément ; incompatible avec le Comet Q)

---

**Q2. Comment utiliser la carte ATX pour contrôler l’alimentation à distance ?**

R2. Consultez le [guide d’utilisation de la carte ATX](../user_guide/gl-atx-board/index.md){target="_blank"}.

---

## Fonctionnalités {#features}

!!! tip "Conseil"

    Les questions ci-dessous portent sur quelques fonctions courantes. Consultez le [guide d’utilisation](../user_guide/index.md) correspondant pour une présentation complète.

**Q1. Dois-je utiliser le service KVM Cloud ?**

R1. Non. Le service cloud est facultatif.

Vous pouvez utiliser des outils tiers de réseau superposé comme Tailscale, ZeroTier ou NetBird pour l’accès à distance sans passer par le cloud.

---

**Q2. Puis-je contrôler plusieurs appareils avec un seul KVM GL.iNet ?**

R2. Les modèles suivants ne peuvent contrôler qu’un seul appareil cible :

* Comet (GL-RM1)
* Comet PoE (GL-RM1PE)
* Comet Pro (GL-RM10)
* Comet 5G (GL-RM10RC)
* Comet Q (GL-RMQ1)

Le Comet X (GL-RM4PE) peut toutefois être connecté à quatre appareils cibles simultanément, mais un seul peut être contrôlé à la fois. Vous pouvez passer rapidement de l’un à l’autre avec le bouton physique en façade sur place, ou depuis la console distante.

Le Comet X (GL-RM4PE) dispose de quatre canaux indépendants à l’arrière. Chacun comprend un port HDMI pour la vidéo, un port Type-C pour les signaux clavier et souris et un port USB 2.0 pour les périphériques USB, comme le Fingerbot ou la carte ATX.

---

**Q3. Qu’est-ce que Wake-on-LAN ?**

R3. Wake-on-LAN (WOL) permet d’allumer un ordinateur à distance ou de le sortir d’un état de faible consommation via le réseau. Un « paquet magique » contenant son adresse MAC déclenche son démarrage. Cette fonction est utilisée pour l’administration à distance, la mise en veille économe et la gestion centralisée des systèmes.

---

**Q4. Les KVM GL.iNet prennent-ils en charge Mouse Jiggle ?**

R4. Oui. Vous pouvez activer Mouse Jiggle dans la console du KVM.

La fonction Mouse Jiggler simule de petits mouvements périodiques de souris pour empêcher l’ordinateur contrôlé de se mettre en veille après une inactivité prolongée, par exemple pendant des réunions à distance ou la gestion de serveurs.

---

**Q5. Les KVM GL.iNet prennent-ils en charge l’audio bidirectionnel ?**

R5. Oui. Activez Speaker et Microphone dans la console du KVM pour transmettre l’audio dans les deux sens.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
